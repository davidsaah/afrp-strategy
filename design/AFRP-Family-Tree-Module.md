# The family tree module

### The book's look on screen, members proposing and the committee deciding, the Hub as the record, and the tree reaching membership, the magazine, the directory and Heritage

**Design note P28 · 2 October 2026 · for the Hub's `tree`, `member`, `join`, `dues`, `access`, `rules`, `magazine`, `memberdir`, `comms` and `reporting` modules**

**Why now.** On 2 October 2026 David decided D68 to D74 (Decisions Register,
Part 5): the tree takes the print book's plate grammar everywhere (D68,
superseding D27); the Hub becomes the tree's record after a parallel run (D69,
superseding D11's staging); members in current national standing contribute
(D70, confirming D13); the living are seen in full only inside a member's own
branch (D71, amending D17 and answer 22); the committee approves in tiers with
clan stewards (D72, amending D14's mitigations); membership and join is the
first integration (D73); the print pipeline waits for the Mid-Year (D74). This
note is what the T2 slices are cut from. It raises Q-262 to Q-270 and adds to
Q-201 and Q-260.

**Since 3 October 2026.** David decided D76 to D79 (Decisions Register, Part 6):
D71's radius reaches third cousins (D76, Q-272); the plate is the default view
and the hourglass stays as an alternative view (D77, Q-270); magazine and life
events is the next integration (D78, Q-265 in part); the second holder of
`tree:moderate` is a committee member the committee seats (D79, Q-262). Later
the same day: the hourglass is drawn in the plate grammar (D80, Q-279), and §6's
list is the structural-kinds row (D81, Q-264). The sections below follow them,
each change marked with the date.

**What it rests on.** D11 to D22 and D28 (the tree, August 2026); D30 to D37
(the tree as the platform's spine, `AFRP-Family-Tree-Integration.md`); D53 (the
tree on Heritage); D36 and P4 (`AFRP-Family-Referral.md`) for what the tree may
never be used for; D66 (the shared drive is the archive of record); answers 22,
23, 27 to 31 in `plan/QUESTIONS-FOR-DAVID.md` (living visibility, custody, one
file, the committee, the grade words, rules as data); R6, R7, D33 for minors;
`AFRP-Family-Tree-Design.md`, `AFRP-Shaheen-1982-Eligibility-Source.md` and
`AFRP-Family-Tree-In-Practice.md` (P27, written the same day against D11's
staging and amended for D68 to D74; §15 below says how the two notes divide the
work). The plate grammar is read from the print edition's own key page ("How to
Read a Tree") and its cover; the book's generator was not read for this note.

**Precedence (D41).** By-law texts first (4.1.1, 4.2.1, 5.1, 16.1.1), then the
register and the named design documents, then the prototype as story, then the
Hub as what is. Where the record is silent this note names the missing piece and
a Q-number; it picks no default.

**Public-repo rule.** No living person, no real tree data, no figures beyond
those already published in the record.

---

## 1. What the record already holds

**Built (slices T1a to T1c, 7 and 8 Sep 2026).** The `tree` module: a GEDCOM 5.5
reader and writer that round-trips the committee's export; every import a
version; the hourglass viewer with draft branches, bundle submission and pending
nodes in place (D19 to D21); the father's line to the top with a per-link grade
and the evidence packet (UNDETERMINED, never a verdict, D16); search; the
proposal queue with sittings, blast radius and the *needs information* state;
import and export under `tree:moderate` with the diff preview, the never-delete
guard and the stale-export refusal; committee direct edits audited with D12
flags; the node on every member (D30) with one audited link (D37); the
life-event pipeline (D31) gated by R6 with D33 consent and offers that never
fire; own-branch mailings (D36). The living-visibility rule is one setting,
`tree.policy.LIVING_VISIBLE_TO`.

**Designed, not built.** The tree on Heritage (slice T1d, D53); "how am I
related"; per-subject photo consent (D22); the death approval gate (workflow
`tree-life-events`); P27's custody register, corrections door, clan-book access
and oral-history consent (slices FT1 to FT5).

**Decided today.** D68 to D74, quoted in §2.

**Practice (role-level).** The record keeper maintains the tree in a desktop
genealogy program and exports GEDCOM; corrections arrive by a web form into a
sheet and by email; the committee listed two members in its 2026 overview; a
first print run is planned with a family-update deadline of 30 September 2027
and sample chapters at the January 2027 Mid-Year (P27 §1.3; the programme
register's `family-tree` entry).

---

## 2. The rules, verbatim, and the parameters they leave

| | Adopted wording (Decisions Register) | Parameters it leaves, and who sets each |
|---|---|---|
| **D68** | The tree is drawn in the print book's plate grammar on every surface. | None. The grammar is specified in §3. *Since 3 Oct 2026:* D77 limits D68 as applied to D19: the plate is the default view on every surface and the hourglass stays available as an alternative view (Q-270 answered). |
| **D69** | The Hub becomes the record of the tree. During a parallel run of 30 to 60 days the Hub wins: the record keeper's edits arrive as GEDCOM imports through the diff preview and are applied as audited committee edits, with conflicts held for a decision and never merged. At the end of the run the external file is read-only and the Hub exports a GEDCOM backup every night under `tree:moderate`. | **Start of the run**: the Family Tree Committee, as a dated act (gated, §7). **Length within 30 to 60 days and the end**: the committee, as a dated act. |
| **D70** | Members in current national standing may propose changes. No account exists for non-members to contribute. | None. |
| **D71** | A signed-in member sees the living in full inside their own branch: blood relatives sharing an ancestor no further back than a great-great-grandparent (out to second cousins), and the spouses of those relatives. Outside it a living person shows a name and a position on the plate only. D28 is unchanged. | **The radius** (great-great-grandparent) is a row on the rules register, set by D71; a change is a dated act of the Board or the committee under a citation. D71's wording also says "out to second cousins", who share a great-grandparent. *Since 3 Oct 2026:* D76 reads the radius: the great-great-grandparent governs and the branch reaches third cousins; the parenthesis is an error (Q-272 answered). |
| **D72** | One committee approval applies an own-household life event or a non-structural correction; two approvals from different committee members apply a structural change. The committee may appoint clan stewards, who pre-review and recommend for their clan and never approve. | **The list of structural kinds**: a row on the rules register, set to §6's list by D81 (3 Oct 2026, Q-264); the Family Tree Committee may amend it by a dated act. *(Until D81: unset, with the list shown as a proposal.)* **Steward appointment, number and term**: the committee (Q-263). **The second holder of `tree:moderate`**: a committee member seated by the committee's own act (FT2), chosen over the project's lead (answer 31) (D79, 3 Oct 2026). |
| **D73** | Membership and join is the first integration. | **The order of the other three** (magazine and life events; directory and comms; Heritage): David (Q-265). *Since 3 Oct 2026:* magazine and life events is next (D78); the order of directory and comms and Heritage stays Q-265. *Since 4 Oct 2026:* Heritage, then directory and comms (D86). |
| **D74** | How the 2027 print edition is produced is decided after the January 2027 Mid-Year. Whatever produces it carries no eligibility force (D32). | **The pipeline**: David and the committee, after the Mid-Year. |

---

## 3. The plate grammar (D68)

### 3.1 What the print edition does

- **One plate per family tree**, numbered *TREE n of N*, organised by clan, each
  plate rooted at one person whose forefathers run down a **trunk** to the
  founder; the plate grows **upward** from the trunk.
- **Node shape by sex**: men are ovals, women rounded rectangles. A node carries
  the **given name only**.
- **The root** is ringed twice in brown; a note under it reads *from t.N* when the
  plate continues another.
- **Line weight carries the patriline**: a limb is bold while the line from the
  root runs father to son; once it passes through a daughter, everything below is
  a hairline. A node's border matches the limb that feeds it.
- **Marks beside a name**: *» t.N*, this branch continues on tree N; *(+k)*, k
  descendants not drawn here but listed; *+* after a woman, she married within the
  family and her children are drawn on her husband's tree.
- **Spouses are not drawn**; they live in the plate's Family Details text.
- **A broken line** marks a family affiliated with a line rather than descended
  from it.
- **Plate furniture**: the clan path as a caption, a stats line (people,
  generations, branches continuing), a small key in a corner, a running header.
- **Palette and type**: white ground; green (about #1F7A4D) for rules and links;
  gold-brown (about #A0672A) for the root ring, figures and ornament; serif type
  throughout.

### 3.2 On screen

- **One renderer, `tree/plates.py`, producing SVG** from the current version; the
  same output is reusable for print if D74 chooses it, and nothing in this note
  depends on that choice.
- **Plates are computed, not stored**: a plate is a root, its descendants to the
  continuation cut and its trunk; continuations (*» t.N*) are chips that open the
  next plate in place, *from t.N* is a breadcrumb on the trunk.
- **Plate roots and numbers are the committee's**: the print edition's table of
  trees is imported as a committee-held list (root person, number, clan path),
  and renumbering is a committee act. How plates are cut where the committee has
  not numbered a line is not in the record (Q-269). *Design choice until then,
  labelled on the screen:* an unnumbered line opens as a plate rooted at the
  person the viewer opened, with no number shown; no number is invented.
- **Bold and hairline are computed per root** and recomputed on re-rooting.
- **Each limb carries its grade** as a small mark from the vocabulary the module
  already uses (answer 29: *documented*, *in the file only*). Whether the plate
  adopts a richer vocabulary is Q-267; until answered the plate uses the two
  words.
- **Tap a node** and a Family Details sheet opens: full name, identifiers,
  generation number, dates as §5 allows, parents, spouses, children, the grade
  and source of each link, attached items (§3.4 of the integration), and
  *Propose a change*.
- **Spouses** appear in the sheet and, in edit mode, as a chip on the node; they
  never enter the plate layout.
- **Pending and draft states** keep D20 and D21: dashed outline and badge,
  visible to every member, one bundle per sitting.
- **Phone**: the trunk pinned at the foot, the plate panned sideways, the key
  collapsible, search in place of the Name Index; 320px and 1280px are the test
  widths.
- **What the plate never shows**: whether a person is a member (D30, D36, P4);
  anything about the living to a signed-out visitor (D28); a relationship
  inferred across a step or adoptive link (R40, slice T1b).
- **Plate by default, hourglass available** (D77, 3 October 2026). The plate is
  the default view on every surface; the hourglass around a focus person stays
  available as an alternative view, chosen by the member, and its route is kept.
  The draft and pending mechanics move onto the plate; the "ancestors and spouse
  together" job is also in the Family Details sheet. The hourglass is drawn in
  the plate grammar, with the same shapes and line weights as the plate (D80,
  answering Q-279).
  *(This bullet read "The hourglass is retired as a view" until D77 answered
  Q-270.)*

---

## 4. The workflows

### 4.1 Contribute (D13, D70; workflow `tree-life-events` steps 1 to 3)

| Step | Who | Module | What happens |
|---|---|---|---|
| Open edit mode on a plate | Member in current national standing | `tree` | Drafts are drawn dashed on the plate. |
| Add a child, add a spouse, correct a name or a date, record a death, attach a source, flag a duplicate, propose a parent | Member | `tree` | Each is a typed proposal; a free-text "note about a person" is not a kind. |
| Submit the sitting | Member | `tree` | One bundle with its blast radius (D21). |
| Declare a life event | Member or household adult | `member` → `tree` | The existing pipeline (D31), R6 gate, D33 consent. |
| Track | Member | `member` | *Pending · needs information · accepted · declined*, each with the reason the committee gave. |

### 4.2 Review and decide (D14, D72)

| Step | Who | Module | What happens |
|---|---|---|---|
| Triage | Platform | `tree` | Own-household life events first; unsourced structural claims to the top for dismissal (D14). |
| Pre-review | Clan steward (a new role, `tree_steward`, scoped to a clan) | `tree` | Annotates and recommends: *recommend accept*, *recommend decline*, *needs information*. Cannot apply anything. |
| First key | Committee member (`tree:moderate`) | `tree` | Applies a non-structural item or an own-household life event. On a structural item, records the first approval. |
| Second key | A different committee member | `tree` | Applies a structural item. The same person cannot be both keys. |
| Needs information | Any committee member | `tree` | The question goes to the proposer; the item stays open and ages (T1c). |
| Merge duplicates; attach an orphan tree | Committee, two keys | `tree` | Structural by §6's proposed list; audited; D12 flags every decision that leaned on either record. |
| Fan out | Platform | `tree` → `member`, `magazine` | As built in T1b: offers, never fires. |

### 4.3 The parallel run and the cutover (D69)

| Step | Who | Module | What happens |
|---|---|---|---|
| Start the run | Committee, dated act | `tree` | Recorded on the module with its start date and planned end; the module's surfaces state which side is the record. |
| Import the record keeper's file | Committee (`tree:moderate`) | `tree` | The existing diff preview, now **against the Hub's current version**: additions and changes that touch nothing changed in the Hub since the last export apply as audited committee edits; anything changed on both sides since the last export is a **conflict**, listed with both readings and held for a decision. |
| Decide a conflict | Committee, keys by §6 | `tree` | Each conflict resolved as a proposal is. |
| Nightly backup | Platform | `tree` | A GEDCOM export written to private storage outside the repository under `tree:moderate`, each a dated row; a failed night is visible on the committee console. |
| End the run | Committee, dated act | `tree` | After it, an import of an external file is refused, naming D69. The export remains. |

This replaces P27's stage 4 (the handover after one clean annual cycle under
D11); P27's custody register (FT1) records the external file's status through
the run and after it.

### 4.4 Find yourself, at join and renewal (D73)

| Step | Who | Module | What happens |
|---|---|---|---|
| Join or renew | Applicant or member | `join`, `dues` | A step offers: *Find yourself on the family tree*. Skipping it is a complete answer. |
| Search | Applicant or member | `tree` | By own name or the oldest ancestor they can name. Candidates are shown; the platform never picks (D16, D30). |
| Propose the link | Applicant or member | `tree` | A link proposal enters the queue; the node stays unattached meanwhile, which is a complete state. |
| The 4.2.1 route | Applicant | `join` | Shown on the same screen as it is today (T1b). |

---

## 5. The people and what each may see

| Person | Sees | May do | Rules |
|---|---|---|---|
| Signed-out visitor | The deceased in full; the living as nothing | Nothing | D28 |
| Member, outside own branch | Deceased in full; living as name and position | Propose any change (D13) | D70, D71 |
| Member, inside own branch | Living in full, minors included as answer 22 has it | The same | D71, answer 22; Q-268 asks whether to revisit minors |
| Household adult | As a member | Declare life events for the household's minors | R6, D33, D35 |
| Clan steward | The clan's queue | Annotate and recommend | D72 |
| Committee member | Everything; the queue; the conflict list; the backups | Keys, imports, exports, merges | D69, D72, `tree:moderate` |
| Membership Committee | The evidence packet | Decide 4.1.1 | D16, D32 |
| Magazine editor | Accepted life events in the content window | As slice 7b | D33, 7b |

**Own branch** is computed from blood links only: a step or adoptive link never
widens it. Its radius is a common ancestor no further back than a
great-great-grandparent, which reaches third cousins (D71 as read by D76, 3 Oct
2026); a fourth cousin is outside it. A person related to the viewer only by marriage outside the radius is
outside it. The kinship engine's lowest-common-ancestor query (built) computes
it; the result is cached per viewer per tree version and invalidated on a new
version.

**R7 is unchanged.** The tree's payload is its own class (answer 22) and is not
a directory payload; the directory itself (§8) stays under the R7 walk.

---

## 6. The structural kinds (D81)

The list, set as the Rules Register's *Structural kinds* row by D81 (3 October
2026, answering Q-264); the Family Tree Committee may amend it by a dated act: a parent link added,
changed or removed; two records merged; a branch moved; a person removed or
marked removed; a clan assignment changed; a sex recorded differently (it
changes the plate's shape and the patriline); a link's grade raised. Everything
else is non-structural: a name spelling, a date, a place, a death date on a
person already recorded as deceased, a source attached, a spouse added without
children.

The Hub reads the list from the rules-register row and the two-key screens cite
D81. *(Until D81 this section was headed "proposed, unset until the committee
sets Q-264", the console labelled the list a proposal, and a DRAFT interim
behaviour, held from production until Q-264 was confirmed, applied it while
the row was unset.)*

---

## 7. Gates

1. **A production environment with backups (D69).** The Hub is not yet in
   service; staging's database has no backups and a fixed expiry. The real tree
   cannot become the record on staging. **The parallel run cannot start until a
   production database exists with backups, access limited to the committee for
   the raw file, and the nightly export landing outside the repository.** This
   joins `plan/MASTER-PLAN.md` §1d items 8 and 9 (staging lifecycle; Q-15 who
   maintains and pays).
2. **A second holder of `tree:moderate` (D72, D79).** The second holder is a
   Family Tree Committee member seated by the committee's own act (FT2), chosen
   over the project's lead (answer 31) (D79, 3 Oct 2026). Until that act and the grant on the Roles
   screen, a structural item records its first key and waits; the console names
   the gate and D79.
3. **Ownership and licence of the tree data (Q-201).** The record keeper's
   compilation and the original author's work are the source. Before the Hub
   becomes the record, the committee and the Board record on what terms the
   Federation holds it. The run's start is the committee's act and should cite
   that record. *Since 4 Oct 2026:* **D87** puts the licence and account in
   the Federation's name; the committee records the cadence and who may open
   the file, the Board records the terms by minute, and the gate clears when
   both are on file.

T2a to T2c and T2e can be built and run against the synthetic tree without any
of these; T2d's cutover cannot leave staging until gate 1 clears.

---

## 8. The integrations after D73 (T2f next, D78; then T2h and T2g, D86)

**Magazine and life events (T2f).** As built in 7 and 7b, reading the accepted
tree; the death approval gate (designed, not built) is built here.

**Directory and comms (T2g).** The directory shows a relationship only inside
the viewer's own branch and only along documented links ("your second cousin
through …"), never across a step or adoptive link; the R7 walk runs over the
whole payload as today. "Fill your branch" mailings as built (D36). A member may
start a referral (P4) from their own branch; the tree supplies nothing to it.

**Heritage (T2h).** Photographs, oral histories and Preservation items attach to
nodes, chiefly the deceased. The archive index that carries those links is
P27 §7.2 (its slice FT4 is folded into T2h); oral-history consent is P27 §6
(FT5, after T2h). **Where the item lives is Q-260**: D22 decided full media with
per-item consent; D66 made the shared drive the archive of record. A node may
carry a drive link today without either being decided; storing the file in the
Hub waits for the answer. *Since 4 Oct 2026:* **D88** answers for now: the
item is listed, its drive link goes to the holding committee's seats only, and
nothing is served to members or stored in the Hub.

---

## 9. The data

**Recorded.** Proposals with kind, author, sitting, sources, steward
recommendations and keys (who, when, which key); conflict rows with both
readings; the run's start and end acts; nightly export rows (date, size, hash,
who can reach it); plate numbering imported from the file.

**Never recorded.** The real GEDCOM in any repository, fixture or test (binding
rule 1, D15); a GEDCOM produced for any member-facing surface; a "not a member"
mark on a node; a free-text note about a living person outside a typed
proposal; anything the integration note forbids.

**Retention.** Proposals, decisions and conflicts are never deleted. Nightly
exports: how many are kept is not decided; until the committee sets it, every
night is kept (no export is deleted by the platform).

---

## 10. Money

None. The print run's costs have no approved budget; D74 leaves the pipeline
open and this note adds no payment door.

---

## 11. Refusals

| Where | The Hub refuses | Naming |
|---|---|---|
| Non-member tries to propose | The proposal | D70 |
| One person gives both keys | The second key | D72 |
| A steward tries to apply | The apply | D72 |
| A structural item with one holder of `tree:moderate` | The apply (records the first key) | D72, gate 2, D79 |
| An external import after the run ends | The import | D69 |
| An import while the run has not started on the production database | The cutover step | D69, gate 1 |
| Living details outside own branch | The fields (served as absent, not hidden) | D71 |
| Anything about the living, signed out | The fields | D28 |
| A relationship across a step or adoptive link | The label | R40 |
| A member-facing GEDCOM | The export | §4 of the integration note |
| A node marked as non-member | The rendering (no such field exists) | D30, D36 |

---

## 12. Journeys for the catalogue (to afrp-test)

Provisional ids carry this note's number; the workbench assigns catalogue ids.

| Provisional id | Journey | Class |
|---|---|---|
| P28-J01 | A member opens their own plate; trunk to the founder; bold and hairline right for a line through a daughter | meets |
| P28-J02 | A member views a living second cousin: dates shown | meets |
| P28-J03 | A member views a living fourth cousin: name and position only | refuses-correctly |
| P28-J19 | A member views a living third cousin: dates shown (D76; added 3 Oct 2026) | meets |
| P28-J04 | Signed out, the same plate: the living show nothing | refuses-correctly |
| P28-J05 | A step-parent's relative never appears in "own branch" | refuses-correctly |
| P28-J06 | A member drafts two changes and submits one bundle; status shows pending | meets |
| P28-J07 | A lapsed member tries to propose | refuses-correctly |
| P28-J08 | A steward recommends; cannot apply | refuses-correctly |
| P28-J09 | One committee member tries to give both keys on a merge | refuses-correctly |
| P28-J10 | Two committee members apply a merge; D12 flags decisions on both records | meets |
| P28-J11 | Parallel run: a non-conflicting external change applies as an audited committee edit | meets |
| P28-J12 | Parallel run: a change made on both sides is held as a conflict | meets |
| P28-J13 | After the run ends, an external import is refused naming D69 | refuses-correctly |
| P28-J14 | A nightly export row appears; a member-facing export does not exist | meets |
| P28-J15 | At join, a person finds a candidate, proposes, and is a member with an unattached node | meets |
| P28-J16 | At join, a person skips the step and nothing about membership changes | meets |
| P28-J17 | No plate, sheet or search result anywhere says whether a person is a member | refuses-correctly |
| P28-J18 | Phone width: the trunk stays pinned and continuation chips open in place | meets |

---

## 13. Out of scope

The print pipeline (D74). Any eligibility reading of the tree (D16, D32). Any
contact with a person in the file who is not a member (D36). Non-member
contributors (D70). Adoption's own decision (open, R40). 4.1.1's three spouse
questions. Arabic-script names (Q-266): the plate renders the names the file
carries.

---

## 14. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| T2-0 | The record: D68–D74 in the register (done 2 Oct 2026); P27, the Family Tree Design and Integration notes pointed at them; the D71 radius and the D72 tiers and structural list as rules-register rows; P28-J01 to J18 proposed to the catalogue | §2 | None |
| T2-R | The Hub's own record (README, the module map, orientation, open questions) says what is built today and what P28 changes, slice by slice; record only, no behaviour | §2, §3.2 | T1d |
| T2a | The plate renderer in the book's grammar, the default view, with the hourglass kept as an alternative view (D77) and drawn in the plate grammar (D80); grades on limbs; D71's own branch in the payload, out to third cousins (D76) | §3, §5, §11 | T2-R |
| T2b | Members propose: edit mode, typed kinds, the bundle, the status page | §4.1, §11 | T2a |
| T2c | Stewards and two keys: the steward role, the tiers, the structural kinds from the rules register (D81), merge and orphan tools | §4.2, §6, §11 | T2b; a second key in practice once the committee seats the member (D79) |
| T2e | Find yourself at join and renewal | §4.4 | T2a |
| T2d | The parallel run: dated start and end, import against the Hub's version with conflicts held, nightly export, the freeze | §4.3, §7 | Built and tested on staging with the synthetic tree; the run against real data on §7 gates 1 and 3 |
| T2f | Magazine and life events; the death approval gate | §8 | T2e (D78: the next integration after membership and join) |
| T2g | Directory and comms: relationships inside one's own branch | §8 | After T2h (D86, 4 Oct 2026) |
| T2h | Heritage: items attached to nodes through P27's archive index (FT4 folded in) | §8; P27 §7.2 | After T2f (D78), before T2g (D86, 4 Oct 2026); items listed and linked for the committee's seats only (D88, for now); Q-260 for the lasting answer |

Order: T1d → T2-R → T2a → T2b → T2c → T2e → T2d (when its gates clear) → T2f
(D78) → T2h → T2g (D86, 4 Oct 2026). Under D75 (3 Oct 2026) the
build-ready slices of `plan/MASTER-PLAN.md` §3.2 may be taken before T1d and the
T2 series. The print pipeline is not a slice until D74's
decision after the Mid-Year.

---

## 15. How this note sits with P27

P27 (`AFRP-Family-Tree-In-Practice.md`) was written the same day against D11's
staging, and is amended for D68 to D74. What it adds that this note lacks stays
there and is built from there:

- **The custody register (P27 §3, FT1).** Records the external file's licence,
  account, key-holders and status. Under D69 it shows the file as the source of
  the run's imports and, after the run, as read-only; Q-201 carried the
  ownership and licence that gate 3 needs, answered by D87 (4 Oct 2026).
- **The corrections door (P27 §4, FT2 in part).** The committee as a CW1 body
  with its seats, the public page and form pointing members in-platform, and
  nothing reading the form's sheet. The queue's tiers are T2c here; the import
  label for changes made outside the queue is T2d here.
- **Clan-book access (P27 §5, FT3).** Served by standing within D71: a book
  carrying living people's details is not served to a member unless it can
  withhold the living outside that member's own branch (Q-202, Q-260).
- **The volunteers' prototype and the archive index (P27 §7).** The index is
  T2h's substance (FT4 folded into T2h); whether a second site exists at all
  stays Q-190.
- **Oral-history consent as a written release (P27 §6, FT5).** Unchanged; it
  follows T2h.
- **The handover (P27 §8, FT6).** Superseded by D69's parallel run (§4.3);
  folded into T2d.

---

## 16. Questions raised

New: Q-262 the second holder of `tree:moderate` (a committee's quorum in
general stays Q-52) · Q-263 stewards: appointment, number, term · Q-264 the list
of structural kinds · Q-265 the order of the three remaining integrations ·
Q-266 Arabic-script names · Q-267 the grade vocabulary on plates · Q-268
whether relatives inside one's own branch see minors' dates (answer 22 says yes
today) · Q-269 how plates are cut where the committee has not numbered a line ·
Q-270 whether D68 replaces D19's hourglass default.

Merged into existing questions: the ownership and licence of the tree data is
added to Q-201; where node media lives (D22 against D66) is added to Q-260.

Answered by D68 to D74: Q-258 (D11's "one clean annual cycle") by D69; Q-259 (a
non-member asking for a change) by D70.

Answered on 3 October 2026: Q-262 by D79; Q-270 by D77; Q-272 by D76. Q-265 is
answered in part by D78 (T2f next), and in full on 4 October 2026 by D86 (T2h,
then T2g).

Raised 3 October 2026: Q-279 (the hourglass's drawing). Answered the same day: Q-279 by D80; Q-264 by D81.

---

## Sources

Decisions Register D11 to D22, D27, D28, D30 to D37, D53, D66, D68 to D74, D75 to D79;
`AFRP-Family-Tree-Design.md`; `AFRP-Family-Tree-Integration.md`;
`AFRP-Family-Tree-In-Practice.md` (P27); `AFRP-Family-Referral.md` (P4);
`AFRP-Shaheen-1982-Eligibility-Source.md`; `AFRP-R6-Minor-Authority.md`;
`plan/QUESTIONS-FOR-DAVID.md` answers 22, 23, 27 to 31; `plan/MASTER-PLAN.md`
T1a to T1d, 7, 7b, §1d; `site/data/workflows.yaml` `tree-life-events`; the
print edition's key page and cover (role-level, read 2 Oct 2026); the Family
Tree committee's September 2026 minutes as carried by the intake (role-level).
