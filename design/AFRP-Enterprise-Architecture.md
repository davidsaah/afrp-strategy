# AFRP Enterprise Platform
### Architecture, build-vs-extend analysis, and delivery plan

**Prepared for:** American Federation of Ramallah, Palestine
**Date:** August 15, 2026
**Assumes:** small funded team (2–4 developers), TypeScript + PostgreSQL, cloud-agnostic
**Companion artifacts:** backend prototype (`afrp-platform/`), web member portal, admin console, mobile app prototypes
**Since 2 October 2026:** the platform is built as the Hub (`plan/MASTER-PLAN.md` §1). Where this document's August assumptions about the Federation's systems have moved, a dated pointer stands beside them. Payments and the books are recorded as practice in `AFRP-Multi-Entity-Ledger.md` §9 and `AFRP-QuickBooks-Integration-Spec.md` §12. The family tree's record and custody are D69 and Q-201.

---

## 0. What changed since the last document

Two findings reshape the plan.

**Breeze ChMS is in the picture.** Local clubs run Breeze — a church management
system. Its API is the single hardest constraint in this entire architecture,
and it is not close:

| Constraint | Source | Consequence |
|---|---|---|
| **20 requests/minute per API key** | Breeze support docs | ~1,200 requests/hour ceiling. A 3,000-person club full scan takes ~8 minutes |
| **One account, one key, per club** | Breeze account model | Not one integration — up to 26 separate tenants, each with its own key, quota, and failure mode |
| **No webhooks** | API reference | Change detection must poll. There is no push |
| **Event reads cached ≤15 min** | API reference | Event data is never live |
| **No vendor API support since Feb 1, 2020** | Breeze support docs | Undocumented behaviour is yours to discover. Breeze returns `false` with HTTP 200 |
| **No documented pagination or rate-limit headers** | API reference | Limits must be enforced client-side, not discovered from responses |

**AFRP already owns Microsoft Dynamics 365 + Power Pages.** `my.afrp.org` is a
Power Pages portal on Dynamics, custom-themed, with federated login to
Facebook/Google/Microsoft already enabled. It exposes four things: membership
registration, Support-a-Cause, digital store, profile. Everything else 404s.

These two facts frame the central decision.

---

## 1. The Dynamics decision

You asked for the tradeoffs rather than a recommendation up front. Here they
are, then the recommendation.

### 1.1 The three options

**A — Extend Power Platform only.** Build everything as Power Pages + Dataverse
+ Power Automate. No custom services.

**B — Custom services alongside Dynamics.** Dynamics stays the CRM system of
record for contacts, memberships, and gifts. Custom TypeScript services own the
family tree, events, Breeze integration, club tooling, and mobile. They
integrate through the Dataverse API.

**C — Replace Dynamics.** Full custom platform. Dynamics retired.

### 1.2 Five-year cost comparison

Figures are planning-grade order-of-magnitude for a 2–4 developer team, in USD.
Licensing assumes AFRP holds Microsoft nonprofit grant pricing — **verify this
before trusting the numbers**, because it swings option A and B by six figures.

| | **A — Power Platform** | **B — Alongside** | **C — Replace** |
|---|---|---|---|
| Initial build | $120k–180k | $280k–420k | $550k–850k |
| Year 1 licensing | $8k–25k | $8k–25k | $0 |
| Years 2–5 licensing | $32k–100k | $32k–100k | $0 |
| Years 2–5 hosting | ~$6k | $30k–60k | $40k–90k |
| Years 2–5 maintenance | $80k–140k | $180k–300k | $300k–500k |
| **5-year total** | **$250k–450k** | **$530k–900k** | **$890k–1.44M** |
| Time to first member value | 2–3 months | 4–6 months | 12–18 months |
| Staffing floor after launch | 0.5 FTE, or a partner | 1.5–2 FTE | 3+ FTE, permanently |
| Bus-factor risk | Low | Medium | **High** |

### 1.3 What each option can and cannot do

| Capability | A | B | C |
|---|---|---|---|
| Membership, dues, giving, receipting | ✅ native | ✅ native | ⚠️ rebuild from zero |
| Events + registration | ✅ adequate | ✅ | ✅ |
| Native mobile app | ⚠️ Power Apps only; poor offline, poor convention check-in | ✅ React Native | ✅ |
| Family tree (30k nodes, recursive queries) | ❌ Dataverse is wrong for graph traversal | ✅ Postgres recursive CTEs | ✅ |
| 26 rate-limited Breeze tenants | ❌ Power Automate can't express a per-tenant token bucket | ✅ purpose-built worker | ✅ |
| Identity resolution across 7 systems | ⚠️ limited fuzzy matching | ✅ | ✅ |
| Nonprofit grant licensing retained | ✅ | ✅ | ❌ forfeited |
| Survives the lead developer leaving | ✅ | ⚠️ | ❌ |

### 1.4 Recommendation: **B, with a hard boundary**

Option A fails on two requirements that are not negotiable for AFRP
specifically. The family tree is a graph problem — 30,000 people, five
centuries, recursive ancestor and descendant traversal. Dataverse is a
relational CRM store and will not do this acceptably at that scale. And the
Breeze integration needs per-tenant token buckets, incremental cursors, and
budget-aware backoff across 26 independent accounts; Power Automate cannot
express that. Those two capabilities are precisely the ones that make this
platform distinctive rather than generic.

Option C fails on organisational sustainability, which is the real constraint
for a volunteer-led federation. It forfeits nonprofit licensing worth real money,
rebuilds solved problems (receipting, fund accounting, campaign attribution),
and creates a permanent 3-FTE obligation that AFRP has no evident mechanism to
fund past the enthusiasm of whoever built it. **The most likely failure mode for
this project is not technical — it is that the person who built it moves on.**
Option C maximises that risk.

Option B costs roughly twice option A and roughly 60% of option C, and it is
the only one that clears both bars.

**The hard boundary that makes B work — and the thing most likely to be
violated under deadline pressure:**

| Dynamics owns | Custom platform owns |
|---|---|
| Contact master record | Family tree (`tree_person`, `tree_relationship`) |
| Membership terms and dues | Events and registration |
| Gifts, campaigns, receipting | Breeze integration and sync state |
| Financial reporting | Identity resolution / merge queue |
| Communication preferences | Club officer tooling |
| | Mobile API |

Contacts flow **Dynamics → platform**. Everything the platform learns about a
person flows **back to Dynamics** as an update to the master. If custom services
ever start writing authoritative contact data that Dynamics does not have, you
have accidentally chosen option C without deciding to — and you will be paying
for both. Write this rule down and enforce it in code review.

### 1.5 Answer these before committing

1. Does AFRP hold Microsoft nonprofit grant licensing, and for how many seats?
2. Who administers the Dynamics instance today — staff, volunteer, or partner?
3. How many contacts are in Dynamics, and what share of actual membership is that?
4. How many of the 26 clubs actually use Breeze, and who owns each API key?
5. Is there budget for 1.5–2 FTE of ongoing maintenance after launch? If the
   honest answer is no, **choose option A and accept its limits** rather than
   building something that decays.

---

## 2. Architecture

### 2.1 System context

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Member web  │  │ Mobile app   │  │ Admin console│  │  afrp.org    │
│  (Next.js)   │  │(React Native)│  │  (React SPA) │  │ (WordPress)  │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       └─────────────────┴─────────────────┴─────────────────┘
                                 │ OIDC + JSON/REST
                    ┌────────────▼────────────┐
                    │   API  (Fastify / TS)   │
                    │   authz · validation    │
                    └────────────┬────────────┘
          ┌──────────────────────┼──────────────────────┐
   ┌──────▼──────┐        ┌──────▼──────┐        ┌──────▼──────┐
   │ PostgreSQL  │        │  Job queue  │        │ Object store│
   │  (primary)  │        │  (pg-boss)  │        │ (S3-compat) │
   └─────────────┘        └──────┬──────┘        └─────────────┘
                                 │
        ┌────────────────┬───────┴────────┬────────────────┐
   ┌────▼────┐    ┌──────▼──────┐   ┌─────▼─────┐   ┌──────▼──────┐
   │ Breeze  │    │  Dynamics   │   │  Square   │   │  Mailchimp  │
   │ ×26 keys│    │   365 CRM   │   │  webhook  │   │   2-way     │
   │ 20/min  │    │ system of   │   │           │   │             │
   │ no hooks│    │  record     │   │           │   │             │
   └─────────┘    └─────────────┘   └───────────┘   └─────────────┘
```

### 2.2 Stack and why

| Layer | Choice | Rationale |
|---|---|---|
| Language | TypeScript everywhere | One language across API, web, and mobile. For a 2–4 person team this is the single biggest force multiplier available |
| API | Fastify | Fast, small, schema-first validation. Less ceremony than NestJS for this size |
| Database | PostgreSQL 16 | Recursive CTEs for the family tree, `pg_trgm` for fuzzy name matching, `jsonb` for source payloads. The tree alone justifies it |
| Queue | pg-boss | Postgres-backed. **Not** Redis — one fewer service to operate, and the job volume here is trivial |
| Web | Next.js (App Router) | SSR for public pages, one framework for member portal and admin |
| Mobile | React Native + Expo | Shares types with the API. Expo removes most native build pain from a small team |
| Auth | Microsoft Entra External ID | Power Pages already federates to it. One IdP for everything |
| Hosting | Containers on Fly.io / Render / Railway | Cloud-agnostic per your preference. Managed Postgres. Trivially portable to AWS or Azure later |
| Object store | Any S3-compatible | Magazine archive, annual reports, tree document scans |

**Deliberately not chosen:** Kubernetes (operational cost far exceeds benefit at
this scale), microservices (a modular monolith is correct for 2–4 developers),
GraphQL (REST plus generated types is less machinery for a known set of clients),
Redis (Postgres covers queue and cache here).

### 2.3 Data model

Full DDL in `afrp-platform/src/db/schema.sql`. The load-bearing decisions:

**`person_source_link` is the reason this platform exists.** One person, N
external identities, each with a confidence score and the rule that matched it.
The `scope_id` column carries the club id for Breeze rows, because Breeze is
per-club — without it you cannot tell Detroit's person 40218 from Chicago's.

**`tree_person` is separate from `person`.** Most of the ~30,000 people in the
Ramallah genealogy are deceased or were never AFRP members. A nullable
`tree_person.person_id` bridges the two. Collapsing them would force every
historical figure into the member table and make every membership query filter
around 30,000 rows of 17th-century ancestors.

**Audit is append-only.** The application role gets INSERT and SELECT on
`audit_log`, never UPDATE or DELETE. Corrections are compensating rows.

**Money is `numeric(12,2)`,** and the pg driver is configured to parse it as a
number rather than let it round-trip through float.

### 2.4 The Breeze connector — where the real engineering is

This is the part of the system most likely to be got wrong, so it is the part
the prototype implements fully. Working code: `src/integrations/breeze/`.

**Rate limiting.** A `TokenBucket` per club, in a `BucketRegistry` keyed by club
id. Every request `await`s a token. Calls queue FIFO rather than failing, so a
burst of workers degrades into an orderly ~3s-apart trickle instead of a
stampede that trips the vendor block. One club exhausting its quota cannot
starve the other 25.

**Change detection without webhooks.** Poll `/api/account/list_log`, extract the
distinct person ids that actually changed, and fetch only those. This is the
difference between an incremental nightly sync and re-reading every person in
every club — which at 20 req/min across 26 clubs would not finish. A persisted
`activity_cursor_at` high-water mark per club makes each poll incremental, with
a 5-minute overlap window because Breeze's clock is not ours and its reads are
cached.

**The cursor rule.** If a run exhausts its request budget, the cursor is **not**
advanced past unprocessed work. Neither is it advanced on failure. The next run
resumes. This is the difference between a sync that falls behind and one that
silently loses a club's data forever — and it is the kind of bug that is
invisible for months. There is a test for it.

**Error semantics, learned from an unsupported API:**

| Response | Handling | Why |
|---|---|---|
| 429 | Retry with exponential backoff from 5s | Another process is likely using the same club key |
| 401 / 403 | **No retry.** Mark `key_expired`, alert | The club rotated its key. Hammering makes it worse |
| 5xx | Retry up to 3× | Transient |
| 200 with body `false` | Treat as error | Breeze actually does this |
| 200 with `errors` key | Treat as error | Ditto |

**Conflict policy per club,** because clubs will disagree about who owns member
contact data. `platform_wins` / `breeze_wins` / `manual`. Under `manual` — the
default — divergent fields land in `field_conflict` for a human, and nothing is
overwritten. Clubs are independent organisations with their own officers; a
national system that silently overwrites their data will lose their cooperation,
and cooperation is the actual dependency here.

### 2.5 Identity resolution

`src/identity/resolve.ts`. Additive weights, clamped to 1:

| Signal | Weight |
|---|---|
| `email_exact` (gmail dots/+tags normalised) | +0.96 |
| `name` fuzzy (≥0.80 on both parts) | up to +0.36 |
| `dob_exact` | +0.30 |
| `phone_exact` | +0.30 |
| `postal_match` | +0.12 |
| **`dob_conflict`** | **−0.55** |

Auto-merge ≥0.95. Human review ≥0.60. Below that, no match.

Three decisions worth defending in review:

- **Name alone never clears review.** "George Yacoub" and "Nadia Khoury" are not
  rare in this community. Name-only merging corrupts the member file, and an
  incorrect merge is far more expensive to undo than a missed one is to catch.
- **The fuzzy gate is 0.80, not 0.90.** Ramallah-family surnames reach AFRP
  through multiple transliterations of the same Arabic name — Yacoub/Yakoub,
  Khoury/Khouri, Mogannam/Muqannam. A 0.90 gate misses exactly the duplicates
  AFRP actually has. This was caught by a failing test during the prototype
  build, not by inspection — which is itself the argument for the test suite.
- **A conflicting DOB is a strong negative signal.** Same name, same phone,
  different birth date is a father and son sharing a household, not a duplicate.

Blocking on last-name prefix, email, and phone keeps this tractable: 30k records
compared pairwise is 450M comparisons; blocked, it is a nightly job.

### 2.6 Security and compliance

| Concern | Approach |
|---|---|
| Authentication | Entra External ID, OIDC, RS256, JWKS cached. Social login underneath one IdP |
| Authorisation | Scopes: `member:read`, `member:write`, `club:admin`, `staff`, `admin:write`. Row-level checks on club-scoped data |
| Breeze API keys | Secrets manager only. `club_breeze_account.api_key_ref` stores a reference, never the key. The schema makes leaking one awkward by construction |
| PII at rest | Postgres encryption at rest; DOB and address restricted to `staff` scope |
| Living individuals in the tree | Restricted by default. The lineage endpoint nulls birth/death years for living people and flags `restricted` |
| Payments | **Never touch card data.** Square hosted checkout only. This keeps AFRP out of PCI scope entirely. *In practice (research, 2 Oct 2026):* the Federation's registration system now uses one card-processing account per entity (AFRP, ARFECF, ARFHSN), and the Hub's card processing is a hosted integration, simulated today behind a production guard (MASTER-PLAN §1a) |
| Audit | Append-only, 7-year retention |
| Backups | Daily automated, 30-day retention, **restore tested quarterly**. An untested backup is not a backup |
| Family tree continuity | The tree is irreplaceable and currently depends on one volunteer's Gmail. Nightly GEDCOM export to object storage, plus offsite copy, from day one. *Since 2 Oct 2026:* D69 makes the Hub the record after a parallel run, with a nightly export under `tree:moderate`. The run needs a production database with backups (P28 §7; MASTER-PLAN §1d). Custody of the master file today is Q-201 |

---

## 3. Delivery plan

Estimates are developer-weeks for a 2–4 person team. Phases 1–2 can overlap
once the schema stabilises.

### Phase 0 — Foundation (4–5 weeks)

| Item | Est. |
|---|---|
| Audit Dynamics: entities, fields, record counts, data quality | 1 wk |
| Entra External ID tenant; OIDC across API, web, Power Pages | 1.5 wk |
| Postgres schema, migrations, CI/CD, environments | 1 wk |
| Dynamics ↔ platform contact sync, both directions | 1.5 wk |
| Fix afrp.org 404s (`/programs/family-tree/`, `/ramallah-preservation-project/`) | 2 days |

**Deliverable:** one login, one contact table, a deploy pipeline. Nothing
user-visible — say so up front so nobody expects a demo.

### Phase 1 — Money and messaging (5–6 weeks)

| Item | Est. |
|---|---|
| Square webhook → gift records, reconciliation | 2 wk |
| Mailchimp two-way sync with membership/club/giving segments | 1.5 wk |
| Member giving + membership history (web) | 1 wk |
| Automated tax receipts | 0.5 wk |
| Auto-renew and lapsed-member sequences | 1 wk |

**Deliverable:** staff answer "who lapsed?" with a query instead of an
afternoon. This is the phase that pays for the project — lead with it.

### Phase 2 — Breeze and clubs (6–8 weeks)

| Item | Est. |
|---|---|
| Breeze connector: rate limiter, client, retry semantics | 1.5 wk |
| Incremental sync worker, cursors, budget management | 2 wk |
| Per-club onboarding: key vault, health checks, conflict policy | 1.5 wk |
| Identity resolution + merge queue UI | 2 wk |
| Club pages and officer console | 1 wk |

**Deliverable:** 26 clubs visible in one system for the first time.
**Risk:** club-by-club onboarding is a *people* problem, not a technical one.
Each club must produce an API key from an account owner who may be a volunteer
with other priorities. Budget calendar time, not just developer time, and expect
this phase to slip for reasons no engineer can fix.

### Phase 3 — Events and mobile (7–9 weeks)

| Item | Est. |
|---|---|
| Event + registration model, Square ticketing | 2 wk |
| Unified calendar (web + afrp.org embed) | 1 wk |
| React Native app: auth, member card, events, giving | 3 wk |
| Convention module: sessions, capacity, QR check-in | 2 wk |
| App Store / Play submission | 1 wk |

**Deliverable:** a member walks into convention and checks in with their phone.
This is the phase members will actually notice — which makes it the one to
schedule against a convention date.

### Phase 4 — Family tree (10–14 weeks)

| Item | Est. |
|---|---|
| Discovery: inventory clan books, assess data quality, plan migration | 2 wk |
| `tree_person` / `tree_relationship`, GEDCOM import/export | 2 wk |
| Migrate from Google Sites; reconcile against Shaheen (1982) | 3–5 wk |
| Tree browsing, search, ancestor/descendant views (web + mobile) | 3 wk |
| Submission + moderation queue | 1.5 wk |
| Privacy rules for living individuals | 0.5 wk |

**Deliverable:** 30,000 people, searchable, contributable, no longer dependent
on one inbox.

**Two flags.** First, the estimate is genuinely uncertain until 4.1 is done —
the data quality of the existing clan books is unknown. Re-estimate after
discovery rather than defending this range. Second, and more important: the
tree currently has a single point of failure — one volunteer, one Gmail account,
one Google Site — holding irreplaceable records. That is a preservation risk
independent of any software argument, and it is worth raising with the board in
exactly those terms. **The nightly GEDCOM export in Phase 0 mitigates it long
before Phase 4 delivers.**

### Phase 5 — Programs and archive (5–6 weeks)

| Item | Est. |
|---|---|
| Reusable application + review workflow (Scholarships, Project Hope, Camp, Leadership) | 2.5 wk |
| Member directory with per-field privacy | 1 wk |
| Searchable document archive (magazine, annual reports, press) | 1.5 wk |

### Summary

| Phase | Weeks | Cumulative |
|---|---|---|
| 0 — Foundation | 4–5 | 5 |
| 1 — Money and messaging | 5–6 | 11 |
| 2 — Breeze and clubs | 6–8 | 19 |
| 3 — Events and mobile | 7–9 | 28 |
| 4 — Family tree | 10–14 | 42 |
| 5 — Programs and archive | 5–6 | 48 |

**~11–12 months** for a 2–4 person team. Phases 1 and 2 can overlap; phases 4
and 5 can slip without blocking anything else.

---

## 4. Sequencing rationale

If only one phase gets funded, fund **Phase 1**. Shortest path to a visible
operational win, no new vendors, and it produces the reporting that justifies
everything after it.

Phase 0 is a prerequisite but should be costed *inside* Phase 1 rather than
asked for separately — it is hard to sell five weeks with no demo at the end.

**Phase 4 is the one everyone will be most excited about and should be built
last.** It is the largest, the riskiest, and the one that benefits most from a
clean contact table and a working identity layer underneath it. Resist the pull
to start there. The Phase 0 GEDCOM export addresses the urgent part — the
preservation risk — without committing to the full build early.

---

## 5. What the prototypes demonstrate

| Artifact | Shows |
|---|---|
| `afrp-platform/` | Runnable API. Schema, Breeze connector with rate limiting and cursor semantics, identity matcher. **33 passing tests**, clean typecheck |
| Member portal prototype | What a member sees: one record, one login |
| Admin console prototype | What staff see: Breeze sync health, budget meters, merge queue, conflict resolution, moderation |
| Mobile prototype | 8 screens including digital member card with convention QR check-in |

The backend is the one to review closely. `README.md` in that repo points at the
three files that matter, and the test suite documents the behaviour that is
easy to get wrong — particularly the cursor-advance rule, which is where a
silent data-loss bug would live.

---

## 6. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Key-person dependency** | High | High | Two developers on every subsystem. Documentation as a deliverable, not an afterthought. This is the most likely failure mode |
| Club-by-club Breeze onboarding stalls | High | Medium | Treat as relationship work with a named owner per club. Platform functions without Breeze; sync is additive |
| Breeze changes or removes its API | Medium | High | Unsupported since 2020. Connector is isolated behind one interface; GEDCOM-style export keeps club data recoverable |
| Family tree data quality worse than expected | Medium | High | Discovery phase before committing. Manual reconciliation budget |
| Dynamics boundary erodes under deadline | Medium | High | Write the ownership table into code review standards. Audit it quarterly |
| Nonprofit licensing assumption wrong | Medium | High | **Verify before committing to option B.** It moves the 5-year total materially |
| Maintenance funding does not materialise | Medium | High | If 1.5–2 FTE is not realistically fundable, choose option A instead and accept its limits |

---

*Prepared August 15, 2026. Breeze constraints verified against Breeze support
documentation and API reference. Dynamics/Power Pages, Square, and Mailchimp
determined from public HTTP inspection of afrp.org and my.afrp.org. Cost
estimates are planning-grade and depend on licensing assumptions stated in §1.5.*

**Sources:** [Breeze API — Advanced Custom Development](https://support.breezechms.com/hc/en-us/articles/360001324153-API-Advanced-Custom-Development) ·
[Breeze API Reference](https://app.breezechms.com/api) ·
[Breeze API v1 (GitHub)](https://github.com/BreezeChMS/breeze-api-v1) ·
[Breeze support docs](https://support.mybreeze.io/category/12-breeze-api-documentation)
