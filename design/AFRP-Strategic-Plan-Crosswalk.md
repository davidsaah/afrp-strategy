# AFRP strategic plan crosswalk
### Every element of the Federation's strategic plans, and what the platform does about each

**Date:** 30 September 2026; section J, rows F13–F17 and notes P9–P17 added 1 October 2026; the second research round's evidence, rows D23, F18, G6, H7, H8 and I3, and the section on the committee's Doc added 2 October 2026; notes P21–P27 added the same day; P28 (the family tree module, from D68–D74) added the same day
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
| **[INTAKE26](https://drive.google.com/drive/folders/1mlUdsgoW-vTI2Ugk-xxmJGb-mGKUq8JW)** | The Federation's and the affiliates' working files: the Federation's own folder, ARFECF's folder, ARFHSN's folder and the officer archive, 2009–2026 | Read September–October 2026 | Working files in the Federation's drive, read through the intake process (D54). They name living people and hold figures, so the public record carries role-only summaries and folder-level links only. A second round on 2 October 2026 added the Board's and the Executive Committee's minutes, mail, the public site and public filings; what it found against the record is in the Decisions Register's conflicts section |

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
| A8 | Refresh priorities: Camp Ramallah, Government Affairs, Arabic classes, Ramallah Works, Family Tree | SP26, INTAKE26 | Partly built · Designed | All five are on the branches. The Arabic term is designed in `AFRP-Selection-Programmes.md` §3 (P12; slices AR1–AR4). **Ramallah Works** is AFRPWorks, the Ramallah Jobs Initiative, placed on the Leadership branch under AFRP (D64); design note P17 (`AFRP-AFRPWorks.md`): a programme page and four gated objects on the job board already built; eleven questions, most the working group's; its owner and fee model are the working group's. **Research (2 Oct 2026):** the sources show AFRPWorks run from the Executive Committee, with a working-group prototype and approved employers browsing (Q-147); the Family Tree kept in a desktop genealogy file not held by the Federation, with one approver (Q-200, Q-201); Government Affairs running local action committees in the clubs and its own tracker (Q-131, Q-183); no written camp screening policy on file (Q-86, Q-165); and the public Arabic page open to members only, against D60 (Q-171). AFRPWorks against P17 in practice: `AFRP-Leadership-Pipeline.md` §2.6 (P25) |

## B. Governance and constitution

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| B1 | Constitutional review: board size, term limits, committee viability | SP19 | Built | By-laws engine; `bylaws-2012.2` in force, `bylaws-2024.1` in parallel with 48 provisional overrides |
| B2 | Enforce Board eligibility; letters to members out of compliance | MIN Feb–Mar 2020 | Partly built · Designed | Good standing is computed (built); the letters are `AFRP-Letters-and-Onboarding.md` §4 (P3; slice LT2) — a notice ends no seat and changes no vote; no attendance notice until Q-53 |
| B3 | A parliamentarian and a three-minute speaking limit at Board meetings | MIN Feb 2020 | Partly built · Proposed | The live floor is built; a speaking timer is not in the record |
| B4 | Executive board, advisory board and executive committee structure | MIN Feb 2020 | Outside | A by-law matter; the engine reads whatever is adopted |
| B5 | **Selection Committee** replacing Nominations, Credentials and Elections | FED2 §G; By-Law Art. XVII, INTAKE26 | Partly built · Designed | The engine carries the 2024 ruleset row; the Article XVII workflow (vacancy → application → eligibility → interview → slate → certification) is `AFRP-Selection-Committee-Workflow.md` (P5; slices SC1–SC7). Two gates stay in the row: which FED2 revision was adopted (Q-17) and what 17.1.1 gates, Divergence item 9 (Q-75). **Research (2 Oct 2026):** the Legal Advisor described delegate voting in May 2026: each community certifies its paid members, they elect delegates, and a member present votes in person with the vote deducted from a delegate's total. The quorum rule and how a community's vote is held and recorded are still unwritten (Q-37) |
| B6 | Presidential Advisory Council of the three immediate Past Presidents | FED2 §C | **Gap** | Not in the 2024 by-law analysis. Whether it was adopted is unknown; P1 §7 carries it — not a body on the register until constituted |
| B7 | Officer and Executive Committee job descriptions tied to by-law sections | FED2 §C | Partly built | Roles and exact grants are built; the descriptions themselves are proposed content |
| B8 | Committee chair and member descriptions; minutes within 30 days; review after two unexcused absences | FED2 Part IV §E, §H | Designed | Committee workspace, `AFRP-Committee-Workspace.md` §3 (P1): the minutes link with the 30-day clock, attendance as marked, the third-absence review prompt; slice CW2 |
| B9 | Quarterly committee report and programme report templates | FED2 Part IV §I | Designed | Committee workspace, `AFRP-Committee-Workspace.md` §4 (P1): reports generated with only two typed fields; slice CW3 |
| B10 | Staff give chairs database access to committee documents and track members' terms | FED2 Part IV §E | Designed | Committee workspace, `AFRP-Committee-Workspace.md` §2 (P1): seats with term ends and expiry follow-ups, the drive link per body; slice CW1 |
| B11 | Deputy President: Club Presidents' monthly call, club health, a buddy system, dormant and new clubs | FED2 §C, INTAKE26 | Partly built | Club lens roll-up; dormant-club dues (D6). The calls are outside. The buddy system is club-to-club pairing, not member referral (P4 is the referral). **Research (2 Oct 2026):** the sources show Breeze onboarding presented as a Federation initiative for every club (Q-230), and three different counts of clubs in use (Q-229) |
| B12 | Young people on every committee | MIN Mar 2020 | Outside · Designed | A by-law matter; the register can report each body's age mix as bands under the floor (P1 §2.6), offered; the path from a high-school senior to a Board seat is `AFRP-Leadership-Pipeline.md` §3 (P25) |
| B13 | Fiscal year | MIN Feb 2020 (proposed Jan–Dec) | Built | The 2024 text keeps June–May (8.7.2); the engine follows the text |
| B14 | Strategic Plan Committee composition | By-Law 7.3.3 | Outside | Deputy President chairs, plus four members appointed by the DP with Board approval. Confirmed by the project owner, 1 Oct 2026: the roster follows By-Law 7.3.3 (Q-14); the register shows any later mismatch (P1 §7) |

## C. Administration and staffing

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| C1 | Executive Director | SP19, MIN 2020–23, SP26, INTAKE26 | Outside · Designed | The hire is outside. `AFRP-Executive-Director.md` (P16): a seat with a grant bundle whose every line cites a clause or a Board decision; the 7.9.3 read as a named-purpose act with an audit line (Q-44's shape); slices ED1–ED4. By-law: must reside in the HQ metro area (Const. V §3, 7.9.7). **Research (2 Oct 2026):** the hire's applicants are held outside the Federation's systems by design, to avoid conflicts of interest; only the outcome is recorded (P16 §7) |
| C2 | Program Coordinator | SP19 | Outside | Hired in 2019; a functional seat on the office map, P16 §5 (Q-142) |
| C3 | Communications Coordinator, manager or intern | FED2 §A, PR | Outside | The comms desk is the tool that role would use; a functional seat on the office map, P16 §5 (Q-142) |
| C4 | File organisation and archives; a central document repository | SP19, SP26, INTAKE26 | Partly built · Designed | Registries and the magazine archive are built. Committee and strategic-plan records are `AFRP-Committee-Workspace.md` (P1). **Decided (D66):** the shared drive is the archive of record; the platform links to it. Incident response and retention: `AFRP-Incident-Response-and-Retention.md` (P15); the drive's retention is the Board's (Q-76). The Executive Director's seat is offered as custodian of the platform's registers, the Executive Secretary of the drive (P16 §5; Q-137). **Research (2 Oct 2026):** the sources show the archive drifting across four places — the drive, the scanning vendor's files, a stand-alone website now down, and a volunteer's prototype archive-and-tree site (Q-190). The archive index under D66 is `AFRP-Family-Tree-In-Practice.md` §7.2 (P27, FT4, folded into P28's T2h) |
| C5 | Every membership payment recorded and cross-referenced by family and Manara | FED2 §C | Built | One ledger with daily close |
| C6 | Welcome packages for Board and committee members | MIN 2020, FED2 Part IV §C (the Board letter), §E, §H, §I (the committee content) | Designed | Letters, `AFRP-Letters-and-Onboarding.md` §5 (P3): the package page read from the registers; slice LT2 |
| C7 | Staffing in Ramallah, the US, or both | MIN 2022 | Outside | — |

## D. Membership, database and the app

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| D1 | A central member database ("No database/CRM" in the 2018 SWOT) | SP19, FED2, MIN, INTAKE26 | Built | The platform is this element. It replaces a landscape in which a member is five to seven unlinked records (Dynamics 365, per-club Breeze, Mailchimp and others). **Research (2 Oct 2026):** the sources show today's CRM holding non-members as vetted contacts with a profile and no consent or retention rule, its occupation field already used for outreach (Q-70, Q-236); the Board recorded in May 2026 that there is no central mechanism to track membership standing. Non-members are row D23 |
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
| D16 | Convention and Mid-Year registration and photographs | APP, INTAKE26 | Partly built · Proposed | Events built; Convention designed; a past-events gallery is not in the record. **Research (2 Oct 2026):** the registration system's event-coordinator role gives a host every guest's contact details, an export and a payment-by-payer report; the record's design is narrower (P13 §2.4; Q-127) |
| D17 | News, press releases, statements, media links, resources | APP | Partly built · Proposed | Website desk built; a press and statement archive is not in the record |
| D18 | Hathihe Ramallah in the app | APP, INTAKE26 | Built · Queued | Magazine archive; operations slices 7–7b. **Research (2 Oct 2026):** the sources show a bimonthly issue made by a staff of five roles with a correspondent per city, paid obituaries and a subscriber ledger kept outside the CRM (Q-193, Q-196); the Magazine's own board under By-Law 6.7.1 is not evidenced (Q-192). **Written (P24):** `AFRP-Magazine-Operations.md` — the issue cycle as run on the built issue module, announcements as they arrive, the subscriber ledger and its one reconciliation, the issue's hand-offs, the back-issue register and the two live stores; slices MG1–MG7; Q-249, Q-250 |
| D19 | Pay on the web, not in the app (avoids the app-store cut) | APP, MIN Dec 2020 | Built | All payment is on the web |
| D20 | Ads shown to members who have not paid dues | APP, MIN Dec 2020 | Outside | Not proposed. The ads desk (A1 frame) sells magazine and programme-book placements instead |
| D21 | Magazine money kept apart from Federation money | MIN Dec 2020, By-Law 6.7.1, INTAKE26 | Built | Multi-entity ledger; purpose on every line. Conflict recorded (2 Oct 2026): By-Law 6.7.1 has the Federation appropriate the funds to guarantee the Magazine's publication, and General Fund magazine lines show money crossing; kept-apart is the 2020 practice, not the text (Q-194). P24 §6 builds the Federation's appropriation as a typed AFRP→ARFECF act citing the budget line and 6.7.1, refused until Q-194 |
| D22 | Family tree in the app, with correction forms and GEDCOM updates | APP, INTAKE26 | Built | GEDCOM round-trip, hourglass, committee queue (D11–D22, D30–D37). Corrections go to a committee, not to one person. **Research (2 Oct 2026):** the sources show the master file in a desktop genealogy product under an account not in the Federation's name, every change applied by one project lead, and the clan books served to approved requesters rather than by standing (Q-200 to Q-202); a second archive-and-tree site was prototyped in July 2026 (Q-190). The migration of the two doors (the public form and e-mail) into the committee queue is `AFRP-Family-Tree-In-Practice.md` §4 (P27; slices FT1–FT6). **Decided (2 Oct 2026, D68–D74):** the tree in the book's plate grammar, the Hub as its record after a parallel run, members in standing proposing, the living in full inside one's own branch, committee approval in tiers with clan stewards, membership and join first: `AFRP-Family-Tree-Module.md` (P28; slices T2-0, T2-R, T2a–T2h) |
| D23 | Non-members the Federation knows: applicants, guests, one-off donors, prospects, media, offices | INTAKE26 | Designed | D60's contact record (name, verified channel, consent) is the designed shape, reused by six notes (Q-70). The sources show non-members held today as CRM contacts without a membership, rows in sheets and trackers, club Breeze profiles and mailboxes, and two of them already used for outreach (Q-236). Which lists move onto the record is Q-76; the club's view, Q-237. **Written (P21):** `AFRP-Contact-Record.md` — one person record with dated, scoped roles, consent per role and class, matching and merging, retention per role and what a club sees; the learner role on D60, every other role switched on by Q-70, whose DRAFT register wording is in P21 §11 (not adopted); slices CR1–CR7; guests Q-238, non-member subscribers Q-239 |

## E. Communications

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| E1 | One consistent message across every channel | PR, FED2 §A | Partly built | Comms desk and website desk; the strategy itself is outside; the approver seat for public statements is open (Q-80) |
| E2 | A newsletter on a fixed schedule | PR audit, FED2 §A | Proposed | A cadence on the comms desk (after slice 5) |
| E3 | A clearer website | PR audit | Built | Public site rebuilt on the design system; its content review is pending |
| E4 | Website handed to emerging leaders | SP19 SWOT | Outside | — |
| E5 | Social media metrics | PR audit | Outside | A scheduling tool, not the platform |
| E6 | Press releases: proactive and reactive, a 24-hour clock, a media list | PR | Designed | Press workflow, `AFRP-Press-Workflow.md` (P6): the statement as one object, the media list on the institution registry; slices PR1–PR2; the 24-hour clock is the 2020–21 proposal's figure, held as a parameter; the approver seat is the one gate (Q-80) |
| E7 | Spokespersons, a storyteller bank, writers, club correspondents, social-media volunteers | PR, MIN 2020–22, INTAKE26 | Designed | Volunteer interests on the member profile, `AFRP-Volunteer-Interests.md` (P7): interests, rosters, the ask, screening rows; slices VI1–VI4; the spokesperson seat is defined in P6 §4 and filled by P7. The Magazine already works through a correspondent per city; whether that is a club seat is Q-195. The correspondent seat and the assisted submission are `AFRP-Magazine-Operations.md` §3.2 (P24) |
| E8 | A record of Palestinian-American accomplishment | FED2 §A | Proposed | A Heritage branch item, if wanted |
| E9 | Annual report | SP19, MIN Dec 2020, afrp.org | Outside · Proposed | The Federation publishes an annual report outside the platform (2024–25 on afrp.org); drawing it from reporting is proposed |
| E10 | Brand guide and its enforcement | FED2 §A | Built | The design system |

## F. Programmes

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| F1 | A youth pipeline from childhood to professional life | SP19, FED2 | Built | Education (ladder by age) and Leadership (ladder by capacity) branches; the path through objects the record holds is `AFRP-Leadership-Pipeline.md` §3 (P25, YL1) |
| F2 | Camp Ramallah: more campers from small communities, more age tiers, a site of its own | SWOT25, INTAKE26 | Built | Camp application, selection, roster and camperships (slices 2 and 2b); the age tiers and a site are Federation decisions. **Research (2 Oct 2026):** no written screening or training policy for camp volunteers is on file (Q-86, Q-165); campers from Ramallah and the upper age are Q-166 and Q-167 |
| F3 | Project Hope: formal processes, succession, one trip per person | SWOT25, flyer, INTAKE26 | Partly built · Designed | Programme template built; the selection cycle is `AFRP-Selection-Programmes.md` §2 (P12; slices SEL1–SEL5); the one-trip rule is not in the rules register — a fact, raised as Q-116. **Research (2 Oct 2026):** in 2024 the Board combined it with the Day of Action because travel was judged unsafe; the joint year's money and committee are Q-172 |
| F4 | Leadership Ramallah with the Mid-Year | SP19, INTAKE26 | Plan only · Designed | Register row and programme plan (slice P1); the pairing is modelled as a Mid-Year sub-event (P8 §6, P12 §2.7) and two optional Mid-Year agreement rows (P13); whether standing is Q-92. **Research (2 Oct 2026):** the sources show Leadership Ramallah and the Young Leaders Committee sharing co-chairs (Q-175) and the 2027 summit set beside the Mid-Year; the application window and cost rules are unwritten (Q-176); whether the Endowment funds it is Q-177. The 2027 joint block: `AFRP-Leadership-Pipeline.md` §4 (P25) |
| F5 | Exchange Mission: missions, alumni database, fellowships, alumni newsletter | SP19, SWOT25, INTAKE26 | Partly built · Designed | Alumni match queue built (slice 9); the mission's and the Fellowship's cycles are `AFRP-Selection-Programmes.md` §2 (P12); fellowship applications are not in the record (Q-119); the alumni newsletter is a consent-only segment (Q-120). **Research (2 Oct 2026):** no delegation has run since 2023; the committee's plan is reverse missions and a Convention symposium slot, which is the Convention committee's and the host agreement's to approve (Q-188, Q-125) |
| F6 | Women to Women: projects, younger women, a representative per city | SWOT25, INTAKE26, afrp.org | Partly built | Care branch; giving through funds. D55 makes it a sub-fund of ARFHSN. **Research (2 Oct 2026):** the sources show its gifts in ARFECF's books for one year (Q-212), the committee approving projects where D63 has the Board approve (Q-114), an endowed-fund question (Q-210), tuition awards (Q-211) and a published minimum gift and project band (Q-213). The tuition awards are kept apart from the Scholarship as a P11 grant row: `AFRP-Scholarship-Awards.md` §6.1 (P26). The `women-to-women-grants` workflow is Designed (P11 §2, §6; P26 §6.1); the row stays Partly built for the giving through funds that is built |
| F7 | RBPN five-year plan: mentorship, ambassadors, conferences | SP19, INTAKE26, afrp.org | Built | Sponsorship desk and job board (slices 10, 10b); mentorship not in the record — the *mentor* interest term is the pool (P7); the Ramallah posting is the job board's posting with a work location (P17 §3.2; Q-155). **Research (2 Oct 2026):** RBPN events now register through a video-meeting events link rather than the portal (Q-181); afrp.org lists a Mentorship Program committee in development with no members |
| F8 | Cultural Preservation: digitisation, oral histories | SP19, INTAKE26 | Designed | Heritage branch. **Research (2 Oct 2026):** oral histories are recorded against one spoken permission (Q-189); minors as volunteers is Q-191; the archive is in four places (Q-190). Oral-history consent as a written, scoped consent and the archive index: `AFRP-Family-Tree-In-Practice.md` §6, §7.2 (P27, FT4–FT5; FT4 folded into P28's T2h); living third parties Q-261 |
| F9 | Scholarships | SP19, flyer, INTAKE26, afrp.org | Built | Scholarship committee engine (slice 4). The 2015 policy statement is found (Q-2); the committee's Foundation seats conflict with D3 (Q-29). **Research (2 Oct 2026):** the 2026 award letter writes a renewal rule — two instalments a year, each released on a verified transcript, enrolment and a minimum GPA (Q-159); the letters go out in AFRP's name for ARFECF's fund (Q-158); whether the Board approves or receives the awards is Q-161; the public page says the Foundation manages the programme (Q-162); about twenty named scholarships exist with no instrument on file (Q-102). Awards and renewal are designed in `AFRP-Scholarship-Awards.md` (P26; slices SA1–SA7); the Ramallah track Q-255, renewal parameters Q-256, an appeal route Q-257 |
| F10 | Medical Mission and human services | SP19, INTAKE26, Form 990 | Designed | ARFHSN roadmap. Intake of ARFHSN's records (Sep 2026) found grant-making, partner agreements and mission workflows the record does not hold; Q-21 to Q-26; P11 written (`AFRP-Care-Grants-and-Partners.md`); credential verification is Q-87. **Research (2 Oct 2026):** ARFHSN's monthly meeting is convened by the Federation's programme director, where D62 says the President (Q-214); its by-laws are in revision (Q-220); the public no-overhead claim (Q-215) and a club's balance held as an earmark (Q-216) are questions |
| F11 | Recruit 21–35 year-olds through RBPN; youth leaders in each club | MIN Mar 2023, INTAKE26 | Partly built | Leadership branch; age-band reporting designed; the Ramallah posting is the job board's posting with a work location (P17 §3.2; Q-155). **Research (2 Oct 2026):** the sources show a Young Leaders Committee with a member per club city that does not match the By-Law 8.10 paragraph (Q-179), and no programme by the name Emerging Leaders (Q-178). Youth leaders in clubs on the path: `AFRP-Leadership-Pipeline.md` §3 (P25) |
| F12 | Programme alumni event at the Convention | MIN Mar 2023 | Proposed | An event type fed by alumni segments (P12 §2.9's segments are its feed) |
| F13 | Care grant-making: a request with quotes, a Board vote with a ceiling, payment on delivery, delivery confirmed | INTAKE26 | Designed | D63 sets the rule: the holding entity's Board approves with a ceiling, two signatories pay on delivery, and a grant closes only with the partner's signed agreement, a delivery confirmation and an inventory of equipment. The grants register is `AFRP-Care-Grants-and-Partners.md` §2 (P11; slices CG1, CG3); it also produces ARFHSN's six-monthly report to the AFRP Board (CG4) |
| F14 | Partner agreements with renewal dates | INTAKE26 | Designed | An agreements register with renewal reminders, serving every programme with an outside partner; a signed agreement is required before a Care grant closes (D63). `AFRP-Care-Grants-and-Partners.md` §3 (P11; slice CG2); the prosthetics renewal overdue (Sep 2026) |
| F15 | The Relief Fund: monthly support to families in Ramallah since 2020, run by the Federation beside ARFHSN's own funds | INTAKE26, MOU, INTAKE26 | Designed | A fund on the funds ledger, `AFRP-Care-Grants-and-Partners.md` §4 (P11; slice CG5 gated). Its holding entity is still Not stated (Q-109) with the deductibility consequence *(since 3 Oct 2026 it is AFRP, D83; the deductibility text waits on the CPA, D9)*; the per-registration Convention amount is a field on the agreement row (P8 §4, P13 §2.2), and whether it applies after 2025 is Q-126. **Research (2 Oct 2026):** the sources show the account reported by the Educational Fund Treasurer and relief gifts booked by the CPA as ARFECF's restricted gifts (Q-109); who sets the Ramallah charities list (Q-207), the giving page's purpose (Q-208), a pre-spend rule (Q-209), club relief drives (Q-180) and clubs giving directly (Q-228) are questions. **Written (P23):** `AFRP-Relief-Fund-and-Senior-Living.md` Part A — the fund row, three paths with authoriser rows, the organisation register, the representative's report of counts and the report to the Board; slices RL1–RL4; the representative's seat is Q-246 and the receiving account Q-247. The per-registration line in a unified registration is `AFRP-Convention-Operations.md` §5.3 (P22; Q-243) |
| F16 | The receipting entity for affiliate gifts | INTAKE26, INTAKE26 | Designed | ARFHSN receipts the Medical Mission and Human Services Network gifts it holds; the Federation's giving pages collect them as its agent (D56, settling Q-21). Each programme's holding entity follows the approved budget (D55). P9 extends D56's question to ARFECF's funds (Q-100). **Research (2 Oct 2026):** AFRP's chart of accounts already carries the agency pattern for every affiliate purpose it collects, not only these (Q-232). Pass-through gifts to the Ramallah Foundation's home with the receipting entity stated: `AFRP-Relief-Fund-and-Senior-Living.md` §9.2 (P23; Q-204) |
| F17 | Safeguarding funds and equipment delivered in Ramallah | INTAKE26 | Designed | An inventory of any equipment is on record before a Care grant closes (D63; `AFRP-Care-Grants-and-Partners.md` §2, inventory as a closing record). Inspections and the local committee are outside the platform (P11 §7; Q-24 carried) |
| F18 | Senior Living: the senior citizens' home in Ramallah | SP26, INTAKE26, afrp.org | Outside · Designed | The sources show the home is the Ramallah Foundation's, built and to be run by it; the Federation's part has been communications, gifts passed through ARFECF and a Convention-voted grant. Whether it is a Federation programme at all is Q-203; receipting Q-204; a club gift with signage Q-205; an agreement with the Foundation Q-206. **Written (P23):** `AFRP-Relief-Fund-and-Senior-Living.md` Part B designs the Federation's part — the Foundation on the registry, the pass-through purpose, the memorial gift and the Convention-voted budget-line payment (slices RL5–RL6) — and marks the capital campaign unoperated; the home itself is outside; recognition and the receipt is Q-248 |

## G. Events and the Convention

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| G1 | Mid-Year guidelines: host bids ~13 months ahead, schedule, room block, fees | FED2 §B, INTAKE26 | Designed | Host-bid workflow, `AFRP-MidYear-Host-Bids.md` (P8; slices HB1–HB4); events built; HA3 (P13) for the Mid-Year event's agreement link. **Research (2 Oct 2026):** the 2020–21 guideline is on file and has the Executive Committee review the bids and announce the host; in 2026–27 the Board chose after quotes and the Federation signed the hotel contract (Q-92). A Mid-Year registrant not asked for dues is Q-225 |
| G2 | Convention guidelines | FED2 §B, MOU | Designed | The Convention element, `AFRP-Convention-Operations.md` (P22; slices CV1–CV8); host bid and agreement P8; P13 §7's four templates |
| G3 | MOU terms: host two years ahead; registration data belongs to the Federation; Relief Fund per registration; dues folded into non-member registration; the Federation's share and 60-day settlement | MOU, INTAKE26 | Designed | Convention element and class CONV68; the settlement is club plan §5 and the settlement statement is `AFRP-Host-Agreements.md` §4 (P13); the terms are P13 §2; the bid and the agreement row are P8. **Research (2 Oct 2026):** the 2026 Convention was settled under a revised agreement the Board minuted and no folder holds (Q-93); the close netted amounts with no schedule row (Q-124); who does what at the close is Q-221 and the payment channel Q-222. P22 (`AFRP-Convention-Operations.md`): the close as dated acts (CV6), netted items held (Q-124), payment signatures (Q-241) |
| G4 | Welcome session for new members at special events | MIN Dec 2020 | Designed | Letters and onboarding, `AFRP-Letters-and-Onboarding.md` §6 (P3): an event type; slice LT3 |
| G5 | Online registration run with the host club | FED2 §B, INTAKE26 | Partly built | Events built; Convention designed; host bid and agreement P8; the unified registration, the membership-gate parameter and the desk are `AFRP-Convention-Operations.md` §5 (P22, CV3). The host fee routed through ARFECF is Q-224 |
| G6 | A Convention in Ramallah (2029) | INTAKE26 | Outside · Designed | The President set a path (amend the by-laws at the 2027 Convention; place Ramallah in the rotation; a steering committee, with the Federation hosting if need be) and a requirements checklist sets gates: a Board-approved budget with stop authority, an independent security assessment, counsel, insurance, a written advisory threshold no Board vote may waive, attendee risk disclosure, reviews at fixed intervals and a go, hold, relocate, postpone or cancel decision. A fourth hosting model the host-bid templates do not carry (P8 §7; Q-223). The amendment is outside; the Convention abroad is designed as a fifth template in `AFRP-Convention-Operations.md` §3.2 (P22, CV2), gated on Q-223 and Q-244 |

## H. Finance and fundraising

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| H1 | Finance Committee approves budgets | SP19, INTAKE26 | Partly built · Designed | Ledger built; the committee's own workspace is `AFRP-Committee-Workspace.md` (P1; slices CW1–CW3). **Research (2 Oct 2026):** a Budget Committee prepares the budget and the General Assembly approves it by practice; the Legal Advisor recorded in May 2026 that no written rule says who passes a budget (Q-234) |
| H2 | A web presence that helps fundraising | SP19 | Built | Funds path |
| H3 | An endowment campaign | SP26, INTAKE26 | Designed | `AFRP-Fund-Rules.md` §7 (P9): the campaign's pledges, tiers as segments, receipting entity Q-100; the endowment's entity and rule at the 4 November 2026 Boards (Q-35). **Research (2 Oct 2026):** the President asked in September 2026 that no new endowed fund be set up until one fundraising strategy exists (H7; Q-210) |
| H4 | "Charitable giving unacknowledged" | SP19 SWOT | Designed | Four contributor moments and an annual statement (D10) |
| H5 | A budget line per programme | SP19 | Designed | Typed budget line (`AFRP-Program-Architecture.md` §3); the line is released against the year's distribution by holding entity (P9 §4 step 7). The Cook Book fund beside the Scholarship Fund: `AFRP-Scholarship-Awards.md` §6.2 (P26; Q-173) |
| H6 | Grant-writing | MIN Sep 2023 | Outside | — |
| H7 | One fundraising strategy across the groups that solicit the same donors | INTAKE26 | Outside | The President's September 2026 message: several groups solicit the same donors with no shared strategy, and the endowment is meant to be the main driver; a meeting is promised. The funds ledger and the club attribution on every gift (D57) report across groups; the strategy is outside. New endowed funds wait on it (Q-210; Q-35). Who coordinates Convention and Mid-Year sponsorship, and the sponsor prospect's collision check, are `AFRP-Convention-Operations.md` §7 (P22; Q-245) |
| H8 | Each entity's money in its own accounts: retitled bank accounts, a card processor per entity, books fed from the CRM, an audit | INTAKE26, Form 990 | Designed | The design is the multi-entity ledger and the QuickBooks spec (D1–D3, D56). The sources show the books moving the same way in 2026: one processor account per entity, QuickBooks fed from the registration system, a liability for each affiliate purpose AFRP collects, and a CPA audit for ARFECF from the year to May 2026. Which of four roles is "the CPA" is Q-231; settling the affiliates' accounts Q-232; dues recognition Q-233. The Convention's books mapping is `AFRP-Convention-Operations.md` §10 (P22, CV7); the bookstore's per-entity orders and processor profiles, never netted, are `AFRP-Magazine-Operations.md` §8 (P24, MG7) |

## I. Government relations and advocacy

| # | Element | Source | Platform | How the platform fulfils it |
|---|---|---|---|---|
| I1 | Decide whether policy work fits the mission | SP19 | Built | Settled in practice: Congressional Outreach sits on the Leadership branch; the Government Affairs Committee is the paragraph under By-Law 8.15 (Q-50 carries the drafting item); public statements on legislation are AFRP's under D65, the affiliates' refused (P6 §6) |
| I2 | Elected-official relations; a stronger advocacy voice | TASKS, SWOT25, INTAKE26 | Designed | Positions, contacts with offices, the outreach register, alerts and members' own advocacy, the lobbying record — `AFRP-Advocacy.md` (P14; slices AD1–AD5); public statements on legislation are AFRP's under D65, the affiliates' refused (P6 §6). **Research (2 Oct 2026):** the sources show local action committees inside the clubs (Q-131), an automated meeting tracker outside the platform (Q-183), town halls with an action segment, a constituent-stories site (Q-184) and paid outreach coordinators; candidate-related activity is Q-132. Government Affairs in operation is `AFRP-Leadership-Pipeline.md` §5.4 (P25, YL5); the `advocacy` and `government-affairs` workflows are both Designed |
| I3 | Washington internships in congressional offices | INTAKE26, ECBL15 | **Gap** | The March 2025 Mid-Year assembly voted a Federation contribution with the funding source left open; ARFECF's by-laws name internships in Washington as an Endowment purpose, while D65 puts Government Affairs on AFRP's General Fund. No programme entry exists; which entity pays, and whether a stipend is advocacy, is Q-182. `AFRP-Leadership-Pipeline.md` §5.4 (P25) builds only the refusal by name until Q-182 is answered |

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
| J6 | The dues rule: who collects club dues, whether a member may opt out, and when they pass to the club | INTAKE26, MIN, INTAKE26 | Built · Outside | Club-collected AFRP dues are held as agent and remitted on the ledger (D1). No Federation document in seventeen years writes the rule down (Q-36); D57 keeps D1 and shows it on the club's statement. The CPA's confirmation of the agency treatment is outside (Q-3). **Research (2 Oct 2026):** no account on either side carries club-collected national dues, and AFRP's deferred-dues line is unused (Q-232, Q-233) |
| J7 | The convention host agreement as the shared rule between the Federation and a host club | MOU, INTAKE26 | Designed | Every Convention runs under a signed host agreement; its terms sit on the event and the platform produces the settlement statement; the same shape serves the Mid-Year (D59, settling Q-34). The bid and the agreement row are `AFRP-MidYear-Host-Bids.md` §4 (P8); the row's terms, schedules and settlement statement are `AFRP-Host-Agreements.md` (P13); the Convention year from award to close is `AFRP-Convention-Operations.md` (P22) |
| J8 | A club attribution on every gift | INTAKE26 | Designed · Proposed | Every gift, from anyone, may carry a club attribution (D57). Today nothing records which club raised or co-funded what (Q-25). Design note P10 |
| J9 | The officer year: the affiliation form by 1 August, the Council and Board seats that derive from it, the hand-over | BL24, INTAKE26 | Designed | The officers form is the By-Law 3.2 filing and the source of every seat derived from it; a dated hand-over carries the balance and the open items (`AFRP-Club-Experience-Plan.md` §4.1, §6.2). No affiliation form is on file for any year; who approves affiliation is Q-40. Under the Q-33 gate |
| J10 | The club's seat in each programme: the camp liaison, the RBPN ambassador, the travel coordinator, the magazine correspondent | INTAKE26 | Designed · Proposed | A programme seat scoped to one club, appointed on the officers form or by the committee, each appointment naming who made it (Club Experience Plan §3.4, §7). Only RBPN names such a seat with a term today; who appoints is Q-45. **Research (2 Oct 2026):** Government Affairs' local action committees are a further club seat in practice (Q-131). The magazine correspondent's seat and assisted submission: `AFRP-Magazine-Operations.md` §3.2 (P24) |
| J11 | Moving each club off Breeze, and the clubs on no system onto the platform | INTAKE26, ADD2 | Designed · Proposed | One club at a time with a named owner on each side; read-only access; identity resolution with a human on every doubtful pair; a parallel run on the platform's screens; a dated cutover (Club Experience Plan §8; workflow `club-migration`). The deep read of Breeze (1 Oct 2026) fixed the path's constraints: the key is the club's account owner's, the API is unsupported and rate-limited, attendance moves only through it, and the account is deleted on cancellation (Breeze Parity §1a). Which club goes first is David's (Breeze Parity §5 q4). **Research (2 Oct 2026):** the sources show Breeze onboarding presented as a Federation initiative, against each club's own decision (Q-230) |
| J12 | The Federation's view of its clubs: every club as counts, and the year-one baseline per club | INTAKE26, SP19, Form 990 | Partly built · Designed | The clubs page in the Federation lens: standing, membership, club life, the Federation's work in the club, the statement balance, the migration state, every cell under the floor (Club Experience Plan §10; D67). The first version of the roll-up is built (B1). **Research (2 Oct 2026):** public filings show the clubs as separate exempt organisations of several kinds; which count of clubs is the Federation's is Q-229; a club's membership rule wider than By-Law 4.1.1 is Q-226; a club's view of its members' details is Q-237 |

---

## The committee's Doc against the record, 2 October 2026

**Recorded 2 October 2026.** D44 makes the committee's Google Doc, "AFRP Strategic Plan
2026 Refresh (Draft)" (30 September 2026, not adopted), the strategy text of record until
the committee adopts a plan. The Doc reproduces this crosswalk as it stood on 30
September. The record has moved since, and the Doc has not. This section lists where the
Doc is now behind the record, and the changes David would paste into it. The Doc is not
edited from this repository. Whether the Doc is refreshed or the committee edits the site
instead is Q-235.

| # | The Doc says | The record now says |
|---|---|---|
| 1 | The family tree "beneath all four as the roots" (summary and framework) | D53 (30 September): the tree joins the Heritage branch, every member keeps a node on it, and the Convention stays the junction |
| 2 | Seventeen rows marked Proposed, wholly or in part: A3, A7, B5, B8, B9, B10, B12, C4, C6, D7, E6, E7, F3, F5, G1, G3, G4 | Each is now Designed, by notes P1 to P8, P12 and P13 written on 1 October (the research report counted fourteen; the row-by-row comparison gives seventeen) |
| 3 | Other statuses as of 30 September | A8 Gap → Partly built · Designed (D64, P17); B2, C1, H1 gained designs; D4 Built → Built · Designed (P19); F2 and F7 Queued → Built; F4 Built → Plan only · Designed (corrected downwards); I2 Outside → Designed (P14); H3 no longer blocked (P9; Q-35); B14 Gap → Outside (Q-14); E9 Proposed → Outside · Proposed |
| 4 | Sections A to I only | Section J (One Federation, J1–J12), rows F13–F17 (1 October) and rows D23, F18, G6, H7, H8 and I3 (2 October) are missing |
| 5 | Eight questions for the committee | Five have an answer on the record: Question 1 for the design record by D42, though adoption stays the committee's; Question 2 by D64; Question 4 by Q-14; Question 5 by D66; Question 8 in part by D55 (Women to Women is a sub-fund of ARFHSN), with Senior Living shown by the research to be the Ramallah Foundation's (Q-203) and Preservation's entity not stated. Three stay open: Question 3 (Q-13), Question 6 (Q-15), Question 7 (Q-17) |
| 6 | Branch table: Emerging Leaders, the High School Senior Award, Senior Living; "Ramallah Works … needs a home" | Ramallah Works is AFRPWorks on the Leadership branch (D64). Three entries were under question: Emerging Leaders (no programme by that name found; Q-178; *retired by D90, 4 Oct 2026*), the Senior Award (still offered publicly; Q-163, Q-164; *since 3 Oct 2026 it continues, D82; since 4 Oct the Scholarship Fund Committee runs it, D85*), Senior Living (Q-203) |
| 7 | Priority 3: "the five governing documents" nobody has on file | Three are found (the Endowment and Scholarship Fund Policy Statements and the 2015 ARFECF by-laws); two remain (ARFECF's exemption letter, the Board Rules & Regulations), and the ARFHSN trustee roster and the Houston General Assembly minutes are now also needed |
| 8 | No goals list; seven priorities | The site shows eight goals distilled for the committee to confirm (D52); they appear nowhere in the Doc. Whether the committee confirms goals, priorities or both is Q-235 |
| 9 | Next steps: design notes "follow for the elements marked Proposed" | P1 to P20 are written (1 October); P21 to P27 (the contact record, Convention operations, the Relief Fund and Senior Living, the Magazine's operations, the leadership pipeline, scholarship awards, the family tree in practice) are written (2 October), and P28 (the family tree module, from D68–D74) the same day |

### The change list to paste into the Doc

Role-level, figure-free. Each item names the place in the Doc and the text to put there.

1. **Summary, proposal 1.** Replace "with the family tree as the roots beneath all four and
   the Convention as the place they meet" with "with the family tree on the Heritage branch,
   every member keeping a node on it, and the Convention as the place the branches meet".
2. **Framework.** Replace "**The family tree** sits beneath all four as the roots." with
   "**The family tree** is on the Heritage branch, beside the Preservation Project, the
   Magazine and the Bookstore. Every member keeps a node on it." Add "the Family Tree" to
   the Heritage row of the branch table.
3. **Framework.** Replace "**Ramallah Works** is on no programme list yet and needs a home."
   with "**Ramallah Works** is AFRPWorks, the Ramallah Jobs Initiative, on the Leadership
   branch." Add "AFRPWorks" to the Leadership row of the branch table.
4. **Branch table, a note beneath it.** "Three entries are under question: Emerging Leaders,
   for which no programme by that name has been found; the High School Senior Award, which is
   still offered publicly; and Senior Living, which is the Ramallah Foundation's home and may
   not be a Federation programme." *(Since 4 Oct 2026: remove Emerging Leaders from the
   branch table, D90; the Senior Award continues, run by the Scholarship Fund Committee, D82
   and D85; Senior Living is the Foundation's project, D91, pending the two Boards. No entry stays under question.)*
5. **Priority 3.** Replace with: "Produce the governing documents the by-laws cite and nobody
   has on file: ARFECF's tax-exemption letter, the Board Rules & Regulations (the authority
   for the dues tiers), the ARFHSN trustee roster and the minutes of the July 2026 General
   Assembly. The Endowment and Scholarship Fund Policy Statements and the 2015 ARFECF
   by-laws were found in October 2026."
6. **A new section after the priorities, "Eight goals, for the committee to confirm".** The
   eight names as the site shows them — know and serve every member; connect the clubs and
   the Federation; bring in and keep the next generation; govern well, and be seen to; speak
   with one voice; fund the mission, and show the return; keep the heritage and the memory;
   run the Federation professionally — with one line: "Distilled from the Federation's
   documents. The committee's wording replaces them." Do not mark any goal confirmed.
7. **The crosswalk tables.** Replace sections A to I with the crosswalk as it stands on 2
   October, or at least change the statuses in rows 2 and 3 of the table above, and add
   section J and rows F13–F18, D23, G6, H7, H8 and I3.
8. **Questions for the committee.** Mark Questions 2, 4 and 5 answered (AFRPWorks on the
   Leadership branch; the roster follows By-Law 7.3.3; the shared drive is the archive of
   record). Mark Question 8 answered for Women to Women (a sub-fund of ARFHSN) and reframe it
   for the rest: "Which entity holds the Preservation Project, and is Senior Living a
   Federation programme at all?" Keep Questions 1, 3, 6 and 7 open. Add: "Does the committee
   confirm goals, priorities, or both, and in which text?"
9. **Next steps.** Replace "Platform design notes follow for the elements marked Proposed …"
   with "The platform's design notes for the elements once marked Proposed are written,
   including notes on the contact record, Convention operations, the Relief Fund and Senior
   Living, the Magazine's operations, the leadership pipeline, scholarship awards, the
   family tree in practice and the family tree module."
10. **A line under the title.** "Refreshed from the design record on [date]; the record's
    open questions carry Q-numbers on the site."

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
| **The four branches**, the tree on the Heritage branch and the Convention as junction | D38–D40, D42, D53 |
| **The five-rung engagement ladder** in every programme | D25 |
| **Three entities on one ledger** (AFRP, ARFECF, ARFHSN), agency treatment of club dues, restricted-fund rules | D1–D3, D7–D10, `AFRP-Multi-Entity-Ledger.md` |
| **Scholarship committee engine** with conflict checks over the tree and cross-border tax positions | Slice 4, `AFRP-Adviser-Brief.md` |
| **Club tools replacing Breeze** | `AFRP-Addendum-2-Breeze-Replacement.md`, B1–B6 |
| **Privacy as data**: per-field directory consent, nothing about the living without sign-in, household consent for minors | D17, D22, D28, D33, R6 |
| **Maintainability as the governing risk**: a plain stack chosen for "who maintains this in 2031" | AFRP-Hub ADR-001 |
| **A journey corpus** that tests the build against the stories it must support | `plan/MASTER-PLAN.md` §1b |

---

## Design notes

P1 to P20 are written as of 1 October 2026 (P10 inside P18); P21 to P27 as of 2 October 2026, from the second research round; P28 the same day, from D68–D74. Each slice row in
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
| P11 | Care grants and partner agreements | F13, F14, F15, F17, J1 | **Written** (`AFRP-Care-Grants-and-Partners.md`, 1 Oct 2026): six slices CG1–CG6; Q-104–Q-114; the Relief Fund's entity is not stated (Q-109; *since 3 Oct 2026 it is AFRP, D83*) |
| P12 | Selection programmes and the Arabic term | A8, F3, F4, F5 | **Written** (`AFRP-Selection-Programmes.md`, 1 Oct 2026): the four selection cycles and the Arabic term; slices SEL1–SEL5 and AR1–AR4; Q-70, Q-76, Q-92 and Q-115–Q-123; the reading of D61 at a future cycle's door is put to David (Q-118) |
| P13 | Host agreements for the Convention and the Mid-Year | G1, G3, J7 | **Written** (`AFRP-Host-Agreements.md`, 1 Oct 2026): the terms, schedules, settlement statement, disputes and archive of the row HB3 generates; slices HA1–HA6; Q-92 and Q-124–Q-130 |
| P14 | Advocacy and the Day of Action | I1, I2 | **Written** (`AFRP-Advocacy.md`, 1 Oct 2026): advocacy as objects; the Day of Action on P12's engine; the lobbying register for D65's condition; slices AD1–AD5; Q-70 and Q-131–Q-136 |
| P15 | Incident response and data retention | C4, D4 | **Written** (`AFRP-Incident-Response-and-Retention.md`, 1 Oct 2026): the incident object, the law register, the retention schedule with attested/proposed/silent rows, a DRAFT policy for the Board; slices IR1–IR5; Q-70, Q-76 and Q-137–Q-141 |
| P16 | The Executive Director as staff | C1 | **Written** (`AFRP-Executive-Director.md`, 1 Oct 2026): the seat, the grants module by module, the 7.9.3 named-purpose read, the Executive Assistant, the office map, the hire's record, succession, the maintainer question; slices ED1–ED4; Q-15, Q-44, Q-56, Q-65 and Q-142–Q-146 |
| P17 | AFRPWorks | A8 | **Written** (`AFRP-AFRPWorks.md`, 1 Oct 2026): the programme page; employer, posting, candidate (a D60 contact record), introduction (brokered), fee as a blank, owner as a body once named, pilot as a dated cycle with D67 counts; the Legal Advisor's four matters; slices AW1–AW4; Q-147–Q-157 |
| P18 | The club experience plan: the people of a club, the club workflows, the club–Federation statement, the migration from Breeze club by club | J1–J12, D7, G1, G3 | **Written** (`AFRP-Club-Experience-Plan.md`, 1 Oct 2026, fourteen sprints; reviewed and applied). Rests on D1, D57, D59, D61, D66 and the Breeze parity note; B3–B6 stay gated on Breeze Parity §5 |
| P19 | The directory in three formats: the members' directory with membership and club identified at Federation and club scale, the professional services directory, the leadership directory of seats and their votes | D4, B8, F11 | **Written** (`AFRP-Directory-Formats.md`, 1 Oct 2026): on-platform only, members only, votes as a property of the seat (David's direction); slices DIR1–DIR3; Q-48, Q-49 |
| P20 | The club journeys: what a club officer does in Breeze today, what the same person does on the platform, the rule, the refusal, the class, the slice — the corpus the clubs component is built from | J5, J9, J10, J11, J12, D7 | **Written** (`AFRP-Club-Journeys.md`, 1 Oct 2026): fifty-nine journeys in twelve groups, seventeen guarded by named gates (fifty-two of 1 Oct 2026, ten guarded; seven added 2 Oct 2026 — P20-A7, D6, D7, D8, I7, I8, J4 — seven of them guarded) |
| P21 | The contact record: one person record for every non-member the platform must hold | D23 (and D7, E6, I1, A8 by its roles) | **Written** (`AFRP-Contact-Record.md`, 2 Oct 2026): one person, dated roles; scope by seat; the two homes as an option; merge with the person's confirmation; consent bound to role and class; retention per role on P15; what a club sees; DRAFT register wording under Q-70 (not adopted); slices CR1–CR7; Q-238, Q-239 |
| P22 | Convention operations: the award, a fourth hosting model abroad, the unified registration, delegates, sponsors, the coordinator's access, the close, the books, the playbook | G2, G3, G5, G6, J7, F15, H7, H8 | **Written** (`AFRP-Convention-Operations.md`, 2 Oct 2026): builds between P8 and P13 without redesigning either; slices CV1–CV8; Q-240–Q-245 |
| P23 | The Relief Fund and Senior Living | F15, F16, F18 | **Written** (`AFRP-Relief-Fund-and-Senior-Living.md`, 2 Oct 2026): the fund row and three paths with authoriser rows; the organisation register and the representative's report of counts; the Federation's part in the Foundation's home, the capital campaign unoperated; slices RL1–RL6; Q-246–Q-248, and a merge into Q-204 |
| P24 | The Magazine and the Bookstore in operation | D18, D21, E7, J10 | **Written** (`AFRP-Magazine-Operations.md`, 2 Oct 2026): the issue cycle as run, announcements, the people, the subscriber ledger, the money, the archive, the two live stores and the Cook Book; slices MG1–MG7; Q-249, Q-250 |
| P25 | The leadership pipeline in practice | F1, F4, F11, B12, A8, I2, I3 | **Written** (`AFRP-Leadership-Pipeline.md`, 2 Oct 2026): one path from a high-school senior to a Board seat; the Young Leader Committee as the text reads; the Senior Award switch; the Day of Action's mode; Government Affairs in operation; slices YL1–YL6; Q-251–Q-254 |
| P26 | Scholarship awards and renewal | F9, F6, H5 | **Written** (`AFRP-Scholarship-Awards.md`, 2 Oct 2026): the award year, the semester filing and release, the hold, letters and cheques, named scholarships as P9 fund rows, the committee's seats; slices SA1–SA7; Q-255–Q-257 |
| P27 | The family tree in practice | D22, F8, C4 | **Written** (`AFRP-Family-Tree-In-Practice.md`, 2 Oct 2026): the migration in four stages — custody of the master file, the corrections queue as the one door, clan books under the record's rules, the handover — with oral-history consent as a written, scoped consent and the archive index; slices FT1–FT6; Q-258–Q-261. Amended the same day for D68–D74: the handover is D69's parallel run, FT4 folds into T2h and FT6 into T2d, Q-258 and Q-259 are answered (D69, D70) |
| P28 | The family tree module: the book's look on screen, members proposing and the committee deciding, the Hub as the record, and the tree reaching membership, the magazine, the directory and Heritage | D22 (and F8, C4 by its Heritage integration) | **Written** (`AFRP-Family-Tree-Module.md`, 2 Oct 2026): from D68–D74; the plate grammar (D68), the parallel run and cutover (D69), contribution by members in standing (D70), the living in full inside one's own branch (D71), approval in tiers with clan stewards (D72), find yourself at join and renewal (D73); slices T2-0, T2-R, T2a–T2h; Q-262–Q-270, with additions to Q-201 and Q-260 |

## Gaps the record cannot close alone

1. **Ramallah Works** (A8). **Done (D64):** identified as AFRPWorks and placed on the Leadership branch.
2. **The Presidential Advisory Council** (B6): proposed in FED2; adoption unknown.
3. **Strategic Plan Committee composition** (B14) against By-Law 7.3.3. **Done (Q-14):** confirmed by the project owner on 1 October 2026.
4. **Who maintains and pays for the platform** (D12).
5. **The archive of record** (C4). **Done (D66):** the shared drive is the archive of record.
6. **FED2 itself**: which revision was adopted at Jacksonville in 2021. It names
   living people, so it is cited here and not committed.
7. **Washington internships** (I3): voted in 2025 with no funding source and no programme entry (Q-182).
8. **The committee's Doc** against this record (Q-235): see the section below.
