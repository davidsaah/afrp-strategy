# The Relief Fund and Senior Living

### Two pieces of Care-branch money the Federation handles but does not fully own: the Relief Fund as it runs, set against the record, and the Federation's part in the Ramallah Foundation's senior home

**Design note P23 · 2 October 2026 · for the Hub's `funds`, `ledger`, `grants` (P11's module), the institution registry, `payments`, `comms` and the Care programme pages**

*Since 4 October 2026 (D99):* the shared shapes this note draws — the authority row (authorisers per path) and the statement run (the Relief Fund) — are built once as the platform primitives of `AFRP-Platform-Primitives.md` (P29 §3, §7); this note's rules are carried as their settings.

**What this note rests on.** The second research round of 2 October 2026 (the care report in full and the federation report's sections on money, the clubs and the Convention's close, both private, read under D54) set against the record: the fund rules note (`AFRP-Fund-Rules.md`, P9: the fund object, §2.1's Relief Fund and Senior Living rows, rules 1, 6, 9 and 14); the Care grants note (`AFRP-Care-Grants-and-Partners.md`, P11: §2 the grants register, §3 the partner register, §4 the Relief Fund, §7 what stays outside, §8 the foreign-grant record); D3 (the Foundation as a partner in the institution registry, D3-B), D7–D10, D40, D55, D56, D57, D59, D63 and D66; the Decisions Register's section "Conflicts between practice and the record found in the research round of 2 October 2026" (the Relief Fund row and the Senior Living row); the workflows `relief-disbursement`, `convention-close` and `giving-funds`; the programme register entries `relief-fund` and `senior-living`; crosswalk rows F15, F16 and F18; the questions Q-109, Q-110, Q-111, Q-126, Q-174, Q-180, Q-203 to Q-209, Q-228 and Q-232; and the 2024 Constitution and By-Laws (Article III §3; By-Laws 6.2.2, 6.8.1, 7.2.3, 7.7.1, 8.7.1, 11.1.2, 11.1.4, 11.1.5), each clause read before it is cited. Outside the record: IRS Publications 526 and 1771, cited in the Sources and used only to frame questions for the outside accountants.

**Since 3 October 2026:** **D83** (David's decision for the design record) names AFRP as the Relief Fund's holding entity; the deductibility and receipt text waits on the CPA (D9). The books carry the fund inside ARFECF, a reconciliation item in the Decisions Register's conflicts table (the books follow D83, or the Boards revisit). Who approves each transfer between the Board's votes and whether D63's closing records apply stay Q-109. The sections below follow D83, each change marked with the date.

This note adds no decision. Where it reads as a rule, the rule is a by-law cited by number, a decision cited by number, a rules-register row, or a *design choice* labelled as such. Where the record is silent it says so and raises a question with an owner. Where practice and the record disagree, the note gives both, builds what the record says, and carries the conflict as a question.

**Precedence (D41).** The by-law texts first: Article III §3 (the Foundation "a separate and legal entity"), By-Laws 6.2.2 and 6.8.1 (the Foundation's Board seat), 11.1.4 and 11.1.5 (no solicitation in an individual capacity for a Federation project; club funds for a Federation project pass through headquarters), 7.7.1 and 11.1.2 (who signs cheques for the Educational Fund and for AFRP). Then the Decisions Register and the named design documents (P9, P11, D55, D57, D63). The prototype's `#/program/senior` evidences a story about a capital campaign, never a rule. The Hub's code shows nothing for either subject: the Relief Fund is CG5, gated and not built; JP-032 (pledges against cash) is designed and not built (P9 §1). Practice found by the research round is evidence of how things run, and never a rule.

**Public-repository rule.** No living person, no beneficiary, no organisation in Ramallah by name, no donor, no figure, no account.

---

## 1. What the record already holds

**Built.** Nothing for either subject. What exists beside them: the restricted-funds engine (a money-taking event names a purpose, the purpose belongs to an entity, only that entity authorises raising in its name, spending releases the restriction); the public giving door; the ledger's gross posting, daily close and reversal-as-new-entry (R20, R22, R24). The purpose catalogue (D8), the four contributor moments (D10), the fund register (P9 FR1), the grants register (P11 CG1) and the Relief Fund's holding shape (CG5) are designed and not built.

**Decided.** A programme's holding entity is the fund that budgets it (D55), which leaves the Relief Fund unnamed. A gift is receipted by the entity that receives it (D9). Raising in another entity's name runs on a purpose catalogue with escalation; a new purpose goes to that entity's board and blocks publication (D8). The contributor hears at four moments: receipt, goal reached, funds transferred, purpose fulfilled (D10). Every amount a club pays or receives through a Federation or affiliate programme is on one club statement, and every gift may carry a club attribution (D57). A Care grant is approved by the holding entity's Board with a ceiling, paid on delivery with two signatories, closed on three records (D63). The Ramallah Foundation is a partner in the institution registry, with agreements and contacts and no governance surfaces (D3-B); the Foundation is shown on the Care branch as a fund and is not joinable (D40). The shared drive is the archive of record (D66).

**Designed (P9, P11).** The Relief Fund sits on the fund register with its entity unset and posts nothing; a gift to it is held as a liability to *the entity to be named* and receipted with no deductibility claim; once the entity is named, monthly support becomes a recurring grant on the register with the Board's vote as approval and the representative's distribution report as delivery; family lists never enter (P11 §4, rule 11 and 12; CG5). The Senior Living campaign and the senior-centre memorial fund are a fund row with entity "not stated" and kind "capital campaign, restricted, ring-fenced" (P9 §2.1). The Program Architecture names Senior Living as the one programme needing a capital-campaign module (§3) and gives it the *Campaign* shape (§6). *Since 3 Oct 2026:* D83 names AFRP as the Relief Fund's holding entity; the fund posts to AFRP, and its receipts claim no deductibility until the CPA gives the text (D9).

**Historically, from the first intakes (role level, no figures).** The Board voted monthly support to families in Ramallah in 2020 with a distribution plan and the condition that recipients are told the Federation is the source, extended it in 2021, and brought collections made outside the Federation's procedure into the fund; the host-agreement template sends a per-registrant amount to the fund; the approved budget funds its Ramallah charities page from it; relief gifts appear as income on the Educational Fund page; the Federation's representative in Ramallah distributes on lists supplied by local partners.

**What the research round adds (role level, no figures).** For the Relief Fund: the account is titled in the Federation's name and reported at every Board meeting by the Educational Fund Treasurer on a one-page statement beside the Education Fund and Cook Book statements; its regular income is the per-registration amount posted as one line after each Convention's settlement; money left by wire straight to the Federation's account in Ramallah in 2020, and since 2024 by transfer to the Education Fund account, which wires Ramallah; ARFECF's reviewed statements book relief gifts as ARFECF's donor-restricted contributions and the Ramallah charities as its largest programme expense; ARFECF's balance sheet carries the Relief Fund as its own bank account and AFRP's carries an amount due to it; a treasurer's projection assumes the per-registration amount continues to 2030. Three kinds of payment are decided three ways (§3). The Young Leaders Committee ran a club-against-club needy-families drive in 2025 and again in 2026, and the CRM holds it as its own fund; the Board said in May 2026 that club donations to needy families should go through the Federation, "preferably the Relief Fund"; the Executive Committee in September 2026 weighed how to align clubs that fund Ramallah projects directly with the fixed charities allocation. For Senior Living: the home is the Foundation's (§8).

---

## Part A — The Relief Fund

## 2. The fund as practised, against the record

| Element | Practice (research, 2 Oct 2026) | The record | Where they part | Question |
|---|---|---|---|---|
| Holding entity | Account in the Federation's name; reported by the Educational Fund Treasurer; ARFECF's books carry the gifts, the charities and the account; AFRP owes it | Not stated (D55 silent; P9 §2.1; P11 §4). *Since 3 Oct 2026:* AFRP (D83) | Practice books it in ARFECF; D83 names AFRP: a reconciliation item (the books follow D83, or the Boards revisit) | Q-109 (entity: D83) |
| Income | A per-registration line after each Convention; appeal gifts in an emergency; periods with no income | The per-registration amount is a host-agreement term (P13 §2.2); its continuation after 2025 is open | A projection assumes it to 2030 | Q-126 |
| Gifts through the Federation's pages | The public giving page offers no Relief Fund purpose; relief gifts reach the Education Fund page | The register says gifts come through My AFRP; D8 requires a catalogue purpose | The purpose does not exist | Q-208 |
| Emergency support | Board vote: a sum per month, a term, a distribution plan, the source condition; extensions by the Board and the General Assembly | The only path the record describes (P11 §4) | None | — |
| Annual Ramallah charities | A line on the Educational Fund page of the budget voted at the Convention, funded from the Relief Fund; the representative distributes to about ten women's organisations and youth clubs; one organisation returns its cheque each year | The register names the line; who sets the list is not written | The list and the amount per organisation are nobody's written act | Q-207 |
| Ad hoc transfers | A seasonal distribution and a one-off wire labelled a donation, with no approval on file | Nothing permits a transfer without an approval | No approval trail | Q-109 |
| Paying route | Relief Fund → Education Fund account → wire to the Federation's account in Ramallah | Not described | Two chequebooks must reconcile | — |
| Reporting | A one-page statement to every Board meeting; the representative's report gives counts and totals | Not in the Fund Rules' table of report duties | Not on the record | Q-174 |
| Club drives | A Young Leaders drive with a per-club tally and a winning club; a separate CRM fund; a Treasurer's proposal of a nationwide relief day | By-Law 11.1.4; D57 attribution | Receiving fund and entity unknown | Q-180 |
| Clubs giving directly | Clubs send money to Ramallah projects themselves; the Board asked for one channel | By-Laws 11.1.4 and 11.1.5; D57 | Whether a rule exists | Q-228 |
| Pre-spend rule | The 2026–27 Treasurer proposes a budget-committee meeting and a written plan before money is authorised | Not a rule | A proposal | Q-209 |
| Family data | Lists stay with partners and the representative | Never enter (P11 rule 12) | None | Q-110 |

**What the note builds from this.** The record's rule stands: the fund posts nothing until a Board names its holding entity (P9 rule 1; P11 rule 11). What can be built now is everything that does not post: the fund row with its evidence, the disbursement request with an authoriser per path as register rows, the beneficiary-organisation register, the representative's report as a form of counts, and the report to the Board as an assembly that switches from "linked document" to "from the ledger" on the day the entity is named. Nothing in this note picks the entity. *Since 3 Oct 2026:* D83 (David's decision for the design record) names AFRP, so the posting parts are no longer held on the entity; the receipt's deductibility text waits on the CPA (D9), and ARFECF's booking of the fund is a reconciliation item in the Decisions Register's conflicts table.

**One reading of D63 the Boards should see before they choose.** D63 governs "a grant or partner project paid from a Care fund" and names the holding entity's Board as approver. The Relief Fund is on the Care branch. If the Boards name ARFECF, D63 read as written makes the ARFECF Board the approver of relief payments, while today the AFRP Board votes emergency support and the General Assembly votes the charities line; if they name AFRP, the AFRP Board is the approver and D63's two-signatory rule meets By-Law 11.1.2; if ARFHSN, D63 applies in the form P11 designed. P11 §4 read D63's closing records as applying only to an ARFHSN-held fund; that is a reading, not a decision. Q-109 already asks whether D63 reaches the fund; this note does not answer it, and the authoriser rows in §4 hold no value until it is answered.

---

## 3. The fund row

The Relief Fund is one row on P9's fund register (FR1), with the properties of P9 §2. Every value is data with its source and date.

| Property | Value now | Source |
|---|---|---|
| Holding entity | **AFRP (D83, 3 October 2026).** *Until D83: not stated.* Evidence of practice attached: the account's title (the Federation's name); the reporter (the Educational Fund Treasurer); the CPA's booking (ARFECF donor-restricted contributions; Ramallah charities as ARFECF programme expense); the balance sheets (an ARFECF bank account; AFRP owing it); the budget page (the Federation's budget, the Educational Fund page). The ARFECF booking is D83's reconciliation item | D83; Q-109; D55 |
| Governing text | The Board's votes of 2020 and 2021 and the General Assembly's of 2021 (emergency support); the Convention decision funding the charities from the fund (year not on file); the host-agreement template's per-registrant term | Programme register `committee_decisions`; P13 §2.2 |
| Kind | Donor-restricted to relief, as the record states it | P9 §2.1 |
| Receipting entity | AFRP (D83); receipts carry no deductibility claim until the CPA gives the text (D9) | D83; P11 §4 and rule 11; D9 |
| Authoriser | Per path, as register rows with no value (§4) | Q-109; Q-207 |
| Transfer rules | A transfer to a paying account and the onward wire are one linked act (§4.4); nothing leaves without an approval act | P11 rule 15; *design choice* for the Relief Fund, by analogy with D63, whose reach to this fund is Q-109 |
| Report duties | The per-meeting statement (§6); the representative's counts (§7) | Practice; Q-174 |
| Aliases | The names the treasurer's reports, the budget, the CRM and ARFECF's statements use for the same fund, carried so a report can be read against any of them | P9 §1's naming-clash practice |
| Opening balance | Entered once, on the day the entity is named (D83 named it on 3 October 2026; the entry waits on the reconciliation item), from the Treasurer's attested statement at a stated date, as a dated act; never computed from the CRM | *Design choice* |

**The needy-families fund in the CRM is its own row, not an alias.** The CRM holds the Young Leaders' drive as a separate fund, and AFRP's chart of accounts carries "needy families" beside "relief" as separate amounts due to ARFECF. Whether the two are one purpose is not stated anywhere. The register carries a second row, entity not stated, with a pointer to the Relief Fund row and the question beside it; neither row merges the other. *Design choice; Q-180.*

**What the row refuses.** Any posting while the holding entity is unset, naming Q-109 (P9 rule 1; *since D83 the entity is set*); any receipt with a deductibility statement before the entity is named (P11 rule 11); a transfer out with no approval act (§4); a field for a person who received relief (P11 rule 12).

**Income lines, each with its source.**

1. **The per-registration amount.** One dated line per Convention, posted from the settlement statement (P13 §4; `convention-close`); the amount and the registrants it applies to are terms of that year's signed host agreement (D59). Whether the term continues after 2025 is Q-126; a Convention whose agreement has no such term posts nothing to the fund, and the settlement says the term is absent. Until the entity is named the line is held as a liability to the entity to be named (P11 §4), which is how AFRP's books already carry it ("due to" the affiliate; Q-232). *Since 3 Oct 2026:* D83 names AFRP; the line posts to AFRP's Relief Fund, and how the "due to" line is settled is the reconciliation item D83 names.
2. **Appeal gifts.** Only through a catalogue purpose (D8). No purpose is published today (Q-208); D8 puts publication behind the holding entity's board, so the purpose cannot publish until Q-109 is answered. *The record, read together.* *Since 3 Oct 2026:* D83 names AFRP, so publication is for AFRP's Board under D8 (Q-208).
3. **Club-attributed gifts and drives.** §5.
4. **A transfer in from another fund** (Women to Women gave to the fund in 2020). Only as a dated act by the giving fund's authoriser; the cross-entity case is the Fund Rules' unsettled one (Q-168's pattern). *Design choice.*

---

## 4. The disbursement request, and its authoriser per path

A disbursement from the Relief Fund is a grant on P11's register (CG1) of a kind that path names, drawing on the fund row above. It carries P11 §2's states. What this note adds is the authoriser for each path as a register row, the evidence each act carries, and the refusals.

### 4.1 Path 1 — emergency support

| | |
|---|---|
| Kind | *Recurring* (P11 §2) |
| Approval act | A vote: a sum per month (the ceiling), a term, a distribution plan as a document on the drive (D66), the source condition (recipients told the Federation is the source); an extension is a new vote naming the one it extends |
| Who has voted, in practice | The AFRP Board; once, the General Assembly |
| Authoriser row | **No value.** If the AFRP Board, its vote stands; if the holding entity is ARFECF or ARFHSN, whether the AFRP Board's vote becomes a request to that entity's Board is Q-109. *Since 3 Oct 2026:* the entity is AFRP (D83); the row still holds no value, and who approves each transfer between the Board's votes is Q-109 |
| Payments | One per month within the ceiling and the term; each with two signatories by role on the paying account's row (§4.4) |
| Delivery | The representative's monthly count of families and amount (§7) |
| Close | At the end of the term, with the representative's report for each month on record. D63's agreement and inventory records apply only if the Boards say D63 reaches the fund (Q-109) |

### 4.2 Path 2 — the annual Ramallah charities

| | |
|---|---|
| Kind | *Annual distribution*: one grant per fiscal year with one line per receiving organisation from the register in §5. *Design choice: a new kind on P11's register, because the beneficiaries are a list of institutions, not one partner* |
| Approval acts | Two, and both must be on file: **(a)** the budget line, voted with the budget (the General Assembly by practice; the written approval path is Q-234); **(b)** the list of organisations and the amount for each, as an act by the body that sets it |
| Authoriser row for (b) | **No value.** Who sets the list and the amounts is not written anywhere (Q-207). The platform refuses to mark the distribution approved while the row is empty, and names Q-207 |
| Payments | Per the distribution's lines, or as one transfer to the Ramallah account with the per-organisation split recorded by the representative; which one is practice, and both are recorded as acts |
| Delivery | Per organisation: the amount handed over, the date, and the organisation's acknowledgement where one is given (§7) |
| A returned cheque | A reversal of that line as its own entry (R24), with the organisation's return recorded on its register row. Whether the organisation stays on next year's list is Q-207's to say; the platform never drops an organisation from the list itself |

### 4.3 Path 3 — between votes

A seasonal distribution and a one-off wire left with no approval on file. The record has no path for this: nothing authorises a transfer without an approval act (P11 rule 15; *design choice* for the Relief Fund, by analogy with D63, whose reach to this fund is Q-109). The platform therefore has **no ad hoc path**: a seasonal distribution is either a payment under an existing path-1 vote or path-2 list within its ceiling, or a new approval act by the body the authoriser row names for "between votes", which has no value (Q-109). A transfer recorded without one refuses and names the question. *The record, applied; the gap is Q-109.*

**The Treasurer's pre-spend rule** (a budget-committee meeting and a written plan before money is authorised) is a register row with no value; if the Board adopts it, it becomes a required document on the approval act for every path (Q-209).

### 4.4 The paying route and the signatories

- **One linked act for two chequebooks.** Since 2024 money leaves the Relief Fund by transfer to the Education Fund account and is wired from there to the Federation's account in Ramallah. The platform records the transfer and the wire as one act with two legs, each on its own account, the grant it pays named on both, so the two statements reconcile. A wire without its transfer, or a transfer without its wire within the period the Treasurer sets, shows unmatched on both statements. *Design choice.*
- **Signatories.** Two by role on each account's row, filled from the holding entity's text once it is named: for an ARFECF account, the Educational Fund Treasurer's signature countersigned by a person the ARFECF Board designates (By-Law 7.7.1); for an AFRP account, the Treasurer countersigned by a senior officer of the Executive Committee (By-Law 11.1.2); for an ARFHSN account, two designated by its Board (ARFHSN III §5; Q-104). Until the row is filled, a payment refuses and names the text it waits on (P11 rule 2).
- **The Ramallah account.** Its two local signatures and its registration are outside the platform (P11 §7). Whose account it is (AFRP's, ARFECF's or ARFHSN's) is not stated: Q-104 asks about ARFHSN's Ramallah account, and the relief wire's receiving account may be a different one. *Q-247.*
- **The foreign-grant record.** Relief paid in Ramallah is a grant abroad by whichever entity holds the fund; P11 §8's fields apply, and whether ARFECF's Ramallah charities belong on its Schedule F is already Q-111.

---

## 5. Club relief drives and clubs' direct giving

**The texts.** By-Law 11.1.4: a club or member "shall not solicit any funds in their individual capacity for any project already undertaken by the A.F.R.P. unless authorized to do so by the Board and Executive Committee". By-Law 11.1.5: "All funds raised for an A.F.R.P. sponsored project from each Local Club/Chapter must be sent through the Federation's main headquarters office to then be forwarded to the respective organization/individual." D57: every gift may carry a club attribution.

**What follows from them, and what does not.** Money a club raises *for the Relief Fund* is money for a Federation project and passes through headquarters (11.1.5): on the platform it is gifts to the fund's catalogue purpose, each with the club's attribution (D57), counted on the club's statement and never the club's money (Club Experience Plan §5.4). The Board's May 2026 statement ("preferably the Relief Fund") is consistent with 11.1.5 for that money. A club's gift to *its own* project in Ramallah, which is not a project the Federation has undertaken, is outside 11.1.5's words; whether the Board makes "one channel" a rule for it, or an attribution-and-report rule that leaves it lawful and visible, is Q-228. The platform builds nothing that blocks or records a club's own giving until that is answered.

**A drive across the clubs** (the Young Leaders' drive; the Treasurer's proposed relief day) is, on the platform, one catalogue purpose with a published end date, gifts attributed to clubs, and a tally that is the sum of attributions per club, shown as a count and an amount per club on the drive's page. A prize is the organisers' and is not modelled. Which fund receives the drive (the Relief Fund row or the needy-families row), and whether the drive needs 11.1.4's authorisation, are Q-180; the drive cannot publish until the receiving row has an entity (D8). *Design choice for the shape; Q-180 and Q-109 for the rest.*

---

## 6. The report to the Board

**The statement, per meeting.** The Educational Fund Treasurer files today a one-page statement: opening balance, deposits with dates, expenses with dates, closing balance (Q-174 asks whether this is the report the platform should produce, and in whose name). The platform's version, once the fund posts, is assembled from the ledger at the close (R22) and adds, per line, what the paper lacks:

- each deposit's source (the Convention and its agreement row; the catalogue purpose; the club attribution as a count);
- each expense's path (1, 2, or a refused path-3 attempt as a count), its approval act and date, and the paying route's two legs;
- the commitments outstanding: path-1 months voted and unpaid; the path-2 line voted and undistributed;
- the representative's counts for the period (§7);
- open questions that block the fund, by number.

**Before the entity is named** the platform posts nothing, so it cannot produce the statement from the ledger. The Treasurer's statement stays the record, filed on the drive and linked from the fund's page (D66), and the page says why. *Design choice; it follows from P9 rule 1.* *Since 3 Oct 2026:* D83 names AFRP, so the switch to "from the ledger" follows once the fund posts (RL1, RL3); ARFECF's booking of the account stays a reconciliation item.

**The projection.** A treasurer's projection in the 2026 General Assembly packet runs the fund forward against fixed grants. The platform's fund page may show a projection only from voted commitments and attested terms: the per-registration amount appears as a projected income line only for a Convention whose signed agreement carries the term (D59); for later years it appears as a blank labelled with Q-126, never as an assumed figure. *Design choice, resting on D59 and on R40's rule that a silent text is flagged, not filled.*

**The year-one baseline (D67).** Families supported per month and organisations supported per year, as counts, from the representative's reports. No other outcome measure is invented.

---

## 7. What the Federation's representative in Ramallah records

The representative is a role the record names in P11 (delivery confirmation, inventory) and in the programme register; no by-law constitutes it, and who appoints it, for how long, and what it may see is not written. On the platform it is a seat on a register row naming who seated it, with the date. *Q-246.*

**What the representative records, and nothing else:**

| Path | Recorded per act | Never recorded |
|---|---|---|
| 1, emergency support | The month; the number of families; the amount distributed; the date; the account the money left; the partner organisations whose lists were used, from §5's register | A family, a person, an address, a telephone, an identity number, a list, a photograph of a recipient |
| 2, annual charities | Per organisation on the register: the amount handed over, the date, the organisation's acknowledgement (a document on the drive where one exists), a return | Any individual connected to the organisation beyond its role-level contact on the register |
| Seasonal, under an existing approval | As path 1 | As path 1 |

The platform has no field that accepts a beneficiary person (P11 rule 12). A free-text note on the representative's report is limited to the counts' explanation and carries a warning that names and identifying details are refused; a note that the office finds to carry one is replaced by a corrected entry naming the old (R27's retraction shape), never edited. *Design choice.*

**The beneficiary-organisation register.** The organisations the charities line and the partner lists come from are institutions on the institution registry (P11 §3's partner register, as a kind): name, kind (women's organisation, youth club, partner supplying lists, other), registration in its jurisdiction where known, role-level contact, the date and act that first put it on the list, each year's line and any return, and the sanctions-check act of P11 §8 by a named person where counsel requires one (Q-112). A partner that supplies family lists is on the register as an organisation; its lists are not. *Design choice, extending P11 §3 to the charities.*

---

## Part B — Senior Living

## 8. Senior Living as practised, against the record

The record calls Senior Living a Federation programme on the Care branch with a capital campaign, pledges against cash and a ring-fenced fund (Program Architecture §3, §6; JP-032; P9 §2.1). The sources show something else:

- **It is the Ramallah Foundation's project.** The Foundation, a separate New York corporation that files as a private foundation, owns, built and will operate a new senior citizens' home in Ramallah that replaces a 1970s home run by a Ramallah women's union. Construction was reported complete in 2026; furnishing, the residents' move, the hiring of an executive director and a ribbon-cutting were announced for the autumn. The by-laws already treat the Foundation as separate: Article III §3 recognises it as "a separate and legal entity with the mission of supporting its own approved mission and constitution", and By-Laws 6.2.2 and 6.8.1 give it one appointed seat on the Board.
- **The Federation's part has been four things.** Communications (an afrp.org page, newsletters, a page in each annual report, a 2026 flyer to club presidents); gifts collected through the Federation's channels and passed to the Foundation, booked by ARFECF's accountants as restricted gifts received and released, and held on AFRP's books as an amount due to the Foundation; a Convention-voted line in ARFECF's budget paid to the Foundation from the Education Fund; and, in 2026, an ask to clubs for memorial gifts and club legacy gifts, with the Foundation offering signage at the home.
- **What was never operated.** No pledge was held in any Federation system; no capital-campaign module, naming-opportunity catalogue or ring-fenced campaign fund existed on the Federation's side; the campaign was the Foundation's. The record's use case for an elder who may live in the residence belongs to the Foundation and the women's union.
- **Money also runs the other way.** The Foundation gives each year to Federation funds.
- **Three public texts disagree on how to give.** The afrp.org page asks for a cheque to the Foundation; the 2024 annual report invited gifts through My AFRP; the portal lists no such cause today; the President's September 2026 message says the Foundation no longer solicits through the Federation's channels.

The conflict is recorded in the Decisions Register's research-round section (the Senior Living row: Q-203, Q-204). This note builds only what is the Federation's in every outcome of Q-203, and marks the rest unoperated.

---

## 9. The Federation's part, and what the platform builds

### 9.1 The Foundation on the registry

The Foundation is a partner in the institution registry, with agreements and contacts and no governance surfaces (D3-B), and is shown on the Care branch as a fund that is not joinable (D40). Its Board seat is a seat on the leadership directory with By-Law 6.8.1 as the appointing text (P19 DIR2). Whether `senior-living` stays a programme on the register or becomes a partner project under the Foundation's registry row is Q-203; nothing in §9 depends on the answer, because every object below hangs off the Foundation's registry row and is shown on whichever page Q-203 names. Whether a written agreement with the Foundation exists or is wanted (the 2023 "sister organisation" memorandum) is Q-206; until one is signed, the pass-through and the budget grant below are recorded as acts, each with its own authority, and the agreement row shows "none on file".

### 9.2 Pass-through giving, with the receipting entity stated

A gift for the Foundation's home made through the Federation is a **catalogue purpose (D8) whose beneficiary is an outside body**. Its page states, before payment: the receiving entity that issues the receipt; that the gift is passed on to the Foundation; when transfers are made; and the deductibility statement that receiving entity may give. *Design choice for the content; D7 and D9 for the principle that what the donor is told before paying is what binds.*

- **Which entity receipts is not decided.** Practice: ARFECF books the gifts as its restricted gifts and releases them on transfer; the public page today routes cheques to the Foundation directly. One path or two, and whose receipt, is Q-204. The purpose's receipting-entity field holds no value, and D8 blocks publication of a purpose until its entity's board approves it, so **the purpose does not publish until Q-204 is answered**. A gift for the home received by cheque at the office before then is held as a liability to the entity to be named, as P11 §4 does for the Relief Fund. *The record, applied.*
- **A tax point for the accountants, not for the platform.** A gift earmarked for a private foundation may carry a different deduction limit for the donor from a gift to a public charity (IRS Publication 526 distinguishes contributions to "50% limit organizations" from those subject to the 30% limit). Whether a gift passed through ARFECF for the Foundation is treated for the donor as a gift to ARFECF or to the Foundation, and what the receipt may therefore say, is for the outside accountants; not confirmed here. *Q-204; it belongs with Q-204.*
- **The transfer.** Gifts held for the Foundation are passed on by a dated transfer act on a schedule the receiving entity's treasurer sets, recorded against the "due to the Foundation" liability (Q-232 asks the cadence for every affiliate purpose; the Foundation is one of AFRP's "due to" lines). The transfer fires D10's third moment ("funds transferred") to every contributor whose gift it carries. The purpose's page shows transfers by date and amount in aggregate. *Design choice; D10.*
- **No pledge.** The purpose takes gifts, not pledges. A promise of a future gift is the Foundation's to record. *Design choice; §9.6.*

### 9.3 The memorial or legacy gift, and its recognition

- **The honoree.** A gift to the purpose may carry "in memory of" or "in honour of" with the honoree's name as the donor writes it, and an optional notification to a person the donor names (name and address or email, used once for that notice). The portal's giving page already carries an "In the memory of" field. A deceased honoree's name is the donor's statement, not a tree record, and never touches the family tree (D36's boundary on the tree's channels). *Design choice.*
- **Recognition is the Foundation's act.** Signage at the home, a plaque or a listing is offered and given by the Foundation. The platform records, on the gift, the recognition the donor asked for and the wording, and passes it to the Foundation with the transfer; it does not promise recognition on the Foundation's behalf, and the page says so. *Design choice.*
- **Whether recognition is a benefit to disclose.** IRS Publication 1771 requires a written disclosure when a payment over a threshold is partly a contribution and partly for goods or services, and treats goods or services of insubstantial value as excluded. Whether signage or a named listing at the Foundation's home is a benefit the receipt must disclose is for the outside accountants. *Q-248.*
- **The CRM's senior-centre memorial fund.** Its past gifts are history for the purpose's page when the giving records are migrated; whether and how they are imported is the giving migration's question, not this note's.

### 9.4 A club's gift to the home

Clubs were asked in 2026 to promote memorial gifts and to consider a club legacy gift recognised by signage. A club gift **made through the Federation's purpose** is a gift with the club as donor, shown on the club's statement as a line (D57: an amount a club pays through a Federation programme), with the recognition request carried as in §9.3. A club gift **made directly to the Foundation** is the club's and the Foundation's business and is outside the platform. Whether the first is a D57 line, a club event or outside the platform because the recipient is an outside foundation is Q-205; the line type is modelled and gated on it. *Design choice for the shape; Q-205 for whether it runs.* *Since 4 Oct 2026:* **D92** answers Q-205: the gift through the Federation's purpose is a D57 line; a direct gift is outside the platform.

### 9.5 The Convention-voted budget grant

A line on the Educational Fund page of the budget, voted with the budget (the General Assembly by practice; Q-234), paid to the Foundation from the Education Fund account. On the platform it is a **budget-line payment** from an ARFECF account to an outside body: the approval act is the budget line with its date; the payment carries the two signatories of By-Law 7.7.1; the payee is the Foundation's registry row; the agreement row shows "none on file" until Q-206 is answered. It is a grant to a domestic private foundation, so P11 §8's foreign-grant record does not apply to it; the Foundation's own spending abroad is its own compliance. It is not a Care grant on P11's register, because it is paid from the Educational Fund and not from a Care fund. *Design choice, resting on D55 (the fund that budgets it) and By-Law 7.7.1.*

The Foundation's yearly gifts to Federation funds are ordinary gifts from an institutional donor on the Foundation's registry row, receipted by the receiving entity (D9).

### 9.6 Communications

The Foundation's milestones appear on the Federation's page as posts attributed to the Foundation, entered by the office from the Foundation's reports, and the flyer to club presidents goes through the comms desk under the consent filter. The platform holds none of the Foundation's books and shows no campaign total it has not itself received. *Design choice; D3-B.*

### 9.7 What is marked unoperated

The record's capital-campaign machinery for Senior Living (Program Architecture §3's module; §6's *Campaign* shape for this programme; JP-032 as applied to Senior Living; P9 §2.1's "capital campaign, restricted, ring-fenced" kind; the programme register's capital-campaign platform need and its "campaign treasurer" and "elder" use cases) describes nothing the Federation operated. This note proposes that each is marked **unoperated** in the record: not deleted, not built, with this section and Q-203 as the reason. JP-032's shape (a pledge is not money until paid) still serves the Endowment campaign (P9 §7, FR5) and is unaffected. The Foundation's residents and the home's operations are never on the platform (Q-203).

---

## 10. Rules

1. The Relief Fund posts nothing and receipts claim no deductibility until a Board names its holding entity (P9 rule 1; P11 rule 11; Q-109). *Since 3 Oct 2026:* D83 names AFRP for the design record; the fund posts to AFRP, and receipts claim no deductibility until the CPA gives the text (D9).
2. Nothing leaves the Relief Fund without an approval act by the authoriser the path's register row names; there is no ad hoc path, and an empty row refuses and names its question (P11 rule 15; *design choice* for the Relief Fund, by analogy with D63, whose reach to this fund is Q-109; Q-207).
3. Emergency support is approved by a vote with a monthly ceiling, a term, a distribution plan and the source condition; an extension is a new vote (the Board's votes of 2020–21 as practice; the approver is Q-109).
4. The annual charities need two acts on file: the budget line and the list with its amounts; the list's approver is Q-207 (*design choice* for requiring both).
5. A transfer to a paying account and the onward wire are one act with two legs (*design choice*).
6. Payments carry the two signatories the holding entity's text requires: By-Law 7.7.1 for ARFECF, 11.1.2 for AFRP, ARFHSN III §5 for ARFHSN.
7. The per-registration amount posts only where that year's signed host agreement carries it (D59; Q-126), and no projection assumes it beyond a signed agreement (*design choice*; R40).
8. Club money raised for the Relief Fund passes through headquarters as gifts with club attribution (By-Law 11.1.5; D57); a club's giving to its own projects is untouched until Q-228 is answered.
9. No beneficiary person is ever recorded; the representative records counts, amounts, dates and organisations (P11 rule 12; *design choice* for the report form).
10. Organisations, never people, are on the beneficiary register; a returned payment is a reversal (R24) and the list changes only by the list's approval act (Q-207).
11. The Ramallah Foundation is a partner on the registry with agreements and contacts only (D3-B; D40; Article III §3).
12. A pass-through purpose states its receiving entity and its transfer before payment, and does not publish until its entity is set (D7, D8, D9; Q-204).
13. Recognition at the Foundation's home is the Foundation's act; the platform records the request and promises nothing (*design choice*; Q-248).
14. The budget grant to the Foundation is a budget-line payment from the fund that budgets it, signed under By-Law 7.7.1 (D55; *design choice* for the object).
15. No pledge, campaign total, resident or operation of the Foundation's is held on the platform (*design choice*; Q-203).
16. Every act is dated, by a named role, and corrected only by a new act naming the old (R24; R27).
17. No figure in this note; every amount lives on the register or the ledger (D54).

---

## 11. What this note raises

| Q | Question | Owner |
|---|---|---|
| Q-246 | The Federation's representative in Ramallah: no by-law constitutes the role. Who appoints it, for what term, with what duties (distributing relief, confirming delivery for Care grants, inventories), how often it reports, and what it may see on the platform? | AFRP Board · Executive Committee |
| Q-247 | Whose is the account in Ramallah that receives the relief wire (AFRP's, ARFECF's, or ARFHSN's account that Q-104 asks about), and who are its two local signatories by role? | AFRP Board · ARFECF Board · General Treasurer · Educational Fund Treasurer |
| Q-248 | Is recognition at the Foundation's home (signage for a club or a named person; a listing) a benefit a receipt must disclose under the quid-pro-quo rules, and who records the agreed wording? | The outside accountants · Ramallah Foundation |
| Q-204 (merged) | For a gift earmarked for the Foundation (a private foundation) and passed through ARFECF: is it, for the donor, a gift to ARFECF or to the Foundation, and which deduction limit and receipt wording follow? Merged into Q-204's detail (2 Oct 2026). | The outside accountants · ARFECF Board |

Carried, not new: Q-109 (the holding entity; who authorises between votes; whether D63 reaches the fund), Q-110 (where the Federation's relief ends and ARFHSN's begins), Q-111 (the foreign-grant record for the Ramallah charities), Q-112 (screening an organisation), Q-126 (the per-registration amount after 2025), Q-174 (the per-meeting statement), Q-180 (club drives and the needy-families fund), Q-207 (the charities list), Q-208 (the giving-page purpose), Q-209 (the pre-spend rule), Q-228 (clubs giving directly), Q-232 (settling the "due to" accounts), Q-234 (the budget's approval path); for Senior Living, Q-203 (programme or partner project), Q-204 (receipting), Q-205 (a club's gift with signage), Q-206 (the Foundation agreement).

---

## 12. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| RL1 The Relief Fund row and its paths | The fund row on FR1 with its evidence, aliases and the opening-balance act; the needy-families row beside it with its pointer; the three paths as kinds on CG1 (*recurring*, *annual distribution*) with the authoriser register rows per path holding no value; the refusals of §3 and §4.3; the linked transfer-and-wire act; signatory rows per account read from the entity's text | §3, §4 | FR1, CG1; the CPA for the receipt's deductibility text (D9). *(Q-109's posting gate cleared by D83, 3 Oct 2026; the authoriser rows still hold no value under Q-109's remainder.)* |
| RL2 The beneficiary-organisation register and the representative's report | Organisations as a kind on the institution registry (CG2's partner register) with the list's yearly lines and returns; the representative's seat as a register row naming who seated it; the report form of counts, amounts, dates and organisations, with no person field and the refused-note warning | §5 (club side excluded), §7 | CG2; the seat may stay unappointed (Q-246) |
| RL3 The report to the Board | The per-meeting statement assembled from the ledger with sources, paths, approvals, commitments, counts and blocking questions; the linked Treasurer's statement and the "why" text while the fund does not post; the projection from signed terms only, Q-126 as a labelled blank; the D67 counts | §6 | RL1; ledger assembly waits on Q-174 *(Q-109 cleared by D83)* |
| RL4 Club relief drives | A drive as a catalogue purpose with an end date, club attribution and the per-club tally of counts and amounts | §5 | **Gated** on Q-180 (receiving row); publication by AFRP's Board under D8 *(Q-109's entity named by D83, 3 Oct 2026)* |
| RL5 Senior Living: the Federation's part | The Foundation's registry row with the 6.8.1 seat link; the pass-through purpose with receiving entity, transfer schedule and deductibility text as fields, unpublished until set; honoree and notification fields; the recognition request passed with the transfer; the transfer act against the "due to" liability firing D10's third moment; the budget-line payment to the Foundation under 7.7.1; milestone posts attributed to the Foundation; the unoperated marks of §9.7 | §9 | Q-204 for publishing the purpose; the Foundation's page shows it (D91, 4 Oct 2026, answering Q-203); the objects build now |
| RL6 A club's gift to the home | The club-donor line on the club statement with the recognition request | §9.4 | C3 (the club statement); Q-205 answered by D92 (4 Oct 2026) |

Order: RL1 after FR1 and CG1; RL2 with CG2; RL3 after RL1; RL5 can run beside RL1, since it needs only the registry and the catalogue; RL4 and RL6 as their gates lift. Three sessions on the master plan's standing loop for RL1–RL3 and RL5.

---

## 13. Journeys proposed

Identifiers are provisional; the Hub's workbench assigns catalogue ids.

| Journey | Tests | Must reach | Slice |
|---|---|---|---|
| P23-J01 The fund posts to AFRP | A per-registration line from a settlement and a gift post to the Relief Fund held by AFRP (D83); the gift's receipt carries no deductibility claim until the CPA gives the text (D9); a transfer out still needs its path's approval act (P23-J02; Q-109) | guarded until the CPA's receipt text (D9) *(rewritten 3 Oct 2026 under D83; it read "The fund posts nothing": each line refused and named Q-109, the gift held to the entity to be named, guarded until Q-109)* | RL1 |
| P23-J02 No ad hoc path | A seasonal distribution entered with no approval act refuses and names Q-109; entered under a path-1 vote within its ceiling and term, it is accepted as that vote's payment | meets (the refusal) | RL1 |
| P23-J03 Two acts for the charities | A charities distribution with the budget line and no list act refuses to be approved and names Q-207; the platform never fills the list | meets (the refusal); guarded until Q-207 for approval | RL1, RL2 |
| P23-J04 One act, two chequebooks | A transfer to the Education Fund account and its wire record as one act; a wire with no transfer shows unmatched on both statements | meets | RL1 |
| P23-J05 Signatories from the text | With the entity set to ARFECF the payment asks for the Educational Fund Treasurer and the ARFECF-designated countersigner (7.7.1); with AFRP, the Treasurer and a senior officer (11.1.2); with the row empty it refuses | guarded until Q-109 *(since D83: the AFRP case, 11.1.2)* | RL1 |
| P23-J06 Organisations, never people | The representative's report accepts counts, amounts, dates and organisations from the register; no field accepts a person; a note carrying a name is replaced by a corrected entry, never edited | meets | RL2 |
| P23-J07 A returned cheque | A returned charities payment is a reversal on its own line; the organisation stays on the register; next year's list changes only by the list's act | meets | RL2 |
| P23-J08 The statement explains itself | Before the entity is named, the fund's page links the Treasurer's statement and says why it is not from the ledger; after, the statement equals the ledger at the close and lists blocking questions by number | meets | RL3 |
| P23-J09 No assumed income | The projection shows the per-registration amount only for a Convention with a signed term; later years show a blank labelled Q-126 | meets | RL3 |
| P23-J10 A drive's tally is attribution | Gifts to a drive attributed to two clubs show per-club counts and amounts on the drive's page and on each club's statement as attribution, never as club money | guarded until Q-180 | RL4 |
| P23-J11 The pass-through tells the donor first | The senior-home purpose cannot publish while its receiving entity is unset; once set, the page states the receiving entity, the pass-through and the transfer schedule before payment | guarded until Q-204 | RL5 |
| P23-J12 Funds transferred | A transfer to the Foundation clears the "due to" liability and every contributor in it hears the third D10 moment | guarded until Q-204 | RL5 |
| P23-J13 Recognition is the Foundation's | A memorial gift with an honoree and a signage request is passed with the transfer; the page and the receipt promise no recognition | meets | RL5 |
| P23-J14 The budget grant | A Convention-voted line pays the Foundation from an ARFECF account with 7.7.1's signatories; the agreement row shows none on file; no foreign-grant record is asked | meets | RL5 |
| P23-J15 No campaign machinery | No pledge, campaign total, naming opportunity or resident record exists for Senior Living; the capital-campaign journey is marked unoperated with Q-203 | meets | RL5 |

---

## 14. What changes in the site's data with this note

`programmes.yaml`: `relief-fund` cites this note under `platform_needs` (the fund row, the three paths with authoriser rows, the organisation register, the representative's report, the statement) and its `organiser` gains the representative's seat as unconstituted (Q-246); `senior-living` cites this note, its `platform_needs` replace "a capital campaign module" with "marked unoperated (P23 §9.7)" and add the pass-through purpose, the memorial gift and the budget-line payment, and its "Campaign treasurer" and "Elder" use cases are marked unoperated. `workflows.yaml`: `relief-disbursement` moves from "Proposed" to "Designed" with this note as the design and its path-3 step reworded to "refused without an approval act (Q-109)"; `giving-funds` gains the pass-through step's receiving-entity and transfer fields and the honoree; `convention-close`'s Relief Fund step cites P23 §3. `experiences.yaml`: the member lens's memorial-gift need and the Educational Fund Treasurer's and Executive Administrator's federation lines cite P23; JP-032 under Senior Living is marked unoperated; a programme-lens line for the representative's report. `questions.yaml`: Q-246 to Q-248 numbered by governance; the fourth question (a gift earmarked for the Foundation) merged into Q-204's detail. The crosswalk: F15 and F18 updated to cite P23, with F18 moving from "Outside · Proposed" to "Designed" for the Federation's part; a P23 row in the design-notes table. `plan/MASTER-PLAN.md`: rows RL1–RL6 after CG6. `AFRP-Fund-Rules.md` §2.1 (the owning agent): the Senior Living row's kind changed to "pass-through purpose for an outside body; capital campaign unoperated", and a needy-families row added.

---

## Sources

**Record.** `design/AFRP-Decisions-Register.md` D3 (D3-B), D7, D8, D9, D10, D36, D40, D41, D54, D55, D57, D59, D63, D66, D67, and the section "Conflicts between practice and the record found in the research round of 2 October 2026" (the Relief Fund and Senior Living rows); `design/AFRP-Fund-Rules.md` (P9) §1, §2, §2.1, §7, rules 1, 6, 9, 14; `design/AFRP-Care-Grants-and-Partners.md` (P11) §2, §3, §4, §7, §8, rules 2, 11, 12, 15; `design/AFRP-Host-Agreements.md` (P13) §2.2, §4; `design/AFRP-Club-Experience-Plan.md` §5; `design/AFRP-Directory-Formats.md` (P19) §4; `design/AFRP-Program-Architecture.md` §3, §6; `design/AFRP-Rules-Register.md` R22, R24, R27, R40; `design/AFRP-Strategic-Plan-Crosswalk.md` F15, F16, F18; `site/data/programmes.yaml` (`relief-fund`, `senior-living`), `workflows.yaml` (`relief-disbursement`, `convention-close`, `giving-funds`), `experiences.yaml`, `questions.yaml` (Q-104, Q-109 to Q-112, Q-126, Q-168, Q-174, Q-180, Q-203 to Q-209, Q-228, Q-232, Q-234); AFRP Constitution and By-Laws 2024, Article III §3, By-Laws 6.2.2, 6.8.1, 7.2.3, 7.7.1, 8.7.1, 11.1.2, 11.1.4, 11.1.5.

**Private research.** Research round, 2 October 2026 (care §1–§3, §6, §7), private. Research round, 2 October 2026 (federation §2–§4, §7), private. The first intakes of 30 September – 1 October 2026 (the Federation's money and governance cards; the ARFHSN cards), private, at role level.

**Outside.** IRS Publication 526, *Charitable Contributions* (deduction limits; contributions "for the use of" an organisation; earmarking): https://www.irs.gov/publications/p526 · IRS Publication 1771, *Charitable Contributions — Substantiation and Disclosure Requirements* (written acknowledgment; quid-pro-quo disclosure; insubstantial benefits): https://www.irs.gov/pub/irs-pdf/p1771.pdf · Comparables as read in the research round (published practice, not re-fetched here): Armenian Relief Society, emergency appeal for Lebanon, https://ars1910.org/emergency-appeal-for-lebanon/ (central collection, local distribution, published bands, no beneficiary lists); PCA Mission to North America, relief disbursement guidelines, https://2019.pcamna.org/?p=15251 (a disbursement committee vote and a named releasing officer). Whether a pass-through gift for a private foundation carries that foundation's deduction limit, and whether signage is a disclosable benefit, are **not confirmed** and are put to the accountants (Q-248, Q-204).
