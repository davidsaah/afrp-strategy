# AFRP Consolidated Platform Map
### Companion to `afrp-mockups/docs/AFRP-Unified-Platform.html` — 19 Aug 2026

**Status:** design document. The "mockups-only" instruction is in force; nothing in the PROPOSED
sections is to be built until David lifts it.

**Since 2 October 2026:** this map is kept as the record of the 19 August mockup. The afrp-mockups and AFRP-Portal repositories it names were folded into afrp-strategy on 29 September 2026. The elements raised since are designed in the notes P21–P28; §7 lists them with their modules. Where a passage below has moved, a dated pointer stands beside it. The mockup is evidence of a story, never of a rule (D41).

---

## 1. What the consolidated document is

`AFRP-Unified-Platform.html` merges the two Unified documents (Member v3.1, Operations v3.1) into a
single mockup-system of **53 frames organized by institution**, adds the Convention as its own
element with six new proposed screens, and adds five further new screens: **M1** household-level
directory inclusion (in Membership & household — you and your family's directory presence decided
person by person where the household lives), **L1/L2** add & approve life events (member submission
form with type-specific gates shown up front; staff approval queue where approve ≠ publish and a
death's approve button is withheld until family approval), **D1** the RBPN professional directory
(Community carries the full member directory, frame 17, plus this opt-in storefront), and **A1**
the ads desk (one order flow selling placements in *Hathihe Ramallah* and the convention programme
book, reachable from both the magazine section and the convention store C2, class MAG / CONV68). The 42 carried-over frames are byte-identical markup,
style-scoped (`.sc-m` / `.sc-o`) so both stylesheets coexist in one file. Every module carries a
build-status badge audited against this repo at commit `152f0af` (243/243 tests):

| Badge | Meaning |
|---|---|
| BUILT | Live routes / modules / tests in this repo; frame and code describe the same behaviour |
| BUILT · PARTIAL | Core objects exist; part of the shown surface is design-only |
| DESIGNED | Specified in docs/design, mocked, no backend module |
| PROPOSED | New in the consolidated document (Convention C1–C6, ARFHSN roadmap) |

## 2. Institution map

**Part I — AFRP** (Constitution & By-Laws 2024; rulesets `bylaws-2012.2` in force, `bylaws-2024.1`
parallel): federation overview (f01, f06) · membership/household/identity incl. directory inclusion
(s01–s05, M1, f02–f03) · money & finance (s06–s07, f07–f10) · events (s08–s09) · governance &
elections (s11–s13, f05) · clubs & local club systems (s18, f11–f14) · family tree (s14) · life
events: add & approve (s15–s16, L1, L2) · community: full & professional directories (s17, D1) ·
Hathihe Ramallah, bookstore & ads desk (s19–s20, A1, f19–f20) · programmes: catalogue, camp, alumni
(s21, f21, f18) · **★ the Convention** (below).

**Part II — ARFECF** (By-Laws 2013; `arfecf-2013`): scholarship program (f15–f17; BUILT —
src/scholarships/*) · endowment (DESIGNED; blocked on Endowment Fund Policy Statement) · policy
alignment note: region map + 4-member interlock cap carried **inactive** — not in the 2013 text.

**Part III — ARFHSN** (By-Laws 2015/2017; `arfhsn-2017`): Medical Mission and human-services
programs as PROPOSED roadmap on the shared programme rails; governance is an interlock with AFRP's
board tooling (14-seat BOT elected by the AFRP Board; amendments 60% of the AFRP Board; no
membership), not a separate portal.

Program-to-institution assignment per David, 19 Aug 2026: scholarships + endowment → ARFECF;
medical mission + human services → ARFHSN; camp, alumni, convention, magazine, bookstore → AFRP.

*Since 1–2 October 2026:* D55 sets each programme's holding entity as the fund that budgets it. Camp Ramallah and the Magazine's assets are ARFECF's, the Convention is AFRP's, and Women to Women and the Medical Mission are ARFHSN's. The bookstore is per title: the cook book's line is ARFECF's by D55's test, and the other titles' entity is not stated (P24 §8.2; Q-197). The Senior Living project is the Ramallah Foundation's, not a programme of any of the three (P23 §8; Q-203).

## 3. The Convention element (Part I, Module 9)

*Since 2 October 2026:* the Convention element is designed in **P22** (`AFRP-Convention-Operations.md`; slices CV1–CV8), building between P8 (bids, HB1–HB4) and P13 (host agreements, HA1–HA6) without redesigning either. Several points below have moved.
- **Delegates** come from the roll the Selection Committee certifies (9.3.5, with the community cap of 9.1.4; P5 §3.8, SC4). Each club's delegation is a dated act with its method stated (officers' selection, members' vote, or the club's own by-laws), and none is refused (Q-37). Presence is marked at the desk, and the weight is certified members divided by present delegates (P22 §6's reading of 9.1.3's 'delegates sent'; Q-37). Whether a club's remittance state gates its credentials, as this mockup shows, is not stated in P22.
- **The desk** covers check-in, platform-printed badges, walk-ins through the same door, and office-only transfers (P22 §5.4).
- **The coordinator's access** in the design is narrower than today's practice (P22 §8; Q-127).
- **The money** lands on the chart the Federation already keeps: the Convention bank account and "Due to Convention Host City" (P22 §10). Any Convention posting to ARFECF is refused (Q-224).

Stands alone under AFRP programmes. Four surfaces:

1. **Member registration** — existing frame s10; runs on membership/payment rails (BUILT-adjacent).
2. **Governance floor** — existing frame f04 rehomed here; weighted delegation per By-Law 9.1.3 on
   the certified roll frozen at record date (src/governance/eligibility.ts).
3. **Participant layer (C1–C3, phone)** — C1 live schedule + stamped one-way announcements
   (operational notices, not marketing; no quiet schedule edits — a change is a broadcast with a
   timestamp); C2 store: merchandise, banquet/excursion tickets (with capacity), programme-book
   ads; desk pickup only; C3 help desk: topic-routed form, registration auto-attached — the only
   two-way door.
4. **Organizer backend (C4–C6, laptop)** — C4 command dashboard (registration by club, credentials,
   capacity, queue); C5 credentialing & club integration; C6 store fulfilment, broadcast composer,
   help-desk queue with owners and clocks.

**Club-system integration — two doors, one truth.** A club either publishes a live feed from its
own club system (read-only to the convention, sync-stamped per row) or files a dated manual roster
at the desk. Both first-class, both labelled at every point of use; nobody edits counts at the
convention layer — corrections happen at the source. Delegate **standing is verified against the
club remittance ledger** (src/ledger/remittance.ts), not self-attested — a missing club remittance
surfaces as a credentialing gate.

**Money.** Store revenue posts gross through existing journal rails (src/ledger/posting.ts) under
`class CONV68`; fees on their own line; refunds as reversing lines; no side spreadsheet.

### Draft API surface (build contract — PROPOSED)

```
GET  /v1/convention/:n/registrations          ?club= &state=
GET  /v1/convention/:n/delegates              ?club=
POST /v1/convention/:n/credentials/:id/verify   → runs standing check vs remittance ledger
POST /v1/convention/:n/credentials/freeze       → freezes delegate roll (idempotent, audited)
GET  /v1/convention/:n/store/catalog
POST /v1/convention/:n/store/orders             → posts journal lines, class CONV68
POST /v1/convention/:n/store/orders/:id/fulfil  → badge-scan pickup
POST /v1/convention/:n/announcements            → stamped broadcast; audience = checked-in
GET  /v1/convention/:n/announcements
POST /v1/convention/:n/inquiries                → help-desk form; registration attached
PATCH /v1/convention/:n/inquiries/:id           → assign / answer / close
```

Scope model: a `convention_chair` grant is `(person, role, program:convention-:n)` — reads club
delegate/registration data across all 26 clubs and stops there; club ledgers, member giving and
consent stay out of scope.

## 4. Honesty notes carried into the public document

The 2024 text **kept the mailed CPA ballot** *(the by-law's ballot handled by an accountant; which of four roles the record means by "the CPA" elsewhere is Q-231)*; the electronic-ballot frames are labelled as the
future-amendment design (AFRP-Electronic-Voting.md), with `bylaws-2012.2` named as in force.
48 provisional overrides pending Board ratification. Public repo quotes operative by-law text
plainly; deliberative material (this doc) stays private.

## 5. Brand assets

The official federation logo (supplied by David, 19 Aug 2026 — closes the delivery-status open
item) lives at `afrp-mockups/docs/assets/AFRP_Logo.png` (public, shown on the site index) and
`AFRP-Portal/docs/brand/AFRP_Logo.png` (private canonical copy). A flat vector adaptation —
`afrp-mockups/docs/assets/afrp-mark.svg` — redraws its elements (olive tree, olives, hanging
sprigs, stone wall, arch) in the v3.1 heritage palette with currentColor ink for light/dark
contexts; it is the product/UI mark (used in the Unified Platform masthead), while the official
logo remains the formal identity.

## 6. Files touched in this delivery

- `afrp-mockups/docs/AFRP-Unified-Platform.html` — new consolidated document (public)
- `afrp-mockups/docs/index.html` — consolidated doc featured; official logo added; footer corrected
  (mailed CPA ballot retained; 2024 ruleset parallel, not adopted)
- `afrp-mockups/docs/assets/AFRP_Logo.png`, `afrp-mockups/docs/assets/afrp-mark.svg` — brand assets
- `AFRP-Portal/docs/brand/AFRP_Logo.png` — canonical logo copy (private)
- `AFRP-Portal/docs/design/AFRP-Consolidated-Platform-Map.md` — this document (private)

Existing Unified Member/Operations documents remain in the repo unchanged for provenance.

## 7. Elements designed since: P21–P28 (2 October 2026)

| Note | Element | Modules | Slices |
|---|---|---|---|
| P21 `AFRP-Contact-Record.md` | The contact record: a non-member as one person with dated roles (cross-cutting; Q-70) | `people`, `member`, `comms`, `programs`, `events`, `clubs`, `magazine`, `payments`; institution registry; retention (IR2) | CR1–CR7 |
| P22 `AFRP-Convention-Operations.md` | Convention operations, from the award to the close and the books | `events`, `payments`, `ledger`, `funds`, `voting`, `clubs`, `governance`; CG2; CW1 | CV1–CV8 |
| P23 `AFRP-Relief-Fund-and-Senior-Living.md` | The Relief Fund's three paths; the Federation's part in the Foundation's home | `funds`, `ledger`, `grants`, institution registry, `payments`, `comms` | RL1–RL6 |
| P24 `AFRP-Magazine-Operations.md` | The Magazine as it runs; the two live stores and the Cook Book | `magazine`, `store`, `funds`, `ledger`, `comms`, `memberdir` | MG1–MG7 |
| P25 `AFRP-Leadership-Pipeline.md` | The leadership path; the Young Leader Committee; the Senior Award switch; the Day of Action's two modes | `programs`, `committees`, `member`, `events`, `alumni`, `voting`, `network`, `reporting` | YL1–YL6 |
| P26 `AFRP-Scholarship-Awards.md` | Scholarship awards and renewal (the scholar's experience) | `scholarship`, `funds`, `ledger`, `comms`, `committees`, `alumni` | SA1–SA7 |
| P27 `AFRP-Family-Tree-In-Practice.md` | The family tree's migration from practice (amended by D68–D74) | `tree`, `member`, `committees`, `comms`, `heritage`, `access` | FT1–FT6 |
| P28 `AFRP-Family-Tree-Module.md` | The family tree module under D68–D74 | `tree`, `member`, `join`, `dues`, `access`, `rules`, `magazine`, `memberdir`, `comms`, `reporting` | T2-0, T2-R, T2a–T2h |

Each slice row is in `plan/MASTER-PLAN.md` §2.
