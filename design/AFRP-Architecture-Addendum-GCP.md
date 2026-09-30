# AFRP Enterprise Platform — Addendum 1
### Corrections, household model, and GCP deployment

**Date:** August 15, 2026
**Supersedes parts of:** *AFRP Enterprise Platform — Architecture, build-vs-extend analysis, and delivery plan*
**Trigger:** portal screenshots and a directive to target GCP while remaining cloud-agnostic

---

## 1. Corrections

Two errors in the previous document, both material.

### 1.1 Payments are Authorize.Net, not Square

I reported Square based on 14 occurrences of the string "square" in the
donations page HTML. Every occurrence was the Astra WordPress theme's CSS class
`.square .posted-on`. It was a false positive from a careless grep, and I did
not check the match context before asserting it.

The actual stack:

| | Previously stated | Correct |
|---|---|---|
| Processor | Square | **Authorize.Net** |
| Stored cards | not modelled | **CIM** — Customer Information Manager |
| Recurring | "auto-renew" hand-waved | **ARB** — Automated Recurring Billing |
| Member-visible | — | Manage Payment Methods, My Subscriptions |

**What changed downstream:** `gift_source` and `link_system` enums, the seed
data, the connector (`src/integrations/payments/authorize-net.ts`), 12 new
tests, and the PCI discussion in §4.

### 1.2 The portal is more complete than I claimed

I reported events, club details, and transaction history as missing, based on
unauthenticated URL probes returning 404. Those probes were unreliable — the
pages exist behind login at slugs I did not guess. **I should not have treated
a guessed-URL 404 as evidence of absence.**

The app's tile grid is authoritative:

> Donations · Transaction History · Manage My Household · Become a Member ·
> Event Registration · Local Club Details · Hathihe Ramallah Magazine ·
> Hathihe Ramallah Online · Publications · AFRP Digital Store ·
> My Subscriptions · My Payment Methods

**This is good news and it changes the plan.** AFRP is not missing modules. It
has a capable portal delivering a poor mobile experience on top of a household
model that fights how families actually work. Both are cheaper to fix than
anything I previously proposed.

### 1.3 Revised recommendation

The previous document recommended custom services alongside Dynamics (option
B), and that still holds for the family tree, Breeze, and mobile. But it should
now be preceded by a **Phase −1** that was not in the plan:

> **Fix the existing portal first. Roughly three weeks of layout, consent, and
> form work delivers more member-visible value than the first three months of
> the custom build.**

Details in the companion *Portal Mobile UX Review*. The headline: form fields
overflow the viewport so members cannot read their own address; the tile grid
is clipped; headers collide with the iOS status bar; SMS is promoted without
capturing consent; and "Fax" is offered as a contact preference while SMS is not.

---

## 2. Households — the structural finding

The portal states:

> "Only couples and their children under the age of 18 should be added to the
> household. All young adults (18+) must be in their own household, even if
> they still live in the same physical home."

That sentence collapses three independent facts into one field:

| Question | Fact type | Should live in |
|---|---|---|
| Who lives together? | address | `household` |
| Who may register / pay / consent for whom? | **authority** | `household_member.can_transact_for` |
| Who does a family tier cover? | **benefit** | `membership_coverage` |

**Consequence today:** a member is silently ejected from their family on their
eighteenth birthday, and a parent loses the ability to register them — while
everyone still lives in the same house and still considers themselves one
family. In this community parents routinely register adult children for
convention. The system forbids it.

### 2.1 The model

```
household ──< household_member >── person
                 role                 (head|spouse|child|dependent|other)
                 can_transact_for      explicit, revocable, auditable
                 left_at               history preserved, not deleted

membership ──< membership_coverage >── person
                 who a family tier actually covers, independent of household
```

Rules implemented in `src/households/rules.ts`, 14 passing tests:

- **Age sets the default, never the rule.** Adding a 12-year-old grants a
  parent authority automatically. Adding a 20-year-old does not — but the adult
  can grant it, which is the case the live portal cannot express at all.
- **Turning 18 prompts a consent refresh, not an ejection.** The now-adult is
  asked to confirm or revoke delegation. They stay in their family either way.
- **An adult in a household is not an error.** It is not even a warning. It is
  normal, and there is a test asserting exactly that.
- **A minor with no authorised guardian *is* an error** — a check the current
  portal does not make, and the one that actually protects members.
- **Unknown birth date is treated as adult.** Assuming minority would hand a
  stranger's record to whoever added them.

Live output from the seeded household (22, 20, and 15-year-old children in one
household, which the portal forbids):

```
Khoury Household
  Marwan Khoury    head    age 52  minor=False  delegates=True   mayActFor=3
  Nadia Khoury     spouse  age 55  minor=False  delegates=True   mayActFor=3
  Tarek Khoury     child   age 21  minor=False  delegates=True   mayActFor=0
  Basim Khoury     child   age 20  minor=False  delegates=False  mayActFor=0
  Layla Khoury     child   age 14  minor=True   delegates=True   mayActFor=0
issues: [('warning', 'reached_majority_confirm_delegation')]
```

Marwan may act for Nadia, Tarek, and Layla — but not Basim, who has not
delegated. No errors; one warning asking a newly-adult member to confirm.

---

## 3. Payments — Authorize.Net

### 3.1 PCI posture — the part that matters

The service **never sees a card number**. The browser posts card data directly
to Authorize.Net via Accept.js, which returns an opaque `dataDescriptor` /
`dataValue` pair. Only that token reaches the API, and it is exchanged for a
payment profile id. Stored: profile id, brand, last4, expiry. Nothing else.

This keeps AFRP in **SAQ A-EP** rather than SAQ D. There is a test asserting no
PAN, CVV, or card code appears in any outbound request body.

> If anyone proposes accepting a card number into the API "just for one flow",
> that changes AFRP's compliance obligations. It belongs in front of the board,
> not in a pull request.

### 3.2 Gateway quirks the connector handles

| Behaviour | Handling |
|---|---|
| JSON responses prefixed with a UTF-8 BOM | Stripped before parse — breaks naive `JSON.parse`, undocumented in the quickstart |
| `resultCode: "Error"` inside HTTP 200 | Treated as an error; status alone is never trusted |
| `E00001` generic transient fault | Marked retryable; all other gateway errors are not |
| Declines arrive as HTTP 200 + `resultCode: Ok` | Approval decided by `transactionResponse.responseCode === '1'` |
| `merchantCustomerId` capped at 20 chars | UUID hyphens stripped, then truncated |

### 3.3 Expiring cards

An expired card silently kills auto-renew. The member is never told; they
simply stop being a member. `GET /v1/admin/expiring-cards` surfaces cards
expiring within 60 days that back an active subscription. Cards are treated as
valid through the **end** of their expiry month, which is a real off-by-one-month
trap.

### 3.4 Worth revisiting separately

The connector sits behind a `PaymentGateway` interface so the processor can be
swapped without touching business logic. Authorize.Net's pricing is not
obviously the best available to a nonprofit — worth a look, but as its own
decision, not bundled into this build.

---

## 4. GCP, without marrying it

Target is GCP; leaving must stay cheap. Those are compatible only if the choice
is made deliberately at each layer. **"Cloud-agnostic" is not something you get
by intending it.**

### 4.1 The rule

Every managed dependency must either speak an **open protocol** or sit behind a
**thin adapter we own**. Anything else is a lock-in decision needing an explicit
argument.

| Layer | On GCP | Portable? | Escape route |
|---|---|---|---|
| Compute | Cloud Run | ✅ | OCI container on `$PORT`. Same image runs on Fargate, Container Apps, Fly.io, Knative |
| Database | Cloud SQL Postgres 16 | ✅ | Standard wire protocol. `pg_dump` to RDS, Azure, Neon, self-hosted |
| Queue | **pg-boss, inside Postgres** | ✅ | Deliberately not Pub/Sub or Cloud Tasks — removes a proprietary surface *and* a component to operate |
| Object storage | Cloud Storage | ⚠️ adapter | S3 interoperability API behind `ObjectStore` |
| Secrets | Secret Manager | ⚠️ adapter | Behind `SecretStore`; adapters for AWS/Azure/Vault/env |
| Identity | **Entra External ID** | ✅ | Intentionally not GCP Identity Platform. AFRP already owns Entra; Power Pages already federates to it |
| SMS | provider behind `SmsSender` | ⚠️ adapter | Twilio / MessageBird / SNS are one adapter each |
| Observability | OpenTelemetry → Cloud Trace | ✅ | Vendor-neutral; repoint the exporter |
| IaC | Terraform | ✅ | Not Deployment Manager, not gcloud scripts |

**Deliberately not used:** Firestore (the tree needs recursive CTEs and the
member model needs joins), Pub/Sub, Cloud Tasks, Cloud Scheduler, Firebase
Auth, Cloud Functions, BigQuery, Memorystore.

### 4.2 Enforcement, not intention

Portability decays unless something mechanical prevents it:

1. **`npm run lint:portability`** fails the build if `@google-cloud/*`,
   `@aws-sdk/*`, `@azure/*`, or `firebase-admin` is imported outside
   `src/platform/`. Currently: *12 source files checked, 0 violations*.
2. **Local dev runs zero cloud services.** `docker compose up` gives Postgres
   and MinIO. If a change breaks local dev, a hard dependency has crept in.
3. **CI runs the suite against plain Postgres**, never against GCP.
4. **Re-read `deploy/PORTABILITY.md` at every phase boundary.**

Item 1 is the one that actually holds the line. The rest is good intentions.

### 4.3 Cost

| | Staging | Production |
|---|---|---|
| Cloud Run | ~$0 (scales to zero) | $25–60/mo |
| Cloud SQL | ~$10/mo | $150–250/mo (HA) |
| Storage, LB, secrets, egress | <$10/mo | $45–90/mo |
| **Total** | **~$20/mo** | **$220–400/mo** |

Comparable on AWS or Azure. Nothing is priced far enough below alternatives to
justify locking in.

### 4.4 Honest caveat

Portability is not free. The adapters are real code to maintain, and choosing
pg-boss over Pub/Sub trades operational polish for independence. That trade is
right for AFRP — a volunteer-led federation that may change hands, budget, or
hosting partner more than once over this system's life. It would be the wrong
trade for a team certain it will stay put.

---

## 5. Revised roadmap

**Phase −1 is new and should be funded first.**

| Phase | Work | Weeks |
|---|---|---|
| **−1** | **Fix the existing portal: mobile overflow, safe areas, SMS consent, remove Fax, expiring-card alerts** | **3–4** |
| 0 | Foundation: Dynamics audit, Entra SSO, schema, CI/CD | 4–5 |
| 1 | Authorize.Net reconciliation, Mailchimp sync, giving history, receipts | 5–6 |
| 1b | **Household redesign: authority separated from membership** | 3–4 |
| 2 | Breeze connector, 26-club onboarding, identity resolution | 6–8 |
| 3 | Events and React Native app | 7–9 |
| 4 | Family tree | 10–14 |
| 5 | Programs and archive | 5–6 |

Roughly **12–13 months** for 2–4 developers, and Phase −1 delivers something
members notice in the first month.

If only one thing gets funded: **Phase −1.** It is three weeks, needs no new
platform, no migration, and no vendor change, and it fixes defects that
currently prevent members from reading their own address on a phone.

---

## 6. What is in the code now

| Added | File | Tests |
|---|---|---|
| Household authority rules | `src/households/rules.ts` | 14 |
| Authorize.Net gateway | `src/integrations/payments/authorize-net.ts` | 12 |
| Platform ports (portability) | `src/platform/ports.ts` | — |
| Portability guard | `scripts/check-portability.mjs` | CI gate |
| Container | `Dockerfile` | — |
| GCP infrastructure | `deploy/terraform/main.tf` | — |
| Portability contract | `deploy/PORTABILITY.md` | — |

Schema now 23 tables including `household`, `household_member`,
`membership_coverage`, `payment_profile`, `subscription`, `contact_consent`.

**59 tests passing, typecheck clean, portability guard clean.**

New endpoints: `GET /v1/households/:id` (with computed authority and
validation), `GET /v1/members/:id/payment-methods`, `GET /v1/members/:id/consent`,
`GET /v1/admin/expiring-cards`.

---

## 7. Open questions

1. **Who owns the Dynamics data model?** The household redesign is a Dynamics
   change, not just an app change.
2. **Is the Authorize.Net merchant account AFRP's or a partner's?** Determines
   whether API credentials are obtainable.
3. **Which of the 26 clubs actually run Breeze**, and who holds each API key?
4. **Was the "18+ own household" rule a deliberate policy** or a workaround for
   a Dynamics constraint? Changes whether this is a technical or governance fix.
5. **Has SMS already been sent** to numbers collected through the current
   "click here" flow? If so, consent evidence should be reconstructed now.
6. **Is there an existing GCP organisation and billing account,** or does one
   need creating?

---

*Corrections verified 15 August 2026: the "square" matches on afrp.org are
Astra theme CSS (`.square .posted-on`); Authorize.Net confirmed on
`my.afrp.org/Support-a-Cause`. Portal module list taken from supplied
screenshots, which are authoritative over my earlier URL probing.*
