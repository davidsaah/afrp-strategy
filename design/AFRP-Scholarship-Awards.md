# Scholarship awards and renewal

### From the committee's decision to the last instalment: the award year, the semester filing, the release, the hold, the letters and the cheques, the named scholarships as fund rows, the committee's seats, and the money beside the Scholarship Fund

**Design note P26 · 2 October 2026 · for the Hub's `scholarship`, `funds`, `ledger`, `comms` (P3's register), `committees` (CW1) and `alumni` modules**

*Since 4 October 2026 (D99):* the shared shapes this note draws — the scoped parameter (instalments), the verifying seat, the cycle with a never-held document policy, verification as a record on file and the filing-window clock — are built once as the platform primitives of `AFRP-Platform-Primitives.md` (P29 §3, §4, §6, §9, §11); this note's rules are carried as their settings.

**What this note rests on.** `AFRP-Scholarship-Program-Spec.md` (Addendum 7, 15 August 2026: the lifecycle, the committee engine, encumbrance, the verification gates, named-scholarship matching), which Hub slices 4 and 4b built in part; the ARFECF By-Laws 6.4.1–6.4.8 and the Scholarship Fund Policy Statement (revised 2015, `bylaws/ARFECF-2015-and-the-fund-policies.md`); D2, D3, D7–D10, D55, D58, D61 and the register's conflicts section of 2 October 2026; P9 (`AFRP-Fund-Rules.md`, the fund object and its rows); P3 (`AFRP-Letters-and-Onboarding.md`, the letter register); P5 (`AFRP-Selection-Committee-Workflow.md`, the three elected seats); P12 (`AFRP-Selection-Programmes.md`, the engine the Scholarship does **not** run on); and the research round of 2 October 2026 (the Education report in full, with the Care report's Women to Women section). The workflow `scholarship-renewal` (added 2 October) is the practice this note designs for.

**Precedence (D41).** The ARFECF by-laws and the 2015 policy first; then the Decisions Register and the named design documents (the spec, P3, P9); then the prototype (`#/program/applications`, a story); then the Hub's `scholarship` and `funds` code (what is). The research round is evidence of practice. Where the spec and a later decision disagree, the decision wins and this note says where (§1.4). Where practice and the record disagree this note builds the record and carries the conflict as a question. Where the record is silent it says so.

**Public-repo rule.** No scholar, applicant, donor or named scholarship is named; no amount, GPA figure or count of units appears; the office's list is described, not reproduced.

---

## 1. What the record already holds

### 1.1 The texts

- **The fund's purposes** include "to select and award scholarships for the education and training of students who give evidence of promise of high achievement and who have need of such aid" (ARFECF 6.4.1).
- **Spending** is limited to 5% a year (6.4.3), and **"the only body that can authorize annual expenditures from the Scholarship Fund ... is the Scholarship Fund Committee"** (6.4.4). Non-earmarked money in the fund is never diverted to another fund or purpose (6.4.8). Amendments to the committee's policies, rules and regulations need two-thirds of the ARFECF Board's voting members (6.4.6). The committee reports in full at the Convention (6.4.7).
- **The 2015 policy**: a mandatory 4% distribution to scholarships and educational causes plus 1% to AFRP for administration, on the 31 May valuation; the committee approves and distributes the annual expenditure; a committee of at least nine — a chairman chosen by the ARFECF President, the executive director, at-large members chosen by the ARFECF Board, and since 2015 three members elected at the Annual Convention; two three-year terms then a year off; employees do not vote; **published application guidelines (not found anywhere)**; and **"follow-up to confirm students keep the required academic standing"**; thank-you letters to donors within 48 hours with the tax-deductibility statement. It names no seat for the Ramallah Foundation.
- **The AFRP by-laws** give the members' franchise for "members of the Scholarship Committee" (5.3; 8.12.5) and constitute no Scholarship Committee (Q-11).

### 1.2 Decided

D3 (the Scholarship's legal home is ARFECF; award receipts and exempt status are ARFECF's). D2 (the Endowment in ARFECF; never mixed with the Scholarship Fund, 6.3.8/6.4.8). D7's ARFECF exception (a surplus stays in the fund it was given to). D8 (a new purpose goes to the entity's Board and blocks publication). D9 (the receiving entity receipts). D10 (four contributor moments, then an annual statement). D55 (the Scholarship is ARFECF's in the 2026–27 budget). D58 (Foundation seats exist only once the ARFECF Board amends the 2015 policy; until then the committee is seated as the policy reads). D61 (past recipients only, as alumni records through the match queue; applicant data and documents never enter — the Hub's binding rule 2).

### 1.3 Built (`AFRP-Delivery-Status.md`, slices 4, 4b, 9)

The committee engine: an application's existence, state, scores and an opaque reference to the committee's packet, never the packet; conflicts **disclosed by degree** over the tree and acknowledged on the record, only the same household refusing (4b replaced the spec's three-degree bar); the median with the spread surfaced; the award budget **entered by the committee** from its report with a source and an as-of date, never computed; encumbrance in whole cents; the Fund boundaries refusing by name (no designated officer for the committee, 6.4.4; never between the Funds, 6.3.8/6.4.8; D7 cannot reach ARFECF; receipts ARFECF's). The alumni match queue resolves a historical recipient to a person, links nothing by itself and contacts no one who asked not to be contacted (slice 9). The `scholarship-renewal` workflow's status note says the engine verifies enrolment before disbursement; **the instalment release, the semester filing, the letters, the document chase and named-scholarship assignment are not built.** The master plan's slice-4 row lists "named awards"; the Delivery Status entry for slice 4 does not say they were built, so this note treats them as not built.

### 1.4 Where the spec has been overtaken

| Spec (15 August 2026) | Since | What stands |
|---|---|---|
| §1, §5: "AFRP is the payer of record" | D3 (20 August): the Scholarship is ARFECF's | ARFECF is the payer; the spec's tax-fact capture applies to ARFECF |
| §3: related within three degrees is blocked | David's correction (8 September; built in slice 4b); **D84** (4 Oct 2026), pending the Scholarship Fund Committee's adoption | Disclosed by degree and acknowledged; only same household refuses |
| §2 lifecycle: "budget check → board approval → offer" | 6.4.4 (text) | The committee's decision authorises; a Board's act, if any, is recorded beside it and gates nothing (§3.3; Q-161) |
| §5.1: verification "every year" | The 2026 award letter (practice): per semester | §2 builds the semester as the unit, graded practice (Q-159) |

### 1.5 Practice (the research round, role level)

The 2026 cycle: a revised online form; the office compiles the continuing cohort; the committee secretary filters responses into one review sheet; the committee reads in advance and decides **by consensus** at one meeting in mid-July; the secretary reports the recommendations to the Board and the incoming President in late August; the programme director verifies each selected applicant's documents and lists the gaps; the office asks whether to chase or hold the cheque; award, missing-documents and rejection letters go out in early September **in AFRP's name over the President's and the committee secretary's signatures**; **the Executive Administrator writes the cheques**; counts and amounts by track are announced, never names. The award letter sets **renewal**: a fixed annual amount in **two instalments, after the fall and winter semesters**, each released only once the office has verified the semester transcript, proof of full-time enrolment with the next semester's schedule, and a cumulative GPA at the published minimum; failure to file, dropping below full time or below the minimum "may result in suspension" and delay or cancellation of the next payment; a scholar whose circumstances change is told to contact the office. **A late application is treated as disqualifying** (June 2026): an applicant not on the review sheet is treated as late or absent. **The committee counts its Foundation representatives as votes** (June 2026). **About twenty named scholarships** sit on an office list reconstructed from the Educational Secretary's reports of the 1990s, two added from a member's memory, none with an instrument, criteria or assignment rule on file; the committee has made their reconciliation the year's priority. **Women to Women** (an ARFHSN sub-fund, D55) now "finalises ... student scholarship evaluations" at its September meeting and has paid college tuition. **The Cook Book fund**, a separate ARFECF chequebook reported at every Board meeting, transferred money in 2025–26 to the Education Fund for the Federation's accounting and CRM systems.

---

## 2. The award year, as objects

The spec's `award` and `award year` objects stand (spec §9's schema, slice 4). This note adds what sits between an award year and money leaving: **the instalment**, its **verification**, its **release**, its **hold**, and the **disbursement** record.

### 2.1 The instalment

*Since 4 October 2026 (D99 review), marked unoperated in the manner of P23 §9.7:* two tracks in the table below have no source at all: the **Ramallah track** (Q-255) and the **medical track with quarter or trimester calendars** (Q-256). Their instalment schedules are **designed; not built until Q-255 and Q-256 are answered**; until then the closing paragraph of this section already has the console show the track unscheduled with its question number. Nothing is deleted.

An award year carries one or more **instalments**, each with: its sequence; the **trigger** (the academic term whose end makes it due); its share of the award year; its state — *scheduled*, *due* (the trigger term has ended), *verified*, *released*, *held*, *suspended* (only by the committee's act, §2.4), *cancelled* (only by the committee's act); and its verification rows.

**The schedule is a register row, not code.** The rows the record holds today are practice, graded so:

| Parameter | Value in the record | Source | Grade |
|---|---|---|---|
| Instalments per award year | Two | The 2026 award letter | practice (Q-159) |
| Trigger terms | After the fall semester; after the winter semester | The 2026 award letter | practice (Q-159) |
| The first instalment | With the award letter, unless the missing-documents letter holds it until the application's gaps close | The 2026 award and missing-documents letters | practice |
| Full time | Not defined in any source; the institution's own definition, attested by the scholar's proof | — | **silent** |
| Minimum cumulative GPA for renewal | "The published minimum"; the register holds the eligibility minimum the programme publishes | The 2026 award letter; the programme's published eligibility | practice (Q-159) |
| Medical track and quarter or trimester calendars | Not stated | — | **silent** (Q-256) |
| Ramallah track | Not stated: the letters read are the US undergraduate track's | — | **silent** (Q-255) |

Until the committee adopts a renewal rule (Q-159) — which, as an amendment to the committee's rules, needs two-thirds of the ARFECF Board (6.4.6) — every row above shows its grade on the scholar's page and the office's console, and **the platform enforces only what the text and the built engine already enforce**: nothing is released before verification (spec §5.1, built as "verifies enrolment before disbursement"); nothing is suspended or cancelled by the platform (§2.4). Where a parameter is silent for a track, that track's instalments are not scheduled and the console says so with the question number; nothing is guessed.

### 2.2 The semester filing and its verification

After each trigger term the scholar files three things **with the office, outside the platform**: the semester transcript, proof of full-time enrolment with the next term's schedule, and the cumulative GPA. **No document enters the platform** (binding rule 2 and D61 for applicants; *design choice by the same principle* for a continuing scholar's documents, which are the same kind of record about the same person). The platform holds, per instalment, three **verification rows**: *transcript on file*, *full-time enrolment on file*, *cumulative GPA at or above the minimum* — each a dated act by the verifying seat (the office's seat on P16's office map; practice: the Executive Administrator, with the programme director for the first instalment's documents), with no content, no grade figure and no document. A verification row that says *below the minimum* is a fact for the committee, not a decision (§2.4).

**The scholar's view.** On the scholar's own page (the `scholar` lens): each instalment's state; what is still missing for the next one; the date the office received each item; and the hardship route (§2.4). Nobody else sees an instalment except the office's seat, the committee's seats and the fund's treasurer (scope R39: nothing in the AFRP or ARFHSN scope).

### 2.3 The release and the disbursement

**Authority.** The committee's decision on the year's awards is the authorising act for the year's expenditure (6.4.4; 2015 policy: "the committee approves and distributes"). Releasing an instalment under that decision, once its three rows are verified, is the office's administrative act and records the verifying seat and date. *Design choice*: the committee does not re-vote each instalment; the release is the decision executed, and a held or suspended instalment returns to the committee (§2.4).

**The disbursement row**: the instalment; the payee (the scholar; spec §1's "paid to the student after enrolment proof"); the method (*cheque by post* in practice on the US track); the date; the **fund** (ARFECF's Scholarship Fund, read from the award; D3) and the **bank account drawn on**, named by the office from the account register; the seat that wrote it. **A disbursement whose account belongs to an entity other than the fund's holding entity does not post**, naming D3, 6.4.8 and Q-158; whether AFRP's office may pay from an AFRP account as ARFECF's agent and settle afterwards is the agency question the register already holds for every affiliate purpose (Q-232) and is not answered here. The posting runs through the ledger's existing release of encumbrance (slice 4) and the multi-entity books; the 1% administration line is P9's (§3.4 there), not this note's.

**Tax facts.** The spec's §5.2 stands with ARFECF as the payer: tax status is collected before the first payment, a flagged case cannot be paid until the adviser's clearance row exists, and the platform computes no tax. Who the adviser is remains the spec's §11 q1 and the register entry's open question.

### 2.4 The hold, the hardship route and suspension

- **A missed filing holds; it never lapses.** An instalment that is *due* with a verification row missing becomes *held* on the date the committee's filing window closes (a parameter with no value until set; the 2026 letter states none for later instalments). Held means **not released and still encumbered** (spec §4: an encumbrance is released only when a year is forfeited, which is a committee act). Both the register's "renewal is not lapsed by silence" and the letter's "may result in suspension" are honoured: the platform holds and tells; only the committee decides more.
- **The hardship route.** The letter tells the scholar to contact the office. On the scholar's page this is a **request to the office**: a dated row with a category the committee defines (illness, bereavement, a term's leave, a change of institution, other) and **no free text about the person's circumstances**; the account the scholar gives goes to the office by its own channel and stays outside the platform (Breeze Parity §4 r2's rule for follow-ups, applied). The row opens a follow-up to the office's seat and a decision item on the committee's queue. What the hardship exception is, is **Q-159**.
- **Suspension and cancellation** are decision items of the committee (6.4.4), each with the seats present and the instalments it touches; suspension keeps the encumbrance, cancellation releases it (spec §4). The scholar is told by a letter row (§4). The platform never moves an award to *suspended* or *cancelled* on a date, a GPA row or a missing filing.
- **What a held instalment becomes at the year's end** — carried into the next award year, paid late, or forfeited — is not written anywhere (**Q-256**). Until answered it stays *held* and encumbered, and the committee's annual report shows it as such.

---

## 3. From the committee's decision to the award

### 3.1 The committee's seats — "Foundation members still vote"

The committee is a body on CW1 seated as the 2015 policy reads (D58): the chairman with the ARFECF President's dated act; the executive director (non-voting is not stated for this seat; the policy's "employees do not vote" is read on the seat's vote property and shown with its source); at-large members with the ARFECF Board's act; three members with a Convention election result (P5 §3.1: the AFRP cycle carries the vacancy and the election). The three-year terms, the year off and the chairman's two-year cap are 6.4.5 and the policy, as the seat refusals P1 already builds.

**A Foundation representative.** A person the Ramallah Foundation sends may hold a seat **only under one of the policy's authorities** — the ARFECF President's chairman seat, an at-large seat chosen by the ARFECF Board, or a Convention-elected seat — and the seat then shows that authority, not "Foundation". **A seat of kind "Foundation representative" is refused**, naming D58 and the 2015 policy, until the ARFECF Board's amending act (two-thirds, 6.4.6) is recorded on the register; the act then creates the kind. A vote, or a share in a consensus, is recorded only for seats present (P1's decision item); a person at the meeting without a seat appears as an attendee and in no tally. *This builds D58 as written; the 2026 practice of three Foundation votes is the register's conflict row and Q-29's conditional answer.*

### 3.2 The decision

A **decision item** on the committee's queue (P1 §3.4) per cycle and track: the seats present; the outcome *consensus* or a tally (the 2026 practice is consensus at one meeting); the disclosed relationships acknowledged (P26 §1.4, built in slice 4b; D84, pending the committee's adoption); the awards made, each creating the award and its award years with the encumbrance (slice 4); scores only under an adopted rubric (the spec's §11 q2; built as refused without one). The decision freezes the cycle's application list.

**Late or absent applications.** Each application carries its received date against the cycle's deadline (31 May, the programme's published calendar). One received after it, or never received, is shown as such. **The platform refuses nothing on lateness**; the committee's practice (treating a late application as disqualifying) is recorded as the committee's dated act on that application, and becomes a rule the platform applies only once the committee adopts a late-application rule as a register row (Q-117 asks every programme committee for one; for the Scholarship the adoption is a rules amendment under 6.4.6). A member who forwards a relative's appeal is answered outside the platform; whether a declined or suspended person has an appeal route at all is **Q-257**.

### 3.3 The report to the Board

The secretary's report to the Board and the President becomes the committee's report generated from the decision (P1 §4.1, CW3): counts by track, new against continuing, the year's commitment against the committee's entered budget and the headroom, the forward commitments (spec §4), the named-scholarship status (§5). **No AFRP Board act gates any award.** Whether the AFRP Board "approves" the year's awards (the 2023 community report's word) or receives the committee's decision (6.4.4) is Q-161; until answered the platform records any Board act on the report as a dated row headed "Board's act on the committee's report (Q-161)" and the release of the first instalment does not read it. *The text governs (6.4.4).*

### 3.4 What else the record asks and this note carries

The lineage test and "committee sponsorship approved by the Board" (Q-160); the public page's "managed by the Ramallah Foundation" (Q-162); the free student membership on award (spec §7.1; the register entry's age-or-enrolment question; dues authority is the Board's under 5.1); the application guidelines the 2015 policy says are published (not on file; the call cannot cite them).

---

## 4. Letters and cheques, on P3's register

Every scholarship letter is an **LT-P row** on P3's register with its class, trigger, signatory seat, wording status, the fields it reads, its consent and **its entity**. This note fills the rows P3 lists as "each programme's design note":

| Row | Letter | Class | Trigger | Reads |
|---|---|---|---|---|
| LT-P-SA1 | Award | operational | The committee's decision creates an award | The award year, the instalment schedule and its grades, the filing duties, the hardship route |
| LT-P-SA2 | Missing documents | operational | The first instalment is held on an application gap | Which on-file flags are missing; the date |
| LT-P-SA3 | Not awarded | operational | The decision freezes the list without an award | Nothing beyond the fact (no score, no rank) |
| LT-P-SA4 | Semester filing reminder | operational | A trigger term ends | What to file for the next instalment |
| LT-P-SA5 | Instalment released | operational | A release (§2.3) | The instalment and its date; no account detail |
| LT-P-SA6 | Instalment held | operational | An instalment becomes held | What is missing; the hardship route |
| LT-P-SA7 | Suspension or cancellation | operational | The committee's decision item | The decision and its date; the appeal route if Q-257 creates one |

**Entity.** P3 sends each letter under its holding entity (D9, D55, D56); for the Scholarship that is **ARFECF** (D3). The 2026 letters went out in AFRP's name over the AFRP President's and the committee secretary's signatures. That is the register's conflict row; the ARFECF Board decides under **Q-158**. Until it does, each row's entity reads ARFECF from the programme register, and **its signatory seat is a register row with no value** — the practice signatories are shown beside it as "practice (2026)". **A row with no signatory, or with wording *open*, produces a draft the office sees and nothing else** (P3 §2, rule 10). So no scholarship letter is sent from the platform until the ARFECF Board answers Q-158 and the wording is adopted and linked on the drive (D66). *This is P3's existing behaviour, not a new gate.*

**Cheques.** The office writes them (the Executive Administrator's seat on the office map, P16 §5); the platform records the disbursement row (§2.3) and prints nothing. The disbursement refuses an account of another entity (§2.3). A returned or uncashed cheque is a reversal row (R24), never an edit.

**Announcements.** Counts and amounts by track, never names (committee practice, August 2026; spec §7.2: Magazine publication only with the scholar's own *magazine_publish* and *photo_publish* consents, both default false).

---

## 5. Named scholarships, as P9's fund rows

**What P9 holds.** A named scholarship is a **sub-fund inside the Scholarship Fund**: its own restriction, its own instrument cited, its own balance and income, reported on the parent's report (P9 §6.2); the fund register refuses any posting to a fund whose holding entity, governing text or kind is unset (P9 §2). The 2018 proposal (a perpetual fund at a minimum, or a one-year sponsorship; donor criteria accepted by the committee; a yearly donor list) is on file as a proposal, not adopted; the published minimum gift and term are figures the record does not adopt (P9 §6.2). Matching scholars to named awards, most-constrained first, with every unfilled award reported with its reason, is the spec's §6.

**What the office's list becomes.** Each name on the office's list enters the fund register as a **candidate row**: the name as the list gives it; the source (the Educational Secretary's reports of the 1990s; the office's list of July 2026; "added from memory" where so); status *instrument not found*; kind, criteria and balance **unset**. A candidate row:

- **receives no posting** (P9 §2's refusal: kind and governing text unset);
- **is not offered to the matcher** and cannot be assigned to an award (spec §6 needs criteria; Q-102);
- shows on the committee's reconciliation page and nowhere public.

**Reconciliation**, the committee's priority for the year, is a set of decision items, one per candidate row, each concluding with a dated act: *instrument found* (the instrument linked on the drive, D66; the row becomes a sub-fund with its kind, criteria and the instrument's terms, and its balance is established by the treasurer's entry with its source); *donor or family confirms terms in writing* (the same, the writing being the instrument); *no instrument and no balance* (the row stays a name, closed, with the history kept); or *referred* (to the ARFECF Board, the CPA or the Legal Advisor). What a name with no instrument may be used for — recognition on a general-fund award, or nothing — is part of Q-102 and the platform offers neither until it is answered.

**A new named scholarship** is a new purpose in ARFECF's name, which goes to the ARFECF Board and blocks publication until approved (D8); a gift to it is a restricted gift receipted by ARFECF (D9), with the surplus and shortfall disclosure on the page (D7's ARFECF exception: a surplus stays in the fund). The donor sees which award carries the name **by count**, never the scholar, unless the scholar gives *donor_may_know* (spec §7.2).

---

## 6. Beside the Scholarship Fund

### 6.1 Women to Women's tuition awards

Women to Women is an ARFHSN sub-fund (D55); its money leaves under D63 (the holding entity's Board approves with a ceiling). Since 2026 its committee "finalises ... student scholarship evaluations" at its September meeting and has paid college tuition for students in Ramallah. **It is not the Scholarship and the platform does not make it one.** Under R39 the AFRP and ARFECF scopes do not read ARFHSN's store, so the Scholarship Committee cannot see who Women to Women funds, and no "already funded elsewhere" check across the two exists or is built. What Women to Women holds about applicants, whether its awards are a selection programme under D61's principle, and whether the two overlap, is **Q-211**; until answered nothing about a Women to Women applicant enters the platform, and a Women to Women tuition payment is a Care grant row on P11's register with its Board approval (D63; Q-114 for the committee-approval practice). The Women to Women sponsorship of Arabic-class fees across entities is Q-168 and is not this note's.

### 6.2 The Cook Book fund

The Cook Book fund is P9's row "Cook Book fund — ARFECF (a 2017 treasurer's report) — historic sales fund — governing text none". The research round shows it **exists**, is reported at every Board meeting by the Educational Fund Treasurer beside the Education Fund and the Relief Fund, takes book sales and interest, and in 2025–26 **transferred money to the Education Fund (ARFECF's operating account) for the Federation's accounting and CRM systems**. No source shows it paying scholarships or any education programme directly; its "education spending" is that transfer.

On the platform: the row's status becomes "exists; reported per Board meeting" with the research round as its source; its kind and governing text stay unset, so **no posting is made to it or from it, and a transfer out refuses naming Q-173** (which entity's books carry it, what it may pay for, who authorises a transfer out). The transfer of 2025–26 is history on the drive (D66), not a ledger row. **It never reaches the Scholarship Fund**: a posting from the Cook Book fund to the Scholarship Fund, if a Board ever wants one, is a new restricted gift from one fund to another and needs an authoriser on both sides; none is stated. The three per-meeting chequebook reports and whether the platform produces them are **Q-174**.

---

## 7. Rules

1. Only the Scholarship Fund Committee authorises the fund's annual expenditure; no designated officer and no AFRP Board act stands in for it (ARFECF 6.4.4; built).
2. The committee is seated as the 2015 policy reads; a seat of kind "Foundation representative" is refused until the ARFECF Board's amending act is recorded (D58; 6.4.6).
3. Only seats present are in a decision's tally or consensus (P1 §3.4).
4. No instalment is released before its three verification rows are recorded (spec §5.1; built for enrolment).
5. No document of an applicant or a scholar enters the platform; verification rows hold no content and no figure (binding rule 2; D61; *design choice* for scholars).
6. The platform never suspends, cancels or lapses an award; a missed filing holds the instalment and keeps its encumbrance (the register's "not lapsed by silence"; spec §4; *design choice*).
7. Suspension and cancellation are committee decision items; cancellation releases the encumbrance (6.4.4; spec §4).
8. Every renewal parameter is a register row with its source and grade; a silent parameter leaves that track unscheduled (R40).
9. A disbursement posts only to the award's fund and from an account of the fund's holding entity (D3; 6.4.8).
10. Every scholarship letter is an LT-P row under ARFECF's name; with no signatory or with wording open it is a draft only (P3; D3; D9).
11. A name on the office's list is a candidate row: no posting, no assignment, until an instrument is recorded (P9 §2, §6.2; Q-102).
12. A new named purpose goes to the ARFECF Board before it can be published (D8); gifts to it are ARFECF's receipts (D9); a surplus stays in the fund (D7).
13. Lateness is shown and refuses nothing until the committee adopts a late-application rule (Q-117; 6.4.6).
14. Recipients are never named in any public or member surface; counts and amounts by track are (practice; spec §7.2).
15. Nothing of ARFHSN's store is read by the scholarship (R39); the Cook Book fund posts nothing until Q-173 is answered.
16. Every refusal names its rule and, where one holds it open, its question.

---

## 8. What this note raises

Carried, not re-asked: Q-2 (the determination letter), Q-11, Q-29, Q-35, Q-76, Q-102, Q-114, Q-117, Q-158, Q-159, Q-160, Q-161, Q-162, Q-168, Q-173, Q-174, Q-211, Q-232; the spec's §11 q1 (the tax adviser), q2 (the rubric), q7 (the free student membership's limit).

| Q | Question | Owner |
|---|---|---|
| Q-255 | The Ramallah track: how its awards are paid (channel, currency, payee, who verifies the semester documents in Ramallah), whether its renewal follows the US letter's two instalments, and in whose name its letters go. No source read states any of it. | Scholarship Fund Committee · ARFECF Board · CPA |
| Q-256 | Renewal parameters the letter does not reach: the filing window after each term; what "full time" means; how a medical-track or quarter-calendar scholar's instalments fall; and what a held instalment becomes at the year's end (carried, paid late, or forfeited, and who decides). | Scholarship Fund Committee · ARFECF Board |
| Q-257 | An appeal route: may a person declined for lateness, or a scholar suspended or cancelled, ask the committee to reconsider; to whom, by when, and is the answer recorded as a new decision naming the first? | Scholarship Fund Committee · Legal Advisor |

---

## 9. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| SA1 Instalments and verification | The instalment object on the award year with its states; the schedule as register rows with source and grade (silent tracks unscheduled, naming Q-255, Q-256); the three verification rows as dated acts with no content; the release as the office's act under the committee's decision; the scholar's page; the office's console of due, verified and held instalments | §2.1–§2.3 | Slice 4's award years; P16 office map for the verifying seat (an office register row until then) |
| SA2 Hold, hardship and committee acts | The *held* state with the encumbrance kept; the hardship request with a category and no free text, opening a follow-up and a decision item; suspension and cancellation as committee decision items with encumbrance effects; the year-end held list on the committee's report | §2.4 | SA1; CW2 for the decision queue (a committee register row until then); Q-256 for the window (held is computed only once set) |
| SA3 Disbursement and accounts | The disbursement row with method, fund, account and seat; the refusal of another entity's account naming D3, 6.4.8, Q-158; reversals as new rows; the tax-status and adviser-clearance gates of spec §5 against ARFECF | §2.3 | FR1 (the fund register); slice 5 for live payments; Q-158 for which account |
| SA4 The committee's seats and decision | CW1 seats as the 2015 policy reads with the Foundation-kind refusal; the decision item with seats present, consensus or tally, disclosures acknowledged; the received-date-against-deadline display; the Board's act recorded beside the report and read by nothing | §3 | CW1, CW2, CW3; D58's amending act lifts the refusal; Q-117 for a late rule; Q-161 for the Board row's heading |
| SA5 Letters | LT-P-SA1 to SA7 on P3's register under ARFECF, signatory rows with no value, drafts only until Q-158 and adopted wording | §4 | LT1 (P3); **Q-158** to send |
| SA6 Named scholarships | Candidate rows from the office's list with source and status; the reconciliation decision items and their four outcomes; a confirmed row becoming a P9 sub-fund with its instrument; matching (spec §6) reading only sub-funds with criteria; the donor's count view | §5 | FR1, FR4 (P9); **Q-102** for assignment and any use of a name without an instrument |
| SA7 The neighbours | The Cook Book fund's status line and its transfer refusal naming Q-173; no read of ARFHSN's store; Women to Women tuition as a P11 grant row only | §6 | FR1; CG1 (P11); Q-173, Q-211 |

Order: SA1 → SA2 → SA3; SA4 with CW1–CW3; SA5 after LT1; SA6 after FR1 and FR4; SA7 with FR1.

---

## 10. Journeys proposed

| Journey | What it tests | Class |
|---|---|---|
| P26-J01 | A scholar's second instalment shows *due* after the fall term with two of three verification rows recorded; release is refused naming the missing row; the third row is recorded and the office releases it | meets once SA1 lands |
| P26-J02 | No transcript, schedule or GPA figure can be attached to a verification row or an instalment; the refusal names binding rule 2 and D61 | meets |
| P26-J03 | The filing window passes with a row missing: the instalment becomes *held*, the encumbrance stays, the scholar's page shows what is missing and the hardship route; nothing becomes *suspended* | guarded until Q-256 sets the window |
| P26-J04 | A hardship request takes a category and refuses free text; it opens a follow-up to the office and a decision item for the committee | meets once SA2 lands |
| P26-J05 | The committee suspends an award by a decision item with seats present; the instalments touched become *suspended*; the encumbrance stays; LT-P-SA7 drafts | guarded until CW2 |
| P26-J06 | A disbursement drawing on an AFRP account for an ARFECF award is refused naming D3, 6.4.8 and Q-158 | meets once SA3 lands |
| P26-J07 | The office tries to seat a member as "Foundation representative" and is refused naming D58; the same person seated as an at-large member by the ARFECF Board's act appears in the tally | guarded until CW1 |
| P26-J08 | A person present at the decision meeting without a seat is an attendee and in no tally or consensus | guarded until CW2 |
| P26-J09 | An application received after 31 May shows "received after the deadline"; nothing is refused; the committee's act not to consider it is recorded on the application | meets once SA4 lands |
| P26-J10 | An AFRP Board act recorded on the committee's report is shown under its Q-161 heading, and the first instalment's release does not read it | guarded until CW3 |
| P26-J11 | An award letter row with no signatory produces a draft the office sees; it cannot be sent; the entity line reads ARFECF | meets once SA5 lands |
| P26-J12 | A candidate row from the office's list refuses a posting and cannot be offered to the matcher; on an *instrument found* act with the drive link it becomes a sub-fund and the matcher reads its criteria | guarded until FR1 and FR4 |
| P26-J13 | A donor of a named scholarship sees "carried by one award this year" and no name, unless the scholar's *donor_may_know* consent exists | guarded until SA6 |
| P26-J14 | A transfer out of the Cook Book fund refuses naming Q-173; the Scholarship Committee's console shows nothing of Women to Women | meets once SA7 lands |

---

## 11. What changes in the site's data with this note

`programmes.yaml`: the `scholarship` entry's `rungs.take_part` cites §2.4 (held, not lapsed; suspension only by the committee), `money` cites §2.3 and §6.2, `organiser` cites §3.1 for the Foundation seats, `questions` gains Q-255 to Q-257, `platform_needs` names slices SA1–SA7. `workflows.yaml`: `scholarship-renewal` gains the instalment states, the verification rows, the hold and the committee's acts as steps and this note as a source; its `status_note` drops "not designed" for the release and the letters; `giving-funds` cites §5 for named scholarships. `experiences.yaml`: the `scholar` lens cites §2.2 for the scholar's page and the `donor` lens §5 for the count view; the lenses carry P26-J01 and P26-J06. `questions.yaml`: Q-255 to Q-257 numbered by governance; Q-159's detail cites 6.4.6 for adoption. The crosswalk: row F9 cites this note, and a P26 row joins the design-notes table. `plan/MASTER-PLAN.md`: rows SA1–SA7. `AFRP-Scholarship-Program-Spec.md` should carry a one-line pointer to §1.4 of this note for the points D3 and slice 4b overtook (the owning agent decides).

---

## Sources

**Record.** ARFECF By-Laws 6.3.8, 6.4.1–6.4.8 (`design/bylaws/ARFECF-Bylaws-2013.pdf`; the 2015 revision as extracted in `design/bylaws/ARFECF-2015-and-the-fund-policies.md`); the Scholarship Fund Policy Statement (2015), as extracted there; AFRP By-Laws 2024, 5.1, 5.3, 8.12.5; `AFRP-Decisions-Register.md` (D2, D3, D7–D10, D55, D58, D61, D63; the conflicts section of 2 October 2026); `AFRP-Scholarship-Program-Spec.md` §1–§11; `AFRP-Fund-Rules.md` (P9) §2, §2.1, §6; `AFRP-Letters-and-Onboarding.md` (P3) §2, §7; `AFRP-Committee-Workspace.md` (P1) §2–§4; `AFRP-Selection-Committee-Workflow.md` (P5) §3.1; `AFRP-Care-Grants-and-Partners.md` (P11); `AFRP-Executive-Director.md` (P16) §5; `AFRP-Delivery-Status.md` (slices 4, 4b, 9); `site/data/programmes.yaml` (`scholarship`), `workflows.yaml` (`scholarship-renewal`), `experiences.yaml` (`scholar`), `questions.yaml`.

**Research.** Research round, 2 October 2026 (education §1, §2, §6a), private. Research round, 2 October 2026 (care §4), private.

**Public.** IRS, *Topic no. 421, Scholarships, fellowship grants and other grants*: https://www.irs.gov/taxtopics/tc421 (cited by the spec; not re-fetched). The research round also read one comparable federation's published named-scholarship application (membership required, late packets not considered, payment to the institution only); it is another organisation's practice, not confirmed with it, and not a rule here.

**Not verified.** Whether the Hub's slice 4 built named-award matching; which bank account the 2026 cheques drew on; the Ramallah track's practice; whether the 2015 policy's "required academic standing" was ever given a figure in a document the committee adopted.
