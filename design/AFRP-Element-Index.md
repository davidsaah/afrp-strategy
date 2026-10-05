# AFRP platform — element index
### Every element discussed, and where it now lives

**Date:** August 2026
**Purpose:** one map from everything raised across this project to the screen that covers it.
**Since 4 October 2026:** the shapes these elements share are built once as the platform primitives of P29 (`AFRP-Platform-Primitives.md`, D99), listed after the P21–P28 table.

**Since 2 October 2026:** the elements raised by the research round and designed in the notes P21–P28 are listed at the end, with the Hub modules each note is written for ("Design notes P21–P28, and their modules"). The mockup screens below predate them, and the prototype evidences a story, never a rule (D41).

---

## The two unified mockups

| File | Audience | Screens |
|---|---|---|
| **AFRP-Unified-Member.html** | Members, on a phone | 20 |
| **AFRP-Unified-Operations.html** | Staff and officers, on a laptop | 20 |

Both inline the same design system byte-for-byte, so they are provably one
product. Both open with a contents list.

**The member document follows one person** — Nadia Khoury of the Detroit Club,
on one continuous day, 4 November 2026 — so the rules are shown *interacting*
rather than described one at a time. She is a national Patron in good standing
and a lapsed Detroit Club member, which is why she can vote federally but not
locally, and why she pays the non-member rate at her own club's dinner.

**The operations document is grouped by lens** — federation, finance, club,
program, magazine — because that grouping *is* the argument: one object model
seen from four angles, not four applications.

---

## Element → screen

### Membership

| Element | Where |
|---|---|
| Dual membership, national and club with independent lapse | Member 02, Ops 12 |
| Household, and who may act for whom | Member 03 |
| The 18th-birthday consent refresh | Member 03 |
| Stored cards, subscriptions, expiring card | Member 04 |
| Per-channel consent, per-field privacy | Member 05 |
| Member 360 — every linked source record | Ops 02 *(since 2 Oct 2026: also a non-member's contact roles, P21 §10)* |
| Identity resolution and the merge queue | Ops 03 |
| Free student membership for scholarship recipients | Member 16, Ops 15 |
| Complimentary Family tier for newlyweds | Member 15–16 |

### Money

| Element | Where |
|---|---|
| Giving history, designations, tax receipt | Member 06 |
| Donate — cause, amount, recurring | Member 07 |
| Daily close, balanced, posted to QuickBooks | Ops 07 |
| Journal batch detail, fees booked gross | Ops 08 |
| Club remittance, dues as a liability | Ops 09 |
| Club ledger modes and connection health | Ops 10 |

### Events and convention

| Element | Where |
|---|---|
| One calendar, federation and club | Member 08, Ops 13 |
| Register self and household | Member 08 |
| QR check-in | Member 09, Ops 13 |
| Convention registration and delegate status | Member 10, Ops 04 |
| Rooms, resources, name tags, child security codes | Ops 13 |

### Governance and voting

| Element | Where |
|---|---|
| Delegate apportionment, with the arithmetic shown | Ops 04 |
| Credentialing and quorum | Ops 04 |
| Ballots a member may and may not vote in | Member 11 |
| Casting a secret ballot | Member 12 |
| The one-time receipt that cannot be reissued | Member 13 |
| Results, abstentions excluded, certification | Ops 05 |
| Roles, scopes and permission refusals | Ops 06 |

### Family tree and life events

| Element | Where |
|---|---|
| Lineage, search, living individuals restricted | Member 14 *(since 2 Oct 2026: the living in full only inside one's own branch, D71; the book's plate grammar, D68; P28)* |
| Provisional records marked unverified | Member 14, Member 16 |
| Weddings, births, graduations, deaths | Member 15 |
| Consent gates before anything is published | Member 15–16 |
| Genealogy used to detect committee conflicts | Ops 16 |
| Genealogy used to trace lost alumni | Ops 18 |

### Directories

| Element | Where |
|---|---|
| Member directory, members-only, per-field opt-in | Member 17 |
| RBPN professional directory, brokered introductions | Member 17 |
| Professional listings sold by subscription | Ops 19 |

### Clubs

| Element | Where |
|---|---|
| Club dashboard and health | Ops 11 |
| Roster with dual membership status | Ops 12 |
| Club events and check-in | Ops 13 |
| Communications, consent-filtered before send | Ops 14 |
| Breeze migration state | Ops 11 |
| Member's own club view | Member 18 |

### Scholarships

| Element | Where |
|---|---|
| Applications, rubric, median ranking | Ops 15 |
| Conflict of interest via the family tree | Ops 16 |
| Budget, encumbrance, forward commitments | Ops 17 |
| Endowment capacity, underfunded named awards | Ops 17 |
| Named-award matching, most constrained first | Ops 17 |
| Historic alumni import and match queue | Ops 18 |
| Family-tree tracing for lost alumni | Ops 18 |

### Magazine and bookstore

| Element | Where |
|---|---|
| Issue plan and copy freeze | Ops 19 |
| Active Manar and Patron members | Ops 19 |
| Weddings, births, graduations, deaths | Ops 19 |
| Professional directory section | Ops 19 |
| Family tree highlight | Ops 19 |
| Upcoming activities | Ops 19 |
| Proof-and-confirm your own entry | Member 19, Ops 19 |
| Read the issue, search the archive | Member 19 |
| Bookstore, member pricing, digital library | Member 20, Ops 20 *(since 2 Oct 2026: neither live store has a member price or digital goods, Q-199; which store is kept, Q-197; P24 §8)* |

---

## Design notes P21–P28, and their modules (2 October 2026)

| Note | Element | Hub modules it is written for | Slices | Its open questions |
|---|---|---|---|---|
| **P21** `AFRP-Contact-Record.md` | The contact record: one person record for every non-member, with dated roles, scope by seat, consent per role and class, retention per role, and merging with the person's confirmation | `people` (Member 360, identity and merge), `member`, `comms`, `programs`, `events`, `clubs`, `magazine`, `payments`; the institution registry; the retention schedule (IR2) | CR1–CR7 | Q-70 (the DRAFT decision is §11), Q-238, Q-239 |
| **P22** `AFRP-Convention-Operations.md` | The Convention element: the award and forfeiture, a hosting model abroad, the unified registration and the desk, delegates, sponsors and the ad book, the coordinator's access, the close, the books, the playbook | `events`, `payments`, `ledger`, `funds`, `voting`, `clubs`, `governance`; CG2; CW1; the QuickBooks mapping | CV1–CV8 | Q-240–Q-245 |
| **P23** `AFRP-Relief-Fund-and-Senior-Living.md` | The Relief Fund's three paths, the organisation register and the representative's report; the Federation's part in the Foundation's senior home | `funds`, `ledger`, `grants`, the institution registry, `payments`, `comms`, the Care programme pages | RL1–RL6 | Q-246–Q-248; Q-109, Q-203, Q-204 |
| **P24** `AFRP-Magazine-Operations.md` | The Magazine as it runs: announcements, the people, the subscriber ledger, the money, the archive; the two live stores and the Cook Book | `magazine`, `store`, `funds`, `ledger`, `comms`, `memberdir`, the institution registry | MG1–MG7 | Q-249, Q-250; Q-192–Q-199 |
| **P25** `AFRP-Leadership-Pipeline.md` | The leadership path from a high-school senior to a Board seat; the Young Leader Committee as the text reads; the Senior Award switch; the Day of Action's two modes; Government Affairs in operation | `programs`, `committees`, `member`, `events`, `alumni`, `voting`, `network`, `reporting` | YL1–YL6 | Q-251–Q-254; Q-163, Q-178, Q-179 |
| **P26** `AFRP-Scholarship-Awards.md` | Scholarship awards and renewal: instalments, the semester filing and release, the hold, letters and cheques, named scholarships as fund rows, the committee's seats | `scholarship`, `funds`, `ledger`, `comms`, `committees`, `alumni` | SA1–SA7 | Q-255–Q-257; Q-158, Q-159 |
| **P27** `AFRP-Family-Tree-In-Practice.md` | The family tree's migration from practice: custody of the master file, the corrections queue as the one door, the clan books, oral-history consent, the archive index (amended by D68–D74) | `tree`, `member`, `committees`, `comms`, `heritage`, `access` | FT1–FT6 (FT4 and FT6 folded into T2h and T2d) | Q-258–Q-261; Q-189, Q-200–Q-202 |
| **P28** `AFRP-Family-Tree-Module.md` | The family tree module: the book's look on screen, members proposing and the committee deciding in tiers, the Hub as the record after a parallel run, and the tree reaching membership, the magazine, the directory and Heritage (D68–D74) | `tree`, `member`, `join`, `dues`, `access`, `rules`, `magazine`, `memberdir`, `comms`, `reporting` | T2-0, T2-R, T2a–T2h | Q-262–Q-270 |

The slice rows are in `plan/MASTER-PLAN.md` §2. The note-by-note crosswalk rows are in `AFRP-Strategic-Plan-Crosswalk.md` (design-notes table).

## Design note P29, and its modules (4 October 2026)

P29 raises no element of its own. It names the shapes the elements above share and builds each once (D99).

| Note | Element | Hub modules it is written for | Slices | Its open questions |
|---|---|---|---|---|
| **P29** `AFRP-Platform-Primitives.md` | The platform primitives: the refusal (§1), the act and append-only record (§2), the scoped parameter and authority row (§3), the dated role with bodies and seats (§4), consent and its key register (§5), the cycle (§6), the statement run (§7), sending and the letter row (§8), the record on file (§9), the work item (§10), the clock (§11), the snapshot (§12) | `core`, `rules`, `access`, `clubs`, `programs`, `scholarship`, `camp`, `comms`, `ledger`, `funds` | A2 (§1, §12); PR0 (§2, §3, §4's base, §9, §11); then CW1, C2, LT1 with CM1, CR1 with AR2, CY1 and CY2, C3 as each primitive's first user | None of its own; an unset value refuses naming its parameter and question (§1, §3) |

---

## Ideas worth keeping hold of

Five things that came out of this work and are easy to lose in the volume.

**1. The magazine is a forcing function.** Nobody updates a membership database
for its own sake; everybody wants their daughter's wedding in the magazine. So
every printed section is generated from live data, and there is no manual entry
path into an auto section. The deadline does the work that no data-quality
campaign could. *It costs nothing extra to build and it improves everything
downstream.*

**2. The family tree is operational, not ceremonial.** It detects committee
conflicts of interest that self-declaration misses, and it reaches alumni whose
addresses died twenty years ago. No commercial CRM can do either. It is the
most distinctive asset in the platform.

**3. Freeze the snapshot.** Ballot electorates at the record date, magazine
sections at the copy freeze, journal batches at the daily close. The same
pattern three times, for the same reason: without it, results cannot be
reproduced and "why wasn't I in it?" has no answer.

**4. Refusals must name their rule.** An ineligible ballot, a blocked payment, a
refused permission, a held death announcement — each says which rule fired and
what would change it. Silent failure is how people lose trust in a system they
cannot argue with.

**5. Age sets defaults, never rules.** Households, voting, scholarships. The
current portal ejects members from their family at eighteen; this one asks them
what they want.

---

## Still open

The questions that gate work rather than merely inform it:

1. **The bylaws** — apportionment, quorum, proxy voting, tie-breaking.
2. **Agency or revenue** for club dues — one signature from the CPA. *(Since 2 Oct 2026: Q-3; which CPA is Q-231.)*
3. **How many scholarship recipients**, across how many years, in what form.
4. **Publication calendar** — everything in the magazine keys off the press date.
5. **Who administers Dynamics today**, and what the licensing actually is. *(Since 2 Oct 2026: the Hub replaces it; in practice the CRM feeds QuickBooks Online, `AFRP-QuickBooks-Integration-Spec.md` §12.)*
6. **Which club goes first** on migration — it should be one that wants to.

---

*All figures in the mockups are either real output from the working engines or
clearly fictional demo data; each document says which is which. Sales tax has
been removed throughout, as requested.*
