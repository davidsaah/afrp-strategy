##############################################################################
# AFRP platform — GCP infrastructure
#
# Deliberately boring. Every resource here has a direct equivalent on AWS and
# Azure, and nothing uses a GCP-only data model. See deploy/PORTABILITY.md.
#
#   terraform init
#   terraform plan  -var project_id=afrp-prod -var env=prod
#   terraform apply -var project_id=afrp-prod -var env=prod
##############################################################################

terraform {
  required_version = ">= 1.7"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}

variable "project_id" { type = string }
variable "region"     { type = string  default = "us-central1" }
variable "env"        { type = string  default = "staging" }
variable "image"      { type = string  default = "us-central1-docker.pkg.dev/PROJECT/afrp/api:latest" }

# Production gets HA and a real machine; staging gets the cheapest thing that
# runs, because a staging bill nobody expected is how staging gets deleted.
locals {
  is_prod         = var.env == "prod"
  db_tier         = local.is_prod ? "db-custom-2-7680" : "db-f1-micro"
  db_availability = local.is_prod ? "REGIONAL" : "ZONAL"
  min_instances   = local.is_prod ? 1 : 0
  max_instances   = local.is_prod ? 10 : 2
  name            = "afrp-${var.env}"
}

provider "google" {
  project = var.project_id
  region  = var.region
}

##############################################################################
# Networking — Cloud SQL is NOT exposed to the internet.
##############################################################################

resource "google_compute_network" "vpc" {
  name                    = "${local.name}-vpc"
  auto_create_subnetworks = true
}

resource "google_compute_global_address" "private_ip" {
  name          = "${local.name}-private-ip"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = google_compute_network.vpc.id
}

resource "google_service_networking_connection" "private_vpc" {
  network                 = google_compute_network.vpc.id
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.private_ip.name]
}

##############################################################################
# Database — plain PostgreSQL 16. No Cloud SQL-only features.
##############################################################################

resource "google_sql_database_instance" "pg" {
  name             = "${local.name}-pg"
  database_version = "POSTGRES_16"
  region           = var.region
  # Staging is disposable; production must not be deletable by accident.
  deletion_protection = local.is_prod

  depends_on = [google_service_networking_connection.private_vpc]

  settings {
    tier              = local.db_tier
    availability_type = local.db_availability
    disk_type         = "PD_SSD"
    disk_size         = 20
    disk_autoresize   = true

    ip_configuration {
      ipv4_enabled    = false
      private_network = google_compute_network.vpc.id
      ssl_mode        = "ENCRYPTED_ONLY"
    }

    backup_configuration {
      enabled                        = true
      start_time                     = "09:00" # UTC — overnight in the US
      point_in_time_recovery_enabled = local.is_prod
      transaction_log_retention_days = local.is_prod ? 7 : 1
      backup_retention_settings {
        retained_backups = local.is_prod ? 30 : 7
      }
    }

    maintenance_window {
      day  = 2 # Tuesday
      hour = 10
    }

    database_flags {
      name  = "cloudsql.iam_authentication"
      value = "on"
    }
  }
}

resource "google_sql_database" "afrp" {
  name     = "afrp"
  instance = google_sql_database_instance.pg.name
}

resource "google_sql_user" "app" {
  name     = "afrp_app"
  instance = google_sql_database_instance.pg.name
  password = google_secret_manager_secret_version.db_password.secret_data
}

##############################################################################
# Secrets — Breeze keys (one per club), Authorize.Net, Mailchimp.
# Values are set out of band; Terraform creates the containers only.
##############################################################################

resource "google_secret_manager_secret" "db_password" {
  secret_id = "${local.name}-db-password"
  replication { auto {} }
}

resource "google_secret_manager_secret_version" "db_password" {
  secret      = google_secret_manager_secret.db_password.id
  secret_data = random_password.db.result
}

resource "random_password" "db" {
  length  = 32
  special = true
}

resource "google_secret_manager_secret" "authorize_net" {
  secret_id = "${local.name}-authorize-net"
  replication { auto {} }
}

##############################################################################
# Storage — magazine archive, annual reports, and the nightly GEDCOM export
# of the family tree. Versioning is on because that tree is irreplaceable.
##############################################################################

resource "google_storage_bucket" "assets" {
  name                        = "${var.project_id}-${var.env}-assets"
  location                    = "US"
  uniform_bucket_level_access = true
  force_destroy               = !local.is_prod

  versioning { enabled = true }

  lifecycle_rule {
    condition { age = 90 num_newer_versions = 5 }
    action    { type = "Delete" }
  }
}

##############################################################################
# Runtime — Cloud Run running a plain OCI container on $PORT.
##############################################################################

resource "google_service_account" "api" {
  account_id   = "${local.name}-api"
  display_name = "AFRP API (${var.env})"
}

resource "google_secret_manager_secret_iam_member" "api_db_password" {
  secret_id = google_secret_manager_secret.db_password.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.api.email}"
}

resource "google_project_iam_member" "api_sql_client" {
  project = var.project_id
  role    = "roles/cloudsql.client"
  member  = "serviceAccount:${google_service_account.api.email}"
}

resource "google_storage_bucket_iam_member" "api_objects" {
  bucket = google_storage_bucket.assets.name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:${google_service_account.api.email}"
}

resource "google_cloud_run_v2_service" "api" {
  name     = "${local.name}-api"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    service_account = google_service_account.api.email

    scaling {
      min_instance_count = local.min_instances
      max_instance_count = local.max_instances
    }

    vpc_access {
      network_interfaces { network = google_compute_network.vpc.id }
      egress = "PRIVATE_RANGES_ONLY"
    }

    containers {
      image = var.image

      # Cloud Run injects PORT. The app reads it like any other platform would.
      env {
        name  = "NODE_ENV"
        value = "production"
      }
      env {
        name  = "DATABASE_URL"
        value = "postgres://afrp_app@${google_sql_database_instance.pg.private_ip_address}:5432/afrp?sslmode=require"
      }
      env {
        name  = "OBJECT_BUCKET"
        value = google_storage_bucket.assets.name
      }
      env {
        name = "DB_PASSWORD"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.db_password.secret_id
            version = "latest"
          }
        }
      }

      resources {
        limits = {
          cpu    = local.is_prod ? "2" : "1"
          memory = local.is_prod ? "1Gi" : "512Mi"
        }
      }

      startup_probe {
        http_get { path = "/health" }
        initial_delay_seconds = 5
        period_seconds        = 5
        failure_threshold     = 6
      }

      liveness_probe {
        http_get { path = "/health" }
        period_seconds = 30
      }
    }
  }

  traffic {
    type    = "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"
    percent = 100
  }
}

output "api_url"     { value = google_cloud_run_v2_service.api.uri }
output "db_host"     { value = google_sql_database_instance.pg.private_ip_address  sensitive = true }
output "bucket_name" { value = google_storage_bucket.assets.name }
