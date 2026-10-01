# AFRP decisions register
### The human decisions the platform design waits on — what has been decided, by whom, and what each one settled

**Maintained:** 8 September 2026. This is the authoritative record of the six blocking decisions
tracked in `AFRP-Delivery-Status.md`. When a decision is made, it is recorded here in the exact
words the design will be built on, with the date, the decider, and the consequences that follow
automatically. Design and planning only — the build hold remains in force.

**Status vocabulary**

| Status | Meaning |
|---|---|
| **Adopted** | Decided and recorded; the design is built on it. |
| **Adopted, countersignature pending** | Decided for design purposes; a professional sign-off (CPA, counsel) is still required before it is defensible on the books. |
| **Partially resolved** | The principal question is answered; a named sub-question remains. |
| **Open** | Not yet decided; the platform carries a labelled default or a refusal. |

**All six blocking decisions were answered on 20 August 2026, twenty more on 20–21 August (Part 2), and twelve more on 8 September as the family tree became the platform's spine (Part 3).** What remains is not decision-making — it is
one countersignature, five missing documents, and a package of conforming by-law amendments.

| # | Decision | Answer | Status |
|---|---|---|---|
| 1 | Club-collected AFRP dues | **Agency** — AFRP's money at the first dollar | Adopted, CPA countersignature pending |
| 2 | Endowment Fund entity | **ARFECF** | Adopted; Policy Statement outstanding |
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
Not decisions. Three kinds of thing:

**One signature**
- The CPA countersignature on the agency treatment (Decision 1).

**Five documents that are cited as governing and have never been produced**
- Endowment Fund Policy Statement.
- Scholarship Fund Policy Statement (2015) — needed to settle the 4%/5% question for both funds.
- ARFECF's exempt-status determination letter — now load-bearing for both endowment and scholarship
  donor receipting.
- Board Rules & Regulations — the authority for the dues ladder.
- A clean, non-redlined copy of the ARFECF 2013 by-laws; and the ARFHSN trustee roster with metro
  seats and term expirations.

**One number**
- The directory grace parameter. 90 days proposed.

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

## Two items for board confirmation rather than decision
These are settled in the design and merely need the board to say so out loud:

1. **Exhibitor and press credentials** are modelled as **non-attendee credentials**, so the
   membership-mandatory rule stays absolute. This is current practice; making it explicit prevents
   it being argued later.
2. **Convention deficit responsibility** is read from the Convention Contract, and the screen says
   plainly where the contract is silent rather than assigning the loss by assumption.

---

*Design and planning only; the build hold remains in force. Demo people and money are fictional;
programs, the 18 chapter clubs, the committees and the by-law citations are real and sourced.*
