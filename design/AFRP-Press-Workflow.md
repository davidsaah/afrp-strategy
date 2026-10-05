# Press releases and public statements

### A statement or release as one object on the comms desk: its kind, its clock, its drafter and approver, the entity it is issued under, the media list it goes to, and the archive it lands in

**Design note P6 · 1 October 2026 · for the Hub's `comms` module, the institution registry and the funds ledger**

*Since 4 October 2026 (D99):* the shared shapes this note draws — the approver seats as authority rows, sending, statements as work items and the 24-hour clock — are built once as the platform primitives of `AFRP-Platform-Primitives.md` (P29 §3, §4, §8, §10, §11); this note's rules are carried as their settings.

**What it rests on.** Crosswalk row E6 ("Press releases: proactive and reactive, a 24-hour clock, a media list"; source PR). The PR working papers behind FED2 §A, read in full: the Media and Public Relations Committee's business plan (May 2018), the Strategic Planning Committee's press-release proposal (undated, 2020–21), the communications-management deck and the communications-intern description. D65 (advocacy and the Federation's public statements are AFRP General Fund activity; the Legal Advisor to confirm the 501(c)(4) limits), D66 (the drive is the archive of record), D9 and D55 (receipts and books follow the holding entity), D50 (roles only on public pages). By-Laws 6.7.1, 7.2.1, 7.9.3, 9.5.2 and 11.1.1, read for the clauses cited. The `communications` workflow (two senders, one consent model). The intakes, at role level: the Government Affairs letters and statements, the Federation's convention folders (a press release per Convention), ARFHSN's Letters & Statements folder, the endowment campaign's spokesperson talking points (August 2025). Outside: the IRS pages on social welfare organisations, on lobbying, and on political campaign intervention by 501(c)(3)s, cited at the end.

**Precedence (D41).** The by-law texts; then the register (D65, D66, D9, D55) and the named design documents (the Four-Lens §9 on communications; the club plan §9; P3's template register, which this note reuses); then the PR papers, which are proposals and plans that were never adopted by any minute found, and are cited as the source of the *shape* and never of a rule; then the prototype's `#/fed/comms`; then the `comms` module as built.

---

## 1. What the record already holds

**Built (`comms`, the Federation desk; slice 5 pending for real email).** Audiences built from segments and rosters with consent checked at build time and the withheld stored by name; three message classes (operational, marketing, programme invitation); a send gated on `message:send`; undeliverable shown as not tracked (workflow `communications`). The audience builder cannot express a non-member (Delivery Status): a media list is not an audience the desk can build today. The design system carries the brand (crosswalk E10).

**Decided.** D65: "the Federation's public statements are AFRP General Fund activity. The platform refuses to charge any of it to ARFECF or ARFHSN." D66: the drive is the archive. D60: a non-member contact record exists (name, verified channel, consent) for the Arabic term, and P4 extends it to referrals — the shape a media contact needs. D10's four contributor moments are not statements and are untouched.

**In the text.** 7.9.3: the Executive Director shall "coordinate all official approved A.F.R.P. communication that will be disseminated from the A.F.R.P. office", "institute a Public Relations campaign to other Arab American Organizations as well as the General Public", "engage in marketing and advertising on behalf of the A.F.R.P.", and "have responsibility for coordinating all media activities, and along with the Board of Directors will decide who will represent the A.F.R.P. with respect to any and all media interaction". 7.2.1: the President is the principal executive officer and presides. 6.7.1: the Magazine "shall be the official media source for information concerning the A.F.R.P.". 11.1.1 is about contracts and instruments, not statements. 9.5.2: a candidate may submit a platform article to the Magazine. Nothing in the 2024 by-laws says who approves the text of a public statement, who signs it, or what a club may say in the Federation's name; "official approved" in 7.9.3 presupposes an approval it does not describe.

**In the PR papers (proposals, 2018–2021).** The 2018 business plan of a Media and Public Relations Committee: a committee chair appointed by the Federation who recruits the members; up to seven media spokespersons who "in the absence of the AFRP President" respond to inquiries; a bank of about twenty storytellers; writers with samples; social-media volunteers; partnerships with other organisations; proactive and reactive work ("prepare and respond to media reports"); a yearly evaluation by the President and the Board; a budget line that was never evidenced as funded. The press-release proposal: volunteers wrote releases and a paid service distributed them, with "limited success in Palestine" and none in mainstream media; the committee worked "on an ad hoc and emergency basis"; recommended a media-relations intern reporting monthly, about ten experienced writers, a rotating committee member on watch to monitor, write and respond, a media list built locally and nationally with the clubs and updated yearly (outlet, press contact, contact details, area of interest — "like politics all news are local"), ready templates, a timetable — proactive releases prepared ahead, feature stories with a release date, "reactive press releases must be done in a less than 24 hours cycle" — and a named contact who can speak for the Federation. The communications-management deck: one communications manager reviewing every outgoing message across social media, email, newsletters, releases and the Magazine, reporting to the Executive Committee, with a scheduling tool. The intern description: drafting releases for the Communications Committee, the newsletter, social media.

**Historically (the intakes, role-level).** The Federation issues statements and letters on legislation and events — signed by the sitting President, on AFRP letterhead, drafted by staff or the Government Affairs Committee; "no written approval rule found (who clears the position text is not stated)"; copies kept as document pairs on the drive with no log of replies; some letters lobby on named bills while one says the Federation "does not take formal positions on final political outcomes". Each Convention's folder holds a press release. ARFHSN's drive has a Letters & Statements folder of letters the Federation President signed naming the Medical Mission as the single channel for a major gift's projects — statements of the Federation about an ARFHSN programme, under the President's signature. The endowment campaign's talking points recommend a trained pool of three or four spokespersons and state compliance lines. A Media and PR committee has appeared in the committee directories since 2017–18 and in the 2026 organisational chart; it is a created committee (8.1.1), not a standing one. The General Assembly adopts resolutions, some political, which are public statements of the membership, minuted. The only 24-hour clock in the record is the proposal's.

---

## 2. The statement as an object

A **statement** is one row on the comms desk's template register (P3 §2, extended), of class *public*, which the three existing classes do not cover because its audience is not members. It carries:

- **kind**: *proactive* (prepared for an event or a programme: a Convention, the Medical Mission, the scholarship, a feature) or *reactive* (a response to a media report, an event, legislation) — the proposal's two;
- **trigger**: for a reactive statement, the dated event the Federation is responding to, typed by the drafter; for a proactive one, the event or programme row it concerns;
- **the clock**: for a reactive statement, 24 hours from the trigger to issue, as the proposal sets it — a follow-up on the drafter's and approver's seats with the time remaining shown; the figure is a parameter row citing the PR proposal, not a by-law, because no text adopts it (*design choice, labelled as the proposal's figure*). A proactive statement has a release date and no clock;
- **drafter seat**: the seat that writes it — the Government Affairs Committee's chair for advocacy, the Executive Director's seat for official communication (7.9.3), the Media and PR committee's chair where it exists on P1's register, a programme committee's chair for its programme; never a person;
- **approver seat**: who approves the text before issue. **The record does not say.** 7.9.3 says the Executive Director coordinates "official approved" communication and, with the Board, decides who represents the Federation to the media; practice is that the President signs. The platform carries the approver seat as a register row per statement kind with no value until the Board sets it, and a statement with no approver recorded cannot be issued — it can be drafted, circulated to seats, and held (*Q-80*). Where the Legal Advisor's review is wanted for a statement on legislation, it is a second approval row (*Q-80* asks whether it is required);
- **signatory seat**: whose name it goes out over — the President's by practice (7.2.1); a spokesperson's where the Board and the Executive Director have named one (7.9.3; §4);
- **entity**: the entity whose name it is issued in. **AFRP for every statement of the Federation** (D65). A statement *about* an ARFECF or ARFHSN programme (a Medical Mission release; a scholarship release) is still the Federation's statement, issued under AFRP's name and charged to the General Fund, unless the affiliate's own Board issues it under its own name — in which case it is that Board's statement on that entity's lens, and the platform records which it is. Any cost of a statement (a distribution service, a paid writer) posts to AFRP's General Fund; the ledger refuses an ARFECF or ARFHSN line for it, by D65's name;
- **the text**: a link to the adopted text on the drive (D66), with the draft's own text held on the platform only until issue; after issue the drive copy is the record and the platform keeps the row, the date, the seats, the audience and the link;
- **audience**: the media list (§3), and optionally the members under the `communications` workflow's operational or marketing class as the Board's rule gives (a statement to members is a member send, consent-checked, and is recorded against the same row);
- **states**: drafted, circulated, approved, issued, withdrawn, superseded (a correction is a new statement linked to the first; the first is never edited, R27's retraction pattern).

**What the Federation's statement is not.** A resolution of the General Assembly (minuted, the voting module's recorded ballot; it is a decision, not a release, and the release about it is a separate row). A letter to an official (P3's register, class operational, the President's seat — the Government Affairs letters; the same row shape, a different class and audience, and *Q-80*'s approver applies to it too). A Magazine article (the Magazine's own copy process, slice 7; 6.7.1). A programme's own invitation or newsletter (the programme-invitation class). A fundraising appeal (giving).

**What the platform refuses.** A statement issued with no approver recorded; a statement charged to an affiliate (D65); a statement whose signatory is a person and not a seat; a statement to a media contact who has not consented to be on the list (§3); editing an issued statement; a club issuing a statement in the Federation's name (§5).

---

## 3. The media list

A **media contact** is a contact record (D60's shape: name, outlet, verified channel, area of interest, the dated consent to receive the Federation's releases, the source of the consent — a reply, a sign-up, a published press contact), on the institution registry under the outlet as an institution, never a member record and never in any member audience. The list is the Federation's; a club may hold its own contacts for its own statements (§5), on its lens, and the Federation's list is not exported to it (the `communications` rule: no list leaves the platform). The proposal's yearly update is a review follow-up on the list's owner seat each year; a contact with no activity and no renewed consent after a parameter with no value is withheld, not deleted, until the owner acts (*Q-70* for the parameter and the consent basis — a published press address is a solicitation address and the record is silent on whether that is consent enough for an unsolicited release; the Legal Advisor to say). Outlets are tagged by area of interest and locality so that a club's local press and the national list are one list filtered, which is the proposal's "all news are local" made a field. The list is readable by the drafter and approver seats and the Executive Director (7.9.3); it carries no member and nothing of a person beyond the contact's own professional details.

*Since 2 October 2026:* the contact record note (P21 §6) offers two homes for a media contact. Under option (a), the media contact is a person record with a *media contact* role anchored to the outlet's registry row, and the registry shows the role under the outlet. Under option (b), the record as written here, the contact stays on the institution registry. P21 offers (a) as a DRAFT under Q-70 and adopts neither. **This section stands as written until Q-70 is answered** (D41). The media contact's retention row is P21 §9's, with no value, and PR1 is touched by no CR slice. A club's own media contacts are among the roles P21 §10 lets a club see.

---

## 4. The spokesperson

7.9.3 gives the Executive Director, with the Board, the decision of "who will represent the A.F.R.P. with respect to any and all media interaction". The platform records that decision as a **spokesperson seat** on P1's register (CW1), appointed by a Board act with the Executive Director's recommendation, dated, for a term; the 2018 plan's "up to seven" and the 2025 talking points' "three or four" are figures from proposals and the platform holds the count as a parameter with no value. The spokesperson seat is what crosswalk E7 and the proposed note P7 (volunteer interests and rosters) will fill from members who have offered to speak and been trained; until VI4 (P7) lands, the seat is a CW1 row with "no appointing text beyond 7.9.3" and the office types the holder. A statement's signatory may be a spokesperson seat; a media inquiry (a reactive trigger) is routed to the spokesperson seats and the Executive Director. A club's own spokesperson is the club's business (§5).

---

## 5. The club's statements and the Federation's

A club speaks for itself. The platform lets a club's officers draft and issue a statement on the club lens, under the club's own name, to the club's own media contacts, with the club's own approver (its president's seat, or whatever its officers form names), and records it on the club's lens only; the Federation sees a count (S7) and never the text unless the club sends it up. A club may not issue a statement in the Federation's name: the Federation's register is the Federation's, its drafter and approver seats are Federation seats, and a club officer's seat does not hold `message:send` on it. Where a club's statement concerns a Federation or affiliate programme, the club's row may carry the programme as attribution, which is what makes the club's count appear on that programme's page. Whether a club's statement on legislation is the club's own tax matter is outside the platform; the club's register row carries the club's tax status as the club states it (club plan §6.1), and the platform says nothing about it.

---

## 6. What a 501(c)(4) and a 501(c)(3) may say — the gate on D65

The record describes AFRP as a 501(c)(4) (an IRS letter of 2011 and the by-laws' entity summary; Q-38, now D65) and ARFECF and ARFHSN as 501(c)(3)s (ARFHSN's text; ARFECF's determination letter is not on file, D2). From the IRS's own pages:

- A 501(c)(4) social welfare organisation "may further its exempt purposes through lobbying as its primary activity without jeopardizing its exempt status", may have to notify members of the share of dues applicable to lobbying or pay a proxy tax, may "engage in some political activities, so long as that is not its primary activity", and any expenditure for political activity may be taxed; campaign intervention "does not promote social welfare" (IRS, *Social welfare organizations*).
- A 501(c)(3) is "absolutely prohibited from directly or indirectly participating in, or intervening in, any political campaign on behalf of (or in opposition to) any candidate for elective public office", and that includes "public statements of position (verbal or written) made on behalf of the organization in favor of or in opposition to any candidate" (IRS, *The restriction of political campaign intervention by section 501(c)(3) tax-exempt organizations*). On legislation, a 501(c)(3) may lobby only if "no substantial part" of its activities is attempting to influence legislation; educational activity on public policy is not lobbying (IRS, *Lobbying*).

What the platform does with this, which is D65 applied and nothing more: every statement is AFRP's unless an affiliate's Board issues it under its own name; a statement an affiliate issues carries a *subject* field the drafter sets — *programme*, *legislation*, *candidate* (distinct from the *kind* of §2, proactive or reactive) — and *legislation* and *candidate* on an affiliate's statement are refused with D65 and the IRS page cited, because the affiliates do not carry advocacy (D65) and a 501(c)(3) may not speak for or against a candidate at all. On AFRP's own statements the platform refuses nothing on content — the Legal Advisor's confirmation of the 501(c)(4) limits (D65's condition) is a review row the approver can require (*Q-80*), and the Federation's own sentence that it "does not take formal positions on final political outcomes" is the Federation's policy to keep or drop, not the platform's rule (*Q-81*: whether the Board has a position policy, and what the dues-notice or proxy-tax consequence of lobbying is for a membership organisation — the Legal Advisor and the CPA). The *kind* field is what lets the General Fund's advocacy cost be reported per D65 and the lobbying share be known if the notice is needed.

---

## 7. Rules

1. A public statement is a row on the comms desk's template register, class *public*, with kind, trigger, clock, drafter seat, approver seat, signatory seat, entity, text link, audience and states (P3 §2's register, extended; *design choice*).
2. A statement is issued only with an approver seat recorded; the seat is a parameter with no value until the Board sets it (7.9.3's "official approved"; *Q-80*).
3. Every statement of the Federation is AFRP's and its cost is the General Fund's; the ledger refuses an affiliate line for it (D65); an affiliate's own statement is its Board's, on its lens.
4. A reactive statement carries a 24-hour clock from its trigger, a figure from the PR proposal held as a parameter and not a rule (*design choice, labelled*).
5. A media contact is a contact record under its own dated consent on the institution registry, never a member and never in a member audience (D60's shape; R27; *Q-70* on the consent basis; D60 is written for the Arabic term and its use for a media contact is a reading, raised as one question for governance with P4's Q-70).
6. The spokesperson is a seat the Board appoints on the Executive Director's recommendation (7.9.3; CW1); a signatory is always a seat (P3 rule).
7. An issued statement is never edited; a correction is a new linked statement (R27's retraction pattern).
8. The drive holds the text of record; the platform holds the row and the link (D66).
9. A club issues statements in its own name only, on its lens, to its own contacts; the Federation sees counts (S7; club plan §9).
10. An affiliate's statement of subject *legislation* or *candidate* is refused with D65 and the IRS page named; nothing on AFRP's own statements is refused on content.
11. Resolutions of the General Assembly, letters to officials, Magazine articles and programme invitations are not statements and keep their own objects (voting; P3; slice 7; `communications`).
12. Every refusal names its rule.

---

## 8. What this note raises

| Q | Question | Owner |
|---|---|---|
| Q-80 | Who approves the text of a Federation public statement or letter to an official before the President signs it: the President alone, the Executive Committee, the Executive Director under 7.9.3, the Government Affairs Committee for advocacy; whether the Legal Advisor's review is required for statements on legislation; and whether the approval is minuted | AFRP Board · President · Legal Advisor |
| Q-70 | The consent basis for the media list (whether a published press contact may be sent an unsolicited release), and the inactivity parameter after which a contact is withheld — one question across notes, Q-70: the non-member contact record and its retention (P4, P6, P12, P14, P15, P17) | Legal Advisor · Executive Director |
| Q-81 | Whether the Federation has a positions policy (the "does not take formal positions on final political outcomes" sentence against statements urging a vote on named bills), and the 501(c)(4) consequences of lobbying for a membership organisation — the dues-notice or proxy-tax question — which the CPA and the Legal Advisor answer together with D65's confirmation, and what the lobbying record must hold for them to answer it (Q-134) | Legal Advisor · CPA · AFRP Board |
| Q-82 | Whether the Media and PR committee is to be constituted on the register (8.1.1), with whom as chair, and whether the communications-manager role of the 2020 deck exists as a seat or as the Executive Director's duty under 7.9.3 | President · Executive Director |

Carried, not new: P7 (volunteer interests, which fills the spokesperson pool); slice 5 (real email); Q-38 → D65's Legal Advisor confirmation.

---

## 9. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| PR1 The statement register and the media list | The *public* class on the template register with the fields of §2 and the states; the approver seat as a parameter row with no value, refusing issue while empty; the entity fixed to AFRP with the affiliate's-own-Board path; the General Fund posting of any cost and the D65 refusal; the 24-hour follow-up; the media contact on the institution registry with consent, locality and area tags; the yearly review follow-up; the drive link as the text of record; the correction as a new linked row; the spokesperson seat on CW1 typed by the office; the club's own statements on the club lens with counts to the Federation; the *subject* field (programme, legislation, candidate) and the affiliate refusal of §6 | §2–§6 | CW1 for the seats; slice 5 for a real send (drafting, approval and the archive row work without it); issue itself gated on Q-80 |
| PR2 Inquiry routing | A media inquiry as a reactive trigger routed to the spokesperson seats and the Executive Director, opening a statement row with the clock | §4 | PR1; VI4 for the pool |

---

## 10. Journeys proposed

| Journey | Tests | Class | Slice |
|---|---|---|---|
| P6-J01 A reactive statement opens from a trigger with a 24-hour follow-up on the drafter's and approver's seats and cannot be issued while the approver seat has no value | §2; 7.9.3; Q-80 | guarded until Q-80 (drafting and holding meet) | PR1 |
| P6-J02 A statement about the Medical Mission is issued under AFRP and its distribution cost refuses an ARFHSN line by D65's name | D65, D9 | meets | PR1 |
| P6-J03 ARFHSN's Board issues its own programme statement on its lens; an ARFHSN statement of subject *legislation* is refused with D65 and the IRS page named | D65; §6 | meets | PR1 |
| P6-J04 A media contact with no consent row is withheld by name from the audience; no member appears in a media audience; the list is not exportable | R27; D60's shape; `communications` | meets | PR1 |
| P6-J05 An issued statement cannot be edited; a correction is a new row linked to it, and the drive link is the text of record | R27's pattern; D66 | meets | PR1 |
| P6-J06 A club officer issues a statement under the club's name to the club's own contacts and cannot issue one in the Federation's name; the Federation sees a count | §5; S7 | meets | PR1 |
| P6-J07 An inquiry routes to the spokesperson seats and the Executive Director and opens a row with the clock | 7.9.3; §4 | guarded until P7 (the seat typed by the office until then) | PR2 |

---

## 11. What changes in the site's data with this note

`workflows.yaml`: a new workflow `press-statements` with §2's steps (trigger, draft, approve, issue, archive, correct) and actors by seat, hands_to `communications`, `funds` (the General Fund posting) and `reporting`, sources this note and 7.9.3, rule_vs_practice "signed by the President; no approval rule written" and "a press release per Convention, a 24-hour clock in no adopted text". `experiences.yaml`: the Executive Director's and the Government Affairs chair's lens rows name the statement register; the club-officer lens names the club's own statements. `questions.yaml`: Q-70 and Q-80–Q-82 numbered. The crosswalk: E6 "Proposed" → "Designed", citing this note; E7 stays on P7 with the spokesperson seat noted; the P6 row → "Written". `plan/MASTER-PLAN.md` §2: rows PR1–PR2. The Delivery Status's "exhibitor and press credentials" item is untouched (that is Convention credentialing, not this note).

---

## Sources

- American Federation of Ramallah, Palestine, *Constitution and By-Laws*, approved 13 July 2024 (`design/bylaws/`): 6.7.1, 7.2.1, 7.9.3, 8.1.1, 9.5.2, 11.1.1.
- `design/AFRP-Decisions-Register.md`: D9, D50, D55, D60, D65, D66.
- `design/AFRP-Letters-and-Onboarding.md` §2 (the template register); `design/AFRP-Club-Experience-Plan.md` §6.1, §9; `design/AFRP-Four-Lens-Architecture.md` §9; `design/AFRP-Committee-Workspace.md` §2.
- The Federation's PR working papers (crosswalk "PR", the Strategic Planning folder): Media and Public Relations Committee business plan (May 2018); press-release proposal (2020–21); communications-management deck; communications-intern description. Proposals; adoption not evidenced.
- The intakes (D54), role level: Government Affairs letters and statements; the convention folders; ARFHSN Letters & Statements; the endowment campaign's spokesperson talking points (August 2025).
- IRS, *Social welfare organizations* — https://www.irs.gov/charities-non-profits/other-non-profits/social-welfare-organizations (read 1 October 2026).
- IRS, *The restriction of political campaign intervention by section 501(c)(3) tax-exempt organizations* — https://www.irs.gov/charities-non-profits/charitable-organizations/the-restriction-of-political-campaign-intervention-by-section-501c3-tax-exempt-organizations (read 1 October 2026).
- IRS, *Lobbying* — https://www.irs.gov/charities-non-profits/lobbying (read 1 October 2026).
- Not confirmed: ARFECF's exempt status (no determination letter on file, D2); whether the 2011 IRS letter describing AFRP as a 501(c)(4) is current.
