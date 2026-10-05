# Platform primitives

### The shapes every design note draws, built once: refusals, acts, parameters and authority, seats, consent, cycles, statements, sending, records on file, work items and snapshots

**Design note P29 · 4 October 2026 · for the Hub's `core`, `rules`, `access`, `clubs`, `programs`, `scholarship`, `camp`, `comms`, `ledger` and `funds` modules, and every slice that follows**

**Why now.** On 4 October 2026 David approved the review of everything designed to date (D99). The review found that P1 to P28 design about twelve shapes again and again, each in its own words, and that the Hub has already built several of them more than once. This note names each shape once, says what it holds and what it refuses, lists the notes that draw it and the Hub code it replaces, and names the slice that builds it. It adds no rule to any note: where a note's rule and this shape differ, the note governs its own programme and this note says where the difference is real.

**What it rests on.** The design notes P1 to P28 as they stand on 4 October 2026; the Decisions Register to D99; the Hub's binding rules (`AFRP-Hub/ai-memory/01-BINDING-RULES.md`), which this note never relaxes; the review itself (`AFRP-Hub/ai-memory/cowork/review/2026-10-04-simplify-abstract-expand.md`), which carries the file-by-file evidence.

**Labels.** *The record* means a note or decision says it; *design choice* means this note chooses a shape the record leaves open, so a later decision can change it without contradicting any rule.

---

## 1. The refusal

**What it is.** One exception type for every refusal the platform makes, carrying what binding rule 9 requires: the rule it applies (a by-law, a decision, a register row, a design-note section), the missing parameter if the refusal is "not set", who sets it, and the open question if one holds it. A view turns it into a message by one helper; nothing writes a refusal message by hand.

**Fields.** `kind` (rule, missing parameter, missing document, open question); `citation`; `parameter_key`; `setter` (a seat or body, never a person); `question` (a Q-number); `message` (generated from the others, never typed).

**Replaces.** About 26 per-app `*Refused` exceptions with free-text messages and 68 hand-written catches in views. `rules.RulesRefused` is already this shape and is the model.

**Used by.** Every note's "refuses, naming…" lines; every slice. Binding rule 9 becomes checkable: a test can assert a refusal names a real Q-number or parameter key.

**Built in.** A2, with the snapshot (§12): A1 deferred both ("concept D", the refusal as a value) to a slice A2 the plan never carried.

## 2. The act and the append-only record

**What it is.** Who did what, on whose authority, when. One rule for recording an actor (a link to the person and a text field for the authority they acted on), one dated act, and one base for records that are never deleted, whose queryset refuses deletion as well as the instance.

**Fields.** `by_person`; `on_authority` (a seat, a grant, a minute); `at`; `kind`; `note`; for an append-only model, `never_deleted_because` and an explicit reset used only by the fixture seeder.

**Rules.** An audit or reason field is never cut to fit: a value too long for its field refuses (the 9 September break-glass record lost its citation to truncation). A correction is a new row naming the old one.

**Replaces.** Twelve `_who` helpers in three variants; actors stored sometimes as text and sometimes as a person link; about 33 per-model delete overrides that a queryset delete bypasses; about 164 audit strings still cut to fit.

**Built in.** PR0.

## 3. The scoped parameter and the authority row

**What it is.** The rules register's parameter, extended: a value that may be set for one scope (an entity, a fund, a programme, a cycle, a template) and graded by where it comes from. An **authority row** is a parameter whose value is a set of seats and how many must act, answering "who may do this act for this scope".

**Fields.** `key`; `scope`; `value` (null means not set; never deleted); `grade` (by-law, minute, practice, template, proposal, design); `authority_citation`; `effective_on`; `owner_seat` (who sets it); `question` (the Q-number while unset). An authority row's value: `seats`, `count_required`, `countersign_rule`.

**Rules (the record).** A null value refuses, naming the parameter, its owner and its question (binding rule 9; the "silence stays silence" rule of every note). A value is never typed into code: rates, caps, periods and days live here.

**One vocabulary (design choice).** The notes grade parameters five ways (P15 §3, P26 §2.1, P13 §2 and §7, P11 and P23, the Rules Register's method). This note takes one list: by-law, minute, practice, template, proposal, design, and null for silent.

**Used by.** P9 (valuation date, waiver authority, a fund's entity), P11 (signatories, ceiling), P13 (template terms), P15 (retention periods), P22 (settlement approvers, stop authority), P23 (authorisers per path), P26 (instalments), P3 (signatory seats, renewal sequence), P6 and P14 (approver seats, Q-80), P1 (quorum, Q-52).

**Replaces.** Hard-coded constants in `camp/services.py`, `network/models.py`, `network/services.py` and `reporting/services.py`; `dues.DuesSchedule`'s own copy of the parameter shape; the named-award rate set in a view.

**Built in.** PR0.

## 4. The dated role, and the body and seat

**What it is.** A person holding a role in a scope for a period: (person, kind, scope, started, ended, the act that started it, state). Three kinds extend it. A **seat** on a body adds authority, term and vote (P1 §2.2). A **contact role** adds its consent and retention (P21 §3.2). An **assignment** adds a slot (P7).

**Bodies and seats.** CW1's body register is the anchor for every "seat, never a person" in the record: signatories (P3), approvers (P6, P14), the verifying seat (P26), the correspondent (P24), the second holder of `tree:moderate` (D79), the Executive Director's grants (P16). Grants are derived from seats; a seat ended ends its grants.

**Replaces.** `clubs.OfficerRole`, `programs.CommitteeSeat` and `scholarship.Seat`, each saying "the roster is the grant", beside `access.Grant`; seven separate "active on this date" implementations.

**Built in.** The base in PR0; bodies and seats in CW1, which takes the three seat tables over as it lands (the migration of each is part of CW1's exit).

## 5. Consent and the consent key register

**What it is.** A consent row that says whose consent, for what purpose, in what scope, through which channel, for which item, under which wording, given or withdrawn; and one register of the purposes a consent can name.

**Fields.** `subject`; `purpose_key` (from the register); `scope`; `role` (P21: a consent given under one role is never read by another); `channel`; `item_ref` (P27: a recording or a photograph); `wording_version`; `granted`; `restrictions` (not before, withheld passages); `held_by` (the subject, or the household adult for a minor under binding rule 7); `source`. Withdrawal is a new row.

**The key register.** Each key: purpose, message class, who holds it for a minor, whether it is re-asked at eighteen. Today the keys are bare strings (`"directory.display"` 54 times, `"comms.email"` 39 times).

**One reading of "latest".** One function returns the latest row with a stable tiebreak (the defect `core/tests_consent_order.py` locks). Six copies exist today, one without the tiebreak.

**Used by.** P7, P12, P21, P22, P24, P27; D22, D33, D89, D93, D94. P7's double gate (an interest row *and* a programme-invitation consent) becomes one consent with a scope (*design choice*).

**Built in.** CR1, which already designs consent per role and channel.

## 6. The cycle

**What it is.** A programme's recurring call: a cycle with a window, places and a deciding body; applications to it; a decision. One engine for every programme that takes applications.

**Fields.** Cycle: `programme`, `entity`, `deciding_body`, `opens`, `closes`, `places`, eligibility rows (scoped parameters), `form_version`, `retention_key`, `state`. Application: `applicant` (a person or a contact role), `arrival_path`, `answers`, `document_policy`, `consent`, `state`. The decision is a decision item of the deciding body (P1 §3.4).

**What differs, and is real.** Membership required or not (P5 under 8.1.2; P12 with D60's contacts). Lateness: P5 refuses by 9.3.4(3); P12 and P26 refuse nothing until Q-117. Documents, three ways: a drive link only (P5), uploaded under the retention clock (P12 under D94), never held (P26, binding rule 2). These are the cycle's settings, not separate engines.

**What differs, and is not.** The state lists (ranked and slated, offered and lapsed, selected and waitlisted) are one superset with per-programme labels.

**Used by.** P5, P8, P12, P14, P17, P25 (the Senior Award), P26; SEL1–SEL3 with SC1–SC3; AR1's terms; the Day of Action.

**Replaces, later.** `camp` Season and Application, `scholarship` Cycle and Application, `programs` Invitation and Enrollment move onto it once it is proven (CY2).

**Built in.** CY1, before SC1.

## 7. The statement run

**What it is.** Lines for an account set and a period, each with its evidence; a query that holds one line while the rest settle; approval through an authority row; an immutable close; a correction as a new line naming the old.

**States.** Draft, confirmed or queried, approved, settled, closed.

**Used by.** P18 §5 (the club statement, D57), P13 §4 (settlement), P23 §6 (the Relief Fund), P11 §5 and P1 §4.4 (the ARFHSN report), P9 §4 (the annual run), P24 §5–6 (the subscriber ledger). Only P18 and P13 state the query hold; this note makes it the base (*design choice*).

**Expansion.** Year-end giving statements per receiving entity are statement runs (D99). The deductibility wording waits on the CPA (D9), so the statement refuses that line by name until it is given.

**Built in.** C3 (the club statement) as the first user.

## 8. Sending and the letter row

**What it is.** One `send(template, audience, class)` that resolves the audience, applies consent, death and merge checks, and writes one letter row per person, so every letter the Federation sends is on the record with its template version.

**Replaces.** `clubs.OperationalNotice`, `clubs.ClubMailing`, `comms.FederationMailing` and `tree.TreeMailing`, all one shape; sending done inside views.

**Used by.** P3 (the template register), P6, P14; LT1–LT3, AR2's class welcome, SC1's calls, every follow-up. Sends switch on with slice 5a (email).

**Built in.** LT1 builds the register and the send; CM1 moves the four mailing tables onto it.

## 9. On file

**What it is.** The platform holds *that* a document exists, never *what* it says: kind, date, the seat that recorded it, a drive link, an expiry.

**Fields.** `subject`; `kind`; `as_of`; `expires_on`; `recorded_by_seat`; `drive_ref` (a typed drive reference, D66); `state`.

**Used by.** P7 §5 (screening), P12 §2.2 (each document kind), P13 §2.8, P22 §3.2 (evidence required), P26 §2.2 (verification), P27 §6.2 (a release on file); D61, D94; binding rule 2.

**Built in.** PR0 (the shape); each slice that records a document uses it.

## 10. The work item

**What it is.** Something waiting for a decider: owned, dated, resolved by an act, never deleted.

**Used by.** P21 §7 (the match queue), P24 §3 (assisted submissions, the death hold), P27 §4 (corrections), P28 §4 (proposals in tiers), P6 (statements), P14 (positions), P3 (wording adoption); C2's secretary queue.

**Replaces.** `clubs.FollowUp`, the tree change-request queue, the identity merge queue, each its own table.

**Built in.** C2, as its first user.

## 11. The clock

**What it is.** A deadline that starts from an event, reads its period from a parameter, belongs to a seat, and on firing raises a work item or changes a state. A clock whose parameter is not set never fires and shows "not set".

**Used by.** P1 §2.2 (90-day seat expiry), P6 §2 (24 hours), P11 §3.2 (renewal reminder), P13 §4 (release and accounting), P15 §2.2 (incidents), P21 §9 (retention), P26 §2.4 (filing window).

**Built in.** PR0 (the shape); fired by the scheduler the Hub already runs.

## 12. The snapshot

**What it is.** A frozen, dated view of a set of records taken at one moment, from which a roll, a slate, a packet or an opening list is produced, so a later change to the live records never changes what was taken.

**Used by.** SC4 (the certified roll), MG2 (the frozen opening list), CW3 and CW4 (the report and the packet), SV2, C5 (the annual snapshot), HA4 and CV6 (settlement).

**Built in.** A2, before SC4.

---

## 13. The order (D99)

1. **R3**, the Hub's record catch-up (with T2-R, T1d and T1e): the stale process text, the boot pack, the README.
2. **PT1**, process tooling: `close_slice`, the findings file, journey stubs generated from the notes.
3. **A2**: the refusal (§1) and the snapshot (§12).
4. **PR0**: the act and append-only record (§2), the scoped parameter and authority row (§3), the dated-role base (§4), on file (§9), the clock (§11).
5. Then D75's order as D96 set it, with the shared pieces taken up by their first users: CW1 (bodies and seats), C2 (the work item), LT1 (sending), CR1 with AR2 (consent), CY1 before SC1 (the cycle), C3 (the statement run).
6. Slice 5a (email) as soon as David supplies the provider; 5b (payments) after.

## 14. What this note does not do

- It changes no binding rule and no decision. Where a programme's note sets a rule, the primitive carries it as a setting.
- It does not migrate built code by itself: each replacement named above happens in the slice that builds the primitive, with that slice's tests, red-team and audit.
- It does not answer any open question. A shape whose value is unset refuses by §1 and §3.

## 15. Journeys

| Id | Journey | Primitive |
|---|---|---|
| P29-J01 | Every refusal on every surface names a rule, a parameter or a Q-number that exists | §1 |
| P29-J02 | A queryset delete on an append-only model refuses; the fixture reset is the only way round | §2 |
| P29-J03 | A reason too long for its field refuses rather than being cut | §2 |
| P29-J04 | A parameter set for one fund does not apply to another; an unset one refuses naming its owner and question | §3 |
| P29-J05 | Ending a seat ends the grants derived from it the same day | §4 |
| P29-J06 | A consent given under one role is not read by another | §5 |
| P29-J07 | Two programmes run cycles with different document policies on the one engine | §6 |
| P29-J08 | A queried statement line holds; the rest settles; the close is immutable | §7 |
| P29-J09 | A send writes one letter row per person and skips the dead and the merged | §8 |
| P29-J10 | A roll taken from a snapshot does not change when a member lapses afterwards | §12 |
