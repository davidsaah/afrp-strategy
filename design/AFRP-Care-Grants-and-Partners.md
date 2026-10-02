# Care grants and partner agreements

### How money leaves a Care fund: the grants register, the partner agreements register, the Relief Fund, the six-monthly report, club co-funding, and what the platform holds for a grant that crosses a border

**Design note P11 · 1 October 2026 · for the Hub's `funds`, `ledger`, `programs` (Care branch), the institution registry and a new `grants` module**

**What this note rests on.** Decision 63 in full (a grant or partner project paid from a Care fund is approved by the holding entity's Board with a spending ceiling, paid on delivery with two signatories, and closed only when the receiving partner's signed agreement, a delivery confirmation and an inventory of any equipment are on record; no approval tiers until ARFHSN adopts a finance manual written for a volunteer board; the platform produces ARFHSN's six-monthly report to the AFRP Board from the ledger and the grants register), with D55, D56, D57 and D62; the `care-grants` and `partner-agreements` workflows in `site/data/workflows.yaml`; the programme register entries for the Medical Mission, Women to Women, the Relief Fund, Senior Living and Project Hope; the crosswalk rows F13, F14, F15, F17 and J1; ARFHSN's By-Laws and Organizing Document (approved 2015, Article III §9 amended 2017; `design/bylaws/ARFHSN-Bylaws-2017.pdf`), read in full; the rules register's ARFHSN rows (HS-OV-1 to -8; R39); the open questions Q-23 and Q-24 (settled by D63 as to the closing records), Q-21 (settled by D56) and Q-22 (settled by D62); and the ARFHSN intake of 30 September 2026 (its board and finance cards and its Medical Mission cards), cited at role level and without figures, as D54 requires. It builds on `AFRP-Fund-Rules.md` (P9): a grant draws on a fund object of that note's §2 and inherits its entity, kind and restriction. Outside the record: the IRS guidance on grants by US charities to foreign organisations, the Form 990 Schedule F instructions, Treasury's anti-terrorist financing guidelines for charities and the OFAC counter-terrorism programme, cited in the Sources and used only to say what record the platform should hold and what counsel should be asked.

This note adds no decision. Where it reads as a rule, the rule is a by-law cited by number, a decision cited by number, a rules-register row, or a *design choice* labelled as such. Where the record is silent it says so and raises a question with an owner.

**Precedence (D41).** ARFHSN's by-laws (2015/2017) are a text and outrank everything below them. D63, D55, D56, D57, D62, D66 and the named design documents come next. Nothing in the prototype covers grant-making: the `#/program/medops` and `#/program/intake` screens evidence a story about the Mission's operations and a sensitive-intake store, never a rule about money leaving. Nothing in the Hub is built for it (`module: none yet`). The draft ARFHSN Finance and Accounting Manual (2026) is unadopted and was adapted from a staffed organisation's manual; it binds nothing and its tiers are not taken (D63; Q-23).

**Public-repository rule.** No living person, no partner institution by name beyond what the programme register already says ("a university with a prosthetics workshop and a rehabilitation centre"), no donor, no figure, no account.

---

## 1. What the record already holds

**Built.** Nothing of the outbound side. What exists beside it: the fund boundaries and restricted-purpose engine (P9 §1); the exact-scope grants of R39, under which Federation scope does not read into the ARFHSN store; the four contributor moments designed and not built (D10); the club statement designed (Club Experience Plan §5) with "Care co-funding" as one of its sixteen line types.

**Decided.** The Medical Mission is a programme of ARFHSN; ARFHSN's Board appoints its chair and approves its spending; the Federation President convenes (D62). Gifts to the Medical Mission and Human Services Network funds are ARFHSN's, receipted by ARFHSN, collected by the Federation's pages as its agent and forwarded without delay (D56). Women to Women is a sub-fund of ARFHSN (D55). How money leaves a Care fund is D63. A co-funded grant lists each club's share and every gift may carry a club attribution (D57). The shared drive is the archive of record and the platform links to it (D66). A programme's holding entity is the fund that budgets it (D55), which leaves the Relief Fund unnamed (F15).

**The text: ARFHSN's by-laws, as read.** ARFHSN is a Michigan non-profit NGO with AFRP as its supporting organisation (Art. I); AFRP is described as a 501(c)(4) and ARFHSN complies with 501(c)(3) (Art. III §1, §7). A fourteen-member Board of Trustees elected by the AFRP Board, all AFRP members in good standing, six from the AFRP Board and eight independent, by metro community (III §2); two consecutive terms (III §3). The Chairman is elected by the trustees and votes only to break a tie; the Treasurer and the Executive Administrator must be the two Detroit-area trustees, because the office is in the Detroit club's building; "all major decisions must be taken upon consultation with the chairman, who will decide when a vote of the BOT is necessary" (III §4). **"All checks authorized by the BOT must be cosigned by two signatures to be designated by the Board"** (III §5). Trustees are unpaid (III §6). **The trustees "supervise, manage, and administer the programs and funds of ARFHSN", limited by the AFRP Board's directions and policy decisions, and "shall submit to the AFRP Board of Directors, beginning six months after its election, and every six months thereafter, a financial and operational report"; the AFRP President may request information between reports and the officers must comply** (III §7). Employment contracts at director rank and above need the AFRP Board (III §8). The AFRP Board retains a certified accountant from outside the Ramallah community to certify the funds and grants received; the fiscal year is 1 June to 31 May (III §9). Two million dollars of liability insurance with an endorsement covering AFRP (III §10). The AFRP Board amends the by-laws by 60% with the whole Board polled (Art. V). A five-member committee under the Chairman to pursue USAID grants (Art. VI). The by-laws name **no signatory for agreements, no approval threshold, no grant procedure and no quorum for the trustees** (HS-OV-7). The trustee roster with seats and term dates is not on file (Q-2), so the six-month clock in III §7 has no recorded start.

**Historically (the intakes, role level, no figures).** ARFHSN's Board, meeting monthly by video call with the AFRP President often present and AFRP's officers copied on every summary, takes a funding request from the Medical Mission committee or a partner with two or three supplier quotes, discusses fit and donor intent, prefers a local supplier for price, warranty and maintenance, **votes an amount "or less"** as a ceiling, has the chair sign a purchase agreement where one is needed, **pays on delivery**, and lets the supplier handle the VAT exemption with ARFHSN's exemption form; a committee review of project invoices before payment was proposed in 2023 and never formalised. A major donor's project fund is held in a dedicated brokerage account; in 2023 the Board refused to move its income to operations because income follows the restriction; payments for that donor's projects are drawn from that account. The Ramallah bank account needs two local signatures (the Federation's representative in Ramallah and a second local signer, hard to find in 2021); it froze once over a lapsed NGO registration and once for inactivity. The 2023 Gaza response ran as a Medical Mission fundraiser branded as such, with over nine-tenths of the money arriving through the Federation's giving pages and forwarded on the Federation treasurer's reading that forwarding "within a reasonable time" preserves deductibility (now D56); the Ministry's supply list and volunteer physicians' needs lists were merged into one purchase sheet with a goal; local-supplier invoices were paid by wire with the supplier's bank certificate and an exchange-rate record filed; humanitarian transfers went to a Gaza hospital, a church body and a parish shelter, some routed from the Network to the Mission, and the Mission minutes record that the boundary between the Mission and the Network's relief work is unresolved. An inventory by the Federation's representative found equipment missing from a Ramallah hospital; since September 2023 the Board has proposed an inventory of delivered items, random inspections, a security agreement drafted by AFRP's legal advisor and signed by the hospital, a local ARFHSN committee in Ramallah and a committee of trusted people to account for supplies, and none is written (Q-24). In 2025 the Federation President wrote to the Ramallah institutions that the Medical Mission is the sole authorised channel for a major donor's healthcare gift. The prosthetics agreement (2025) is a three-party memorandum between a university's prosthetics workshop, "the Federation's Human Services Network" and a rehabilitation centre, with the Minister of Health as witness and not a party: a one-year term, renewal agreed at least 30 days before expiry or it lapses, amendments by written consent of all three, disputes amicably then in the Ramallah courts, obligations on each side and a per-case price annex; it was **signed for the Federation by ARFHSN's president**, and its renewal fell due in September 2026 with no renewal record found. An earlier draft with an annual budget for three years and an oversight committee of two Ramallah-based members and a centre representative was superseded by the signed text. One club funds a medication subsidy each year; another supplied part of a Ramallah transfer and has run Mission fundraisers; relief money for one community passed through ARFHSN's account to its club in 2017; Women to Women pledges to projects from its own account; club presidents were briefed to run local appeals in 2020. The Federation's 2020 Board stopped individual fundraising for relief outside the Federation's procedure and brought unauthorised collections into the Relief Fund; a Federation resolution that money goes to people and not to the municipality is why ARFHSN, not the Federation, took a sanitation project. The six-monthly report has been seen presented once (November 2023); the USAID committee is not seen; a CPA review rather than an audit is under way for 2026; ARFHSN decided in August 2026 to move to QuickBooks with accrual accounting and CRM-generated receipts; its revised by-laws are in committee for the AFRP Board's vote.

---

## 2. The grants register

A grant is the object D63 describes. One register across the Care funds, scoped by holding entity (R39: the ARFHSN store is read only at ARFHSN's scope or by an exact grant), with these states. Each transition is a dated act by a named role; nothing is deleted; a correction is a new act naming the old.

| State | Record the act carries | Who | Rule |
|---|---|---|---|
| **Requested** | Purpose; the receiving partner (from the partner register, §3); the programme; the fund it would draw on; the quotes (two or three, each a document on the drive, D66); the kind (equipment purchase, partner project, humanitarian transfer, per-case programme, recurring subsidy, grant to a club); the currency of the quotes | Programme committee, for a partner or a committee member | Observed practice; `care-grants` step 1 |
| **Checked** | Fit with the programme; the fund's restriction covers the purpose (a restricted donor's project fund only its projects; a sub-fund only its purposes); the purpose as it was published to donors when the money was raised (D7, D8); any club share proposed (D57) | Programme committee; the platform shows the restriction check | D2, D3 (restriction follows the gift); D8; the 2023 and 2024 donor-intent findings as practice |
| **Approved** | The Board's vote with a date; the **ceiling**; the fund; the partner; the purpose; who moved and the count; whether the chair's tie-break was used (III §4); no approval tier | The holding entity's Board (ARFHSN's for the Medical Mission, Women to Women and Human Services funds) | D63; D62; D55; ARFHSN III §4, §7 |
| **Agreed** | The partner agreement on the agreements register (§3), signed; for a supplier purchase, the purchase agreement or order | Entity chair or designated signatory | D63 (required for close); `care-grants` step 5 |
| **Paid** (one or more payments) | Each payment: amount, within the ceiling; currency and the conversion evidence where the invoice is not in dollars; the account it left (US or Ramallah); the invoice; **two signatories by role**; the delivery it pays for | Entity treasurer and a second designated signatory | ARFHSN III §5; D63 ("paid on delivery") |
| **Delivered** | A delivery confirmation: who confirmed, when, what arrived, where; the partner's acknowledgement | The Federation's representative in Ramallah; the receiving partner | D63 |
| **Inventoried** | For equipment: each item, identifier, location, custodian, date; a link to the partner's security agreement where one exists | The Federation's representative in Ramallah; the partner | D63; the 2023 proposals (Q-24) |
| **Closed** | The three closing records on file; outcome recorded; contributors told the funds were transferred and the purpose fulfilled (D10); the Board informed | Platform refuses to close without all three | D63 |
| **Lapsed / withdrawn** | A request not approved, or an approval not paid within the period the Board set | The Board, or the clock | *Design choice* |

**What the register refuses, by name.** A payment above the ceiling; a payment with one signatory; a payment while the fund's holding entity is unset (P9 rule 1; the Relief Fund today, §4); a payment from a fund whose restriction does not cover the purpose; a close without the signed agreement, the delivery confirmation or the inventory; a tier-based approval (D63 says none exists; a request that names a tier is a defect); a grant to an individual (the register has no object for it: relief to families runs through a partner on lists the platform never holds, §4 and §7).

**The signatories are a register row, not a guess.** III §5 says two signatures "designated by the Board" and the record does not say who they are by role. The row holds the designated roles for each account (the US operating account, the restricted brokerage accounts, the Ramallah account) with the Board's designation date; until a row is filled, payment from that account refuses and names III §5. *Q-104.*

**Delivery and the per-case shape.** The prosthetics agreement pays per patient on a medical and financial report, and the centre a fee per completed case: a grant of the kind *per-case programme* carries a ceiling for the year, each case a payment within it, each case's delivery the partner's completion report, and **no patient data**: the platform holds the case count and the amount, never a name or a diagnosis (programme register, data classes). *Design choice.* The same shape serves a medication subsidy (a monthly count and amount) and the Relief Fund's monthly support (§4).

**Currency.** Invoices in shekels were paid in dollars with an exchange-rate record. A payment carries the invoice currency, the dollar amount, the rate and its evidence; the ledger posts in dollars (R20's gross rule applies to the dollar amount). *Design choice.*

**Where the money came from.** A grant draws on a fund (P9 §2): a Care fund, a sub-fund, a restricted donor's project fund in its own account, with the restriction check at *Checked*. Money raised by an appeal under D8's catalogue is spent on that purpose; the Board's 2024 reading that a published wording ("humanitarian and medical needs for Palestine") covered a West Bank project from a Gaza appeal is a finding the Board records on the grant, not a rule the platform applies. The platform shows the purpose as published at the gift.

**Approval tiers.** None, by D63, until ARFHSN adopts a finance manual written for a volunteer board (Q-23). The draft manual's thresholds, roles and petty-cash rules are not modelled, and a register row for a future manual holds no value.

**Federation grants to clubs** (start-up stipends, revival travel, the 2017 relief pass-through) have no written procedure (`care-grants` open item). They are not Care grants; they are General Fund lines decided by the Board by number (Club Experience Plan §5.2, "grant to a club"). Whether they run on this register as the kind *grant to a club* with the AFRP Board as the approver and 7.2.3's limits in place of a Care ceiling is for David; the kind is modelled and gated. *Q-105.*

---

## 3. The partner agreements register

One register for every agreement with an outside party that a programme runs under, serving the Medical Mission first and the Arabic teaching partner, the scanning vendor, sponsors, foundation grants received and the Convention and Mid-Year host agreements (D59; P13) on the same object.

| Field | What it holds | Source |
|---|---|---|
| Parties | The outside parties by organisation; the entity that carries the obligation on this side | D55 (the fund that budgets the programme carries it); D62 for the Mission |
| Kind | Partner memorandum; supplier purchase agreement; security or custody agreement for equipment; host agreement; sponsorship; teaching partner; foundation grant received | `partner-agreements` workflow |
| Programme and grant | The programme it serves; the grants that depend on it | §2 |
| Term | Start, end; whether it lapses or renews; the renewal condition as the text states it (the prosthetics text: renewal agreed at least 30 days before expiry, otherwise it lapses) | The agreement |
| Notice period | The agreement's own notice; **no default** where the text has none | `partner-agreements` open item; *Q-106* |
| Obligations | Each side's, as the text states them, and the schedule of fees or shares as register rows (figures on the register, not in any note) | The agreement |
| Witness; dispute forum; amendment rule | As the text states them (the prosthetics text: a Ministry witness who is not a party; amicable settlement then the Ramallah courts; amendment by written consent of all parties) | The agreement |
| Signatory | The role that signed for this side, and the authority it signed under | *Q-107* (§3.1) |
| Documents | The signed copy and annexes linked on the drive; the platform keeps the register, not the document | D66 |
| Compliance record | The partner's screening act and the use-of-funds reports (§8) | *Q-111*, *C9* |
| Renewal decision | Renew, renegotiate or let lapse, with its date and the body that decided | `partner-agreements` step 8 |
| Status | Draft; signed; in force; renewal due; lapsed; superseded (with the superseding agreement named); a note may add states its object needs (P13 §2.9 adds *approved* and *closed*) | *Design choice* |

### 3.1 Who signs, and for whom

The prosthetics memorandum was signed by ARFHSN's president "on behalf of the Federation". Under D55 and D62 the obligation is ARFHSN's: the fund that budgets the Mission is ARFHSN's, and ARFHSN pays. The register records the entity that carries the obligation and the role that signed, and shows a mismatch (an agreement signed in one entity's name for another's programme) rather than correcting it. Who may sign for each entity is not in the record: ARFHSN's by-laws name no signatory for agreements (III §5 is about cheques); AFRP's By-Law 11.1.1 lets the Executive Committee and Board jointly authorise an officer to execute an instrument and requires the Executive Committee, including the legal advisor, to approve the final language before execution; ARFECF's text names the President and Treasurer for cheques and nothing for agreements. The platform holds a signatory row per entity, by role, with the authority cited, and refuses to mark an agreement *signed* for an entity whose row is empty. *Q-107.*

### 3.2 The renewal reminder

The platform reminds the programme committee and the entity's chair before each agreement's expiry, at the agreement's own notice period, and again on expiry; an agreement past its renewal date with no decision recorded shows *renewal overdue* on the programme's page and on the six-monthly report. The first case is the prosthetics agreement, whose renewal check fell due in September 2026 and is not on record: on the day the register is loaded it shows overdue, and the ARFHSN chair is asked (the intake's question 3 to David). Where an agreement states no notice period the reminder fires only at a date the committee sets on the register; the platform proposes none. *Q-106.*

### 3.3 Grants received

Foundation grants received by ARFECF (two funders, with report deadlines and conditions such as no lobbying and no sanctioned recipients) have the same shape seen from the other side: a term, obligations, reports due, a signatory. Whether they sit on this register is an open item of the workflow; the object fits, and this note proposes they do, as a kind, so that one calendar holds every report deadline. *Design choice, for the owning agent to confirm; Q-108.*

---

## 4. The Relief Fund

**What the record holds (F15).** Monthly support to families in Ramallah since 2020, voted by the Federation's Board in an emergency (extended in 2021) with a distribution plan required; the Federation's representative in Ramallah distributes to families on lists supplied by local partners, and recipients are told the Federation is the source; fundraising for it only through the Federation's procedure (the 2020 Board, and By-Law 11.1.4); a separate bank account with its balance in each Board packet; a per-registrant amount from each Convention under the host-agreement template; the approved budget funds the Ramallah charities page from it by a Convention decision; relief donations appear as income on the Educational Fund page; Women to Women has given to it; in 2017 it transferred to ARFECF's operating account for Medical Mission equipment; the Mission minutes propose splitting a humanitarian request between the Mission and "the relief fund".

**What is not stated.** Its holding entity: the budget page is the Federation's, the income line sits on the Educational Fund page, and D55 does not name it. The answer has a consequence the record should see before the Boards choose: AFRP is a 501(c)(4) (ARFHSN Art. III §1; the 2011 IRS letter in the officer archive), so a Relief Fund held by AFRP receipts gifts with no deductibility statement, while one held by ARFECF or ARFHSN does, under that entity's determination (ARFECF's letter is missing, P9 §9). Also not stated: who approves each monthly transfer once the Board's vote has set the support; where the Federation's relief ends and ARFHSN's relief projects begin; whether D63's closing records apply (they do only if the fund is a Care fund held by ARFHSN); and whether the partners' family lists ever enter any Federation system.

**What the platform does until the entity is named.** The Relief Fund exists on the fund register (P9 §2.1) with its entity unset, and posts nothing; its page says so and names D55 and F15. Gifts to it on the Federation's pages are a catalogue purpose (D8) held as a liability to *the entity to be named*, with the receipt carrying no deductibility claim, so that nothing is promised the Boards may not be able to keep. *Design choice.* Once the entity is named, the monthly support is a grant of the kind *recurring* on the register: the Board's vote and the distribution plan are the approval act with a ceiling per month and a term; each month's transfer is a payment with two signatories; the representative's distribution report is the delivery confirmation; there is no equipment and no inventory; the report carries counts of families and the amount, **never the lists**. The family lists stay with the partners and the representative, outside the platform, on the same principle as D61's rule for minors' documents and the Mission's rule on patient data. *Design choice; Q-109 and C7.*

---

## 5. The six-monthly report

ARFHSN's by-laws require "a financial and operational report" to the AFRP Board beginning six months after the trustees' election and every six months after (III §7); the record shows it presented once. D63 makes the platform produce it from the ledger and the grants register.

**Assembled, per period, per fund held by ARFHSN:**

- opening and closing balances by account and by fund, from the ledger (the daily close, R22), including the restricted donor funds and the Women to Women sub-fund;
- gifts in by fund and channel: collected by the Federation as agent and forwarded, with the forwarding dates (D56); direct; by club attribution as counts (D57);
- grants by state: requested, approved with ceilings, paid, delivered, inventoried, closed, lapsed; payments against ceilings; refusals the register made (a second signatory missing, a close attempted without its records), as counts;
- agreements in force, renewals due in the next period, renewals overdue;
- club co-funding lines raised and settled (§6);
- missions held and volunteers who travelled, as counts (the mission as an event type is the programme register's item, not this note's);
- the compliance calendar: the NGO registration renewal in Palestine, the Form 990 and the CPA review or audit (III §9), the insurance (III §10), the Ramallah account's status;
- the Board's votes in the period, by date and subject;
- what the AFRP President requested between reports and when it was answered (III §7).

**As an act.** The ARFHSN Treasurer assembles; the Chairman approves; the report is delivered to the AFRP Board as a dated document linked on the drive (D66) and its figures are the ledger's at the close, never retyped. The six-month clock runs from the trustees' election date, which is not on file (the roster is missing, Q-2): the clock starts from a register row the ARFHSN Board fills, and until then the report is produced on demand and labelled so. The same assembly serves the Care branch's year-one baseline (D67: grants made and delivered, mission volunteers) and the annual report of the Federation's own funds policies (P9 §8). *Design choice for the assembly; the duty is III §7.*

---

## 6. Club co-funding (D57)

- A club's share of a grant is a line on the club's statement against ARFHSN (Club Experience Plan §5.2, "Care co-funding": club → ARFHSN; raised by the club's gift or pledge against a grant; D57, D63). A co-funded grant lists each club's share, pledged and paid, on the grant and on the six-monthly report.
- A club-attributed gift to a Care fund is attribution, counted on the club's statement and never the club's money (D57; Club Experience Plan §5.4).
- A club appeal for a Care purpose is a club event whose receipts go to the holding entity under the purpose catalogue (D8, D56); whether it needs By-Law 11.1.4's authority ("a Chapter Club … shall not solicit any funds in their individual capacity for any project already undertaken by the A.F.R.P. unless authorized …") is open (Club Experience Plan §7).
- A committee sub-fund (Women to Women) is the pattern for a club or committee fund held under ARFHSN's exemption: its own account, its own purposes, its spending through this register with ARFHSN's Board as the approver (D63), reported inside ARFHSN's books. Whether the Women to Women committee's own approval of a project is a step before the Board's or is the Board's by delegation is not written (the programme register's question); the platform records both as acts and requires the Board's.
- A pass-through to a club (relief money for a club's community, 2017) is a grant of the kind *grant to a club* (§2) and is gated with it.

---

## 7. What stays outside the platform

- **Inspections and the local committee in Ramallah** (Q-24): proposed since 2023, not written. The platform holds the inventory and links an inspection report when one exists; it does not schedule inspections or seat a committee no text constitutes.
- **The security or custody agreement with a receiving hospital**, drafted by the Federation's legal advisor: when signed it is an agreement on the register (§3, kind *security agreement*) linked to the inventory; its drafting is outside.
- **The Ramallah bank account** and its two local signatories, its registration with the Palestinian authorities and its reactivation: outside. The platform records which account a payment left and holds the NGO registration renewal as a calendar item on the compliance record so the lapse that froze the account is at least foreseen.
- **Volunteer credentialing**: no step exists in any record; the platform does not invent one (programme register).
- **Patient data, beneficiary lists, partners' per-patient reports**: never enter (programme register; §4).
- **Sanctions screening itself**: the platform records that a named person screened a partner on a date against a named list and what they found; the platform never screens, never pronounces, and never holds a list of individuals (§8).

---

## 8. The foreign-grant compliance record

Every Care grant in the record pays a partner outside the United States. The record is silent on what ARFHSN keeps to show that such a grant is a charitable expenditure under its own control, and silent on sanctions. This section says what the platform should be able to hold, and puts the rules themselves to the CPA and the Legal Advisor as questions. Nothing here is a rule until one of them says it is.

**What the public guidance says, in outline.** The IRS has long held that a US charity may fund a foreign organisation's work and keep its own exempt purpose, and that gifts to it stay deductible, where the charity **retains discretion and control over the use of the funds, keeps records showing they were used for exempt purposes, and limits distributions to specific projects** (Rev. Rul. 68-489 and, on deductibility of gifts later sent abroad, Rev. Rul. 63-252 and 66-79, as IRS Announcement 2003-29 summarises them). The Form 990's Schedule F asks, for grants to foreign organisations and foreign individuals, the region, purpose, amount and method of disbursement, and asks the organisation to describe **how it monitors the use of the grants**. Treasury's Anti-Terrorist Financing Guidelines (voluntary best practices for US-based charities) describe collecting basic information on a foreign recipient, checking it against the government's sanctions lists, and documenting the check. The Office of Foreign Assets Control's counter-terrorism programme lists designated persons and organisations, and dealings in Gaza and the West Bank are where that list bites; general licences for humanitarian activity exist and are specific to a programme and a time, so whether any applies is counsel's question, not the platform's. ARFHSN's own by-laws oblige the trustees to comply with directions that preserve its 501(c)(3) status (III §7), and the foundation grants ARFECF receives already bind it to no lobbying and no sanctioned recipients. "Expenditure responsibility" and "equivalency determination" are the private-foundation rules (section 4945); whether the CPA wants ARFHSN, a public charity, to keep an equivalent record is for the CPA.

**What the platform holds, as fields on the partner and the grant (§2, §3):**

| Record | Held as | Who writes it |
|---|---|---|
| The partner's identity and standing: organisation, registration in its jurisdiction, officers by role, the documents on the drive | Partner register fields with document links (D66) | Programme committee |
| A pre-grant inquiry on the partner (what it does, who runs it, what it will do with the funds) | A dated act with its document | Programme committee |
| The written agreement limiting the use of funds to the project, with a reporting duty on the partner | The agreement (§3), with its *use-of-funds reporting* term | Entity signatory |
| The partner's use-of-funds reports and any site confirmation | Documents on the grant, dated; the delivery confirmation and inventory of D63 are the first of them | Partner; the Federation's representative |
| The sanctions check: who checked, on what date, against which list, and the result | A dated act by a named person; **the platform never performs it and never records a verdict of its own** | The role counsel names |
| The Schedule F extract for the tax year: region, purpose, amount, method, and the monitoring description drawn from the records above | A report assembled from the register | Platform; the CPA reviews |
| Counsel's answer on any general licence or other authority relied on for a Gaza or West Bank payment | A document linked on the grant | Legal Advisor |

**The questions, with owners.** What record the CPA wants for each foreign grant to meet the discretion-and-control standard and to complete Schedule F (*Q-111*, CPA). Who screens a partner, against which list, how often, and who may release a payment where a match is possible (*Q-112*, Legal Advisor · ARFHSN Board). Whether any OFAC authorisation is relied on for payments into Gaza and the West Bank, and how a humanitarian transfer to a church body or a hospital is documented (*Q-113*, Legal Advisor). Whether the forwarding of Federation-collected gifts to ARFHSN (D56) needs a written agency agreement for the CPA's purposes (*Q-3*, carried). Whether ARFECF's Care-adjacent spending (Ramallah charities from the Relief Fund on the Educational Fund page) is a foreign grant on ARFECF's Schedule F (*Q-111* again, with the Relief Fund's entity, *Q-109*).

---

## 9. Rules

1. A grant from a Care fund is approved by the holding entity's Board with a spending ceiling, as a dated vote (D63; D62; D55).
2. It is paid on delivery, each payment within the ceiling, with two signatories designated by the Board (D63; ARFHSN III §5); a payment refuses while the account's signatory roles are unset (*design choice*; *Q-104*).
3. It closes only when the partner's signed agreement, a delivery confirmation and an inventory of any equipment are on record (D63).
4. No approval tiers apply until ARFHSN adopts a finance manual written for a volunteer board (D63; Q-23).
5. A grant draws on a fund whose holding entity is set and whose restriction covers the purpose as published to donors (D55; D7; D8; P9 rule 1); a restricted donor's project fund funds only its projects (D2, D3 by analogy; ARFHSN practice 2023).
6. Every agreement with an outside party is on the register with its parties, term, obligations, signatory, documents on the drive and renewal decision (D66; `partner-agreements`); the entity that carries the obligation is the fund that budgets the programme (D55).
7. The renewal reminder fires at the agreement's own notice period; where the text has none, at a date the committee sets, and the platform proposes none (*design choice*; *Q-106*).
8. An agreement is marked signed for an entity only by a role that entity's register row names (*design choice*; *Q-107*; AFRP By-Law 11.1.1 for AFRP's own).
9. A co-funded grant lists each club's share; a club-attributed gift is a count, not the club's money (D57).
10. The platform produces ARFHSN's six-monthly financial and operational report to the AFRP Board from the ledger and the register, as a dated act approved by the Chairman (ARFHSN III §7; D63).
11. The Relief Fund posts nothing until a Board names its holding entity; its receipts claim no deductibility until then (D55; P9 rule 1; *design choice*).
12. Beneficiary lists, patient data and per-patient reports never enter the platform; a per-case grant holds counts and amounts (programme register; *design choice* following D61's shape).
13. Inspections, the local committee, the Ramallah account's signatories and sanctions screening are outside the platform; the platform holds the dated record that a named person did them (Q-24; *design choice*).
14. A foreign payment carries the compliance record of §8 as fields; the rules behind the fields are the CPA's and the Legal Advisor's to state (*Q-111* to *C10*).
15. Every state change is a dated act by a named role; nothing is deleted (R24's shape).
16. Figures stay on the register and the ledger, never in this note (D54).

---

## 10. What this note raises

| Q | Question | Owner |
|---|---|---|
| Q-104 | Who the two signatories designated under ARFHSN By-Law III §5 are, by role, for each of ARFHSN's accounts (the US operating account, the restricted brokerage accounts, the Ramallah account), and the date the Board designated them | ARFHSN Board |
| Q-105 | Whether Federation grants to clubs (start-up stipends, revival travel, relief passed through to a club) run on the grants register with the AFRP Board as approver and By-Law 7.2.3's limits, or stay a budget line outside it | David · AFRP Board |
| Q-106 | The renewal notice for an agreement whose text states none; whether a Board-wide default is wanted at all | ARFHSN Board · programme committees |
| Q-107 | Who may sign an agreement for each entity, by role and under what authority; and whether the prosthetics agreement, signed by ARFHSN's president "on behalf of the Federation", binds ARFHSN, AFRP or both | ARFHSN Board · AFRP Executive Committee · Legal Advisor |
| Q-108 | Whether foundation grants received (and their report deadlines) sit on the agreements register as a kind | David · the programme director role |
| Q-109 | The Relief Fund's holding entity (AFRP, ARFECF or ARFHSN), with the deductibility consequence stated; who approves each monthly transfer after the Board's vote; whether D63's closing records apply to it | AFRP Board · ARFECF Board · ARFHSN Board · CPA |
| Q-110 | Where the Federation's relief ends and ARFHSN's relief projects begin; whether the partners' family lists ever enter any Federation system (this note says never) | AFRP Board · ARFHSN Board |
| Q-111 | What record ARFHSN (and ARFECF, for Ramallah charities) keeps for each grant to a foreign organisation to meet the IRS discretion-and-control standard and Form 990 Schedule F, and whether an expenditure-responsibility-style file is wanted | CPA |
| Q-112 | Who screens a partner against the sanctions lists, how often, which list, and who may release a payment where a match is possible | Legal Advisor · ARFHSN Board |
| Q-113 | Whether any OFAC authorisation is relied on for payments into Gaza and the West Bank, and how humanitarian transfers to church bodies and hospitals are documented | Legal Advisor |
| Q-114 | Whether the Women to Women committee's approval of a project is a step before ARFHSN's Board or the Board's approval by delegation | ARFHSN Board · Women to Women Committee |

Carried, not new: Q-23 (the finance manual), Q-24 (safeguarding beyond the three records), Q-2 (the trustee roster, which starts the six-month clock), Q-3 (the CPA on agency), the programme register's credentialing question, and Club Experience Plan §7's 11.1.4 question.

---

## 11. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| CG1 The grants register | The grant object and its states (§2), scoped to the holding entity under R39; kinds; the restriction check against the fund (P9 FR1); the ceiling; the Board vote as a dated act; refusals by name; the club-share list (D57) feeding the club statement's Care co-funding line (C3) | §2, §6 | P9 FR1 (fund objects) first; the signatory rows may stay unset (the refusal is the behaviour) |
| CG2 The partner agreements register | The agreement object (§3) with kinds, terms, obligations as register rows, signatory rows per entity, documents on the drive, the renewal reminder at the agreement's own notice, the overdue state, the renewal decision; the prosthetics agreement as the first load, entered by the office from the drive, showing overdue on day one | §3 | None; Q-106 and Q-107 are register rows |
| CG3 Payment, delivery, inventory, close | Payments with two signatories by role, currency and conversion evidence, the account; the delivery confirmation and the equipment inventory as acts by the Ramallah representative; the per-case and recurring shapes with counts and no beneficiary data; close only on the three records; contributor notices at transfer and fulfilment (D10) | §2 | CG1; D10's notices depend on the comms rows of `giving-funds` |
| CG4 The six-monthly report | The assembly of §5 as a dated act approved by the Chairman, delivered to the AFRP Board and linked on the drive; the clock from a register row; the Care baseline counts (D67) from the same assembly | §5 | CG1–CG3 for content; produces on demand until the election date is on the register |
| CG5 The Relief Fund | The fund with entity unset posting nothing; gifts held as a liability to the entity to be named with no deductibility claim; once named, the recurring grant with the Board's vote as approval and the representative's report as delivery; family lists never modelled | §4 | Q-109 for posting; the holding shape builds now |
| CG6 The compliance record | The partner fields of §8, the dated screening act by a named person, the use-of-funds reports, the Schedule F extract per tax year and entity | §8 | Q-111–Q-113 for the rules; the fields build now and stay empty |

Order: P9's FR1 before anything here; then CG1 and CG2 together (the agreement is the grant's closing record and the Mission's renewal is overdue today); CG3; CG4 once a period of data exists; CG5 and CG6 as their gates lift. Four sessions, on the master plan's standing loop.

What the Hub's record should take in the same pass: ARFHSN's by-law citations for the Care lens (Art. I; III §1, §2, §4, §5, §7, §9, §10; Art. V; Art. VI) on the rules register's ARFHSN rows; HS-OV-7's quorum gap noted on the vote act; R39's exact-scope grant as the access rule for the grants register; the `care-grants` and `partner-agreements` workflows moved from "Proposed" to "Designed" with this note as the design.

---

## 12. Journeys proposed

Identifiers are provisional; the Hub's workbench assigns catalogue ids.

| Journey | Tests | Must reach | Slice |
|---|---|---|---|
| P11-J01 A grant is approved by the holding entity's Board with a ceiling | A Medical Mission request lands with quotes; the ARFHSN Board's vote records the ceiling and the fund; the AFRP Board, the committee and an officer are each refused the approval step by name (D62, D63) | meets | CG1 |
| P11-J02 No tier exists | A request that names an approval tier is refused; the manual's thresholds appear nowhere | meets | CG1 |
| P11-J03 The restriction is checked before the vote | A request drawing on a donor's project fund for a purpose outside its projects refuses at *Checked*; the purpose as published at the gift is shown | meets | CG1 |
| P11-J04 Two signatories or nothing | A payment with one signatory refuses (III §5); with the account's signatory roles unset it refuses and names Q-104; with both it posts within the ceiling; one over the ceiling refuses | meets (the refusals) | CG3 |
| P11-J05 Paid on delivery, closed on three records | A payment before a delivery confirmation refuses; a close without the inventory refuses; with the agreement, the confirmation and the inventory it closes and the contributors hear (D10) | meets | CG3 |
| P11-J06 A per-case grant holds counts, never patients | The prosthetics grant records cases and amounts within the year's ceiling; no field accepts a name or a diagnosis | meets | CG3 |
| P11-J07 A payment in another currency | A shekel invoice is paid in dollars with the rate and its evidence; the ledger posts the dollar amount gross | meets | CG3 |
| P11-J08 The renewal is overdue on day one | The prosthetics agreement loaded from the drive shows *renewal overdue* with its 30-day term; the committee and the chair are reminded; a renewal decision clears it | meets | CG2 |
| P11-J09 No default notice | An agreement whose text has no notice period gets no reminder until the committee sets a date; the platform proposes none | meets | CG2 |
| P11-J10 Signed only by a named role | Marking an agreement signed for ARFHSN refuses while its signatory row is empty; an agreement signed in AFRP's name for an ARFHSN programme shows the mismatch and is not corrected by software | meets (the refusal); guarded until Q-107 for the mismatch's resolution | CG2 |
| P11-J11 A co-funded grant lists each club's share | Two clubs' pledges against one grant appear on the grant and on each club's statement as a Care co-funding line; an attributed gift is a count and never settles | meets | CG1, C3 |
| P11-J12 The six-monthly report is the ledger's | The report's balances equal the daily close; grants by state, agreements due and overdue, club lines and the compliance calendar appear; the Chairman's approval dates it; nothing in it is typed | meets | CG4 |
| P11-J13 The clock starts from the register | With no election date on file the report is on demand and says so; with a date it is due every six months from it (III §7) | meets | CG4 |
| P11-J14 The Relief Fund posts nothing | A gift to the Relief Fund is held to an entity to be named and receipted without a deductibility claim; a transfer from it refuses and names D55 and F15 | guarded until Q-109 | CG5 |
| P11-J15 Family lists never enter | No field on a recurring relief grant accepts a beneficiary; the delivery confirmation is a count and an amount | meets | CG5 |
| P11-J16 The platform never screens | A partner's screening act records who, when, which list and the result as typed by a named person; no code path consults a list or marks a partner cleared or blocked | meets | CG6 |
| P11-J17 Schedule F assembles from the register | For a tax year and an entity, the extract lists each foreign grant's region, purpose, amount and method with the monitoring description built from delivery and use-of-funds records; a grant with no partner jurisdiction is flagged, not guessed | guarded until Q-111 | CG6 |
| P11-J18 Federation scope reads nothing | A Federation-lens user without an exact grant sees counts of ARFHSN grants and no request, partner or payment (R39) | meets | CG1 |

---

## 13. What changes in the site's data with this note

`workflows.yaml`: `care-grants` and `partner-agreements` move from "Proposed" to "Designed" with this note as the design and `grants` as the module; the open items carry Q-104–Q-114 by their governance numbers; `care-grants` gains the compliance record as a step and the Relief Fund's holding path; `partner-agreements` closes the "how far ahead the reminder goes" item as "the agreement's own notice, no default" and the "foundation grants" item as proposed here. `programmes.yaml`: `medical-mission`, `women-to-women` and `relief-fund` cite this note under platform needs; `relief-fund` gains the deductibility consequence of its entity question; the Mission's agreements entry gains the overdue state. `experiences.yaml`: the committee-member and programme-organiser lenses gain the grant and agreement steps for the Care branch; a federation-staff line for the six-monthly report. `questions.yaml`: Q-104 to C11. The crosswalk: F13, F14, F15, F17 and J1 updated to "Designed" with this note; the P11 row marked written. `plan/MASTER-PLAN.md`: rows CG1–CG6 after FR1–FR6. `AFRP-QuickBooks-Integration-Spec.md` (the owning agent): ARFHSN as its own company with the weekly deposit report it asked for, which this note assumes and does not design.

---

## Sources

Record: `design/AFRP-Decisions-Register.md` D7, D8, D9, D10, D41, D54, D55, D56, D57, D61, D62, D63, D66, D67; `design/bylaws/ARFHSN-Bylaws-2017.pdf` (Articles I–VI, read in full); `design/AFRP-ARFECF-ARFHSN-Rulesets.md` Part 2 and HS-OV-1 to -8; `design/AFRP-Rules-Register.md` R20, R22, R24, R39; `design/AFRP-Fund-Rules.md` (P9); `design/AFRP-Club-Experience-Plan.md` §5, §7; `design/AFRP-Strategic-Plan-Crosswalk.md` F10, F13–F17, J1, P11; `site/data/workflows.yaml` (`care-grants`, `partner-agreements`, `giving-funds`), `programmes.yaml` (`medical-mission`, `women-to-women`, `relief-fund`, `senior-living`, `project-hope`), `questions.yaml` (Q-2, Q-3, Q-21 to Q-26); AFRP Constitution and By-Laws 2024, By-Laws 7.2.3, 11.1.1–11.1.5; the ARFHSN intake of 30 September 2026 and the Federation's money cards (private, in the planning Project), at role level.

Outside the record:
- IRS Announcement 2003-29, on US charities' grants to foreign organisations (the discretion-and-control standard of Rev. Rul. 68-489; Rev. Rul. 63-252 and 66-79 on deductibility; records to keep; Treasury's guidelines): https://www.irs.gov/pub/irs-tege/a2003_29.pdf
- IRS, Instructions for Schedule F (Form 990), Statement of Activities Outside the United States (Parts II and III; the monitoring description): https://www.irs.gov/instructions/i990sf
- IRS, Instructions for Schedule D (Form 990), Part V Endowment Funds: https://www.irs.gov/instructions/i990sd (cited for P9)
- U.S. Department of the Treasury, Anti-Terrorist Financing Guidelines: Voluntary Best Practices for U.S.-Based Charities (2002, revised 2005–2006): the Treasury press release and guidelines at https://home.treasury.gov/news/press-releases/hp122 and the response to comments at https://home.treasury.gov/system/files/136/archive-documents/0929-responsetocomments.pdf (the guidelines' current location on the Treasury site not confirmed during drafting)
- Office of Foreign Assets Control, Counter Terrorism Sanctions programme page (designations, general licences for humanitarian activity, guidance): https://ofac.treasury.gov/sanctions-programs-and-country-information/counter-terrorism-sanctions; the sanctions list search at https://sanctionssearch.ofac.treas.gov/ (not re-fetched during drafting)
- Internal Revenue Code section 4945 (private-foundation expenditure responsibility), named only to say it does not bind a public charity directly; not fetched.
