# AFRP program experience — architecture
### The consolidation map, the engagement ladder, and the template every program is written against

**Date:** 20 August 2026 · design and planning only, build hold in force.
**Why this document exists:** David's observation, verified against the prototype — *"a lot of
functionality that is thin for any of the programs and a lot of redundancies in the platform."*
Both are true, both are measured below, and they are the same problem.

---

## Part 1 — The diagnosis, measured

The prototype has **97 routes across 5 lenses**: 35 federation, 30 member, 17 program, 9 club,
5 door. That sounds like a lot of platform. It is mostly the same platform, counted repeatedly.

### 1.1 Nineteen programs, five surfaces

Only five of the nineteen programs have a surface of their own — RBPN, the Magazine, the Medical
Mission, Senior Living, the Bookstore. The other fourteen exist **only as charter text in a
document**: Camp Ramallah, Leadership Ramallah, the Arabic Program, Project Hope, Women to Women,
the Scholarship, the Outstanding High School Senior Award, Emerging Leaders Summit, Day of Action,
Congressional Outreach, the Family Tree, the Preservation Project, the Educational & Cultural
Exchange Mission, and the Convention's own programming.

What the program lens actually contains is a **generic administrative pipeline** —
`applications`, `intake`, `registry`, `lifecycle`, `budget`, `disbursement`, `conflicts`,
`alumni`, `endowment`. Those are the seven stations, one set, shared by everyone.

**So a program today is a row in a registry with a workflow attached.** That is precisely why it
reads as thin: the administration is built and the *experience* was never built. Nobody's year in
Camp Ramallah is anywhere in this platform. Neither is anybody's job running it.

### 1.2 The redundancy, counted

The same object, given a new URL each time a different role looked at it:

| Object | Routes today | Where |
|---|---|---|
| Convention | **8** | `fed/convention` `fed/convops` `fed/convcmd` `fed/convdesk` `member/convention` `member/convlive` `member/convhelp` `member/convstore` |
| Elections & voting | **9** | `member/voting` `member/ballot` `+confirm` `+sealed` `fed/floor` `fed/results` `fed/mailedballot` `fed/credentialing` `fed/calendar` |
| Events | **8** | `fed/events` `club/events` `club/newevent` `program/newevent` `member/events` `member/event/harvest` `+lecture` `+party` |
| Money | **7** | `fed/ledger` `fed/finance` `fed/qbo` `fed/controls` `program/budget` `program/disbursement` `club/remit` |
| Identity & support | **4** | `fed/crm` `fed/member360` `fed/identity` `fed/supportdesk` |
| Institutions | **4** | `fed/institutions` `fed/inst` `fed/newinst` `fed/hsn` |
| Directory | **3** | `fed/directory` `member/directory` `member/dirinclusion` |
| Governance | **3** | `fed/board` `fed/committees` `fed/boardroom` |
| Clubs (federation view) | **3** | `fed/clubs` `fed/clubhealth` `fed/migration` |

And `member/home` is registered **twice** — a literal duplicate.

### 1.3 The single cause

The platform was built by enumerating **functions per role**. Every time a new role needed to see
an existing thing, a new screen was created rather than the existing one taught to adapt. Functions
multiplied; experiences never got built at all.

**The fix is one move, not two.** Collapse the object duplication, and the room that frees is
exactly where the program experiences go.

---

## Part 2 — The consolidation map: 97 → ~40

The organising principle changes from **lens × screen** to **object × role**. One canonical surface
per object, which changes what it shows and what it lets you do according to who is looking and
what grants they hold. A federation officer and a member land on the *same* convention route and
see different things — instead of two routes that drift apart.

| Merge group | From | To | Notes |
|---|---|---|---|
| **Convention** | 8 | **2** | `convention` (tabs: before · on-site · store · help; operator controls appear with the role) and `convention/live`. |
| **Elections** | 9 | **3** | `election` (calendar, credentialing, results — the operator arc), `ballot` (confirm and sealed become *states*, not routes), `floor` (live weighted vote). |
| **Events** | 8 | **2** | `events` (list and management, role-adaptive; the builder is a mode, not a route) and `events/:id` — the three worked examples become sample ids. |
| **Money** | 7 | **2** | `money` (multi-entity ledger with entity/fund/program filters; daily close, QuickBooks and controls as tabs) and `money/remit` for the club-side action. |
| **Identity & support** | 4 | **1** | `people` (member 360 · merge queue · support desk). `fed/crm` is an as-is comparison, not a product surface — it moves into documentation. |
| **Institutions** | 4 | **1** | `institutions` — registry, detail and the charter wizard are states of one surface. ARFHSN is a detail instance, not its own route. |
| **Directory** | 3 | **1** | `directory`, with your-household-inclusion as a panel on it. |
| **Governance** | 3 | **1** | `governance` — board · committees · workspace. |
| **Clubs (fed)** | 3 | **1** | `clubs` — registry, health and onboarding/migration. |
| **Household & family** | 6 | **3** | `household`, `family` (tree + life events, federation approval as a role view), and the turning-eighteen consent refresh becomes a **life-event state**, not a route. |
| **Comms** | 3 | **2** | `inbox` (receiving) and `comms` (composing, role-adaptive). |
| **Club lens** | 9 | **4** | `club/dashboard` `club/roster` (households folds in) `club/officers` `club/voting`. Events, remittance and comms move to the shared surfaces. |
| **Programs** | 17 | **2** | **The headline.** `programs` (the registry) and `program/:slug` — *one templated surface that renders any of the nineteen*. The admin stations become tabs inside it. |

**Net effect: ~97 routes → ~40 distinct surfaces — while going from 5 programs with a surface to
19.** Fewer things to build, more of AFRP actually represented. If you prefer to count each
program page separately it is ~58, but they are one thing built once.

### Progress — first three routes retired, 20 Aug 2026
| Was | Now | What actually moved |
|---|---|---|
| `fed/lifeevents` | the tree queue | It was the same submissions under a second vocabulary, with a nav badge reading **9** while the tree computed **6**. What was genuinely unique there was not intake but **release** — a death held for family approval, a marriage needing two, a relocation offering a club transfer. Those are now a **step on a queue item**: open any item to see its gate and what approving it sets off. |
| `member/lifeevent` | `member/family` | Its five kind pills were links to itself with no state. The one submission form now carries all six kinds. **Graduation and relocation touch no edge at all** — they are the honest exception to "everything is a tree change", and they sit in the same queue at blast radius zero rather than justifying a second one. |
| `program/conflicts` | inside `program/applications` | The review row already deep-linked to it. The kinship reading now expands where the decision is made, instead of being a module you navigate away to. |

**Then the seven object-merges, same day: 96 → 72.**

| Merged surface | From | What made them one object |
|---|---|---|
| `convention` | **8** | The same convention seen by an operator, a commander, a desk volunteer and an attendee. |
| `money` | **7** | One ledger. Entity, fund and programme are *filters*, not separate places. |
| `institutions` | 4 | Registry, one record, and the wizard are states of one surface; ARFHSN is an instance, not a route. |
| `people` | 3 | One person: who they are, whether we hold them twice, what they asked for. |
| `directory` | 3 | The directory and the consent governing it. |
| `governance` | 3 | The board, its committees, the room they work in. |
| `clubs` | 3 | The eighteen, their health, and the door a nineteenth comes through. |

**The merge carries content across verbatim rather than deleting it** — every original
panel becomes a tab, and a test asserts each source screen's distinctive text still renders.
That is the difference between consolidation and loss: the interface goes from thirty-one
routes to seven, and nothing a member or an officer could previously do went away.

**99 → 72 routes overall**, and no capability lost. The condolence circle still releases on *verification* rather than on review, because a queued death is a stalled condolence and the kindest behaviour in the platform must not be the slowest.

### What is deliberately *not* merged
- `door/join`, `door/login`, `door/recovery` stay separate. The front door is where existence-blindness
  lives; merging them creates exactly the cross-surface leaks S7 exists to prevent.
- `floor` stays its own route. A live weighted vote in progress must not share a surface with
  anything that can be navigated away to by accident.
- `workbench` (rulesets) stays separate. It edits the rules the other surfaces obey.

---

## Part 3 — The engagement ladder

Every program gets the **same five rungs**. This is what makes "depth of engagement" a thing the
platform can see, an organizer can act on, and a board can compare across programs without
flattening what makes each one different.

| Rung | Name | What it means |
|---|---|---|
| 1 | **Hear** | They know it exists. On a list, saw it in the Magazine, a cousin mentioned it. |
| 2 | **Show up** | One time. Came to the lecture, opened the mission newsletter, attended once. |
| 3 | **Take part** | Committed participation. Enrolled, a camper, an applicant, through a season. |
| 4 | **Give or serve** | Contributes back. Donated, volunteered, mentored, hosted, chaperoned. |
| 5 | **Lead** | Carries responsibility. Committee member, chair, organizer, trustee. |

### 3.1 Four things every rung must carry
A rung is only real if all four exist. Where one is missing, the program's write-up says so rather
than inventing it.

1. **The participant's experience** — what this rung actually feels like in *this* program. Rung 3
   of Camp Ramallah is a fortnight in a bunk; rung 3 of RBPN is showing up to quarterly calls.
2. **The organizer's view** — what they see, and what the next-rung invitation is.
3. **The evidence** — what the platform can *observe* that places someone on this rung. **No rung
   without evidence.** A rung inferred from nothing is fiction, and fiction in a member record is
   how people get wrongly solicited.
4. **The stall signal** — how long on a rung before it means something, and what the organizer does
   about it. Often the answer is *nothing*, and that must be stated.

### 3.2 The ladder connects to the Rails
**Rung 5 in one program is frequently rung 1 in the next.** A Camp Ramallah counsellor hears about
Leadership Ramallah because of what they just did. That handoff is the existing Rails mechanic, and
the ladder gives it a trigger point rather than leaving it as narrative. The ladder does not replace
`AFRP-Program-Architecture.md` — it is the rung-level detail underneath it.

### 3.3 Five rules the ladder must obey — built in, not bolted on
These are stated up front because the red team will attack exactly here, and because getting them
wrong turns a warm organisation into a sales funnel.

1. **A rung is not a score, and the member never sees a number.** The participant sees *"here is
   what's next, if you'd like it."* They never see "you are a 2." A member who comes to the hafli
   every year for twenty years and nothing else is **not** a failure of the platform.
2. **Declines stay invisible.** The existing design records a declined program invitation *nowhere
   a committee can see*. Rung movement must not become a back door to that — an organizer must not
   be able to infer a decline from a rung that failed to advance.
3. **Stall signals must survive a life event.** Someone dropping from rung 3 to rung 1 may have had
   a death in the family. Where a bereavement or life event is on record, the stall signal is
   **suppressed, not queued** — and the suppression is invisible to the organizer, or it leaks the
   life event.
4. **Small programs cannot publish rung counts (S7).** A program with four participants showing
   "one at rung 4" identifies that person. Rung distributions are subject to the same complementary
   suppression as every other published figure, composed across tabs and across time.
5. **Downward movement is normal and is never a flag.** People step back. The organizer view shows
   *where people are*, not *who fell*.

---

## Part 4 — The program template

Every one of the nineteen is written against this. Six get it at full depth; thirteen get the same
headings, shorter. Uniformity is the point: it makes the thin ones **visibly** thin instead of
invisibly thin, which is how they get fixed.

1. **What it is, in its own words** — sourced from afrp.org and the program's own material.
2. **Who it's for** — eligibility, ages, prerequisites, and who is quietly excluded today.
3. **The operating year** — the real calendar: recruitment window, season, deadlines, the event, the wrap.
4. **The five rungs** — the four things from §3.1, for each rung, participant and organizer paired.
5. **The organizer** — who actually runs it (committee, chair, club, staff, partner), what authority
   they hold, and what they must escalate.
6. **Money** — what it costs, who pays, which entity's books, which of the four money treatments.
7. **The handoffs** — which programs feed it, which it feeds, and at which rung the handoff fires.
8. **What's missing** — the honest gap list: rungs with no evidence, stations with no owner,
   decisions nobody has made.

---

## Part 5 — Sequence

1. This document, agreed. ← *you are here*
2. Read AFRP's real program material (blocked — see below) and afrp.org program by program.
3. Six flagship programs at full depth, paired participant/organizer.
4. Thirteen to the template.
5. Red-team all nineteen at the established bar — breakers per target, two adversarial skeptics per
   finding defaulting to refuted, then consistency and coverage sweeps.
6. Rebuild the prototype on the consolidated map, with `program/:slug` rendering all nineteen and
   the ladder live.
7. Redraft into six section documents, retiring the overlapping ones.

### Blocked
AFRP's own program material — the `AFRP Management` folder — is connected on a device named **rafa**,
while this session is bridged to **ramallah**. Until that folder is reachable, everything in steps 3
and 4 rests on afrp.org and the existing charters, which is a materially weaker source for the
operating year, the real rung evidence, and who actually runs each program.

---

*Design and planning only. Demo people and money are fictional; programs, the 18 chapter clubs,
committees and by-law citations are real and sourced.*
