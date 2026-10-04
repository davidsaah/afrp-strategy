# The family tree as the platform's spine — integration design

**2 October 2026:** D68–D74 (Decisions Register, Part 5) change the decisions this document extends: D69 supersedes D11's staging, D71 amends D17, D72 amends D14's mitigations, D70 confirms D13, D68 supersedes D27 and D73 makes membership and join the first integration. The design built on them is `AFRP-Family-Tree-Module.md` (P28); the text below is left as written.

**Drafted 8 September 2026.** The tree stops being one programme among nineteen
and becomes the substrate the rest of the platform resolves people through.
This document states what that means, what it must never mean, and which
existing decisions it extends rather than replaces.

**Status: proposed.** Four questions were settled by David Saah on 8 September
2026 and are recorded below as **D30–D40**; they belong in
`AFRP-Decisions-Register.md` under those numbers. Everything else here is
design derived from them and from the decisions already ratified in D11–D22.
Nothing in this document overrides a ratified decision, and where it appears to,
the ratified decision wins and this document is wrong.

---

## 1. What was already decided, and is not reopened

The tree's spine was settled on 20–21 August 2026. This work **extends** it:

| | Decision | Consequence here |
|---|---|---|
| **D11** | Body of record is **staged** — a governed mirror now, the platform after one clean annual cycle | The GEDCOM is the master **today**; the platform is not yet the record. Integration must survive the handover without a rebuild. *Since 2 Oct 2026: D69 supersedes D11's staging. The Hub becomes the record after a parallel run of 30 to 60 days in which the Hub wins; the external file is then read-only, with a nightly export (P28 §4.3).* |
| **D12** | A correction touching a decided line **re-evaluates and flags** | Life events feeding the tree inherit this: a corrected birth re-opens what leaned on it. |
| **D13** | **Any member may propose anything** | The life-event surfaces are proposal surfaces, not write surfaces. *Since 2 Oct 2026: D70 confirms D13 for members in current national standing; no account exists for non-members.* |
| **D14** | **Every life event queues** for the committee | Confirmed and unchanged by D31 below. *Since 2 Oct 2026: D72 amends D14's mitigations. One committee key applies an own-household life event or a non-structural correction, and two different keys apply a structural change. Clan stewards recommend and never approve.* |
| **D15** | Public build: deceased real, living synthetic | Unchanged. The real file never enters the repository. |
| **D16** | The tree is **evidence for a human decision, never a verdict** | The load-bearing constraint on D30. |
| **D17** | All members see everything in-platform | The exposure ceiling for statistics, mailings and stories. *Since 2 Oct 2026: D71 amends D17. A signed-in member sees the living in full only inside their own branch (blood relatives sharing an ancestor no further back than a great-great-grandparent, and their spouses); outside it, a name and a position only. D28 is unchanged.* |
| **D22** | Photos: **per-item consent held by the subject**; a minor's runs through the household and is **re-asked at eighteen** | The pattern D33 extends to announcements. |

---

## 2. The decisions this document adds

### D30 · Every member has a node; a node is never a lineage claim

Every member is represented on the tree by a **node**. The node may be
unattached, or joined only by marriage, and that is a complete and unremarkable
state — not a deficiency, not a lesser membership, and never displayed as one.

**No membership decision reads the node.** Not eligibility, not standing, not
dues, not the franchise. The node exists so the platform has one way to name a
person across modules; it is not evidence and carries no claim.

This keeps D16 intact. **By-Law 4.2.1's Associate route exists precisely for
people the genealogy cannot reach** — 5,819 people in the file have no recorded
parents and 3,870 carry no clan — and a rule that made membership depend on a
line would deny exactly the people that route protects. The platform must not
be able to express "member without a node" as an error state, because it is not
one.

A **lineage claim** is a separate, optional, member-initiated object: a proposed
path with its per-link confidence, assembled for the Membership Committee under
D16. Having a node does not create one. Not having a claim is not a finding.

### D31 · Life events queue; the queue is where integrity lives

Confirms **D14** against the pressure to auto-write. A declared birth, baptism,
graduation, marriage or death **queues to the Family Tree Committee** and reaches
the tree when the committee accepts it. Nothing a member declares writes the
genealogy directly.

The cost is real and is accepted: the committee sits in the path of every life
event, and D13 already loads that queue. The mitigations are the ones D14's own
note names — the queue triages itself, own-household events clear first,
structural changes wait for a quorum, and an unsourced structural claim sorts to
the **top** for dismissal rather than the bottom for review.

**Who may declare** is now answered and needs no new rule: **R6 (register)**.
A parent declaring their own newborn holds the `consent` power by path P1; an
event delegate holds nothing here. `authority.services.may` is the gate.

### D32 · The new edition of the book carries no eligibility force

By-Law 4.1.1 admits a Regular Member of origin from ancestral Ramallah *"as
defined within Aziz Shaheen's book entitled 'Ramallah'"*. **4.1.1 continues to
point at Shaheen 1982** — the fixed 1982 volume, as published.

The platform may organise, section, index and typeset a **new edition**. That
edition is a publication. It is **not** the by-law's test and must never be
presented as one.

The reason is circularity: the platform's data would write the book, the book
would be the by-law, and the by-law would decide membership from the platform's
own data — the machine citing itself, which is the fault the rules register was
built to catch. Repointing 4.1.1 at a new edition is a **by-law amendment under
16.1.1, a delegate vote**, and until such a vote the book tooling ships with no
eligibility force and says so on its own surface.

### D33 · An announcement follows the photograph

Births, baptisms and any other announcement about a minor run on **D22's
pattern, extended from images to announcements**:

- the **household consents** at the time, through R6's `consent` power;
- the announcement is **withdrawable** while the subject is a minor;
- the choice is **re-asked of the subject directly at eighteen** — a decision
  her parents made at six does not silently become hers at thirty.

**A published magazine issue cannot be unprinted**, and the platform must say so
before consent is taken rather than after: withdrawal removes the announcement
from every surface the platform controls — the archive, the tree, search — and
cannot recall a printed page. That sentence belongs on the consent screen.

Baptism is **religious data**. It is recorded because the community records it,
held under the same consent as any other life event, and it is never a field any
eligibility, programme or directory surface reads.

---

## 3. The integration map

The tree touches eight modules. In every one it is the **resolver of who a
person is**, never the decider of what they may have.

**Membership.** The join wizard creates a node (D30). The member's record shows
the node and, if one exists, the lineage claim's status — with the 4.2.1 route
offered on the same screen, so the absence of a line is visibly a path and not a
dead end. This is the fix for `JD-009` and `JD-010`, the two rated-0 door rows.

**Life events.** One declaration surface, five kinds, one pipeline: declare →
R6 authority check → queue (D31) → committee decision → tree write →
downstream fan-out. The fan-out is the integration:

| Event | Downstream, on acceptance |
|---|---|
| Birth | node created · magazine announcement offered under D33 · household updated |
| Baptism | recorded on the node under D33; no downstream surface reads it |
| Graduation | node updated · the graduation dues incentive becomes offerable |
| Marriage | both spouses' nodes joined · a new household · the newlywed incentive becomes offerable |
| Death | `LivingGuardedModel` terminates the record · magazine holds it until the family approves (`JP-026`) · the deceased become publishable heritage under D15 |

**Two things the fan-out must not do.** It must not grant a membership or a dues
benefit by itself: **dues authority is the Board's** under By-Law 5.1, the
existing free-year incentive (`JD-004`) cites no Board decision, and an
incentive fired automatically by a life event is the platform legislating money.
The pipeline **offers**; a person accepts; the authority for the offer is named
on the screen or the offer is not made. And it must not resolve a spouse's own
eligibility: 4.1.1's "married to one having such origin" carries three open
questions in the register — a same-sex spouse, an unmarried partner, and a
member who divorces the spouse they were admitted through. Marriage creates
nodes and a household. It does not answer those.

**Magazine.** `JM-078` already has the archive as genealogy source material —
that is the tree reading the magazine. This adds the other direction: the
magazine reads the tree for announcements, under D33 and `JP-026`.

**Preservation project.** The tree supplies the people; the project supplies
place, photographs and story. A preserved item attaches to nodes rather than to
typed names, so the same person is not three records.

**The book.** Sections organised from the tree, clan by clan, with the platform
producing the manuscript and carrying **no eligibility force** (D32).

**Statistics.** Clan composition by chapter club, generational spread,
geographic drift — derived and read-only. The exposure ceiling is D17 and R7
together *(since 2 Oct 2026: D71 in place of D17's "everything")*: **aggregates only where a cell would name a minor**, and the
k-anonymity floor already used for camp rows (`JP-066`, k≥3 including the reason
the row is suppressed) applies unchanged.

**Reunions.** A reunion is an event whose invitation list is a subtree. It reads
the tree, respects consent, and never exports it.

**Gap-filling.** A paid member receives their own branch and is asked to fill
what is missing. It is a **mailing**, so it runs the comms consent filter and
records the withheld by name, exactly as `clubs.ClubMailing` does. It shows the
member their own branch — never a file, never a download, never another
family's.

---

## 4. Custody of the GEDCOM

Unchanged and restated because integration multiplies the temptation:

- The real file **never enters any repository** (D15, and the Hub's binding
  rule 1).
- **Import and export sit under `tree:moderate`** — the Family Tree Committee
  alone (`JF-070`). No member-facing surface produces a GEDCOM, and no
  integration described above is a reason to add one.
- Under **D11** the file is still the master and the platform is a governed
  mirror. Every integration here must work identically after the handover, and
  the surfaces say which side of it they are on. *Since 2 Oct 2026: superseded by D69. During the parallel run the Hub wins, and the record keeper's edits arrive as imports through the diff preview, applied as audited committee edits with conflicts held. After the run the external file is read-only and the Hub exports nightly under `tree:moderate`. Who owns the data, and on what terms, is Q-201.*

---

## 5. What this does not do

It does not make the tree decide anything. It does not create a membership, a
dues benefit, or an eligibility finding. It does not answer 4.1.1's three open
spouse questions, or the club attachment of a minor in two households (R6 §6,
ratified as staying open). It does not repoint By-Law 4.1.1. It does not widen
who may hold the GEDCOM. And it does not change D17 — the widest exposure in the
platform, still flagged as the one setting worth revisiting before launch. *Since 2 Oct 2026: D71 has revisited it (own branch only).*

---


### D34 · A step-parent holds nothing until someone grants it

Marrying into a household confers **no authority over the children already in
it**. R6's P1 requires the household's **parent relation**, and a spouse joining
the household is not placed in it by the marriage.

A step-parent acquires authority the same way anyone else does: a standing
holder names them to the release list for an event, or a guardianship is
recorded under P2. Nothing is automatic and nothing is inherited from the
marriage.

The cost is deliberate and must be designed for rather than hidden: **a
step-parent cannot collect their step-child until a standing holder names
them**, and the surfaces should make that grant obvious and easy at the moment
it is needed — on the camp registration screen, on the household screen — rather
than leaving a parent to discover it at a locked gate.

### D35 · Where two standing holders disagree, the more protective answer wins

R6 established that separated parents hold authority independently and that
neither needs the other's agreement. It did not say what happens when they
disagree. It does now:

- a **withdrawal of consent beats a grant** of it;
- a **removal from a release list beats an addition** to it;
- where one holder's instruction would expose the child and another's would
  not, the one that does not, applies.

This is deterministic, needs no adjudication, and cannot be gamed by timing —
which last-writer-wins can. Neither parent can override the other **into**
exposure; either can always pull back toward it. A recorded restriction (R6 §4)
still overrides everything, and where the conflict is about the restriction
itself the platform refuses and routes under R40.

### D36 · The tree is not a mailing list for people who never joined it

Gap-filling requests, customised stories and every other tree-driven
communication go **to signed-in members, about their own branch**. The platform
never initiates contact with a person who is in the file but not a member.

The file was submitted to AFRP for the family-tree project. Using it to reach
roughly 27,000 living people who never agreed to hear from the federation is a
different purpose than the one it was given for, and it is not one a build
decision may take. Recruitment through the tree, if it is ever wanted, starts
with the submitting project lead's agreement and a Board decision, not with a feature.

### D37 · The household and the tree are two models, linked by one node

They answer different questions and must not be merged:

- **The household** — `core.Household`, `HouseholdLink`, `authority/` — is *who
  lives together now and who may act*. It changes the day a divorce is recorded.
- **The tree** — `tree.Individual` and its families — is *descent and history*.
  A marriage that ended is still a marriage; the children still belong to the
  family record it created.

Between them sits exactly **one audited link per person**: `Person` ↔ tree node,
established once (D30), revocable with a reason, never duplicated. A blended or
separated family breaks any model that derives one of these from the other,
which is why neither derives from the other here.

---

## 6. Scenarios the build must answer, and the rules that answer them

These are not open questions. Each is settled by a decision above or by one
already ratified; they are listed because each is a place the obvious
implementation is wrong.

### Divorce

| Scenario | The rule |
|---|---|
| A divorce is recorded | Both parents keep every power. R6 P3: separation "does not by itself reduce either one's authority." |
| The marriage in the tree | **Not deleted.** The family record persists with a dissolution date — the children belong to it, and it is history. |
| The divorcing member was admitted under 4.1.1 "married to one having such origin" | The life event **does not touch the membership**. Whether it survives is an open question in the rules register; a divorce must not answer it by inference. |
| The child now lives in two households | R6 §6, ratified: authority is per person; pickup runs through the release list; directory choices take the more protective; **club attachment stays OPEN**. |
| The camp four-per-family cap | Follows the **household**, not the parent — and a child in two households counts once. A cap that double-counts a child of divorce penalises them for it. |

### Blended families

| Scenario | The rule |
|---|---|
| A new spouse joins a household with children | **D34** — nothing until granted. |
| A step-child wants camp or a programme | **Already eligible.** Camp has no descent test — selection is quota, per-club odds and the family cap. Nothing reads lineage, and nothing should start. |
| A step or adopted child is linked into a Ramallah family | The link is typed **non-lineage** and can never produce a 4.1.1 path. This is not a preference: a marriage that manufactures eligibility breaks **D16** and **D32** at once. |
| Half-siblings across two marriages | One tree, two family records, one household — the model already carries this once D37 keeps them separate. |
| A child with two parents and two step-parents | Up to four adults, two households, one release list per event. **D35** resolves their disagreements. |

**Adoption needs its own decision and does not have one.** An adopted child may
be wholly a family member socially and not a descendant genealogically, and the
tree's premise is that descent is evidence. Until that decision exists the
platform records the adoptive link as non-lineage, says so plainly on the
person's card, and refuses to infer anything from it — R40.

### The committee's bulk workflow

| Scenario | The rule |
|---|---|
| A committee member exports, edits in Family Tree Maker, re-imports | **A diff preview before apply**, naming what the import adds, changes, and would remove. Under D11 the file is master, so this is the moment the platform's accepted changes can vanish — silently, and with no way to tell afterwards. *Since 2 Oct 2026: under D69 the Hub wins during the run, and an import's conflicts are held for a decision and never merged (P28 §4.3).* |
| The import file is missing 200 people | **Never a deletion.** `JF-056` already holds: a person is closed as merged or deceased, never deleted. An older file is an older file. |
| Two committee members import different exports | Refused, not merged. A single-writer lease on the import, and an import whose parent export is not the current one is rejected with what changed since. |
| The committee wants to change a record directly | Allowed, and **audited like any other change** — who, when, why — and **D12** applies: a correction touching a decided line re-evaluates and flags it. |
| A proposal needs more information | A **third decision state**: *needs information*, with the question visible to the proposer and the request staying open. Not a rejection with a note — the queue's aging must show it as still live. |

### Communications and the relationship view

| Scenario | The rule |
|---|---|
| A gap-filling or story mailing | Members only, own branch only (**D36**), through the comms consent filter, recording the withheld by name as club mailings do. **No file, no download, no other family's branch.** |
| A customised story about a living relative | Consent under D22/D33. **Stories about the deceased are the safe centre of this feature** — already published in Shaheen 1982 under D15 — and are where its emotional weight belongs. |
| A story or mailing would name a person a restriction exists against | **Suppressed**, without telling the recipient why. R6 §4 already forbids stating a restriction's substance to the person refused; the same applies here. |
| "How am I related to X" | The oldest known harm in consumer genealogy: in a 28,000-person, fifteen-generation file this **will** eventually reveal a half-sibling, an adoption, or a non-paternity event to someone who did not know. The feature must be designed for that outcome rather than surprised by it — the path shown to its documented links, no inference across a non-lineage link, and no claim the record does not carry. |

---

### D38 · The four branches, and the roots beneath them

The programme structure is renamed and re-cut. What the code calls **rails**
(`programs/rails.py`) becomes **branches**, to hold one motif across the
platform, and the four are:

| Branch | Members, in order | Shape |
|---|---|---|
| **Education** | Camp Ramallah (13–17) · Arabic Program · HS Senior Award (senior year) · Scholarship (college) · Project Hope (18–29) · Leadership Ramallah (21+) | **ladder — by age** |
| **Leadership** | Emerging Leaders (16–24) · RBPN (career) · Congressional Outreach · Day of Action · ECEM missions | **ladder — by capacity** *(since 2 Oct 2026: "Emerging Leaders" names no programme in any source, and the 16–24 band has no source, Q-178; P25 §2.2)* |
| **Heritage** | Preservation Project · Hathihe Ramallah · Bookstore | **cluster** |
| **Care** | Medical Mission · Women to Women · Senior Living · *Ramallah Foundation* · *Endowed Fund* | **destinations** *(since 2 Oct 2026: Senior Living is the Foundation's project, Q-203, P23 §8; the Relief Fund is on the Care branch, P23)* |

*Since 30 Sep – 2 Oct 2026:* D53 puts the family tree on the Heritage branch ("The family tree is part of Heritage"), so the next paragraph is superseded on that point. The HS Senior Award's status is in question (Q-163). *Since 3 Oct 2026:* it continues (D82).

**The family tree is not on this list. It is the roots.** D30 already made every
member's node the thing the rest of the platform resolves people through, so the
tree sits *beneath* all four branches rather than inside Heritage. Heritage
keeps Preservation, the magazine and the bookstore, and grows from it.

**The Convention is not on this list either.** It is the junction where all four
branches meet — the whole federation in one room once a year — and it is
reachable from every branch and owned by none. It is not a rung on anything.

### D39 · A branch has a shape, and the shape decides what "next" means

Only one branch is genuinely a sequence, and a model that assumes otherwise will
invite people to advance from the Preservation Project to the magazine as though
that were a promotion. Each branch therefore declares a shape:

- **ladder — by age.** Ordered; a milestone fires an invitation into the inbox.
  Education. The Arabic Program is the exception inside it: a rung open at any
  age, which the invitation logic must know rather than schedule.
- **ladder — by capacity.** Ordered by readiness, not birthday; entry is at
  Emerging Leaders and the order is a suggestion, never a prerequisite.
  Leadership. *Since 2 Oct 2026: Emerging Leaders has no source (Q-178). P25 §2.2 enters the branch at whichever of its programmes a person first takes part in, as a design choice. The young-adult rungs are Leadership Ramallah, the Day of Action and the Young Leader Committee's club gatherings (P25 §3).*
- **cluster.** Unordered, always open, no "next" and no milestone invitations.
  Nobody graduates from Preservation to the magazine. Heritage.
- **destinations.** Entered by choice or capacity to give; never invited by
  progression. Care.

The rails module's existing promise is unchanged and now applies per shape:
programmes are windows, not gates; skipping a leg is normal; nothing auto-enrols
anyone; a milestone fires an **invitation**, and declining is recorded where the
member can see it and nowhere a committee can.

**Branches and rungs are orthogonal.** A branch is horizontal — movement across
programmes. The five-rung ladder of D25 (*Hear · Show up · Take part · Give or
serve · Lead*) is vertical, inside one programme. A member is somewhere on a
branch and at some rung of each programme on it, and neither number implies the
other.

### D40 · A fund is shown on its branch and cannot be joined

The **Ramallah Foundation** (NY, 1943) and the **Endowed Fund** (ARFECF,
proposed) appear on the Care branch as where it leads. They are **not
programmes**: no enrolment, no rungs, no invitations, no charter obligations.
You give to them; you do not join them.

This is also what keeps the Endowed Fund off the critical path. Its **Endowment
Fund Policy Statement has never been produced** — one of the five missing
documents — and a fund may be listed while its policy is outstanding, where a
programme with rungs and a lifecycle could not be.

---

## 7. What the rename actually costs

**Corrected 8 September 2026, by slice T1a, which did the work.** This section
originally claimed eleven files and about 59 occurrences. That inventory was
wrong: it was produced by grepping for the word rather than for the *sense*, and
**three unrelated senses of "rail" live in this codebase**. Only one belongs to
this decision. The six shared services every programme runs on are also called
rails, by another design document, and renaming those would have broken a live
term. **Six files carried this decision's sense and six changed.**

The lesson is the section's own: a rename inventory counts meanings, not
strings, and a grep cannot tell them apart. `programs/rails.py` is now
`programs/branches.py`; the member route `/me/pathway/` is `/me/branches/`.

**Do the rename and the re-cut in one slice, not two.** Renaming first leaves
the four old groupings under new names — which is worse than either state,
because the words would then be right and the contents wrong. The re-cut moves
RBPN out of the youth pipeline, moves the Arabic Program from Heritage to
Education, moves Emerging Leaders from Education to Leadership *(since 2 Oct 2026: no source, Q-178)*, adds the
bookstore to Heritage, adds Senior Living to Care, lifts the tree out to the
roots and the Convention out to a junction. Every one of those is a change of
meaning, and the tests that name the old rails are the ones that will catch a
half-finished migration.

---

## Provenance

| Section | Grade |
|---|---|
| D30 node ≠ lineage claim | **decided** — David Saah, 8 Sep 2026 |
| D31 life events queue | **decided** — confirms ratified D14 |
| D32 book carries no eligibility force | **decided** — David Saah, 8 Sep 2026 |
| D33 announcements follow D22 | **decided** — David Saah, 8 Sep 2026 |
| D34 step-parent holds nothing until granted | **decided** — David Saah, 8 Sep 2026 |
| D35 the more protective answer wins | **decided** — David Saah, 8 Sep 2026; closes a gap R6 left |
| D36 the tree is not a mailing list | **decided** — David Saah, 8 Sep 2026 |
| D37 household and tree are two models | **decided** — David Saah, 8 Sep 2026 |
| D38 four branches, tree as roots, Convention as junction | **decided** — David Saah, 8 Sep 2026 |
| D39 per-branch shape decides what "next" means | **decided** — David Saah, 8 Sep 2026 |
| D40 a fund is shown, not joined | **decided** — David Saah, 8 Sep 2026 |
| §3 integration map, §4 custody, §6 scenarios, §7 rename cost | proposed — derived from the above and from D11–D22; unratified |
| **Adoption** | **undecided** — recorded as open under R40; the platform infers nothing until it is answered |

**To do:** add D30–D33 to `AFRP-Decisions-Register.md`; add the catalogue rows
in `tree-integration-rows.yaml` to `journeys/catalog.yaml`; correct the stale
"family tree cannot be built" block in `ai-memory/08-OPEN-QUESTIONS.md`, whose
five named documents have been on disk since 7 September.
