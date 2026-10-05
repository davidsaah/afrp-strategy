# AFRP decisions register
### The human decisions the platform design waits on — what has been decided, by whom, and what each one settled

**Maintained:** 4 October 2026. This is the authoritative record of the decisions the platform's
design is built on: Decisions 1 to 99, in seven parts (the first six blocking decisions below;
Part 2, 20–21 August 2026; Part 3, 8 September; Part 4, 30 September; D53–D67, 30 September to
1 October; Part 5, 2 October; Part 6, 3 October; Part 7, 4 October). When a decision is made, it is
recorded here in the exact words the design will be built on, with the date, the decider, and the
consequences that follow automatically.

**This register is the history.** Topics run through chains of decisions, and an earlier decision
keeps its text with a pointer to what amended or superseded it. The current rule on each topic,
with the decisions behind it and every decision still waiting on a body's act, is stated in
`site/data/decisions.yaml` and rendered as the site's **Rules in force** page
(`docs/history/rules-in-force.html`) under Decision 99. A build session reads that page; where it
and this register differ, this register governs (D41) and the page is corrected.

**Status vocabulary**

| Status | Meaning |
|---|---|
| **Adopted** | Decided and recorded; the design is built on it. |
| **Adopted, countersignature pending** | Decided for design purposes; a professional sign-off (CPA, counsel) is still required before it is defensible on the books. |
| **Partially resolved** | The principal question is answered; a named sub-question remains. |
| **Open** | Not yet decided; the platform carries a labelled default or a refusal. |

**The six blocking decisions below were answered on 20 August 2026, twenty more on 20–21 August
(Part 2), and twelve more on 8 September as the family tree became the platform's spine (Part 3).**
Ninety-nine decisions are recorded as of 4 October 2026. What is still left is listed under "What
is actually left" below; the open questions, each with a status under D99, are in
`site/data/questions.yaml`.

| # | Decision | Answer | Status |
|---|---|---|---|
| 1 | Club-collected AFRP dues | **Agency** — AFRP's money at the first dollar | Adopted, CPA countersignature pending |
| 2 | Endowment Fund entity | **ARFECF** | Adopted; Policy Statement found 1 Oct 2026 (status note under D3) |
| 3 | Scholarship's legal home | **ARFECF** | Adopted; conforming amendment needed |
| 4 | Digital voting | **Approved as the direction** (already done) | Adopted; ratification to be calendared |
| 5 | The two 9.1.3 drafts | ⚠ **REOPENED 21 Aug** — recorded in error | Needs an answer |
| 6 | Dormant-club prepaid dues | **Stay valid for the remainder of the year** | Adopted; directory grace still unset |

---

## Decision 1 — Club-collected AFRP dues are held as agent
**Status: Adopted, countersignature pending · decided by David Saah, 20 Aug 2026 · CPA countersignature outstanding**

### The adopted wording
> When a club collects AFRP membership dues, the club acts as AFRP's **agent**. The money is
> AFRP's from the first dollar. The club never owns it, never books it as revenue, and holds it in
> trust until it is remitted to the General Treasurer.

### Why the operative text supports it
This is a reading the by-laws already lean toward, which is what makes it defensible:

- **By-Law 5.2** — host-collected dues and fees "must be promptly remitted to the General
  Treasurer" and **do not count toward host convention proceeds**. Money that cannot count as the
  collector's proceeds was never the collector's money.
- **By-Law 11.1.5** — all club-raised funds for AFRP-sponsored projects route through Federation
  headquarters.
- **By-Law 8.12.4** — dues are valid for voting only when paid from the applicant's own funds,
  which frames the member as paying AFRP directly rather than paying their club.

### What this settles, automatically

| # | Consequence |
|---|---|
| A | AFRP dues are AFRP's money **at the moment of collection**, through any channel and any collector. |
| B | On the **club's** books, collected AFRP dues are a **custodial liability**, never revenue. A club's income statement never shows AFRP dues at all. |
| C | On **AFRP's** books, unremitted collections are a **receivable from the club**, recognised at collection rather than at remittance. |
| D | **Standing starts at collection, not remittance.** Because the member has paid AFRP the moment they hand money to the club, By-Law 4.3.1 standing and the 5.3 April 30 franchise test key to the **collection date or postmark**. A slow-remitting club cannot disenfranchise its own members. *(New interpretive consequence — see the override note below.)* |
| E | The receipt the member receives is **AFRP's receipt**, issued in AFRP's name, whichever channel collected. Clubs do not issue receipts for AFRP dues. |
| F | **Reversals (S3)** run against AFRP with the club's receivable adjusted. The club is not out of pocket for a member's chargeback unless the collection failure was the club's. Standing reverts with an effective date; frozen rolls are annotated, never recomputed. |
| G | **Convention money** needs no special rule. By-Law 5.2's host-remittance clause is now simply an instance of the general rule, consistent with the settled position that convention money is federation money at the first dollar. |

### What agency does *not* cover — the three other treatments stay distinct
Agency applies to **AFRP dues only**. The platform continues to run four separate money
treatments, and this decision changes only the first:

1. **AFRP dues** — agency. AFRP's money at the first dollar. *(This decision.)*
2. **The club's own local dues** — club money, club revenue. By-Law 4.3.1 requires both national
   and club dues, so a single payment often carries both; the platform **splits it at the point of
   capture** into two ledger destinations rather than settling and re-dividing later.
3. **Club haflis, local fundraisers and club events** — club money, split by **collection channel,
   not by occasion**. Platform-collected receipts are federation-held and remitted; off-platform
   receipts stay with the club.
4. **Club funds raised for AFRP-sponsored projects** — a **conduit** under 11.1.5. Neither club
   revenue nor an agency collection; routed through headquarters with the purpose preserved.

### Follow-on work this creates (design, not decisions)
- **Attestation and reconciliation.** Because standing now begins at collection, a club could in
  principle assert collections it has not made. Each collection event is individually attested
  (member, amount, date, channel, collector), reconciled against the remittance, and any variance
  opens a queue item with an owner and a clock. A variance never silently adjusts a member's
  standing in either direction.
- **Override register entry.** Consequence D is an interpretation, not an express rule — 5.3 says
  dues must be "received at the A.F.R.P's office by, or postmarked by, April 30th," and agency makes
  receipt by the agent receipt by AFRP. This is being entered as a provisional AFRP-lineage override
  pending Board adoption, in the same class as every other provisional reading.
- **Effective date.** Prospective from adoption, with the current membership year restated. Carried
  as a parameter, not hard-coded.

### What the CPA is still being asked to countersign
That the agency characterisation is correct for AFRP's books and filings, and that recognising the
receivable at collection rather than at remittance is right for the fiscal year (Jun 1 – May 31)
against a membership year of Jan 1 – Dec 31. If the CPA disagrees, consequences B, C and F change
and the first ledger tables change with them.

---

## Decision 2 — The Endowment Fund sits in ARFECF
**Status: Partially resolved · entity decided by David Saah, 20 Aug 2026 · Policy Statement outstanding**

> **Challenged, 1 October 2026.** A 2025 "AFRP Endowed Fund Investment and Distribution Guide" (an undated draft, approver blank) describes the fund as held across AFRP's and ARFECF's investment accounts, with distribution capped at a share of a three-year average and a share of every restricted gift to operations. It is not adopted; an investment policy statement goes to both boards on 4 November 2026. Until then this decision stands and the 2012 Endowment Fund Policy Statement governs the rule (Q-35).

### The adopted wording
> The Endowed Fund is held by **ARFECF** — the American Ramallah Federation Education & Charitable
> Fund — and is governed by ARFECF's by-laws and its Endowment Fund Committee.

### What this settles

| # | Consequence |
|---|---|
| A | The Fund is governed by ruleset **`arfecf-bylaws-2013.1`**, not by AFRP's. Every endowment screen names that ruleset. |
| B | The **Endowment Fund Committee has exclusive authority** to authorise Fund expenditures (ARFECF 6.3.4). Not the ARFECF Board, not the AFRP Board. |
| C | Non-earmarked funds may **never** be diverted between the Endowment Fund and the Scholarship Fund (6.3.8) — the platform refuses the transfer and names the rule. |
| D | Fund-policy amendments require **2/3 of all voting Board members** — a fixed denominator of 15 (EC-OV-11) — and must be taken at a meeting, not by poll, because abstention functions as a No. |
| E | Any AFRP-to-ARFECF flow **crosses an entity line** and therefore requires a recorded agreement in the institution registry. The 1% administration fee is itself an agreement, not a setting. |

### What is still outstanding on this decision
1. **The Endowment Fund Policy Statement is not on file.** It is cited as governing and has never
   been produced. Until it is, the platform runs the operative by-law text alone.
2. **The 4% floor versus the 5% cap is still live.** ARFECF 6.3.3 sets a **cap** — expenditures
   "limited... only to five (5%) percent." The 2015 Scholarship Fund Policy Statement is understood
   to make 4% plus 1% **mandatory**. A cap and a floor are not the same instrument. The platform
   currently enforces the cap from the operative text and shows the Policy Statement figures as
   **unsourced and inactive** until the document arrives.
3. **ARFECF's own exempt status is unconfirmed.** We hold no determination letter. If gifts to the
   endowment are being receipted as deductible, that letter needs to be on file — ARFHSN's text
   describes AFRP as 501(c)(4) and ARFHSN as 501(c)(3), and ARFECF's status is simply not evidenced
   in anything we have.

### Interaction with Decision 3 — worth deciding together
Putting the endowment in ARFECF raises the stakes on the scholarship's legal home. If the
scholarship also lives in ARFECF, endowment income funds it **inside one entity** and no agreement
is needed. If the scholarship goes to the Ramallah Foundation, every distribution **crosses an
entity line** and requires a standing inter-entity agreement with terms, review dates, and a stated
consequence if it lapses. Decision 3 is now materially cheaper one way than the other, and the board
should see that before it votes.

---

## Decision 3 — The scholarship's legal home is ARFECF
**Status: Adopted · decided by David Saah, 20 Aug 2026 · conforming amendment required**

### The adopted wording
> The scholarship is held by **ARFECF**, alongside the Endowed Fund. The Ramallah Foundation's
> continuing role in the scholarship is a **partnership recorded as an agreement**, not a governance
> role.

### Why this is the cheaper answer — and it is materially cheaper
Because Decision 2 put the endowment in ARFECF, putting the scholarship there too means endowment
income funds the scholarship **inside a single entity**. No money crosses an entity line, so no
standing inter-entity agreement, no per-distribution terms, no lapse consequence to administer. Had
the scholarship gone to the Foundation, every single distribution would have needed one.

### What this settles

| # | Consequence |
|---|---|
| A | Both funds are governed by **`arfecf-bylaws-2013.1`**. The Scholarship Fund Committee holds exclusive authority over Scholarship Fund expenditures (6.4.4), the Endowment Fund Committee over Endowment Fund expenditures (6.3.4), and **neither may divert non-earmarked funds to the other** (6.3.8 / 6.4.8). Same entity is not the same fund. |
| B | The **Ramallah Foundation stays a partner** in the institution registry — agreements and contacts only, no governance surfaces, no ruleset lineage, no minutes. Its historic joint role in the scholarship is captured as a recorded agreement with terms, a review date, and a stated consequence if it lapses. |
| C | Award receipts and the donor-facing exempt status are **ARFECF's**, not AFRP's and not the Foundation's. |
| D | Committee members serve up to **two consecutive three-year terms**; the Chairman a maximum of two consecutive one-year terms (6.4.5, 6.6.1). Holdover time counts against the limit (EC-OV-20). |
| E | The **4% floor versus 5% cap conflict now governs both funds**, not one. This raises its priority — see below. |

### The drafting gap this exposes — and it needs an amendment
AFRP members are certified to vote for "members of the Scholarship Committee" (By-Laws 5.3 and
8.12.5), **yet no AFRP by-law constitutes a Scholarship Committee**. The only textual bridge is the
ARFECF Scholarship Fund Secretary's seat on the AFRP Executive Committee (7.1.1) and the reference
to "the Federation Scholarship Committee" at 7.6.1. With ARFECF confirmed as the home, this is now
definitively a **cross-entity election**: AFRP's franchise electing an ARFECF body. That works, but
it must be written down. See the amendment package below.

### What this makes urgent
The **4% floor versus 5% cap** question now sets the spend rule for the endowment *and* the
scholarship. ARFECF 6.3.3 and 6.4.3 both read as a **cap** — "limited... only to five (5%) percent."
The 2015 Scholarship Fund Policy Statement is understood to make 4% plus 1% **mandatory**. A cap and
a floor are different instruments and cannot both be enforced by the same control. Until the Policy
Statement is produced, the platform enforces the by-law cap and shows the Policy Statement figures
as unsourced and inactive.

---

### Status note, 1 October 2026
- **The Scholarship Fund Policy Statement (revised 2015) is found**, with the 2012 Endowment Fund Policy Statement. Both make a 4% programme distribution and a 1% transfer to AFRP **mandatory** each fiscal year: together they equal the by-laws' 5% limit, so the "floor versus cap" framing above is withdrawn. The policies fix the distribution at the cap, split 4 + 1, measured on the 31 May valuation. Still open: who may waive or carry it over. Extract in `design/bylaws/ARFECF-2015-and-the-fund-policies.md`.
- **The committee's make-up conflicts with this decision.** The 2015 policy sets the Scholarship Fund Committee as a chairman, the executive director, at-large members chosen by the ARFECF Board and three members elected at the Convention. It names no Ramallah Foundation seats. The committee's current overview lists three Foundation representatives among its members (Q-29). Recorded here as a conflict for the ARFECF Board; nothing in the platform seats them until it is resolved.

---

## Decision 4 — Digital voting is the approved direction
**Status: Adopted and confirmed · Board decision, reconfirmed by David Saah 20 Aug 2026 · ratification to be calendared**

### The position
> The Board has already approved full digital voting as the direction — for elections, referenda and
> the convention floor. This is settled and is not reopened.

The platform is designed and mocked for it end to end. Until the conforming amendment to By-Law 9.2
is ratified, **the adopted 2024 text is still the law**: the mailed CPA ballot, sealed envelopes, a
June 10 postmark, ties broken by a draw from a bag. The platform runs that process in full and
labels it the **transitional channel**, with the digital design carried as an adopted direction,
honestly labelled. Nothing about this is hidden from a member looking at a ballot screen.

**What remains is a calendar item, not a decision:** which convention the 9.2 amendment is put to,
and who drafts it. The Constitution Committee has the drafting workbench.

---

## Decision 5 — The two 9.1.3 amendment drafts
**Status: ⚠ REOPENED 21 Aug 2026 — recorded in error, never actually decided**

### The correction
On 20 Aug the answer *"have the option for both"* was written down here as **"advance both
amendments."** On 21 Aug David confirmed he meant something else entirely: that a **member**
keeps both options — voting through their delegate, or extracting to vote independently —
which By-Law 9.1.3 already provides and which both drafts preserve.

So the question this register recorded as answered **was never actually asked**. Whether
either amendment goes to the floor is still open, and is left open here rather than quietly
kept as adopted. The drafts are ready; the decision to advance them is not made.

### What still needs deciding
- **Weights fix at opening.** 9.1.3 lets a certified member extract their vote from their
  delegation and never says when that stops, so weights can shift mid-count. *(This is S4,
  demonstrated live at motion M-3 in the prototype.)*
- **The at-large roll.** Members with no chapter club have no delegation to be counted in and
  the text is silent on what becomes of their vote.

Both are 2/3 delegate-vote matters, which means 9.1.3's weighted fractional voting applies to
the amendments that fix 9.1.3.


## Decision 6 — Prepaid dues stay valid for the remainder of the year
**Status: Adopted · decided by David Saah, 20 Aug 2026 · one parameter still unset**

### The adopted wording
> When a club goes dormant mid-year, dues its members have already paid **stay valid for the
> remainder of the membership year**. A member is not disrupted by their club's dormancy.

### What this settles

| # | Consequence |
|---|---|
| A | Dormancy is a **club-state change, not a member-state change**. The member's standing runs to 31 December on what they already paid. |
| B | The AFRP portion was never the club's money in the first place (Decision 1), so nothing about it is in question — it is remitted or recovered as a receivable regardless of the club's state. |
| C | The **club portion** is held rather than refunded, and carries the member to year end. No refund workflow is built, and no clawback. |
| D | By-Law 4.3.1's conjunctive test — AFRP standing **and** club standing — is satisfied for the remainder of the year even though the club is dormant, because the member did everything the by-law asked of them. This is entered as a provisional override, since 4.3.1 does not contemplate a dormant club. |
| E | At year end the member needs a home: either the club revives, or they transfer to another club, or they fall to the **at-large roll** — which Decision 5 is now building. The two decisions fit together. |

### The one parameter still unset — the directory grace period
Separate from the above: after a member's dues lapse at year end and are not renewed, **how long do
they remain visible in the member directory?** The parameter **defaults to 0**, meaning a lapse is
currently an instant disappearance from the directory — which is almost certainly not the intent and
reads as harsh to the member and to everyone who was looking for them.

The platform will not invent this number. **A 90-day grace is the sensible default** — it covers the
common case of a late renewal without leaving non-members visible indefinitely, and the directory
entry can be shown with a quiet "renewal pending" state rather than silently. Confirm 90 days or
name a different figure and it is set.

---

## The conforming-amendment package these decisions create
Four amendments now need drafting for the convention floor. They should go as a package, because
three of them touch Article IX and a floor that adopts them piecemeal creates new gaps:

| # | Amendment | Source | Why |
|---|---|---|---|
| 1 | **By-Law 9.2 revision** — digital voting | Decision 4 | Conforms the text to the Board's approved direction; retires the mailed-ballot machinery or makes it explicitly the fallback channel. |
| 2 | **By-Law 9.1.3 — weights fix at opening** | Decision 5 | Closes the mid-count weight shift (S4). |
| 3 | **By-Law 9.1.3 — the at-large roll** | Decision 5 | Enfranchises members with no chapter club; also gives Decision 6's year-end case somewhere to land. |
| 4 | **Scholarship Committee — constitution and cross-entity election** | Decision 3 | Members are certified to vote for a committee no AFRP by-law constitutes. Writes down the ARFECF home and the cross-entity election. |

All four are **2/3 delegate-vote matters** under By-Law 16.1.1 and 9.1.1(3), which means the weighted
fractional voting of 9.1.3 applies to the amendments that fix 9.1.3 — worth stating plainly to the
floor rather than letting someone discover it mid-debate. Submission deadline is **60 days before
the General Assembly** to the Executive Director or Executive Assistant, with the Constitutional
Committee's review distributed to the Board and the Council of Chapter Club Presidents **45 days
before**.

---

## What is actually left, now that the decisions are made
*Brought up to date 4 October 2026 (D99). The list as written on 8 September named one signature,
five missing documents and one number; three of the documents have since been found.*

**Signatures and acts by a body**
- The CPA countersignature on the agency treatment (Decision 1; Q-3).
- Every other decision waiting on a body's act (D55, D58, D84, D87, D91, D93, D94, D97 and others)
  is listed, with the body and the act, on the Rules in force page under "Waiting on a body's act",
  generated from `site/data/decisions.yaml`.

**Documents cited as governing and still not on file (Q-2)**
- ARFECF's exempt-status determination letter, load-bearing for endowment and scholarship donor
  receipting.
- The Board Rules & Regulations, the authority for the dues tiers.
- The ARFHSN trustee roster, with seats and term dates.

*Found in October 2026 (Q-2):* the Endowment Fund Policy Statement (2012), the Scholarship Fund
Policy Statement (revised 2015) and the 2015 ARFECF by-laws; see the status note under Decision 3
and `design/bylaws/ARFECF-2015-and-the-fund-policies.md`.

**One number**
- The directory grace parameter (Decision 6). 90 days proposed; still unset.

**The open questions** are in `site/data/questions.yaml`, each with a status under D99 (open, for
now, in part, pending an act, parked) and, where one applies, the cluster whose single ask to its
owning body would answer it.

---

## Part 2 — decisions of 20–21 August 2026

The six above were the blocking set. Building since then surfaced twenty more, all
answered by David. They are recorded here in the same form, because a future session
that cannot see this conversation will otherwise re-open every one of them.

### Money and restricted funds — 21 August

| # | Decision | Answer | Note |
|---|---|---|---|
| 7 | Surplus on a restricted appeal | **To the receiving entity's general fund** | Lawful *only because* it is disclosed on the ticket before payment — see below. |
| 8 | Who authorises raising in another entity's name | **A purpose catalogue, with escalation** | Catalogue purposes are one-click by that entity's officer; a new purpose goes to its board and blocks publication. |
| 9 | Deductibility of a fundraising ticket | **Ticketed events are non-deductible entirely** | A contribution *beyond* the ticket receives nothing in return, so it is receipted separately as a deductible gift. |
| 10 | Contributor communications | **Four moments, then an annual statement** | Receipt · goal reached · funds transferred · purpose fulfilled. |

**Decision 7 needs its condition stated, or it becomes a problem.** A restricted gift may
only be spent as the donor was told. Sending surplus to the general fund is therefore
clean *if and only if* the donor was told that before they paid. The platform enforces it:
a money-taking event **cannot publish** unless the surplus and shortfall rules are printed
on the ticket page. Remove the disclosure and the same decision becomes a donor who gave
for an ambulance and funded something else without knowing.

**Decision 7 does not reach every entity, and the red team was right to catch it.** The
federation's answer — surplus to the receiving entity's general fund — holds only where a
general fund exists *and* that entity's own rules permit the move. **It cannot apply to
ARFECF**: By-Law 6.3.8 forbids diverting non-earmarked money between the Endowment and
Scholarship Funds, and ARFECF has no general fund to sweep into. For ARFECF purposes the
surplus stays in the fund it was given to, and the screen says why. A platform-wide rule
that quietly overrides an entity's own by-laws is not a rule, it is a bug.

**And authorisation is not uniform either.** A "designated officer" cannot stand in for the
**Endowment Fund Committee (6.3.4)** or the **Scholarship Fund Committee (6.4.4)**, which
hold *exclusive* expenditure authority over their funds. Decision 8's catalogue still holds;
the authoriser it names is per purpose, not per entity.

**Decision 9 was implemented as a split, not a flattening.** Treating the whole $100 dinner
ticket as non-deductible is the conservative call and it stands. But flattening a separate
$250 gift into the same treatment would cost the federation a deduction the donor is
genuinely entitled to, so the two are receipted separately — the ticket as a purchase, the
gift by the receiving entity.

### The family tree — 20–21 August

| # | Decision | Answer |
|---|---|---|
| 11 | Where the body of record lives | **Staged** — a governed mirror now; the platform becomes the record after one clean annual cycle |
| 12 | A correction changes a line a decision was made on | **Re-evaluated and flagged to the committee** — never auto-revoked |
| 13 | Who may propose a change, about whom | **Any member may propose anything** |
| 14 | Life events and the tree | **Every life event queues** for the committee |
| 15 | What ships in the public build | **Deceased real, living synthetic** |
| 16 | Does the tree decide By-Law 4.1.1 eligibility | **Evidence for a human decision**, never a verdict |
| 17 | Who sees living people in-platform | **All members see everything** |
| 18 | The tree's first job | **Lineage verification** for 4.1.1 and the Scholarship |

*Later (2 October 2026):* **D11**'s staging is superseded by **D69** (the Hub becomes the record after a parallel run). **D13** is confirmed by **D70** (members in current national standing). **D14**'s mitigations are amended by **D72** (one key for small changes, two for structural, clan stewards). **D17** is amended by **D71** (the living in full only inside one's own branch). See Part 5.

**13 and 14 together set the committee's workload**, so the queue triages itself rather
than reducing it: own-household life events clear first, structural changes wait for a
quorum, and an unsourced structural claim sorts to the *top* for dismissal rather than the
bottom for review. **17 is the widest exposure in the platform** — 28,000 members able to
browse living people's dates — and it is recorded as a deliberate choice matching how the
Google Group works today, not as an oversight.

### The tree viewer — 21 August

| # | Decision | Answer |
|---|---|---|
| 19 | The default view | **Hourglass** around a focus person; any node re-centres |
| 20 | Unapproved edits | **Shown in place, marked pending**, visible to everyone |
| 21 | How a sitting of work reaches the committee | **One bundle**, with its aggregate blast radius |
| 22 | Photos and documents | **Full media, per-item consent** |

*Later (2 October 2026):* P28 retires the hourglass as a view in favour of the plate (D68); whether **D19** is superseded is Q-270. **D20**'s pending marks move onto the plate (T2a). See Part 5.

*Later (3 October 2026):* **D77** answers Q-270: the plate (D68) is the default view on every surface, and the hourglass stays available as an alternative view. **D19** no longer sets the default; it is not superseded. See Part 6.

**Decision 22 was implemented with the consent held by the subject, not the uploader.**
Anyone may contribute a photograph; only the person in it decides who sees it. Deceased
people cannot consent, so their images are set by the committee on next-of-kin request with
the depositor's rights recorded. A minor's images run through the household and are
**re-asked of her directly at eighteen** — a choice her parents made at six does not
silently become hers at thirty.

### Presentation and privacy — 21 August

| # | Decision | Answer | Consequence |
|---|---|---|---|
| 27 | Tree viewer styling | **Keep the platform styling** | The tree stays box-and-line in the platform palette rather than adopting the book's oval plate grammar. Internal consistency wins over publication kinship. Fun Facts keeps the book palette, because it *is* a page of the book. |
| 28 | Living people's birth dates on the web | **Nothing for the living without sign-in** | Signed out, a living person shows a name and a position in the line and no dates at all. Deceased people are unaffected — already published in Shaheen 1982, and the heritage is almost entirely theirs. This diverges deliberately from the printed volume, which does carry them. |
| 29 | What to build next | **Finish the consolidation** — elections and events | 72 → 60 routes. |

*Later (2 October 2026):* **D27** is superseded by **D68** (the tree is drawn in the print book's plate grammar on every surface). **D28** is unchanged (D71). See Part 5.

### Program experience — 20 August

| # | Decision | Answer |
|---|---|---|
| 23 | Depth per program | **Tiered** — six flagship at full depth, thirteen to the same template |
| 24 | How far to simplify | **Consolidate hard** |
| 25 | The engagement spine | **A five-rung ladder** per program |
| 26 | Documentation shape | **Six section documents**, replacing the sprawl |

---

## Part 3 — the family tree as the platform's spine, 8 September 2026

Eleven decisions taken as the tree stopped being one programme among nineteen
and became the substrate the rest of the platform resolves people through.
Stated in full in `AFRP-Family-Tree-Integration.md`; recorded here because a
session that cannot see that document will otherwise re-open every one.

| # | Decision | Answer |
|---|---|---|
| 30 | Every member on the tree | **A node — and a node is never a lineage claim.** No membership decision reads it |
| 31 | Life events reaching the tree | **They queue** (confirms D14); R6 answers who may declare |
| 32 | The new edition of the book | **Carries no eligibility force** — 4.1.1 still points at Shaheen 1982 |
| 33 | Announcing a birth or baptism | **D22's pattern**: household consents, withdrawable, re-asked at eighteen |
| 34 | A step-parent joining a household | **Nothing** over the children in it until a standing holder names them |
| 35 | Two standing holders disagreeing | **The more protective answer wins** |
| 36 | Using the tree to reach people | **Members only, about their own branch** |
| 37 | The household and the tree | **Two models, one audited link** |
| 38 | The four branches | Education · Leadership · Heritage · Care; the tree is the **roots**, the Convention the **junction** |
| 39 | What "next" means on a branch | **Each branch declares a shape**; only an age ladder fires milestones |
| 40 | The Foundation and the Endowed Fund | **Funds** — shown on their branch, not joinable |

**D30 is the load-bearing one, and its point is negative.** By-Law 4.2.1's
Associate route exists precisely for people the genealogy cannot reach, and
5,819 people in the committee's file have no recorded parents. A rule making
membership depend on a line would deny exactly the people that route protects.
So the node carries no claim, and the platform has no way to render an
unattached one as a defect.

**D32 closes a circularity nobody had noticed.** By-Law 4.1.1 defines a Regular
Member by Shaheen 1982 — the book *is* the eligibility test. Had the new
edition inherited that force, platform data would write the book, the book would
be the by-law, and the by-law would decide membership from platform data.

**D35 closes a gap R6's ratification left open.** R6 said separated parents act
independently and neither needs the other's agreement — true for granting,
silent on disagreement. Without D35 a child-safety outcome would turn on who
clicked second.

**D34's cost is real and was accepted deliberately:** a step-parent cannot
collect their step-child until a standing holder names them. The grant is
therefore signposted from the household and camp screens rather than buried, so
it is not discovered at a locked gate.

**What D30–D40 did not settle**, and the platform keeps asking rather than
picking: the club attachment of a minor in two households (ratified as staying
**open**, By-Law 4.3.1 is silent), 4.1.1's three spouse questions, and adoption
— which has no decision at all, so an adoptive link is recorded, named
non-lineage, and nothing is inferred from it.

---

## Decision 41 — the prototype evidences stories, not rules
**Status: Adopted · stated by David Saah, 8 September 2026**

### The adopted wording
> The mockups have **most of the major stories** in them, with **significant
> logic and build gaps** that still need to be resolved. It is an amazing first
> pass repository.

### What it settles
The prototype is **strong evidence of a story and weak evidence of a rule.** It
captures most of the major user journeys walked end to end, and it is the origin
of the platform's design system. Where it is thin is the logic behind the
screens — the rules, the edge cases, the by-law mechanics — and in places it
disagrees with itself.

Precedence, highest first:

1. **The operative by-law texts** in `docs/bylaws/`.
2. **This register** and the named design documents.
3. **The prototype and the narrative mockups** — inspiration, not specification.
4. **The code** — evidence of what *is*, never of what *should be*.

*Since 29 September 2026:* the by-law texts now live at `design/bylaws/` in afrp-strategy, since AFRP-Portal was folded into it. The list above is left as written; `docs/bylaws/` in item 1 is the Portal-era path. (Pointer added 2 October 2026.)

### Why it had to be written down
`CLAUDE.md` told every session a module may be cut from a design document *"or
from the public prototype"*, and `08-OPEN-QUESTIONS.md` went further — *"the
prototype is the design record"* — using that to license building the remaining
screens without a design document. Both are corrected as of this decision.

**45 catalogue rows cite the prototype and no design document; 43 of them pass.**
Most are story rows — the front door, sign-in, recovery, the eighteenth-birthday
refresh — and the prototype is a fine source for those. The narrow work is
finding the rows whose assertion is really a *rule*, and giving each one a
rule's source.

### What it does not mean
The prototype is not discredited or downgraded. **This decision narrows what it
is cited *for*; it does not lower what it is worth.**

---

## Decision 42 — the Federation's strategic plan uses the four branches
**Status: Adopted · David Saah, 30 September 2026**

### The adopted wording
> The refreshed Federation strategic plan is organised on Decision 38's four
> branches — **Education · Leadership · Heritage · Care** — with the family tree
> as the roots and the Convention as the junction.

### What it settles
- One four-part framework across the platform and the strategic plan. The
  "rails (Education, Health, Legacy, Advocacy)" wording in the Strategic Planning
  Committee's minutes of 10 September 2026 is superseded by this decision, and
  so is the "Rails" paragraph of `AFRP-Delivery-Status.md`. "Rails" in
  `AFRP-Program-Architecture.md` §2 keeps its separate meaning: the six shared
  platform services.
- Outcome metrics for donors are reported per branch, using the five-rung
  ladder (D25) and stage-to-stage conversion.
- `AFRP-Strategic-Plan-Crosswalk.md` maps every element of the existing
  strategic plans onto the platform under this framework.

### What it does not settle
- Whether the Strategic Planning Committee and the Board adopt the framework
  for the Federation. This decision governs the design record and the draft
  that goes to the committee; the committee recommends and the Board decides.
- Where Ramallah Works sits: it is on no register.

---

## Part 4 — the site as the staging area, 30 September 2026

David approved `plan/SITE-OVERHAUL-PLAN.md` and its ten recommendations on
30 September 2026 ("this all sounds great, push the plan and build").

| # | Decision | Answer |
|---|---|---|
| 43 | Where discussion happens | **GitHub Discussions for the build team; the committee's Google Doc for the committee.** Each open question carries one Q-number used in both |
| 44 | Which strategy text is canonical | **The committee's Google Doc until the committee adopts the plan**; the site shows the latest draft and links to it |
| 45 | Leadership Ramallah's branch | **Education**, confirming D38 |
| 46 | The six shared services | **Called "shared services" on the site now**, and in the design record at the site plan's Phase 7. "Rails" no longer means two things |
| 47 | How site pages are written | **Markdown and data files in `site/`, rendered into `docs/` by `site/build.py`** |
| 48 | The prototype's framing | **Explained on the Prototype section first; re-framed onto the branches later**, as its own step |
| 49 | The 21 August Board Packet | **Kept as a dated record** in the Library |
| 50 | Names on new site pages | **Roles only.** No living person is named on a new narrative page |
| 51 | Internal history on public pages | **The lesson without figures or programme names** |
| 52 | The eight strategic goals | **Published as "distilled from the Federation's documents, for the committee to confirm"**; the committee's wording replaces them when it comes |

---

## Decision 53 — the family tree joins the Heritage branch
**Status: Adopted · David Saah, 30 September 2026**

### The adopted wording
> The family tree is part of Heritage.

### What it settles
- The Ramallah Family Tree sits on the **Heritage** branch, with the
  Preservation Project, Hathihe Ramallah and the Bookstore. It takes Heritage's
  shape, a cluster: no "next" step and no milestone invitations.
- This supersedes D38's placement of the tree as the **roots** beneath all four
  branches. The Convention stays the junction (D38).
- **D30 is unchanged**: every member still has a node on the tree, a node is
  never a lineage claim, and no membership decision reads it. Education,
  Leadership and Care keep drawing on the tree through that node; only the
  tree's place in the programme frame changes.
- D42's framing of the strategic plan follows: four branches and the junction.

### What it does not settle
- Nothing about lineage, eligibility or the tree committee's authority changes.
- AFRP-Hub's `programs/branches.py` still lifts the tree out as the roots; slice
  T1d in `plan/MASTER-PLAN.md` moves it.

---

## Decision 54 — how outside sources are taken in
**Status: Adopted · David Saah, 30 September 2026**

### The adopted wording
> Every source the project owner hands over (a drive folder, a document set, a website, a repository) goes through one intake process: inventory; one card per document; workflows written out step by step, with roles; a map against this record (match, extends, gap, conflict, answers, record against source) and the four branches; a report. The full report, with names and figures, is kept privately in the planning Project, outside this repository. Only role-level, figure-free changes that the project owner approves are written here. An intake proposes changes and never decides them: a new rule enters only as a decision in this register.

### What it settles
- The first intakes were ARFHSN (30 September 2026), ARFECF, the Federation's own folder and the officer archive (1 October 2026). Their corrections are in `AFRP-Delivery-Status.md` under "Site S3"; D55–D67 below are the decisions taken on their findings.
- A source folder named after a living person is cited by description, never by title.

---

## Decision 55 — a programme's holding entity is the fund that budgets it
**Status: Adopted · David Saah, 1 October 2026 · pending confirmation by the AFRP and ARFECF Boards**

### The adopted wording
> Until a Board says otherwise, each programme's holding entity is the fund that carries it in the Federation's approved budget. For 2026–27: Camp Ramallah, the Arabic Program, Project Hope, the Educational and Cultural Exchange Mission and the Scholarship are ARFECF's (the Educational Fund); the Magazine's assets and the camp land account are ARFECF's; Government Affairs, Congressional Outreach and the Day of Action are AFRP's (the General Fund); Women to Women is a sub-fund of ARFHSN; the Medical Mission is ARFHSN's (D62).

### What it settles
- Q-27 and Q-18. The "confirm" flags on programme plans cite the budget as their evidence.
- Receipts, books and the tax return for each programme follow its holding entity (D9).

### What it does not settle
- The Boards may move a programme; the register follows the next approved budget.
- *Since 2 October 2026:* the Preservation Project. Q-18 named it and D55's wording does not; which entity holds it is Q-277.

---

## Decision 56 — ARFHSN receipts the gifts it holds; AFRP collects as its agent
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> Gifts to the Medical Mission and the Human Services Network funds are ARFHSN's. ARFHSN is the receipting entity under D9; the Federation's giving pages collect such gifts as ARFHSN's agent and forward them without delay.

### What it settles
- Q-21. The receipt a donor gets names ARFHSN, the 501(c)(3), with its exempt-status language.
- The CPA's answer to Q-3 covers the same agency treatment for club dues; the two are to be put to the CPA together.

---

## Decision 57 — one club-share statement
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> Every amount a club pays or receives through a Federation or affiliate programme is recorded against the club on one statement: dues remitted (D1), camp rebates, Leadership Ramallah travel shares, event reimbursements, convention and Mid-Year settlements, grants to clubs, and co-funding of Care grants. Each programme sets its own terms. Every gift, from anyone, may carry a club attribution, and a co-funded grant lists each club's share.

### What it settles
- Q-30 and Q-25. One shared service on the funds ledger, not a rule per programme.
- Q-36 stays D1: the dues remittance rule is unchanged; the statement is where it shows.

### What it does not settle
- Whether clubs take gifts to their own purposes through the platform (B3) is still David's answer to give.

---

## Decision 58 — D3 amended: the Ramallah Foundation may hold seats on the Scholarship Committee
**Status: Adopted · David Saah, 1 October 2026 · conditional on the ARFECF Board amending the 2015 Scholarship Fund Policy**

### The adopted wording
> Decision 3 is amended: the Ramallah Foundation's role in the scholarship may include seats on the Scholarship Fund Committee. The seats exist only once the ARFECF Board amends the Scholarship Fund Policy Statement (2015) to provide them, by two-thirds of the Board as the policy requires. Until then the platform seats the committee as the 2015 policy reads: a chairman, the executive director, members chosen by the ARFECF Board and three members elected at the Annual Convention.

### What it settles
- Q-29. The conflict recorded under D3 on 1 October is resolved by amendment, not by refusal.
- Q-11. The members' vote for Scholarship Committee seats has its basis in the 2015 policy's three elected seats; the AFRP by-laws should still name what they elect (a drafting item for the Constitution Committee).

---

## Decision 59 — the host agreement is the rule for every Convention
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> Each Convention runs under a host agreement signed by the Federation and the host club before the Convention, recording the Federation's share, the holdback, the settlement date and each side's obligations. The platform records those terms on the event and produces the settlement statement. A change to the share goes from the Convention Innovation Committee to the Board; it does not happen on the floor.

### What it settles
- Q-34, and the source for the convention workflow's close step.
- The same shape serves the Mid-Year.

---

## Decision 60 — non-members may buy an Arabic class
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> A person who is not a member may register for an Arabic class at the public rate. The platform keeps a contact record for them (name, verified channel, consent) and not a membership. Members pay the member rate.

### What it settles
- Q-31, carrying the programme committee's decision of August 2026 into the platform.
- A non-member purchase is a new caller of the one payment door; the design note for the Arabic term covers it as a design change, not a parameter.

---

## Decision 61 — what historical programme records the platform takes
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> Camp Ramallah: past seasons come in as camper records (camper, household, club, year, attended) so retention and alumni reporting work; applications, consent forms, medical forms and travel forms never enter the platform, for past seasons or future ones. The health record stays a bought system outside the platform, as the camp workflow already says, and the platform holds only whether the form is on file. The Scholarship: past recipients only, as alumni records through the match queue (slice 9); applicant data and documents never enter (binding rule 2). Project Hope: past participants as alumni records (name, year, club); applications, consents and passports stay out and are deleted from the drive on the committee's rule. Leadership Ramallah and the Day of Action: past participants as programme alumni; applications, essays and résumés never enter. Future cycles of every programme apply in the platform.

### What it settles
- Q-32. The import plan per programme.

### What it does not settle
- How long the camp's paper and drive copies of past forms are kept, and who deletes them: a retention rule for the committee and the Board, outside the platform.
- **Amended the same day.** The first wording admitted camp documents under a retention rule; the project owner withdrew it: no medical, consent or travel document of a minor is stored in the platform.

---

## Decision 62 — the Medical Mission is a programme of ARFHSN
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> The Medical Mission is a programme of ARFHSN. ARFHSN's Board appoints the committee's chair and approves its spending. The Federation President convenes.

### What it settles
- Q-22, and the entity on the Medical Mission's register entry.

---

## Decision 63 — Care grants: how money leaves
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> A grant or partner project paid from a Care fund is approved by the holding entity's Board with a spending ceiling, paid on delivery with two signatories, and closed only when the receiving partner's signed agreement, a delivery confirmation and an inventory of any equipment are on record. No approval tiers apply until ARFHSN adopts a finance manual written for a volunteer board. The platform produces ARFHSN's six-monthly financial and operational report to the AFRP Board from the ledger and the grants register.

### What it settles
- Q-23, Q-24 and Q-26. The outbound side of giving, which the record did not hold.

---

## Decision 64 — AFRPWorks is on the Leadership branch
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> AFRPWorks, the Ramallah Jobs Initiative, is a programme on the Leadership branch beside the RBPN job board, held by AFRP.

### What it settles
- Q-39 and Q-12 ("Ramallah Works" in crosswalk row A8).

### What it does not settle
- Its owning committee and fee model, which the working group names.

---

## Decision 65 — AFRP carries advocacy; the affiliates never do
**Status: Adopted · David Saah, 1 October 2026 · the Legal Advisor to confirm the 501(c)(4) limits**

### The adopted wording
> Government Affairs, Congressional Outreach, the Day of Action and the Federation's public statements are AFRP General Fund activity. The platform refuses to charge any of it to ARFECF or ARFHSN.

### What it settles
- Q-38.

---

## Decision 66 — the shared drive is the archive of record
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> The Federation's shared drive is the archive of record. The platform holds its own registers and links to the drive for documents; it does not become the archive.

### What it settles
- Q-16 and crosswalk row C4.

---

## Decision 67 — a year-one baseline for outcomes
**Status: Adopted · David Saah, 1 October 2026**

### The adopted wording
> Each branch reports, for its first year, two or three counts that exist today: for example campers per club per year, scholars by track, mission volunteers, grants made and delivered, members by level. The five-rung ladder measures (D25, D42) follow from the first full year of platform data.

### What it settles
- Q-19. The first outcome report is not empty.

---

## Part 5 — the family tree module, 2 October 2026

Seven decisions taken by David on 2 October 2026 on how the tree looks, where its
record lives, who contributes, who sees the living, how the committee approves,
and what is built first. The design they are built on is
`AFRP-Family-Tree-Module.md` (P28); `AFRP-Family-Tree-In-Practice.md` (P27) is
amended to follow them. The earlier decisions they change keep their text above,
each with a pointer here.

---

## Decision 68 — the tree is drawn in the book's plate grammar
**Status: Adopted · decided by David, 2 October 2026 · supersedes D27**

### The adopted wording
> The tree is drawn in the print book's plate grammar on every surface.

### What it settles
- **Supersedes D27** ("keep the platform styling"). The plate grammar (one plate
  per tree, a trunk to the founder, ovals and rounded rectangles, bold and
  hairline limbs, the continuation marks) is specified in P28 §3.
- Each limb carries its grade, so the plate never looks more certain than the
  record is (P28 §3.2).

### What it does not settle
- Whether D68 also replaces D19 (the hourglass as the default view): P28 retires
  the hourglass as a view and D68 names only D27 (Q-270).
- The richer grade vocabulary (Q-267) and how plates are cut where the committee
  has not numbered a line (Q-269).

*Later (3 October 2026):* **D77** limits D68 as applied to D19: the plate is the
default on every surface, and the hourglass stays available as an alternative
view (Q-270 answered). See Part 6.

---

## Decision 69 — the Hub becomes the record of the tree
**Status: Adopted · decided by David, 2 October 2026 · supersedes D11's staging**

### The adopted wording
> The Hub becomes the record of the tree. During a parallel run of 30 to 60 days
> the Hub wins: the record keeper's edits arrive as GEDCOM imports through the
> diff preview and are applied as audited committee edits, with conflicts held
> for a decision and never merged. At the end of the run the external file is
> read-only and the Hub exports a GEDCOM backup every night under
> `tree:moderate`.

### What it settles
- **Supersedes D11's staging** (a governed mirror until one clean annual cycle).
  Q-258 (what a clean cycle means) is answered by this decision; P27's stage 4
  is replaced by the parallel run (P28 §4.3, slice T2d).
- The run's start, its length within 30 to 60 days and its end are the Family
  Tree Committee's dated acts.

### What it does not settle
- The terms on which the Federation holds the tree data (Q-201); the run's start
  should cite them (P28 §7, gate 3). *Later (4 October 2026):* **D87** puts the
  licence and account in the Federation's name and names who records the
  cadence and the terms; the run waits on those acts. See Part 7.
- A production database with backups (P28 §7, gate 1; `plan/MASTER-PLAN.md` §1d
  items 8 and 9). The run cannot start on staging.
- How many nightly exports are kept: every one is kept until the committee sets
  a retention.

---

## Decision 70 — members in standing contribute
**Status: Adopted · decided by David, 2 October 2026 · confirms D13**

### The adopted wording
> Members in current national standing may propose changes. No account exists
> for non-members to contribute.

### What it settles
- **Confirms D13** and bounds it: "any member" is a member in current national
  standing.
- Q-259 (a non-member asking for a change) is answered for the platform: there
  is no contributor account for a non-member.

---

## Decision 71 — the living in full inside one's own branch
**Status: Adopted · decided by David, 2 October 2026 · amends D17 and Q22 (answer 22 in `plan/QUESTIONS-FOR-DAVID.md`); D28 unchanged**

### The adopted wording
> A signed-in member sees the living in full inside their own branch: blood
> relatives sharing an ancestor no further back than a great-great-grandparent
> (out to second cousins), and the spouses of those relatives. Outside it a
> living person shows a name and a position on the plate only. D28 is unchanged.

### What it settles
- **Amends D17** ("all members see everything") and answer 22's "paid members
  see everything". The radius is a row on the rules register, set by this
  decision; a change is a dated act under a citation.
- Own branch runs along blood links only; a step or adoptive link never widens
  it (P28 §5).
- **D28 is unchanged**: signed out, nothing about the living.

### What it does not settle
- Whether relatives inside one's own branch see minors' dates; answer 22 says
  yes today (Q-268).
- Whether the radius is a great-great-grandparent (third cousins) or second
  cousins, as the wording's parenthesis says; the two disagree (Q-272).

*Later (3 October 2026):* **D76** answers Q-272: the great-great-grandparent
governs and the branch reaches third cousins; "(out to second cousins)" in the
wording above is an error. The wording is left as adopted. See Part 6.

---

## Decision 72 — the committee approves in tiers, with clan stewards
**Status: Adopted · decided by David, 2 October 2026 · amends D14's mitigations**

### The adopted wording
> One committee approval applies an own-household life event or a
> non-structural correction; two approvals from different committee members
> apply a structural change. The committee may appoint clan stewards, who
> pre-review and recommend for their clan and never approve.

### What it settles
- **Amends D14's mitigations**: every life event still queues (D14, D31); the
  quorum for structural changes becomes two keys from different committee
  members.

### What it does not settle
- The list of structural kinds: a rules-register row left unset, with P28 §6's
  list shown as a proposal (Q-264).
- Steward appointment, number and term (Q-263).
- A second holder of `tree:moderate`, without whom no structural change applies
  (Q-262); a committee's quorum in general is Q-52.

*Later (3 October 2026):* **D79** answers Q-262: the second holder is a Family
Tree Committee member seated by the committee's own act (FT2), chosen over
the project's lead (answer 31). See Part 6. **D81** answers Q-264: P28 §6's list
is the structural-kinds row's value, which the committee may amend by a dated
act.

---

## Decision 73 — membership and join is the first integration
**Status: Adopted · decided by David, 2 October 2026**

### The adopted wording
> Membership and join is the first integration.

### What it settles
- "Find yourself on the family tree" at join and renewal is built first (P28
  §4.4, slice T2e); skipping it is a complete answer and no membership decision
  reads the node (D30).

### What it does not settle
- The order of the other three: magazine and life events, directory and comms,
  Heritage (Q-265).

*Later (3 October 2026):* **D78** places magazine and life events (T2f) next;
the order of directory and comms and of Heritage stays Q-265. See Part 6. *Later (4 October 2026):* **D86** sets it: Heritage, then directory and comms. See Part 7.

---

## Decision 74 — the print pipeline is decided after the Mid-Year
**Status: Adopted · decided by David, 2 October 2026**

### The adopted wording
> How the 2027 print edition is produced is decided after the January 2027
> Mid-Year. Whatever produces it carries no eligibility force (D32).

### What it settles
- No print pipeline is designed or built before the Mid-Year; P28's renderer is
  reusable for print if this decision later chooses it.

---

## Part 6 — 3 October 2026

Five decisions taken by David on 3 October 2026 in the question walk-through:
the order of the build-ready slices (Q-278, in part), the tree's radius
(Q-272), the hourglass (Q-270), the next tree integration (Q-265, in part) and
the second key-holder (Q-262). The earlier decisions they read or limit keep
their text above, each with a pointer here. Two other answers the same day are
not decisions and change no rule: on Q-276 David keeps the hold on slice 5's
email provider and payment account for now, and on Q-70 he sends the contact
record's shape (P21 §11) and its consent basis to the Membership Committee and
the Legal Advisor before deciding. Both questions stay open.

Later the same day David answered four more questions, recorded as D80 to D83:
the hourglass is drawn in the plate grammar (Q-279), P28 §6's list becomes the
structural-kinds row (Q-264), the Senior Award was not retired and continues
(Q-163), and AFRP holds the Relief Fund (Q-109, in part; who approves a
transfer between the Board's votes and whether D63's closing records apply stay
open, and the deductibility text waits on the CPA).

---

## Decision 75 — the build-ready slices go first
**Status: Adopted · David Saah, 3 October 2026 · answers Q-278 in part**

### The adopted wording
> The build-ready slices Q-278 lists (CW1, FR1, DIR1, C1, C2, AR1, CR1 with
> AR2, SC1, SC4, SA1, MG2 and MG1) may be taken before T1d, the T2 series,
> B2b, slice 3 and slice 11, in that order. Within that order a session still
> takes the lowest unstarted, ungated slice, and never a closed gate. LT1
> follows P3 §9's gate column: its template register, letter rows, lists and
> drafts are built now, and only a send waits on slice 5.

### What it settles
- Q-278's order of the build-ready slices against the rows above SP0.
  `plan/MASTER-PLAN.md` §3.2's dated note becomes this order; the twelve
  opening prompts of 2 October 2026 may be pasted.
- P3 §9's two readings of LT1: the gate column governs. LT1's row in
  `plan/MASTER-PLAN.md` §2 and P3 §9's order line follow it. AR2's class
  welcome, SEL3's rows and SA5, which wait on LT1's register, wait on the
  register being built, not on slice 5; their sends and AR2's live money still
  wait on slice 5.

### What it does not settle
- Where the record-only slice R3 sits. David did not say; it stays with Q-278,
  which remains open on that point.
- Any slice's own gate, which stands: for example MG1's assisted door on
  Q-195 (*answered 4 Oct 2026 by D89*), and every send or live payment that waits on slice 5, which waits on
  Q-276.
- The order among T1d, the T2 series, B2b, slice 3 and slice 11 themselves,
  which stays as `plan/MASTER-PLAN.md` §2 and §3.2 have it.

---

## Decision 76 — D71's radius reaches third cousins
**Status: Adopted · David Saah, 3 October 2026 · reads D71; D71's wording is left as adopted**

### The adopted wording
> Decision 71's own branch is blood relatives sharing an ancestor no further
> back than a great-great-grandparent, which reaches third cousins, and the
> spouses of those relatives. The parenthesis "(out to second cousins)" in
> Decision 71's wording is an error; the great-great-grandparent governs.

### What it settles
- Q-272. The Rules Register's *Tree radius* row keeps its value,
  great-great-grandparent, and its note of the disagreement points here.
- P28 §2 and §5 read the radius as reaching third cousins. A journey is
  proposed for T2a: a living third cousin's dates are shown (P28-J19).

### What it does not settle
- Whether relatives inside one's own branch see minors' dates (Q-268).
- A later change of the radius, which is a dated act of the Board or the
  Family Tree Committee under a citation (D71; P28 §2).

---

## Decision 77 — the hourglass stays as a second view
**Status: Adopted · David Saah, 3 October 2026 · limits D68 as applied to D19**

### The adopted wording
> The plate (Decision 68) is the tree's default view on every surface. The
> hourglass around a focus person (Decision 19) stays available as an
> alternative view. Decision 68 does not retire the hourglass, and Decision 19
> no longer sets the default view.

### What it settles
- Q-270. D68 is limited as applied to D19: D68 makes the plate the default and
  does not remove the hourglass; D19 stands for the hourglass as a view and no
  longer for the default.
- T2a: the hourglass route is kept as a second view, and where the hourglass
  was the default the plate now opens. The redirect reads "plate by default,
  hourglass available" (P28 §3.2).

### What it does not settle
- Whether the hourglass is redrawn in the plate grammar or keeps its built
  style. The record is silent; it is David's to say. (Q-279)
- The grade vocabulary (Q-267) and how plates are cut where the committee has
  not numbered a line (Q-269).

*Later (3 October 2026):* **D80** answers Q-279: the hourglass is drawn in the
plate grammar, with the same shapes and line weights.

---

## Decision 78 — magazine and life events is the next tree integration
**Status: Adopted · David Saah, 3 October 2026 · answers Q-265 in part**

### The adopted wording
> After membership and join (Decision 73), the next integration of the family
> tree is magazine and life events.

### What it settles
- T2f's place: it comes next after T2e among the integrations. SP0's order
  line and P28 §14's order line name T2f next.

### What it does not settle
- The order of directory and comms (T2g) and Heritage (T2h) after it. Q-265
  stays open on that point. *Later (4 October 2026):* **D86** sets it:
  Heritage (T2h), then directory and comms (T2g).
- Where a Heritage item's file lives (Q-260). Oral-history consent (Q-189,
  Q-261).

---

## Decision 79 — the second holder of `tree:moderate` is a committee member the committee seats
**Status: Adopted · David Saah, 3 October 2026 · the seat is filled by the Family Tree Committee's act (FT2)**

### The adopted wording
> The second holder of `tree:moderate` that Decision 72 requires is another
> member of the Family Tree Committee, seated by the committee's own act (FT2).

### What it settles
- David chose this over the project's lead (the pack's option A, from answer 31). The grant is made by name on the Roles screen after the committee's act and is never seeded (answer 28); until it is made, a structural item records its first key and waits (D72, T2c).
- Q-262. P28 §7 gate 2 and T2c name this decision: T2c builds the two-key path
  now, and a structural change applies in practice once the committee has
  seated the member and the grant is entered.

### What it does not settle
- Which member, and when the committee acts (FT2, P27 §4.2).
- A committee's quorum in general (Q-52), stewards (Q-263) and the list of
  structural kinds (Q-264).
  *Later the same day:* D81 sets the list (Q-264).
- Whether the project's lead also holds the role later, under answer 31.

---

## Decision 80 — the hourglass is drawn in the plate grammar
**Status: Adopted · David Saah, 3 October 2026 · answers Q-279; reads D77 with D68**

### The adopted wording
> The hourglass kept as an alternative view by Decision 77 is drawn in the
> plate grammar of Decision 68, with the same shapes and line weights as the
> plate.

### What it settles
- Q-279. T2a redraws the hourglass route in the plate grammar (P28 §3, §3.2)
  and keeps it as the second view D77 keeps; the plate stays the default.

### What it does not settle
- The grade vocabulary (Q-267) and how plates are cut where the committee has
  not numbered a line (Q-269), as under D77.

---

## Decision 81 — the structural kinds of tree change
**Status: Adopted · David Saah, 3 October 2026 · answers Q-264; sets D72's parameter; the Family Tree Committee may amend it by a dated act**

### The adopted wording
> The list of structural kinds proposed in `AFRP-Family-Tree-Module.md` §6
> becomes the value of the Rules Register's *Structural kinds* row, the
> parameter Decision 72 left unset: a parent link added, changed or removed;
> two records merged; a branch moved; a person removed or marked removed; a
> clan assignment changed; a sex recorded differently; a link's grade raised.
> Every other change is non-structural. The Family Tree Committee may amend
> the list by a dated act.

### What it settles
- Q-264. The Rules Register's *Structural kinds* row takes the list as its
  value. P28 §6's "proposal" and "DRAFT interim" labels are removed, and T2c's
  gate is no longer held by Q-264.

### What it does not settle
- Stewards (Q-263); the grade vocabulary that "a link's grade raised" reads
  (Q-267). A structural change still applies in practice only once the second
  holder of `tree:moderate` is seated and granted (D79, FT2).

---

## Decision 82 — the Senior Award was not retired and continues
**Status: Adopted · David Saah, 3 October 2026 · answers Q-163; recorded by the project owner**

### The adopted wording
> The Outstanding High School Senior Award was not retired. It continues. The
> programme register's "retired 31 Aug 2026" status is corrected.

### What it settles
- Q-163. The programme register's status line and the conflicts-table row
  below follow this decision.
- YL6 switches on in principle; it still waits on what its row also names: the
  body that runs the award (Q-164) and a budget line before any money line
  (D55), with past applicants' files under Q-76.
- Q-20 (a successor) falls away: there is no gap to fill while the award
  continues.

### What it does not settle
- Which body runs the award (Q-164; the register's organiser question).
  *Later (4 October 2026):* **D85** answers Q-164: the Scholarship Fund
  Committee. Who
  scores (Q-117). The budget line that names its fund (D55). Past applicants'
  files (Q-76).

---

## Decision 83 — AFRP holds the Relief Fund
**Status: Adopted · David Saah, 3 October 2026 · David's decision for the design record · answers Q-109 in part · the deductibility and receipt text waits on the CPA (D9)**

### The adopted wording
> The Relief Fund is held by AFRP. The deductibility statement and receipt
> text for gifts to it follow Decision 9 and wait on the CPA.

### What it settles
- Q-109's entity part. P23 §3's holding-entity row takes AFRP; P9's fund
  register (FR1), P11 §4 and P22's Relief Fund liability (CV7) follow. The
  programme register's `relief-fund` entry takes AFRP as its entity.
- The slices whose gate was Q-109 for posting (CG5, RL1, RL3, RL4, CV7) lose
  that gate. Any receipt's deductibility text still waits on the CPA.
- Q-208 and the other questions that waited on the entity now read AFRP: a
  public purpose for the fund is for AFRP's Board under D8.

### What it does not settle
- Who approves each transfer between the Board's votes, and whether Decision
  63's closing records apply to the fund. Both stay open under Q-109.
- The books. In practice (research, 2 October 2026) the account is booked
  inside ARFECF, with AFRP owing it. This is recorded as a reconciliation item
  in the conflicts table below: the books follow D83, or the Boards revisit.
- The deductibility and receipt text (the CPA, D9). Q-207 (the charities
  list), Q-180 (club drives), Q-126 (the per-registration amount), Q-232
  (settling the "due to" accounts).

---

## Part 7 — 4 October 2026

Four decisions taken by David on 4 October 2026 in the question walk-through:
the scholarship conflict-of-interest rule (Q-273), recorded in D58's
conditional form, the body that runs the Senior Award (Q-164), the order
of the tree's last two integrations (Q-265's remainder), and who holds the
tree's master file (Q-201). A fifth, D88, answers Q-260 for now: drive-held
documents are not served to members; Q-260 stays open for the lasting answer.
A sixth, D89, answers Q-195: two doors for a life event, the household's own
and the correspondent's, and it makes an exception to D33's consent pattern.
A seventh, D90, retires the Emerging Leaders entry (Q-178). An eighth, D91,
records Senior Living as the Ramallah Foundation's project (Q-203), pending
the two Boards' confirmation. A ninth, D92, puts a club's gift to the home
through the Federation on the club's statement (Q-205). A tenth, D93, requires
a written, scoped release for every oral history (Q-189). An eleventh, D94,
extends D61 and reads it at a future cycle's door, for now (Q-118).

Later the same day David took four more together, to clear the way for the
build (D95 to D98): deaths keep the family contact's approval (D95, limiting
D89); SC1 and SC4 are built now and LT1's register goes before CR1 with AR2
(D96); clan books by standing with no approval step (D97, Q-200); and what
T2f and T2e do where the record is silent (D98).

Last, David approved the review of everything designed to date (D99): the
platform primitives first (P29), the slice queue reshaped, the open questions
triaged, a generated "Rules in force" view, and the process tooling. P26 §1.4 and §3.2, the scholarship specification's §3 and
the by-law notes that cited Q-273 keep their text, each with a pointer here.

---

## Decision 84 — scholarship conflicts are disclosed, and only the household refuses
**Status: Adopted · David Saah, 4 October 2026 · answers Q-273 · conditional on the Scholarship Fund Committee adopting it as its conflict policy (ARFECF By-Law 6.4.4; 6.4.6 if it is adopted as a rules amendment)**

### The adopted wording
> A reviewer on the Scholarship Fund Committee who is related to an applicant
> discloses the relationship by degree, and the disclosure is acknowledged on
> the record of the decision; only a reviewer in the applicant's own household
> is refused. The specification's three-degree block (August 2026) is
> withdrawn. Until the committee adopts this as its conflict policy, the
> platform applies it as built in slice 4b and labels it pending adoption.

### What it settles
- Q-273. David's correction of 8 September 2026 (P26 §1.4, §3.2) now has a
  D-number; P26 and the specification's §3 cite D84 in place of "not yet a
  D-number".
- The pattern: like D58, the rule is the design record's, and the committee's
  exclusive authority over its fund (ARFECF 6.4.4) is kept by the condition.
- The Hub: no build change. Slice 4b already applies the rule; the
  "pending adoption" label is the only thing it lacks, for a build session to
  add with the Hub record's next pass.

### What it does not settle
- Whether, when and by what act the Scholarship Fund Committee adopts it, and
  whether that act is a rules amendment needing two-thirds of the ARFECF Board
  under 6.4.6 (P26 §3.2's reading). The record holds no such act.
- The rubric and who scores (Q-117). The committee's seats (D58). Who approves
  the year's awards (Q-161).

---

## Decision 85 — the Scholarship Fund Committee runs the Senior Award
**Status: Adopted · David Saah, 4 October 2026 · answers Q-164 · reads D82**

### The adopted wording
> The Outstanding High School Senior Award, which continues under Decision 82,
> is run by the Scholarship Fund Committee, as the programme register first
> held it ("the Scholarship Committee, on an award track"). The Leadership
> Ramallah committee's running of the award from 2013 to 2020 is kept on the
> register as its history.

### What it settles
- Q-164. The programme register's organiser is the Scholarship Fund
  Committee; the Leadership Ramallah committee's years stay as history.
- YL6's body and LT-P-YL1's: the award's decision item is the Scholarship
  Fund Committee's (P25 §5.1). YL6 no longer waits on Q-164.
- The conflicts-table row on the award's organiser: the record's body is
  kept, and the practice of 2013–2020 is history, not a rule.

### What it does not settle
- The budget line that names the fund before any money line (D55). In
  practice the award was paid from the Education Fund on the Leadership
  Ramallah chair's request; whether the line now sits in the Scholarship
  Fund, under the committee's authority in ARFECF By-Law 6.4.4, or elsewhere
  is for the ARFECF Board's budget.
- The committee's own act taking the award on. No such act is on file.
- Who scores and on what sheet (Q-117); past applicants' files (Q-76);
  whether the award is announced at the Convention (the register's earlier
  text) or by newsletter (practice); whether D84's conflict rule reaches the
  award's reviewers.

---

## Decision 86 — Heritage comes before directory and comms
**Status: Adopted · David Saah, 4 October 2026 · answers the rest of Q-265 · completes D78**

### The adopted wording
> After magazine and life events (Decision 78), the family tree's remaining
> integrations are built in this order: Heritage, then directory and comms.

### What it settles
- Q-265, in full: the order after D73 is magazine and life events (T2f, D78),
  Heritage (T2h), then directory and comms (T2g). SP0's order line and P28
  §14's order line follow.
- FT5 (oral-history consent), which follows T2h, can come before T2g.

### What it does not settle
- Where a Heritage item's file lives (Q-260): T2h runs on drive links until it
  is answered, and no item's file is stored in the Hub before then.
  *Later the same day:* **D88** answers Q-260 for now: not served; the links
  are for the committee's seats only.
- Oral-history consent (Q-189, Q-261). Each slice's own gates, which stand.
- Where the T2 series sits against the build-ready slices, which D75 sets.

---

## Decision 87 — the Federation holds the tree's master file
**Status: Adopted · David Saah, 4 October 2026 · answers Q-201 · the Family Tree Committee's acts and the AFRP Board's minute it calls for are not yet on file**

### The adopted wording
> The licence and the account that hold the tree's master file and its cloud
> copy are held in the Federation's name. The Family Tree Committee records,
> as dated acts, who may open the file and the export cadence into the Hub;
> the AFRP Board records, by minute, the terms on which the Federation holds
> the record keeper's compilation and the original author's work. Decision
> 69's parallel run starts only after both are on file and cites them. After
> the run, the external file is read-only (Decision 69).

### What it settles
- Q-201: whose licence and account (the Federation's), and who records the
  cadence (the committee) and the terms (the Board).
- FT1's licence-holder and account rows take "the Federation (D87)"; the
  key-holder and cadence rows, and the terms, take values only from the
  committee's acts and the Board's minute, and read "not stated" until then.
- P28 §7 gate 3 has its route: it clears when both are on file, not before.

### What it does not settle
- When the licence and account move, and who in the Federation's name holds
  the account (a seat, not a person). The record holds no act on either.
- The terms themselves, which are the Board's. Whether the Legal Advisor
  reviews them is not stated.
- P28 §7 gate 1 (production with backups; `plan/MASTER-PLAN.md` §1d items 8
  and 9; Q-15). How many nightly exports are kept (D69).

---

## Decision 88 — for now, drive-held documents are not served to members
**Status: Adopted for now · David Saah, 4 October 2026 · answers Q-260 for now; Q-260 stays open for the lasting answer · D22 and D66 unchanged**

### The adopted wording
> For now, a document or media item held on the shared drive (Decision 66),
> such as a clan book or an item attached to a tree node, is not served to
> members. The platform lists it in its own registers and gives its drive
> link to the seats of the committee that holds it only. No drive share link
> is given to a member, and the platform stores no copy. This holds until
> David or the Board decides how such items are served (Q-260).

### What it settles
- How FT3 and T2h are built now: FT3 lists the clan books and serves none;
  T2h shows a node's items from the archive index and links them for the
  committee's seats only. Neither stores a file in the Hub.
- P27 §5.2's interim ("lists the books and serves none") is now the rule,
  not a refusal waiting on a question.

### What it does not settle
- The lasting answer to Q-260: serving from the drive inside the sign-in
  boundary (the pack's option A), or copying into platform storage, which
  would need D66 amended (option B). Q-260 stays open.
- Clan-book access by standing (Q-200) and living dates in the books (Q-202).
  Oral-history consent (Q-189, Q-261). Download and print, refused wherever a
  living person appears (P27 §5.2).
- Which seats count as "the committee that holds it" for an item with no
  committee title on the archive index. The index's committee-title field
  names it; an item without one is linked to no seat.

---

## Decision 89 — two doors for a life event: the household's and the correspondent's
**Status: Adopted · David Saah, 4 October 2026 · answers Q-195 · makes an exception to D33's consent pattern for the Magazine's assisted door; D22 otherwise unchanged**

### The adopted wording
> A household may submit its own life event or announcement to the Magazine.
> A Magazine correspondent, or the editor, may also submit one on a
> household's behalf, and the correspondent's attestation that the family
> agreed is enough for it to print. This covers every kind of life event the
> Magazine prints: weddings, births, graduations and deaths. The attestation
> is recorded with the entry: who entered it, on what date, and from what. For
> a birth this is an exception to Decision 33's pattern, under which the
> household consents; Decision 33 otherwise stands.

### What it settles
- Q-195. MG1's assisted door opens: an assisted submission with an
  attestation on record prints in the next issue's section without the
  household being asked. The household's own door (proof-and-confirm, P24
  §3.2) stays as it is.
- P24 §3.2's "pending until the household's consent act is on record" now
  applies only to an assisted submission with no attestation recorded.
- For a death, the attestation stands as the family's approval for what the
  Magazine prints.

### What it does not settle
- R34's gate for recording a death on the member record and the tree (T2f),
  which D89 does not change: the Magazine may print a death on an attestation
  before or without the tree recording it. *Later the same day:* **D95**
  takes deaths out of D89: a death prints only on the named family contact's
  approval, as slice 7 built it.
- Withdrawal. Under D22 a consent is withdrawable and a minor's is re-asked at
  eighteen; what a household or the grown child can withdraw of an attested
  item, beyond the printed issue that cannot be recalled (D33; R27), is not
  stated.
- The obituary fee (Q-193). Keeping unconfirmed submissions (Q-76). Who holds
  the correspondent seat (the Club Experience Plan §3.4; C1).

---

## Decision 90 — Emerging Leaders is retired from the register
**Status: Adopted · David Saah, 4 October 2026 · answers Q-178 · the Strategic Planning Committee to reflect it in its draft**

### The adopted wording
> The programme register's Emerging Leaders entry is withdrawn: no Federation
> programme of that name or age band is found in any source. The Leadership
> branch is entered at whichever of its programmes a person first takes part
> in (P25 §2.2, a design choice; Decision 39 makes the order a suggestion,
> never a prerequisite). The Youth Summit's history is carried on the Day of
> Action's entry.

### What it settles
- Q-178. The `emerging-leaders` entry leaves `site/data/programmes.yaml`; the
  Leadership branch's summary, P25 §2.2, the architecture notes and the
  Family Tree Integration note's D38–D39 text stop naming an entry rung.
- The Hub follows in slice T1e (`plan/MASTER-PLAN.md`): the `els` programme
  leaves the seed and the Leadership ladder, its plan and journey JP-039 with it.
- The committee's draft: the branch-table note loses Emerging Leaders (the
  crosswalk's change list, item 4).

### What it does not settle
- The Young Leader Committee: its composition (Q-179), whether it and the
  Leadership Ramallah committee are one body (Q-175), its drive (Q-180).
- How a row already seeded for the programme leaves a live database. The
  record does not say; T1e's build session reports it.

---

## Decision 91 — Senior Living is the Ramallah Foundation's project
**Status: Adopted · David Saah, 4 October 2026 · answers Q-203 · pending confirmation by the AFRP and ARFECF Boards**

### The adopted wording
> The Senior Living Project is the Ramallah Foundation's capital project, not
> a Federation programme. The Foundation is held on the partner register under
> Decision 3's shape; the Federation's part (communications, gifts passed
> through, and any Convention-voted budget grant) is recorded as agreements
> with it. The register entry becomes a partner project on the Care branch.

### What it settles
- Q-203, for the design record. RL5 builds on the Foundation's page: its
  registry row (D3-B, D40) carries the Federation's part. P23 §9.7's marks
  stand: Program Architecture §3 and §6's capital campaign, and JP-032 for
  Senior Living, are unoperated.
- The programme register's `senior-living` entry stays on the Care branch as
  a partner project, not a Federation programme.

### What it does not settle
- The two Boards' confirmation, which the status names; until it is on file
  the decision is the design record's, as D83 was for the Relief Fund.
- Receipting gifts passed through (Q-204). A club's gift to the home (Q-205;
  *later the same day, D92*).
  A written agreement with the Foundation (Q-206).

---

## Decision 92 — a club's gift to the Foundation's home is a club-statement line
**Status: Adopted · David Saah, 4 October 2026 · answers Q-205 · with the Council of Chapter Club Presidents**

### The adopted wording
> A club's gift to the Ramallah Foundation's home made through the
> Federation's pass-through purpose is recorded on the club's statement under
> Decision 57, with the club as donor and its recognition request carried to
> the Foundation. A gift a club makes directly to the Foundation is outside
> the platform.

### What it settles
- Q-205. RL6 is no longer gated on it: the club-donor line on the club
  statement with the recognition request builds with C3. P20-I8 meets once
  the pass-through purpose is published, which waits on Q-204.

### What it does not settle
- Receipting the gift and publishing the purpose (Q-204). Whether the
  recognition is a benefit the receipt must disclose (Q-248). Q-203's
  Boards' confirmation (D91).
- The Council of Chapter Club Presidents' view, which the question names; no
  act of the Council is on file.

---

## Decision 93 — oral histories need a written, scoped release
**Status: Adopted · David Saah, 4 October 2026 · answers Q-189 apart from the release's text · the wording pending the Legal Advisor and the Preservation committee · applies D22**

### The adopted wording
> Decision 22 applies to oral histories through a written release, signed by
> the narrator and held on the drive, granting each scope separately
> (community archive, public web, print, research, excerpts), each defaulting
> to no. A recording without a release on file is shown to the Preservation
> committee's seats only. A recording made before this decision under a spoken
> permission is treated the same until the narrator signs a release.

### What it settles
- Q-189, apart from the release's text. FT5 builds as P27 §6.2 has it: the
  consent row per recording with the five scopes defaulting to no. P27 §6.3's
  interim for existing recordings (committee seats only) becomes the rule.
- P27-J09 to J11 are no longer held by Q-189; they meet once FT5 lands.

### What it does not settle
- The release's wording, which the Legal Advisor drafts and the Preservation
  committee adopts. FT5 builds the consent row now; no item reaches a scope
  until a signed release on the adopted form is on file.
- Living third parties named in a recording (Q-261): their passages stay
  withheld until it is answered.
- A narrator who has died before signing. The record does not say whether
  next of kin may sign; P27 §6.2's next-of-kin path covers withdrawal, not a
  first grant.

---

## Decision 94 — for now, D61 extended to the Exchange Mission and the Fellowship, and read at the door
**Status: Adopted for now · David Saah, 4 October 2026 · answers Q-118 for now · pending ARFECF Board confirmation; Q-118 stays open for the lasting answer · reads D61**

### The adopted wording
> For now, Decision 61 is extended: the Educational and Cultural Exchange
> Mission and the Palestine Fellowship take past delegates and fellows as
> programme alumni (name, year, club where known); past applications, essays,
> recommendation letters, proposals, CVs, passports, photo ID, consent and
> release forms and media waivers never enter. Decision 61's "never enter"
> governs past cycles; a future cycle's applicant may type a statement and
> upload documents at the platform's door, held under the retention clock.
> Passports, photo ID, consent, release, medical and travel forms never enter
> for any cycle. From a selection discussion the committee keeps a summary
> per applicant, the votes and a decision note; no note of an applicant's
> political views is kept.

### What it settles
- How SEL2 is built now: the document upload at a future cycle's door opens,
  under the retention clock. P12 §2.2's reading is the rule for now, and the
  Exchange Mission's extension in P12 is no longer only a design choice.
- What a selection committee keeps: a summary per applicant, the votes and a
  decision note; no free-text note of an applicant's political views (with
  AD1).

### What it does not settle
- The lasting answer and the ARFECF Board's confirmation; Q-118 stays open.
- Retention periods (Q-76). Scoring (Q-117). Q-115 and Q-116.
- If the lasting answer reads "never enter" as every cycle, what becomes of
  documents uploaded under this decision. The record does not say.

---

## Decision 95 — a death prints only on the family contact's approval
**Status: Adopted · David Saah, 4 October 2026 · limits D89 · keeps R34 and slice 7's built hold**

### The adopted wording
> Decision 89's correspondent route covers weddings, births and graduations.
> A death printed in the Magazine needs the approval of the named family
> contact, as slice 7 built it: the person who reported the death cannot be
> that contact, and no role overrides the hold. A correspondent may still
> enter a death on a family's behalf; it waits for the family contact.

### What it settles
- The conflict between D89 and slice 7's built hold: the hold stands, and MG1
  changes nothing in it.

### What it does not settle
- The obituary fee (Q-193). R34's gate on the tree side (T2f).

---

## Decision 96 — SC1 and SC4 are built now; LT1's register goes before CR1 with AR2
**Status: Adopted · David Saah, 4 October 2026 · reads D75**

### The adopted wording
> SC1 and SC4 are built in D75's order now, behind the Q-33 setting that
> already governs the Selection Committee's rules; the governance gate of
> `plan/MASTER-PLAN.md` §1d does not hold them. LT1's template register,
> letter rows, lists and drafts are taken before CR1 with AR2, so the class
> welcome is not left unbuilt; LT1's sends still wait on slice 5.

### What it settles
- Two of the items the build-prompt check of 4 October left for David: the
  order within D75 is CW1, FR1, DIR1, C1, C2, AR1, LT1 (register only), CR1
  with AR2, SC1, SC4, SA1, MG2, MG1.

### What it does not settle
- Q-33 itself. Where R3 sits (Q-278). Slice 5 (Q-276).

---

## Decision 97 — clan books by standing, with no approval step
**Status: Adopted · David Saah, 4 October 2026 · answers Q-200 · within D71 and D88**

### The adopted wording
> Clan books are served to signed-in members in good standing within Decision
> 71's limits, with no approval step, once a book can be served inside the
> sign-in boundary (Decision 88 holds them back for now); a book carrying
> living people's details beyond a name and a position is not served by
> standing (Q-202). Until then access stays with the project's own process,
> which the Board records by minute with its test.

### What it settles
- Q-200 for the platform: FT3 builds access by standing and no approval step.

### What it does not settle
- The Board's minute of today's practice, which the wording asks for and is
  not on file. Q-202. When books can be served (D88; Q-260).

---

## Decision 98 — T2f and T2e where the record is silent
**Status: Adopted · David Saah, 4 October 2026 · reads P28 §5 and §8**

### The adopted wording
> T2f builds nothing the record does not state. Its session reports what
> slices 7 and 7b built, writes the slice's journeys, and leaves anything
> further NOT BUILT, naming P28 §8. At join and renewal (T2e), a person who
> is not yet a member is shown no living person's details on the tree beyond
> what Decision 28 already allows a signed-out visitor.

### What it settles
- Two of the gaps the T2 prompt check of 4 October found: T2f's scope and
  what a join applicant sees of a living relative.

### What it does not settle
- What, if anything, T2f should add to slice 7's hold. Prompts for FT1, FT2,
  FT3 and FT5, which are to be written later.

---

## Decision 99 — simplify, abstract, expand: the primitives first, the queue reshaped, the questions triaged
**Status: Adopted · David Saah, 4 October 2026 · from the review of everything designed to date (`AFRP-Hub/ai-memory/cowork/review/2026-10-04-simplify-abstract-expand.md`)**

### The adopted wording
> 1. The shapes the design notes draw again and again are built once, as the
>    platform primitives of `AFRP-Platform-Primitives.md` (P29), before the
>    slices that would otherwise each build their own: A2 (the refusal and the
>    snapshot) and PR0 (the act and append-only record, the scoped parameter
>    and authority row, the dated-role base, the record on file, the clock),
>    then each remaining primitive in the first slice that needs it.
> 2. The slice queue is reshaped: done rows move to an appendix; rows that
>    build one mechanism are merged onto it; a row whose gate holds only one
>    action is a build row; slice 5 is split into 5a (email) and 5b (payments);
>    R3, T2-R, T1d and T1e are one record slice; rows A2, PR0, PT1, CY1, CY2 and
>    CM1 are added.
> 3. The open questions carry a status (open, for now, in part, pending an
>    act, parked); questions a decision already answers are closed with it;
>    questions no slice or gate cites are parked; the rest are grouped into
>    clusters, each put to its owning body as one ask.
> 4. The register stays the history. A generated "Rules in force" view states
>    the current rule per topic with the decisions behind it, and a generated
>    list names every decision waiting on a body's act. A build session reads
>    those.
> 5. Process tooling (PT1) generates the counts and records the registry now
>    only checks, renders each round's findings from one file, and generates
>    journey stubs from the design notes; the strategy site publishes through
>    a script that fails on a build error.
> 6. A slice that only builds a register or a form, and touches none of
>    voting, payments, by-laws, authority, the tree, scholarships, the
>    directory or `core.decision`, runs a lighter loop: build, one combined
>    attack that includes its fix layer, and the hygiene lints. Every other
>    slice keeps the full four steps.

### What it settles
- How the Hub is built from here: P29 is the design note for the shared
  pieces; `plan/MASTER-PLAN.md` carries the reshaped queue and the order.
- Item 6 relaxes the written four-step rule for register and form slices
  only, by David's decision.

### What it does not settle
- Any binding rule, which stands unchanged; any decision's content.
- The email provider for slice 5a and the staging database's survival past
  5 October 2026, which wait on David.
- Each primitive's detail, which its building slice settles within P29.

---

## Two items for board confirmation rather than decision
These are settled in the design and merely need the board to say so out loud:

1. **Exhibitor and press credentials** are modelled as **non-attendee credentials**, so the
   membership-mandatory rule stays absolute. This is current practice; making it explicit prevents
   it being argued later.
2. **Convention deficit responsibility** is read from the Convention Contract, and the screen says
   plainly where the contract is silent rather than assigning the loss by assumption.

---

## Conflicts between practice and the record found in the research round of 2 October 2026

**Recorded 2 October 2026 · no decision's text is changed here.** The second research
round (five reports under D54: Education, Leadership, Heritage, Care and the Federation
itself) read the Federation's drive, mail, public pages and filings against this register,
the by-laws and the named design documents. Where the sources show practice contradicting a
decision or a by-law, the conflict is recorded below with both sides cited and a question
number. Under D41 the by-law text wins over this register, and this register and the design
documents win over practice; a research finding is evidence of practice and never a rule.
Every row is for the owner named to settle; nothing in the platform changes until it is.
The questions are in `site/data/questions.yaml` (Q-158 onward; additions to earlier rows are
marked "research, 2 Oct 2026").

| What the record says | What the sources show | Question | Owner |
|---|---|---|---|
| D13 (any member may propose anything), D14 (every life event queues for the committee), D17 (all members see everything); the programme register's "the Family Tree Committee decides every change". **Since 2 Oct 2026:** D70 confirms D13 for members in current national standing; D72 amends D14 (one committee key for a small change, two different keys for a structural one, clan stewards who never approve); D71 amends D17 (the living in full only inside one's own branch). These settle the platform's rule; today's approval of access stays Q-200 | One project lead receives, approves and applies every change from a form or email; the committee has two members; the master file lives in a commercial desktop genealogy product not held in the Federation's name, shared by personal invitation; the clan books are PDFs behind an access request the lead approves "by agreement with the board", a rule asserted and not minuted | Q-200 | AFRP Board · Family Tree committee · David |
| D11 (a governed mirror now; the platform becomes the record after one clean annual cycle); the programme register's "GEDCOM database". **Since 2 Oct 2026:** D69 supersedes D11's staging: the Hub becomes the record after a parallel run of 30 to 60 days, the external file then read-only, with a nightly export; the run waits on Q-201 (now carrying who owns the tree data and on what terms) and a production database (P28 §7) | The body of record is a desktop genealogy file not held by the Federation, with a cloud copy; no licence holder, export cadence or second key-holder is written | Q-201 (answered by D87, 4 Oct 2026: the licence and account move into the Federation's name; the committee's acts and the Board's minute on terms are not yet on file) | Family Tree committee · David · Executive Director |
| D28 (nothing for the living without sign-in). **Since 2 Oct 2026:** D71 leaves D28 unchanged and adds that a signed-in member sees the living in full only inside their own branch, so a book carrying living dates cannot be served to every member by standing (P27 §5, amended) | The clan-book PDFs, like the printed 1982 volume, carry living people's dates and are served to approved requesters rather than to signed-in members by standing | Q-202 | Family Tree committee · Legal Advisor |
| D66 (the shared drive is the archive of record; the platform links to it). **Since 2 Oct 2026:** D69 makes the Hub the one record of the tree and D68 its one look on every surface; a second viewer of the tree outside the Hub would sit beside both. Where node media lives (D22 against D66) is Q-260 | A volunteer's prototype site (July 2026) holds the archive and the tree with per-person profiles, and the Preservation committee sought volunteers (February 2026) to rebuild its stand-alone website — a third archive beside the drive and the vendor's files, and a further viewer of the tree | Q-190 | David · Preservation committee · Family Tree committee · AFRP Board |
| D22 (full media, per-item consent held by the subject) | Oral histories are recorded against one spoken permission covering "the Ramallah community and any other projects"; no written release, no separate print or web switch, no takedown rule | Q-189 (answered by D93, 4 Oct 2026: a written, scoped release for every recording; the release's text is the Legal Advisor's and the Preservation committee's) | Preservation committee · Legal Advisor · David |
| D55 (Women to Women is a sub-fund of ARFHSN) | ARFECF's reviewed financial statements show Women to Women gifts as ARFECF's donor-restricted revenue in one year, released the next, with a matching expense line; the Education Fund's chequebook carries a tuition gift matching a Women to Women project | Q-212 | ARFECF Board · ARFHSN Board · CPA |
| D55 (programmes sit in the fund that budgets them) and `AFRP-Fund-Rules.md` §2 (non-earmarked money never crosses funds) | Women to Women (ARFHSN) pays Arabic Program (ARFECF) fees for member women each term; the Cook Book fund transferred money to the Education Fund for the Federation's systems; the Scholarship's letters go out in AFRP's name for ARFECF's fund | Q-168, Q-173, Q-158 | ARFHSN Board · ARFECF Board · AFRP General Treasurer · CPA |
| D62 ("The Federation President convenes") | The Federation's programme director issues the monthly ARFHSN invitation and the ARFHSN secretary sets the agenda; the President attends | Q-214 | David · ARFHSN Board |
| D63 (a Care grant is approved by the holding entity's Board with a ceiling) | Women to Women's public procedure has the committee approve all projects, and the ARFHSN minutes show the committee reporting, not the Board voting, on them | Q-114 | ARFHSN Board · Women to Women Committee |
| D1 (club dues held as agent; CPA countersignature pending) and D56 (AFRP collects ARFHSN's gifts as its agent) | AFRP's chart of accounts carries a liability for every affiliate purpose collected on the affiliates' behalf (ARFECF, ARFHSN and the Ramallah Foundation); card payments now run through one processor account per entity, replacing one AFRP account with transfers by hand. The agency pattern is in practice for every affiliate purpose and not only the two cases the decisions name; no account on either side carries club-collected national dues | Q-232, Q-3 | AFRP General Treasurer · ARFECF Treasurer · ARFHSN Treasurer · CPA |
| The programme register's Senior Award entry: retired 31 August 2026 by Board resolution, last files 2024; `AFRP-Program-Architecture.md` §6; Q-20's premise. **Since 3 Oct 2026:** D82 records that the award was not retired and continues; the register's status is corrected and Q-20 falls away | Awards were made in 2023, 2024 and 2025; applications were taken on an online form in 2025; the public site still offered the award in October 2026 and the programmes flyer filed in September 2026 lists it; no retiring resolution was found | Q-163 (answered by D82), Q-20 (falls away under D82) | AFRP Board · David |
| The programme register's Senior Award entry: the Scholarship Committee, on an award track, announced at the Convention. **Since 4 Oct 2026:** D85 keeps the Scholarship Fund Committee as the body; the 2013–2020 practice is the register's history | From 2013 to 2020 the award sat with the Leadership Ramallah committee, whose chair requested its budgeted sum from the ARFECF Board and signed the letters; it was announced by newsletter each September | Q-164 (answered by D85; the announcement venue and the budget line stay open) | David · Leadership Ramallah committee |
| The programme register's Emerging Leaders entry (ages 16 to 24; an entry rung on the Leadership branch); `branches.yaml`; `AFRP-Family-Tree-Integration.md` | No programme by that name exists in any document, mailing, budget line, committee tab or web page; the age band has no source; the one 2021 mention most plausibly refers to the Youth Summit for adults aged 21 to 35, reported from 2023 as the Day of Action | Q-178 (answered by D90, 4 Oct 2026: the entry is retired) | David · Strategic Planning Committee |
| By-Law 8.10 paragraph (the Young Leader Committee: a chairman and four members, President-appointed with Board approval, all alumni of Project Hope or Leadership Ramallah); `AFRP-Committee-Workspace.md`; `AFRP-Selection-Programmes.md` | A Young Leaders Committee (also called the Youth Outreach Committee) of two co-chairs and members listed by club city, with a filled Board seat and no appointment record or alumni check; its co-chairs run Leadership Ramallah; the directory has no Leadership Ramallah tab | Q-179, Q-175 | AFRP Board · President · Constitution Committee |
| The programme register's Senior Living entry (a Federation programme, entity to confirm); `AFRP-Program-Architecture.md` §3 (the capital-campaign module: pledges against cash) and §6 (the *Campaign* shape); journey JP-032 | The project is the Ramallah Foundation's: the Foundation owns, built and will operate the home; construction is complete; the Federation's part was communications, gifts passed through and a Convention-voted budget grant; no pledge was ever held in a Federation system | Q-203 (answered by D91, 4 Oct 2026, pending the AFRP and ARFECF Boards' confirmation: the Foundation's project, a partner row), Q-204 | David · AFRP Board · ARFECF Board · CPA |
| D3 and D55 (the Scholarship is ARFECF's; the Foundation's role is an agreement) | The public scholarship page says the programme is "managed by the Ramallah Foundation Inc"; the Foundation is a private foundation on its public filings | Q-162 | David · ARFECF Board |
| D58 (Foundation seats exist only once the ARFECF Board amends the 2015 policy) | The 2026 committee counts its Foundation representatives as votes; the Scholarship Program Overview lists three | Q-29 (answered by D58, conditional on the amendment) | ARFECF Board · Scholarship Fund Committee |
| ARFECF By-Law 6.4.4 (the Scholarship Fund Committee's exclusive authority over its fund) | The 2023 community report says the AFRP Board approved the year's scholarships; the 2026 committee report "presents recommendations" to the Board and the incoming President | Q-161 | ARFECF Board · Legal Advisor |
| The programme register's Scholarship entry: renewal "is not lapsed by silence" | The 2026 award letter: failure to file the semester documents "may result in suspension"; the recipient must contact the office | Q-159 | Scholarship Fund Committee · ARFECF Board |
| The programme register's Relief Fund and Convention entries: holding entity not stated; registration and Relief Fund amounts are "Federation money from the first dollar"; `AFRP-Care-Grants-and-Partners.md` §4. **Since 3 Oct 2026:** D83 (David's decision for the design record) names AFRP as the holding entity; the deductibility and receipt text waits on the CPA (D9). **Reconciliation item:** the books carry the fund inside ARFECF, so either the books follow D83 or the Boards revisit it | ARFECF's balance sheet carries the Relief Fund as its own bank account with AFRP owing it; ARFECF's reviewed statements book relief gifts as ARFECF's donor-restricted contributions and the Ramallah charities as its programme expense; the Educational Fund Treasurer reports the account at every Board meeting; ad hoc transfers left with no approval on file | Q-109 (entity: D83; the reconciliation, who approves between votes and D63's reach stay open) | AFRP Board · ARFECF Board · ARFHSN Board · CPA |
| D59 (a signed host agreement before every Convention); the programme register's "no signed host agreement has been found for any year" | The Board's minutes of September 2026 say the 2026 Convention was reconciled "under a revised Federation/city convention agreement"; its text is in no folder read | Q-93 | Executive Director · Legal Advisor · Convention Innovation Committee |
| `AFRP-Host-Agreements.md` §4 (dues excluded from the gross; netting only where a schedule row exists) | The 2026 settlement netted a sum the host owed the Federation against the release and charged a Federation-hosted dinner to the host's side, neither with a schedule row | Q-124 | AFRP Board · Convention Innovation Committee |
| `AFRP-Host-Agreements.md` §2.4 (the host's event-coordinator role is a scoped grant that reads no member record) | The registration system's coordinator role gives the host every registered guest's contact information with an export, full seating control, the waitlist and a payment-by-payer report; the design narrows today's access | Q-127 | AFRP Board · Digital Infrastructure Committee · Legal Advisor |
| `AFRP-MidYear-Host-Bids.md` §3 (the Board chooses the Mid-Year host; "practice is a Board choice") | The 2020–21 Mid-Year guideline, now on file, has the Executive Committee review applications and announce the selection, as By-Law 10.2.1 reads; 2026–27 practice had the Board choose after quotes, the Federation sign the hotel contract and the Executive Committee set the fee | Q-92 | AFRP Board · Executive Committee |
| By-Law 5.2 and the host-agreement template (membership-mandatory for every registrant); the board-confirmation item above | A 2026 Mid-Year registrant was not asked for dues at registration | Q-225 | AFRP Board · Digital Infrastructure Committee |
| Q-86's premise ("The camp screens its staff"); `AFRP-Volunteer-Interests.md` §9 | No written screening, training or reporting policy for camp volunteers is on file; the sources do not show the premise that the camp screens its staff | Q-86, Q-165 | AFRP Board · Camp Ramallah committee · Legal Advisor |
| By-Law 6.7.1 (the Federation "shall appropriate the necessary funds to guarantee [the Magazine's] publication"); the programme register's Magazine entry and crosswalk row D21 ("magazine money kept apart from Federation money", 2020 minutes) | Kept-apart is the 2020 practice; the by-law imposes a Federation funding duty; General Fund magazine lines from 2018 to 2024 and a seed deposit when the Magazine's account opened in 2023 show money crossing | Q-194 | AFRP Board · ARFECF Board · CPA |
| By-Law 6.7.1 (subscription policy set by the Magazine's independently selected Board; a one-year seat on the AFRP Board appointed at the General Assembly); the programme register's "its own board" | A staff of five roles and a treasurer, paid per issue; no board roster, minutes or appointment record found | Q-192 | AFRP Board · the Magazine · Constitution Committee |
| `AFRP-Magazine-Bookstore-Use-Cases.md` UC-2 (deaths are never auto-published; family approval), §0 (three issues a year), UC-9 and UC-11 (back issues, clan books, downloads, member pricing; sales as exchange revenue) | Six issues a year; obituaries are family-submitted paid placements with a tribute, graduations a standing type; two online stores sell seven titles to US addresses with no member price, back issues, clan books or downloads; the cook book line is a Board-reported chequebook on ARFECF's budget | Q-193, Q-196, Q-197, Q-199 | the Magazine · AFRP Board · ARFECF Board · CPA |
| The programme register's Bookstore entry (`in_service: None found`; "no source document exists"); the platform map's entity AFRP | Two public stores exist, on the website and the member portal; the only money evidence (the Cook Book fund) is ARFECF's | Q-197, Q-173 | AFRP Board · ARFECF Board · David |
| D60 (a non-member may register for an Arabic class at the public rate) | The public page in October 2026 says registration is open to adult members | Q-171 | David · the programme director |
| The programme register's Exchange Mission entry: a standing October delegation; the committee's August 2026 decision to pay a Convention symposium slot from Mission funds | No delegation has run since 2023 and the committee's plan is reverse missions; Houston's symposia were run by a Federation committee with the host club; whether the Mission's decision to pay a slot stands beside that committee and the host agreement is Q-125 | Q-188, Q-125 | Exchange Mission committee · AFRP Board · Convention Innovation Committee |
| D65 (Government Affairs, Congressional Outreach and the Day of Action are AFRP General Fund activity) and ARFECF By-Law 6.3.1 ("Internships in Washington" as an Endowment purpose) | The March 2025 Mid-Year assembly voted a Federation contribution to congressional internships with the source left open; the programme has no register entry | Q-182 | AFRP Board · ARFECF Board · CPA · Legal Advisor |
| `AFRP-Advocacy.md` and Q-132 (the platform refuses a candidate as the subject of a position) | The 2025–26 sources raise candidate-related questions the record does not answer | Q-132 | Legal Advisor · AFRP Board · CPA |
| The programme register's Congressional Outreach entry ("the 2020 proposal for a representative per club was not adopted"; "the tracker was last edited in 2023"); `AFRP-Advocacy.md` | Local action committees were launched inside the chapter clubs in 2025–26; the committee replaced its spreadsheet with an automated tracker on Microsoft Forms, SharePoint and Power Automate | Q-131, Q-183 | Government Affairs Committee · Council of Chapter Club Presidents · Digital Infrastructure Committee |
| The programme register's Day of Action entry (applicants answer about fifteen questions; who selects); `AFRP-Advocacy.md` P14-J11 (an application whose political-views answers are shown to the deciding body only) | The 2026 cycle was an open registration, free for adult members, with no application and no selection; the page and the mailing differ on the deadline and the eligibility sentence | Q-115 | Government Affairs Committee · President · AFRP Board |
| The programme register's AFRPWorks entry ("built by a volunteer developer"); `AFRP-AFRPWorks.md` ("browse" against "brokered" as a contradiction) | The prototype is built under the Executive Committee; an employer submits, is approved, then browses; the research reads the announcement and the minutes as a sequence (a gate, then browsing), which is evidence for the working group and not a rule | Q-147, Q-155 | President · AFRP Board |
| D44 (the committee's Google Doc is the canonical strategy text until the committee adopts a plan) | The Doc is a 30 September snapshot: it still has the tree as the roots (superseded by D53), seventeen rows marked "Proposed" that are now "Designed", no section J and no goals list (D52) | Q-235 | David · Strategic Planning Committee |
| `AFRP-Breeze-Club-Parity.md` §1 (about ten clubs run Breeze by their own choice) and crosswalk J11 (each club's decision to move onto the platform) | The Deputy President's reports present Breeze onboarding as a Federation initiative with a Federation target of every club | Q-230 | Deputy President · AFRP Board · David |
| `AFRP-Club-Experience-Plan.md` §6.3 (a club's members are a subset of people who could be Federation members under By-Law 4.1.1) | A club's 2026 by-laws draft admits anyone who considers themselves part of the Ramallah community and supports the club | Q-226 | Membership Committee · Constitution Committee · Legal Advisor |
| D57 and By-Law 11.1.5 (club money for Federation projects passes through headquarters; 11.1.4 bars soliciting for them without authority) | Clubs raise and send money to Ramallah projects directly; the Board in May 2026 asked for one channel, preferably the Relief Fund | Q-228 | AFRP Board · Council of Chapter Club Presidents |
| ARFHSN By-Laws Article III §2 (fourteen trustees; a Chairman); Q-2 (the trustee roster not on file) | The state filing lists a President, a Secretary, a Treasurer and directors; the working sheet lists a larger committee; three sources disagree | Q-2 | ARFHSN Board |
| D61 (future cycles of every programme apply in the platform) and Q-70 (D60's contact record) | The CRM creates a vetted contact with a profile (club, date of birth, occupation, address) before any consent is recorded, and the Medical Mission used the occupation field for outreach in 2026; the AFRPWorks prototype holds candidate profiles outside any rule | Q-70, Q-236, Q-151 | David · Membership Committee · Legal Advisor · AFRP Board |
| `AFRP-Club-Experience-Plan.md` §6.4 and `AFRP-Selection-Committee-Workflow.md` §3.8 (a club's delegation is selected by its officers); By-Law 9.1.3 (silent on method) | The Legal Advisor's description to the Board (May 2026) has the community's certified members vote on delegates | Q-37 | AFRP Board · Legal Advisor · Constitution Committee |
| The record's rule for what is read about a club's people: counts for the Federation's view (`AFRP-Breeze-Club-Parity.md` §3; B1 as built), a member's contact fields only under that member's dated, per-field consent (the member directory, `AFRP-Directory-Formats.md`, P19), and any wider read as a named-purpose act (Q-44) | The club president's portal view today shows members' names and contact details, and the CRM feedback asked for every member's name, email, address and phone by club | Q-237 | AFRP Board · Council of Chapter Club Presidents · Legal Advisor |

**What this section does not do.** It changes no decision. Where a row's practice is
wanted as the rule, the owner decides and the decision is recorded above in register form
with its D-number; where the record is wanted as the rule, the owner corrects the practice
and the row closes. The programme register, the crosswalk and the design documents are
corrected to say "the sources show X" in their own passes; this table is the list of what
those passes must not resolve on their own.

---

*Design and planning only; the build hold remains in force. Demo people and money are fictional;
programs, the 18 chapter clubs, the committees and the by-law citations are real and sourced.*
