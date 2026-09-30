# AFRP strategic plan crosswalk
### Every element of the Federation's strategic plans, and what the platform does about each

**Date:** 30 September 2026
**Status:** design record. This document **proposes** the design notes the
proposed elements need; it does not by itself make any of them buildable.
**Decision 42** (the Decisions Register) settles the framework used here.

---

## Why this document exists

The Federation has run a Strategic Planning Committee since at least 2018. Its
record is a set of documents held in AFRP's Drive, not in this repository:

| Short name | Document | Date | Status |
|---|---|---|---|
| **SP19** | AFRP Strategic Plan 2018–2023, revision "0509919" | May 2019 | Presented at the July 2019 Convention |
| **FED2** | 2020–2021 Strategic Planning Committee Recommendations ("Federation 2.0", Phase 2), 73 pages | Revision 3 May 2021 | Presented at the 2021 virtual Mid-Year; its table of contents says voted on at the 2021 Jacksonville Convention. No minutes of the vote are on file |
| **TASKS** | Tasks for SP Subcommittees | after July 2021 | Implementation list for FED2 |
| **MOU** | Approved Convention Memorandum of Understanding | October 2022 | Approved |
| **MIN** | Committee minutes, 2020–2023 | 2020–2023 | Record |
| **APP** | AFRP App Requirements, three drafts | 2020–2021 | Working papers behind FED2 §A |
| **PR** | Media and PR Committee business plan; press-release proposal; social media audit; communications-management deck | 2018–2021 | Working papers behind FED2 §A |
| **SWOT25** | Committee and programme SWOT responses to the Deputy President's survey | March 2025 | Record |
| **SP26** | Strategic Planning Committee minutes | 10 September 2026 | Record; the committee restarting |

**FED2 matters to this repository directly.** By-Law 17.1.4 (2024) says "review
the Strategic Planning Proposal for the full details of the committee's
description". That is FED2 §G. `AFRP-Bylaws-Ingestion-Architecture.md` carries it
as cited and not on file; it has now been located (see that document).

The 2018–2023 plan period has ended and no successor plan exists. SP26 asked for
a baseline outline of the existing plans; this crosswalk is its platform half.

---

## Status key

| Status | Meaning |
|---|---|
| **Built** | In AFRP-Hub and tested. Nothing is in service yet: no DNS, no live payments, no real member data |
| **Partly built** | Core objects exist; part of the element is design-only |
| **Designed** | In this design record, not built |
| **Plan only** | In the Hub as a register row and a programme plan (slice P1), with no working surface |
| **Queued** | A slice in `plan/MASTER-PLAN.md` |
| **Proposed** | Not in the record. Needs a design note before a build session may touch it |
| **Outside** | Not a platform job: a hire, a policy, a by-law, or money |
| **Gap** | The strategy names it and nothing in the record accounts for it |

---

## A. Mission, framework and planning

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| A1 | Mission: ties between Ramallah people in Palestine and the US; heritage for US-born youth; educate the American public | SP19, programme flyer | Built | Public site pages |
| A2 | The plan is a living document; the committee recommends and does not implement | FED2 | Outside | The document registry can hold each version |
| A3 | A yearly action plan with monthly actions and a core group that meets regularly | MIN Jan 2020 | Proposed | The committee workspace (P1) |
| A4 | Annual retreat on mission and vision | MIN 2020, FED2 §A KPIs | Outside | — |
| A5 | Evaluate programmes; review or retire those that do not contribute | MIN Feb 2020 | Designed | Five-rung engagement ladder (D25) and stage-to-stage conversion (`AFRP-Program-Architecture.md` §1) |
| A6 | Outcome-based metrics per area, to show donors a return and support an endowment campaign | SP26 | Partly built | The four branches are built (D38–D40, slice T1a); the conversion metric is designed |
| A7 | A yearly survey of every committee: purpose, what worked, SWOT, 3–5 year goals, budget | SWOT25 | Proposed | Annual planning form (P2) |
| A8 | Refresh priorities: Camp Ramallah, Government Affairs, Arabic classes, Ramallah Works, Family Tree | SP26 | Partly built · **Gap** | All but Ramallah Works are on the branches. **Ramallah Works is on no register and in no design document** |

## B. Governance and constitution

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| B1 | Constitutional review: board size, term limits, committee viability | SP19 | Built | By-laws engine; `bylaws-2012.2` in force, `bylaws-2024.1` in parallel with 48 provisional overrides |
| B2 | Enforce Board eligibility; letters to members out of compliance | MIN Feb–Mar 2020 | Partly built | Good standing is computed; the letters are proposed (P3) |
| B3 | A parliamentarian and a three-minute speaking limit at Board meetings | MIN Feb 2020 | Partly built · Proposed | The live floor is built; a speaking timer is not in the record |
| B4 | Executive board, advisory board and executive committee structure | MIN Feb 2020 | Outside | A by-law matter; the engine reads whatever is adopted |
| B5 | **Selection Committee** replacing Nominations, Credentials and Elections | FED2 §G; By-Law Art. XVII | Partly built · Proposed | The engine carries Art. XVII. The vacancy → application → eligibility → interview → slate workflow is proposed (P5), blocked on FED2 being on file and on Divergence item 9 (floor nominations) |
| B6 | Presidential Advisory Council of the three immediate Past Presidents | FED2 §C | **Gap** | Not in the 2024 by-law analysis. Whether it was adopted is unknown |
| B7 | Officer and Executive Committee job descriptions tied to by-law sections | FED2 §C | Partly built | Roles and exact grants are built; the descriptions themselves are proposed content |
| B8 | Committee chair and member descriptions; minutes within 30 days; review after two unexcused absences | FED2 §C | Proposed | Committee workspace (P1). The Hub refuses committees today because no design note exists |
| B9 | Quarterly committee report and programme report templates | FED2 §C | Proposed | Committee workspace (P1) |
| B10 | Staff give chairs database access to committee documents and track members' terms | FED2 §C | Proposed | Committee workspace (P1) |
| B11 | Deputy President: Club Presidents' monthly call, club health, a buddy system, dormant and new clubs | FED2 §C | Partly built | Club lens roll-up; dormant-club dues (D6). The calls are outside |
| B12 | Young people on every committee | MIN Mar 2020 | Outside · Proposed | A by-law matter; the workspace can report each committee's age mix |
| B13 | Fiscal year | MIN Feb 2020 (proposed Jan–Dec) | Built | The 2024 text keeps June–May (8.7.2); the engine follows the text |
| B14 | Strategic Plan Committee composition | By-Law 7.3.3 | **Gap** | Deputy President chairs, plus four members appointed by the DP with Board approval. The 2026 roster should be checked against it |

## C. Administration and staffing

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| C1 | Executive Director | SP19, MIN 2020–23, SP26 | Outside | The ED is a role with grants. By-law: must reside in the HQ metro area (Const. V §3, 7.9.7) |
| C2 | Program Coordinator | SP19 | Outside | Hired in 2019 |
| C3 | Communications Coordinator, manager or intern | FED2 §A, PR | Outside | The comms desk is the tool that role would use |
| C4 | File organisation and archives; a central document repository | SP19, SP26 | Partly built · Proposed | Registries and the magazine archive are built. Committee and strategic-plan records are proposed (P1). **Undecided:** the platform or a shared drive as the archive of record |
| C5 | Every membership payment recorded and cross-referenced by family and Manara | FED2 §C | Built | One ledger with daily close |
| C6 | Welcome packages for Board and committee members | MIN 2020, FED2 §C | Proposed | Letters (P3) |
| C7 | Staffing in Ramallah, the US, or both | MIN 2022 | Outside | — |

## D. Membership, database and the app

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| D1 | A central member database ("No database/CRM" in the 2018 SWOT) | SP19, FED2, MIN | Built | The platform is this element. It replaces a landscape in which a member is five to seven unlinked records (Dynamics 365, per-club Breeze, Mailchimp and others) |
| D2 | Services to local clubs; connectivity among clubs | SP19 | Partly built · Queued | Club lens; Breeze parity B1–B2 built, B3–B6 queued |
| D3 | Business intelligence and retention rates | SP19 | Partly built | Reporting built; conversion designed |
| D4 | Member-only information behind a password | SP19 | Built | Passwordless sign-in; members-only directory; nothing about the living without sign-in (D28) |
| D5 | Dues online, including the Manara tier with automatic renewal | SP19 | Partly built | Join and renewal built. Manara renewal refuses until the Board Rules & Regulations are on file |
| D6 | Getting members registered on the new system | MIN Sep 2023 | Built · Queued | Join wizard built; email provider is slice 5 |
| D7 | Clubs drive national sign-ups; families refer non-member Ramallah families | MIN Sep 2023 | Proposed | Referral into the club's follow-ups (P4) |
| D8 | Benefits for long-time members and sponsors | MIN Sep 2023 | Proposed · Outside | The recognition-tiers register exists; the benefits are a Board decision |
| D9 | Member demographics | MIN Mar 2023 | Built | Member 360, household |
| D10 | Mass communication to members | MIN Mar 2023 | Partly built | Comms desk; email provider gated (slice 5) |
| D11 | Training for local clubs | MIN Mar 2023 | Outside | — |
| D12 | An operations and maintenance budget for the system | MIN Mar 2023 | **Gap** | Who maintains the platform after launch, and who pays, is in no document |
| D13 | A mobile app | SP19, APP | Designed | Web first, works on a phone. Native app deferred (`AFRP-Portal-Mobile-UX-Review.md`) |
| D14 | Events calendar with reminders; a live itinerary with 30-minute reminders | APP | Partly built · Designed | Events built; push needs the native app; the itinerary is Convention C1 |
| D15 | Donate button for each programme and fund | APP | Built | The funds money path (payments simulated until slice 5) |
| D16 | Convention and Mid-Year registration and photographs | APP | Partly built · Proposed | Events built; Convention designed; a past-events gallery is not in the record |
| D17 | News, press releases, statements, media links, resources | APP | Partly built · Proposed | Website desk built; a press and statement archive is not in the record |
| D18 | Hathihe Ramallah in the app | APP | Built · Queued | Magazine archive; operations slices 7–7b |
| D19 | Pay on the web, not in the app (avoids the app-store cut) | APP, MIN Dec 2020 | Built | All payment is on the web |
| D20 | Ads shown to members who have not paid dues | APP, MIN Dec 2020 | Outside | Not proposed. The ads desk (A1 frame) sells magazine and programme-book placements instead |
| D21 | Magazine money kept apart from Federation money | MIN Dec 2020 | Built | Multi-entity ledger; purpose on every line |
| D22 | Family tree in the app, with correction forms and GEDCOM updates | APP | Built | GEDCOM round-trip, hourglass, committee queue (D11–D22, D30–D37). Corrections go to a committee, not to one person |

## E. Communications

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| E1 | One consistent message across every channel | PR, FED2 §A | Partly built | Comms desk and website desk; the strategy itself is outside |
| E2 | A newsletter on a fixed schedule | PR audit, FED2 §A | Proposed | A cadence on the comms desk (after slice 5) |
| E3 | A clearer website | PR audit | Built | Public site rebuilt on the design system; its content review is pending |
| E4 | Website handed to emerging leaders | SP19 SWOT | Outside | — |
| E5 | Social media metrics | PR audit | Outside | A scheduling tool, not the platform |
| E6 | Press releases: proactive and reactive, a 24-hour clock, a media list | PR | Proposed | Press workflow (P6) |
| E7 | Spokespersons, a storyteller bank, writers, club correspondents, social-media volunteers | PR, MIN 2020–22 | Proposed | Volunteer interests on the member profile (P7) |
| E8 | A record of Palestinian-American accomplishment | FED2 §A | Proposed | A Heritage branch item, if wanted |
| E9 | Annual report | SP19, MIN Dec 2020 | Proposed | Drawn from reporting |
| E10 | Brand guide and its enforcement | FED2 §A | Built | The design system |

## F. Programmes

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| F1 | A youth pipeline from childhood to professional life | SP19, FED2 | Built | Education (ladder by age) and Leadership (ladder by capacity) branches |
| F2 | Camp Ramallah: more campers from small communities, more age tiers, a site of its own | SWOT25 | Built | Camp application, selection, roster and camperships (slices 2 and 2b); the age tiers and a site are Federation decisions |
| F3 | Project Hope: formal processes, succession, one trip per person | SWOT25, flyer | Partly built · Proposed | Programme template built; one-trip rule not in the rules register |
| F4 | Leadership Ramallah with the Mid-Year | SP19 | Plan only | Register row and programme plan (slice P1); the Mid-Year pairing is not modelled |
| F5 | Exchange Mission: missions, alumni database, fellowships, alumni newsletter | SP19, SWOT25 | Partly built · Proposed | Alumni match queue built (slice 9); fellowship applications not in the record |
| F6 | Women to Women: projects, younger women, a representative per city | SWOT25 | Partly built | Care branch; giving through funds. Which entity runs it is open (`AFRP-Program-Architecture.md` §0) |
| F7 | RBPN five-year plan: mentorship, ambassadors, conferences | SP19 | Built | Sponsorship desk and job board (slices 10, 10b); mentorship not in the record |
| F8 | Cultural Preservation: digitisation, oral histories | SP19 | Designed | Heritage branch |
| F9 | Scholarships | SP19, flyer | Built | Scholarship committee engine (slice 4) |
| F10 | Medical Mission and human services | SP19 | Designed | ARFHSN roadmap |
| F11 | Recruit 21–35 year-olds through RBPN; youth leaders in each club | MIN Mar 2023 | Partly built | Leadership branch; age-band reporting designed |
| F12 | Programme alumni event at the Convention | MIN Mar 2023 | Proposed | An event type fed by alumni segments |

## G. Events and the Convention

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| G1 | Mid-Year guidelines: host bids ~13 months ahead, schedule, room block, fees | FED2 §B | Proposed | Host-bid workflow (P8); events built |
| G2 | Convention guidelines | FED2 §B, MOU | Designed | The Convention element |
| G3 | MOU terms: host two years ahead; registration data belongs to the Federation; Relief Fund per registration; dues folded into non-member registration; the Federation's share and 60-day settlement | MOU | Designed · Proposed | Convention element and class CONV68; a settlement statement is not in the record |
| G4 | Welcome session for new members at special events | MIN Dec 2020 | Proposed | Letters and onboarding (P3) |
| G5 | Online registration run with the host club | FED2 §B | Partly built | Events built; Convention designed |

## H. Finance and fundraising

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| H1 | Finance Committee approves budgets | SP19 | Partly built | Ledger built; the committee's own workspace is P1 |
| H2 | A web presence that helps fundraising | SP19 | Built | Funds path |
| H3 | An endowment campaign | SP26 | Designed | Blocked on the Endowment Fund Policy Statement (D2) |
| H4 | "Charitable giving unacknowledged" | SP19 SWOT | Designed | Four contributor moments and an annual statement (D10) |
| H5 | A budget line per programme | SP19 | Designed | Typed budget line (`AFRP-Program-Architecture.md` §3) |
| H6 | Grant-writing | MIN Sep 2023 | Outside | — |

## I. Government relations and advocacy

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| I1 | Decide whether policy work fits the mission | SP19 | Built | Settled in practice: Congressional Outreach sits on the Leadership branch; Government Affairs Committee is By-Law 8.15.1 |
| I2 | Elected-official relations; a stronger advocacy voice | TASKS, SWOT25 | Outside | — |

---

## What the platform adds that no strategic plan contains

These exist in the design record and the Hub and appear in none of the
strategy documents. A refreshed plan should name them, because the committee
has not yet seen them.

| Element | Record |
|---|---|
| **Digital voting**, approved by the Board as the direction | D4, `AFRP-Electronic-Voting.md` |
| **By-laws as versioned rulesets**, the 48 provisional overrides and the four-amendment package | `AFRP-Bylaws-Reconciliation.md`, `AFRP-Bylaws-2024-Divergence.md` |
| **The family tree as the platform's spine**, and as evidence rather than a verdict on eligibility | D11–D22, D30–D37 |
| **The four branches**, the tree as roots and the Convention as junction | D38–D40, D42 |
| **The five-rung engagement ladder** in every programme | D25 |
| **Three entities on one ledger** (AFRP, ARFECF, ARFHSN), agency treatment of club dues, restricted-fund rules | D1–D3, D7–D10, `AFRP-Multi-Entity-Ledger.md` |
| **Scholarship committee engine** with conflict checks over the tree and cross-border tax positions | Slice 4, `AFRP-Adviser-Brief.md` |
| **Club tools replacing Breeze** | `AFRP-Addendum-2-Breeze-Replacement.md`, B1–B6 |
| **Privacy as data**: per-field directory consent, nothing about the living without sign-in, household consent for minors | D17, D22, D28, D33, R6 |
| **Maintainability as the governing risk**: a plain stack chosen for "who maintains this in 2031" | AFRP-Hub ADR-001 |
| **A journey corpus** that tests the build against the stories it must support | `plan/MASTER-PLAN.md` §1b |

---

## Proposed design notes

Each needs a design note in `design/` before a build session may pick it up.
The rows in `plan/MASTER-PLAN.md` §2 say so.

| # | Design note | Covers | Ready to write? |
|---|---|---|---|
| P1 | Committee workspace and reporting | A3, B8–B10, C4, H1 | **Yes.** FED2 §C holds the content. It is the note the "board workspace + committees" blocked row is waiting for |
| P2 | Annual committee planning survey | A7 | **Yes.** SWOT25's form is complete |
| P3 | Welcome, renewal and Board letters; new-member welcome | B2, C6, G4 | Content yes; signatory and approved wording are open |
| P4 | Family referral into club follow-ups | D7 | **Yes**, on B1's follow-ups |
| P5 | Selection Committee workflow | B5 | Blocked: FED2 on file; Divergence item 9 |
| P6 | Press-release workflow | E6 | Yes |
| P7 | Volunteer interests and rosters | E7 | Yes |
| P8 | Mid-Year host bids | G1 | Yes |

## Gaps the record cannot close alone

1. **Ramallah Works** (A8): named as a priority in SP26 and on no register.
2. **The Presidential Advisory Council** (B6): proposed in FED2; adoption unknown.
3. **Strategic Plan Committee composition** (B14) against By-Law 7.3.3.
4. **Who maintains and pays for the platform** (D12).
5. **The archive of record** (C4): the platform, a shared drive, or both.
6. **FED2 itself**: which revision was adopted at Jacksonville in 2021. It names
   living people, so it is cited here and not committed.
