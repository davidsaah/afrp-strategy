# AFRP — multi-entity ledger and club remittance
### Addendum 6

**Date:** August 15, 2026
**Trigger:** clubs keep their own books; clubs are separately incorporated
**Since 2 October 2026:** the research round found how the Federation's own books now run across the three entities. That is recorded in §9 as practice, never as a decision; D1 and D56 stand, and nothing below changes because of it.

---

## 1. The four answers, and what they cost

| Answer | Consequence |
|---|---|
| **National collects, then remits to clubs** | One merchant account, one payment experience. A periodic remittance run replaces per-club payment plumbing. **Much simpler than the alternative** |
| **Only larger clubs keep formal books** | Three ledger modes: `qbo` (synced), `platform` (lightweight internal), `none` (statement only). "No books" is a supported state, not an error |
| **Clubs are separately incorporated** | No consolidation. **But it changes how national must book club dues — see §2** |
| **Each club administers its own connection** | Dead connections are expected, not exceptional. Postings queue; national's close never waits on a club |

*In practice (research, 2 Oct 2026):* the Federation now runs **three card-processing accounts, one per entity (AFRP, ARFECF, ARFHSN)**, replacing one AFRP account whose receipts were moved to the affiliates by hand; the registration system's pay links name the receiving entity's processor profile. That is the split between the Federation's entities, not the club split this table answers, and it leaves the club rows above as written; see §9 and Q-232.

Taken together this is a **much better outcome than the worst case.** No
split-tender payments, no inter-entity due-to/due-from between 27 ledgers, no
consolidation eliminations. One collection point and a monthly payout run.

---

## 2. The accounting point that matters

Because clubs are **separate legal entities**, club dues collected by national
are **not national's revenue.** National is holding money for someone else.

```
On collection                                    On remittance
Dr  Gateway clearing     1,194.74                Dr  Due to local clubs   1,240.00
Dr  Merchant fees           45.26                    Cr  Cash                 1,240.00
    Cr  Due to local clubs    1,240.00   ← LIABILITY, not income
```

**Booking club dues as revenue would overstate national's income — and its
990 — by the entire club-dues line.** On the seeded run above that is $3,360 in
a single month across five clubs. Across 26 clubs and a year it is a materially
wrong Form 990.

The club's own books mirror it:

```
Dr  Cash                 1,240.00
    Cr  Membership dues      1,240.00     ← the club's revenue, in the club's ledger
```

### 2.1 The caveat, which is real

Under ASC 958 a recipient organisation **may** recognise revenue rather than a
liability if it holds **variance power** (the ability to redirect the funds
elsewhere) or is **financially interrelated** with the beneficiary — one can
influence the other's operating and financial decisions, and has an ongoing
economic interest in its net assets.

**A federation and its chartered clubs could plausibly meet that test.** That is
a judgement for AFRP's CPA, not for a schema.

So `treatment` is set per club and defaults to the conservative `agency`. Under
`revenue`, national books the dues as income and the payout as a grant to an
affiliate. Both are implemented and tested; the numbers move materially between
them, which is exactly why it is an explicit setting rather than an assumption
buried in a query.

**Ask the accountant this once, get it in writing, and record the answer in
`club_ledger_profile.treatment`.**

*In practice (research, 2 Oct 2026):* the Federation's chart of accounts already books every affiliate purpose it collects (ARFECF's, ARFHSN's and the Ramallah Foundation's) as a "due to" liability, the agency pattern of D1 and D56 applied more widely than either decision names. No account on either side yet carries club-collected national dues. Which of the four roles called "the CPA" gives the written answer is Q-231; the countersignature itself is still Q-3 (D1).

---

## 3. Worked remittance run

Real output from the implemented engine:

```
REMITTANCE RUN — August 2026

club             mode          gross       due   carried   note
Detroit          qbo         1240.00   1240.00      0.00
Chicago          qbo         1120.00   1120.00      0.00
Houston          platform     880.00    880.00      0.00
Jacksonville     none         120.00    120.00      0.00   statement only, no club-side journal
Cleveland        none          40.00      0.00     40.00   below club minimum of 50.00 — carried forward
TOTAL PAYABLE                          3360.00     40.00 carried

NATIONAL — collection (agency)
  1200 Dr  1194.74   Detroit — club dues collected
  6100 Dr    45.26   Detroit — processing fees
  2400   Cr 1240.00  Due to Detroit — held for a separate entity
  club dues in national INCOME: false

NATIONAL — payout            DETROIT — receipt
  2400 Dr  1240.00             1000 Dr  1240.00
  1010   Cr 1240.00            4000   Cr 1240.00

Jacksonville keeps no books -> club-side entry: none (statement only)
```

### 3.1 Two behaviours worth knowing

**Small balances carry forward.** Cleveland collected $40 against a $50
minimum, so it accumulates rather than generating a cheque. Without this, small
clubs are either nickel-and-dimed with tiny payments or quietly never paid.

**Who bears the processing fee is a policy setting.** `national_absorbs` (the
club receives full dues; national eats the ~3.9%) or `prorated_to_club` (the
club receives net). Clubs *will* ask, so decide it before the first run rather
than after. Currently defaulted to `national_absorbs`, which is the more
generous and more common choice.

---

## 4. Dead club connections

Volunteer treasurers administer these, and QuickBooks refresh tokens expire
after ~100 days of disuse. **Expect connections to die routinely** — with a
dozen clubs on QBO, roughly one a month is a reasonable planning assumption.

```
BLOCKED  Chicago         Connection expired. Only the club treasurer can
                         re-authorise. 2 postings queued.
URGENT   Houston         Refresh token expires in 6 days. Chase the treasurer now.
WARN     San Francisco   Never connected — send the treasurer an authorisation link.
OK       Detroit         Healthy.
```

Three design rules follow:

1. **A dead club connection never blocks national's close.** National's books
   are complete regardless of any club's connection state.
2. **Club-side postings queue and replay** on reconnection. Nothing is lost, and
   nothing needs re-running by hand.
3. **The nag starts 21 days out**, because after expiry only the club treasurer
   can fix it — and a volunteer treasurer is not a same-day responder.

`v_club_connection_risk` drives this, and self-service re-authorisation should
be a one-click link emailed to the treasurer rather than a support ticket.

---

## 5. Three ledger modes

| Mode | Who | What happens |
|---|---|---|
| `qbo` | Larger clubs with a bookkeeper | Full two-sided posting; club-side entries sync to their QuickBooks |
| `platform` | Clubs wanting books without QuickBooks | Lightweight ledger inside the platform; exportable |
| `none` | Most volunteer clubs | National posts correctly; the club receives a **statement**, not a journal |

**`none` is the default and it is not a deficiency.** Most volunteer-run clubs
have a treasurer with a spreadsheet and a bank account, and a system that treats
that as an error state will simply be worked around. The statement — what was
collected, from whom, what was remitted — is genuinely all most clubs need.

A club can move `none → platform → qbo` as it grows without any migration.

---

## 6. What is in the code

| Component | File | Tests |
|---|---|---|
| Remittance runs, agency vs revenue, fee policy, carry-forward | `src/ledger/remittance.ts` | 16 |
| Multi-entity schema — club ledger profiles, per-club QBO connections, runs, lines, sources | `src/db/schema.sql` | — |
| Connection triage | `src/ledger/remittance.ts` | |

**Schema now 62 tables. 179 tests passing, typecheck clean, portability guard clean.**

---

## 7. Delivery

| # | Work | Effort | Notes |
|---|---|---|---|
| 1 | **Get the agency-vs-revenue answer in writing** | — | **Blocks everything.** One conversation with the CPA |
| 2 | Club ledger profiles + survey of who keeps books | 1 wk | Needs a call to 26 clubs, not a developer |
| 3 | Remittance run + national-side posting | 1.5 wk | Engine written |
| 4 | Club statements (the `none` path) | 1 wk | Serves the majority of clubs |
| 5 | Per-club QBO connection + self-service re-auth | 2 wk | Multi-tenant OAuth |
| 6 | Club-side posting with queue and replay | 1.5 wk | |
| 7 | Connection monitoring and treasurer nags | 3 days | Do not skip — this is the recurring failure |
| 8 | Parallel run with 2–3 clubs | 3–4 wk | Calendar time |

**About 9–11 weeks**, and item 1 gates the rest. Slots alongside the national
QuickBooks work rather than after it — the collection-side entries are the same
daily close.

---

## 8. Open questions

1. **Agency or revenue?** §2.1. Get it in writing from the CPA. *Since 2 Oct 2026:* this is Q-3 (D1's countersignature, put together with D56's agency treatment); which CPA is meant is Q-231; the books already use the agency pattern for affiliate purposes (§9).
2. **Who bears the processing fee** — national or the club?
3. **How many clubs actually keep books,** and on what? Needs a survey, and it
   is a phone call rather than a query. *In practice (research, 2 Oct 2026):* clubs keep their own books (some in Breeze, some in QuickBooks); none is in the Federation's file. The count is still not stated.
4. **What is the remittance cadence and minimum?** Monthly with a $25 floor is
   modelled; clubs may want quarterly.
5. **Are all 26 clubs separately incorporated,** or only some? A club inside
   AFRP's legal entity is consolidated and behaves completely differently.
6. **Do any clubs currently collect dues directly?** If so, migrating them to
   national collection is a member-facing change and a governance conversation.
7. **Who signs off a remittance run** before payment? Modelled as
   `remittance_run.approved_by`; the policy is undecided. *Since 2 Oct 2026:* the cadence and approver for settling each affiliate's "due to" account is Q-232; club dues are still Q-36 under D1 and D57.

---

## 9. In practice: the Federation's books across the entities (research, 2 October 2026)

What the Federation's own files show, recorded as evidence of practice under D41. None of it is a decision, none of it changes D1 or D56, and none of it sets a default for the platform. Each line names the question that holds it.

- **Accounts retitled per entity.** Bank accounts that had carried the wrong entity were retitled to the right one in 2025–26. *In practice (research, 2 Oct 2026); the agency treatment is Q-3 and Q-232.*
- **Three processor accounts.** One card-processing account per entity (AFRP, ARFECF, ARFHSN), with ARFHSN's own merchant account set up in spring 2026; the pay links choose the entity's profile and whether the payer covers the card fee. *In practice; Q-232.*
- **QuickBooks is already integrated with the current CRM.** QuickBooks Online holds AFRP's and ARFECF's books from the 2026 Mid-Year, with ARFHSN to follow, fed from the registration system, with monthly statements and budget-versus-actual. The platform's own QuickBooks connection is still absent from the Hub (MASTER-PLAN §1a); the integration the Hub replaces is the CRM's, not a blank. *In practice; `AFRP-QuickBooks-Integration-Spec.md` §11.*
- **The "due to" family.** AFRP's chart carries a liability for each affiliate purpose collected on the affiliates' behalf (ARFECF's, ARFHSN's and the Ramallah Foundation's), plus "Due to Convention Host City" and a Convention bank account (P22 §10). How often and on whose approval each is settled is **Q-232**.
- **The Relief Fund in ARFECF's books.** ARFECF's balance sheet carries the Relief Fund as its own bank account, with AFRP owing it. The record's rule stands: the fund posts nothing until a Board names its holding entity. *In practice; Q-109 (P23 §2).* *Since 3 Oct 2026:* D83 names AFRP; the fund posts to AFRP, and ARFECF's booking is the reconciliation item D83 names (the books follow D83, or the Boards revisit).
- **The Convention leg through ARFECF.** ARFECF's balance sheet carries an amount due to AFRP for the Convention host fee. The Convention is AFRP's (D1 G), and the platform refuses a Convention posting to an ARFECF account. *In practice; Q-224 (P22 §10).*
- **Review and audit.** Both AFRP and ARFECF had financial reviews for the year to May 2025. ARFECF moves to a CPA audit from the year to May 2026 (FY2026); AFRP stays on review. *In practice; the export the outside firm needs is the QuickBooks spec's §6.*
- **"The CPA" is four roles.** The outside firm that reviews or audits and files the returns; the General Fund Treasurer, a CPA in practice; a volunteer financial adviser, also a CPA; and the bookkeeper. This document's "the CPA" (§2.1, §7 item 1, §8 q1) means the person who countersigns the treatment, which is not written. Which role is meant is **Q-231**.


---

*Agency-versus-revenue treatment per ASC 958 guidance on contributions held for
others. Figures are from the implemented engine against seeded data and are
illustrative.*

**Sources:** [Recording contributions held for others](https://www.nonprofitaccountingbasics.org/contributions/whose-money-it-recording-contributions-held-others) ·
[Revenue recognition for not-for-profits (RSM)](https://rsmus.com/content/dam/rsm/insights/financial-reporting/1pdf/Revenue-recognition-considerations-for-not-for-profit-organizations-202309.pdf) ·
[Misconceptions in not-for-profit accounting (CPA Journal)](https://www.cpajournal.com/2025/06/04/misconceptions-in-not-for-profit-accounting/)
