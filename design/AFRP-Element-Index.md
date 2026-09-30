# AFRP platform — element index
### Every element discussed, and where it now lives

**Date:** August 2026
**Purpose:** one map from everything raised across this project to the screen that covers it.

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
| Member 360 — every linked source record | Ops 02 |
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
| Lineage, search, living individuals restricted | Member 14 |
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
| Bookstore, member pricing, digital library | Member 20, Ops 20 |

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
2. **Agency or revenue** for club dues — one signature from the CPA.
3. **How many scholarship recipients**, across how many years, in what form.
4. **Publication calendar** — everything in the magazine keys off the press date.
5. **Who administers Dynamics today**, and what the licensing actually is.
6. **Which club goes first** on migration — it should be one that wants to.

---

*All figures in the mockups are either real output from the working engines or
clearly fictional demo data; each document says which is which. Sales tax has
been removed throughout, as requested.*
