# The Magazine and the Bookstore in operation

### How Hathihe Ramallah is actually made, paid for and mailed, who makes it, and what the two existing stores and the Cook Book are, set against the designed magazine and the Hub's bookstore

**Design note P24 · 2 October 2026 · for the Hub's `magazine`, `store`, `funds`, `ledger`, `comms`, `memberdir` (the leadership directory) and the institution registry**

*Since 4 October 2026 (D99):* the shared shapes this note draws — the correspondent's seat, consent, the statement run (the subscriber ledger) and assisted submissions and the death hold as work items — are built once as the platform primitives of `AFRP-Platform-Primitives.md` (P29 §4, §5, §7, §10); this note's rules are carried as their settings.

**What this note rests on, and what it does not repeat.** `AFRP-Magazine-Bookstore-Use-Cases.md` (August 2026; "the use-case note" below) designs the issue as a dated sequence of steps with a copy freeze, eight magazine use cases (UC-1 to UC-8), three bookstore use cases (UC-9 to UC-11) and a sales-tax design (§5). Slices 7 and 7b built the magazine half of it (`AFRP-Delivery-Status.md`): the issue on its dated sequence, five auto sections generated at the freeze with no manual entry path, proof and confirm, a death held for the named family contact, the statutory-notice clock, the magazine's own authority that no Federation grant confers, the archive searched through the directory gate, the ads desk refusing payment, the print consents, and open register rows for cadence, back issues, five-or-six sections, 6.5.2's period and the delivery allowance. This note does not restate any of that. It adds what the second research round of 2 October 2026 found about how the Magazine and the stores actually run (the heritage report in full, private, read under D54), sets it against the record, and designs what is missing: the issue cycle as practised, announcements as they arrive, the people, the subscriber ledger and its reconciliation, the appeal, the Magazine's money under By-Law 6.7.1, the archive, the two existing stores against the Hub's, and the Cook Book.

Also read: D9, D22, D28, D33, D41, D54, D55, D57, D60, D61, D66; the Decisions Register's section "Conflicts between practice and the record found in the research round of 2 October 2026" (the Magazine and Bookstore rows); the Rules Register's R24, R27, R34; the fund rules note (P9 §2, §2.1) and the Care grants note (P11 §3); the Club Experience Plan §3.4 (the club's seat in a programme); the directory note (P19 §4); the workflows `magazine` and `magazine-announcements`; the programme register entries `magazine` and `bookstore`; crosswalk rows D18, D21, E7 and J10; the questions Q-66, Q-70, Q-76, Q-95, Q-173, Q-174, Q-192 to Q-199; and the 2024 Constitution and By-Laws (Article III §2; By-Laws 6.2.2, 6.5.2, 6.7.1, 9.5.2, 10.1.4, 10.2.1 H), each clause read before it is cited. Outside the record: IRS Publication 1771, the USPTO's and the Copyright Office's public guidance, cited in the Sources.

This note adds no decision. Where it reads as a rule, the rule is a by-law cited by number, a decision cited by number, a rules-register row, or a *design choice* labelled as such. Where practice and the record disagree, the note gives both, builds what the record says, and carries the conflict as a question.

**Precedence (D41).** The by-law texts first: Constitution Article III §2 (the Magazine "shall operate independently with its own editorial staff and subscription management as provided for within the By-Laws"); By-Law 6.7.1 (the Federation "shall appropriate the necessary funds to guarantee its publication"; subscription fee collection and policy determined by "the Magazine's independently selected Board in consultation with the Federation's Board of Directors"; a one-year Board seat appointed at the General Assembly); 6.2.2 (one voting member of the Magazine on the Board); 6.5.2, 9.5.2, 10.1.4, 10.2.1 H (the Magazine's statutory duties). Then the register and the named design documents, the use-case note among them. The prototype's `#/program/magazine`, `#/member/magazine`, `#/program/bookstore` and `#/member/bookstore` evidence stories. The Hub's `magazine` and `store` modules show what is built and never what should be. The two live stores and the Magazine's working practice are evidence of how things run, never rules.

**Public-repository rule.** No living person, no subscriber, no correspondent by name, no title that is a person's name, no third-party retailer by name, no price, no figure.

---

## 1. What the record already holds

**Built.** The magazine half of the use-case note, as slices 7 and 7b record it (above). The bookstore: `plan/MASTER-PLAN.md` §1a lists "the bookstore" and a store desk among what the Hub has built, and the programme register says catalogue, member pricing, orders and inventory are built with JF-066 a guarded refusal; `AFRP-Delivery-Status.md` carries no slice entry that says what the store module does line by line, so a build session inventories it from its own code before changing it (D41: the code shows what is). Live payments wait on slice 5.

**Decided.** The Magazine's assets have been held by ARFECF since November 2022 (D55); receipts and books follow the holding entity (D55, D9). Nothing about a living person shows without sign-in (D28). A birth is announced on D22's pattern, household consents, withdrawable (D33); a death is a life event with a family-approval gate (R34). Per-field visibility and print are consents, and a retraction is a new entry (R27). The shared drive is the archive of record (D66). A non-member is held as a contact record, not a membership (D60; Q-70).

**Designed and not built.** Graduations as a life-event type (UC-2); the bookstore's catalogue of back issues, clan books, merchandise and downloads at a member price (UC-9); fulfilment (UC-10); sales as exchange revenue with sales tax as a liability (UC-11); the Michigan-first registration and nexus monitor (§5.3).

**What the research round adds (role level, no figures).**

- **The issue.** Six issues a year in English and Arabic; the September/October issue is the Convention issue; each is laid out by a design agency, printed by a printer, mailed by a mailing house, and sent digitally as an email campaign to a contact list wider than the membership; in 2026 the campaigns for the May/June and July/August issues went out in mid-June and mid-August, and stipends and printer payments fall on the first of June, August and October.
- **Announcements.** Weddings, births, graduations and obituaries reach the editor directly or through a city correspondent named on the inside cover, under guidelines printed in the magazine (2020); obituaries are family-submitted **paid placements** with a head shot, dates, city, survivors and a tribute; graduations are a standing type (school, next school, honours, degree, family, a colour photograph) for spring graduates; story ideas go to the magazine's mailbox and club news through the correspondent.
- **The people.** An executive editor, an Arabic editor, a general manager, a subscriptions and circulation manager, an advertising role and a treasurer, the editors, designer and subscription manager paid a stipend per issue. No board roster, minutes or appointment record for the 6.7.1 board, and none for the 6.2.2 seat.
- **Subscribers.** Since the May/June 2025 issue print goes only to paid print subscribers and a digital copy comes with a renewed membership; cheques and renewals are also kept in the subscription manager's own ledger beside the CRM; in 2026 the two were found to differ; the price rises in 2027; auto-renew needs a saved card.
- **The appeal.** August 2026, not November: a report of print subscriptions not renewed; lapsed subscribers removed from the next issue's mailing list; email to younger contacts and a letter on letterhead through the mailing house to older households, with returns wanted before the Convention issue; then a list of payments received since the appeal, including online payments the manager had not seen.
- **Money.** Income is subscriptions and obituaries ("Subs & Obits", deposited monthly); expenses per issue; a new account opened in September 2023 with a seed deposit after the restructure; a managed investment account; General Fund magazine lines in both directions from 2018 to 2024.
- **The archive.** A history CD/DVD of back issues produced and sold around 2013–14; the magazines of 1959–2018 are in the Preservation grant's scanning scope; no public back-issue archive online.
- **The stores.** Two: a WooCommerce shop on afrp.org (seven titles) and a "Digital Store" on the CRM's Power Apps portal (six of the same titles at the same prices), both US-only, no member price, no stock shown, no digital goods; the afrp.org product page for the cook book carries the site's "tax-deductible" donation text. No owner, committee, order log, stock record or fulfilment routine in any folder; the bookstore's overview sheet is an empty template.
- **The Cook Book.** A separate chequebook reported by the Educational Fund Treasurer at every Board meeting since at least 2017; income book sales and interest; reprints paid from it; a 2025–26 transfer to the Education Fund for the Federation's accounting and CRM systems; the book was compiled by a Detroit women's union in 1976 and reprinted by the Federation; a museum store resells it; a trademark application in its name is pending, handled by the Legal Advisor with outside counsel.

The conflicts are recorded in the Decisions Register's research-round section: By-Law 6.7.1's funding duty against "magazine money kept apart" (Q-194); the 6.7.1 board not evidenced (Q-192); the use-case note against practice on cadence, deaths, graduations, product lines and revenue (Q-193, Q-196, Q-197, Q-199); the bookstore entry's "none found" against two stores (Q-197, Q-173).

---

## 2. The issue cycle as run, on the built issue module

The built issue module (UC-1, UC-8; slice 7) is right for a bimonthly; what it lacks is the issue's outside hand-offs and the cadence as data.

**Cadence.** Six issues a year is practice; slice 7 left cadence as an open register row. The row is the Magazine's to attest under its own authority (Article III §2: "its own editorial staff"; slice 7's grant that no Federation role confers), with the source and date. The platform does not set it. *The record, applied.*

**The Convention issue and the statutory notice.** By-Law 10.1.4 makes a notice of the Convention's date printed in the Magazine sufficient notice if given at least sixty days before. Slice 7 computes the last qualifying issue from the register's period and refuses to close it without the notice. With six issues a year and a July Convention, the September/October "Convention issue" reports on the Convention and is never the qualifying issue; the qualifying issue is one whose **mail date** is at least sixty days before the Convention. *The by-law, applied to practice; nothing new is built.*

**The hand-offs each issue makes, as dated acts on the issue** (*design choice*: the issue records that each hand-off happened and to whom; the platform does not run the vendors):

| Hand-off | To | What leaves the platform | Record kept |
|---|---|---|---|
| Layout | The design agency | The frozen sections and the editorial copy | The date and the issue's content hash; corrections after freeze roll to the next issue (UC-4) |
| Print | The printer | Nothing from the platform (the agency sends the print file) | The date the print file was approved |
| Mail | The mailing house | The print mailing list for the issue (§5.3) | The date, the count, the vendor's registry row, the agreement it is held under (Q-66) |
| Digital | The email campaign | The issue link to the issue's audience under the consent filter (§5.4) | The date and the count sent |
| Payments | The Magazine's account | Stipends and the printer, per issue | Ledger lines tagged to the issue (§6) |

**What the vendors hold.** The design agency holds copy and photographs; the mailing house holds names and addresses for each run. Both are vendors on the store register the incident-response note keeps (P15; IR5) with the agreement each works under. Whether a mailing house may hold members' addresses, and under what agreement, is already Q-66; the issue's mail hand-off refuses while that agreement row is empty and names Q-66. *The record (Q-66), applied.*

---

## 3. Announcements as they arrive

The use-case note's loop ("every printed section generated from the live system, never assembled by hand") is built and holds. What practice adds is **who enters** and **what an obituary is**.

### 3.1 Four types, from practice

Weddings, births, graduations and obituaries. This answers the use-case note's §8 q8 (graduations "now?") from practice: graduations are already a standing type. The five-or-six section question stays the Magazine's register row (slice 7b).

- **Weddings, births, deaths** are life events and reach the magazine through the family tree's queue (D14, D31) with their consents: a birth on D22's pattern (D33), a death through the family-approval gate (R34).
- **A graduation** is not a lineage fact and has no place in the tree's queue. It is an **announcement on the member's record** with the fields practice uses (school or college, the next institution, honours, degree, a photograph under its own photo consent), dated, and printed only with the graduate's print consent, or, for a minor, the household's on D33's pattern. *Design choice.* For a scholarship recipient the award history prints only with the recipient's consent (UC-2).

### 3.2 Who enters: the household, the correspondent, the editor

Practice has three doors: the family itself, the city correspondent, and the magazine's mailbox. The built rule is that nothing is typed straight into a section. The design keeps that rule and gives the two assisted doors a lawful shape:

- **The correspondent** is the club's seat in the Magazine (Club Experience Plan §3.4; crosswalk J10, E7), appointed on the officers form or by the Magazine, the appointment naming who made it.
- **An assisted submission.** The correspondent, or the editor for an email that reached the mailbox, enters the announcement *on the household's behalf*. It lands as a **pending submission** naming who entered it and from what (a correspondent's note, an email, a printed form). It is not printable until the household's consent act is on record: for a member household, the member confirms through the proof-and-confirm link (UC-4), asked once; for a household with no member, the confirmation comes back through the channel the submission arrived on and is recorded as a consent with its source (R27). What consent the correspondent must hold, and whether an editor's assisted submission is allowed at all, is Q-195; **the assisted door builds as pending-only and prints nothing until Q-195 is answered**. *Design choice for the shape; Q-195 for whether it opens.* *Since 4 Oct 2026:* **D89** answers Q-195: the correspondent's or editor's recorded attestation that the family agreed is enough to print a wedding, birth or graduation; the household is not asked. A death still prints only on the named family contact's approval (D95, limiting D89). A submission with no attestation recorded stays pending as above.
- **The loop still closes.** An assisted submission is a life event or announcement in the same queue, so the data still gets current; what the platform refuses is an announcement that exists only in the editor's layout.

### 3.3 The obituary: an approval and an order

Practice treats an obituary as a placement the family pays for, with a tribute. The record treats a death as a life event needing family approval and says nothing about a fee. Both hold, as two objects:

1. **The death**, as a life event, approved by the named family contact (R34; slice 7's built hold). The family contact who submits and pays is recorded as that contact.
2. **The placement order**: the tribute text, the head shot, dates, city of residence, survivors as the family writes them, the issue requested, the size, and the fee. The survivors' names are the family's text in the tribute and are never linked to person records. *Design choice.*

**What the fee is** (exchange revenue for the placement, a memorial gift, or each by the payer's choice) and which entity receipts it is Q-193. Until it is answered the order is taken, printed when approved, and its fee **is not posted**: it is held as an amount received for an unclassified purpose against ARFECF (D55, the holder of the Magazine's assets), and the receipt says "payment received", with no deductibility statement. IRS Publication 1771's quid-pro-quo rules are the frame the accountants will use where a payment is partly a gift and partly for a service; not confirmed here. *The record, applied; Q-193.*

---

## 4. The people: a staff, an absent board, a Board seat

**What the text sets.** Article III §2: the Magazine operates independently, with its own editorial staff and subscription management. By-Law 6.7.1: subscription fee collection and policy are determined by the Magazine's "independently selected Board in consultation with the Federation's Board of Directors"; the Magazine appoints one of its board members to the Federation's Board for one year at the General Assembly. By-Law 6.2.2 counts "one (1) member of the Magazine" among the Board's voting members. By-Law 9.5.2: a candidate's platform article goes to "the Manager of the Magazine" and must meet "the criteria set forth by the Magazine staff". By-Law 6.5.2: the Magazine publicises the Member-at-Large call before the Mid-Year. By-Law 10.2.1 H: a Magazine representative attends the Mid-Year.

**What practice shows.** A paid staff of five roles and a treasurer, and no board.

**What the platform holds** (*design choice*: seats as register rows, as P19 §4 does for every body):

| Seat | Text | Holder now |
|---|---|---|
| The Magazine's board (members, chair) | 6.7.1 | **Not evidenced.** The rows exist with no holder; the page says the board is not evidenced and cites Q-192 |
| The Magazine's seat on the AFRP Board | 6.2.2, 6.7.1 | Not stated; the leadership directory (P19 DIR2) shows the seat with its vote under 6.2.2 and "appointing body not evidenced" |
| The Manager (9.5.2) | 9.5.2 | The by-law's "Manager" is not mapped to a staff role; whether it is the general manager is part of Q-250 |
| Executive editor; Arabic editor; general manager; subscriptions and circulation manager; advertising; treasurer | Article III §2 ("its own editorial staff and subscription management") | Staff roles appointed by the Magazine, each a dated row naming who appointed; the magazine module's authority grants go to these rows (slice 7's own authority) |
| City correspondents | Club Experience Plan §3.4 | Club seats (§3.2) |
| Mid-Year representative | 10.2.1 H | Named per Mid-Year by the Magazine |

**Policy acts.** The print-only rule (2025), the calendar-year term with its cut-off, the 2027 price and auto-renew are subscription policy, which 6.7.1 gives to the board "in consultation with" the Federation's Board. None of these acts is on file with its author. The platform records each as a **subscription-policy act** with its author's seat and date and the consultation with the Federation's Board as a linked item; an act whose author is a staff seat where 6.7.1 names the board shows that mismatch and is not corrected by software (P11 §3.1's practice for agreements). *Design choice; Q-192, Q-249.*

**Stipends** are payments from the Magazine's account to vendors or individuals on the issue (§6); the platform does not hold payroll or tax forms for them.

---

## 5. The subscriber ledger and its reconciliation

### 5.1 The subscription

One object per subscription, never a flag on a membership:

| Field | What it holds |
|---|---|
| Subscriber | A member, or a contact record for a non-member or a household (D60's shape; Q-70) |
| Format | Print, or digital; digital-with-membership is not a subscription but a benefit read from standing, and is shown as such |
| Term | The term the subscription-policy act sets (today a calendar year, with a cut-off after a stated issue) |
| Payments | Each payment with its channel (card on the portal; cheque at the office; cash or card at an event), the date, the evidence for a manual one, and who keyed it |
| Status | Paid, in grace to the cut-off, lapsed |
| Auto-renew | Only with a stored payment authorisation and its pre-charge notice (LT5's gate: slice 5 and the auto-renewal decision) |
| Mailing address | The subscriber's address for print, under the address consent the subscriber gives for this purpose |

*Design choice for the object; D60 and Q-70 for the non-member shape; R27 for the address consent.*

### 5.2 Reconciliation, once

The subscription manager's own records and the CRM disagreed in 2026. The platform's subscriber ledger starts from **one reconciliation act**: the manager's records and the CRM's subscription payments compared line by line by the manager with the Magazine's treasurer; every manual payment keyed with its channel and evidence; every difference resolved by a dated note; the act closed with both signatures and the opening list frozen (R43's shape: a roll frozen at adoption is never recomputed). After that the manager keys manual payments into the ledger and keeps no second record. *Design choice; it is the use case practice asked for.*

### 5.3 The print list for each issue

At the issue's freeze the platform produces the mailing list from print subscriptions **paid or in grace** at that date, and hands it to the mailing house as §2's dated act with the count. Lapsed print subscribers are excluded automatically; the "report of print subscriptions not renewed" is the list's complement, available to the manager as a count and a list for the appeal (§5.5). Export to anyone but the mailing house under its agreement is refused (P19 rule 6's export refusal; Q-66 for the mailing house). *Design choice.*

### 5.4 The digital issue

Today the digital issue goes by email campaign to a list wider than the membership. On the platform the issue's digital audience is a register row the Magazine sets (members by standing, print subscribers, digital subscribers, the public), and the send goes through the consent filter to those in the audience with a consented email channel. Whether the digital issue is a member benefit, a subscriber benefit or public is Q-196. Until it is answered the audience row is set per issue by the Magazine's own seat as a dated act with its source (Article III §2: its own subscription management), shown as *practice* where it copies the March 2025 notice; a send with no audience row does not leave. *Design choice: the Magazine sets it; the platform does not.*

### 5.5 The appeal

An appeal to lapsed subscribers is a comms campaign to the not-renewed list, with a reply-by date set before the next issue's freeze. The channel is each person's consented channel: email where an email is consented, post where only an address is. Practice in 2026 chose the channel by age band; the platform does not use a date of birth to pick a channel, because a birth date held for standing and minors' protection (R7) is not consented for marketing segmentation. *Design choice; it departs from 2026 practice, and the Magazine may ask for the age split as its own consent question.* Post goes through the mailing house under Q-66. After the appeal the manager sees one list of payments received since the appeal's date by every channel, so a subscriber who paid online is never written to again.

---

## 6. The Magazine's money

**The two texts.** By-Law 6.7.1: "the A.F.R.P. shall appropriate the necessary funds to guarantee its publication." D55: the Magazine's assets are ARFECF's. The 2020 practice of keeping magazine money apart (crosswalk D21) is a practice that sits beside a by-law duty; the conflict is Q-194. The design carries both and decides neither.

**The fund rows** (P9 §2.1 already has "the Magazine's assets", ARFECF, kind not stated). This note splits it as P9 asks for rows that hold two: the Magazine's **operating account** (subscriptions, obituary fees, advertising, gifts in; per-issue costs out) and its **managed investment account** (kind not stated; Q-95 asks which ARFECF assets are donor-restricted). Both ARFECF's (D55), both with the aliases the treasurer's reports use.

**What posts where.**

| Line | Posts as | Entity | Status |
|---|---|---|---|
| A subscription | Exchange revenue for the term | ARFECF (D55's test; Q-194) | Posts once FR1 has the row |
| An obituary fee | Not classified | Held (§3.3) | Waits on Q-193 |
| An advertisement | Exchange revenue | ARFECF | The ads desk's payment path refuses until paying for ads is decided (slice 7) |
| A gift to the Magazine | A restricted gift to the Magazine | ARFECF (D55's test; Q-194), receipted by ARFECF (D9) with no deductibility statement until ARFECF's determination letter is on the registry (P9 §6.2) | Posts once FR1 has the row |
| Per-issue costs (stipends, design, print, mailing) | Expense, tagged to the issue | ARFECF | Posts |
| An appropriation from the Federation | An inter-entity transfer from AFRP's General Fund to ARFECF for the Magazine, recorded only as a dated act citing the budget line that voted it and 6.7.1 | AFRP → ARFECF | **Gated** on Q-194: until the Boards say what the Federation appropriates and how it is recorded, an untyped transfer between the two refuses |
| A seed deposit or a loan to the Magazine | As above, with its terms | AFRP → ARFECF | As above; P9 rule 8 (a loan only with the authority that approved it) |

*Design choice for the table; D55, D9, P9 rules 1, 6 and 8, and By-Law 6.7.1 for its terms.*

**The per-issue report.** The treasurer's chequebook report becomes, once the rows post, a per-issue statement from the ledger: income by kind and costs by kind against each issue, and the account's balance at the Board's meeting date. In whose name the Educational Fund Treasurer's set of reports is filed is Q-174; the Magazine's report is one of them in practice. *Design choice; Q-174.*

---

## 7. The archive

Slice 7 built the archive of issues printed on the platform, searched by family name through the directory gate, frozen as printed (UC-8). What exists before the platform is three things: the paper back issues; the 2013–14 history CD/DVD; and the 1959–2018 scans the Preservation grant is producing.

- **Where they live.** The scans and the DVD's content are documents on the shared drive, the archive of record (D66). The platform holds an **issue register** for back issues (volume, number, date, the drive link, whether scanned, the scanning act) and links to the drive; it does not ingest the scans. Full-text search over back issues is not built until the Magazine and the Board decide their openness. *D66; design choice for the register.*
- **Who may read them.** Whether back issues are open, a member benefit or public is Q-196. Whatever the answer, a back issue names living people with dates and life events, and **nothing about a living person shows without sign-in** (D28): a signed-out reader may be shown a back issue's cover and table of contents, and nothing that names a living person, until the Board decides otherwise by decision. *D28, applied.*
- **Selling the archive.** The DVD was a product; whether back issues are sold, and at a member price, is Q-199 (§8).

---

## 8. The bookstore: two stores against the Hub's

### 8.1 What each has

| | afrp.org shop (WooCommerce) | Portal "Digital Store" (Power Apps) | Hub `store` (MASTER-PLAN §1a; the register) | Use-case note |
|---|---|---|---|---|
| Titles | Seven books | Six of the seven | Catalogue built; contents not in the record | Books, back issues, clan books, merchandise, downloads |
| Member price | None | None | Built | Yes (UC-9) |
| Shipping | US addresses only | Shipping-address step | Not stated | Not stated |
| Stock | Not shown | Not shown | Inventory built | Decremented at payment |
| Digital goods | None | None | Not stated | Entitlements |
| Deductibility text | The site's donation text appears on the cook book's page | Not observed | — | Never on a sale (UC-11) |
| Owner | Not recorded | Not recorded | `store:manage` grant | Not stated |
| Order log | Not found | Not found | Built | Fulfilment queue (UC-10) |

### 8.2 What the record says, and what follows

- **Which store is kept** is Q-197. Until it is answered the Hub's store is **not populated from either live store** and nothing is migrated; it stays as built, on the fixture. *The record, applied.*
- **Each title has a holding entity.** D55's test (the fund that carries it in the approved budget) gives ARFECF for the cook book, whose sales are Educational Fund income; the other six titles have no budget line, so their entity is not stated, and a sale of them posts nothing on the platform until Q-197 names it (P9 rule 1, applied to a product line). An order with lines from two entities posts each line to its own entity and never nets them; the payment goes to the processor profile of the entity that receives it (the Federation now runs one card account per entity, research round). *Design choice resting on D55, P9 rule 1 and the Club Experience Plan §5.1's rule that entity lines never net.*
- **A purchase is not a gift.** No sale, product page or order confirmation carries a deductibility statement (UC-11; D9). The live shop's cook-book page shows the donation text today; the platform refuses it on any catalogue entry. *UC-11, applied.*
- **Shipping as a stated rule.** "US addresses only" is practice in both stores. On the platform it is a catalogue parameter set by the store's owner, **shown on the catalogue page before checkout** (the visitor lens already asks for this), with no default: until the owner sets it, checkout refuses and names Q-197. *Design choice.*
- **Member pricing** is built and practised nowhere. Whether a member price exists, and on which lines, is Q-199; the built price is held at no value (list price for all) until then. *The record, applied; Q-199.*
- **Clan books** are not for sale today; they are PDFs behind the family tree's access request, which carries living people's dates (Q-202). They are never a store product while Q-199 and Q-202 are open, and never without sign-in (D28). *D28; Q-199, Q-202.*
- **Sales tax** follows the use-case note §5 (Michigan first, the nexus monitor); whether Michigan registration exists is Q-198. *Carried.*
- **Fulfilment** has no owner in practice; UC-10's queue stands, and the fulfilment seat is a register row with no holder until Q-197 names the store's manager.

### 8.3 Stock, reprints and resellers

- **Stock.** Per title: on hand (by location if more than one), on consignment (per reseller), and each movement as a dated act: a reprint received, a sale, a consignment out, a consignment sold or returned, a write-off. *Design choice extending UC-9's inventory.*
- **A reprint** is an order to a printer paid from the title's fund, recorded with the quantity received; the cook book's reprints have been paid from the Cook Book fund.
- **A reseller** (a museum store sells the cook book today) holds stock under a written term: wholesale or consignment, price, settlement period. The term is an agreement on P11's partner-agreements register (CG2) of a new kind, *reseller*, with the signatory row per entity (Q-107). No such agreement is on file; on load the reseller's row shows "no agreement on file" and stock it holds is recorded only from a dated count. *Design choice; Q-173 for the terms.*

---

## 9. The Cook Book

**As found.** A separate fund (a Board-reported chequebook) of ARFECF's by D55's test; a product line in both stores; a book compiled by a third party (a Detroit women's union, 1976) and reprinted by the Federation; resold by at least one museum store; a trademark application in its name pending. P9 §2.1's row says "whether it still exists is not stated"; it exists. Its 2025–26 transfer to the Education Fund for systems is a cross-fund movement the Fund Rules do not allow for non-earmarked money (the Decisions Register's research-round row; Q-173).

**The fund row** (FR1): holding entity ARFECF on D55's evidence, for the Boards to confirm (Q-173 asks "which entity's books carry the fund"); kind not stated (a sales fund; neither restricted by a donor nor designated by a Board resolution on file); authoriser for a transfer out **not stated** (Q-173), so a transfer out refuses and names the question; report duty: the Educational Fund Treasurer's per-meeting statement (Q-174). Once its kind and governing text are set, sales post to it as exchange revenue for the title and reprints and the title's costs post against it. Until then nothing posts to or from it (P9 rule 1; P26 §6.2): a sale is held as a liability for the fund to be completed, and a transfer out refuses naming Q-173. *P9 §2, applied.*

**The rights row on the catalogue entry.** Every title carries: the copyright holder as the record knows it, with its source, or "not stated"; any licence or permission under which the Federation reprints or sells it, linked on the drive; any trademark (the mark, the applicant entity, the status, the registration number when granted). Trademark and copyright protect different things: a mark identifies the goods' source; copyright protects the text (USPTO, Sources). Who holds the copyright of a 1976 third-party compilation, and in which entity's name the mark is applied for, are Q-173; the term of a work published before 1978 turns on its publication and renewal facts, which the Legal Advisor confirms (Copyright Office Circular 15A; not confirmed here). While the copyright row says "not stated", the platform sells the existing stock the Federation holds and **refuses to record a new reprint order**, naming Q-173. *Design choice: a reprint is a new copy; a sale of stock already printed is not.*

The other six titles get the same rights row on load, each "not stated" until the Legal Advisor fills it; a title whose row is "not stated" may be sold from existing stock and not reprinted. *Design choice, applied evenly.*

---

## 10. Rules

1. Cadence, sections, audience and every other magazine parameter are the Magazine's register rows, attested by its seats; the platform sets none (Article III §2; slice 7).
2. The qualifying issue for the Convention notice is the one mailed at least sixty days before; the Convention issue never is (By-Law 10.1.4; slice 7).
3. Nothing is printed that was typed straight into a section; an assisted submission is pending until the household's consent act is on record, and the assisted door stays closed until Q-195 is answered (the use-case note §0; R27; D33; *design choice*). *Since 4 Oct 2026:* an attestation recorded under D89 is the consent act for an assisted submission.
4. A graduation is an announcement on the member's record, not a tree declaration, printed only on the graduate's print consent or, for a minor, the household's (*design choice*; D33's pattern).
5. An obituary is two objects: a death under the family-approval gate (R34) and a placement order; the fee is held, unposted, until Q-193 classifies it, and its receipt makes no deductibility claim (*design choice*; D9).
6. The 6.7.1 board, its 6.2.2 seat and the 9.5.2 Manager are seats with their texts cited and no holder until evidenced; a subscription-policy act records its author and shows a mismatch with 6.7.1 without correcting it (By-Laws 6.2.2, 6.7.1, 9.5.2; *design choice*; Q-192).
7. A subscription is its own object for a member or a contact, with every payment's channel and evidence; the ledger opens with one closed reconciliation act and no second record is kept after it (D60; Q-70; R43's shape; *design choice*).
8. The print list goes only to the mailing house, only under its agreement, only as a dated act with a count (Q-66; P19 rule 6; *design choice*).
9. An appeal goes to each person's consented channel; a birth date never chooses a channel (R7; R27; *design choice*).
10. The Magazine's assets are ARFECF's (D55); its operating income posts to ARFECF on D55's budget test, for the Boards to confirm with Q-194; an appropriation from the Federation is a typed inter-entity act citing the budget line and 6.7.1, refused until Q-194 is answered (By-Law 6.7.1; P9 rules 6 and 8).
11. Back issues live on the drive (D66); nothing in a back issue that names a living person shows without sign-in (D28); openness is Q-196.
12. Each title has a holding entity and posts nothing until it is set; an order never nets entities (D55; P9 rule 1; *design choice*).
13. No sale carries a deductibility statement (UC-11; D9).
14. Shipping limits are shown before checkout and have no default (*design choice*).
15. A reseller holds stock only under a recorded agreement or a dated count (*design choice*; Q-173).
16. A title whose copyright row is "not stated" is sold from stock and never reprinted (*design choice*; Q-173).
17. Every act is dated, by a named seat, and corrected only by a new act naming the old (R24; R27).
18. No figure, price or person in this note (D54).

---

## 11. What this note raises

| Q | Question | Owner |
|---|---|---|
| Q-249 | Who adopted the subscription policies in force (print only for paid print subscribers from 2025; the calendar-year term and its cut-off; the 2027 price; auto-renew), and was the Federation's Board consulted as By-Law 6.7.1 requires? Until the 6.7.1 board exists, which body may set subscription policy? | The Magazine · AFRP Board · Constitution Committee |
| Q-250 | By-Law 9.5.2's "Manager of the Magazine" and "the criteria set forth by the Magazine staff": which staff role is the Manager, and where are the criteria for candidates' platform articles written? | The Magazine · Selection Committee |

Carried, not new: Q-66 (the mailing house and post), Q-70 (the contact record for non-member subscribers), Q-95 (the kind of the Magazine's investment account), Q-107 (who signs a reseller agreement), Q-173 (the Cook Book fund, copyright, trademark, resale), Q-174 (the per-meeting reports), Q-192 (the 6.7.1 board), Q-193 (the obituary fee), Q-194 (6.7.1's funding duty), Q-195 (the correspondent seat's consent), Q-196 (the digital issue and back issues), Q-197 (the bookstore's owner and which store), Q-198 (sales tax), Q-199 (product lines and member price), Q-202 (clan books with living people's dates).

---

## 12. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| MG1 Announcements as they arrive | Graduation as an announcement on the member record with its fields and print consent; the assisted submission (correspondent or editor) as pending-only with its source and enterer; the household's consent act through proof-and-confirm or the arriving channel; the obituary as a death plus a placement order, its fee held unposted with a "payment received" receipt | §3 | The assisted door is open under D89 (4 Oct 2026); the obituary fee posts on Q-193; C1 for the correspondent seat |
| MG2 The subscriber ledger | The subscription object for members and contacts; payments by channel with evidence; the reconciliation act and frozen opening list; status and the cut-off from the policy act; the print list at freeze as a dated hand-off to the mailing house | §5.1–§5.3 | The hand-off waits on Q-66; contacts use D60's record (Q-70 for retention); auto-renew stays on LT5's gate. *Since 2 October 2026:* a non-member subscriber is P21's subscriber role, built in CR6 and gated as P21 §14 says (Q-70; Q-239 for the address and the list); until then MG2 builds the subscription for members and a non-member subscription refuses by name |
| MG3 The digital issue and the appeal | The audience register row; the send under the consent filter; the not-renewed list; the appeal by consented channel with a reply-by date; the payments-since list | §5.4–§5.5 | The audience row's value is Q-196; post waits on Q-66 |
| MG4 The issue's hand-offs and the people | The hand-off acts on the issue (layout, print, mail, digital, payments); the vendors on the store register; the 6.7.1 board and 6.2.2 seat as empty rows with their texts; the staff rows and the subscription-policy act with the mismatch shown; the 9.5.2 Manager row | §2, §4 | IR5's store register for the vendor rows; Q-192, Q-249, Q-250 for holders |
| MG5 The Magazine's money | The operating and investment rows on FR1; posting by kind; the per-issue statement; the Federation's appropriation as a typed act, refused until Q-194 | §6 | FR1; Q-194 for the appropriation; Q-193 for obituary fees |
| MG6 The back-issue register | Issues as rows with drive links and the scanning act; signed-out access limited to cover and contents; no full-text ingestion | §7 | Q-196 for openness |
| MG7 The bookstore reconciled | Per-title holding entity and rights rows; entity-split orders and per-entity processor profiles; the shipping parameter shown before checkout; no deductibility text on any entry; stock movements, reprints and consignment; the *reseller* agreement kind on CG2; the Cook Book fund row with its transfer refusal; member price held at list | §8, §9 | Q-197 before any live catalogue or migration; Q-173 for rights and reprints; Q-198 for tax; Q-199 for price and lines; CG2 for the reseller kind |

Order: MG2 first (it replaces a second ledger kept by hand and needs only FR1 and D60's record); MG5 with it; MG1 and MG4 next; MG3 after MG2; MG6 when the scans reach the drive; MG7 when Q-197 is answered, except the refusals (deductibility text, entity split, shipping default), which build now against the fixture.

---

## 13. Journeys proposed

Identifiers are provisional; the Hub's workbench assigns catalogue ids.

| Journey | Tests | Must reach | Slice |
|---|---|---|---|
| P24-J01 A graduation on the correspondent's word | A correspondent enters a graduation for a member with an attestation that the family agreed; the entry records who, when and from what; it prints in the next issue's section; the member is not asked *(rewritten 4 Oct 2026 under D89; it read: pending, the member confirms once through proof-and-confirm, guarded until Q-195)* | meets once MG1 lands | MG1 |
| P24-J02 No consent, no print | An assisted submission with no household consent act and no attestation recorded (D89) is absent from the frozen section and listed in the exceptions report | meets | MG1 |
| P24-J03 An obituary is approved and ordered | A death approved by the named family contact and a placement order with its tribute both exist; the fee is held unposted with a "payment received" receipt that makes no deductibility claim | meets (the hold); guarded until Q-193 (posting) | MG1 |
| P24-J04 One subscriber ledger | After the reconciliation act closes, a cheque keyed by the manager and a portal payment appear in one list with channels; no second list exists | meets | MG2 |
| P24-J05 Only paid print is mailed | At freeze, a lapsed print subscriber is absent from the mailing list; the hand-off records the count and the vendor; with the mailing house's agreement row empty the hand-off refuses and names Q-66 | guarded until Q-66 | MG2 |
| P24-J06 The appeal never chases a payer | A lapsed subscriber who pays online after the appeal's send is on the payments-since list and receives no follow-up | meets | MG3 |
| P24-J07 No age-based channel | An appeal to a person with a consented email goes by email whatever their age; to one with only an address, by post | meets | MG3 |
| P24-J08 The board is shown absent | The 6.7.1 board rows and the 6.2.2 seat show their texts and "not evidenced"; a subscription-policy act authored by a staff seat shows the mismatch | meets | MG4 |
| P24-J09 Magazine money stays typed | A transfer from AFRP's General Fund to the Magazine without a cited budget line and 6.7.1 refuses and names Q-194 | meets (the refusal) | MG5 |
| P24-J10 A back issue signed out | Signed out, a back issue shows its cover and contents and no page naming a living person | meets | MG6 |
| P24-J11 A purchase is not a gift | No catalogue entry, order or receipt carries a deductibility statement; an attempt to add the donation text to a product refuses | meets | MG7 |
| P24-J12 An order splits by entity | An order of the cook book and another title posts the cook book line to ARFECF and refuses the other line while its entity is unset, naming Q-197 | guarded until Q-197 | MG7 |
| P24-J13 US-only is said before checkout | With the shipping parameter set to US only, the catalogue page says so before the cart; with it unset, checkout refuses and names Q-197 | meets | MG7 |
| P24-J14 No reprint without rights | A reprint order for a title whose copyright row is "not stated" refuses and names Q-173; a sale from stock proceeds | meets | MG7 |
| P24-J15 Consignment is counted | Stock sent to a reseller is recorded as on consignment with no agreement on file shown; stock on hand drops by the same count | meets | MG7 |

---

## 14. What changes in the site's data with this note

`programmes.yaml`: `magazine` cites this note under `platform_needs` (the subscriber ledger, the assisted submission, the obituary as order, the hand-offs, the board seats as empty rows, the money table, the back-issue register) and its `organiser` notes the 9.5.2 Manager as unmapped (Q-250); `bookstore` cites this note, its `in_service` and `platform_needs` carry the two-store comparison and the per-title entity and rights rows, and its `money` drops "register and collect in Michigan first" as a statement of fact in favour of Q-198. `workflows.yaml`: `magazine-announcements` moves from "Proposed" to "Designed" with this note, its "Hold a death until the family approves" step cites R34 (not D33), and it gains the reconciliation and the print-list hand-off steps; `magazine`'s bookstore step cites §8 and gains the per-title entity and the shipping statement. `experiences.yaml`: the visitor lens cites §8.2 for the shipping statement; the club officer lens's correspondent lines cite §3.2; a programme-lens line for the subscription manager's single ledger and the Magazine treasurer's per-issue statement. `questions.yaml`: Q-249 and Q-250. The crosswalk: D18 and D21 cite P24, E7 and J10 cite §3.2; a P24 row in the design-notes table. `plan/MASTER-PLAN.md`: rows MG1–MG7. `AFRP-Magazine-Bookstore-Use-Cases.md` (the owning agent): a header note that §0's "three times a year" and §8 q1, q6 and q8 are answered in practice by P24, and that UC-2's death rule stands beside the paid placement (P24 §3.3). `AFRP-Fund-Rules.md` §2.1: the Magazine row split into operating and investment accounts; the Cook Book row's status changed from "whether it still exists is not stated" to "exists; transfers out unauthorised until Q-173".

---

## Sources

**Record.** `design/AFRP-Magazine-Bookstore-Use-Cases.md` (whole); `design/AFRP-Delivery-Status.md` slices 7, 7b, P1; `plan/MASTER-PLAN.md` §1a; `design/AFRP-Decisions-Register.md` D9, D14, D22, D28, D31, D33, D41, D54, D55, D60, D61, D66, and the section "Conflicts between practice and the record found in the research round of 2 October 2026" (the Magazine and Bookstore rows); `design/AFRP-Rules-Register.md` R7, R24, R27, R34, R43; `design/AFRP-Fund-Rules.md` (P9) §2, §2.1, §6.2, rules 1, 6, 8; `design/AFRP-Care-Grants-and-Partners.md` (P11) §3, §3.1; `design/AFRP-Club-Experience-Plan.md` §3.4, §5.1; `design/AFRP-Directory-Formats.md` (P19) §4, rule 6; `design/AFRP-Incident-Response-and-Retention.md` (P15) and MASTER-PLAN row IR5 (the store register); `design/AFRP-Strategic-Plan-Crosswalk.md` D18, D21, E7, J10; `site/data/programmes.yaml` (`magazine`, `bookstore`), `workflows.yaml` (`magazine`, `magazine-announcements`), `experiences.yaml`, `questions.yaml` (Q-66, Q-70, Q-95, Q-107, Q-173, Q-174, Q-192 to Q-199, Q-202); AFRP Constitution and By-Laws 2024, Article III §2, By-Laws 6.2.2, 6.5.2, 6.7.1, 9.5.2, 10.1.4, 10.2.1 H.

**Private research.** Research round, 2 October 2026 (heritage §1, §4, §5, §7), private. Research round, 2 October 2026 (education §6a, the Cook Book fund), private. Research round, 2 October 2026 (federation §4, one card-processing account per entity), private.

**Outside.** IRS Publication 1771, *Charitable Contributions — Substantiation and Disclosure Requirements* (quid-pro-quo disclosure where a payment is partly a gift and partly for goods or services): https://www.irs.gov/pub/irs-pdf/p1771.pdf · USPTO, *Trademark, patent, or copyright* (what a mark protects against what copyright protects): https://www.uspto.gov/trademarks/basics/trademark-patent-copyright · U.S. Copyright Office, Circular 15A, *Duration of Copyright*: https://www.copyright.gov/circs/circ15a.pdf (the term of a work published before 1978 depends on notice and renewal; how it applies to the cook book is **not confirmed** and is for the Legal Advisor, Q-173) · The two stores and a museum store's listing as read in the research round on 2 October 2026 (https://afrp.org/shop/, https://afrp.org/product-category/books/, https://my.afrp.org/AFRP-Digital-Store/; not re-fetched here).
