# AFRP strategic plan crosswalk
### Every element of the Federation's strategic plans, and what the platform does about each

**Date:** 30 September 2026; section J, rows F13–F17 and notes P9–P17 added 1 October 2026
**Status:** design record. This document **proposes** the design notes the
proposed elements need; it does not by itself make any of them buildable.
**Decision 42** (the Decisions Register) settles the framework used here.

---

## Why this document exists

The Federation has run a Strategic Planning Committee since at least 2018. Its
record is a set of documents held in AFRP's Drive, not in this repository:

The links open the Federation's shared drive and work only for people with AFRP drive access. All of them except INTAKE26 are in [the Strategic Planning folder](https://drive.google.com/drive/folders/14bkSAWf37yzBG_Cvb0xWJu0xLOa5onn-).

| Short name | Document | Date | Status |
|---|---|---|---|
| **[SP19](https://drive.google.com/file/d/1HH6lFL9eDIVrloKc5oRJdJ2R9kNxIssi/view)** | AFRP Strategic Plan 2018–2023, revision "0509919" | May 2019 | Presented at the July 2019 Convention |
| **[FED2](https://drive.google.com/file/d/1vG4nE6RJF_OT1PQqnZrrsjwnwatBgqhr/view)** | 2020–2021 Strategic Planning Committee Recommendations ("Federation 2.0", Phase 2), 73 pages | Revision 3 May 2021 | Presented at the 2021 virtual Mid-Year; its table of contents says voted on at the 2021 Jacksonville Convention. No minutes of the vote are on file. Part IV §E, §G, §H, §I read in full on 1 Oct 2026 for P1 and P5 |
| **[TASKS](https://drive.google.com/file/d/1h8tGGmcCbH9iN20OBJD6eakj48BY_lVY/view)** | Tasks for SP Subcommittees | after July 2021 | Implementation list for FED2 |
| **[MOU](https://drive.google.com/file/d/1kWL45gTmtbNTLZg5LkQpkxoqUcrrzPi6/view)** | Approved Convention Memorandum of Understanding | October 2022 | Approved |
| **[MIN](https://drive.google.com/drive/folders/1t12CvhoRPqwVNqf3SZI_iIG-ym3WMPB5)** | Committee minutes, 2020–2023 | 2020–2023 | Record |
| **[APP](https://drive.google.com/file/d/1XAhEWuxk3TDLrOQI-v-a1vYtBtFUW9pT/view)** | AFRP App Requirements, three drafts | 2020–2021 | Working papers behind FED2 §A |
| **[PR](https://drive.google.com/drive/folders/1g2xb06r8ik9aE2N83AhVZ7vn38ftjlpV)** | Media and PR Committee business plan; press-release proposal; social media audit; communications-management deck | 2018–2021 | Working papers behind FED2 §A |
| **[SWOT25](https://drive.google.com/drive/folders/1AjFFC7P6gaGndOJBJSNGmFijQzAO7t1a)** | Committee and programme SWOT responses to the Deputy President's survey | March 2025 | Record |
| **[SP26](https://docs.google.com/document/d/1ux3nnjUfjSkdRWgWV5j7Lbsn9tYT2pWGrcv-uhJhaao/edit)** | Strategic Planning Committee minutes | 10 September 2026 | Record; the committee restarting |
| **[INTAKE26](https://drive.google.com/drive/folders/1mlUdsgoW-vTI2Ugk-xxmJGb-mGKUq8JW)** | The Federation's and the affiliates' working files: the Federation's own folder, ARFECF's folder, ARFHSN's folder and the officer archive, 2009–2026 | Read September–October 2026 | Working files in the Federation's drive, read through the intake process (D54). They name living people and hold figures, so the public record carries role-only summaries and folder-level links only |

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
| A3 | A yearly action plan with monthly actions and a core group that meets regularly | MIN Jan 2020 | Designed | The committee workspace, `AFRP-Committee-Workspace.md` (P1): meetings, the decisions queue and follow-ups on each body's page; slices CW1–CW2 |
| A4 | Annual retreat on mission and vision | MIN 2020, FED2 §A KPIs | Outside | — |
| A5 | Evaluate programmes; review or retire those that do not contribute | MIN Feb 2020 | Designed | Five-rung engagement ladder (D25) and stage-to-stage conversion (`AFRP-Program-Architecture.md` §1); the survey's "not structured to achieve its purpose" answers are the review's input (P2 §5) |
| A6 | Outcome-based metrics per area, to show donors a return and support an endowment campaign | SP26 | Partly built | The four branches are built (D38–D40, slice T1a); the conversion metric is designed |
| A7 | A yearly survey of every committee (one run, March 2025): purpose, what worked, structure, short- and long-term goals, budget | SWOT25 | Designed | Annual planning survey, `AFRP-Committee-Planning-Survey.md` (P2): the cycle, the versioned form (no SWOT grid on the 2025 form, though the letter names one), the roll-up; slices SV1–SV2; whether it is yearly is Q-59 |
| A8 | Refresh priorities: Camp Ramallah, Government Affairs, Arabic classes, Ramallah Works, Family Tree | SP26 | Partly built · Designed | All five are on the branches. The Arabic term is designed in `AFRP-Selection-Programmes.md` §3 (P12; slices AR1–AR4). **Ramallah Works** is AFRPWorks, the Ramallah Jobs Initiative, placed on the Leadership branch under AFRP (D64); design note P17 (`AFRP-AFRPWorks.md`): a programme page and four gated objects on the job board already built; eleven questions, most the working group's; its owner and fee model are the working group's |

## B. Governance and constitution

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| B1 | Constitutional review: board size, term limits, committee viability | SP19 | Built | By-laws engine; `bylaws-2012.2` in force, `bylaws-2024.1` in parallel with 48 provisional overrides |
| B2 | Enforce Board eligibility; letters to members out of compliance | MIN Feb–Mar 2020 | Partly built · Designed | Good standing is computed (built); the letters are `AFRP-Letters-and-Onboarding.md` §4 (P3; slice LT2) — a notice ends no seat and changes no vote; no attendance notice until Q-53 |
| B3 | A parliamentarian and a three-minute speaking limit at Board meetings | MIN Feb 2020 | Partly built · Proposed | The live floor is built; a speaking timer is not in the record |
| B4 | Executive board, advisory board and executive committee structure | MIN Feb 2020 | Outside | A by-law matter; the engine reads whatever is adopted |
| B5 | **Selection Committee** replacing Nominations, Credentials and Elections | FED2 §G; By-Law Art. XVII | Partly built · Designed | The engine carries the 2024 ruleset row; the Article XVII workflow (vacancy → application → eligibility → interview → slate → certification) is `AFRP-Selection-Committee-Workflow.md` (P5; slices SC1–SC7). Two gates stay in the row: which FED2 revision was adopted (Q-17) and what 17.1.1 gates, Divergence item 9 (Q-75) |
| B6 | Presidential Advisory Council of the three immediate Past Presidents | FED2 §C | **Gap** | Not in the 2024 by-law analysis. Whether it was adopted is unknown; P1 §7 carries it — not a body on the register until constituted |
| B7 | Officer and Executive Committee job descriptions tied to by-law sections | FED2 §C | Partly built | Roles and exact grants are built; the descriptions themselves are proposed content |
| B8 | Committee chair and member descriptions; minutes within 30 days; review after two unexcused absences | FED2 Part IV §E, §H | Designed | Committee workspace, `AFRP-Committee-Workspace.md` §3 (P1): the minutes link with the 30-day clock, attendance as marked, the third-absence review prompt; slice CW2 |
| B9 | Quarterly committee report and programme report templates | FED2 Part IV §I | Designed | Committee workspace, `AFRP-Committee-Workspace.md` §4 (P1): reports generated with only two typed fields; slice CW3 |
| B10 | Staff give chairs database access to committee documents and track members' terms | FED2 Part IV §E | Designed | Committee workspace, `AFRP-Committee-Workspace.md` §2 (P1): seats with term ends and expiry follow-ups, the drive link per body; slice CW1 |
| B11 | Deputy President: Club Presidents' monthly call, club health, a buddy system, dormant and new clubs | FED2 §C | Partly built | Club lens roll-up; dormant-club dues (D6). The calls are outside. The buddy system is club-to-club pairing, not member referral (P4 is the referral) |
| B12 | Young people on every committee | MIN Mar 2020 | Outside · Designed | A by-law matter; the register can report each body's age mix as bands under the floor (P1 §2.6), offered |
| B13 | Fiscal year | MIN Feb 2020 (proposed Jan–Dec) | Built | The 2024 text keeps June–May (8.7.2); the engine follows the text |
| B14 | Strategic Plan Committee composition | By-Law 7.3.3 | **Gap** | Deputy President chairs, plus four members appointed by the DP with Board approval. The 2026 roster should be checked against it; the register will show the mismatch (P1 §7) |

## C. Administration and staffing

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| C1 | Executive Director | SP19, MIN 2020–23, SP26 | Outside · Designed | The hire is outside. `AFRP-Executive-Director.md` (P16): a seat with a grant bundle whose every line cites a clause or a Board decision; the 7.9.3 read as a named-purpose act with an audit line (Q-44's shape); slices ED1–ED4. By-law: must reside in the HQ metro area (Const. V §3, 7.9.7) |
| C2 | Program Coordinator | SP19 | Outside | Hired in 2019; a functional seat on the office map, P16 §5 (Q-142) |
| C3 | Communications Coordinator, manager or intern | FED2 §A, PR | Outside | The comms desk is the tool that role would use; a functional seat on the office map, P16 §5 (Q-142) |
| C4 | File organisation and archives; a central document repository | SP19, SP26 | Partly built · Designed | Registries and the magazine archive are built. Committee and strategic-plan records are `AFRP-Committee-Workspace.md` (P1). **Decided (D66):** the shared drive is the archive of record; the platform links to it. Incident response and retention: `AFRP-Incident-Response-and-Retention.md` (P15); the drive's retention is the Board's (Q-76). The Executive Director's seat is offered as custodian of the platform's registers, the Executive Secretary of the drive (P16 §5; Q-137) |
| C5 | Every membership payment recorded and cross-referenced by family and Manara | FED2 §C | Built | One ledger with daily close |
| C6 | Welcome packages for Board and committee members | MIN 2020, FED2 Part IV §C (the Board letter), §E, §H, §I (the committee content) | Designed | Letters, `AFRP-Letters-and-Onboarding.md` §5 (P3): the package page read from the registers; slice LT2 |
| C7 | Staffing in Ramallah, the US, or both | MIN 2022 | Outside | — |

## D. Membership, database and the app

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| D1 | A central member database ("No database/CRM" in the 2018 SWOT) | SP19, FED2, MIN | Built | The platform is this element. It replaces a landscape in which a member is five to seven unlinked records (Dynamics 365, per-club Breeze, Mailchimp and others) |
| D2 | Services to local clubs; connectivity among clubs | SP19 | Partly built · Queued | Club lens; Breeze parity B1–B2 built, B3–B6 queued |
| D3 | Business intelligence and retention rates | SP19 | Partly built | Reporting built; conversion designed |
| D4 | Member-only information behind a password | SP19 | Built · Designed | Passwordless sign-in; members-only directory; nothing about the living without sign-in (D28). The directory's three formats (members with membership and club shown, professional services, the leadership seats) are design note P19, on-platform only; "near me" is Q-48; a member's own access, correction, erasure and copy requests (P15 §4; Q-140) |
| D5 | Dues online, including the Manara tier with automatic renewal | SP19 | Partly built | Join and renewal built. Manara renewal refuses until the Board Rules & Regulations are on file |
| D6 | Getting members registered on the new system | MIN Sep 2023 | Built · Queued | Join wizard built; email provider is slice 5 |
| D7 | Clubs drive national sign-ups; families refer non-member Ramallah families | MIN Sep 2023 | Designed | Referral into the club's follow-ups, `AFRP-Family-Referral.md` (P4): rests on B1's follow-ups and C2's contact record; slices RF1–RF3; sending is gated on Q-68 |
| D8 | Benefits for long-time members and sponsors | MIN Sep 2023 | Proposed · Outside | The recognition-tiers register exists; the benefits are a Board decision |
| D9 | Member demographics | MIN Mar 2023 | Built | Member 360, household |
| D10 | Mass communication to members | MIN Mar 2023 | Partly built | Comms desk; email provider gated (slice 5) |
| D11 | Training for local clubs | MIN Mar 2023 | Outside | — |
| D12 | An operations and maintenance budget for the system | MIN Mar 2023 | **Gap** | Who maintains the platform after launch, and who pays, is in no document (Q-15); P16 §8 gives Q-15 a shape; it gates IR5 (backups and the store register) |
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
| E1 | One consistent message across every channel | PR, FED2 §A | Partly built | Comms desk and website desk; the strategy itself is outside; the approver seat for public statements is open (Q-80) |
| E2 | A newsletter on a fixed schedule | PR audit, FED2 §A | Proposed | A cadence on the comms desk (after slice 5) |
| E3 | A clearer website | PR audit | Built | Public site rebuilt on the design system; its content review is pending |
| E4 | Website handed to emerging leaders | SP19 SWOT | Outside | — |
| E5 | Social media metrics | PR audit | Outside | A scheduling tool, not the platform |
| E6 | Press releases: proactive and reactive, a 24-hour clock, a media list | PR | Designed | Press workflow, `AFRP-Press-Workflow.md` (P6): the statement as one object, the media list on the institution registry; slices PR1–PR2; the 24-hour clock is the 2020–21 proposal's figure, held as a parameter; the approver seat is the one gate (Q-80) |
| E7 | Spokespersons, a storyteller bank, writers, club correspondents, social-media volunteers | PR, MIN 2020–22 | Designed | Volunteer interests on the member profile, `AFRP-Volunteer-Interests.md` (P7): interests, rosters, the ask, screening rows; slices VI1–VI4; the spokesperson seat is defined in P6 §4 and filled by P7 |
| E8 | A record of Palestinian-American accomplishment | FED2 §A | Proposed | A Heritage branch item, if wanted |
| E9 | Annual report | SP19, MIN Dec 2020 | Proposed | Drawn from reporting |
| E10 | Brand guide and its enforcement | FED2 §A | Built | The design system |

## F. Programmes

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| F1 | A youth pipeline from childhood to professional life | SP19, FED2 | Built | Education (ladder by age) and Leadership (ladder by capacity) branches |
| F2 | Camp Ramallah: more campers from small communities, more age tiers, a site of its own | SWOT25 | Built | Camp application, selection, roster and camperships (slices 2 and 2b); the age tiers and a site are Federation decisions |
| F3 | Project Hope: formal processes, succession, one trip per person | SWOT25, flyer | Partly built · Designed | Programme template built; the selection cycle is `AFRP-Selection-Programmes.md` §2 (P12; slices SEL1–SEL5); the one-trip rule is not in the rules register — a fact, raised as Q-116 |
| F4 | Leadership Ramallah with the Mid-Year | SP19 | Plan only · Designed | Register row and programme plan (slice P1); the pairing is modelled as a Mid-Year sub-event (P8 §6, P12 §2.7) and two optional Mid-Year agreement rows (P13); whether standing is Q-92 |
| F5 | Exchange Mission: missions, alumni database, fellowships, alumni newsletter | SP19, SWOT25 | Partly built · Designed | Alumni match queue built (slice 9); the mission's and the Fellowship's cycles are `AFRP-Selection-Programmes.md` §2 (P12); fellowship applications are not in the record (Q-119); the alumni newsletter is a consent-only segment (Q-120) |
| F6 | Women to Women: projects, younger women, a representative per city | SWOT25 | Partly built | Care branch; giving through funds. Which entity runs it is open (`AFRP-Program-Architecture.md` §0) |
| F7 | RBPN five-year plan: mentorship, ambassadors, conferences | SP19 | Built | Sponsorship desk and job board (slices 10, 10b); mentorship not in the record — the *mentor* interest term is the pool (P7); the Ramallah posting is the job board's posting with a work location (P17 §3.2; Q-155) |
| F8 | Cultural Preservation: digitisation, oral histories | SP19 | Designed | Heritage branch |
| F9 | Scholarships | SP19, flyer | Built | Scholarship committee engine (slice 4). The 2015 policy statement is found (Q-2); the committee's Foundation seats conflict with D3 (Q-29) |
| F10 | Medical Mission and human services | SP19 | Designed | ARFHSN roadmap. Intake of ARFHSN's records (Sep 2026) found grant-making, partner agreements and mission workflows the record does not hold; Q-21 to Q-26; P11 written (`AFRP-Care-Grants-and-Partners.md`); credential verification is Q-87 |
| F11 | Recruit 21–35 year-olds through RBPN; youth leaders in each club | MIN Mar 2023 | Partly built | Leadership branch; age-band reporting designed; the Ramallah posting is the job board's posting with a work location (P17 §3.2; Q-155) |
| F12 | Programme alumni event at the Convention | MIN Mar 2023 | Proposed | An event type fed by alumni segments (P12 §2.9's segments are its feed) |
| F13 | Care grant-making: a request with quotes, a Board vote with a ceiling, payment on delivery, delivery confirmed | INTAKE26 | Designed | D63 sets the rule: the holding entity's Board approves with a ceiling, two signatories pay on delivery, and a grant closes only with the partner's signed agreement, a delivery confirmation and an inventory of equipment. The grants register is `AFRP-Care-Grants-and-Partners.md` §2 (P11; slices CG1, CG3); it also produces ARFHSN's six-monthly report to the AFRP Board (CG4) |
| F14 | Partner agreements with renewal dates | INTAKE26 | Designed | An agreements register with renewal reminders, serving every programme with an outside partner; a signed agreement is required before a Care grant closes (D63). `AFRP-Care-Grants-and-Partners.md` §3 (P11; slice CG2); the prosthetics renewal overdue (Sep 2026) |
| F15 | The Relief Fund: monthly support to families in Ramallah since 2020, run by the Federation beside ARFHSN's own funds | INTAKE26, MOU | Designed | A fund on the funds ledger, `AFRP-Care-Grants-and-Partners.md` §4 (P11; slice CG5 gated). Its holding entity is still Not stated (Q-109) with the deductibility consequence; the per-registration Convention amount is a field on the agreement row (P8 §4, P13 §2.2), and whether it applies after 2025 is Q-126 |
| F16 | The receipting entity for affiliate gifts | INTAKE26 | Designed | ARFHSN receipts the Medical Mission and Human Services Network gifts it holds; the Federation's giving pages collect them as its agent (D56, settling Q-21). Each programme's holding entity follows the approved budget (D55). P9 extends D56's question to ARFECF's funds (Q-100) |
| F17 | Safeguarding funds and equipment delivered in Ramallah | INTAKE26 | Designed | An inventory of any equipment is on record before a Care grant closes (D63; `AFRP-Care-Grants-and-Partners.md` §2, inventory as a closing record). Inspections and the local committee are outside the platform (P11 §7; Q-24 carried) |

## G. Events and the Convention

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| G1 | Mid-Year guidelines: host bids ~13 months ahead, schedule, room block, fees | FED2 §B | Designed | Host-bid workflow, `AFRP-MidYear-Host-Bids.md` (P8; slices HB1–HB4); events built; HA3 (P13) for the Mid-Year event's agreement link |
| G2 | Convention guidelines | FED2 §B, MOU | Designed | The Convention element; host bid and agreement P8; P13 §7's four templates |
| G3 | MOU terms: host two years ahead; registration data belongs to the Federation; Relief Fund per registration; dues folded into non-member registration; the Federation's share and 60-day settlement | MOU | Designed | Convention element and class CONV68; the settlement is club plan §5 and the settlement statement is `AFRP-Host-Agreements.md` §4 (P13); the terms are P13 §2; the bid and the agreement row are P8 |
| G4 | Welcome session for new members at special events | MIN Dec 2020 | Designed | Letters and onboarding, `AFRP-Letters-and-Onboarding.md` §6 (P3): an event type; slice LT3 |
| G5 | Online registration run with the host club | FED2 §B | Partly built | Events built; Convention designed; host bid and agreement P8 |

## H. Finance and fundraising

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| H1 | Finance Committee approves budgets | SP19 | Partly built · Designed | Ledger built; the committee's own workspace is `AFRP-Committee-Workspace.md` (P1; slices CW1–CW3) |
| H2 | A web presence that helps fundraising | SP19 | Built | Funds path |
| H3 | An endowment campaign | SP26 | Designed | `AFRP-Fund-Rules.md` §7 (P9): the campaign's pledges, tiers as segments, receipting entity Q-100; the endowment's entity and rule at the 4 November 2026 Boards (Q-35) |
| H4 | "Charitable giving unacknowledged" | SP19 SWOT | Designed | Four contributor moments and an annual statement (D10) |
| H5 | A budget line per programme | SP19 | Designed | Typed budget line (`AFRP-Program-Architecture.md` §3); the line is released against the year's distribution by holding entity (P9 §4 step 7) |
| H6 | Grant-writing | MIN Sep 2023 | Outside | — |

## I. Government relations and advocacy

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| I1 | Decide whether policy work fits the mission | SP19 | Built | Settled in practice: Congressional Outreach sits on the Leadership branch; the Government Affairs Committee is the paragraph under By-Law 8.15 (Q-50 carries the drafting item); public statements on legislation are AFRP's under D65, the affiliates' refused (P6 §6) |
| I2 | Elected-official relations; a stronger advocacy voice | TASKS, SWOT25 | Designed | Positions, contacts with offices, the outreach register, alerts and members' own advocacy, the lobbying record — `AFRP-Advocacy.md` (P14; slices AD1–AD5); public statements on legislation are AFRP's under D65, the affiliates' refused (P6 §6) |

## J. One Federation

The goal, in the project owner's words: clubs, the Federation and the affiliates
share programmes, initiatives and the four core functions. These rows are what
the Federation's and the affiliates' working files (INTAKE26) show of that
sharing today.

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| J1 | Clubs co-fund Care work: a club's yearly gift to a Care programme, club appeals passed through ARFHSN, a club or committee fund held in ARFHSN's books | INTAKE26 | Designed | Co-funding of Care grants is a line on the club's statement, and a co-funded grant lists each club's share (D57). The money sits with the holding entity (D55, D56). The grants register is `AFRP-Care-Grants-and-Partners.md` §6 (P11); slice CG1 lists each club's share |
| J2 | One club cost-share rule across programmes: camp rebates, Leadership Ramallah travel shares, RBPN event reimbursements, Arabic volunteers | INTAKE26, SWOT25 | Designed | One club-share statement on the funds ledger; each programme sets its own terms (D57, settling Q-30). Design note P10 |
| J3 | Club–Federation money on one statement: dues, convention settlement, ad-book share, Mid-Year sponsorship, grants to clubs, event amounts due to a club | INTAKE26, MOU | Partly built · Designed | The remittance ledger for dues is built (D1). The single statement per club is decided (D57) and designed: one account per club per holding entity, sixteen line types each tied to a programme term, a run with a query hold and an immutable close (`AFRP-Club-Experience-Plan.md` §5). The terms no committee has written are Q-47 |
| J4 | Clubs in the affiliates' governance: ARFECF's Board seats spread over three regions defined by lists of clubs (2015) | INTAKE26 | Designed · Outside | The ARFECF Board-composition check reads the regional seats (`design/bylaws/ARFECF-2015-and-the-fund-policies.md`). The club lists are out of date and are the ARFECF Board's to bring current. The clubs' place in the Federation's own governance waits on the 2026 restatement (Q-33) |
| J5 | Named shared services, and what each club gives up for them: the member database and registration, video calls, the newsletter and the Magazine, by-law templates, the monthly club presidents' meeting | SP19, FED2, INTAKE26 | Partly built · Proposed | The member database, registration, the comms desk and the magazine are built; the club tools replacing Breeze are built in part (B1–B2) and queued (B3–B6). Which club tool each shared service replaces, and what a club gives up, is now written (Club Experience Plan §8.6, §9.1; Breeze Parity §1a). Club governance features wait on Q-33 |
| J6 | The dues rule: who collects club dues, whether a member may opt out, and when they pass to the club | INTAKE26, MIN | Built · Outside | Club-collected AFRP dues are held as agent and remitted on the ledger (D1). No Federation document in seventeen years writes the rule down (Q-36); D57 keeps D1 and shows it on the club's statement. The CPA's confirmation of the agency treatment is outside (Q-3) |
| J7 | The convention host agreement as the shared rule between the Federation and a host club | MOU, INTAKE26 | Designed | Every Convention runs under a signed host agreement; its terms sit on the event and the platform produces the settlement statement; the same shape serves the Mid-Year (D59, settling Q-34). The bid and the agreement row are `AFRP-MidYear-Host-Bids.md` §4 (P8); the row's terms, schedules and settlement statement are `AFRP-Host-Agreements.md` (P13) |
| J8 | A club attribution on every gift | INTAKE26 | Designed · Proposed | Every gift, from anyone, may carry a club attribution (D57). Today nothing records which club raised or co-funded what (Q-25). Design note P10 |
| J9 | The officer year: the affiliation form by 1 August, the Council and Board seats that derive from it, the hand-over | BL24, INTAKE26 | Designed | The officers form is the By-Law 3.2 filing and the source of every seat derived from it; a dated hand-over carries the balance and the open items (`AFRP-Club-Experience-Plan.md` §4.1, §6.2). No affiliation form is on file for any year; who approves affiliation is Q-40. Under the Q-33 gate |
| J10 | The club's seat in each programme: the camp liaison, the RBPN ambassador, the travel coordinator, the magazine correspondent | INTAKE26 | Designed · Proposed | A programme seat scoped to one club, appointed on the officers form or by the committee, each appointment naming who made it (Club Experience Plan §3.4, §7). Only RBPN names such a seat with a term today; who appoints is Q-45 |
| J11 | Moving each club off Breeze, and the clubs on no system onto the platform | INTAKE26, ADD2 | Designed · Proposed | One club at a time with a named owner on each side; read-only access; identity resolution with a human on every doubtful pair; a parallel run on the platform's screens; a dated cutover (Club Experience Plan §8; workflow `club-migration`). The deep read of Breeze (1 Oct 2026) fixed the path's constraints: the key is the club's account owner's, the API is unsupported and rate-limited, attendance moves only through it, and the account is deleted on cancellation (Breeze Parity §1a). Which club goes first is David's (Breeze Parity §5 q4) |
| J12 | The Federation's view of its clubs: every club as counts, and the year-one baseline per club | INTAKE26, SP19 | Partly built · Designed | The clubs page in the Federation lens: standing, membership, club life, the Federation's work in the club, the statement balance, the migration state, every cell under the floor (Club Experience Plan §10; D67). The first version of the roll-up is built (B1) |

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

## Design notes

Every note is written as of 1 October 2026 (P10 inside P18). Each slice row in
`plan/MASTER-PLAN.md` §2 names its note and its gate.

| # | Design note | Covers | Status |
|---|---|---|---|
| P1 | Committee workspace and reporting | A3, B8–B10, C4, H1 | **Written** (`AFRP-Committee-Workspace.md`, 1 Oct 2026): bodies, seats, workspace, reports, the Board packet; slices CW1–CW5; Q-50–Q-58 and Q-75 (the content is FED2 Part IV §E, §H, §I) |
| P2 | Annual committee planning survey | A7 | **Written** (`AFRP-Committee-Planning-Survey.md`, 1 Oct 2026); slices SV1–SV2; Q-59–Q-61 |
| P3 | Welcome, renewal and Board letters; new-member welcome | B2, C6, G4 | **Written** (`AFRP-Letters-and-Onboarding.md`, 1 Oct 2026); slices LT1–LT5; signatory and wording still open (Q-62, Q-63, Q-65) |
| P4 | Family referral into club follow-ups | D7 | **Written** (`AFRP-Family-Referral.md`, 1 Oct 2026); rests on B1's follow-ups and C2's contact record; slices RF1–RF3; Q-68 is the one gate on sending |
| P5 | Selection Committee workflow | B5 | **Written** (`AFRP-Selection-Committee-Workflow.md`, 1 Oct 2026): the cycle as objects; slices SC1–SC7; Q-73–Q-79; FED2 §G read (revision 3 May 2021), adoption record still not on file; floor nominations carried as a labelled state, not resolved |
| P6 | Press-release workflow | E6 | **Written** (`AFRP-Press-Workflow.md`, 1 Oct 2026); slices PR1–PR2; Q-70 and Q-80–Q-82; the approver of a Federation statement is not written anywhere and is the one gate |
| P7 | Volunteer interests and rosters | E7 | **Written** (`AFRP-Volunteer-Interests.md`, 1 Oct 2026); slices VI1–VI4; Q-83–Q-88 |
| P8 | Mid-Year host bids | G1 | **Written** (`AFRP-MidYear-Host-Bids.md`, 1 Oct 2026); slices HB1–HB4; Q-89–Q-94; P13 fills the agreement row HB3 generates |
| P9 | Fund rules as found: the annual distribution on the 31 May valuation, the emergency transfer, restricted gifts, the entity for each fund | H3, H5, F16 | **Written** (`AFRP-Fund-Rules.md`, 1 Oct 2026): six slices FR1–FR6; Q-35 and Q-95–Q-103. Both policy statements and the 2015 by-laws are on file (`design/bylaws/ARFECF-2015-and-the-fund-policies.md`); the endowment's holding entity waits on the 4 November 2026 boards (Q-35) |
| P10 | Club share and settlement: one statement per club on the funds ledger | J1, J2, J3, J6, J8 | **Written** as `AFRP-Club-Experience-Plan.md` §5 (1 Oct 2026): one account per club per entity, the line types, the run and the close. D57 and D1 |
| P11 | Care grants and partner agreements | F13, F14, F15, F17, J1 | **Written** (`AFRP-Care-Grants-and-Partners.md`, 1 Oct 2026): six slices CG1–CG6; Q-104–Q-114; the Relief Fund's entity is not stated (Q-109) |
| P12 | Selection programmes and the Arabic term | A8, F3, F4, F5 | **Written** (`AFRP-Selection-Programmes.md`, 1 Oct 2026): the four selection cycles and the Arabic term; slices SEL1–SEL5 and AR1–AR4; Q-70, Q-76, Q-92 and Q-115–Q-123; the reading of D61 at a future cycle's door is put to David (Q-118) |
| P13 | Host agreements for the Convention and the Mid-Year | G1, G3, J7 | **Written** (`AFRP-Host-Agreements.md`, 1 Oct 2026): the terms, schedules, settlement statement, disputes and archive of the row HB3 generates; slices HA1–HA6; Q-92 and Q-124–Q-130 |
| P14 | Advocacy and the Day of Action | I1, I2 | **Written** (`AFRP-Advocacy.md`, 1 Oct 2026): advocacy as objects; the Day of Action on P12's engine; the lobbying register for D65's condition; slices AD1–AD5; Q-70 and Q-131–Q-136 |
| P15 | Incident response and data retention | C4, D4 | **Written** (`AFRP-Incident-Response-and-Retention.md`, 1 Oct 2026): the incident object, the law register, the retention schedule with attested/proposed/silent rows, a DRAFT policy for the Board; slices IR1–IR5; Q-70, Q-76 and Q-137–Q-141 |
| P16 | The Executive Director as staff | C1 | **Written** (`AFRP-Executive-Director.md`, 1 Oct 2026): the seat, the grants module by module, the 7.9.3 named-purpose read, the Executive Assistant, the office map, the hire's record, succession, the maintainer question; slices ED1–ED4; Q-15, Q-44, Q-56, Q-65 and Q-142–Q-146 |
| P17 | AFRPWorks | A8 | **Written** (`AFRP-AFRPWorks.md`, 1 Oct 2026): the programme page; employer, posting, candidate (a D60 contact record), introduction (brokered), fee as a blank, owner as a body once named, pilot as a dated cycle with D67 counts; the Legal Advisor's four matters; slices AW1–AW4; Q-147–Q-157 |
| P18 | The club experience plan: the people of a club, the club workflows, the club–Federation statement, the migration from Breeze club by club | J1–J12, D7, G1, G3 | **Written** (`AFRP-Club-Experience-Plan.md`, 1 Oct 2026, fourteen sprints; reviewed and applied). Rests on D1, D57, D59, D61, D66 and the Breeze parity note; B3–B6 stay gated on Breeze Parity §5 |
| P19 | The directory in three formats: the members' directory with membership and club identified at Federation and club scale, the professional services directory, the leadership directory of seats and their votes | D4, B8, F11 | **Written** (`AFRP-Directory-Formats.md`, 1 Oct 2026): on-platform only, members only, votes as a property of the seat (David's direction); slices DIR1–DIR3; Q-48, Q-49 |
| P20 | The club journeys: what a club officer does in Breeze today, what the same person does on the platform, the rule, the refusal, the class, the slice — the corpus the clubs component is built from | J5, J9, J10, J11, J12, D7 | **Written** (`AFRP-Club-Journeys.md`, 1 Oct 2026): fifty-two journeys in twelve groups; ten guarded by named gates |

## Gaps the record cannot close alone

1. **Ramallah Works** (A8). **Done (D64):** identified as AFRPWorks and placed on the Leadership branch.
2. **The Presidential Advisory Council** (B6): proposed in FED2; adoption unknown.
3. **Strategic Plan Committee composition** (B14) against By-Law 7.3.3.
4. **Who maintains and pays for the platform** (D12).
5. **The archive of record** (C4). **Done (D66):** the shared drive is the archive of record.
6. **FED2 itself**: which revision was adopted at Jacksonville in 2021. It names
   living people, so it is cited here and not committed.
