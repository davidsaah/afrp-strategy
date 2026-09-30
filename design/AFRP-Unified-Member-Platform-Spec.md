# AFRP Unified Member Platform
### Technical assessment and build roadmap

**Prepared for:** American Federation of Ramallah, Palestine
**Date:** August 15, 2026
**Scope:** afrp.org and my.afrp.org

---

## The headline

AFRP does not need to buy a member platform. **You already own one and are using roughly a fifth of it.**

`my.afrp.org` runs on **Microsoft Dynamics 365 with a Power Pages portal** — an enterprise-grade CRM that most nonprofits your size cannot afford or do not have the capacity to run. It is correctly stood up, custom-themed, and already has federated login wired to Facebook, Google, and Microsoft.

It currently exposes exactly four things: membership registration, a donation page, a digital store, and a profile page. There are no events, no giving history, no member directory, no club affiliation, and no connection to the family tree.

Meanwhile, member data is scattered across at least six systems that do not talk to each other. **The work ahead is integration and extension, not procurement.** That is a much cheaper and much more winnable project than a rebuild, and it is the argument to take to the board.

---

## 1. Current state

### 1.1 What is actually running

| Layer | System | Notes |
|---|---|---|
| Public website | WordPress + Astra theme + Beaver Builder | `afrp.org`. Page-builder driven, no structured content types |
| CRM / system of record | **Microsoft Dynamics 365** | The strategic asset. Underused |
| Member portal | **Microsoft Power Pages** | `my.afrp.org`, custom theme, PWA-enabled |
| Authentication | Power Pages local accounts + Facebook / Google / Microsoft (Entra) | Federation already enabled — big head start |
| Payments | **Square** | Donations, membership dues, and digital store |
| Email marketing | **Mailchimp** | Separate list, no CRM sync |
| Meetings / town halls | **Microsoft Teams** | Ad-hoc event links posted as news items |
| Family tree | **Google Groups + Google Sites + Google Forms + a personal Gmail** | Entirely outside the stack |
| Documents | PDFs on WordPress | Magazine, annual reports, convention materials |

### 1.2 Portal pages that exist today

Verified live:

- `/Support-a-Cause` — cause-designated donations
- `/Membership-Registration/` — join and renew
- `/AFRP-Digital-Store/` — bookstore
- `/My-Profile` — profile
- `/SignIn`, `/Register` — auth

Verified **absent** (404): events, event registration, member directory, donation history, convention pages, family tree.

### 1.3 Where the member record fragments

A single engaged member currently exists as **five to seven unlinked records**:

1. A Dynamics contact (if they joined through the portal)
2. A Square customer (dues)
3. A second Square customer (donation — often a different email)
4. A third Square customer (bookstore order)
5. A Mailchimp subscriber
6. A Google Groups member (family tree), pending manual approval
7. A row in a local club's private spreadsheet

**What this costs you, concretely:**

- You cannot answer "who gave last year but has not renewed?" without manual reconciliation.
- You cannot segment Mailchimp by membership status, club, or giving level.
- Lapsed-member outreach is a manual export-and-compare exercise.
- Local club officers have no roster of their own members.
- Year-end tax receipts have to be assembled by hand from Square.
- A member has three or four logins and no single place to see their own history.
- The family tree — your single most distinctive asset — is invisible to the CRM, so you cannot tell whether a family-tree contributor is even a member.

### 1.4 Other confirmed gaps

- **Broken links.** `/programs/family-tree/` and `/ramallah-preservation-project/` both return 404 from linked navigation paths. Worth a full crawl.
- **No event calendar.** Convention, mid-year meeting, town halls, Camp Ramallah, Day of Action, and 26 clubs' local events are announced only as one-off news posts.
- **No application flows.** Scholarships, Project Hope, Leadership Ramallah, and Camp Ramallah all describe programs with no visible way to apply.
- **Static club directory.** 26 cities across 18 states, listed as plain text with `mailto:` links and Facebook URLs. No map, no club-managed pages, no rosters.
- **No searchable archive.** *Hathihe Ramallah*, annual reports, past conventions, and press releases are loose PDFs with no full-text search.

---

## 2. Target architecture

**Principle: Dynamics 365 is the single source of truth. Everything else is a view onto it or a feed into it.**

```
                    ┌─────────────────────────────┐
                    │   Microsoft Entra External   │
                    │   ID  — one login, everywhere│
                    └──────────────┬──────────────┘
                                   │ OIDC
         ┌─────────────────┬───────┴───────┬──────────────────┐
         │                 │               │                  │
   ┌─────▼─────┐    ┌──────▼──────┐  ┌─────▼──────┐   ┌───────▼──────┐
   │ afrp.org  │    │ my.afrp.org │  │ Family Tree│   │ Club admin   │
   │ WordPress │    │ Power Pages │  │ (new app)  │   │ console      │
   └─────┬─────┘    └──────┬──────┘  └─────┬──────┘   └───────┬──────┘
         │                 │               │                  │
         └─────────────────┴───────┬───────┴──────────────────┘
                                   │  Dataverse API
                    ┌──────────────▼──────────────┐
                    │      DYNAMICS 365           │
                    │  Contact · Membership ·     │
                    │  Gift · Event · Club ·      │
                    │  Person (genealogy)         │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
         ┌────▼────┐         ┌─────▼─────┐        ┌─────▼─────┐
         │ Square  │         │ Mailchimp │        │   Teams   │
         │ webhook │         │  2-way    │        │  events   │
         └─────────┘         └───────────┘        └───────────┘
```

### 2.1 Authentication

Power Pages already supports external identity providers, and Facebook / Google / Microsoft are enabled. The recommendation is to consolidate on **Microsoft Entra External ID** (formerly Azure AD B2C) as the single identity provider, with social login as options underneath it.

Then point everything at it:

- WordPress via an OpenID Connect plugin
- Power Pages via its native Entra configuration
- The family tree app via standard OIDC
- Any future club-admin tooling

**Result: one account, one password reset flow, one place to revoke access.** This is the keystone — do it first, because every later phase assumes it.

Keep local Power Pages accounts alive during migration and run a one-time linking pass so existing members are not locked out.

### 2.2 Core data model

Use the **Microsoft Cloud for Nonprofit** common data model where it fits rather than inventing custom entities. Key tables:

| Entity | Purpose | Notes |
|---|---|---|
| `Contact` | The person. The spine of everything | Extend with: club affiliation, clan, membership status, family-tree Person link |
| `Membership` | Term-dated membership record | Tier, start, end, auto-renew, payment reference |
| `Gift` / `Transaction` | Every dollar in | Cause designation, Square reference, receipt status, soft credits |
| `Club` | The 26 local chapters | Officers, geography, own page, own roster |
| `Event` + `Registration` | Convention, town halls, camp, club events | Sessions, capacity, ticket types, check-in |
| `Program Application` | Scholarships, Project Hope, Camp, Leadership | Reusable application + review workflow |
| `Person` (genealogy) | Family tree individual | Distinct from Contact; optional link where a member matches |
| `Relationship` | Genealogical edges | Parent, spouse, child, with date qualifiers |

Design note: keep `Person` (genealogy) separate from `Contact` (member). Most of the 30,000 people in the tree are deceased or not members, and most members will map to exactly one Person. A nullable link between them is the right relationship — collapsing them will cause pain.

---

## 3. Roadmap

Estimates are in **developer-weeks for one competent full-stack developer** with Power Platform familiarity, and assume AFRP staff availability for decisions and testing. They do not include license costs or board approval cycles.

### Phase 0 — Foundation (3–4 weeks)

The unglamorous work that everything else depends on. Do not skip it.

| # | Item | Est. |
|---|---|---|
| 0.1 | Audit the existing Dynamics instance — entities, fields, record counts, data quality, existing automations | 1 wk |
| 0.2 | Full crawl of afrp.org; fix 404s including family-tree and preservation-project paths | 2 days |
| 0.3 | Dedupe existing contacts; establish a matching rule (email + name + DOB) | 1 wk |
| 0.4 | Stand up Entra External ID; configure Power Pages against it; link existing local accounts | 1 wk |

**Deliverable:** a trustworthy contact table and one working login. Nothing user-visible. Say so up front so nobody expects a demo.

### Phase 1 — Close the loop on money and messaging (4–6 weeks)

Highest operational payoff per hour. This is what makes staff stop doing manual reconciliation.

| # | Item | Est. |
|---|---|---|
| 1.1 | Square webhook → Dynamics. Every dues payment, donation, and store order lands on the right contact | 2 wks |
| 1.2 | Mailchimp two-way sync — membership status, club, giving level as merge fields and segments | 1.5 wks |
| 1.3 | Member-facing giving and membership history in the portal | 1 wk |
| 1.4 | Automated year-end tax receipts | 0.5 wk |
| 1.5 | Membership auto-renew + lapsed-member reminder sequence | 1 wk |

**Deliverable:** staff can answer "who lapsed?" in a query instead of an afternoon. Members can see their own history. This is the phase that pays for the project.

### Phase 2 — Events and clubs (5–7 weeks)

| # | Item | Est. |
|---|---|---|
| 2.1 | Event + Registration entities; unified calendar on afrp.org pulling from Dynamics | 2 wks |
| 2.2 | Registration and ticketing via Square; confirmation emails | 1.5 wks |
| 2.3 | Convention module — sessions, capacity, QR check-in | 1.5 wks |
| 2.4 | Club entity + club pages; club affiliation on contact records | 1 wk |
| 2.5 | Club officer console — view roster, post local events | 1 wk |

**Deliverable:** one calendar for the whole federation, and 26 clubs that can finally see and serve their own members.

### Phase 3 — Family Tree (8–12 weeks)

The crown jewel, and the reason to do the rest. Deserves its own discovery phase before committing to the estimate.

| # | Item | Est. |
|---|---|---|
| 3.1 | Discovery — inventory the clan books, assess data quality, define the migration path off Google Sites | 2 wks |
| 3.2 | `Person` + `Relationship` model; GEDCOM import/export | 2 wks |
| 3.3 | Migrate existing clan data; reconcile against the 1982 Shaheen genealogies | 2–4 wks |
| 3.4 | Tree browsing and search UI — ancestor/descendant views, clan navigation | 2 wks |
| 3.5 | Member submission with moderation queue (replaces Google Forms + the personal Gmail inbox) | 1.5 wks |
| 3.6 | Privacy rules — living individuals restricted, deceased public to members | 0.5 wk |

**Deliverable:** 500 years and 30,000 people, searchable, contributable, and no longer dependent on one volunteer's inbox.

**Risk flag:** this is the phase most likely to run long, because the data quality of the existing clan books is unknown until 3.1 is done. Treat the range as genuinely uncertain and re-estimate after discovery.

**Continuity flag:** the family tree currently has a single point of failure — one volunteer, one Gmail account, one Google Site. That is a preservation risk for irreplaceable data, independent of any software argument. It is worth raising with the board in those terms.

### Phase 4 — Programs and archive (4–6 weeks)

| # | Item | Est. |
|---|---|---|
| 4.1 | Reusable application + review workflow for Scholarships, Project Hope, Camp Ramallah, Leadership Ramallah | 2.5 wks |
| 4.2 | Member directory with per-field privacy controls and opt-out | 1 wk |
| 4.3 | Searchable document archive — magazine, annual reports, press, convention materials | 1.5 wks |

---

## 4. Sequencing rationale

If the board will only fund one phase, fund **Phase 1**. It is the shortest path to a visible operational win, it requires no new vendors, and it produces the reporting that justifies everything after it.

Phase 0 is non-negotiable as a prerequisite but should be framed as part of Phase 1's cost rather than as a standalone ask — it is hard to sell a month of work with no demo at the end.

**Phase 3 is the one people will be most excited about and should be started last.** It is the largest, the riskiest, and the one that benefits most from a clean contact table and a working identity layer underneath it. Resist the pull to start there.

---

## 5. Open questions

These need answers from AFRP staff before the estimates firm up:

1. **Who administers the Dynamics instance today?** Internal staff, a volunteer, or an outside partner? This determines whether the work is additive or a handover.
2. **What Dynamics licensing is in place?** Nonprofit grant pricing, Microsoft Cloud for Nonprofit, or standard? Affects which entities are available out of the box.
3. **How many contacts are in Dynamics today**, and what share of the membership do they represent?
4. **Is Square a deliberate choice or inherited?** Dynamics has native payment connectors; worth knowing whether Square is load-bearing.
5. **Who owns the family tree data**, and is there board appetite to migrate it off Google?
6. **What is the actual budget and timeline?** The phases can be resequenced significantly around a hard convention date.
7. **Is there an existing member directory** that was deliberately withheld for privacy reasons? If so, Phase 4.2 is a policy question before it is a technical one.

---

## 6. What I would want screenshots of

Everything above was determined from the public web. These are behind login and would sharpen the estimates most:

- The `my.afrp.org` member dashboard after sign-in
- The membership registration flow, including tier options and pricing
- `/My-Profile` — which fields exist on the contact record
- The Dynamics admin view: entity list, contact record layout, contact count
- The family tree members-only Google Site and a sample clan book page
- The Google Form used for family tree submissions
- Any existing Dynamics reports or dashboards staff rely on
- Square dashboard — item/category structure for dues vs. donations vs. store

---

*Findings verified against afrp.org and my.afrp.org on August 15, 2026 via public HTTP inspection. Estimates are planning-grade and should be revised after Phase 0 discovery.*
