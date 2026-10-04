# AFRP Scholarship Program
### Addendum 7 — applications, committee, awards, and disbursement

**Date:** August 15, 2026
**Status:** implemented, 41 tests, end-to-end cycle runs

> Superseded on payer and Board approval by D3, ARFECF 6.4.4 and P26 §1.4 (`AFRP-Scholarship-Awards.md`).
>
> *Since 2 October 2026:* four passages below are kept as written and are overtaken, each with a dated pointer: §1 and §5 ("AFRP is the payer of record") by **D3** (20 August 2026: the Scholarship is ARFECF's); §3's three-degree block by **David's correction of 8 September 2026, recorded in P26 §1.4 and §3.2 (built in slice 4b)** (disclosed by degree and acknowledged, only the same household refuses; recorded as **D84** on 4 October 2026, pending the Scholarship Fund Committee's adoption); §2's "board approval" by ARFECF 6.4.4 (the committee's decision authorises; Q-161); §5.1's yearly verification by the 2026 award letter's per-semester practice (P26 §2; Q-159). Awards, instalments, renewal, letters and named scholarships are designed in **P26** (SA1–SA7).

---

## 1. Your four answers, and what each one costs

| Decision | Consequence |
|---|---|
| **Paid to the student** after enrolment proof | Flexible for the student. Makes AFRP the payer of record — tax status, qualified/taxable split and non-resident withholding all become AFRP's to capture. See §5. *Since 20 August 2026 (D3): the payer is ARFECF, and the tax-fact capture applies to ARFECF (P26 §1.4, §2.3); which account pays in practice is Q-158* |
| **Multi-year with annual continuation review** | Right for scholars. Commits money AFRP has not raised, so future years must be **encumbered**. See §4 — this is the one that quietly breaks programs |
| **Open to any Ramallah descendant**; free membership onboards | Widest reach, and it turns the scholarship into recruitment. Descent is verified **against the family tree** — the first time that archive does operational work |
| **Both endowed and annual** named scholarships | Each carries its own funding, criteria and capacity. Matching scholars to them is a real assignment problem. See §6 |

---

## 2. Lifecycle

```
form → application → review (recusal) → rank → match to named awards
     → budget check → board approval → offer → accept
       (since 2 Oct 2026: under ARFECF 6.4.4 the committee's decision authorises;
        a Board act is recorded beside it and gates nothing — P26 §3.3, Q-161)
     → [each year] verify → authorise → disburse → continuation review
     → graduation
```

Every step is a state on a record, so a partially-complete past can be loaded
without inventing the missing steps.

---

## 3. Committee — the conflict problem is the real one

AFRP is a federation of families descended from one ancestor. A committee
member being related to an applicant is **normal, not scandalous.** Scoring
your own niece without saying so is the problem.

So conflicts are **detected, not merely declared**:

| Source | Effect |
|---|---|
| Reviewer is the applicant | Blocked |
| Same household | Blocked |
| Related within 3 degrees in the family tree | Blocked. *Since 8 September 2026 (David's correction, recorded in P26 §1.4 and §3.2; built in slice 4b; D84, 4 Oct 2026, pending the committee's adoption):* disclosed by degree and acknowledged, not blocked; only the same household refuses (P26 §1.4) |
| Related beyond 3 degrees | **Disclosed on the record, not blocked** |
| Self-declared | Always honoured, never questioned |

Three degrees covers parent/child, sibling, grandparent, aunt/uncle, and first
cousin. Beyond that it is disclosed only — **a 6-degree bar in this community
would leave no committee at all.**

The family tree earns its keep here. It is the only system that knows a
reviewer is an applicant's second cousin, and that is precisely the
relationship self-declaration misses: near enough to matter, far enough to feel
deniable.

**A recusal is not an empty review.** They are separate states with separate
counts, so "did not score" and "could not score" stay distinguishable forever.
An audit of a contested award turns on that difference.

### 3.1 Scoring

Weighted rubric to 100 (academic 30, need 30, community 20, essay 20 —
illustrative; the committee sets the real one). Ranking uses the **median**, not
the mean, so one harsh or generous reviewer cannot move an outcome.

**Spread is surfaced, not smoothed.** Two reviewers 80 points apart on the same
application is a signal the rubric was read differently — averaging it hides
exactly the case the committee should discuss. Ties are left tied and flagged;
breaking them is the committee's job.

Seats require a member in good standing, re-checked rather than assumed —
standing lapses quietly, and someone who forgot to renew should not keep voting
on awards. A lapsed seat is **suspended, not deleted**, so history survives and
reinstatement is one row.

---

## 4. Budget and encumbrance — the thing that breaks programs

A four-year award made in 2026 commits money in 2027, 2028 and 2029.

**If the committee counts only this year's new awards against this year's
budget, it will over-commit — and the failure appears two years later as a
scholar whose funding evaporates mid-degree.** That is the worst outcome this
program can produce, and it is arithmetic, not fundraising.

From the working engine:

```
CYCLE BUDGET 2026-27
  budget                        60,000.00
  encumbered (continuing)       16,000.00   ← committed before the committee met
  committed (new awards)        29,000.00
  AVAILABLE                     15,000.00

FORWARD COMMITMENTS
  2026-27  committed 45,000  budget 60,000  headroom 15,000
  2027-28  committed  5,000  budget 60,000  headroom 55,000
  2028-29  committed  5,000  budget 45,000  headroom 40,000
```

`AVAILABLE` is the only number the committee should be shown. Two behaviours
worth knowing:

- **A forfeited year releases its encumbrance.** A scholar who withdraws frees
  money to re-award. Not returning it under-awards every year after the first.
- **The system warns when continuing awards exceed 80% of a budget** — solvent,
  but with almost no room for new scholars, which is a governance problem
  before it is a financial one.

### 4.1 Endowed scholarships

Corpus untouchable; awards come from a spending rate on a **trailing average**
market value — the standard smoothing that stops awards lurching with the
market. A rate above 10% is rejected: that is not a spending policy, it is
spending the corpus.

The engine says plainly when a named endowment cannot fund its own award:

```
Haddad Memorial (Medicine)   endowed   spendable 11,250.00   2/2 awards
Zarou Engineering            endowed   spendable  4,050.00   0/1 awards
                                       ↳ funds 0 of 1 intended awards
```

Zarou Engineering is a $90,000 endowment trying to make a $6,000 award at 4.5%.
**It cannot, and finding that out in August is far kinder than finding out
after an offer letter.** Either the award amount comes down or the endowment
needs growing — a conversation to have with the donor's family.

---

## 5. Disbursement, and the tax facts AFRP now owns

Because AFRP pays the **student** directly, AFRP is the payer of record.

*Since 20 August 2026:* D3 makes the Scholarship ARFECF's, so ARFECF is the payer of record and this section's tax facts are ARFECF's to capture. A disbursement drawn on another entity's account does not post (P26 §2.3, SA3; D3; ARFECF 6.4.8). In practice (research, 2 Oct 2026), the 2026 letters went out in AFRP's name and the office wrote the cheques; see Q-158. P26 §2 replaces §5.1's yearly gate with three verification rows per semester instalment (Q-159, Q-256).

### 5.1 Gates — nothing moves until verified

| Verification | When |
|---|---|
| Proof of enrolment | Every year |
| Bank details | Every year |
| Tax form (W-9 / W-8BEN) | Every year |
| Transcript | Years 2+ — this *is* the continuation review |

`authoriseDisbursement()` refuses while any gate is open and **names what is
missing**. "The payment didn't go through" with no reason is how a scholar
misses a tuition deadline.

### 5.2 Tax — the system captures facts and flags cases. It does not compute tax.

Under **IRC §117**, a scholarship is tax-free to a **degree candidate** at an
eligible institution to the extent it pays tuition, required fees, books,
supplies and required equipment. **Room, board, travel and optional equipment
are taxable to the student.**

Three cases from the working engine:

```
US student, Michigan    AUTHORISED  net $2,500  withholding 0%
  flag: 700.00 is taxable to the student (room, board, travel).
        AFRP does not withhold; tell the student so it is not a surprise in April.

Student at Birzeit      AUTHORISED  net $2,500  withholding 0%
  flag: study is in PS — grant is likely FOREIGN-source and outside US
        withholding. Confirm with a tax adviser.

NRA on F-1 in the US    BLOCKED     net $2,402  withholding 14%
  flag: non-resident alien with US-source taxable income — withholding at 14%
        (F/J/M/Q visa rate). Report on Form 1042-S. A treaty may reduce this.
  blocked: tax treatment flagged and not yet cleared by an adviser
```

**The middle case matters most to AFRP.** Scholarship income is generally
sourced to *where the study takes place*. A grant to a student at Birzeit is
likely foreign-source and outside US withholding entirely; the same grant to a
student at Michigan is not. Given AFRP's ties to Ramallah this will come up
constantly, and it is the kind of thing that is easy to get wrong in both
directions.

**Design rule: any flagged case cannot pay until a named adviser clears it.**
The software records `adviserClearedBy`; it never decides. A tax adviser signs
this off, not a function.

`tax_status: unknown` is a **blocking state**, not a shrug — collect the W-9 or
W-8BEN before the first payment, not after.

---

## 6. Named scholarships — matching is a real problem

Assignment is deliberately **not** a greedy pass down the ranked list.
Scholarships are filled **most-constrained first**.

Why it matters, from the run:

```
Layla Khoury (87.0, medicine, GPA 3.8) → Haddad Memorial (Medicine)  $5,000
Rana Salameh (75.0, medicine, GPA 3.4) → Haddad Memorial (Medicine)  $5,000
Basim Yacoub (75.0, Detroit)           → Shaheen Family (Detroit)    $4,000
Mona Zarou   (88.0, engineering)       → General Scholarship Fund    $3,000
```

Mona Zarou ranked **first overall** and did not get the Zarou Engineering award
— because that endowment has no capacity this year. Meanwhile Layla, ranked
second, took the restricted medical award she uniquely qualified for.

A naive top-down pass would have given Layla the general fund first, and the
Haddad Memorial — a donor's restricted money — would have sat unawarded for a
year. Every unfilled award and unmatched scholar is reported **with a reason**,
so the committee can see whether the constraint was funding, criteria, or
competition.

---

## 7. Integrations

### 7.1 Membership — the free student membership

Recipients get a **complimentary student membership in their own name**,
created on award acceptance. Modelled as `is_complimentary` on the membership,
so it counts for standing and voting without touching the ledger — $0 produces
no journal entry.

**This is the recruitment mechanism, not a perk.** A scholarship brings an
unaffiliated family into AFRP through their child, and that child becomes a
member of record at eighteen rather than a dependent on someone else's card.
It is also why the household work matters: the scholar gets their own
membership without being ejected from their family.

### 7.2 Magazine

Publication requires **explicit consent** — `scholar_consent.magazine_publish`
and `photo_publish`, both defaulting false and separately revocable. Accepting
an award never implies consent to appear in *Hathihe Ramallah*.

Donor stewardship is a third, separate consent (`donor_may_know`). A donor
learning who received their named award is powerful for retention and must
still be the scholar's choice.

### 7.3 Family tree

Two jobs, both operational rather than ceremonial:

1. **Descent verification** — the eligibility gate, since the program is open
   to any Ramallah descendant rather than to members.
2. **Conflict detection** — §3.

---

## 8. Historic data

The program has run for years. `is_historic` on applications and awards lets a
past award exist with **no application, no reviews, and partial fields**, so
history can be loaded without fabricating records that never existed.

Suggested import tiers, cheapest first:

| Tier | Data | Effort |
|---|---|---|
| 1 | Recipient, year, amount, scholarship name | Low — a spreadsheet import |
| 2 | + institution, field, graduation | Medium |
| 3 | + applications, scores, committee minutes | High — often unrecoverable |

**Do tier 1 for everything and stop.** It gives the alumni list, the named-award
history, and total giving impact — which is 90% of the value. Tier 3 is worth
it only for years where the paperwork genuinely survives.

---

## 9. What is in the code

| Component | File | Tests |
|---|---|---|
| Committee composition, conflicts, scoring, ranking | `src/scholarships/committee.ts` | 41 combined |
| Endowment capacity, encumbrance, forward projection, matching | `src/scholarships/budget.ts` | |
| Verification gates, tax assessment, authorisation, progress | `src/scholarships/disbursement.ts` | |
| Schema — scholarships, cycles, applications, reviews, conflicts, awards, award years, verifications, disbursements, consent | `src/db/schema.sql` | — |

**Schema now 75 tables. 220 tests passing, typecheck clean, portability guard clean.**

---

## 10. Delivery

| # | Work | Effort |
|---|---|---|
| 1 | Application form builder + versioned payloads | 2 wk |
| 2 | Committee console: queue, rubric, recusal | 2.5 wk |
| 3 | Budget, encumbrance, forward projection | 1.5 wk |
| 4 | Named scholarships + matching | 1.5 wk |
| 5 | Board approval workflow | 1 wk |
| 6 | Verification upload + review | 2 wk |
| 7 | Disbursement + ledger posting | 1.5 wk |
| 8 | Scholar tracking + graduation | 1 wk |
| 9 | Historic import (tier 1) | 1 wk |
| 10 | Magazine + membership integration | 1 wk |

**About 15 weeks.** Items 1–2 deliver the first usable cycle; 6–7 can follow
before the first disbursement is due.

---

## 11. Open questions

1. **Who is the tax adviser** who clears flagged disbursements? The workflow
   needs a named person before the first non-resident award.
2. **What is the actual rubric,** and how many reviewers per application?
3. *(Since 8 September 2026 (David's correction, P26 §1.4): disclosed by degree, only the same household refuses. Recorded as D84 (4 Oct 2026), conditional on the Scholarship Fund Committee adopting it as its conflict policy; no such act is on file.)* **Is 3 degrees the right conflict bar?** It is a committee policy question,
   and I have set a default rather than a rule.
4. *(Since 2 October 2026: the office's list of about twenty names enters as candidate rows, "instrument not found", refusing posting and matching until reconciled — P26 §5, SA6; Q-102.)* **How many named scholarships exist,** and does each have written donor
   criteria? Undocumented criteria are the most common cause of a stranded
   named fund.
5. **Are any named endowments underfunded** relative to their award amount, as
   a named family's scholarship (example) in §4.1 shows? Worth auditing before the next cycle.
6. **What historic data actually survives,** and for how many years?
7. **Does the free student membership have an age or enrolment limit?**
8. **Who approves the budget** — the committee recommends and the board
   approves, or the committee decides within an envelope?

---

*IRC §117 treatment and non-resident withholding per IRS guidance, August 2026.
Rubric weights, spending rates, conflict thresholds and all figures are
illustrative; AFRP's committee and tax adviser set the real ones.*

**Sources:** [IRS Topic 421 — Scholarships and fellowship grants](https://www.irs.gov/taxtopics/tc421) ·
[IRS — Withholding on scholarships paid to nonresident aliens](https://www.irs.gov/individuals/international-taxpayers/withholding-federal-income-tax-on-scholarships-fellowships-and-grants-paid-to-nonresident-aliens)
