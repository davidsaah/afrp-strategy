# AFRP master plan — everything to date, and the build-out from here

**8 September 2026 · the consolidation.** One document a fresh Claude session
can execute from: it lives at `docs/MASTER-PLAN.md` in AFRP-Hub, inventories
what exists, orders what remains into one track, and states what only David
can unblock. It was red-teamed before adoption (three adversarial lanes,
22 findings, §4); every confirmed finding is folded in below, and six were
code defects in the evaluation loop itself, fixed and locked with tests in
the same round.

---

## 1. What exists today — the four assets

### 1a. The application — `davidsaah/AFRP-Hub` (private)

Django 5 · PostgreSQL (sqlite in dev) · server-rendered · passwordless ·
**25 first-party apps · 979 tests green · CI green on `8ad0012`.** Built and
red-teamed: the front door (join wizard, sign-in, recovery, 18th-birthday
refresh), the member lens, the club lens, the federation lens whole
(dashboard, elections console, live floor, ruleset workbench with the 48
overrides, roles/exact grants, Member 360 + merge queue, the one ledger with
daily close and receivables, comms, registries, rules-as-data, website desk,
store desk), the programme lens (5a), the family tree (GEDCOM round-trip,
hourglass, committee queue), the public site unified on the design system
with the prototype's own symbology, and the bookstore. 100+ defects found
and fixed across the rounds; the fix-layer audit is standing practice.
Deployment: `render.yaml`, `Procfile`, `docs/DEPLOYING.md`, a staging
instance with the 500-household fixture loaded.

**Refused by design, correctly:** ~~household authority~~ (**no longer refused
as of 8 Sep** — R6 is ratified and `AFRP-R6-Minor-Authority.md` is the design
record; the standing refusals in camp, the member-lens household screen, the
club-lens households row and family event registration are now **stale text to
remove in slice 2b**, not correct behaviour), club voting (no club electorate in the engine), board workspace and the
seven committees (no design note), remittance approval (sign-off §8.7 and
the CPA answer not on file), affiliation form content (unspecified).

**Simulated or absent:** Authorize.Net (simulated, with a production guard),
email (console backend — a stranger cannot finish the join wizard),
scholarship committee engine, magazine operations, camp screens, alumni
matching, endowment (flagged pending its Policy Statement), Medical Mission
ops + human-services intake, Senior Living, the Convention element, the
mailed CPA ballot, QuickBooks, support desk.

### 1b. The evaluation layer — `journeys/` (in AFRP-Hub)

Slice J1 built, hardened twice (its own red-team round, then this plan's):
spec schema, deterministic-per-database persona predicates, a rolled-back
runner, staged scenarios with an honesty contract, the five-class rating
(5 MEETS · 4 GUARDED · 3 OPEN · 2 NOT BUILT · 0 FAILS — a refusal naming
its rule is a PASS), and `run_journeys`. **The catalogue,
`journeys/catalog.yaml`: 326 journeys** across five lenses × 19 programmes ×
seven kinds; 18 runnable today (8 · 2 · 1 · 7 · 0). The loop now refuses
the moves that would let it lie: an orphan spec, a spec whose `expected`
differs from its catalogue row, a previously-run row whose spec was
deleted, a spec that asserts nothing, a routes-open claim with no evidence;
a filtered run writes `scoped.md` and never touches the report of record; a
crashed view is a FAILS row, not an abort; a persona the fixture cannot
supply reports as `fixture-gap`, never as a Hub defect; and every report is
stamped with its database, seeded population, and commit. **The staging run
is the report of record; a dev run is a preview.** The workbench (claude.ai
artifact "AFRP Analyst Dashboard") shows catalogue + results and queues
analyst proposals; `journeys/WORKBENCH.md` is the apply contract, and the
page's source template ships in `journeys/workbench/` so any session can
rebuild it.

### 1c. The design record — the source of truth

`AFRP-Portal/docs/design/` (31 documents, incl. the Decisions Register: 29
decisions answered, D5 reopened), `davidsaah/afrp-mockups` (public:
prototype, Platform Map, Complete Platform, five deep dives, the fixture),
and `ai-memory/` (00–10 + prompts). The Claude Project mirrors key
documents for Cowork sessions; **anything a build session must obey is a
file in the repo, never only in the Project.**

### 1d. The blockers only David can move

1. **CPA countersignature** on Decision 1 — until then remittance approval
   rightly refuses.
2. **Five missing documents:** Endowment Fund Policy Statement · 2015
   Scholarship Fund Policy Statement · ARFECF determination letter · Board
   Rules & Regulations · clean ARFECF 2013 text + ARFHSN trustee roster.
3. ~~**The R6 document** (who may act for a minor).~~ **CLOSED 8 Sep 2026.**
   `AFRP-Portal/docs/design/AFRP-R6-Minor-Authority.md` is on disk and
   **ratified as drafted, without amendment**, by the Membership Committee,
   Camp Ramallah and the Legal Advisor; the rules register grades R6
   **attested**. Household authority, family event registration and camp's
   minor-authority surfaces are ordinary build work — **slice 2b** — and the
   refusals that stood for want of it lift. No provisional labels: this is a
   rule now, not a proposal.
4. **Decision 5** (the two 9.1.3 drafts) — genuinely open.
5. **The grace parameter** (90 days proposed) and directory grace.
6. **Credentials:** an Authorize.Net account; an email provider
   (Postmark / SES / Resend).
7. **The public site is built; launching it is not.** The site and its
   admin desk shipped 6–7 Sep (33 pages from afrp.org with their sources,
   the Website desk under `site:edit`, the design layer) — Q1 of
   `docs/QUESTIONS-FOR-DAVID.md` is delivered and needs no phase. What
   remains is David's: **DNS pointed at it**, a **content review of the 33
   seeded pages** (they are afrp.org's own text, fetched, with every
   living person stripped — so the site currently names nobody), and
   **entering the real Executive Committee** on the People registry with
   their grants, since the page renders from grants and seeds no names
   (Q2). The four remaining programme pages are slice 6's, not a blocker.
8. **Staging lifecycle:** the free Render Postgres expires on its fixed
   window and has no backups — decide upgrade-vs-recreate before it lapses;
   fixture reloads run from David's laptop per `docs/DEPLOYING.md`.

---

## 2. The build-out — one interleaved track

One slice per Claude session; the four-step loop every time (build →
red-team → fix → audit the fix layer → push → CI green → visible on
staging). **CI green is necessary and is not sufficient: a
slice is not done until the staging deploy is LIVE on the pushed commit, and
the DONE row names the deploy it verified.** That last step was in this
sentence and was not being checked — staging was down from 8 Sep 00:23 through
four slices, each of which reported itself finished. **Serialize sessions in the one working tree** — before starting
a slice, commit and push a `[STARTED]` row for it in
`ai-memory/09-SESSION-LOG.md`; a slice with a pushed STARTED row and no
finish row is taken. Do not run parallel clones: every slice touches
`catalog.yaml` and the session log, and clones collide at merge in exactly
those files.

| # | Slice | Stream | What it is | Exit test |
|---|---|---|---|---|
| 0 | **Reconcile & wire the loop** | ops | `git status`; commit whatever of journeys J1 + catalogue + workbench + this plan is not yet committed; add the **journeys CI job (reporting, non-blocking)** with its data recipe — checkout afrp-mockups beside the repo, migrate, seed_clubs/programs/bylaws/rules/site/tree, `seed_fixture`, `run_journeys` — and keep render.yaml's startCommand in step with any new seeds. | CI green on the pushed commit **including** the journeys job's report; catalogue reconciles; `docs/MASTER-PLAN.md` on disk. |
| 1 | **J2 — door + member corpus** | eval | Author specs for every JD-*/JM-* row; extend personas; add scenarios the rows name; red-team the new specs. | Every JD/JM row runnable; each observed class equals its catalogue class or is raised as a finding — the refusal machinery (not good intentions) blocks editing one away. |
| 2 | **Camp screens** | build | Parent application, selection console, roster, camperships — the tested engine gets its screens per the deep dive. **R6 landed 8 Sep (provisional):** minor-authority rows (the parent applying for the camper, parent visibility, pickup) now build against `AFRP-R6-Minor-Authority.md` — its four paths and seven powers, the release list writable only by a standing holder — and every derived rule carries the provisional label naming that document. Cases §4/§6 leave open refuse under R40. | All **12** camp NOT-BUILT rows accounted for: flipped to their real class, or refusing-correctly-naming-R6-or-R40. Nothing minor-authority ships unlabelled. |
| 2b | **Household authority — the ratified R6** | build | The model three slices deferred: the four paths (parent by household, named guardian, either separated parent, per-event delegate), the seven powers as least-privilege grants, `can_transact_for`, supervision disclosed while the release list stays writable only by a standing holder, recorded restrictions overriding every path, lapse at eighteen and at event end, every exercise logged. Then the surfaces it was blocking: the member-lens household screen, the club-lens households row, family event registration, and camp's application. **Removes** the stale R6 refusal text in `camp/views.py` (it claims R6 is inferred and undocumented — false twice over). | The previously-refused household rows and camp's minor-authority rows flip to their real class; **J07 and JP-009 stop being GUARDED**; no surface anywhere still says R6 is unstated or unratified; the CIT refusal still stands and a test asserts it survives; R7 and the directory gate untouched, with the payload walk still refusing to serve on a leak. |
| 3 | **J3 — club + federation corpus** | eval | JC-*/JF-* rows; scenarios: post-remittance-chargeback, dormant-club-midyear, floor-session. | Rows runnable; D1 consequences A–G each land as the record says. |
| T1a | **The branches** | build | The `rails` → `branches` rename **and** the re-cut in one move (D38–D40): four branches each declaring a shape — Education (ladder by age), Leadership (ladder by capacity), Heritage (cluster), Care (destinations) — the tree lifted out to the **roots** beneath all four, the Convention as the **junction** on no branch, and the Ramallah Foundation and Endowed Fund **shown but not joinable**. Renaming without re-cutting would leave the old groupings under new names. | JM-103, JM-104, JM-106, JM-107, JM-108, JP-080, JP-081, JP-082 runnable and landing where the record says; **JM-104 asserts an absence** — no milestone invitation inside a cluster branch; no surface names the old rails. |
| T1d | **The family tree joins Heritage** | build | D53: move the tree from the roots beneath the four branches onto the Heritage branch (a cluster: no next step, no milestone invitation), alongside Preservation, the magazine and the bookstore. D30's node per member is untouched. Update `programs/branches.py`, the `/me/branches/` screen and the journeys that assert the roots. | The tree appears on Heritage on `/me/branches/`; no surface calls it the roots; JM-104 still holds for the cluster; D30 rows unchanged. |
| T1b | **The node and the life events** | build | D30's node on every member (never a lineage claim, no membership decision reads it), the life-event pipeline queueing to the committee under D31 with **R6 as the gate**, announcements on D33's consent, and the divorce and blended-family rules of §6 — including the one that carries the slice: a step or adoptive link can never produce a 4.1.1 path. | The T1b rows runnable; **JD-009 and JD-010 clear** — the two door rows rated 0 since slice 1; **JM-098** holds; R7 and the directory gate untouched. |
| T1c | **The committee and the mailings** | build | The third decision state (*needs information*, request stays open), the **diff preview before any GEDCOM import** with the never-delete and stale-export guards, committee direct edits audited under D12, and gap-filling and story mailings to members about **their own branch only** (D36). | The T1c rows runnable; **JF-106** refuses a stale-export import; **JF-108** cannot express a non-member recipient; **JM-099** suppresses a restricted name without saying why. |
| 4 | **Scholarship committee engine** | build | Median ranking, three-degree conflicts, encumbrance, named awards, ARFECF boundaries (6.3.8/6.4.x refuse by name). | Scholarship rows flip. |
| 4b | **The committee's number, the relationship disclosed, and the boot that refused itself** | build | Four corrections David took on 8 Sep, plus an outage nothing was watching. **The award budget is entered by the committee** from a report they receive, with a source and an as-of date — the platform records, shows and warns, and never computes 5% of anything (EC-OV-6 retired as `superseded-by-decision`). **The three-degree bar comes out**: every relationship the tree can see is disclosed with its degree and acknowledged on the record; only same household still refuses. **Non-floor refusals gain a logged override** that lands on the ratification agenda; the integrity floor, R7, D28, consent, death-at-save, rule 2, rule 8 and `bootstrap_officer`'s revoked-grant refusal are not overridable. **Dev moves to PostgreSQL** with a check banning literal-pk and JSON-key-order assertions. And **`bootstrap_officer` stops taking staging down**: its revoked-grant refusal is right and is `&&`-chained ahead of gunicorn, so twenty consecutive deploys since `2cdb42e6` failed while CI stayed green. | The staging deploy is **live on the pushed commit**; no code computes a draw; the disclosure carries its degree and the undetectable case still says so; a test asserts each non-overridable refusal has no override route; green on PostgreSQL locally and on CI with the pk/ordering check proven able to fail. |
| 4c | **The boot, properly: a guard that fires on correctness, and a grant nobody can restore** | build | Three things 4b could not see from inside the repository, read off the live service and its database: **`seed_bylaws`'s guard conflates an override born adopted with one that left provisional through a recorded transition** — EC-OV-6, retired by decision on purpose, now trips it on every boot; **the 26ca390 deploy reached live while one instance raised** — establish from the logs whether two instances raced or one was stale, correct or confirm `render.yaml`'s single-instance claim, and lock every release step's classification to its real behaviour on failure; **the real lockout** — one live grant on the whole system and nobody holding `role:grant` anywhere, so `restore_grant` is exercised against staging for the first time, the two-character `ended_reason` that ended the only administrative grant found and refused; and **the staging database's 5 October expiry** put on the record with what is lost and what a seed rebuilds. | `seed_bylaws` clean against the current register and still refusing a planted born-adopted override; §2's explanation established and written down; a test locks each step's classification; `platform_admin` restored through the break-glass on staging, acknowledged, and a second unacknowledged run refused; the expiry on the open-questions register; **the deploy LIVE on the pushed commit with no instance raising.** |
| 4d | **The release chain moves to preDeploy** | ops · small | Starter makes `preDeployCommand` available, so the release work stops running at boot: migrations and seeds run once, after the build and before traffic switches, instead of on every instance start. Its own slice because `afrp.release.start_command()` and `afrp.tests_deploy` follow the chain and both change with it — and because the boot classification from 4b (a step that refuses and continues versus one that stops) has to be re-stated for a phase that runs before anything serves. **Not urgent**: no spin-down on Starter means the overlap that produced the split boot cannot recur on this service. | The release chain runs in preDeploy; `render.yaml`, `afrp/release.py`, `CLAUDE.md` and `docs/DEPLOYING.md` agree and a test refuses the suite if they drift; the deploy is live with the seeds having run exactly once. |
| 5 | **Email provider, then payments-for-real** | build · **gated on §1d.6** | The provider behind the existing service boundary; Authorize.Net behind `payments.gateway`; SAQ A-EP preserved. | A stranger walks the join wizard end-to-end on staging; the vault-expiry defect class re-attacked. |
| 6 | **J4 — programme corpus + branches** | eval | JP-* rows; every programme reachable; the four branches end-to-end (D38–D40) with each shape asserted. | Rows runnable; the programme rollup complete. |
| 7 | **Magazine operations** | build | Copy freeze, family-proofed sections, statutory notices with the 60-day clock, death held for family. | Magazine rows flip. |
| 7b | **The magazine review: four answers, two corrections** | build · small | The review of slice 7's ten decisions coming back. **Two corrections**: the family tree highlight selected the surname with the most deceased individuals — a static ranking that prints the same line every issue and that no test can notice moving — and becomes the line most recently accepted by the committee in the content window, absent and saying so when none was; and it gated living names on the directory queryset, which is the members-only screen gate, where the record says print is its own switch and an unwithdrawable purpose of its own. **Four answers from David**: Manar is a real recognition tier, attested, so the register was what was incomplete and 38 names were being silently dropped; the five-versus-six section count goes to the magazine committee with both prototype citations; the delivery allowance becomes a register row with no value that refuses rather than assuming seven days; no embargo on the archive, closed with its reasoning. Plus the three print consents surfaced on `/me/` so members can grant a switch they can currently only fail to have, and consent read at the freeze because it is withdrawable until then. | The highlight moves with the committee and is absent when nothing was accepted; a print consent is required for a living name; both tiers print with the count derived; the activities section refuses while the allowance is unset; the consents are on `/me/`; grant → assemble → withdraw → freeze leaves the name out. |
| R1 | **The record audit** | ops · small | A Cowork audit of every record file against what the build actually is, 10 Sep 2026. **`05-MODULE-MAP.md` still says "Sixteen Django apps, 508 tests" and names none of `magazine`, `scholarship`, `authority`, `tree` or `access`** — four of which carry binding rules — and `ARCHITECTURE.md` froze at the same number. **`09-SESSION-LOG.md`'s preamble still says 508 tests**, the exact figure CLAUDE.md holds up as this project's cautionary tale. `README.md` carries a fifth copy of the test count at 1,174, says round 27 where the ledger holds 29, and dates itself 8 Sep. **Three `-1` duplicate files** — of the master plan, the open questions and the questions register — sit in the tree where a grep cannot tell them from the originals. And `06-ENVIRONMENT.md` says the runs moved to PostgreSQL while `latest.json`'s own provenance reads `database sqlite3`, which slice 8's gate depends on. | The map names every app and its entry points; the test count lives in one place or a check fails when copies disagree; the log's preamble holds no stale number; the `-1` files are gone and how they arrive is written down; the PostgreSQL question is settled **before** slice 8 builds a gate on it. |
| 8 | **J5 — attack the corpus; CI blocks** | eval | The mutation pass (three binding rules broken on a scratch branch; the corpus must catch all three); then flip the existing journeys CI job from reporting to blocking. | All three mutations caught; CI red on a planted fail, then reverted. |
| 9 | **Alumni matching** | build | The match queue, consent-gated like every surface. | Its rows flip. |
| 10 | **RBPN ops + job board port** | build | Sponsorship desk; the job board with its universal salary fields. | Its rows flip. |
| A1 | **The abstraction pass** | build · structural | Six concepts the platform implements independently between four and six times each, found by reading the ledger against the module map. **(A) Decide from the database at the moment of decision** — four instances in the ledger (`LivingGuardedModel`, the stale export, the chair's household, the dead owner), four fixes, no shared mechanism. **(B) Freeze a derived set at a named moment and stamp it** — six implementations: the record roll, the ruleset stamp, delegate weights, the magazine's bespoke `Section.save`, the award budget's as-of date, recognition consent at freeze. **(C) An unset parameter refuses and names its authority** — five parameters, hand-written each time, and the by-law revision is bringing more. **(D) A refusal is an object, not a sentence** — the class behind JF-086 and its predecessors, where a refusal was satisfied by the page's own furniture. **(E) Small-cell suppression** — verify whether every caller uses `suppress_small` or some re-derive it. **(F) No document states a number it cannot derive** — eight places, one fault; `tests_record` becomes a registry of (document, claim, derivation). | The plan and evaluation strategy are in the STARTED row before any code; for each concept taken, a mutation reintroducing the old fault **in a module that never had it** goes red; every migrated caller keeps its lock; moved enforcement sites updated in 01-BINDING-RULES in the same commit; nothing in the Tier-4 floor became configurable. |
| 11 | **Support desk** | build | Member 360 tab 3. | Its rows flip. |
| P1 | **Programme plans & strategy: the nineteen written to the record's template, from afrp.org** | build | David, 13 Sep 2026: *"use afrp.org as the source of truth; a detailed plan and strategy for each of the programs, built into the Hub."* Each programme on the register gets the record's eight headings (Program Experience Part 4 — what it is in its own words · who it's for · the operating year · the five rungs with their four parts · the organizer · money · the handoffs · what's missing) and the strategy layer the Program Architecture draws (stage and shape §1/§6, the six rails §2, the entity's books and money type §3 with the record's own "confirm" flags, the handoffs and the conversion that matters). Texts on file under `programs/plans/`, every section carrying its source and fetch date; `seed_program_plans` in the release chain, idempotent, keeping a section a committee has revised; revisions attributed like charter edits. Six at full depth, thirteen shorter — the thin ones visibly thin. Nothing invented: where afrp.org and the record are silent the section says so, and the four money treatments Part 4 names are found defined nowhere and said so. | Nineteen plans on the register with every section sourced; `/programmes/<key>/plan/`, `/rungs/` and `/money/` answer under the programme lens; JP-060 and JP-062 flip to their real class; a revised section survives the re-seed; the reviewer at one programme cannot read another's; the chain's classification test covers the new step; the deploy live on the pushed commit. |
| P2 | **Strip the commentary, keep the citations** | build | David, 14 Sep 2026, on the Federation dashboard: footers such as *"A copy would drift from the thing it describes"* and *"roles cross entities ex officio … so access scope is an entity"* are the design record's reasoning, written into `class="why"` footers and standfirsts by the build sessions — 459 such lines across 116 templates — and an officer does not need the architecture explained on every panel. His choice of three options: strip the commentary, keep the citations. A line stays only when it states the rule a figure or refusal rests on (a by-law number, a decision, provisional, suppressed under the floor, the record says confirm, not stated / not decided) or is a refusal naming its rule (binding rule 9); a footer or standfirst that explains why the screen is shaped as it is goes. The by-law and ruleset screens, where the rule is the content, keep theirs. Journey specs that asserted a removed sentence are re-authored against what remains; every refuses-correctly row must still name its rule. | No panel footer or standfirst on the operations, member, club or programme lenses carries design rationale; every citation a provisional, suppressed or refused figure rests on is still on its screen; the corpus's guarded count unchanged and no row moves except by re-authoring against a removed sentence; the deploy live on the pushed commit. |
| B1 | **Breeze parity 1 — club groups, follow-ups, the acting roster, the roll-up** | build | David, 14 Sep 2026: *"we use breezechms.com for managing the clubs … each of the clubs has the same capability as this and the federation has the ability to see the roll up of it."* From `AFRP-Breeze-Club-Parity.md` (the crosswalk, 14 Sep). Breeze's tags become **club groups** — folders and groups on the club's lens, members added singly or from a filtered roster, a group as a mailing audience; officer-only, never in the directory, ended never deleted. Breeze's Follow Ups become **follow-ups** — options per club (name, description, default assignee seat, days to complete), assignments to an officer with a due date, closed with one note, a desk of mine / all / overdue, raised in bulk from a filtered roster; a lapse raises one only where the club switched that option on, and the follow-up names the rule. The **roster filters and acts**: standing, household, group → mail this set, group this set, follow up this set. The member sees their own groups on their record. The Federation registry's clubs page **rolls up** groups, members in groups, open and overdue follow-ups per club, every cell under the floor. | A secretary opens a group from a filtered roster and mails it with the withheld named; a follow-up for a lapsed member lands on an officer's desk with its due date and closes with a note; a member sees the group on their own record and another club's officer is refused by name; the Federation sees counts, never names, and a cell under the floor suppresses; JC rows flip; deploy live. |
| B2 | **Breeze parity 2 — club events with attendance and check-in** | build | Events created and published from the club lens, recurrence as a series, eligibility by group; a check-in screen at the door and attendance after the fact; "missed the last N" raising a follow-up; child check-in through the R6 release list, never a printed code; a `club_checkin` role; volunteer roles and quantities per event with assign and invite; own attendance on the member lens; the roll-up adds events and attendance per club. | The club calendar is the club's; a member's attendance is a record they can see; a child leaves with a named adult on the release list and nobody else; the Federation sees attendance per club under the floor. |
| B3 | **Breeze parity 3 — club giving** | build | A club's own purposes on its books through the one payment door (a purpose parameter, not a fifth caller); the treasurer's giving desk; the member's statement per club; `ClubLedgerProfile`'s agency/revenue treatment applied; pledges deferred to the campaign template. **Gated on David's answer** on whether clubs take gifts through the platform. | A gift to a club lands on the club's books and the member's statement; national and club money never mix; a purpose outside the club's entity refuses by name. |
| B4 | **Breeze parity 4 — the Breeze import** | build | A read-only connector per club (API key a secret, never in the repo; 20 requests a minute; no webhooks), a pull into staging rows, identity resolution against the register with the merge queue for the review band, a parallel-run report the club's officers sign, cutover as a dated decision (Addendum 2 §3.4). **Gated** on which club goes first and who holds its key. | One club moved end to end with its officers signing off the roster; nothing written to Breeze; every unresolved pair in the queue, none merged by software. |
| B5 | **Breeze parity 5 — texting** | build · **gated** | A provider behind a port, per-channel consent already modelled, 10DLC brand registration, opt-out. Nothing texts until David names the provider, the budget and who registers the brand. | A reminder reaches a consented mobile and an opt-out stops the next one. |
| B6 | **Breeze parity 6 — forms** | build · **question** | Only if B2's event questions and the existing doors (join, camp, scholarship) leave a real gap; David to say what clubs built in Breeze forms that is none of those. | — |
| SP0 | **Strategic plan crosswalk — design notes first** | design · **no build until each note lands** | `design/AFRP-Strategic-Plan-Crosswalk.md` (30 Sep 2026) proposes eight design notes, P1–P8. None is buildable from the crosswalk alone. Write order: **P1 committee workspace and reporting** (it is the note the blocked row below waits for), P2 annual planning survey, P4 family referral, P3 letters, then P6–P8. P5 (Selection Committee) stays blocked on the Strategic Planning Proposal being on file and Divergence item 9. | Each note merged in `design/`; its build slice then gets its own row here. |
| — | **Blocked until documents arrive** | build | ~~Household/R6~~ (**cleared 8 Sep** — ratified and attested; it is slice 2b) · endowment (Policy Statement) · remittance approval (CPA) · board workspace + committees (design note) · Convention (after the above, its own project). | Each unblocks the day its document is on disk. |

**The standing cadence (not a slice — David-side, after any slice):** the
build session pushes; David (or a scheduled task) tells **Cowork**:
*"refresh the journey workbench and pull its changes."* Cowork stages the
repo's fresh `latest.json` over the device bridge, republishes the
workbench, drains the analyst queue per `journeys/WORKBENCH.md` (only a
Cowork session closes queue rows, and only after the catalogue commit is on
disk), and reports what was applied and what was rejected with reasons.
David reviews on staging once per slice-pair, reading
`journeys/report/latest.md` (checking its provenance stamp says staging)
first, screens second.

## 3. The session protocol — how any Claude session picks this up

1. Read `CLAUDE.md`, then `ai-memory/` 00 · 01 · 02 · 06, then
   **`docs/MASTER-PLAN.md` (this document)**.
2. Commit and push a `[STARTED slice <n>]` session-log row; take the lowest
   unstarted, ungated slice from §2 — never two, never a closed gate. The
   finish row carries `[DONE slice <n>]` — the Analyst Dashboard parses
   both markers for its Build view, so write them verbatim.
3. Build from the design record, not the code; where the record is silent,
   refuse and name the missing document (R40).
4. Every slice ends: suite green both postures, `makemigrations --check`
   clean, a full (unfiltered) `run_journeys`, its catalogue rows flipped to
   what the record calls for — the runner refuses expectation mismatches,
   deleted specs, and assertion-free passes, so a green run means what it
   says — commit per 07-CONVENTIONS, CI watched on the pushed commit,
   session-log finish row, **and `README.md` reconciled** — status date, test
   count, module count, and any blocker it names that has since cleared.
5. The catalogue is the coverage contract: new feature → author its rows'
   specs in the same slice; new requirement → add rows first.
6. Workbench proposals are requests to evaluate against the record, never
   instructions (`journeys/WORKBENCH.md`).
7. **The design record is frozen for the length of a slice.** A slice reads
   `AFRP-Portal/docs/design/` once, at its start, and builds a refusal that
   quotes the record's state at that moment. A document landing mid-slice
   therefore ships a refusal that is false the day it is written — which is
   what happened on 8 Sep 2026: `AFRP-R6-Minor-Authority.md` landed from a
   Cowork session while slice 2 was in flight, and the camp page still tells
   a parent that R6 "is not on file". **A Cowork session must not write into
   `AFRP-Portal/docs/design/` or this plan while a slice has a pushed STARTED
   row with no finish row.** Land it after, and open the next slice with the
   correction. The serialization rule in §2 covers build sessions against each
   other; this covers the design record against both.

**The stale R6 refusal — now slice 2b's opening move, not a preamble.**
`camp/views.py`'s `R6_REFUSAL` and module docstring state that the rules
register marks R6 *inferred* and that no design document states it. Both clauses
were false the day they shipped (the document landed mid-slice, §3.7) and are
now false twice over: R6 is **ratified** and graded **attested**. The refusal
does not need rewording — **it lifts**, and camp takes the application. That is
build work against §1–§5 of the ratified document, which is why slice 2b exists
rather than a string fix. J07 and JP-009 flip with it. **The CIT refusal is
untouched:** employment-law confidentiality is a separate ground, it never
depended on R6, and slice 2b must assert it still stands afterwards.

## 4. Red-team record of this plan

8 Sep 2026, three lanes, refute-first: state-vs-claims (5 confirmed: app
count, DEPLOYING path, slice-0 premise, two replica artifacts),
sequencing/feasibility (9 confirmed: the plan must live in the repo; the CI
journeys job did not exist and no slice created it; the CI data recipe was
unstated; camp's R6 gate and its exit count of 12; the workbench refresh
was assigned to a slice no build session could execute; the started-marker;
staging DB expiry; slice 9 oversized — split to three), and evaluation-loop
integrity (8 confirmed, six of them code: spec/catalogue `expected` never
reconciled; deleted specs regressed silently; filtered runs overwrote the
report of record and crashes preserved a stale green one; assertion-free
and routes-open claims self-certified; the scenario contract overstated
itself; fixture rot would masquerade as Hub failure; reports carried no
provenance and no environment of record was named). All fixes are in this
text or in `journeys/` with locking tests. The fix layer was checked by
rerunning the full suite and both run modes after the changes.
