# AFRP-Hub build plan — from the design record to a working application

**5 September 2026.** The plan for building what `davidsaah/afrp-mockups`
describes, in the order the design itself suggests, sized honestly, with the
questions that decide it listed at the end.

> **Status, refreshed with every slice.** Phase 0 and Phase 1 done. Phase 2
> (member lens) done except the household slice, refused for want of a
> document (R6). Phase 3 (club lens) done as far as the record allows: club
> voting and households refused. The 500-household fixture is loaded on
> staging and the screens were walked at volume. Build commentary on the
> screens now sits behind `BUILD_NOTES` (off by default) and the staging
> sign-in code shows on screen behind `SHOW_SIGNIN_CODE`. Phase 4 (federation
> lens) in progress: 4a done (dashboard, directory at scale, the lens's own
> shell); 4b done (the election console); 4c done (the registry: clubs,
> programmes, officer terms, events, people, entities — add, suspend/retire,
> and a delete that refuses by name when anything points at the record); 4d done
> (the live floor); 4e done (the ruleset workbench); 4f done (roles &
> permissions — the exact-grant model, R39, replacing the staff-flag gate); 4g
> done (People: Member 360 and the identity & merge queue); 4h done (the
> communications centre at federation scope); 4i done (money — the one ledger,
> closing days and building runs as statements). Phase 4 is finished as far as
> the record allows: the board workspace has no design document and the
> Convention is after the twenty. Phase 5a (the programme lens) is done. On
> 6 September David answered questions 1–21; the answers changed six things
> the same day (notices unfiltered, role:grant reaching down, an office
> carrying its grant, the Executive Committee approving remittance runs by
> name, a fee schedule the admin sets, a vote deleted while a draft or
> cancelled after) and scheduled the slices in §5 below. The
> Django admin is hardened to the same rules: ledgers read-only, deletes
> refuse by name, every model registered with search and filters. Rows below say **ported**, **built** or **refused** per screen; a
> refusal names the missing document.

---

## 1. What the record actually specifies

Read in full for this plan: the 58-screen prototype, the Platform Map (17
modules, each badged), the Complete Platform reference (9 sections, S1–S7,
rules R1–R45), the Portal Build Spec (tokens, breakpoints, the accessibility
gate), the 42 canonical frames (Unified Member 01–21, Unified Operations
01–21), the five deep dives, and `AFRP-Portal/src` — a TypeScript backend
prototype the Map's "Built" badges are audited against.

### The five lenses, 58 screens

| Lens | Screens | Colour | Who it is for |
|---|---|---|---|
| **Front door** | 5 | green | Nobody signed in. Join, sign in, recover, the 18th-birthday refresh. |
| **Member** | 16 | green | A member, seeing their own record. |
| **Club** | 6 | olive | An officer running one club — separately incorporated, one shared record. |
| **Federation** | 18 | pine | Staff running the Federation: people, money, elections, clubs, institutions. |
| **Programme** | 13 | gold | Programme leads: scholarships, magazine, bookstore, endowment, mission, intake. |

### The seventeen modules, as the Map badges them

| Module | Map status | Hub today |
|---|---|---|
| Front door — join, sign in, recover, refresh | Designed | **Join services built; screens: 2 of 5 ported** |
| Federation operations (grants, refusals) | Built | `reporting` on `is_staff`; **exact-grant model not built** |
| Membership, household & identity | Built | Membership ✅ · household authority model ❌ · merge queue ❌ |
| Money, giving & finance | Built | `payments` + `funds` ✅ · **daily close, gross-fee journals, remittance liability ❌** |
| Events & calendar | Built | `events` ✅ · event builder ❌ · QR check-in ❌ |
| Governance & elections | Built | `voting` ✅ (the strongest module) · mailed CPA ballot ❌ · board workspace ❌ |
| Clubs & local club systems | Built · partial | `clubs` back office ✅ · registry/health/migration ❌ |
| Family tree | Built | `tree` ✅ — GEDCOM in the file's own shape, hourglass, line & evidence packet, corrections queue, committee console (6 Sep 2026) |
| Life events — add, approve, release | Built | ❌ |
| Community — the two directories | Designed | `memberdir` ✅ · `network` (RBPN) ✅ · household-level inclusion ❌ |
| Hathihe Ramallah, bookstore & ads desk | Designed | ❌ |
| Programmes — six sections, charters | Designed | `programs` seven-station shape ✅ · charters/registry ❌ |
| The integrated progression (Pathways) | Designed | ladder ✅ · invitations/inbox ❌ |
| The Convention | Proposed | ❌ |
| Scholarship (ARFECF) | Built | roll entries only; **committee, median ranking, conflicts, budget ❌** |
| Endowment fund | Designed | ❌ |
| Medical Mission · Human services intake · Governance interlock (ARFHSN) | Designed | ❌ |
| Institution registry | Proposed | `bylaws` entities/franchises ✅ · registry screens ❌ |

**Where the Hub is strong:** the rules. Sixteen apps, 508 tests, the PCI
boundary, R7, Decision 28, scoped standing, sealed ballots, the by-law
register with 48 overrides. Where it is weak: **screens** (3 of 58 ported) and
**five backend modules the design calls Built** that the Hub never got — the
ledger's daily close, the identity merge queue, life events, the household
authority model, and the scholarship committee. All five have a reference
implementation in `AFRP-Portal/src` to port from.

---

## 2. The rules the plan obeys

From the Build Spec and the project's own discipline. These are the
definition of done for every screen, not aspirations:

- **Mobile first.** Design at < 560px, single column, bottom tab bar; persistent
  left nav from 900px; two-column only on dashboards ≥ 1120px. Forms never wider
  than 640px.
- **The accessibility gate (WCAG 2.2 AA).** Touch targets ≥ 48px (44 absolute
  floor). Inputs ≥ 16px so iOS does not zoom. Every input a real `<label for>`.
  Visible `:focus-visible`. Contrast ≥ 4.5:1. Errors in text, never colour alone.
  **No horizontal scroll at 320px — enforced by a CI test that walks every route.**
- **Prototype is the record.** Every screen matches its `data-route` in
  `prototype.html`: same panels, same copy, same rule named in the foot. The
  stylesheet is the prototype's, verbatim; `app.css` carries only what the
  server needs.
- **Refusals name the rule** (S6). Where the by-laws are silent the screen
  flags OPEN and routes to the committee (R40). No defaults.
- **Nothing invented.** Real clubs, real programmes, real by-law text. People
  and money are the synthetic fixture.
- **Each slice: build → red-team → fix → audit the fix layer → push → CI green
  → visible on staging.** A slice is not done until the page has been opened.

---

## 3. The plan, in phases

Ordered so that each phase leaves a **usable, reviewable lens** on staging, and
so the audiences arrive in the order they exist: members first, the officers
who serve them second, the staff who serve both third, programme leads last.

### Phase 0 — Finish the shell · 1 slice

The shell is ported but the prototype's frame is richer than what is there.

- Breakpoints per the Build Spec: bottom tab bar below 560px; sidebar groups
  per lens with counts; theme toggle in the topbar.
- The page-head icon tile, breadcrumbs, the **stat tile** row (big number,
  caps label, the explanatory line that names the by-law), the **role chip**
  (who you are acting as).
- The **320px horizontal-overflow CI test** across every route.
- Load the 500-household fixture onto staging so every later screen has data.

### Phase 1 — The front door, complete · 2 slices · 5 screens

| Screen | Backend | State |
|---|---|---|
| Landing | none | ✅ ported |
| Sign in | `accounts` | ✅ ported |
| **Join — the seven-step wizard** | `join` services exist | port the screen; family branch; postal address at checkout |
| **Recover access** | new: two paths, 72-hour undo, 7-day both-lost | build |
| **18th-birthday refresh** | new: the 90-day window, consent moves to her own channel | build |

### Phase 2 — The member lens · 4 slices · 14 screens

The fixture makes this lens worth looking at: 1,571 people, 2,704 charges.

| Screen | Backend | Work |
|---|---|---|
| Home | `member` ✅ | **ported (2a)** — attention list, coming up, the two standing pills |
| Membership & household | `dues` ✅ · **household authority ❌** | **ported (2a)**; `can_transact_for` still to build |
| Payments & giving | `payments` ✅ | **ported (2a)** |
| Household | **authority model ❌** | **refused (2d)** — R6 "who may act for a minor" is *inferred* in the Rules Register, stated by no document; two questions sit with the Membership Committee, Camp Ramallah and the Legal Advisor. Not built until one is on disk. |
| An event / Events | `events` ✅ | **ported (2b)** — register self; household waits on the authority model |
| Your ballot | `voting` ✅ | **built (2c)** — choose / confirm / sealed, receipt once, refusal shown not hidden |
| My programmes | `programs` ✅ | **ported (2b)** — eligibility stated from the charter |
| Your club | `clubs` ✅ | **ported (2b)** |
| RBPN | `network` ✅ | **ported (2b)** — storefront read view; buying and asking wait on the desk |
| Inbox | gathered live from the modules | **built (2d)** — every notice with its class; invitations answered here; mute is a dated consent row |
| My pathway | `programs.rails` · invitations ✅ | **built (2d)** — four rails over the register; ask → invitation → inbox → enrolment |
| Magazine · Bookstore · Ads desk | ❌ | member-side read views first; ops in Phase 5 |
| Directory & disclosure | `memberdir` ✅ | **ported (2c)** — withheld fields named; capped fields offer no public |
| ~~Family tree~~ · ~~Guided scenarios~~ | — | deferred / prototype-only |

### Phase 3 — The club lens · 2 slices · 6 screens

| Screen | Backend | Work |
|---|---|---|
| Club dashboard | `clubs` ✅ | **ported (3a)** — stat tiles; affiliation form, ruleset check and migration named unbuilt |
| Roster — two status columns | `clubs` ✅ | **ported (3a)** — sorted by household; 13.2 warning on a lapsed officer |
| Households | authority model (Phase 2) | **refused** with the household slice — R6 inferred, no document |
| Officers & affiliation | `clubs` roster ✅ · `AffiliationFiling` ✅ | **built (3b)** — the filing recorded (3.2 deadline, 6.4.1 effect); the form’s content is unspecified and not held |
| Communications — consent-filtered | `clubs.ClubMailing` ✅ | **built (3b)** — roster − no consent − no address; the withheld stored by name with the mailing |
| Club voting | `voting` ✅ (federation only) | **refused (3b)** — no club electorate or club ruleset in the engine; the ballot page says so |

### Between the lenses — switches for a staging site

| Switch | Default | What it does |
|---|---|---|
| `BUILD_NOTES` | off | shows the "not built / later slice / this build" commentary on the screens, for builders; a member never sees it |
| `SHOW_SIGNIN_CODE` | off | puts the one-time code on the code page; breaks existence-blindness on purpose, staging only, warned at startup |

### Phase 4 — The federation lens · 6 slices · 16 screens

The heaviest phase. Three backend modules port from `AFRP-Portal/src`.

| Screen | Backend | Work |
|---|---|---|
| Federation dashboard | `reporting` ✅ | **ported (4a)** — tiles read filings, the latest roll and the merge queue; open items; the entity map |
| People — Member 360 | `identity` ✅ | **built (4g)** — resolve.ts ported verbatim (weights, blocking, thresholds); a scan puts scored pairs with reasons on the queue; Member 360 shows every row that references a person with standing computed live, addresses masked without member:pii:read at the exact scope, money only with giving:read; a merge re-points every reference, collapses a shared channel, leaves frozen rolls, closes the loser as merged (never deleted) with the map of what moved; refuses a conflicting DOB, a death, two accounts, a collision. The Hub does not auto-merge above 0.95: a person confirms. Support desk (tab 3) is later |
| Money — one ledger | `ledger` ✅ | **built (4i)** — posting.ts and remittance.ts ported (integer cents): the daily close over the Hub's charges — dues, gifts by purpose, club dues as a liability (R21) — fees gross (R20; a charge with no fee reported refuses the close), reversals as their own entries (R24), one frozen batch per day/fund/kind with a deterministic doc number (R22), a second close refused; the remittance run as a statement with carry-forward and fee policy; **approval refused** because sign-off (§8.7) and the CPA's agency answer (§7.1) are not on file. Controls, QuickBooks connection, endowment distribution: later |
| Election · Results | `voting` ✅ | **built (4b)** — the console: draft, certify (shares shown once), open, close, count with two shares, result with its arithmetic and hash; merge queue listed as the gate |
| Live floor | `voting` floor ✅ | **built (4d)** — seat delegations, extract, put and open a question, record hands, close and reconcile exactly; the two-thirds bar shown, the chair rules the type |
| Ruleset workbench | `bylaws` ✅ | **built (4e)** — the version chain per entity (nothing governs today, and the screen says so), verification and ratification recorded with a person and a date, the 48-override ratification agenda heaviest first, rule-by-rule divergence with the design record's cost tiers, the floor from the engine's own table. Not built: the parallel run (re-evaluating last cycle under a draft) — the engine has no such evaluator |
| Governance — board workspace | **no design document on disk** | not built, and said so: `AFRP-Portal/src/governance/` holds the ballot and eligibility engines (already `voting`), nothing for motions or minutes; the override ratification queue lives on the workbench (4e). Refer to the record before inferring |
| Roles & permissions | `access` ✅ | **built (4f)** — policy.ts ported verbatim: (person, role, scope), fifteen roles, seven exact-scope permissions (board-confidential included, carried by no role yet); grants ended never deleted, derived ex officio; the federation gate is now `requires(permission)` on every screen and the staff flag opens only the admin; the refusal names the permission, the scope, what is held and what opens. Not built: the interlock cap (needs a Board-membership role the vocabulary lacks) |
| Communications centre | `comms` ✅ | **built (4h)** — the club filter lifted into one function both scopes run; audience = resolved national records (current standing, or any on file) minus no consent minus no verified address; undeliverable shown as not tracked, not zero; every send stores the withheld by name; gated on message:send |
| Clubs — registry & health | `registry` ✅ | **built (4c)** — the registry: charter, dormancy with its reason, delete refused by name; health tiles on the dashboard |
| Institutions | `funds.Entity` ✅ | **built (4c)** — the entity registry; partner vs administered; the nine-tab record is later |
| Events console + builder | `events` ✅ | **built (4c)** — create, publish, cancel; one scope per event; tiered pricing and the six-step builder are later |
| Convention | **❌** | registration, delegate status, command centre — scoped separately |
| Directory (management scale) | `memberdir` ✅ | **ported (4a)** — coverage through the directory gate; the export refusal by the same button |
| The fixture · Every screen | — | port (staging only) |
| ~~The CRM today~~ · ~~Family tree~~ | — | static / deferred |

### Phase 5 — The programme lens · 5 slices · 12 screens

| Screen | Backend | Work |
|---|---|---|
| Programmes overview · Lifecycle · Registry · Programme | `programs` ✅ | **built (5a)** — the programme lens: overview over the register with suppressed pipeline counts; the eight-stage lifecycle with the three stage-conversion queries computed, not placeholders; the registry as versioned data — five statuses, dated and attributed transitions, install from a template born proposed, the Award retired as the record says; the programme record with cohort (names only with roster:read at the programme), ladder, charter, committee and history. Gated on program:read at any scope; a chair sees their own programme |
| **Scholarship applications** | **scholarships/*.ts → ❌** | build: median ranking, three-degree conflicts (S6), encumbrance, named awards |
| Alumni & recruiting | ❌ | build match queue (tree tracing deferred) |
| Magazine operations | ❌ | build: copy freeze, auto sections, statutory notices, death held for family |
| Bookstore operations | ❌ | build: catalogue, member pricing, sale never a gift |
| RBPN & sponsorship | `network` ✅ | port |
| Endowment | ❌ | build **flagged** — pending the Policy Statement |
| Medical Mission ops · Human services intake | ❌ | build with the entity banner; intake is a separate store, exact grants only |
| Senior Living campaign | ❌ | pledges vs cash; restricted and ring-fenced |

---

## 4. The size of it

| Phase | Slices | Screens | New backend |
|---|---|---|---|
| 0 Shell | 1 | — | overflow test |
| 1 Front door | 2 | 5 | recovery, refresh |
| 2 Member | 4 | 14 | household authority, inbox, invitations |
| 3 Club | 2 | 6 | affiliation form, consent filter |
| 4 Federation | 6 | 16 | merge queue, ledger, grants, board workspace, registry, builder |
| 5 Programme | 5 | 12 | scholarship, magazine, bookstore, endowment, mission, intake |
| **Total** | **20** | **53** | |

Twenty slices. A slice is one session: built, attacked, fixed, audited,
pushed, opened in a browser. The prototype took twenty-plus days of design
and sixteen red-team rounds; the build is proportionate, and pretending
otherwise is how the first sixteen modules ended up with three screens.

**Deferred, by decision:** the Convention as its own element. The family
tree was deferred here and then un-deferred by David on 6 September 2026
("make a family tree using the same format"); it is built in §5 below.
Tree tracing in alumni and conflicts still waits on member links.

---

## 5. What I will not do

- Decide an open question. Same-sex spouse under 4.1.1, a minor in two
  households, the grace parameter, agency-vs-revenue for club dues — each
  screen flags them OPEN and routes them. R40.
- Invent a screen the prototype does not have, or a rule the record does not
  cite.
- Widen the PCI boundary, touch the integrity floor, or put a real person in
  the fixture.
- Call anything done that has not been opened in a browser at 320px and 1280px.

---

## 6. Decisions — 5 September 2026

David answered four of the five:

| Question | Decision |
|---|---|
| Order after the member lens | **Club → Federation → Programme** — the order the audiences exist in |
| Backend depth | **Screens over existing data first; the five engines as their own slices after.** A panel that needs an engine says so on the screen rather than pretending |
| The Convention | **After the twenty.** A project, not a screen |
| Review cadence | **Once per phase, on staging.** A whole lens, judged whole |
| Email | *open* — console backend for now; the join wizard cannot be tested end to end until a provider exists |

**What that changes in §3.** Phases 4 and 5 split: the screens ship in-phase
over existing data, and the engines — ledger, merge queue, exact grants, board
workspace, scholarship committee — become slices 21–25, each red-teamed alone.
The twenty become **twenty-five**, and every lens is visible sooner.

## 7. The questions as they were asked

1. **Order after the member lens.** Club → Federation → Programme is the
   order the audiences exist in. You are the federation administrator; you may
   want Federation second so you can run the thing.
2. **Backend depth.** Phases 4 and 5 carry five modules the design calls Built
   that the Hub never got. Port them fully from `AFRP-Portal/src`, or put
   screens over existing data first and build the engines as their own slices?
3. **The Convention.** Proposed in the Map, 12 panels in the prototype, and
   its own deep dive. In the twenty, or after?
4. **Review cadence.** One review per phase on staging, or per slice?
5. **Email.** Codes in the Render logs, or a transactional provider so you can
   sign in without me?


## 5. Scheduled by David's answers of 6 September 2026

| Slice | From | Work |
|---|---|---|
| **Role vocabulary as data** | answers 9, 12, 14, 15 | roles become editable rows (name, permissions), seeded from policy.ts plus the Executive Committee titles at https://afrp.org/about-us/executive-committee/ and a committee-chair role; board-confidential carried by the Executive Committee and committee chairs; the Roles screen edits them. The people themselves are entered by an admin, never seeded |
| **Programme charter edit** — built | answer 7 | `lifecycle.amend` on the programme's record page under `program:manage` at that programme: name, host, template, stage, mission, band, flags, metrics; validated as install validates, one transaction, refused when nothing changes; one attributed `CharterEdit` (before, after, authority, who) per changed field; the key never changes and status moves by transition |
| **Dues schedule and incentives** — built | answer 5 (addendum) | `dues.DuesSchedule`: versioned rows (individual, family, patron, student, club; effective date; authority; who), never edited or deleted; `price_for(tier, on)` prices a term by the schedule in force on its collection date and refuses to guess before the first; `dues.DuesIncentive`: the kinds the platform knows (graduation, newlywed) switched on or off with free years and an authority; renew and join read both; the Money screen sets them under `dues:write`; the renewal screen shows the schedule in force and a free year when one applies |
| **Voting suspension** — built | answer 3 | `voting.Suspension` (person, from, until inclusive or until lifted, authority required, recorded by); `eligible_people` and `why_not_eligible` read it at the record date; a certified roll stays frozen; the People registry withholds and lifts the vote, each with its authority or reason; never deleted, never for the dead |
| **Governance: the seven committees** | answer 8 | committee rows and seats under the federation lens; needs a design note first (no document on disk) |
| **Upload-and-draft rulesets** | answer 10 | upload a governing document, draft a ruleset with a language model's help, admin edits, verification blind to the draft, ratification as built; a draft can be discarded, a ratified text never |
| **The family tree** — built | answers 22, 23; the GEDCOM David pointed at | `tree`: a reader and writer for the Family Tree Maker export (GEDCOM 5.5 lineage-linked, patronymic chains, `_FREL/_MREL`, `_MEND`, `_SCHEMA`, CONC/CONT, ANSI) that puts the file back line for line in its own order; every import a version, links carried by xref; the hourglass, the father's line to the top with per-link confidence and the evidence packet (UNDETERMINED, never a verdict); search; any member proposes, the committee decides from a triaged queue in sittings with a blast radius; import and export under `tree:moderate` (the `family_tree_committee` role); "paid members see everything" as one setting, `tree.policy.LIVING_VISIBLE_TO`; signed out, the deceased only. The committee's file lives on private storage, never in the repository; `seed_tree` makes a synthetic one of the same shape. 880 tests |
| **Decision 1, consequence C** — built | AFRP-Decisions-Register Decision 1 | club-collected national dues booked by the daily close as a receivable from the collecting club at collection (Dr Due from local clubs, class the club / Cr Membership dues), settled when the club marks them remitted (Dr Cash / Cr Due from), adjusted on reversal (F: out of the receivable while unremitted, out of cash once remitted); the club's own dues taken in person stay off AFRP's books (treatment 2); the close records the day's receivable and settlements and the Money screen shows them. The account number is the platform's placeholder on the prototype's chart until the QuickBooks mapping |
| **Rules as data** — built | David, 6 Sep 2026: "do not hardcode rules" | `rules`: the register of every parameter the by-laws set (AFRP-Bylaw-Flexibility §1, Tier 1 and Tier 2) as versioned rows with an effective date and an authority — a by-law citation, a Board minute, an executive order, or a proposal; the engines read the row in force (grace, the join minimum age, the floor's amendment threshold, the refresh window, the recovery delay, the tree's living horizon, the renewal screen's membership year); a silent or self-contradicting text is "not set" and a read refuses by citation; a parameter nobody reads yet is "declared" so the inventory is whole; the Rules & parameters screen sets a value under `rules:set` (platform admin, President, Recording Secretary, Legal Advisor). The integrity floor and the suppression floor stay out of reach by design |
| **Phase 6 — the public site** — first cut built | answer 1; David, 6 Sep 2026: "as much from the afrp.org website in the public-facing site" | `website`: the public site at the root on its own template (afrp.org's five sections, hero, footer; the design system's stylesheet); 33 pages seeded from afrp.org's own texts (`website/seed/afrp_org`, each with its source and fetch date, people's names stripped; testimonials, staff lists and news never seeded); programmes from the registry joined to their pages; clubs from the register; the Executive Committee from grants by title; announcements between dates; news posts an admin writes; the Website desk on the federation lens under `site:edit` (settings, pages with a safe small markdown and a preview, announcements, news, re-seed that keeps edited pages). The sign-in door moved to /welcome/. Design document still owed: this is the structure of afrp.org on the platform's template, not a redesign |
