# AFRP program experience — architecture
### The consolidation map, the engagement ladder, and the template every program is written against

**Date:** 20 August 2026 · design and planning only, build hold in force.
**Why this document exists:** David's observation, verified against the prototype — *"a lot of
functionality that is thin for any of the programs and a lot of redundancies in the platform."*
Both are true, both are measured below, and they are the same problem.

**Since 2 October 2026:** this map is kept as written. Where a lens, object or programme it describes has moved since, a dated pointer stands at that place. There are four additions. **The contact record** is a cross-cutting object (P21; Q-70). **The scholar** is a member-lens experience (P26). **The family surface** follows D68–D74 (P28). **The programme list** has been corrected by the research round: Emerging Leaders has no source (Q-178), the Senior Award's status is in question (Q-163; *since 3 Oct 2026 it continues, D82*), and Senior Living is the Foundation's (Q-203). The experiences themselves are now written in `site/data/experiences.yaml` (sixteen lenses).

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

*Since 2 October 2026:* four of these names have moved.
- "Emerging Leaders Summit" names no programme in any source. The 2021 mention is most plausibly the Youth Summit, reported since 2023 as the Day of Action (Q-178; P25 §2.2).
- The Outstanding High School Senior Award's status is in question (Q-163). *Since 3 Oct 2026:* it continues (D82); its body is Q-164.
- Senior Living is the Ramallah Foundation's project, and the Federation's part is communications, gifts passed through and a budget grant (P23 §8–§9; Q-203).
- The Bookstore's two live stores and the Hub's store are set side by side in P24 §8, and which is kept is Q-197.

The Convention's own programming is designed as an element in P22.

What the program lens actually contains is a **generic administrative pipeline** —
`applications`, `intake`, `registry`, `lifecycle`, `budget`, `disbursement`, `conflicts`,
`alumni`, `endowment`. Those are the seven stations, one set, shared by everyone.

**So a program today is a row in a registry with a workflow attached.** That is precisely why it
reads as thin: the administration is built and the *experience* was never built. Nobody's year in
Camp Ramallah is anywhere in this platform. Neither is anybody's job running it.

*Since 2 October 2026:* the experiences are written per lens in `site/data/experiences.yaml`, sixteen of them. The research round added the **scholar**, a member-lens experience for a new or continuing Scholarship recipient on the US or Ramallah track. The scholar files after each semester to have the next instalment released, receives a missing-documents letter that says what is missing and by when, and is never named in public (counts and amounts by track only). The scholar's workflows are `scholarship-cycle` and `scholarship-renewal`. It rests on P26 §2 (the instalment, the semester filing, the release and the hold), with Q-158, Q-159 and Q-255 open.

### 1.2 The redundancy, counted

The same object, given a new URL each time a different role looked at it:

| Object | Routes today | Where |
|---|---|---|
| Convention | **8** | `fed/convention` `fed/convops` `fed/convcmd` `fed/convdesk` `member/convention` `member/convlive` `member/convhelp` `member/convstore` |
| Elections & voting | **9** | `member/voting` `member/ballot` `+confirm` `+sealed` `fed/floor` `fed/results` `fed/mailedballot` `fed/credentialing` `fed/calendar` |
| Events | **8** | `fed/events` `club/events` `club/newevent` `program/newevent` `member/events` `member/event/harvest` `+lecture` `+party` |
| Money | **7** | `fed/ledger` `fed/finance` `fed/qbo` `fed/controls` `program/budget` `program/disbursement` `club/remit` |
| Identity & support | **4** | `fed/crm` `fed/member360` `fed/identity` `fed/supportdesk` *(since 2 Oct 2026, the same object also holds non-members: the contact record, P21)* |
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

*Since 2 October 2026, pointers on the surfaces above:*

- **`people` holds the contact record (P21), a cross-cutting object.** A non-member is held as one person record with no membership on it, carrying dated roles: learner, applicant, referred, club prospect, giver, guest, subscriber, media or office contact, candidate, alumnus. Each role has its owning scope, consent rows per channel and message class, and a retention row. Member 360 shows the roles; the merge queue links a contact to a member only with the person's confirmation (P21 §3, §7, §10; slices CR1–CR7). Only the learner role is decided (D60) and the alumnus record is D61. Every other role is a reading of D60 under **Q-70**, whose DRAFT decision is P21 §11 and is not adopted. Every surface that meets a non-member reads this object: `programs` (the Arabic door, applications, AFRPWorks), `events` (guests, Q-238), the Magazine (subscribers, Q-239), `clubs` (prospects), `money` (a one-time giver) and `institutions` (media and office contacts, whose home is an option under Q-70).
- **`family`** follows D68–D74 and P28. It draws the book's plate grammar (D68); the hourglass stays as a second view (D77), drawn in the same grammar (D80). The Hub becomes the record after a parallel run (D69, superseding D11's staging). Members in standing propose (D70). A signed-in member sees the living in full only inside their own branch: blood relatives sharing an ancestor no further back than a great-great-grandparent, and their spouses (D71). The committee decides with one key, or two different keys for a structural change, and clan stewards never approve (D72); the structural kinds are the rules-register row D81 set. Membership and join is the first integration (D73), with find-yourself at join and renewal (P28 §4.4). The federation approval in the household row is now D72's committee keys.
- **`convention`** gains the desk, the unified registration, delegates from the roll and the close as dated acts (P22 §5, §6, §9).
- **`money`** meets a Federation that already runs one card-processing account per entity and keeps QuickBooks integrated with its current CRM. That is practice, recorded in `AFRP-Multi-Entity-Ledger.md` §9 and `AFRP-QuickBooks-Integration-Spec.md` §12; D1 and D56 stand.

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

*Since 1–2 October 2026:* D39 makes programmes "windows, not gates", so nothing moves anyone between rungs or programmes. P25 §3 draws the Leadership path as what the platform already records about one person, read in order. It is a "my path" page only the member sees, with unvisited programmes shown as links and never as a next step owed. The branch outcomes are counts under the floor (S7). The "trigger point" above is therefore an invitation the member may look at, never a step the platform takes.

### 3.3 Five rules the ladder must obey — built in, not bolted on
These are stated up front because the red team will attack exactly here, and because getting them
wrong turns a warm organisation into a sales funnel.

1. **A rung is not a score, and the member never sees a number.** The participant sees *"here is
   what's next, if you'd like it."* *(Since 2 Oct 2026: P25 rule and slice YL1 go further: no "next" or "required" string on any branch surface; D39.)* They never see "you are a 2." A member who comes to the hafli
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

*Since 13 September – 2 October 2026:* the template is the programme register's eight headings (MASTER-PLAN slice P1; `site/data/programmes.yaml`, twenty-one entries), updated field by field from the research round with "In practice (research, 2 Oct 2026)" lines and their questions.

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
*Since 1–2 October 2026:* unblocked in part. The intakes of 1 October and the research round of 2 October read the Federation's own files, mail and public pages at role level. The private reports are in the planning Project, and their public text is in the register and the notes P21–P28.

AFRP's own program material — the `AFRP Management` folder — is connected on a device named **rafa**,
while this session is bridged to **ramallah**. Until that folder is reachable, everything in steps 3
and 4 rests on afrp.org and the existing charters, which is a materially weaker source for the
operating year, the real rung evidence, and who actually runs each program.

---

*Design and planning only. Demo people and money are fictional; programs, the 18 chapter clubs,
committees and by-law citations are real and sourced.*
