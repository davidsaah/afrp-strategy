# The family tree in practice

### The migration from how the tree is kept today to what D66 and D68 to D74 decide: custody of the master file, the corrections queue, access to the clan books, the volunteers' second site, and oral-history consent as a written, scoped consent

**Design note P27 · 2 October 2026 · for the Hub's `tree`, `member`, `committees` (CW1, CW2), `comms`, `heritage` (the archive index) and `access` modules**

**Amended 2 October 2026 for D68 to D74.** This note was written the same day against D11's staging, before David decided D68 to D74 (Decisions Register, Part 5). Those decisions win (D41) and the note now follows them: the handover after one clean annual cycle is replaced by D69's parallel run (`AFRP-Family-Tree-Module.md`, P28 §4.3, slice T2d); who proposes follows D70, how the committee approves follows D72, and what a member sees of the living follows D71. What this note adds that P28 lacks stays here — the custody register (§3), the corrections door (§4), clan-book access (§5), oral-history consent as a written release (§6) and the volunteers' prototype with the archive index (§7); P28 §15 says how each sits with P28, and §11 below marks the slices folded into P28's.

**What this note rests on.** `AFRP-Family-Tree-Design.md` (20 August 2026: lineage as evidence, D15–D18) and `AFRP-Family-Tree-Integration.md` (8 September 2026: D30–D40, custody of the GEDCOM, the committee's bulk workflow); the Decisions Register's family-tree decisions D11–D22, D27–D28, D30–D37, D53 and D66, and its conflicts section of 2 October 2026; the built slices T1a–T1d and the GEDCOM round-trip (`AFRP-Delivery-Status.md`); the `tree-submission` workflow (added 2 October), which records today's practice; and the research round of 2 October 2026 (the Heritage report's sections on the Family Tree and the Preservation Project). P1 (`AFRP-Committee-Workspace.md`) gives the committee its seats and queue; P15 (`AFRP-Incident-Response-and-Retention.md`) the retention schedule.

**Precedence (D41).** The by-law texts (4.1.1, 4.2.1) first; then the Decisions Register and the named design documents; then the prototype (`#/member/family`, `#/fed/tree`, a story); then the Hub's `tree` module (what is). Today's practice is evidence. **Every decision in this note's subject already exists**; the practice differs from almost all of them. So this note designs the **migration** — the order in which practice moves onto what the record decides — and builds nothing that contradicts a decision. Where a step needs a practice owner's act, it waits for it and says so. The register's conflicts section is explicit that "nothing in the platform changes until it is" settled; this note keeps to that: each step that would change what members experience today is gated on its question.

**Public-repo rule.** No living person is named, including the project's lead; no clan book, family or file is named; no figure beyond what the record already publishes.

---

## 1. What the record already holds

### 1.1 Decided

| # | Decision | What it requires of the migration |
|---|---|---|
| D11 → D69 | D11's staging (a governed mirror until one clean annual cycle) is **superseded by D69**: the Hub becomes the record after a parallel run of 30 to 60 days in which the Hub wins; the external file is then read-only and the Hub exports a GEDCOM backup every night | The master file is the source of imports until the run ends; every surface says which side is the record; the custody register (§3) records the file's status through the run and after it; the cutover is P28 §4.3 (T2d) |
| D12 | A correction touching a decided line is re-evaluated and flagged, never auto-revoked | Built (T1c) |
| D13, D70 | **Members in current national standing may propose changes**; no account exists for non-members to contribute (D70, confirming D13) | The proposal surface is for every signed-in member in standing; nobody's approval stands in front of proposing |
| D14, D72 | **Every life event queues** for the committee (D14); **one committee approval** applies an own-household life event or a non-structural correction, **two approvals from different committee members** a structural change; clan stewards pre-review and never approve (D72, amending D14's mitigations) | The committee, not a person outside it, decides what reaches the tree |
| D15 | Public build: deceased real, living synthetic | The real file never enters any repository |
| D16 | The tree is evidence for a human decision, never a verdict | Unchanged by anything here |
| D17, D71 | D17's "all members see everything" is **amended by D71**: a signed-in member sees the living in full inside their own branch (blood relatives sharing an ancestor no further back than a great-great-grandparent, and their spouses); outside it a living person shows a name and a position only | Access inside the platform is by membership standing within D71, not by approval |
| D20 | Unapproved edits shown in place, marked pending | Built (the hourglass viewer); moves onto the plate in T2a (D68) |
| D21 | One bundle per sitting of work, with its blast radius | Built |
| D22 | Full media, **per-item consent held by the subject**; the deceased set by the committee on next-of-kin request with the depositor's rights recorded; a minor's through the household, re-asked at eighteen | The pattern for oral histories (§6) |
| D28 | **Nothing for the living without sign-in** | The clan books and the tree never render signed out |
| D30–D37 | Every member a node, never a lineage claim; life events queue; the new edition has no eligibility force; announcements follow D22; the tree is not a mailing list (D36); household and tree are two models | Unchanged |
| D53 | The tree is on the Heritage branch | — |
| D68, D73, D74 | The tree drawn in the print book's plate grammar on every surface (superseding D27); membership and join the first integration; the print pipeline decided after the January 2027 Mid-Year | P28; nothing in this note depends on them |
| D66 | **The shared drive is the archive of record**; the platform holds its registers and links to the drive for documents | The clan books, recordings and releases live on the drive; the platform indexes and links |

### 1.2 Built (`AFRP-Delivery-Status.md`)

The GEDCOM parser round-trips the master file byte-identically; 28,226 people and 10,399 families imported (the published counts); the kinship engine; the hourglass viewer with draft branches, bundle submission and pending nodes in place (D19–D21); the committee queue with a third state, *needs information* (T1c); **a diff preview before any import applies anything; an import missing people deletes nobody; a second import from a stale export is refused with what changed since; a committee direct edit is audited and D12 flags the decisions on the corrected line** (T1c); a single-writer lease on imports (Integration §6); member nodes and the life-event pipeline with R6 as its gate (T1b); mailings to members about their own branch only, the audience builder unable to express a non-member (T1c, D36); the book organised from the tree with no eligibility force (T1c, D32); the tree on Heritage (T1d). Import and export sit under `tree:moderate`, the Family Tree Committee alone (JF-070).

### 1.3 Today's practice (the research round, role level)

| # | Practice | The decision it differs from | Question |
|---|---|---|---|
| 1 | The master file lives in **a commercial desktop genealogy product not held in the Federation's name**, with the product's cloud copy | D11, now D69 (the Hub the record after a parallel run) | Q-201 |
| 2 | The interactive tree is that product's cloud sharing, **joined by personal invitation** | D17, now D71 (the living in full inside one's own branch) | Q-200 |
| 3 | The clan genealogy books are PDFs on a members-only site, **reached by a request the lead approves "by agreement with the board"** — a rule asserted, not minuted | D71 (amending D17); D28 for the living dates the books carry | Q-200, Q-202 |
| 4 | **Corrections arrive by form or e-mail** to the lead, who applies them; the committee has two members | D13, D14, now D70 and D72 (members in standing propose; the committee decides through a queue with one or two keys) | Q-200 |
| 5 | **A volunteer's prototype site** (July 2026) links archive items to per-person tree profiles; the Preservation committee sought youth volunteers (February 2026) to rebuild its stand-alone website | D66 (the drive is the archive), D69 (one tree, one record) | Q-190, Q-191 |
| 6 | **Oral histories are recorded on one spoken question** granting "full permission and rights to share this video with the Ramallah community and any other projects that would benefit"; no written release, no separate print or web permission, no takedown or next-of-kin clause | D22 (per-item consent held by the subject) | Q-189 |

The public page (2025) lists the fields a member may ask to update: births, deaths, marriage and divorce dates, immigration dates and name corrections. The programme director convenes the committee's strategy meetings; a web agency changes the public page on its monthly allowance.

---

## 2. The migration, in stages

The order below is the design. Each stage has an entry condition that is a question answered or an act recorded, never a date the platform sets; each leaves today's practice working until the stage after it is entered. *Design choice*: a migration that switches off a working practice before its replacement is accepted by the people who run it would break D69's parallel run, in which the record keeper's edits keep arriving as imports until the committee ends the run.

| Stage | What changes | Entry condition | What stays as it is |
|---|---|---|---|
| **Stage 0 — Mirror** (today, built) | The committee imports exports of the master file into the governed mirror through the diff preview; members see the tree in-platform under D17 today, narrowed to D71 in T2a | Built | The master file, the product's sharing, the clan-book site, the form and e-mail, all as today |
| **Stage 1 — Custody recorded** | The master file's custody is a register on the platform: licence holder, account, cloud copy, key-holders, the agreed export cadence, the last export imported (§3) | Q-201 answered: whose licence and account, who else can open it, what cadence | The master file stays in the product until D69's run ends |
| **Stage 2 — One door for proposals** | Members propose in-platform (built); the public page and the form point signed-in members to it; requests already in the lead's hands are worked to the end the old way and arrive through the next import (§4) | The Family Tree Committee's dated act adopting the platform's queue as its intake, with its seats on CW1 | The lead applies accepted changes to the master file until D69's run starts; during the run the Hub wins |
| **Stage 3 — Access by the record's rule** | The clan books and the interactive tree are reached by signed-in members by standing within D71 (and nothing signed out, D28), not by personal approval (§5) | Q-200 (the Board says what the test is and whether "by agreement with the board" exists as a minute) **and** Q-202 (the living dates the books carry, and under what consent) | The product's cloud sharing continues for whoever the lead invites; the platform neither stops nor mirrors it |
| **Stage 4 — The parallel run and the cutover** | **Superseded by D69.** The Hub becomes the record after a parallel run of 30 to 60 days in which the Hub wins; at its end the product's file is read-only and the Hub exports every night (P28 §4.3, slice T2d; §8 below) | The committee's dated act starting the run, on P28 §7's gates (a production database with backups; Q-201) | — |

The oral-history consent (§6) and the volunteers' site (§7) are not stages of the tree's migration; they run beside it and are gated on their own questions.

---

## 3. Stage 1 — custody of the master file

The platform does not hold or operate the desktop product and does not ask for its credentials. It holds a **custody register** for the master file, one row per fact, each dated, sourced and attributed: the product (named generically on public surfaces); the **licence holder** (a person or the Federation); the **account** that holds the file and its cloud copy (by role, never by credential); **key-holders** — who else can open the file; the **export cadence** the committee adopts; and, per import, the **export's date and the supplying seat** (the stale-export refusal and the lease are built). Rows with no value show "not stated (Q-201)". *Design choice*: the platform records custody so that the Board can see it; it decides nothing about it. Under D69 the register also shows the file as the source of the parallel run's imports and, after the run's end, as read-only; P28's nightly export rows sit beside it.

**What the register makes visible.** "The last export imported" against the cadence, so a mirror that has gone stale is seen; "one key-holder" as a fact on the committee's page and on the Federation lens's risk view (P15's incident register reads it for the *availability* class); the licence's renewal date as a follow-up to the committee's seat (the agreements register's renewal pattern, P11).

**What it never does.** Store the file outside the mirror's import path; export the tree to anyone outside `tree:moderate` (Integration §4); hold the product's credentials.

---

## 4. Stage 2 — the corrections queue as the one door

### 4.1 What is built and what stage 2 adds

The queue exists (T1b, T1c): any signed-in member proposes (D13; D70 bounds it to members in current national standing); every life event queues (D14); a sitting of work is one bundle with its blast radius (D21); pending changes show in place (D20); the committee decides with three states, *needs information* keeping the request open; R6 gates who may declare for a minor; an unsourced structural claim sorts to the top for dismissal (D14's note). D72's tiers and clan stewards are built in P28's slice T2c. **Stage 2 adds no queue.** It adds the joins that move today's two doors (the form and e-mail to the lead) onto it.

### 4.2 The committee on the register

The Family Tree Committee becomes a CW1 body (P1 already makes the tree's committee an instance): its seats with their appointing acts, or "no appointing text" where none is found (P1 §2.2) — the record holds no constituting act for this committee and no seat for "the project lead". The lead, if a committee member, holds a committee seat like any other; **the platform has no seat called "project lead"**, and nobody outside the committee applies a change. Under D72 one committee member's approval applies an own-household life event or a non-structural correction, and a structural change needs two approvals from different committee members; clan stewards recommend and never apply (P28 §4.2, T2c). D14's note that structural changes wait for a quorum is now D72's two keys; the second key-holder is a committee member seated by the committee's own act (D79, 3 Oct 2026; Q-262) and a committee's quorum in general stays Q-52. *This builds D14 as amended by D72; how the committee is constituted is the Board's, under Q-200 and Q-52.*

### 4.3 Moving the two doors

- **Signed-in members.** The public page's "how to update" text points to the in-platform proposal (the change goes through the programme director and the web agency, as practice does). The fields the public page lists map onto proposal kinds the queue already holds (birth, death, marriage, divorce, immigration date, name correction); immigration date is a node fact, not a life event, and is proposed as an edit. *Design choice.*
- **The form and e-mail.** Not imported. The form's rows are personal data collected under no platform consent; the platform does not read the form's sheet or the lead's mailbox. Requests already received are worked by the lead the old way and **arrive through the next export**: the diff preview shows them as changes made outside the queue, attributed to the import and its supplying seat, and the committee accepts or questions the import as a whole (built). From stage 2's entry the form tells a member to propose in-platform. **D70 answers Q-259 for the platform**: no account exists for non-members to contribute. Whether the committee keeps its own public form open to non-members outside the platform is the committee's practice, which the platform does not read; Q-69 still holds whether a non-member contact may be linked to a node.
- **The lead's own work.** De-duplication and pruning in the master file continue until D69's run ends and arrive as imports through the diff preview (during the run, against the Hub's version, with conflicts held, P28 §4.3); a merge the platform sees is a node closed as merged, never deleted (JF-056, built).

### 4.4 What the committee sees that it does not see today

The queue's ageing, the triage order, and per decision the seats present, the bundle, the sources and D12's flags. Counts of proposals decided per quarter go to the committee's report (P1 §4.1, CW3) and to Heritage's outcome line "corrections and life events resolved by the Family Tree Committee" (`branches.yaml`) under the floor.

---

## 5. Stage 3 — access to the clan books under the record's rules

### 5.1 What the record says

- **D17, amended by D71**: D17 had all members see everything, recorded as matching "how the Google Group works today" and as the one setting worth revisiting before launch; the research round shows access is in fact by the lead's approval. D71 now sets the rule: a signed-in member sees the living in full only inside their own branch, and outside it a name and a position.
- **D28**: nothing about the living without sign-in. The clan books carry living people's dates, as the printed 1982 volume does (Q-202).
- **D66**: documents live on the drive; the platform links to them.
- **4.1.1** points at Shaheen 1982, the fixed volume; the clan books are publications of the project, not the eligibility test (D32's reasoning applies to them by the same logic: nothing the platform serves becomes the by-law's test).

### 5.2 The design, switched on at stage 3

- **Who.** A signed-in member in good standing (4.3.1, scoped as the directory's ceiling is, D28 and P19 rule 2), with no approval step. A member within the directory's grace window keeps access for the same window (the directory's grace, attested in P3; D6 for a dormant club). Nobody signed out; no contact record; no associate member distinction is made unless the Board says so under Q-200.
- **What.** Each clan book is an item on the archive index (§7.2) with its drive location, its date, its compiler's credit as the committee records it, and its living-data flag (Q-202).
- **How it is served.** The drive is the archive of record (D66), but members do not have drive access, and a drive share link handed to members would let a book leave the sign-in boundary at the first forward. The record is silent on how a document held on the drive is served to members. **Q-260** asks it. Until answered the platform lists the books and **serves none**, and the page says "access by the project's process (Q-200, Q-260)". *R40 (a silent text is flagged, not filled); design choice* *Since 4 Oct 2026:* **D88** makes this the rule for now: nothing is served to members, and the drive link goes to the holding committee's seats only; Q-260 stays open for the lasting answer.
- **D71's limit.** A clan book is a fixed document and cannot withhold the living outside each viewer's own branch, so a book carrying living people's details beyond a name and a position is **not served to members by standing**. Whether a book without living details is produced, or such a book is served to the committee only, is Q-202 (widened 2 October 2026). A book carrying only the deceased is served by standing once Q-260 is answered.
- **No download where a living person is in it.** If a book carrying living people's dates is ever served under Q-202's answer, it is viewed in the platform and is not offered as a download, printed or exported, on the same reasoning as the directory's export refusal (P19 rule 6) and D36's "never a file, never a download". *Design choice*, offered with Q-202.
- **The interactive tree.** The platform's tree (the hourglass today, the plate from T2a under D68) is the members' interactive tree under D71; the product's cloud sharing continues for whoever the lead invites and is outside the platform. The platform neither imports nor mirrors its invitation list.

### 5.3 Why stage 3 waits

D71 now sets the platform's rule, amending D17. Switching it on for the clan books still changes what an approved-access practice does today, and the register's conflicts row (Q-200) is the Board's to settle for that practice; stage 3 enters on Q-200, Q-202 and Q-260 and builds D71. If the Board adds an approval step, the decision is recorded with its D-number and stage 3 builds that instead. The platform does not pick.

---

## 6. Oral-history consent as a written, scoped consent

### 6.1 What the record says and what practice does

D22 makes consent per item and held by the subject; the deceased are set by the committee on next-of-kin request with the depositor's rights recorded; a minor's runs through the household and is re-asked at eighteen. D33 adds the sentence that belongs on every consent screen: a published issue cannot be unprinted. The programme register says the archive "ingests only consent-classed material; print consent is its own switch". Practice is one spoken question at the start of the recording (§1.3, item 6). The Oral History Association's published best practice is to obtain and document the narrator's informed consent and to "secure a signed legal release form, ideally when the interview is completed", and to respect a narrator's right "to restrict access to the interview" (OHA, *Best Practices*).

### 6.2 The consent, as a record

The release itself is a document — written, signed, held on the drive (D66) — whose wording the Legal Advisor drafts and the Preservation committee adopts (Q-189). The platform holds, per recording, a **consent row** that mirrors what the signed release grants:

| Field | What it holds |
|---|---|
| The recording | An archive-index item (§7.2): its drive location, date, interviewer's seat, the narrator's node |
| The narrator | A member record, a contact record with consent (D60's pattern), or a deceased person's node |
| Release on file | A dated on-file flag with the drive link; no scan in the platform |
| Scopes, each a separate yes or no | **Community archive** (signed-in members, D28's ceiling); **public web** (signed out, only where the narrator is deceased or grants it); **print** (the Magazine and any book; with D33's sentence that print cannot be recalled); **research use** by a named outside party; **excerpts** in Federation communications |
| Restrictions | A closed period ("not before" a date); passages withheld, as the narrator sets them; a pseudonym if the narrator chooses one |
| Third parties | Living people named in the recording — **the record is silent** on whose consent covers them (**Q-261**) |
| Withdrawal | A new row, never an edit (R27); it removes the item from every surface the platform controls at once and cannot recall a printed page (D33) |
| After the narrator's death | The committee sets the item on next-of-kin request, recording the depositor's rights (D22) |
| A minor narrator | Through the household adult holding R6's consent power; re-asked of the narrator at eighteen (D22, D33) |

**Every scope defaults to no.** A recording with no release on file is shown to the committee's seats only.

### 6.3 What has already been recorded

Whether the 2022 spoken permission covers the existing recordings, and for which scopes, is **Q-189**. Until it is answered each existing recording carries the consent class "spoken permission (2022 form); scope not determined (Q-189)" and is shown to the Preservation committee's seats only; nothing is published, printed or linked to a tree profile from it. *R40 (a silent text is flagged, not filled); design choice* The committee may seek a written release from a living narrator at any time, and the new row then governs. *Since 4 Oct 2026:* **D93** answers Q-189: this is the rule, not an interim; a recording on the spoken permission stays with the committee's seats until the narrator signs a release.

### 6.4 Photographs and contributed records in the same archive

The drive's photograph files are named with families' names and the folder holds contributed service records and biographies of members' relatives (the register's `data_classes`). They follow D22 as photographs already do: per-item consent held by the subject, the deceased by the committee on next-of-kin request. The index (§7.2) holds titles the committee writes, never the drive's file names, so no family's name becomes a platform field by accident. *Design choice.*

---

## 7. The volunteers' second site, and the archive index

### 7.1 What the record says about a second site

D66 makes the drive the archive of record and the platform its index; D69 makes the Hub the one record of the tree and D68 its one look on every surface; D71 and D28 bound who sees the living; Integration §4 forbids any integration that becomes a reason to export the tree, and §3 already designs "a preserved item attaches to nodes rather than to typed names". The volunteer's prototype proposes authentication, the clan books linked per clan after sign-in, a dashboard for the lead, and asks whether the product has an interface to link to rather than build a second tree database. **Whether the Federation wants a second public archive-and-tree site at all is Q-190**; who may serve on a volunteers' team under eighteen is Q-191.

### 7.2 What the platform offers, which is what the prototype was reaching for

**The archive index** — the Preservation Project's register of items (D66's "the platform holds its own registers"): one row per item with the drive location, kind (photograph, document, recording, clan book, contributed biography), date or period, the committee's title and credit, its consent row (§6.2 for recordings; D22 for the rest) and **links to tree nodes**, each link a dated act by a committee seat. A member sees, on a person's page in the tree, the items linked to that node that the member's standing and the item's consent allow. That is the prototype's "per-person profile with linked documents, videos and photographs", inside the sign-in boundary, on the one tree. The index is the substance of P28's Heritage integration (§8 there): its slice FT4 is folded into T2h, which comes after T2f (D78, 3 Oct 2026) and whose place against T2g is Q-265, and where an item's file lives is Q-260.

**What the platform does not do for a second site.** It sends no tree data, no person, no node and no archive item to any site outside it, by feed, export or interface; a public site that wants a deceased person's story may link to the platform's public renderings, which already show the deceased real and the living as nothing (D15, D28). *Rule from Integration §4 and D36, restated, not new.* If the Board under Q-190 adopts a second site as a front end, it would need its own decision on custody, access and the living, and a design note of its own.

### 7.3 The volunteers

Members who offer *archive help* or *oral-history interviewer* are volunteers on P7's rosters with their own dated opt-in; a person under eighteen holds no interest row (P7 §2) until Q-191 says otherwise. Interviewers record each interview against the release (§6.2), not against a spoken question.

---

## 8. Stage 4 — superseded by D69's parallel run

D11 said the platform becomes the body of record "after one clean annual cycle", and this note first offered a DRAFT test of a clean cycle under Q-258. **D69 (2 October 2026) supersedes D11's staging and answers Q-258**: the Hub becomes the record after a parallel run of 30 to 60 days in which the Hub wins; the record keeper's edits arrive as GEDCOM imports through the diff preview and are applied as audited committee edits, with conflicts held for a decision and never merged; at the end of the run the external file is read-only and the Hub exports a GEDCOM backup every night under `tree:moderate`. The run is designed in P28 §4.3 and built in slice T2d; its start waits on P28 §7's gates. The DRAFT is withdrawn.

What carries over from this note: the single-writer lease, the never-delete rule and D12 (built), and the custody register (§3), which records the run's start and end acts and the file's read-only status after it. Nothing in the run changes D28 or D36; D71 governs what members see.

---

## 9. Rules

1. The master file is the source of imports until D69's parallel run ends, and read-only after it; the platform imports only through the diff preview, refuses a stale export, deletes nobody (built), and during the run holds a conflict for a decision rather than merging it (D69).
2. Any signed-in member in current national standing may propose any change (D13, D70); only the committee decides — one approval for an own-household life event or a non-structural correction, two from different members for a structural change, clan stewards recommending only (D14, D72); there is no "project lead" seat (*design choice* for the seat).
3. The platform never reads the form's sheet or a person's mailbox; changes made outside the queue arrive only through an import and are shown as such (*design choice*).
4. Nothing about the living renders signed out (D28); inside, a member sees the living in full only within their own branch (D71); clan-book access by standing switches on only at stage 3's entry.
5. A clan book carrying living people's details is not served to members by standing (D71; Q-202); if served under Q-202's answer it is viewed, never downloaded, printed or exported (P19 rule 6; D36; *design choice*).
6. No tree data, person, node or archive item leaves the platform for another site (Integration §4; D36).
7. The drive is the archive; the platform's archive index holds locations, titles the committee writes, consent rows and node links, never the files (D66).
8. An oral-history recording is shown beyond the committee only under a written release's recorded scopes; every scope defaults to no; withdrawal is a new row and cannot recall print (D22, D33, R27).
9. Existing recordings under the spoken permission are committee-only until Q-189 is answered. *Since 4 Oct 2026 (D93):* until the narrator signs a written release.
10. The deceased are set by the committee on next-of-kin request with the depositor's rights recorded (D22).
11. A minor's consent runs through the household and is re-asked at eighteen; a minor holds no volunteer interest (D22, D33, R6, P7 §2).
12. Custody facts are recorded, dated and attributed; the platform holds no credential (*design choice*).
13. Every refusal names its rule and, where one holds it open, its question.

---

## 10. What this note raises

Carried, not re-asked: Q-52 (quorum), Q-69 (a non-member contact linked to a node), Q-189, Q-190, Q-191, Q-199 (whether clan books are sold), Q-200, Q-201, Q-202; adoption (no decision; R40). From P28: Q-262 (the second key-holder). Answered since: Q-258 by D69 and Q-259 by D70 (2 October 2026); Q-262 by D79 (3 October 2026).

| Q | Question | Owner |
|---|---|---|
| Q-258 | What "one clean annual cycle" means for D11's handover, who records its end, and whether the DRAFT in §8 is the test — **answered by D69** (the parallel run replaces the handover) | David · Family Tree Committee |
| Q-259 | May a person who is not a member ask for a change to the tree (today's public form accepts anyone), and if so through what door and under what consent, given D13 says "any member"? — **answered by D70** for the platform (no account for non-members to contribute) | Family Tree Committee · Membership Committee · Legal Advisor |
| Q-260 | How a document held on the drive (the archive of record, D66) is served to signed-in members without leaving the sign-in boundary: served by the platform from the drive, copied into the platform's storage, or not served; widened by P28 to items attached to tree nodes | David · Digital Infrastructure Committee · Executive Director |
| Q-261 | Living people named in an oral history who are not its narrator: whose consent covers them, and whether a passage about a living third party is withheld from every scope until they agree | Preservation committee · Legal Advisor |

---

## 11. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| FT1 The custody register | The register rows for the master file (licence holder, account by role, cloud copy, key-holders, cadence, renewal) with "not stated (Q-201)"; under D69, the file's status through the parallel run and read-only after it; the per-import export date and supplying seat beside the built stale-export check; the staleness view against the cadence; the single-key-holder fact on the committee page and P15's risk view | §3 | None to build; licence holder and account read the Federation (D87, 4 Oct 2026); the other values wait on the committee's acts and the Board's minute D87 calls for |
| FT2 The committee as a body and the corrections door | The Family Tree Committee on CW1 with its seats and "no appointing text" where none is found; the committee's adoption act for stage 2; the public page's pointer (an office task); the form's notice; nothing reads the form's sheet; decision counts to CW3 and the Heritage outcome line. **In part folded:** the approval tiers into T2c (D72); the label on imports for changes made outside the queue into T2d (D69) | §4 | CW1, CW2, CW3 for the full shape (a committee register row until then); the committee's adoption act to enter stage 2; non-members answered by D70 |
| FT3 Clan books by the record's rule | The clan books as archive-index items with the living-data flag; access by standing and the grace window, signed in only; books with living details not served by standing (D71), view-only if served under Q-202's answer; the "access by the project's process" page until switched | §5 | **Q-200, Q-202, Q-260** (D88, 4 Oct 2026: not served for now) |
| FT4 The archive index — **folded into T2h** | Items with drive location, kind, period, committee title and credit, consent row, node links as dated acts; the person page's linked items under standing and consent; no outbound feed | §7.2 | None; the tree's person page (built) |
| FT5 Oral-history consent | The consent row per recording with the release on-file flag and the five scopes defaulting to no, restrictions, withdrawal, next-of-kin and the minor's path; existing recordings committee-only with Q-189 named | §6 | T2h (FT4 folded into it); the release wording (the Legal Advisor and the Preservation committee; Q-189 otherwise answered by D93, 4 Oct 2026); Q-261 for third parties (passages withheld until answered) |
| FT6 The handover — **folded into T2d** | Superseded by D69: the parallel run, its dated start and end and the freeze are P28's slice T2d; the lease, never-delete and D12 carry over | §8 | P28 §7's gates |

Order: FT1 now; FT2 with CW1; FT3 on its three questions; FT5 after T2h. FT4 and FT6 are folded into P28's T2h and T2d and are not built as slices of their own.

---

## 12. Journeys proposed

| Journey | What it tests | Class |
|---|---|---|
| P27-J01 | The custody page shows licence holder and account as the Federation (D87) and the cadence as "not stated" until the committee's act *(rewritten 4 Oct 2026 under D87; it read: licence holder, account and cadence "not stated (Q-201)")*; an import older than the cadence shows the mirror stale; no field accepts a credential | meets once FT1 lands |
| P27-J02 | A signed-in member in standing proposes a name correction; it queues; one committee approval applies it as a non-structural correction (D72); a structural change waits for a second key from a different member; the decision shows who approved | guarded until T2c |
| P27-J03 | An import carries a change made in the product that never went through the queue; the diff preview labels it "made outside the queue" with the supplying seat; the committee accepts the import as a whole | meets (T1c) once T2d adds the label |
| P27-J04 | Nothing reads the change-request form's sheet; an attempt to bulk-load it as proposals is refused naming D13 and S1 | meets |
| P27-J05 | Before stage 3, the clan books page lists books and serves none, naming Q-200 and Q-260; signed out, the page does not render | meets once FT3's listing lands |
| P27-J06 | After stage 3, a member in good standing opens a clan book carrying only the deceased; a book carrying living details is not offered by standing (D71); no download, print or export affordance exists; a lapsed member past the grace cannot open it | guarded until Q-200, Q-202, Q-260 |
| P27-J07 | An archive item linked to a deceased person's node shows on that person's page to a signed-in member; an item whose consent row grants only the committee shows to nobody else | meets once T2h lands |
| P27-J08 | No endpoint, export or feed sends a node, a person or an archive item to an outside site | meets |
| P27-J09 | A recording with a written release granting community archive and not print appears to signed-in members and is refused to the Magazine's issue builder naming the print scope | guarded until FT5 |
| P27-J10 | A narrator withdraws; the item disappears from every platform surface the same day; the consent screen had said a printed page cannot be recalled; the withdrawal is a new row | guarded until FT5 |
| P27-J11 | A recording made on the 2022 spoken permission shows only to the Preservation committee's seats, naming Q-189 | meets once FT5 lands |
| P27-J12 | A seventeen-year-old cannot be recorded as an archive volunteer or an interviewer; a minor narrator's consent is taken from the household adult and re-asked at eighteen | meets (P7-J03, R6) |

---

## 13. What changes in the site's data with this note

`programmes.yaml`: `family-tree`'s `platform_needs` cite this note's stages 1–4 and slices FT1–FT6, its `questions` gain Q-258 to Q-260; `preservation-project`'s `data_classes` cite §6 for the written, scoped consent and its `platform_needs` cite §7.2 for the archive index and Q-261. `workflows.yaml`: `tree-submission` cites this note as its migration and gains the stage 2 adoption act as a step; `tree-life-events` cites §4.3 for the fields the public page lists. `experiences.yaml`: the `member` lens gains the linked archive items on a person's page; the `committee-member` lens the custody page and the queue's counts. `questions.yaml`: Q-258 to Q-261 numbered by governance. The crosswalk: rows D22, F8 and C4 cite this note, and a P27 row joins the design-notes table. `plan/MASTER-PLAN.md`: rows FT1–FT6. *Amended 2 October 2026:* the same entries now also cite P28 and D68–D74; Q-258 and Q-259 are marked decided (D69, D70); FT4 and FT6 are marked folded into T2h and T2d.

---

## Sources

**Record.** AFRP By-Laws 2024, 4.1.1, 4.2.1, 4.3.1; `AFRP-Decisions-Register.md` (D6, D11–D22, D27–D28, D30–D37, D41, D53, D60, D66, D68–D74; the conflicts section of 2 October 2026); `AFRP-Family-Tree-Design.md`; `AFRP-Family-Tree-Integration.md` §2–§6; `AFRP-Family-Tree-Module.md` (P28); `AFRP-Delivery-Status.md` (the family tree, slices T1a–T1d); `AFRP-Committee-Workspace.md` (P1) §2, §4; `AFRP-Volunteer-Interests.md` (P7) §2; `AFRP-Directory-Formats.md` (P19) rules; `AFRP-Incident-Response-and-Retention.md` (P15); `AFRP-Care-Grants-and-Partners.md` (P11, the agreements register's renewal pattern); `site/data/programmes.yaml` (`family-tree`, `preservation-project`), `workflows.yaml` (`tree-submission`), `branches.yaml`, `questions.yaml`.

**Research.** Research round, 2 October 2026 (heritage §1, §3, §6, §7), private.

**Public.** Oral History Association, *Best Practices*: https://oralhistory.org/best-practices/ (read 2 October 2026: informed consent documented; "secure a signed legal release form, ideally when the interview is completed"; the narrator's right "to restrict access to the interview"). FamilySearch, *The FamilySearch GEDCOM Specification* (version 7): https://gedcom.io/specifications/FamilySearchGEDCOMv7.html (the interchange format the mirror's imports use; whether the product in use exports GEDCOM 7 or 5.5.1 on a schedule is **not confirmed**). Ancestry's living-persons policy, as read by the research round (living people hidden in shared trees by default, with a removal route): https://www.ancestry.com.au/c/legal/PrivacyForYourFamilyTree — another organisation's practice, not a rule here.

**Not verified.** Whether any Board minute records the lead's "by agreement with the board"; whether the clan books carry living people's dates in every volume; whether the desktop product offers an interface the volunteers asked about.
