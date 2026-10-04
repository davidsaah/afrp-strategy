# ARFECF and ARFHSN — entity rulesets
### The two sister entities, encoded from their governing texts, with prior claims verified

**Date:** August 2026
**Sources:** ARFECF By-Laws revised Jan 12, 2013 (PDF, OCR of a marked-up copy) · ARFHSN By-Laws and Organizing Document, approved Chicago Convention July 2015, amended Houston Convention July 2017 (Art. III §9, fiscal year).
**Mode:** design and planning. No buildout. Extraction of ARFECF performed by an analysis agent; ARFHSN read directly. Every provisional interpretation is an OVERRIDE REGISTER entry — provisional, pending Board adoption, per AFRP-Bylaws-Ingestion-Architecture.md.

**The federation's entity picture, as the three texts actually draw it:**

| | AFRP | ARFECF | ARFHSN |
|---|---|---|---|
| Legal status | MI non-profit; lead organization | Separate MI non-profit | Separate MI non-profit, NGO, 501(c)(3) |
| Membership | Regular + Associate, own dues | **Fully derived from AFRP** (Art. V §2) — no dues, no application, no independent standing | **None.** No membership at all |
| Governing body | Board of Directors (floating size) | 15-seat role-based Board | 14-seat Board of Trustees **elected by the AFRP Board** |
| Amended by | 2/3 delegate vote at AGM | **2/3 membership vote** at AGM | **60% of the AFRP Board**, full-Board poll required, no member reference |
| Franchise | Weighted club delegations + DP mail ballot | One-member-one-vote (provisional — see EC-OV-3) | No franchise; AFRP Board acts |
| Fiscal year | Jun 1 – May 31 (8.7.2) | **Unstated** (see EC-OV-5) | Jun 1 – May 31 (Art. III §9, amended 2017) |

Three entities, **three different franchises**, one room at the Annual Convention. The engine must run each as its own `franchise:` mode and never let one entity's machinery answer another entity's question. Note also: **the AFRP 2024 text never mentions ARFHSN**, and ARFHSN's own text calls AFRP a "supporting organization" and describes AFRP as 501(c)(4) while ARFHSN is 501(c)(3) — the affiliation article of a future AFRP revision should recognize ARFHSN the way it recognizes ARFECF and the Foundation (flagged in the override register as a drafting recommendation, not an override).

---

## Part 1 — ARFECF-2013 ruleset

### 1.1 Corrections to the prior analysis (important)

The extraction agent verified every ARFECF claim in AFRP-Bylaws-Reconciliation.md against the 2013 text. Most were confirmed verbatim. **Two were not found in the document at all:**

1. **There is no region map in the ARFECF 2013 by-laws.** No §4.1, no West/Central/East, no per-region board seats, no time-zone assignment of individual members, no Santa Rosa or Atlanta. The reconciliation doc's entire "two region maps are in force at once" conflict is unsupported by this text.
2. **There is no 4-member interlock cap.** The only interlock rule is the reverse: *"The AFRP President and Deputy President shall not be elected to any office of ARFECF"* (Art. V §4) — and the Board composition **mandates** AFRP overlap (AFRP President and Deputy President are ex officio ARFECF Board members).

> **Update, 1 October 2026.** Both clauses are in the ARFECF By-Laws as revised at the 2015 Chicago Convention, which is the latest ARFECF text found. The analysis below read the 2013 text; the "phantom" finding is withdrawn and EC-OV-1 is superseded. The 1% to AFRP is in the 2012 Endowment and 2015 Scholarship Fund Policy Statements, both now found. See `design/bylaws/ARFECF-2015-and-the-fund-policies.md`.

Both phantom claims appear in the same section of the reconciliation doc, suggesting a common source — most likely a **different (earlier or later) ARFECF version, or the Scholarship Fund Policy Statement**. Question for David below. Also corrected: the "1% of assets paid to AFRP" figure is **not** in these by-laws — Art. V §1 says only *"an annual fee shall be paid as agreed to by the Board and AFRP"*; the 1% comes from the 2015 Scholarship Fund Policy Statement.

The file is an OCR of a marked-up copy (§11.2 contains a literal "Replace with" redline marker). The clean canonical 2013 text should be obtained to rule out other silent divergences.

### 1.2 Ruleset inventory (citations to the 2013 text)

**Membership — fully derived.** Art. V §2: *"All Regular Members in good standing of AFRP and all Associate Members of AFRP shall also be Regular Members and Associate Members, respectively, of ARFECF."* One roster, a derived view. Board eligibility keys to AFRP standing (Art. V §5).

**Board — 15 voting seats, composed by role, no geography.** Art. V §4: AFRP President · AFRP Deputy President · Chairmen of the Scholarship Fund, Endowment Fund, Investment, and Audit Committees · SFC Secretary · 2 SFC members chosen by its Chairman · 2 EFund members chosen by its Chairman · 1 Investment member chosen by its Chairman · 3 at-large chosen by the President. Executive Director sits non-voting. Officers (President, VP, Treasurer) elected by the Board for 1-year terms; the Board Secretary is the SFC Secretary (elected by the SFC, §9.1, not chosen by the Board). President max two consecutive 1-year terms (§7.1); President must have served as elected VP (§7.2); VP auto-succeeds mid-term (§8.1).

**Committees.** Standing: Endowment Fund, Investment, Audit, Scholarship Fund (§6.1). ARFECF President appoints each Chairman; the Board appoints other members (Art. V §4; initial round by the AFRP President). Fund-committee member terms: up to two consecutive 3-year terms; any Chairman max two consecutive 1-year terms (6.3.5, 6.4.5, 6.6.1). **Investment and Audit Committees are hollow** — no composition, size, or duties defined, yet they supply 3 of 15 Board seats.

**Money.** 5% cap, both funds, verbatim (6.3.3 = 6.4.3): *"The annual expenditures from the [Fund] shall be limited in each year only to five (5%) percent of all assets and income derived from the investment of the corpus of the [Fund] in that year."* A **cap** ("limited... only to"), where the 2015 Policy Statement makes 4%+1% **mandatory** — the floor-vs-cap conflict is real and remains a David decision. Only the Fund Committees may authorize Fund expenditures (6.3.4/6.4.4); non-earmarked funds may never be diverted across funds (6.3.8/6.4.8). President's discretionary limit $2,000 max twice per term; >$2,000 Board majority; >$10,000 AGM budget only (§7.3). Treasurer deposits within two weeks, countersigned by President/VP/Board designee (§10.1). EFund purposes include, as *examples*: Ramallah Charitable Institutions, Project Hope, Leadership Program, Internships in Washington (6.3.1). **No fiscal year stated anywhere.**

**Meetings & voting.** AGM and Mid-Year held "in cooperation with" AFRP's (Art. VII §1). Board meets ≥6×/year (VII §2); standing committees monthly (VII §3). Robert's Rules governs (VII §4); Board and committee members may attend electronically (VII §4 — **not** general membership). Board polls: non-repliers deemed to abstain (Art. V §6). Rules & Regulations and Fund-policy amendments: 2/3 of all (voting) Board members (V §3, 6.3.6, 6.4.6). **No quorum defined for any body.**

**Amendment.** Art. IX §1: *"repealed or amended upon an affirmative two-thirds (2/3) membership vote at the Annual General Meeting."* Notice (IX §2): ≥60 days — published in Magazine AND on the ARFECF website, OR mailed to all members in good standing.

### 1.3 ARFECF override register (provisional — pending Board adoption)

| ID | Gap (citation) | Provisional interpretation | Rationale |
|---|---|---|---|
| EC-OV-1 | **Superseded (1 Oct 2026).** The ARFECF By-Laws as revised at the 2015 Chicago Convention contain both clauses this row called unsupported: five at-large seats; fifteen seats in three regions of five (West, Central, East), each defined by a list of clubs (Art. V §4.1); and no more than four ARFECF directors who also sit on the AFRP Board. The January 2013 marked-up copy carries them as an "open point"; the 2015 text carries them as rules. | Treat the 2015-revised text as operative unless a later text is found. The regional club lists are out of date and need the ARFECF Board to bring them current; until then the engine checks the regions as written and reports a club it cannot place. | Found in the Federation's officer archive (2018–22 files); see `design/bylaws/ARFECF-2015-and-the-fund-policies.md` |
| EC-OV-2 | "2/3 membership vote" denominator unstated (IX §1) | 2/3 of members present and voting at the AGM | Robert's Rules default (adopted at VII §4); any stricter reading makes amendment impossible |
| EC-OV-3 | How an ARFECF membership vote runs in the joint room (no delegate/credential machinery anywhere in the text) | One-member-one-vote among natural persons present in good standing; the engine runs ARFECF ballots as a **separate franchise** with separate eligibility and tally, even in the same session as AFRP votes | Importing AFRP's delegate weighting into ARFECF has no textual basis |
| EC-OV-4 | No quorum for AGM, Board, or committees | Robert's Rules defaults: majority of the body for Board/committees; for the AGM, those registered and present, loudly flagged for the revision | VII §4 adopts Robert's "except as provided," and nothing is provided |
| EC-OV-5 | No fiscal year | Inherit AFRP's (Jun 1 – May 31), since AFRP staff administer ARFECF day-to-day (V §1) | Single administering staff, single calendar |
| EC-OV-6 | 5% cap parse + valuation basis (6.3.3/6.4.3): "5% of all assets and income derived from the investment of the corpus" is ambiguous; no valuation date | 5% of total Fund assets plus that year's investment income, valued at fiscal-year start; basis and valuation date exposed as parameters. Floor-vs-cap vs the Policy Statement stays an open David decision | More natural parse; matches Policy Statement's "% of all Assets" framing |
| EC-OV-7 | Treasurer "elected" (V §4) vs "appointed by the Board" (§10.1) | Board selects Treasurer by majority vote | Both texts agree the Board chooses; one verb needed |
| EC-OV-8 | "Three at large members chosen by the President" — which President? (V §4) | ARFECF President after the initial constitution; AFRP President for the initial board only | Parallels the "first Board Member... Thereafter" committee handoff in the same section |
| EC-OV-9 | No Board-member terms | Derived seats last as long as the underlying role; chairman-chosen seats refresh with the choosing Chairman; at-large 1 year, coterminous with officers | Coheres with the 1-year officer cycle |
| EC-OV-10 | AFRP officer turnover cascades into 2 ex officio ARFECF seats | Seat follows the office in real time; transitions timestamped to AFRP election results | Plain ex officio reading |
| EC-OV-11 | "2/3 of all members of the Board" (V §3, 6.3.6, 6.4.6) + poll non-reply = abstain (V §6): abstain functions as No; is the ED in the denominator? | Denominator = 15 voting members (ED excluded — 6.3.6/6.4.6 say "voting members"); fixed-denominator matters taken at meetings, not polls; the abstain-as-No effect surfaced in the UI | 6.3.6/6.4.6 are explicit; effect is textual even if unintended |
| EC-OV-12 | Poll deadline unstated; "Executive Assistant" undefined in this document | Poll issuer sets a stated deadline at issuance (default 7 days, configurable); "Executive Assistant" = AFRP's EA (AFRP administers, V §1) | Polling clause inoperable without a deadline |
| EC-OV-13 | "Committees meet... as called for by the Chairman of the Board" (VII §3) — likely drafting slip | Committee's own Chairman or the President (ex officio member of all committees) may call meetings; monthly cadence mandatory | Preserves both readings |
| EC-OV-14 | Do derived Associate Members vote in ARFECF? (V §2 vs IX §1 "membership vote") | Non-voting, mirroring the AFRP category they derive from | "Respectively" imports the category's incidents |
| EC-OV-15 | Notice channel grouping (IX §2) | (Magazine AND website) OR (mail to all members in good standing), 60 days either way | Comma placement; engine verifies one full channel |
| EC-OV-16 | President must have been "duly elected Vice President" (§7.2) — impossible for a first President; does a §8.1 succession stub count against the two-term cap? | Stub terms don't count against the cap (only full elected terms); §7.2 unenforceable for the inaugural cycle | §8.1 distinguishes the stub from "his/her regular term" |
| EC-OV-17 | Electronic attendance limited to Board/committee members (VII §4) | Remote attendance = presence for Board/committee purposes only; membership-level remote voting requires amendment | Expressio unius |
| EC-OV-18 | Legal Advisor selection/term unstated (§12.1) | Board-appointed under the "such other officers" clause, 1-year term | Only mechanism in the document that can produce the role |
| EC-OV-19 | Investment + Audit Committees hollow; Policy Statements incorporated but not attached (6.3.1, 6.4.1) | Apply the 6.3.5/6.4.5 term pattern to Investment and Audit; ingest the Policy Statements as first-class rule sources when supplied | Consistency across standing committees |
| EC-OV-20 | Term-limit holdover ("until their respective successors are appointed") can extend service indefinitely | Holdover time counts against consecutive service; any break resets consecutiveness | Prevents the holdover clause from nullifying the limit |
| EC-OV-21 | AGM-approved budget (§7.3) vs Fund Committees' exclusive spend authority (6.3.4/6.4.4) | AGM approves an aggregate operating budget; Fund Committees retain exclusive authorization of Fund expenditures within the 5% caps | Harmonizes rather than nullifies either clause |
| EC-OV-22 | No election machinery at all (no credentials, nominations, ballots, tie-break, proxy, record date) | Robert's Rules defaults plus explicit configured overrides, every one tagged "no textual basis — revision candidate" | Same principle as EC-OV-2/3/4 |

---

## Part 2 — ARFHSN-2017 ruleset

ARFHSN — the **American Ramallah Federation Human Services Network** — is the simplest of the three entities to model, because it has **no membership and no franchise**. It is a 501(c)(3) NGO whose entire governance runs through the AFRP Board.

> *Since 2 October 2026 (research round; role level).* **The by-laws are in revision.** Counsel's draft of revised ARFHSN by-laws (July 2026) is with a four-trustee review committee. It goes next to the full ARFHSN board and then to the AFRP Board, with November 2026 as the target. The review covers Board authority, the AFRP–ARFHSN relationship, financial oversight, programme references and compliance. Until the AFRP Board votes under Art. V, the 2015/2017 text below is operative. Which text is operative on the day the Hub seats the Care lens, and whether the revision changes D62, D63 or Art. III §5 and §7, is **Q-220**.
>
> **Who convenes the monthly meeting.** D62 says the Federation President convenes ARFHSN. In practice the Federation's programme director issues the monthly invitation, the ARFHSN secretary sets the agenda, and the President attends. This is a conflict between the record (D62) and practice, and it is recorded in the Decisions Register's research-round conflicts table. Whether convening is an office service to ARFHSN (an agency role, Q-3's pattern) or the President's power is **Q-214**. D62 stands until it is answered (D41).

### 2.1 Ruleset inventory (citations to the 2015/2017 text)

**Identity.** Michigan non-profit NGO; educational and charitable purposes (job training centers, vocational scholarships and grants, senior-citizen services awareness, elderly assistance, food/shelter for needy families, economic development in the Palestinian Territories); AFRP is its "supporting organization" (Art. I, II). Note Art. III §1 describes AFRP as **501(c)(4)** while ARFHSN operates as **501(c)(3)** — an entity-status fact the ledger and receipt language must respect (donations deductible to ARFHSN, not necessarily to AFRP).

**Board of Trustees — 14 members, elected by the AFRP Board of Directors** (Art. III §2). All must be AFRP members in good standing. Composition: 6 from the AFRP BOD, one each from Detroit, Jacksonville, Houston, San Francisco/San Jose, Chicago, Metro-Washington D.C.; 8 independent members (not affiliated with the AFRP BOD), one from each of Detroit, Jacksonville, Houston, SF/San Jose, Washington D.C., Chicago, Knoxville/Birmingham, and representing New York/New Jersey, Kentucky/Cleveland, Los Angeles/San Diego — plus a catch-all: trustees "can be elected from any city, a Ramallah native who resides in the United States."

**Terms.** Initial stagger by vote rank: top 5 → 3 years, next 5 → 2 years, next 4 → 1 year; thereafter the AFRP BOD elects replacements annually (Art. III §2). Max two consecutive terms; re-eligible after **two years** off (Art. III §3). Vacancies filled by the AFRP BOD from the same metro area for the remainder of the term; candidate ties broken by the BOT Chairman **by coin flip** (Art. III §2).

**Officers** (Art. III §4). Chairman elected by the BOT — presides but **cannot vote except to break a tie**. Treasurer and Executive Administrator must be the two Detroit-area trustees (HQ is the Ramallah Club of Detroit building in Westland, MI, shared with AFRP's office). Major decisions require consultation with the Chairman, who decides when a BOT vote is necessary.

**Controls.** Two co-signatures on all checks, designated by the Board (III §5). No trustee compensation; expenses only when the matter can't be handled by conference call (III §6). BOT manages programs and funds but is **subordinate to AFRP BOD directions and policy decisions**, and must comply to preserve 501(c)(3) status (III §7). Financial and operational report to the AFRP BOD every 6 months; the AFRP President may demand information between reports and officers "must comply" (III §7). All employment contracts at director/manager rank or above require AFRP BOD approval (III §8). AFRP BOD retains a certified accountant **from outside the Ramallah community** to certify financial operations (III §9). **Fiscal year Jun 1 – May 31** (amended from calendar year, Houston 2017). $2M liability insurance with an endorsement covering AFRP (III §10). 501(c)(3) dissolution clause (Art. IV). Standing 5-member USAID grant committee: BOT Chairman, Executive Administrator, AFRP President + 2 appointed by the BOT Chairman (Art. VI).

**Amendment — the sharpest rule in the document** (Art. V): amendments are moved by any AFRP Board member, with AFRP's Board acting "in its capacity as the highest governing body of ARFHSN, **without any reference to the general membership of AFRP**." Passage requires **a favorable vote of 60% of the members of the Board of AFRP**, and **polling of the entire Board is required** for any amendment. Quorum for other business: "any number of the members of the Board present." Non-amendment issues need a full-Board poll only if 5 Board members request it or the President deems it important enough.

### 2.2 ARFHSN override register (provisional — pending Board adoption)

| ID | Gap (citation) | Provisional interpretation | Rationale |
|---|---|---|---|
| HS-OV-1 | "60% of the members of the Board of AFRP" (Art. V) — AFRP's Board size floats (active Past Presidents + compliant club presidents + …) | Denominator = AFRP's voting Board membership as of the poll's issuance date, computed by the AFRP entity's own roster engine, frozen for the poll's duration | Mandatory full-Board poll is a fixed-denominator vote; a moving denominator mid-poll is unworkable |
| HS-OV-2 | Interaction with AFRP 6.2.4 (non-reply = abstain) — a non-reply functions as a No against the 60% threshold | Textual and enforced; the poll UI states plainly that silence counts against passage, and the deadline is stated at issuance | Same arithmetic as AFRP/ARFECF fixed-denominator votes; consistency across the register |
| HS-OV-3 | "Two consecutive terms" cap (III §3) — terms are 1, 2, or 3 years in the initial stagger; does a 1-year initial term count as a full term? | Every elected term counts as one term regardless of length; vacancy-fill remainders under 18 months do not count | Mirrors EC-OV-16's stub-term logic; keeps the initial stagger from producing absurdly short careers |
| HS-OV-4 | "Not associated with or affiliated with the BOD of AFRP" for the 8 independent seats — undefined | Independent = not currently a voting member of the AFRP BOD; ex-members and committee members are eligible | Narrowest reading that gives the clause effect; III §2 already requires all trustees to be AFRP members |
| HS-OV-5 | Geographic seat map (III §2) names 6 + 10 metro constituencies for 14 seats, with a catch-all "any city" clause | Seat rows encoded as a versioned schedule (same pattern as dues/regions); the catch-all fills any seat the named metros cannot | The text's own arithmetic doesn't close; the catch-all is its escape valve |
| HS-OV-6 | Chairman "cannot vote on issues before Board unless there is a tie" (III §4A) vs 14-member board | Chairman excluded from the voting denominator (13 voting trustees); tie-break vote recorded as such | Plain text; denominator must reflect it |
| HS-OV-7 | No BOT quorum stated (Art. V's "any number present" governs AFRP-Board business, not BOT meetings) | Robert's Rules default: majority of the BOT (7 of 13 voting + Chairman presiding) | Only defensible gap-filler; flagged for the revision |
| HS-OV-8 | AFRP text never mentions ARFHSN; ARFHSN calls AFRP 501(c)(4) supporting organization | Entity registry models ARFHSN as AFRP-controlled (governance parent: AFRP BOD) with separate 501(c)(3) books; recommend the next AFRP revision add ARFHSN to Const. Art. III | Matches both texts' actual mechanics; the drafting gap is AFRP's, not ARFHSN's |

---

## Part 3 — Questions for David

1. **Where did the ARFECF region map and the 4-member interlock cap come from?** They are not in the 2013 by-laws. If they live in a newer ARFECF revision or in the Scholarship Fund Policy Statement, upload it — otherwise they'll stay inactive in the engine. Related: a clean (non-redlined) copy of the 2013 text would rule out other OCR-era divergences.
2. **Electronic voting:** the adopted 2024 AFRP text kept the mailed CPA ballot. Should the e-voting design (AFRP-Electronic-Voting.md) be repositioned as a drafted amendment for the Constitution Committee — the drafting-workbench use case — rather than a build target?
3. **ARFHSN roster:** is there a current list of the 14 trustees, their metro seats, and term expirations? The stagger machinery needs the actual seat history to compute who is up for election each year.
4. **The Scholarship Fund Policy Statement (2015), Endowment Fund Policy Statement, Board Rules & Regulations, Investment Committee policy, and the Strategic Planning Proposal** (now incorporated by reference in AFRP 17.1.4) are all cited as governing and none are on file. Each is a first-class rule source in the ingestion design — upload as available.

---

*Design and planning only. ARFECF text is an OCR of a marked-up copy; ARFHSN text is an OCR with visible scan artifacts ("Bv-Laws", "can-y", "Angles") read through. All overrides are provisional pending Board adoption.*
