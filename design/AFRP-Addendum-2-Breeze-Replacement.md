# AFRP Enterprise Platform — Addendum 2
### Breeze replacement, life events, and directories

**Date:** August 15, 2026
**Builds on:** Addendum 1 (corrections, households, GCP)
**Trigger:** four product decisions, and a directive to fuse family-tree functions into the member experience

---

## 1. The four decisions

| # | Decision | Biggest consequence |
|---|---|---|
| 1 | **Wedding → Family tier, free year one**, then renews at the Family rate | Revenue-positive only when a non-member is involved. See §2 — this needs a policy tweak |
| 2 | **Life events write PROVISIONAL tree records** — visible immediately, canonical only after moderation | Correct call. Needs a `state` column on genealogy tables and a view that cannot leak unverified data |
| 3 | **The club portal REPLACES Breeze** | Changes Breeze from a permanent dependency into a migration source. Materially larger club-portal scope, materially better end state |
| 4 | **Directories members-only, per-field opt-in** | Privacy modelled as data, not as a rendering decision. Absence of a row means "not visible" |

Decision 3 is the one that changes the architecture. In Addendum 1, the Breeze
connector was permanent infrastructure — 26 rate-limited tenants, forever, on
an API the vendor stopped supporting in 2020. It is now a **migration tool with
a finish line.** That is a strictly better place to be, and the connector
already written does not go to waste: it becomes the extraction path.

---

## 2. The wedding benefit has a revenue problem

Modelled from the implemented rules (`planWeddingBenefit`), annual dues:

| Scenario | Year 1 forgone | Year 2+ revenue | Was | Change |
|---|---|---|---|---|
| **Both already Individual members** | $180 | $150 | $180 | **−$30/yr, permanently** |
| One member + one non-member | $90 | $150 | $90 | **+$60/yr** |
| Both non-members | $0 | $150 | $0 | **+$150/yr** |
| Patron + non-member | $1,000 | $1,150 | $1,000 | **+$150/yr** |

**The benefit is a recruitment instrument, and it works.** Two of the three
common cases add recurring revenue, and the case that adds most is exactly the
one AFRP most wants — a member marrying someone outside the federation.

But when **both spouses are already members**, the upgrade costs a free year
*and* permanently reduces the household from two Individual dues to one Family
dues. Every AFRP-couple wedding is a small permanent revenue reduction.

**Three options, and this is a board decision rather than an engineering one:**

- **A — Accept it.** Frame it as retention spending. Two members who marry are
  the least likely to lapse; $30/yr is cheap loyalty. Simplest to explain.
- **B — Restrict the free year to weddings involving a non-member.** Keeps the
  recruitment upside, removes the leak. Harder to explain, and it means telling
  an AFRP couple they get less than a couple who married out — which reads
  badly in a community that values marrying in.
- **C — Free year for both, but keep two memberships** rather than collapsing
  to a Family tier. Year 1 forgone $180, year 2+ back to $180. No permanent
  leak, and no Family-tier upsell either.

**My recommendation is A**, with the caveat stated openly to the board. The
recruitment gain from mixed marriages very likely exceeds the leak from
member-member ones, but that depends on a ratio only AFRP knows. If most
weddings are between two existing members, reconsider — and the platform will
be able to answer that question after the first year, which it currently cannot.

The rules engine implements A. Switching to B or C is a change to one function
with tests already around it.

**Two safeguards already built in:**

- A **Patron, Manar, or Life member is never "upgraded" to Family** —
  that would be a downgrade dressed as a gift. Their existing tier is extended
  twelve months from its current end date instead.
- A **non-member spouse gets a membership created for them.** Requiring them to
  already exist would waste the single best recruitment moment AFRP gets.

---

## 3. Replacing Breeze — feature parity

### 3.1 The honest starting point

Breeze is a **church** management system. A meaningful share of it is built for
Sunday morning and is dead weight for a cultural federation:

| Breeze module | Relevant to AFRP? |
|---|---|
| Service Planning, Song Library, SongSelect®, Worship App | **No.** Worship tooling |
| Volunteer scheduling by service | Partially — AFRP has volunteers, not service rotas |

That matters for the replacement argument: **you are not rebuilding all of
Breeze. You are rebuilding the roughly 70% of it that a federation actually
uses**, and dropping the rest.

### 3.2 Parity matrix

| Breeze module | What clubs use it for | Replacement | Difficulty | Notes |
|---|---|---|---|---|
| **People** | Member records, custom fields | `person` + `club_group` + household model | **Easy** | Already stronger — the platform resolves identity across systems, Breeze cannot |
| **Families** | Grouping households | `household` + `household_member` | **Easy** | Already better; Breeze has the same 18+ problem in a different shape |
| **Tags / Groups** | Committees, ministries, segments | `club_group`, `club_group_member` | **Easy** | Direct equivalent |
| **Events** | Club calendar | `event` + `club_officer` publishing | **Easy** | Plus national-calendar publishing Breeze has no concept of |
| **Rooms & resources** | Preventing double-booking | `club_resource`, `event_resource` | **Medium** | Needs a real conflict check, not just a join table |
| **Check-in & attendance** | Events, camps, name tags | `event_registration.checked_in_at` + QR | **Medium** | Name-tag printing is fiddly. Child check-in needs a security code — safeguarding, not convenience |
| **Forms** | Sign-ups, registrations | Program application engine | **Medium** | Generalising beyond program applications is real work |
| **Email** | Club communication | Email port + Mailchimp | **Easy** | Already planned |
| **Text messaging** | Reminders, alerts | SMS port + `contact_consent` | **Medium** | Consent model already built. **This is the one clubs will miss most if it slips** |
| **Giving** | Online + text giving | Authorize.Net + `gift` | **Medium** | Per-club fund accounting needs care |
| **Reporting** | Attendance, giving | Postgres + a reporting view layer | **Medium** | Breeze's reports are unsophisticated; parity is a low bar |
| **Mobile app (staff)** | Officer lookups, check-in | React Native club-officer mode | **Medium** | Already in the roadmap |
| **Data import/export** | Onboarding, backup | CSV + GEDCOM + API | **Easy** | Must ship before migration, not after |

### 3.3 What is genuinely hard

Three things, and none of them are the database:

1. **Text messaging.** Breeze bundles SMS. Replacing it means a provider,
   number provisioning, opt-out handling, and carrier registration (10DLC) —
   which takes weeks of calendar time regardless of engineering effort. **Start
   this early**; it is the item most likely to hold up a club cutover.
2. **Child check-in.** Breeze prints name tags with security codes so a child
   is released only to the adult who dropped them off. Camp Ramallah needs
   this. It is a safeguarding requirement, not a feature.
3. **Twenty-six migrations, each a relationship.** The technical migration is
   the easy half. Each club has officers who chose Breeze, learned it, and will
   reasonably ask why they should change. **Budget calendar time and a named
   owner per club, not developer weeks.**

### 3.4 Migration path per club

```
1. CONNECT      read-only Breeze API access, existing connector
2. EXTRACT      full pull: people, families, tags, events, attendance, giving
                (~8 min per 3,000 people at the 20 req/min ceiling)
3. RECONCILE    identity resolution against the platform; merge queue for
                anything in the 0.60–0.95 review band
4. PARALLEL     both systems live, platform read-only. 2–4 weeks.
                Club officers verify their own roster — they will find things
                identity resolution cannot
5. CUTOVER      writes move to the platform; Breeze becomes read-only
6. ARCHIVE      final export retained; Breeze subscription cancelled
```

Steps 1–3 are automated and already largely built. **Step 4 is where the real
risk lives** and it cannot be shortened by writing more code.

Order the clubs deliberately: start with **one enthusiastic mid-sized club**
(Detroit is the obvious candidate), then the clubs already in trouble on
Breeze, then the rest. The three clubs currently `degraded`, `key_expired`, or
`not_connected` are arguably the easiest sells — their Breeze is already not
working.

---

## 4. Life events → tree

### 4.1 The provisional model

```
Member announces ──▶ life_event(submitted)
                          │
                          ├──▶ membership grant     (Family tier, free yr 1)
                          ├──▶ tree writes          state = 'provisional'
                          └──▶ announcement         (feed, restricted if minor)
                                     │
                          moderator reviews
                                     │
                    ┌────────────────┴────────────────┐
                approve                            reject
                    │                                 │
           state = 'canonical'              state = 'rejected'
           enters v_tree_canonical          outcomes reversed via
                                            life_event_outcome
```

Two implementation details that matter more than they look:

**`v_tree_canonical` exists so that forgetting to filter is not possible.** Any
query reading `tree_person` directly could leak unverified records into a
500-year archive. The view is the default read path; the raw table is for
moderation only.

**`life_event_outcome` records everything an event produced** — the membership
grant, each tree row, the announcement — so a rejection reverses cleanly. Without
it, rejecting a wedding six weeks later leaves an orphan Family membership
nobody can explain.

### 4.2 Safeguarding, built into the rules

| Rule | Behaviour |
|---|---|
| A newborn's tree record | **Always** provisional and restricted. Not configurable |
| Births and adoptions to social media | **Never** auto-published. Hard-coded, not a default |
| Any life event involving a minor | Blocked from auto-publish regardless of consent |
| Deaths | Never auto-published; require family approval |
| Who may report | Active members only, adults only |
| Birth reported by a non-parent | Flagged for the moderator |
| Neither spouse in the tree | Flagged — a moderator must attach the couple to a lineage |

These are in `src/life-events/rules.ts` with 18 tests. The social-publishing
rule is deliberately not a setting: AFRP posting a member's newborn's name and
photo to Facebook because a checkbox defaulted on is a foreseeable harm, and
configuration is not a good place to keep that promise.

---

## 5. Directories

**Members-only, per-field opt-in, absence means invisible.** `directory_visibility`
has no row per field until the member sets one, and no row means not visible.
Privacy defaults closed rather than depending on a boolean somebody forgot.

Each field carries a scope rather than a boolean: `members` · `club` · `clan` ·
`none`. A member can show their city federation-wide, their email only to their
own club, and their phone to nobody.

**RBPN (professional directory)** is a separate opt-in — `professional_profile.is_listed`
defaults false. Contact details are never published; introductions are brokered
through `introduction_request`. That keeps the network valuable without turning
the membership into a lead list, which is the failure mode of every professional
directory that has ever been built.

---

## 6. Revised roadmap

| Phase | Work | Weeks |
|---|---|---|
| **−1** | Portal mobile fixes, SMS consent, remove Fax | 3–4 |
| 0 | Foundation: Dynamics audit, Entra SSO, schema, CI/CD | 4–5 |
| 1 | Authorize.Net reconciliation, Mailchimp sync, receipts | 5–6 |
| 1b | Household redesign | 3–4 |
| 2 | **Club portal to Breeze parity** — people, groups, events, resources, check-in, messaging, reporting | **10–14** |
| 2b | **SMS provider + 10DLC registration** — start during Phase 1 | 2 (+ calendar time) |
| 3 | **Club migrations** — 26 clubs, staged | 12–20 (mostly calendar) |
| 4 | Events, ticketing, React Native app | 7–9 |
| 5 | **Life events + provisional tree + announcements feed** | 5–7 |
| 6 | **Directories: member + RBPN** | 4–5 |
| 7 | Family tree: migration, explorer, moderation | 10–14 |
| 8 | Social + program integrations | 4–6 |

Roughly **16–20 months** for 2–4 developers — up from 12–13 in Addendum 1,
because replacing Breeze is a much larger commitment than syncing with it.

**Sequencing notes worth arguing about:**

- **Phase 2 is now the biggest single block.** It was "integrate with Breeze";
  it is now "be better than Breeze at the things clubs actually use daily".
- **Phase 3 is mostly calendar, not engineering.** Twenty-six clubs at 2–4
  weeks of parallel running each, some overlapping. Do not staff it as a coding
  problem.
- **Phase 5 (life events) depends on Phase 7 (tree) for the canonical target**
  — but not fully. Provisional records can accumulate against a
  not-yet-migrated tree and be attached during migration. That is worth doing:
  it means announcements can launch early and the goodwill arrives sooner.
- **Start 2b in Phase 1.** 10DLC registration is calendar time nobody can
  compress, and every club cutover waits on it.

---

## 7. What changed in the code

| Added | File | Tests |
|---|---|---|
| Wedding benefit + tree write planning + safeguarding | `src/life-events/rules.ts` | 18 |
| Provisional genealogy state, `v_tree_canonical` | `src/db/schema.sql` | — |
| Life events, outcomes, announcements | `src/db/schema.sql` | — |
| Directory visibility, RBPN profiles, introductions | `src/db/schema.sql` | — |
| Club groups, resources, officers | `src/db/schema.sql` | — |
| Social accounts and post queue, programs and applications | `src/db/schema.sql` | — |

**Schema now 38 tables. 77 tests passing, typecheck clean, portability guard clean.**

---

## 8. Open questions

1. **What proportion of AFRP weddings are between two existing members?** This
   decides whether the wedding benefit is net revenue-positive (§2). Nobody can
   currently answer it — which is itself an argument for the platform.
2. **Who moderates the genealogy queue,** and what is an acceptable turnaround?
   Provisional records are only a good design if review actually happens.
3. **Which club goes first?** It should be one that wants to, not one that is
   easiest technically.
4. **Is there a budget line for club migration support** — someone whose job is
   phoning 26 clubs — or is that expected to come out of developer time? If the
   latter, add 30% to Phase 3.
5. **Does any club use Breeze's child check-in for Camp Ramallah?** If so, that
   feature is a blocker for their cutover, not a nice-to-have.
6. **Should the RBPN directory be a revenue line?** Currently modelled as a
   free member benefit.
7. **Who owns the social accounts today,** and do clubs post independently? The
   model supports per-club accounts; the governance is undecided.

---

*Breeze module list from breezechms.com and Breeze support documentation,
August 2026. Revenue figures modelled from the implemented rules with
illustrative dues; substitute AFRP's real tier pricing before taking §2 to a
board.*

**Sources:** [Breeze ChMS](https://www.breezechms.com) ·
[Breeze API reference](https://app.breezechms.com/api) ·
[Breeze API support policy](https://support.breezechms.com/hc/en-us/articles/360001324153-API-Advanced-Custom-Development)
