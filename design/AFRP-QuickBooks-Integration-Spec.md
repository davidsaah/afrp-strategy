# AFRP × QuickBooks Online
### Integration specification

**Date:** August 15, 2026
**Addendum 4 to:** AFRP Enterprise Platform architecture
**Status:** posting engine and connector implemented, 45 tests passing
**Since 2 October 2026:** the research round found the Federation already keeps its books in QuickBooks Online, integrated with the current CRM, with a real chart of accounts. §12 records what the sources show, as practice and never as a decision; the open questions of §11 carry their answers in practice. D1 and D56 stand.

---

## 1. Decisions

| # | Decision | Consequence |
|---|---|---|
| 1 | **QuickBooks Online** | REST API, OAuth 2.0, real webhooks, sandbox. Far friendlier than Breeze — the hazards here are accounting hazards, not vendor ones |
| 2 | **Daily summary journal entries** | One balanced entry per day per fund. The platform stays the donor system of record; QuickBooks holds the ledger |
| 3 | **Dues recognised in full when paid** | Simple. See §7 — worth one conversation with whoever signs the 990. *In practice (research, 2 Oct 2026):* this is the Federation's practice, and its chart already holds an unused deferred-dues account; the conversation is Q-233, with the outside firm |
| 4 | **Classes per fund** | Endowed Fund, Scholarship, Medical Mission each become a QB Class. Standard nonprofit pattern, works in every QBO tier |

Decision 2 is the one that keeps this maintainable. The alternative — a Sales
Receipt per gift with each member as a QuickBooks Customer — would put
thousands of customer records into the accounting file and produce a ledger no
bookkeeper wants to read. **QuickBooks answers "what did we receive"; the
platform answers "who gave it".** Traceability is preserved by
`journal_source`, which records exactly which gifts make up each summary line.

---

## 2. Chart of accounts

Placeholder numbers — substitute AFRP's real chart before go-live.

*Since 2 October 2026:* the real chart exists and is in use (§12). Among what it already carries: a Convention bank account and a **"Due to Convention Host City"** liability (P22 §10 maps the Convention's lines onto them); a "due to" liability for each affiliate purpose AFRP collects (Q-232); on ARFECF's side, the Relief Fund as its own bank account with AFRP owing it (Q-109). The mapping is typed by the bookkeeper against that chart, never by a build session (§10 item 2). The table below stays as the engine's test fixture.

| Account | Type | Purpose |
|---|---|---|
| 1200 · Undeposited / Gateway Clearing | Bank | Captured by Authorize.Net, not yet in the bank |
| 1010 · Operating Checking | Bank | Where settlements land |
| 4000 · Contributions — Unrestricted | Income | General Fund |
| 4100 · Contributions — Endowment | Income | Endowed Fund |
| 4200 · Contributions — Scholarship | Income | Scholarship Program |
| 4300 · Contributions — Medical Mission | Income | |
| 4400 · Contributions — Project Hope | Income | |
| 4500 · Program Fees — Camp Ramallah | Income | Exchange revenue, not a contribution |
| 4800 · Membership Dues | Income | |
| 4900 · Refunds & Chargebacks | Contra-income | Kept visible, never netted |
| 4950 · Net Assets Released — Unrestricted | Income | Release entries |
| 5900 · Net Assets Released — Restricted | Expense-type | Release entries |
| 6100 · Merchant Processing Fees | Expense | **Never netted into revenue** |

**Class list** (one per fund): `Unrestricted` · `Endowment` · `Scholarship` ·
`Medical Mission` · `Project Hope` · `Camp Ramallah`.

Every journal line carries a class. That is what makes the fund report come out
right, and it is the most common thing to get wrong when a class is optional.

---

## 3. Posting rules

### 3.1 The fee rule — the one that matters most

Authorize.Net deposits **net of fees**. Booking the net figure as revenue is the
single most common nonprofit bookkeeping error: it understates contribution
revenue *and* understates expenses, and it misstates the 990.

A $1,000 gift with a $29.30 fee posts as **three lines, not two**:

```
Dr  1200  Gateway Clearing            970.70    [class: Endowment]
Dr  6100  Merchant Processing Fees     29.30    [class: Endowment]
    Cr  4100  Contributions — Endowment      1,000.00   [class: Endowment]
```

The donor gave $1,000. The 990 must say $1,000. The $29.30 is an expense AFRP
incurred, not a reduction in generosity.

### 3.2 Worked daily close

Real output from the implemented engine against seeded data:

```
DAILY CLOSE — 2026-01-16   (297 gifts in scope, 4 batches)

doc number             fund                     debit      credit  bal
260116-CAMPRAMA-REV    Camp Ramallah          1025.00     1025.00   ok
260116-MEDICALM-REV    Medical Mission        1308.00     1308.00   ok
260116-PROJECTH-REV    Project Hope            148.00      148.00   ok
260116-SCHOLARS-REV    Scholarship Program    1978.00     1978.00   ok
TOTAL                                         4459.00     4459.00   BALANCED

pass 1: inserted 4 batches
pass 2: 4 duplicate posts BLOCKED by the unique constraint
unbalanced batches in the database: 0
```

Hundreds of gifts, four journal entries, every one balanced, every one
traceable back to its source rows.

### 3.3 Refunds and chargebacks post separately

They are **not** netted into revenue. A chargeback is something a finance
committee should be able to see, and netting hides it.

### 3.4 Net assets released from restriction

When restricted money is spent on its purpose:

```
Dr  5900  Net Assets Released — Restricted    12,500   [class: Scholarship]
    Cr  4950  Net Assets Released — Unrestricted   12,500   [class: Unrestricted]
```

The engine refuses to release from a **permanently restricted** fund — the
endowment corpus is not releasable, and that is enforced in code rather than
left to whoever runs the close.

### 3.5 Zero-dollar memberships

The wedding benefit grants a **$0 Family membership**. It produces no journal
entry — there is no cash and no revenue. It is still recorded in the platform
as a membership with `amount = 0`, so the count is right in membership
reporting even though the ledger is silent. Do not let anyone "book" it as
in-kind revenue; it is a waived fee, not a contribution.

---

## 4. Idempotency — guarded in three places

Double-posting to a general ledger is the worst thing this system could do. It
is prevented three times over:

| Layer | Mechanism |
|---|---|
| **1. Application** | Deterministic doc number from `(date, fund, kind)`. Same inputs, same string, every time |
| **2. Database** | `unique (period_date, fund_id, batch_kind)` and `unique (doc_number)` on `journal_batch` |
| **3. QuickBooks** | `DocNumber` sent to QBO. A duplicate returns fault **6240**, which the connector treats as *already posted* — success, not an error to retry |

**A bug caught by a test, worth recording:** the first doc-number format was
`AFRP-260815-ENDOWE-REV` — 22 characters against QuickBooks' 21-character
`DocNumber` limit. QuickBooks truncates silently, so doc numbers would have
collided across funds and quietly destroyed the idempotency they exist to
provide. The format is now budgeted to 19 characters with the limit asserted in
code, and a test proves two similarly-named funds do not collide after
truncation.

---

## 5. The OAuth trap

This is the failure mode most likely to bite in production, and it has nothing
to do with accounting.

- **Access tokens last 1 hour.** Cheap; refresh eagerly.
- **Refresh tokens ROTATE on every use** and **expire after ~100 days of
  disuse.**

So an integration that goes quiet — a slow summer, a paused programme — comes
back to a dead connection that only a QuickBooks admin can re-authorise.

Mitigations, all implemented:

| Risk | Mitigation |
|---|---|
| Connection dies from disuse | Scheduled refresh on a timer regardless of traffic |
| No warning before death | `daysUntilRefreshExpiry()` drives an alert well ahead |
| Rotated token lost on crash | Persist **before** the request proceeds; a failed persist aborts the call |
| Concurrent refreshes rotate twice | Refreshes serialised through a single in-flight promise |
| Dead token retried forever | A 400 on refresh is **not** retryable — it raises for a human |

---

## 6. Reconciliation

```
Authorize.Net settles          Platform knows              QuickBooks sees
─────────────────────          ──────────────              ───────────────
gross     $4,459.00       ←→   sum(gift.amount)      ←→    Cr revenue (gross)
fees        -$132.15      ←→   sum(gift.fee_amount)  ←→    Dr fee expense
net       $4,326.85       ←→   expected deposit      ←→    Dr clearing
                                                            ↓
                                              bank deposit clears clearing
```

`reconcileSettlement()` compares the gateway's figures against the platform's
and surfaces any variance. A few cents is fee rounding; a few hundred dollars
is a missing transaction. Neither is silently absorbed.

---

## 7. The one accounting question to settle

AFRP has chosen to **recognise dues in full when paid**. That is common for
organisations of this size and it is simpler.

*Since 2 October 2026:* "whoever signs the 990" is the outside firm, one of four roles the record has called "the CPA" (Q-231); the question itself is Q-233. ARFECF moves to an audit from the year to May 2026, so the answer matters more for ARFECF than it did.

It is worth one conversation with whoever signs the 990, because a $1,000 Patron
membership paid in March covers twelve months, and an auditor may take the view
that it is not all March revenue. Deferring would recognise roughly $83.33 per
month instead. The effect is on *timing* and year-over-year comparability, not
on totals.

**No rewrite is needed if the answer changes.** `fund.deferral_policy` is
already in the schema, the posting engine reads it, and there is a test proving
that flipping it to `monthly` redirects the credit to a deferred revenue
account. Switching is a data change plus a release schedule.

Two related questions for the same conversation:

- **Are membership dues partly a contribution?** Under ASC 958, dues above the
  value of benefits received are a contribution rather than exchange revenue.
  Splitting them is more correct and more work. Currently modelled as a single
  revenue line.
- **Are Camp Ramallah fees and convention tickets exchange revenue?** Almost
  certainly yes (ASC 606), which is why 4500 is a Program Fees account rather
  than a Contributions one. Worth confirming.

---

## 8. Failure modes and what happens

| Failure | Behaviour |
|---|---|
| A fund has no QuickBooks account mapped | Close **fails loudly** for that fund. Never posts to a default account |
| Fees exceed gross | Rejected as corrupt data, not treated as a small day |
| A gift references an unknown fund | Warned and excluded; never silently dropped |
| Batch does not balance | Raises before any API call. QBO would reject it anyway; failing locally gives a usable message |
| QuickBooks returns 6240 | Treated as already posted. No retry, no duplicate |
| QuickBooks 429 | Honours `Retry-After`, backs off |
| QuickBooks 5xx | Retries up to 3×, then marks the batch `failed` for a human |
| Refresh token dead | Alerts. **No automated recovery** — re-authorisation requires a QB admin |
| A posted entry needs reversing | **Not automated.** Reversing an entry in someone's general ledger is a bookkeeper's decision |

---

## 9. What is in the code

| Component | File | Tests |
|---|---|---|
| Posting engine — batches, fees, releases, reconciliation | `src/ledger/posting.ts` | 26 |
| QuickBooks Online connector — OAuth, rate limit, batch, webhooks | `src/integrations/quickbooks/client.ts` | 19 |
| Ledger schema — funds, batches, lines, settlements | `src/db/schema.sql` | — |

**Schema now 45 tables. 122 tests passing, typecheck clean, portability guard clean.**

The posting engine is **pure** — it computes a plan and does not write. That is
what makes the fee arithmetic, the balance assertion, and the release rules
testable without a database, which matters because all three are easy to get
quietly wrong.

---

## 10. Delivery

| # | Work | Effort | Notes |
|---|---|---|---|
| 1 | Connect the QBO app, sandbox first | 3 days | Needs an Intuit developer account |
| 2 | Map chart of accounts and classes | 1 wk | **Bookkeeper-led, not developer-led** |
| 3 | Fund and campaign mapping | 3 days | |
| 4 | Daily close job + posting | 1 wk | Engine already written |
| 5 | Settlement reconciliation | 1 wk | |
| 6 | Token lifecycle monitoring and alerts | 3 days | Do not skip |
| 7 | Parallel run — post to sandbox, compare to manual books | **3–4 wks** | Calendar time. Do not compress |
| 8 | Cutover + first month-end close together | 1 wk | Sit with the bookkeeper |

**About 8–9 weeks**, of which meaningful parts are somebody else's calendar
rather than engineering. Slots after Phase 1 (Authorize.Net reconciliation),
because the gift data must be trustworthy before it reaches the ledger.

---

## 11. Open questions

1. **Who is AFRP's bookkeeper or accountant**, and will they sit for the
   chart-of-accounts mapping? This integration cannot be specified without them.
   *In practice (research, 2 Oct 2026):* the office's Executive Administrator keeps the books, with a volunteer financial adviser alongside. Whether they sit for the mapping is not stated.
2. **What is the actual chart of accounts and class list today?** Everything in
   §2 is placeholder. *In practice:* the chart exists in QuickBooks Online for AFRP and ARFECF (§12); the class list is not stated.
3. **Does AFRP have an annual audit or a review?** Determines how strict the
   dues-recognition answer needs to be. *In practice:* reviews for AFRP and ARFECF for the year to May 2025; **ARFECF moves to a CPA audit from the year to May 2026 (FY2026)**; AFRP stays on review. Dues recognition is Q-233.
4. **Is the Endowed Fund truly permanently restricted** (corpus untouchable) or
   board-designated? They are accounted for very differently, and the engine
   currently refuses to release from it. *Since 1 Oct 2026:* Q-95.
5. **Who reconciles the bank today,** and would they rather see one deposit per
   settlement batch or per day? *In practice:* the bookkeeper reconciles monthly and the Treasurer reviews. The batch-or-day preference is not stated.
6. **Are local clubs in the same QuickBooks file** or do they keep their own
   books? If separate, this is 26 more integrations — please confirm before
   Phase 3 planning. *In practice:* clubs keep their own books (some in Breeze, some in QuickBooks); none is in the Federation's file (`AFRP-Multi-Entity-Ledger.md` §9).

---

## 12. In practice: the books as they stand (research, 2 October 2026)

Evidence of practice under D41, from the Federation's own minutes, reports and balance sheets, read at role level. It is not a decision and sets no default. D1 (club dues held as agent; the countersignature pending, Q-3) and D56 (AFRP collects ARFHSN's gifts as its agent) stand unchanged.

- **QuickBooks is integrated with the current CRM.** QuickBooks Online holds AFRP's and ARFECF's books from the 2026 Mid-Year, with ARFHSN to follow. It is fed from the registration system, with monthly statements and budget-versus-actual. Committee chairs are to get budget sheets from the books without the organisation's full statements. What the Hub replaces is therefore a working CRM-to-QuickBooks feed, not an empty ledger; the Hub's own connection is still absent (MASTER-PLAN §1a).
- **Accounts retitled per entity.** Bank accounts that carried the wrong entity were retitled to the right one in 2025–26.
- **Three processor accounts.** One card-processing account each for AFRP, ARFECF and ARFHSN, replacing one AFRP account with transfers made by hand. The pay links name the entity's processor profile and whether the payer covers the fee. For this spec that means one gateway clearing account per entity, not one for the Federation (§2's 1200). The mapping is the bookkeeper's.
- **The chart, structure only.** AFRP has operating and Convention bank accounts, "Due to Convention Host City", a "due to" family for ARFECF, ARFHSN and Ramallah Foundation purposes, the unused deferred-dues account, and income lines for dues, the endowment distribution, the Convention host fee and card-fee income. ARFECF has separate bank accounts for operating, the Relief Fund, the Magazine, the cook book and camp, with "due from AFRP" lines per purpose. P22 §10 maps the Convention onto these. P24 §6 maps the Magazine's two rows. P23 §2 and Q-109 cover the Relief Fund.
- **The Relief Fund is booked as an ARFECF bank account.** The platform's rule stands: the fund posts nothing until a Board names its holding entity (Q-109). *Since 3 Oct 2026:* D83 names AFRP; the fund posts to AFRP, and the ARFECF bank account is the reconciliation item D83 names (the books follow D83, or the Boards revisit).
- **Review and audit.** AFRP and ARFECF had reviews for the year to May 2025. ARFECF moves to audit from FY2026.
- **"The CPA".** Four roles answer to the name: the outside firm that reviews or audits and files; the General Fund Treasurer, a CPA in practice; a volunteer financial adviser, also a CPA; and the bookkeeper. Every "CPA" or "accountant" in this spec (§7, §10, §11) needs one of them named. **Q-231** asks which.

---

*QuickBooks Online API behaviour from Intuit developer documentation and
integration guides, August 2026. Chart of accounts, class list, and fee rates
are illustrative and must be replaced with AFRP's actual values.*

**Sources:** [QuickBooks Online API integration guide](https://www.getknit.dev/blog/quickbooks-online-api-integration-guide-in-depth) ·
[QBO API rate limits](https://satvasolutions.com/blog/quickbooks-online-api-limitations-guide) ·
[Nonprofit revenue recognition — exchange vs contribution](https://www.criadv.com/insight/nonprofit-revenue-recognition/)
