# AFRP Consolidated Platform Map
### Companion to `afrp-mockups/docs/AFRP-Unified-Platform.html` — 19 Aug 2026

**Status:** design document. The "mockups-only" instruction is in force; nothing in the PROPOSED
sections is to be built until David lifts it.

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

## 3. The Convention element (Part I, Module 9)

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

The 2024 text **kept the mailed CPA ballot**; the electronic-ballot frames are labelled as the
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
