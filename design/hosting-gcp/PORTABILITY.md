# Running on GCP without marrying it

The target is Google Cloud. The constraint is that leaving must stay cheap.
Those are compatible, but only if the choice is made deliberately at each
layer — "cloud-agnostic" is not a property you get by intending it.

## The rule

**Every managed service we depend on must have a portable interface in front
of it, or be a service whose interface is an open standard.**

Two ways to satisfy that:

1. **Open protocol.** Postgres is Postgres whether it runs on Cloud SQL, RDS,
   Azure Database, or a laptop. No abstraction needed — the wire protocol *is*
   the abstraction.
2. **Thin adapter.** Where the API is proprietary (secrets, object storage,
   push), we define our own interface and write one small adapter per cloud.
   The application only ever sees our interface.

Anything that satisfies neither is a lock-in decision and needs an explicit
argument, not a default.

## Layer by layer

| Layer | On GCP | Portable? | Escape route |
|---|---|---|---|
| Compute | **Cloud Run** | ✅ Yes | It runs an OCI container listening on `$PORT`. Identical image runs on ECS/Fargate, Azure Container Apps, Fly.io, Knative, plain Kubernetes |
| Database | **Cloud SQL for PostgreSQL 16** | ✅ Yes | Standard Postgres wire protocol. `pg_dump`/restore to RDS, Azure, Neon, Supabase, or self-hosted. No Cloud SQL-only features used |
| Job queue | **pg-boss (inside Postgres)** | ✅ Yes | Deliberately **not** Pub/Sub or Cloud Tasks. Job volume here is trivial; keeping the queue in the database we already run removes a proprietary dependency *and* an operational component |
| Object storage | **Cloud Storage** | ⚠️ Adapter | GCS supports the S3 interoperability API. Access via an S3-compatible client behind `ObjectStore` — same code hits S3, R2, or MinIO |
| Secrets | **Secret Manager** | ⚠️ Adapter | Behind a `SecretStore` interface. Adapters for GCP Secret Manager, AWS Secrets Manager, Azure Key Vault, Vault, and env vars for local dev |
| Identity | **Microsoft Entra External ID** | ✅ Yes | Intentionally NOT GCP Identity Platform. Entra is SaaS and cloud-neutral, AFRP already owns it, and Power Pages already federates to it. Standard OIDC either way |
| Email | **SMTP or a provider SDK** | ✅ Yes | SMTP is portable by definition |
| SMS | **Provider behind `SmsSender`** | ⚠️ Adapter | Twilio/MessageBird/SNS are all one small adapter |
| CDN / TLS | **Cloud Load Balancing** | ✅ Yes | Cloudflare in front makes this swappable in an afternoon |
| CI/CD | **GitHub Actions → Artifact Registry** | ✅ Yes | Builds a container and pushes it. Registry target is one line of config |
| Observability | **OpenTelemetry → Cloud Trace** | ✅ Yes | OTel is vendor-neutral. Point the exporter elsewhere and nothing else changes |
| IaC | **Terraform** | ✅ Yes | Not Deployment Manager, not gcloud scripts. Provider-specific modules, portable tooling and workflow |

## What we deliberately do NOT use

These are good products. Each one would also be a one-way door.

- **Firestore / Datastore / Bigtable** — the family tree needs recursive CTEs
  and the member model needs real joins. Postgres is the right store on merit,
  and it happens to also be the portable one.
- **Pub/Sub, Cloud Tasks, Cloud Scheduler** — pg-boss covers queueing and cron
  at this scale. One fewer proprietary surface, one fewer thing to operate.
- **Firebase Auth / Identity Platform** — Entra is already in the estate.
- **Cloud Functions** — splitting the API across a proprietary function runtime
  buys nothing here and costs portability.
- **BigQuery** — if analytics outgrows Postgres, revisit. It has not.
- **Memorystore / Redis** — no cache tier is needed yet. Adding one is a
  performance decision, not an architectural one.

## Cost sketch

Cloud Run scales to zero, so non-production environments cost close to nothing.

| | Staging | Production |
|---|---|---|
| Cloud Run | ~$0 (scales to zero) | $25–60/mo |
| Cloud SQL | db-f1-micro, ~$10/mo | db-custom-2-7680 + HA, $150–250/mo |
| Cloud Storage | <$5/mo | $10–30/mo |
| Load balancer | shared | ~$20/mo |
| Secret Manager, Artifact Registry, egress | <$5/mo | $15–40/mo |
| **Total** | **~$20/mo** | **$220–400/mo** |

Roughly comparable on AWS or Azure. Nothing here is priced so far below
alternatives that it would justify locking in.

## Proving portability instead of assuming it

Intent decays. Make it mechanical:

1. **Local dev runs zero GCP services.** `docker compose up` gives Postgres and
   MinIO. If a change breaks local dev, it has introduced a hard dependency —
   the compose file is the canary.
2. **Adapter interfaces live in `src/platform/`**, and the concrete adapters in
   `src/platform/gcp/`. A lint rule forbids importing `@google-cloud/*` outside
   that directory. This is the rule that actually holds the line; the rest is
   good intentions.
3. **CI runs the whole suite against plain Postgres and MinIO**, never against
   GCP. If tests need real GCP, coupling has crept in.
4. **Re-read this file at each phase boundary.** Every long-lived system that
   ended up locked in also started out intending not to be.

## Honest caveat

Portability is not free, and this document should not pretend otherwise. The
adapters are real code to write and maintain, and choosing pg-boss over Pub/Sub
trades some operational polish for independence. That trade is right for AFRP
specifically — a volunteer-led federation that may change hands, budget, or
hosting partner more than once over this system's life. It would be the wrong
trade for a team that is certain it will stay put.
