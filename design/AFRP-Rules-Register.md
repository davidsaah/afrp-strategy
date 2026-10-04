# AFRP rules register — reconciled from source

**Compiled 5 September 2026.** This document exists because the dossier it
reconstructs is gone.

`afrp-mockups/docs/fixture/spec.py` opens by saying it matches *"the platform's
own rules dossier (**RULES.md**)"*, and the prototype cites rules by number from
**R1 to R43**. `RULES.md` is on no disk, in no git history of any of the six AFRP
repositories, and in no GitHub repository under this account. `gen.py` imports
`roster` from `/home/claude/tree` — a sandbox path — so the dossier was a working
file in an earlier session that was never committed. The rule numbers survive
only as citations.

**This register is those citations, gathered and graded.** It is not the dossier
and does not claim to be. Where a rule's wording here was inferred from the
sentence that cites it, the register says so, and the inference is marked.

**Since 2 October 2026:** the register also holds the family tree's parameter rows that D71 and D72 set. They are in "The family tree, set by decision", with a one-line pointer on each older row that D69–D72 now touch. Those rows are T2-0's record work in `AFRP-Family-Tree-Module.md` (P28) §14.

---

## Method, borrowed from the family's own

`AFRP-History/docs/METHOD.md` sets out how this family handles evidence, and this
register follows it rather than inventing a second standard:

> **The chart is a guide, not a source.** A chart cannot be its own evidence,
> least of all when the people printing it are the people who drew it.

The code is this project's chart. A rule that exists only because the code
implements it is **not attested** — it is the machine citing itself, which is the
same fault as the fabricated corroboration row found in red-team round 11.

> **TWO WITNESSES** means two genuinely independent texts carry the claim.
> **ONE TRADITION** means both carry it but are drinking from the same well.

Applied here:

| Grade | Meaning |
|---|---|
| **documents** | The rule restates operative by-law text held in `docs/bylaws/`. |
| **attested** | Cited in the design record (prototype, fixture spec, or a design doc) with its substance stated. |
| **one tradition** | Cited in more than one place, but every citation descends from the same lost `RULES.md` or the same handoff paraphrase. |
| **inferred** | Wording reconstructed by this register from the sentence that cites the number. **Not evidence.** |
| **no evidence** | The number is cited and nothing states what it says. |

> **Print uncertainty rather than smooth it.** Corrections appear at the same
> size as the claim they replace.

So the gaps below are set out at the same weight as the entries.

---

## The register

`Hub` records whether `davidsaah/AFRP-Hub` implements the rule, and whether it
**cites the rule number** — the code names only R7, R2 and (since 8 Sep 2026)
R6 by number, so most implementations are still unlabelled and would not
survive their author leaving.

### Identity, minors and the directory

| Rule | Statement | Grade | Hub |
|---|---|---|---|
| **R7** | Minors never appear in any directory payload. A person with no birth date on file is treated as a possible minor and excluded. *Since 2 Oct 2026:* unchanged by D71. Whether relatives inside one's own branch see a minor's dates on the tree is Q-268. | **attested** — stated in the prototype (*"R7 keeps a minor out of every directory, so the household browser shows a count and no names"*) and in the build handoff | ✅ `core/directory.py`, `core/payload.py`; **cited by number**, 18 times |
| **R4** | Household composition and club attachment. Cited jointly with R40 on the minor-in-two-households question. | **inferred** — 33 citations, none stating it | ◐ `core.Household` exists; **the two-household case is now half-modelled** — `authority.services.club_attachment` (slice 2b) holds every club the minor's households reach and flags the person OPEN rather than picking one, which is what §6 ratified. The rule that would *resolve* it is still with the Membership Committee under By-Law 4.3.1, so this stays deliberately unfinished. |
| **R6** | Guardian and delegation authority — who may act for a minor. **Stated in full:** `AFRP-R6-Minor-Authority.md` — four authority paths, seven enumerated powers, supervise designated / release consented, restrictions override, authority lapsing at eighteen, every exercise logged. | **attested** (8 Sep 2026) — the paths decided by David Saah; the power set, the supervise/release split, the restriction model and the two routed answers **ratified as drafted, without amendment**, by the Membership Committee, Camp Ramallah and the Legal Advisor, each on its own sections. Provenance in that document's table. | ✅ **`authority/` (slice 2b, 8 Sep 2026)** — `services.may(adult, minor, power)` is the one gate; `paths_for` resolves P1–P4, `can_transact_for` wraps the `transact` power, `standing_holders` bounds who may write a release list, `exercise` logs every use with its path. **Restrictions are checked before the paths**, so a new path cannot silently outrun them. `club_attachment` holds both and picks neither. R7 is untouched: no power reaches a directory payload, asserted in both the service and screen tests. |
| **R34** | A death is a life event with a family-approval gate; the deceased are withheld from the directory. *Since 2 Oct 2026:* a life event is proposed only by a member in current national standing (D70). One committee approval applies an own-household life event (D72). The family-approval gate for a death is slice T2f (P28 §8). | **attested** — stated in the prototype | ◐ `LivingGuardedModel` terminates the record; **no approval gate** — the platform never announces a death, and nothing in the Hub implements who approves |
| **R27** | Per-field visibility is a consent. The room and the archive both honour it; moderation logs never de-anonymise; **a retraction is a new entry, never an edit** (with S5). | **attested** | ◐ per-field audiences exist in `memberdir`; retraction-as-new-entry does not |

### Money and the multi-entity ledger

These five are the rules the Hub's `payments` and `funds` modules touch daily
**without citing any of them**. `AFRP-Multi-Entity-Ledger.md` in this directory
is their fuller statement.

| Rule | Statement | Grade | Hub |
|---|---|---|---|
| **R20** | The processing fee is booked as an AFRP expense; the gift or dues line **stays gross**. | **attested** | ✅ `ChargeRecord.fee_cents` (NULL until reported); `ledger/posting.build_revenue_batch` books the fee as an expense and revenue gross; a charge with no fee reported refuses the close |
| **R21** | Club dues collected nationally are held as a **liability to the club** until the monthly remittance. | **attested** | ✅ `ledger/remittance.build_collection_batch` credits Due to local clubs on collection; the run is a statement until approval, which is refused while §7.1 and §8.7 are open |
| **R22** | The daily close is an **idempotent batch key**. | **attested** | ✅ `ledger.JournalBatch` unique on (period_date, fund, kind) and on doc_number; `DailyClose` unique per day; a second close refused |
| **R23** | Event money routes by the event's **HOST** field; the class code is attribution only. | **attested** | ◐ `events` has a club; host-vs-attribution is not separated |
| **R24** | A reversal is **its own journal entry** and never edits the original (with S3). | **attested** | ✅ `payments._reverse` — reversals are new rows; the original stands; `ledger` posts each as its own batch on the day it was reversed |
| **R25** | Restricted classes post gross, reverse via receivables, report per entity (with S3). | **attested** | ◐ `funds` reverses; no receivable |
| **R26** | A banquet seat is **inventory, not a donation**. | **attested** | ❌ not modelled |
| **R38** | Programme attribution: costs ride the hosting programme's budget line. | **attested** | ❌ no budget lines |
| **R43** | A capacity or roll figure is **frozen at adoption and never recomputed** — no mid-cycle clawback. | **attested** (with R12) | ✅ in `voting` (frozen rolls); ❌ in `funds` capacity |

### Governance, franchise and reporting

| Rule | Statement | Grade | Hub |
|---|---|---|---|
| **R40** | **Where the by-laws are silent or admit two readings, flag the question OPEN, route it to the named committee, and never decide it silently.** | **attested** — 47 citations, the most-cited rule in the design record; every open question in the fixture carries it or its shape | ✅ **the module's whole design** — `bylaws.eligibility.assess` returns UNDETERMINED and names the committee. **Not cited by number anywhere in the Hub.** |
| **R12** | The certified roll is a **snapshot**, frozen on a date, never recomputed (with R43). | **attested** | ✅ `voting` freezes the roll and the weights |
| **R14** | A one-time receipt belongs to the **electronic** flow; mailed-ballot status is inclusion status, not a receipt. | **attested** | ◐ electronic receipts exist; the mailed CPA ballot is not built |
| **R16** | During a club migration only the migrating club's membership is touched; the other membership and the club-of-record pointer move **only if the member acts** (with R2). | **attested** | ❌ no migration module |
| **R39** | Exact grants — five sensitive permissions at their strictest. **Federation scope does not read into the ARFHSN store.** | **attested** | ✅ `access/policy.py` (policy.ts ported verbatim), `access/services.requires` on every federation view; `access/tests.py` locks the reach matrix and exact-scope sensitivity. The staff flag now opens only the Django admin |
| **R2** | Cited with R16 on migration; the Hub uses "R2" for a different rule (no real living person in fixtures). | ⚠ **collision** — see below | ✅ under the Hub's own meaning |

### The family tree, set by decision (2 October 2026)

These rows are not reconstructions. Their source is the Decisions Register itself, so their grade is **decided**, a grade outside the reconstruction's scale above. Each value is changed only by a dated act under a citation, never by an edit to this table.

| Row | Statement | Set by | Value | Hub |
|---|---|---|---|---|
| **Tree radius** | A signed-in member sees the living in full inside their own branch: blood relatives sharing an ancestor no further back than the radius, and the spouses of those relatives. Outside it, a living person shows a name and a position on the plate only. Own branch runs along blood links only; a step or adoptive link never widens it. D28 is unchanged: signed out, nothing about the living. | **D71** (amends D17 and answer 22 of `plan/QUESTIONS-FOR-DAVID.md`); read by **D76** | **Great-great-grandparent.** A change is a dated act of the Board or the Family Tree Committee under a citation (P28 §2). The radius reaches third cousins. D71's parenthesis ("out to second cousins") disagreed with this value; *since 3 Oct 2026* D76 reads it as an error and the great-great-grandparent stays (Q-272 answered). | ❌ not built; slice T2a puts the branch in the payload (P28 §5, §11) |
| **Tree approval tiers** | One committee approval (`tree:moderate`) applies an own-household life event or a non-structural correction. Two approvals from **different** committee members apply a structural change. Clan stewards, appointed by the committee, pre-review and recommend for their clan and never approve. Every life event still queues (D14, D31). | **D72** (amends D14's mitigations); **D79** for the second key-holder | One key, or two different keys. A structural item with one key records it and waits. The second holder of `tree:moderate` is a Family Tree Committee member seated by the committee's own act (FT2), chosen over the project's lead (answer 31) (D79, 3 Oct 2026). Steward appointment, number and term are Q-263. A committee's quorum in general is Q-52. | ❌ not built; slice T2c (P28 §4.2) |
| **Structural kinds** | The list of change kinds that need two keys under D72. | **D72**; set by **D81**; the Family Tree Committee may amend it by a dated act | **Set by D81 (3 Oct 2026; Q-264).** A parent link added, changed or removed; two records merged; a branch moved; a person removed or marked removed; a clan assignment changed; a sex recorded differently; a link's grade raised. Every other change is non-structural (P28 §6). *(Until D81 this row read "Unset (Q-264)", with P28 §6's list shown as a proposal.)* | ❌ not built; slice T2c |

**Pointers from D69 and D70, which set no parameter of their own here.**
- D69 makes the Hub the record of the tree after a parallel run of 30 to 60 days. The run's start, length and end are the committee's dated acts, and nightly exports run under `tree:moderate` (P28 §4.3; slice T2d). Changes in the run are audited committee edits, with conflicts held and never merged, which is R24's and R27's never-edit-the-original shape applied to the tree.
- D70 bounds who may propose: members in current national standing. No account exists for non-members to contribute, so Q-259 is answered for the platform. Standing is read with `standingAt` per scope (4.3.1).

### Numbers that are cited but say nothing

**R1, R3** — every apparent citation is a false positive: they are reviewer
columns (`R1 R2 R3`) in the scholarship median table and a retry suffix in a
QuickBooks batch key. **No evidence** that R1 or R3 exist as rules.

---

## Two collisions, printed rather than resolved

**R2 means two different things.** The prototype cites R2 with R16 on club
migration. The Hub's `ai-memory/01-BINDING-RULES.md` numbers its own rules R1–R9
independently — its R2 is *"scholarship applicant data never enters this repo."*
**The Hub's numbering is a parallel invention, not the dossier's**, and I created
it. Two documents now use `R2`, `R4`, `R6` and `R7` for different rules, and only
R7 means the same thing in both by luck.

That needs a decision rather than a patch. The options are to renumber the Hub's
nine to a distinct prefix, or to adopt the dossier's numbering and drop the
parallel set. **Neither is mine to choose.**

**S-numbers are stable.** S1, S3, S5 and S7 are cited consistently across the
prototype, the design record and the Hub, and mean the same thing in all three.
They came from red-team rounds 1–2 and were written down at the time.

---

## The six open questions, verbatim from the fixture

These live in `openQuestionCatalog` in `afrp-fixture.json` — the only place in
the entire record where questions, their by-law, and their routing are held as
structured data rather than prose. **All six are about who counts as family.**
Two were answered and ratified on 8 September 2026; four are still open, and the
platform models none of the six.

| Question | By-law / rule | Routes to |
|---|---|---|
| By-Law 4.1.1 admits a person "married to one having such origin". The text is gender-neutral and names no restriction. **Does a same-sex spouse qualify?** | 4.1.1 | Membership Committee |
| Where two parents of the same sex raise a child, the GEDCOM pedigree qualifiers (`_FREL`/`_MREL`) assume a father slot and a mother slot. **Which slot carries which parent, and does the child inherit descent through either?** | 4.1.1 / tree | Family Tree Committee + Membership Committee |
| 4.1.1 says "married to". **A long-term unmarried partner is not married to.** Is the Associate route (4.2.1, "special circumstances") the intended home? | 4.1.1 | Membership Committee → Board |
| A member admitted under "married to one having such origin" **divorces that spouse.** The by-laws are silent on whether the membership survives the marriage. | 4.1.1 | Membership Committee |
| After a remarriage **a minor belongs to two households** with different clubs, different directory choices and different pickup authority. By-Law 4.3.1 says nothing about minors in two households. **Provisional answer 8 Sep** (`AFRP-R6-Minor-Authority.md` §6): authority is per person, not per household; pickup runs through the release list; directory choices resolve to the more protective; **club attachment stays OPEN** to the Membership Committee. | 4.3.1 (silent) / R4, R40 | Membership Committee + Camp Ramallah |
| Camp pickup authority reads the household and delegation model. **A court-appointed guardian is neither parent nor delegate.** **Provisional answer 8 Sep** (§6): the court-appointed guardian is path P2, established by the appointing order rather than by the household — a recording procedure, not a new rule. | R40 / R6 | Camp Ramallah + Legal Advisor |

**Four of the six are unanswered; two were answered and ratified on 8 September
2026**, in `AFRP-R6-Minor-Authority.md`, by the committees named beside them.
Note what the second answer contains: the pickup and directory halves are settled
rules, and the **club attachment half is ratified as staying OPEN** — the
Membership Committee decided that the platform holds both attachments and keeps
asking rather than picking one. A question can be answered by a decision to leave
it open, and that is not the same as an unanswered question.

The four that remain are unanswered in the plain sense, and the Hub models none
of their cases. That is correct
under R40 — but the Hub also does not *ask* them, and a question nobody is shown
is not the same as a question left open. The register is where they become
visible; `bylaws.services.ratification_agenda` is where they would become an
agenda.

---

## What is still missing, and where I looked

Following `AFRP-History/docs/METHOD.md` §4 — *a negative check names the edition
searched and admits that silence is weak evidence.*

**`RULES.md` — searched 5 September 2026, not found.** Searched: every file on
`C:\Users\David\Projects` including all clones; `git log --all --diff-filter=A`
across AFRP-Hub, AFRP-Portal, afrp-mockups and AFRP-History; and
`gh repo list davidsaah` in full (ten repositories). The `afrp-mockups` README
names a companion repository **`afrp-platform`** which does not exist under this
account — it is the most likely former home of the dossier, and may have been
renamed to AFRP-Portal or never pushed.

**What would settle it:** the file itself, or the Claude Project that held it. If
`RULES.md` is recovered, **this register is superseded and should be deleted, not
merged** — a reconstruction has no standing beside its source.

**Five design documents named by the build handoff remain unlocated** *(since 2 Oct 2026: all five are now in this repository's `design/` directory)*:
`AFRP-Family-Tree-Design.md`, `AFRP-Decisions-Register.md`,
`AFRP-Camp-Directory-Network-Plan.md`, `AFRP-Test-Fixture-500.md`,
`AFRP-Program-Experience-Architecture.md`. Two of them are now partly recoverable
from other sources: the fixture's spec is `afrp-mockups/docs/fixture/spec.py`
(266 lines, with the seed, the four clubs and their Shaheen-1982 sizes), and the
family tree has substantial material in `AFRP-History` and `AFRP-FTB` — neither
of which is the design document, and both of which are described below.

---

## The family tree, on the evidence

Recorded here because two sessions have now called it "blocked" while material
sat unexamined. It is not blocked for want of data. It is blocked for want of a
**design** that says how the tree becomes the platform's identity substrate.

*Since 2 October 2026:* the design is D68–D74 and P28 (`AFRP-Family-Tree-Module.md`), with P27 for the migration from practice. D68 carries the grade on every limb of the plate (P28 §3.2), which is the point the first bullet below makes. The rows this register holds for it are in "The family tree, set by decision" above.

**`AFRP-History` (public, on disk)** — *The One Line*, by David Saah and John
Mogannam. A book built deterministically from sources: sixty-six generations from
Adam to Rāshid al-Ḥaddādīn and about eighteen more to the present, eighty-four in
all. Its method is the strongest evidence discipline anywhere in this project.

Three things in it bear directly on the platform:

- **Every entry carries a grade** — `scripture · classical · attested ·
  documents · oral tradition · no evidence` — and a **TWO WITNESSES** or **ONE
  TRADITION** badge. An identity substrate that stores relationships without
  storing their grade throws away the part the family actually argues about.
- **حديد or حداد** — *iron* or *blacksmith*, one letter apart, "in an Ottoman
  clerk's hand barely distinguishable." The book prints it as a lead **with the
  trap named beside it**. This is the same defect class as `NEAR_HOMOGRAPHS` in
  `bylaws/eligibility.py`, where Shqair sits one letter from Shukair and
  Shakara is a different clan from Sharaka. The family's own scholarship reached
  that conclusion independently, and it is why fuzzy matching must never be
  reintroduced.
- **Negative results are published so nobody runs them twice** — the Ḥaram
  al-Sharīf corpus, searched in full on 21 August 2026, result recorded.

**`AFRP-FTB` (private)** — a Vite/React GEDCOM **chart builder**: a parser, a d3
force layout, page tabs, SVG export. Its `DescendantViewMode` is
`'Patrilineal' | 'Daughters' | 'FullBloodline'`, which is the same distinction
red-team round 8 found violated when step-parents were walked as blood ancestors
across 12.3% of the file.

It is a drawing tool, and `METHOD.md` is explicit that **the chart is a guide,
not a source.** Building the platform's identity substrate from it would repeat
precisely the error the book was rewritten to correct.

---

## What this register does not do

It does not decide the R-number collision, it does not answer any of the six
questions, and it does not stand in for `RULES.md`. It makes the citations
legible and says, for each one, how much weight it can carry — which is the
least this project's own standard permits, and the most this evidence supports.
