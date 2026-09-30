# AFRP By-Laws 2024 — ruleset extraction and divergence report
### Parallel encoding of bylaws-2012 and bylaws-2024, per David's decision of 16 Aug 2026

**Date:** August 2026
**Source:** AFRP Constitution & By-Laws approved July 13, 2024, Jacksonville Convention (uploaded 16 Aug 2026), read against AFRP-Bylaws-Reconciliation.md (the 2009/2012 analysis).
**Mode:** design and planning. No buildout. Extraction performed by parallel analysis agents; every provisional interpretation below is an OVERRIDE REGISTER entry — flagged provisional, pending Board adoption, per the override policy in AFRP-Bylaws-Ingestion-Architecture.md.

**Status of the two rulesets:** `afrp-bylaws-2012.2` (superseded 13 Jul 2024) and `afrp-bylaws-2024.1` (adopted 13 Jul 2024, effective date unstated — see override AFRP-OV-17). Both encoded; divergence below is the parallel-run report. 2024 is not yet declared governing in the engine — David asked for the parallel run first.

**Headline findings**
1. **Weighted fractional delegate voting survives** (9.1.3, verbatim, now with an explicit Deputy-President carve-out). The engine correction list stands.
2. **The Deputy President mailed-CPA-ballot process survives** — the adopted 2024 text did NOT introduce electronic voting. The words "and/or email" were bolted onto 9.2.2's envelope-and-postmark process, and that is the only electronic language in the document. The AFRP-Electronic-Voting.md design therefore describes a FUTURE AMENDMENT, not the current law. Flagged as the largest gap between David's recorded direction ("voting will be electronic") and the adopted text.
3. **Membership year moved to Jan 1 – Dec 31** and dues authority moved from the Assembly to the Board (5.1); the voting-dues deadline moved to **April 30** and the old receipt-vs-postmark contradiction is fixed by disjunction.
4. **A new 9-member Selection Committee (Article XVII)** now gates every Federation seat, and took over membership certification — while the old Credentials Committee constituting provisions were deleted, leaving Credentials and Election as phantom committees with duties but no composition.
5. The old ballot-window impossibility is **not fixed and arguably worse** (return deadline moved earlier to Jun 10; certification has no deadline).

---

## A. AFRP-2024 ruleset inventory

### A.1 Membership categories & eligibility
- **Regular Membership** — By-Law 4.1.1: age 18+, origin from ancestral Ramallah "as defined within Aziz Shaheen's book entitled 'Ramallah'", or married to one having such origin. (Const. VII §1 delegates to By-Laws.)
- **Associate Membership** — By-Law 4.2.1: for those failing 4.1.1, "due to special circumstances," approved by **majority vote of the Board of Directors after recommendation by the Membership Committee**. "An Associate Membership is a non-voting membership; therefore, Associate Members are ineligible to vote on any A.F.R.P. matters."
- These are the **only two categories**. No Life/Patron/Manar/Family/Student tier appears anywhere in the 2024 text (grep-confirmed: zero hits for Patron, Manar, Life Member, student, complimentary, waiver).
- **Household joint application** — 8.12.3: one household member may sign and pay for all qualified household members, listing names and ages. **Household definition** — 8.12.8: "Household is defined as husband and/or wife and unmarried children over the age of 18."
- Application mechanics — 8.12.2: application (or a signed letter with sufficient identifying info for applicant + household) accepted; annual renewal notices to all current members.
- Chapter member ≠ automatic AFRP member — 3.1: "A member of any Chapter Club **may be deemed** a member of the A.F.R.P., provided they qualify for A.F.R.P. membership and are members in Good Standing according to By-Law 4.3.1."

### A.2 Good standing
- **By-Law 4.3.1\*\*** (unchanged 2012 text, verbatim): *"A member in Good Standing ('Good Standing') is one that adheres to and complies with the Constitution and By-Laws of the A.F.R.P., and has paid his/her AFRP and Local Club (if any) current membership year Annual Dues."*
- **Still conjunctive** national + club. `standingAt()` as AND-across-scopes remains correct.
- Downstream uses: Board membership (6.2.3, both AFRP and Chapter Club standing required), committee members (8.1.2, standing "during the prior year of appointment" plus club standing, maintained during tenure), candidates (9.3.1), by-law amendment proposers (16.1.1), automatic officer removal (13.2).

### A.3 Dues rules & deadlines
- **5.1\*\*\*\*\***: "The amount(s) and structure of the Annual Membership Dues shall be determined by the **Board of Directors** from time to time. The membership year shall be from **January 1 to December 31st**."
- **5.2\*\*\*\*\*** (fully rewritten): convention registrants who qualify for membership **must pay dues prior to the Annual Convention**; payment "may be a condition to registration"; dues are **separate from and in addition to** registration fees; non-eligible registrants may be required, "in the sole discretion of the A.F.R.P.," to remit a fee or donation; host-collected dues/fees **must be promptly remitted to the General Treasurer** and do not count toward host convention proceeds; **30 days before the Convention** the General Treasurer sends host officials the list of members whose dues are paid. The old **under-26 full-time-student dues waiver is deleted** — no student waiver exists in 2024.
- **Voting eligibility deadline — 5.3\*\*\*\*\***: dues "must be **received at the A.F.R.P's office by, or postmarked by, April 30th**" to vote for Deputy President, Members At Large, Scholarship Committee members, and Executive Committee members. **8.12.5\*\*\*\*\*** repeats the identical received-or-postmarked April 30 test for applications+dues → certification. The receipt-vs-postmark conflict is resolved by disjunction (either test suffices) and both sections now agree.
- **Own-funds rule — 8.12.4\*\*** (survives verbatim from old 8.15.4): "The only dues to be accepted as valid for purposes of voting are those that are paid by credit card, check or money order from the applicant's personal or business fund, whether the applicant is an individual or a head of a household on behalf of himself or herself and those members of his or her own household."
- 9.4.3: dues-for-votes = grounds for Selection Committee to disqualify the membership, the votes, and the candidate. 9.5.5: payment of dues on behalf of others prohibited "except members of their own families [families to mean husband and wife, their children and their spouses]".
- List handoff — 8.12.6: membership lists (alphabetical per community) to **Selection Committee** and Executive Assistant **no later than May 10**; applications to Selection Committee by May 10 for verification, then returned.
- 8.12.7\*: Executive Assistant custodian; list shared with Federation and ARFECF members upon Executive Committee approval.

### A.4 Voting modes
- **Mode selection — 9.1.1** (unchanged): delegate voting required when (1) a delegate requests it and the President polls "the Chairpersons designate of the Club delegates present" and **15% or more of those polled favor** it; (2) "voting for elective offices of the Federation and the Convention city, where a contest exists"; (3) Constitution/By-Law amendments requiring General Assembly vote.
- **9.1.2**: everything else by voice vote or counting of raised hands of members present.
- **Weighted fractional delegate voting SURVIVES — 9.1.3** (verbatim): *"Other than the election of the Deputy President, each club or community shall have the right to send to the Convention a delegation consisting of one or more delegates. Each delegate will independently cast a proportionate number of votes equaling the total number of certified members from his/her Chapter Club divided by the number of delegates sent to the Convention; However, any certified member attending the Convention shall have the option to cast his/her vote independently in which case, his/her vote shall be deducted from the number of votes cast by the delegates representing his/her community."* Note the new leading clause "Other than the election of the Deputy President," which explicitly carves DP out of delegate voting. Member extraction survives. Still no rounding rule, no delegate cap, no declaration deadline.
- **9.1.4**: community vote cap = "the number of persons whose membership had been certified by the **Selection Committee**" (certifier changed from Credentials to Selection Committee).
- **Deputy President mailed-CPA-ballot process SURVIVES — 9.2**, with edits:
  - 9.2.1: within 30 days after receiving the certified membership list, the **Selection Committee** (was Credentials) mails each certified member a ballot + pre-addressed return envelope; return address = "a Certified Public Accountant or **independent agency** chosen by the **Election Committee**."
  - 9.2.2: vote for one candidate, sealed BALLOT envelope inside larger envelope, "and **mail and/or email** it so as to reach the Certified Public Accountant or the independent agency **postmarked no later than June 10** of each year." (Deadline moved Jun 20 → **Jun 10**; the word "email" is the only electronic-voting language in the entire document, and it is bolted onto a postmark/envelope process.)
  - 9.2.3: sealed envelopes held by CPA/agency; turned over to "the Chairpersons of the **Election and the Credentials Committees**" on written request pre-Convention; not opened until election day of the Annual Convention.
  - 9.2.4: plurality wins "irrespective of the percentage of votes or the number of candidates." **Tie: "decided by a draw from a bag under the direction of the Election Committee."**
  - 9.2.5: overvote (marks for >1 candidate) disqualified.
- **There is NO general electronic voting regime in the 2024 text.** Remote *presence* is acknowledged ("in person or otherwise") for Board/Council meetings (10.3.1, 10.4.1, 10.5.1), and email is permitted for amendment submissions (16.1.1) and the ballot return in 9.2.2, but no e-ballot process, no identity/authentication, no vote secrecy language.
- Secret ballot on the floor: Members At Large "by vote through a secret ballot" (6.5.2); campaign disqualification by Board "by secret ballot" (9.4.2).
- Board voting: only Board members vote at Mid-Year/Board meetings (10.6.1). Board polls: 6.2.4 (Executive Assistant polls Board on all major issues "whenever possible"; a member-initiated poll requires approval of ≥5 Board members; non-repliers "shall be considered to abstain"); **7.9.10\*\***: "The passage of such polling shall be by **simple majority of the votes casted. Abstaining and non-voting members of the Board of Directors shall not be counted.**"

### A.5 Election calendar (all fixed dates in the 2024 text)
| Date | Event | Citation |
|---|---|---|
| **Feb 28** | DP candidates submit written intention "by registered letter or in person" to the **Selection Committee** at AFRP HQ; postmarks after Feb 28 not considered | 9.3.4(3)\*\* |
| **+15 days of receipt** | "the A.F.R.P. Board of Directors at large" evaluates and approves applicant "by a simple majority of voting members" | 9.3.4(3) |
| **Mar 31** ("March 31th") | **Credentials Committee** certifies candidate eligibility | 9.3.4(3) |
| **Apr 30** | Dues + applications received or postmarked → certified to vote for DP, MAL, Scholarship Committee, EC | 5.3\*\*\*\*\*, 8.12.5\*\*\*\*\* |
| **May 10** | Membership Committee furnishes per-community lists to Selection Committee + Executive Assistant; applications handed to Selection Committee for verification | 8.12.6 |
| **+30 days after receiving certified list** | Selection Committee mails DP ballots | 9.2.1 |
| **Jun 10** | Ballot return "postmarked no later than" to CPA/agency | 9.2.2 |
| **Aug 1** | Chapter Club affiliation forms (officers, addresses, phones, emails) to Federation Office | 3.2 |
| **Mid-Year Meeting** | MAL candidacies submitted (candidate need not attend); convention bids in writing due; candidates address the Board | 6.5.2, 10.1.1, 9.5.3 |
| **Convention −60 days** | Constitutional amendment notice to all Chapters (Const. XI §3); by-law amendment submissions to ED/EA (16.1.1); convention date printed in Magazine = sufficient meeting notice (10.1.4) |  |
| **Convention −45 days** | Reviewed by-law amendments to Board + Council of Chapter Club Presidents | 16.1.1 |
| **Convention +120 days** | Final convention accounting to AFRP office | 10.1.7 |
| **Convention −30 days** | General Treasurer sends host the paid-members list | 5.2\*\*\*\*\* |

### A.6 Quorum
- **Annual Meeting — 10.1.5** (verbatim): "Twenty Five (25) paid members shall be deemed to be have a quorum and may transact any business that comes before it and elect officers regardless of the percentage of members present, or delegates holding votes of absentee members." Fixed count; unchanged.
- **Board — 10.3.1** (verbatim): "During the interval between Conventions, the Board of Directors shall meet a minimum of six (6) times per year, inclusive of the Mid-Year and Convention. A majority of those present (in person or otherwise) shall be needed to discuss and transact Federation business." Still **no Board quorum** — a decision rule of majority-of-those-present, with remote presence counting. Same formula for Council of Past Presidents (10.4.1) and Council of Chapter Club Presidents (10.5.1).

### A.7 Thresholds by motion type
| Motion | Threshold | Citation |
|---|---|---|
| Constitution amendment/repeal | 2/3 delegate vote at AGM — "may be repealed or amended upon an affirmative two-thirds (2/3) delegate vote at the Annual General Meeting" | Const. XI §2 |
| By-law amendment | "A two-thirds (2/3) majority delegate vote of the general assembly" | 16.1.1 |
| Board Rules & Regulations | "two-thirds (2/3) affirmative vote of **all members of the Board of Directors**" | 6.2.1 |
| Past President reinstatement to active voting | "2/3's Board Approval" | 6.3.1 |
| Board polling (general passage rule) | Simple majority of votes cast; abstentions/non-voters not counted | 7.9.10\*\* |
| Board-member-initiated poll request | Approval by ≥5 Board members | 6.2.4 |
| DP applicant approval | Simple majority of voting members of Board at large, within 15 days | 9.3.4(3) |
| Associate membership | Board majority | 4.2.1 |
| Committee creation by General Assembly | Majority | 8.1.1 |
| Campaign-violation disqualification | Board majority by secret ballot | 9.4.2 |
| Trigger delegate voting | 15% of polled delegation chairpersons | 9.1.1(1) |
| Elective offices (contested) | Plurality (DP explicitly "irrespective of the percentage of votes") | 9.2.4 |
| Expenditure >$2,000 | Board majority | 7.2.3 |
| Expenditure >$10,000 | Only via budget approved at AGM | 7.2.3 |

### A.8 Abstention handling
- Board polls: non-reply = abstain (6.2.4); abstentions and non-voters excluded from the simple-majority denominator (7.9.10).
- Assembly/floor votes: **silent** — no abstention rule anywhere for the General Assembly.
- Interaction unresolved: 6.2.1's "2/3 of all members" is a fixed-denominator rule where abstention functions as No; 7.9.10's votes-cast rule excludes them; the text does not say which applies if Rules & Regulations are adopted by poll.

### A.9 Tie-breaking
- DP mailed ballot: "draw from a bag under the direction of the Election Committee" (9.2.4).
- **No tie rule for any other election.** The old text's other-offices tie provision (recon doc cited old 8.12.1) does not exist in 2024 — 8.12.1 is now Membership Committee composition. Fallback is Robert's Rules (Const. IX §4, 12.1) = repeated balloting.

### A.10 Officer terms, limits, eligibility
- General limit — 9.3.3: "maximum of four (4) consecutive one (1) year terms in the same office, except the President, who shall not succeed himself/herself to the same office, but may by reelected three (3) years following his/her presidency."
- President: must be "a duly elected Deputy President and have served in that capacity during the preceding year" (7.2.2); DP auto-succeeds on termination of President's term/incapacity (7.3.1; EC + Board decide inability/refusal).
- DP eligibility (7.3.2, 9.3.4): AFRP good standing prior 3 years; 4 years elected/appointed service to Local Club and/or Federation (or proven local-community service record if no club); **not from the same city as the President**; Feb 28 filing; Board-at-large approval; Credentials certification by Mar 31.
- Candidates generally — 9.3.1\*\*: good standing "immediately after the election and throughout their term"; Chapter Club membership mandatory if a club exists. 9.3.2: must be present at Annual Meeting; special-circumstance exceptions decided by President after consulting Legal Advisor, final.
- MAL — 6.5.1/6.5.2: not a Past President or Local Chapter President; 2-year staggered terms; two elected per year by secret ballot; candidacies filed at Mid-Year (presence at Mid-Year not required); stale 2009 transition language remains ("For 2009, there will be no election as the current six (6) Board of Directors at Large will be reduced to four (2) with two (2) having their term expiring in 2009").
- Historian — 6.2.2: Board elects one of its members at the Annual Convention, 3-year term; Board may replace by special election; duties Board-defined.
- Executive Secretary (7.4.1\*\*\*\*\*), General Treasurer (7.5.1\*\*\*\*\*), Financial Secretary (7.5.2\*\*\*\*\*), Educational Fund Treasurer (7.7.1\*\*\*\*\*): each "shall reside in the Headquarters metro area, **or any other area within the United States** so long as his/her duties and responsibilities may be fully performed remotely... (determined in the sole discretion of the Board)". New remote-work allowance in all four.
- Executive Director: Const. V §3\*\* "shall reside in the Headquarters metro area"; 7.9.7\*\* candidate "must agree in writing to work from the Federation's Headquarters office"; at-will (7.9.4/7.9.5); hired by Board on recommendation of 5-member President-appointed Board Selection Committee (7.9.4); vacancy process 7.9.7–7.9.8; other employees selected by EC, approved by Board (7.9.9); quarterly evaluation + salary recommendation at Annual Meeting (7.9.6). ED got **no** remote flexibility in 2024.
- Legal Advisor: "may be elected from any community, and shall be a licensed attorney in good standing" (7.8.1).
- Removal: 13.1 (failure to fulfill duties or detrimental conduct — no procedure/threshold stated); **13.2 automatic**: "Any elected officer who, during his/her tenure of office looses his/her status as a Member in Good Standing in the A.F.R.P. or his Chapter Club, if any, shall be removed and replaced by a one appointed by the President."

### A.11 Committees — composition and size
- Constitution VIII §1\* standing list (14): Council of Past Presidents; Council of Local Club Presidents; Fund Raising; Investment; Finance; Program Development; Strategic Plan; Young Leader; RBPN; **Constitution**; **Selection**; Membership; Young Adults Program; Youth Program. By-Law 8.2.1\* repeats the list "mandated by the Constitution" and **adds the Government Affairs Committee** (also described at 8.15.1: Board-established, DC representation, Board-appointed chair/members).
- Standing committee members: 1-year terms, President-appointed unless otherwise specified, after consultation with Committee on Appointments "(if necessary)" (8.1.3). Eligibility: good standing prior year + club standing, maintained (8.1.2).
- Fundraising: **9 members, 3 per region** (regions per 10.1.1), 3-year staggered terms, one per region elected annually by General Assembly (8.5.1\*); four President-appointed sub-committees (Emergency, Corporate, Grants & Foundations, Membership dues), each chaired by the Executive Director (8.5.2–8.5.5).
- Investment: composition per Board-established Investment Committee policy (8.6.2\*) — external document.
- Finance: proposes annual budget to Board at General Assembly (8.7.1); **fiscal year June 1 – May 31** (8.7.2).
- Strategic Plan: chaired by DP + 4 members appointed by DP with Board approval (7.3.3).
- Young Leader: Chairman + 4 members, President-appointed with Board approval, must be alumni of Project Hope or Leadership Ramallah (text located under heading "8.10 – Constitutional Committee", By-Law 8.10.1).
- Constitutional Committee: "As described in Article XV – 16.1 Amendments to By-Laws" (8.10.1) — a broken cross-reference (amendments are Article XVI); no composition given anywhere.
- Committee on Appointments: ≥3 Board members excluding EC, selected by the Board (8.11.1).
- Membership: one member per community with a Local Chapter (generally club president or representative) + Executive Assistant + General Treasurer (8.12.1).
- RBPN, Young Adults Program, Youth Program: rules/regulations/policies set by Board (8.9.1, 8.13.1, 8.14.1).
- **Selection Committee — Article XVII (new)**: "responsible for screening, vetting and approving every individual recommended for a vacant Federation seat, including standing committee chairs, committee members, Executive Committee members, Deputy President, and Constitution-ratified program chairs" (17.1.1). **Nine members**, slate presented by EC to Board, "no more than two individuals from the same city," diversity in geography/age/gender/family-clan/experience (17.1.2). Local Club presidents submit 1–2 recommendations via President (17.1.3). Staggered 3/3/3 with 1-, 2-, 3-year initial terms; reappointment allowed; "service may not exceed six years (two consecutive terms)" (17.1.3). Duties: advertise/recruit for chairs, EC seats, program chairs, DP; guarantee deadline compliance; review applications; "Rank three top candidates based on merits"; interview top three for all positions except DP; for DP, recommend the candidate slate for election (17.1.4). 17.1.4 defers to an external "Strategic Planning Proposal" for full job descriptions.
- Dissolution Trustees: 7 (President, DP, Legal Advisor, 2 ex-Board, 2 ex-EC), Board-appointed (15.2.1); 90-day CD then 5-year CD; unrevived funds → educational scholarships for members per 4.1.1 (15.2.2–15.2.6); uncompensated (15.2.8).
- **Credentials Committee and Election Committee: no composition, appointment, or size anywhere in the 2024 text** despite operative duties at 9.2.1, 9.2.3, 9.2.4, 9.3.4(3). The old 8.11 Credentials provisions (7 members incl. General Treasurer; certify/deny; dues non-refundable; May 25 list; Board final on challenges) are **deleted**.

### A.12 Board composition
- 6.2.2 voting: all Council of Past Presidents members + all Council of Local Club Presidents members + 4 Members At Large + Executive Committee members + 1 RBPN + **1 Young Leader Committee (new seat)** + 1 Magazine + 1 Ramallah Foundation. Non-voting: Executive Director, Executive Assistant. Board also elects the Historian (3-year term) from among its members.
- Executive Committee (7.1.1\*): President; Deputy President; Executive Secretary; **Scholarship fund Secretary of the ARFECF**; Educational Fund Treasurer; "the General Fund (Treasurer; Financial Secretary)"; Legal Advisor; **President of ARFECF**; Executive Director; Executive Assistant. All are Board members (ED/EA non-voting). Elected at GA except ED, EA, and ARFECF officials (7.1.2\*).
- Past President active-voting test (6.3.1): attend **3 of the preceding 5 conventions** AND not miss **3 consecutive Midyear Meetings**; President compiles the annual eligible list, printed in the Annual Committee Directory; reinstatement by petition + 2/3 Board.
- Council of Chapter Club Presidents: chaired by the DP; consists of presidents of clubs that complied with Article III (affiliation form by Aug 1) (6.4.1, 3.2). Board denominator still floats.

### A.13 Financial controls
- President discretionary: ≤$2,000 off-budget, **max twice per term**; >$2,000 Board majority; >$10,000 only in the AGM-approved budget (7.2.3).
- Checks: signed by Treasurer, countersigned by "a senior officer of the Executive Committee of the home office" (11.1.2); General Treasurer co-signs with Financial Secretary (7.5.1/7.5.2); Educational Fund Treasurer countersigned by an ARFECF Board designee (7.7.1).
- General Treasurer pays all invoices incl. payroll/insurance/taxes (7.5.1); Financial Secretary collects/receipts/deposits all income (7.5.2).
- Contracts: EC + Board jointly authorize; "The Executive Committee Including the legal advisor must approve the final language before contract execution" (11.1.1).
- Gifts: EC and Board may accept contributions/bequests (11.1.3). No individual/club solicitation for AFRP projects without Board+EC authorization (11.1.4). **All club-raised funds for AFRP-sponsored projects route through Federation HQ** (11.1.5).
- Convention: host-collected dues/fees promptly remitted to General Treasurer (5.2); final accounting ≤120 days via Convention Liaison, a Council of Past Presidents member appointed by the President (10.1.7); Convention Contract Guidelines govern host/AFRP rights (10.1.6).
- ED hiring gated on Board determining the general fund can cover the expense (7.9.7).
- Fiscal year Jun 1–May 31 (8.7.2); membership year Jan 1–Dec 31 (5.1).

### A.14 Convention rules
- 10.1.1: locations selected **2 years in advance** by the general membership at the Annual Convention; only Regular Members in good standing vote at the Annual Meeting; bidding city needs **≥50 paid members for ≥5 consecutive years**; written bid by Mid-Year Meeting; **3 regions** — Region 1: San Francisco, San Jose, San Diego, Los Angeles, Houston; Region 2: Detroit, Chicago, Cleveland, New York, Louisville/Lexington; Region 3: Jacksonville, Birmingham, Knoxville, Washington D.C.; annual rotation; "A Convention cannot return to a region within a three year period"; a declining region forfeits until the next rotation. (Identical to old AFRP map; ARFECF-map divergence untouched by this document.)
- 10.1.2\*\*\*\*\* and 10.1.3\*\*\*\*\*: **"Reserved."** — two by-laws deleted outright in 2024 (old content excised; the old registration/dues-bundling and student-waiver material from old 5.2 territory is the likely casualty).
- 10.1.4: Magazine announcement ≥60 days prior = sufficient notice of Annual Meeting.
- 10.1.6: Convention Contract Guidelines incorporated by reference.
- Mid-Year (10.2.1\*\*\*\*\*): in Detroit **"or elsewhere in the USA as approved by the Executive Committee"** (new flexibility); attendee item A "Reserved"; attendees: EC, Council of Past Presidents, committee chairs, host-city committee member, ED+EA (travel reimbursed), Foundation President or designee, Magazine representative.
- No tier schedule ($20k/$30k/$40k), Relief Fund levy, ticket/ad-book rules in the bylaws — those live only in the Convention Contract, which the 2024 bylaws neither absorb nor amend.

### A.15 Entity relationships
- **Magazine** — Const. III §2: "official media source for communication among the members"; "shall operate independently with its own editorial staff and subscription management." 6.7.1: AFRP "shall appropriate the necessary funds to guarantee its publication"; subscription fee collection and policy determined by the Magazine's independently selected Board in consultation with the AFRP Board; 1 AFRP Board seat, 1-year, appointed at GA.
- **Ramallah Foundation, Inc.** — Const. III §3: separate legal entity, own mission and constitution; 1 Board seat 1-year (6.8.1); its President or designee attends Mid-Year (10.2.1G).
- **ARFECF** — Const. III §4\*: "a separate and legal entity with the mission of supporting its own approved mission and By Laws." Cross-officers: ARFECF Scholarship Fund Secretary, Educational Fund Treasurer, and ARFECF President sit on the AFRP EC (7.1.1\*), excluded from AFRP election (7.1.2\*); Educational Fund Treasurer's checks countersigned by ARFECF Board designee (7.7.1\*\*\*\*\*); membership list shared with ARFECF (8.12.7\*); Scholarship Fund Secretary is Secretary of "the Federation Scholarship Committee" (7.6.1\*).
- **ARFHSN: not mentioned anywhere** (grep-confirmed; also no "Housing"/"Senior" hits).
- **Chapter Clubs** — Const. IV; 1.2, 3.1 (affiliation requires AFRP approval; club governing laws must not conflict; must remain in good standing with State/Federal regulations); 3.2 (Aug 1 affiliation form); 15.1.1 (dissolved club assets revert to AFRP).

### A.16 Notice requirements
- Constitutional amendment: notice "sent to all Chapters" **≥60 days** before AGM (Const. XI §3). **The Magazine-publication requirement is gone** — Chapters-only notice.
- By-law amendment: member submits by mail/email to ED/EA ≥60 days before GA; Executive Assistant forwards to Constitutional Committee Chair; after review, provided to Board and Council of Chapter Club Presidents ≥45 days before GA, "who shall discuss such amendments with their Chapter Clubs"; Constitutional Committee submits recommendations for/against to GA (16.1.1).
- Annual Meeting notice: Magazine announcement ≥60 days (10.1.4).
- MAL candidacies: publicized in advance by the Magazine (6.5.2).
- Affiliation form: Aug 1 (3.2).
- Paid-members list to host: Convention −30 days (5.2).

### A.17 Amendment procedure
- Constitution: 2/3 delegate vote at AGM (Const. XI §2); 60-day notice to Chapters (XI §3); XI §1: "This Constitution supersedes in all respects, the A.F.R.P.'s previous Constitution; and, upon adoption the previous Constitution is concurrently revoked and rescinded." **Still no effective-date or non-retroactivity clause.**
- By-Laws: 16.1.1 as above; 2/3 delegate vote. Amendments are delegate-vote matters per 9.1.1(3), hence weighted fractional voting applies.
- Parliamentary authority: Robert's Rules (Const. IX §4, 12.1); President appoints a Parliamentarian **other than the Legal Advisor** for AGM and Mid-Year; Parliamentarian's decision final (12.2).

---

## B. Divergence: 2012 → 2024

### B.1 Changed rules

| Rule | Old (per reconciliation doc) | 2024 | Engine impact (vs. recon doc's final change list 1–11) |
|---|---|---|---|
| Dues authority | Annual Assembly decision (old 5.1) | **Board of Directors "from time to time"** (5.1\*\*\*\*\*) | Versioned dues-schedule pattern still right, but the approving body/motion type changes: Board resolution, not Assembly vote. Affects the dues-ladder workflow noted under recon Q6. |
| Membership year | Sep 1 – Aug 31 (old 5.1) | **Jan 1 – Dec 31** (5.1\*\*\*\*\*) | `standingAt()` (change #4) period boundaries; every "current membership year" derivation; lapse dates; renewal cycle. |
| Voting-eligibility dues deadline | Feb 28 — received (old 5.3) vs postmarked (old 8.15.5), contradictory | **Apr 30, "received... by, or postmarked by"** in both 5.3\*\*\*\*\* and 8.12.5\*\*\*\*\* | Election calendar (change #3): date moves, and the receipt/postmark question (recon Q4) is resolved as a disjunctive either-test. |
| DP filing calendar | Nov 1 postmark to Credentials → +15d Board → Dec 31 Credentials certification (old 9.3.4(3)) | **Feb 28** registered letter/in person to **Selection Committee** → +15d Board-at-large simple majority → **Mar 31** Credentials certification (9.3.4(3)) | Election calendar (change #3): three of the seven fixed dates move; receiving committee changes. |
| Ballot return deadline | Jun 20 postmark to CPA (old 9.2.2) | **Jun 10** "mail and/or email... postmarked no later than" (9.2.2); "or independent agency" alternative added (9.2.1–9.2.3) | Change #2 (mailed-ballot mode): deadline earlier; email channel added without a process; window math changes (see B.3). |
| List-certification pipeline | Membership Cmte lists by May 10 to Credentials/Election/EA (old 8.15.6); Credentials certified lists to Election Cmte + Exec Secretary by May 25 (old 8.11.2) | Membership Cmte lists to **Selection Committee** + EA by **May 10** (8.12.6); **the May 25 step and old 8.11.1–8.11.3 Credentials provisions are deleted**; "Membership and voting eligibility must be certified by the Selection Committee" (9.3.5); community vote cap keyed to Selection Committee certification (9.1.4) | Changes #2/#3: certification actor swaps from Credentials to Selection Committee; the challenge/finality路径 (old 8.11.3 "Board decision final", dues non-refundable) no longer exists. |
| Campaign-violation investigator | Credentials and/or Election Committee (old 9.4.2) | **Selection Committee** investigates; chairpersons request President call Board meeting; Board majority secret ballot (9.4.2) | Disciplinary workflow actor change. |
| Board composition | PPs + club presidents + 4 MAL + EC + 1 RBPN + 1 Magazine + 1 Foundation | Adds **1 Young Leader Committee seat** and a Board-elected **Historian** (3-yr term, special-election replacement) (6.2.2) | Board denominator (change #5 abstentions/thresholds; floating 2/3-of-all base grows by one voting seat). |
| Convention registration & dues | Old 5.2: registration included dues; **student waiver** (full-time college, under 26, photo ID) | 5.2\*\*\*\*\*: dues separate from and in addition to registration; prepayment may be a registration condition; host remits dues to General Treasurer; **student waiver deleted**; discretionary fee for non-eligible registrants | Removes one comped-membership path recon flagged under 8.15.4 (recon Q7); dues-vs-registration ledger split; new remittance handshake. |
| Standing committees list | Old list incl. Credentials (per old structure) | Const. VIII §1\*: adds Selection, Membership, Young Adults Program, Youth Program; 8.2.1\* adds Government Affairs; **no Credentials, no Election, no Scholarship Committee** in either list | Committee registry; role model (change #6). |
| Selection Committee | Old: 5-member ED-hiring body only (7.9.4) | 7.9.4's 5-member "Board Selection Committee" survives, **plus new Article XVII**: 9-member vetting/nominating body, ≤2 per city, 3-yr staggered, 6-yr cap, gates every Federation seat, replaces Credentials as membership certifier | New committee object; new eligibility gate in every election/appointment workflow; note the name collision (two "Selection Committees"). |
| Officer residency | Exec Secretary/Treasurers HQ-resident | Exec Secretary, General Treasurer, Financial Secretary, Educational Fund Treasurer may reside **anywhere in the US** if duties performable remotely, Board's sole discretion (7.4.1, 7.5.1, 7.5.2, 7.7.1, all \*\*\*\*\*) | Eligibility validation for these four offices. ED still HQ-bound (Const. V §3, 7.9.7). |
| Mid-Year location | Detroit (old 10.2.1) | Detroit **or elsewhere in USA** by EC approval (10.2.1\*\*\*\*\*) | Minor; event model. |
| Const. amendment notice channel | Chapters + **published in the Magazine** (old Const. XI §3, per recon) | **Chapters only** — Magazine publication requirement dropped (Const. XI §3) | Change #9 (notice-obligation layer): the Magazine is no longer a hard statutory gate for constitutional amendments; it remains one for Annual Meeting notice (10.1.4). |
| 10.1.2 / 10.1.3 | Had content (uncited in recon doc) | **"Reserved."** (both \*\*\*\*\*) | Whatever they contained is repealed; ruleset diff needs the old text to record the deletion. |
| DP carve-out in 9.1.3 | Recon's verbatim quote begins "Each club or community…" | 9.1.3 now opens "**Other than the election of the Deputy President,** each club or community…" | Confirms DP is outside delegate voting; mode-selector logic (change #2). |
| By-law amendment routing | (old 16.1.1 uncited in detail) | Email submission allowed; Constitutional Committee review; 45-day distribution to Board + Council of Chapter Club Presidents (16.1.1) | Notice-obligation layer (change #9). |

### B.2 Unchanged but flagged as problems in the recon doc (still open)
- **4.3.1\*\* conjunctive good standing** — unchanged; recon change #4 (conjunctive `standingAt()`) stands; the Nadia Khoury demo narrative remains wrong.
- **8.12.4\*\* own-funds rule** (old 8.15.4) — unchanged verbatim; comped/complimentary memberships still unenfranchised on a plain reading (recon Q7). (One collision removed: the student waiver is gone.)
- **Two family definitions** — 8.12.8 household vs 9.5.5 families: **both survive verbatim, still contradictory** (recon Q9).
- **No Board quorum** — 10.3.1 unchanged (recon #5 in scorecard).
- **Flat 25-member Annual Meeting quorum** with the amend-the-Constitution-with-25-people exposure — 10.1.5 unchanged.
- **9.1.3 weighted fractional voting**: no rounding rule, no delegate cap, no extraction-declaration deadline — all still absent (recon Q1).
- **6.2.4 non-reply = abstain** vs 2/3-of-all-members thresholds (6.2.1, 6.3.1) — unchanged; abstention-as-No effect persists for fixed-denominator votes (recon Q5). (7.9.10, also unchanged since 2012, excludes abstentions for simple-majority polls only.)
- **No effective-date / non-retroactivity clause** — Const. XI §1 unchanged (recon Q23, "the single most important omission").
- **2009 transitional debris in 6.5.1** ("For 2009... reduced to four (2)") — still present.
- **Board size floats** (active PPs + compliant clubs) — unchanged.
- **AFRP region map** (10.1.1) unchanged → the AFRP-vs-ARFECF two-map conflict (Houston, Knoxville, Louisville/Lexington, Santa Rosa, Atlanta) persists (recon Q10).
- **Attendance-derived Past President voting eligibility** (6.3.1) — unchanged; recon change #7 stands.
- **Automatic removal on standing lapse** (13.2) — unchanged.
- **$2,000/twice, $10,000-budget, countersignature controls** (7.2.3, 11.1.2, 7.5.x, 7.7.1) — unchanged; recon change #10 stands.
- **120-day convention accounting** (10.1.7) unchanged → the 90-day contract conflict is untouched (recon Q21) — though the contract is outside this document.
- **No conflict-of-interest rule** anywhere (recon Q16).
- **No recorded-vote right; secret-vs-open per motion unchanged.**
- **9.3.1's** odd "in Good Standing immediately **after** the election" phrasing — unchanged.

### B.3 Old-text contradictions: fixed vs left standing
| Contradiction | Status in 2024 |
|---|---|
| Feb 28 receipt (5.3) vs postmark (8.15.5) | **FIXED** — both now Apr 30, "received by, or postmarked by" (5.3, 8.12.5). |
| Jun 20 return deadline vs ballots lawfully mailable to Jun 24 (30 days after May 25 certified list) | **NOT FIXED — arguably worse.** The May 25 anchor (old 8.11.2) is deleted; 9.2.1's 30-day clock now runs from the Selection Committee "receiving the list of certified memberships" (Membership Committee delivers May 10 per 8.12.6, but certification itself — 9.3.5 — has **no deadline**), and the return deadline moved earlier to **Jun 10**. Mailing 30 days after May 10 = Jun 9, one day before the return postmark deadline; if certification takes any time, the window is negative. Recon Q3 remains open with new numbers. |
| 90-day (contract) vs 120-day (10.1.7) convention accounting | **LEFT STANDING** — 10.1.7 still says 120; the bylaws don't address the contract's 90. |
| Two family definitions (8.15.8 vs 9.5.5) | **LEFT STANDING** — now 8.12.8 vs 9.5.5, verbatim. |
| Two region maps (AFRP 10.1.1 vs ARFECF §4.1) | **LEFT STANDING** — AFRP map reprinted unchanged. |
| Membership year vs fiscal year offset | **CHANGED, not resolved** — now Jan–Dec vs Jun–May (5-month offset instead of 3); the Apr 30 deadline sits inside both. |
| Const. VIII committee list vs By-Law 8.2.1 list | **NEW/CONTINUING mismatch** — 8.2.1 claims Government Affairs is "mandated by the Constitution"; the Constitution's list omits it. Credentials/Election appear in neither list yet retain duties. |
| Receipt-vs-postmark inside 9.2.2 | **NEW** — "reach the [CPA]... postmarked no later than June 10" mixes a receipt verb with a postmark test, plus "email" with no e-equivalent. |

---

## C. The 24 open questions, rechecked

1. **Weighted delegate voting kept?** — **ANSWERED-BY-2024: kept.** 9.1.3 survives verbatim plus an explicit DP carve-out. Sub-questions (rounding precision; extraction declaration timing) — **STILL-OPEN**; the text adds nothing.
2. **DP mailed CPA ballot / electronic voting** — **ANSWERED-BY-2024, against the earlier answer the team had.** 9.2 survives as a physical mailed-ballot process (envelopes, numbering, postmark, sealed custody, draw from a bag), now with "or independent agency," a Jun 10 deadline, and the words "and/or email" in 9.2.2. **The promised electronic-voting rewrite did not happen.** The AFRP-Electronic-Voting.md design has no basis in the adopted text; flag CHANGED — the question becomes "is the e-voting design a future amendment, or must the engine implement 9.2 as written with an email side-channel?"
3. **Jun 20/Jun 24 impossibility** — **CHANGED, not resolved.** New window: certification (no deadline) + 30-day mailing clock vs Jun 10 return. Needs rewording: "what is the certification deadline, and should 9.2.1's clock be replaced with a fixed mailing date?"
4. **Postmark or receipt (Feb 28)** — **ANSWERED-BY-2024.** Now Apr 30, and the test is disjunctive: "received at the A.F.R.P's office by, **or postmarked by**, April 30th" (5.3, 8.12.5). Engine applies whichever is satisfied.
5. **Abstentions** — **STILL-OPEN** for floor votes (silent). For Board polls, 7.9.10 (present since 2012, arguably under-weighted in the recon doc) says simple majority of votes cast, abstentions/non-voters "shall not be counted" — but the 6.2.1/6.3.1 2/3-of-**all**-members thresholds remain fixed-denominator, and whether such matters may be decided by poll is unstated.
6. **Source of Patron/Manar/Life/Family/Student tiers** — **STILL-OPEN**, and sharper: 5.1\*\*\*\*\* now expressly delegates dues "amount(s) and structure" to the **Board**, so the tier ladder is legitimately a Board schedule — but the schedule document itself is still unseen. The recon's note that 5.1 made dues "an annual Assembly decision" is now wrong.
7. **Do complimentary memberships vote?** — **PARTIALLY ANSWERED.** The student waiver (old 5.2) is **deleted**, removing one collision. The own-funds rule (8.12.4) survives, so any remaining comped tier (newlywed year, scholarship membership — Board-schedule creatures) still appears unenfranchised. STILL-OPEN for those.
8. **Is 4.3.1 enforced as written?** — **STILL-OPEN.** Text unchanged; the practice question remains for the client.
9. **Which household/family definition governs payment?** — **STILL-OPEN.** Both definitions survive verbatim (8.12.8, 9.5.5).
10. **Authoritative region map** — **STILL-OPEN.** 10.1.1 reprints the old AFRP map; ARFECF divergence unaddressed; still stale vs the 26-club list.
11. **Ramallah Foundation in scope?** — **STILL-OPEN.** Const. III §3 and 6.8.1 unchanged (Board seat, Mid-Year attendee); no Foundation documents referenced.
12. **Magazine's own books?** — **ANSWERED-BY-2024 (confirming independence).** Const. III §2: "operate independently with its own editorial staff and subscription management"; 6.7.1: subscription collection and policy determined by the Magazine's independently selected Board "in consultation with" AFRP's Board. Model the Magazine outside AFRP's books, AFRP appropriating publication funds.
13. **Board Rules & Regulations / Investment policy in writing?** — **STILL-OPEN.** 6.2.1 and 8.6.2\* still cite them; nothing supplied. (The old ARFECF Endowment Policy citation is outside this document.)
14. **4% floor vs 5% cap (ARFECF)** — **STILL-OPEN / OUT OF SCOPE of this document.** The 2024 AFRP text says nothing about scholarship spend rates.
15. **Asset valuation date** — **STILL-OPEN**, same.
16. **Conflict-of-interest authority** — **STILL-OPEN.** Zero conflict-of-interest language in the 2024 text. Note the new Selection Committee (Art. XVII) is the natural home for a vetting/recusal rule but has none.
17. **SFC elected vs appointed count** — **STILL-OPEN**, with a new wrinkle: 5.3/8.12.5 still list "members of the Scholarship Committee" among positions members are certified **to vote for** (consistent with election), yet no AFRP by-law constitutes a Scholarship Committee; 7.6.1 references "the Federation Scholarship Committee" only via its Secretary.
18. **Required academic credentials** — **STILL-OPEN.** Not addressed.
19. **1% administration fee actually paid?** — **STILL-OPEN.** Not addressed.
20. **Convention tier schedule current?** — **STILL-OPEN.** Bylaws still delegate to "Convention Contract Guidelines" (10.1.6) without restating money terms.
21. **90 vs 120 days** — **STILL-OPEN.** 10.1.7 unchanged at 120.
22. **Convention operations module scope** — **STILL-OPEN** (product decision); the bylaws add one new operational handshake: host remittance of dues + the −30-day paid-list (5.2\*\*\*\*\*).
23. **Effective date / non-retroactivity clause** — **ANSWERED-BY-2024: NO.** Const. XI §1 readopted verbatim with no effective-date or savings clause. The versioned-ruleset design still has nothing textual to anchor to; the engine needs an interpretive override (treat adoption date Jul 13 2024 as the effective boundary, prospective-only).
24. **Numbers moved to an amendable schedule?** — **PARTIALLY ANSWERED.** Dues amounts: yes — 5.1\*\*\*\*\* delegates amount and structure to the Board. Everything else ($2,000/$10,000 limits, 25-member quorum, 15% trigger, 2/3 thresholds, committee sizes, dates) remains hard-coded in the by-law text.

---

## D. Ambiguities in the 2024 text itself

1. **Phantom committees: Credentials and Election.** Duties survive (Election Committee chooses the CPA/agency 9.2.1, receives sealed ballots 9.2.3, directs the tie draw 9.2.4; Credentials certifies DP candidates by Mar 31, 9.3.4(3); both chairs receive ballots pre-Convention, 9.2.3) but the old constituting provisions (old 8.11.x) are deleted and neither appears in Const. VIII §1 or 8.2.1. No size, appointment method, or challenge/finality process exists; the old "denied member's dues not refundable" and "Board decision final" rules are gone. **Provisional interpretation:** treat Credentials and Election as President-created committees under 8.1.1/8.1.3 (President appoints, 1-year terms), with membership certification residing in the Selection Committee per 9.3.5 and candidate certification in Credentials per 9.3.4(3); challenges escalate to the Board by analogy to 9.4.2, decision final. Rationale: 8.1.1 is the only surviving creation authority; 9.3.5 is explicit about the Selection Committee.
2. **Two bodies both named "Selection Committee."** 7.9.4/7.9.7–7.9.8: a 5-member, President-appointed "Board Selection Committee" for ED hiring. Article XVII: a 9-member, EC-slated/Board-approved standing Selection Committee. 9.3.4(3), 8.12.6, 9.2.x, 9.4.2 just say "Selection Committee." **Provisional:** election/certification duties → the Article XVII committee; ED hiring → the 7.9.4 committee; model them as distinct entities with distinct composition rules. Rationale: Art. XVII's mandate expressly covers seats and the DP slate; 7.9.4's is expressly the ED.
3. **Ballot-window arithmetic (9.2.1 + 8.12.6 + 9.3.5 + 9.2.2).** Certification has no deadline; the 30-day mailing clock starts on an undefined receipt event; return postmark is Jun 10. A fully lawful sequence yields a zero or negative voting window. **Provisional:** engine treats certification as due at May 10 handoff + 7 days, and mailing due **May 17** (giving ≥24 days of member voting window before Jun 10); surface any later mailing as a rule violation. Rationale: only a fixed mailing date makes 9.2.2 satisfiable; the recon doc already recommended anchoring mailing to a date.
4. **"Mail and/or email... postmarked no later than June 10" (9.2.2).** Email has no postmark; "so as to reach... postmarked" mixes receipt and postmark; email of a secret ballot to a CPA destroys ballot secrecy and the sealed-envelope custody chain (9.2.3). **Provisional:** physical ballots — postmark ≤ Jun 10; emailed ballots — server receipt timestamp ≤ 23:59:59 Jun 10 local time of the AFRP office; emailed ballots logged sealed (unopened attachment) until election day. Rationale: postmark is the stated test for the physical channel; receipt timestamp is email's only analogue; custody parity with 9.2.3.
5. **Abstention regime collision (6.2.1 vs 6.2.4 vs 7.9.10).** Rules & Regulations need "2/3 affirmative... of all members" (6.2.1); poll non-repliers are deemed to abstain (6.2.4); poll passage is "simple majority of the votes casted," abstainers "not counted" (7.9.10). Unstated: whether 2/3-of-all matters may be decided by poll at all, and if so which denominator wins. **Provisional:** 7.9.10 governs only simple-majority polls; any fixed-denominator threshold (6.2.1, 6.3.1) must be taken at a meeting, with abstentions counting against (arithmetically inevitable). Rationale: 7.9.10 states its own scope ("passage of such polling... simple majority"); a specific fixed-denominator rule overrides a general polling rule.
6. **No floor-election tie-breaker.** 9.2.4's draw-from-a-bag applies only to the DP mailed ballot; the old other-offices tie rule is gone. **Provisional:** Robert's Rules default — repeated balloting until majority/plurality resolves; offer the draw as an Assembly-adopted special rule. Rationale: 12.1 makes Robert's Rules the gap-filler.
7. **Broken cross-reference and orphaned text in 8.10.** Heading "8.10 – Constitutional Committee"; 8.10.1 says "As described in Article XV – 16.1" (Article XV is Dissolution; amendments are XVI), then the paragraph beneath describes the **Young Leader Committee** (chair + 4, Project Hope/Leadership Ramallah alumni). The Constitutional Committee has **no stated composition** despite 16.1.1 duties. **Provisional:** read the cross-reference as Article XVI 16.1; treat the Young Leader text as its own committee provision misplaced under 8.10; Constitutional Committee composition defaults to 8.1.3 (President-appointed, 1-year). Rationale: only reading consistent with 16.1.1 and the committee lists.
8. **Committee-list mismatch.** 8.2.1 includes Government Affairs among committees "mandated by the Constitution"; Const. VIII §1 omits it (it appears under 8.15.1 as Board-established). Scholarship Committee is a votable-for position (5.3, 8.12.5) but constituted nowhere in AFRP text. **Provisional:** Government Affairs = standing committee (by-law mandate suffices); Scholarship Committee = ARFECF body whose members AFRP members elect — cross-entity election needing ARFECF-side reconciliation. Rationale: 7.6.1's "Federation Scholarship Committee" + the ARFECF Scholarship Fund Secretary EC seat.
9. **Selection Committee gate vs. floor nominations and direct election.** 17.1.1 says the committee approves "every individual recommended for a vacant Federation seat, including... Executive Committee members, Deputy President"; but 9.3.1 still contemplates candidates "nominated by the Selection Committee **or from the floor**," 6.5.2 has MAL self-filing at Mid-Year, and 7.1.2 has GA election of the EC. Is Selection Committee approval a prerequisite for floor nominees? **Provisional:** Art. XVII governs *recommended slates*; floor nomination under 9.3.1 survives as an independent path (later, more specific provisions do not expressly repeal it). Flag as high-priority for a clarifying amendment — this decides whether elections are gate-kept.
10. **17.1.4 incorporates an external document**: "Please review the Strategic Planning Proposal for the full details of the committee's description and members responsibilities." The bylaws delegate operative detail to an unversioned, unattached proposal. **Provisional:** treat the Strategic Planning Proposal as a governing external document (same class as Board Rules & Regs, Investment policy, Convention Contract Guidelines); engine cannot implement 17.1.4 fully until supplied.
11. **ED residency vs. remote-work wave.** Const. V §3 requires the ED to "reside in the Headquarters metro area" and 7.9.7 requires written agreement to work from the HQ office, while all four financial/secretarial officers gained remote allowances (\*\*\*\*\*). **Provisional:** deliberate — enforce HQ residency for ED only. Rationale: the 2024 drafters touched the neighboring sections and left the ED rule intact twice.
12. **"Reserved" by-laws 10.1.2, 10.1.3 and Mid-Year attendee item A.** Deleted content with no record in-document of what was removed. **Provisional:** ruleset diff records these as repealed slots; obtain the pre-2024 text of these clauses to complete the version history (probable location of the old registration-includes-dues/student-waiver language).
13. **Candidate standing timed "immediately after the election" (9.3.1).** Literally, a non-member could be elected and then attain standing. Combined with 9.3.4(1) (DP: 3 prior years of standing), only DP has a pre-election standing test. **Provisional:** require good standing at nomination for all offices (certification via 9.3.5 implies it), with 9.3.1's "after" read as *continuing* obligation. Rationale: 8.1.2 requires prior-year standing for mere committee members; reading officers lower would be absurd.
14. **Historian vs. term-limit interaction.** Board-elected Historian, 3-year term (6.2.2) vs 9.3.3's 4×1-year cap for "each officer." **Provisional:** Historian is a Board function, not an "officer" under 9.3.3; 3-year terms renewable subject to no stated cap.
15. **"The Treasurer" ambiguity in 11.1.2.** Checks "signed by the Treasurer and countersigned by a senior officer of the Executive Committee of the home office," while 7.5.1/7.5.2 have General Treasurer co-signing with the Financial Secretary (who is an EC officer). Two countersignature formulations for the same instrument. **Provisional:** General Treasurer + Financial Secretary satisfies both (Financial Secretary = senior EC officer of home office); enforce that pairing as the default control.
16. **Membership year vs voting deadline vs fiscal year.** Jan 1–Dec 31 membership year (5.1), Apr 30 certification cutoff (5.3), Jun 1–May 31 fiscal year (8.7.2). A member paying May 1–Dec 31 is in good standing for the year (4.3.1) but cannot vote in that year's elections. Not a contradiction, but every "members in good standing" count still needs a which-calendar tag. **Provisional:** standing = membership-year basis; franchise = Apr 30 snapshot; finance = fiscal-year basis; expose all three as distinct derived sets.
17. **No electronic voting, no ARFHSN, no membership tiers.** Confirmed silences (grep: zero hits for ARFHSN/Housing/Senior/student/Patron/Manar/Life/electronic/waiver/complimentary). The AFRP-Electronic-Voting.md design, the tier ladder, and any ARFHSN entity all rest entirely on Board schedules/rules or future amendments — none on the adopted 2024 text.
18. **Typographical corruption to preserve in the canonical import**: Const. III §2 "A.F.R.P. A.F.R.P."; 6.5.1 "reduced to four (2)"; 9.3.4(3) "March 31th"; 10.1.5 "deemed to be have a quorum"; 13.2 "looses... replaced by a one"; XI §3 "voted upon a (as provided...)"; 7.1.1's "the General Fund (Treasurer; Financial Secretary)". Store verbatim with normalized readings layered as interpretations.

Files: /home/claude/bylaws/afrp-2024.txt (source, 1,334 lines); /mnt/user-data/uploads/Projects/AFRP-Portal/docs/design/AFRP-Bylaws-Reconciliation.md (superseded-text analysis compared against).