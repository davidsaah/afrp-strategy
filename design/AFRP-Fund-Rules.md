# The fund rules, as found

### Each fund as an object on the ledger: its holding entity, its governing text, its distribution rule, the emergency transfer, restricted gifts, the annual run as a dated act, the campaign, and what each Board must do

**Design note P9 · 1 October 2026 · for the Hub's `funds`, `ledger`, `scholarship`, `payments`, the institution registry and the `bylaws` register**

**What this note rests on.** The crosswalk (rows H3, H5, F16; note P9) asked for the fund rules "as found": the two policy statements and the 2015-revised ARFECF by-laws located in the Federation's drive on 1 October 2026 (`design/bylaws/ARFECF-2015-and-the-fund-policies.md`), the Decisions Register (D2, D3, D7–D10, D40, D55–D58), the rules register rows for the affiliates (`AFRP-ARFECF-ARFHSN-Rulesets.md`), the ledger model (`AFRP-Multi-Entity-Ledger.md`), the `giving-funds` and `remittance-ledger` workflows, the programme register, and the open questions Q-2, Q-3, Q-21 (settled by D56) and Q-35. The intakes of September–October 2026 (the Federation's money folders, the officer archive 2009–2026 and ARFECF's archive) are cited at role level and without figures, as D54 requires. Outside the record: Michigan's enactment of the Uniform Prudent Management of Institutional Funds Act and the IRS forms that report endowments and restricted gifts, cited in the Sources.

This note adds no decision. Where it reads as a rule, the rule is a by-law or policy cited by number, a decision cited by number, a rules-register row, or a *design choice* labelled as such. Where the record is silent it says so and raises a question for the Board that owns it.

**Precedence (D41).** The ARFECF by-laws (revised 2015) and the two fund policy statements are texts and outrank everything below them, including D2 and D3 where they disagree. The Decisions Register and the named design documents come next. The prototype's `#/program/endowment` and `#/institutions` evidence a story and never a rule. The Hub's `funds` and `scholarship` modules (slices 4 and 4b) show what is built and never what should be. The 2025 "Endowed Fund" guide and the 2025 Donor Policy Manual are **drafts with the approver blank** (D2's challenge note; Q-35): they are evidence of an intention and bind nothing until a Board adopts them.

---

## 1. What the record already holds

**Built (slices 4 and 4b, 8 September 2026; the restricted-funds engine of the prototype port).** The Scholarship Fund's spending limit is enforced as By-Law 6.4.3's cap over a valuation the committee enters with a source and an as-of date; **no code computes a percentage of anything** (slice 4b retired EC-OV-6 as superseded by decision). The fund boundaries refuse by name: a designated officer cannot stand in for the Scholarship Fund Committee (6.4.4); money never moves between the Endowment and Scholarship Funds (6.3.8 / 6.4.8); Decision 7's surplus rule cannot reach ARFECF; award receipts are ARFECF's. A money-taking event must name a purpose, a purpose belongs to an entity, only that entity authorises raising in its name, the money reaches that entity's restricted account, and spending releases the restriction (Delivery Status, "Restricted funds"). The public giving door (J12) is built; the four contributor moments (D10), the surplus-before-payment rule (D7, journeys JM-067 and JF-088), the purpose catalogue (D8) and pledges against cash (JP-032) are designed and not built. The ledger posts gross with fees as an expense (R20), closes daily as an idempotent batch (R22), reverses as new entries (R24); restricted classes post gross and report per entity, without the receivable R25 asks for.

**Decided.** The Endowment Fund sits in ARFECF (D2, *challenged* on 1 October by the unadopted 2025 guide; stands until the Boards of 4 November 2026, Q-35). The scholarship's legal home is ARFECF (D3), amended by D58 to let the Ramallah Foundation hold Scholarship Committee seats once the ARFECF Board amends the 2015 policy by two-thirds. Surplus on a restricted appeal goes to the receiving entity's general fund only where one exists and only because the donor read the rule before paying; never within ARFECF (D7). Raising in another entity's name runs on a purpose catalogue with escalation (D8). A gift is receipted by the entity that receives it (D9); ARFHSN receipts the Medical Mission and Human Services Network gifts and the Federation collects them as its agent (D56). The Endowed Fund and the Foundation are funds shown on the Care branch and not joinable (D40). A programme's holding entity is the fund that budgets it (D55). Every gift may carry a club attribution (D57).

**The texts, as the extract records them.** Both policy statements make a distribution of **4% of the fund's assets to its purposes plus 1% of its assets to AFRP** mandatory in each fiscal year (1 June to 31 May); "assets" are the property and funds allocated to the fund less its liabilities; the fund's committee approves and distributes; an annual report of donations and distributions by 31 March; thank-you letters within 48 hours carrying the tax-deductibility statement. The by-laws limit each fund's annual expenditure to 5% (6.3.3, 6.4.3) and give each fund's committee exclusive authority over it (6.3.4, 6.4.4); non-earmarked money never crosses between the funds (6.3.8, 6.4.8); rules and fund-policy amendments take two-thirds of all voting Board members (Art. V §3, 6.3.6, 6.4.6; EC-OV-11: a fixed denominator, at a meeting). The Endowment statement alone adds the emergency transfer (a fixed sum to AFRP, at most once every three years, on the Board's confirmation of a deficit), a share of a year's third-party donations for the committee's donor-visit travel on a budget the ARFECF Board approves, and a committee of at least seven. The Scholarship statement alone adds the committee's make-up (D58), published application guidelines (not found) and follow-up on academic standing. Neither text names a valuation date; neither says who may waive or carry over an unspent balance.

**Historically (the intakes, role level, no figures).** The Endowment was created by a Convention vote in the mid-1990s as a Federation fund with rules approved by member ballot; it was moved under ARFECF in 2011 on outside counsel's advice, with the IRS correspondence kept in the officer archive, and the audit notes since then call it *board-designated and unrestricted*. The 1% administration fee was first proposed in that 2011 exchange. Every ARFECF budget and audit note since 2012 applies the two rates to the **31 May valuation of the Scholarship and Endowment Funds taken together**, and the Federation's July budget carries the result as a transfer line into the Educational Fund page and an income line on the General Fund page; the 1% is paid from the Educational Fund's cash to the General account during the year. Two departures from the rule are on record without a written authority: in the 2020 market fall the year's budget was set on a reduced base, and in one recent year the unspent half of a distribution was carried into the next year's budget as its own line. A loan from the Educational Fund to an outside group was made in 2017 on a Federation Board motion the ARFECF Board concurred with, repayable from that group's donations and convention proceeds; neither policy contemplates a loan. The Magazine's assets were moved under ARFECF's account in 2022; a camp land account and a donor-restricted camp endowment are held inside ARFECF and kept out of income. A Donor Policy Manual and a gift-agreement template (2025) would allocate **a share of every restricted gift to general operations** and give the AFRP Executive Board, through its Finance Committee, oversight of gifts; their approval lines are blank. An ARFECF 2012 Investment Committee Policy Statement is the only investment policy text found; the Investment Committee said in September 2026 that it operates without Board-approved parameters and is writing an investment policy statement for **both Boards on 4 November 2026**, covering every fund of both entities as one portfolio. An ARFECF 2021 amendment package proposed naming the AFRP Board as the governing authority for ARFECF's budget; no adoption is recorded. The Endowment Fundraising Committee runs a five-year pledge campaign in tiers (an endowment goal, annual instalments, pledge cards, QR codes and the website, a pledge ledger in a spreadsheet, thank-you letters, the first cash transferred to the investment account in 2025–26); it has asked the Board for full Board giving and proposed re-allocating convention ad-book revenue raised outside the host community to the endowment with a share to the home club, a policy for the Convention Innovation Committee. The annual report of donations and distributions the policies require by 31 March is not seen after 2013.

**The naming clash, stated once.** The by-laws and policies name two funds, the *Endowment Fund* and the *Scholarship Fund*. The audits name two investment accounts, *Education Fund* and *Endowment Fund*. The Federation's budget names an *Educational Fund* page whose "4% transfer" is computed on both funds together, beside a General Fund page. ARFECF's treasurer reports name an *Education Fund checking* account distinct from both investment funds. This note uses the by-law names for the two funds and "ARFECF's operating account" for the checking account; the register carries the aliases so a report can be read against any of them. *Design choice.*

---

## 2. The fund as an object

A fund is a ledger object with the following properties, each carried as data with its source and date, never as a constant in code. The platform refuses any posting to a fund whose holding entity, governing text or kind is unset, and names the gap.

| Property | What it is | Source of the value |
|---|---|---|
| Holding entity | AFRP, ARFECF or ARFHSN; the entity whose books and tax return carry the fund | D2, D3, D55, D56; a Board confirmation where the record says "confirm" |
| Governing text | The by-law article and the policy statement that rule the fund, by citation and version | `bylaws/` and the extract; the register's ruleset ids (`arfecf-bylaws-2013.1` for both ARFECF funds, D2-A) |
| Kind | True endowment (donor-restricted as to principal); board-designated (quasi-endowment); donor-restricted purpose fund; sub-fund of another fund; operating | The gift instrument or the Board resolution that created the fund, cited; **not stated for most funds today** (§2.1) |
| Receipting entity | The entity whose name and exempt-status language a receipt carries | D9, D56; the determination letter on file for the entity (ARFECF's is missing) |
| Distribution rule | The formula as the policy states it, and the parameters it needs (§3) | The policy statement; parameters attested on the register |
| Authoriser | The body with exclusive authority over spending from the fund | 6.3.4, 6.4.4 for the two ARFECF funds; D63 (the holding entity's Board) for the Care funds; By-Law 7.2.3 and the approved budget for the General Fund |
| Transfer rules | What may leave the fund other than its purposes, with the approval each needs | 6.3.8, 6.4.8 (never between the two funds); the emergency transfer (§5); the 1% administration transfer (§3.4) |
| Report duties | What must be reported, to whom, by when | The policies' 31 March report; ARFECF Art. VI (committee reports at the Convention); ARFHSN Art. III §7; Form 990 Schedule D Part V |
| Aliases | The names the budgets, audits and the CRM use for the same fund | §1, the naming clash |

### 2.1 The funds the record names (one row per fund in the register, splitting the rows below that hold two)

| Fund | Holding entity | Kind as the record states it | Governing text | Status |
|---|---|---|---|---|
| Endowment Fund | ARFECF (D2, challenged; Q-35) | The audits say board-designated, unrestricted; the 2025 drafts say permanently restricted principal; **not settled** | ARFECF 6.3; Endowment Fund Policy Statement 2012 | Rule in force; entity confirmed at the 4 November Boards |
| Scholarship Fund | ARFECF (D3) | Not stated; the audits treat it as the fund's own assets | ARFECF 6.4; Scholarship Fund Policy Statement 2015 | Rule in force |
| Named scholarships within the Scholarship Fund | ARFECF | Donor-restricted purpose funds, each with written donor criteria (a 2018 proposal; adoption not shown) | 6.4; the donor's instrument | Whether any exists is a question on the scholarship register. *Since 2 October 2026:* the office's list (about twenty names) enters as **placeholder candidate rows**, one per name, with status *instrument not found* and kind, criteria and balance unset; each refuses posting and matching until the committee's reconciliation act confirms an instrument (P26 §5, SA6; Q-102) |
| Camp Ramallah endowment and the camp land account | ARFECF (D55) | Donor-restricted (camp gifts kept out of income "because they form the endowment for a future camp") | The Board's resolution and the gifts' designations, not found as text | Entity confirmed by budget; kind to be confirmed |
| The Magazine's assets | ARFECF (D55) | Not stated; a separate valuation within ARFECF's account since 2022 | The 2022 ARFECF Board approval | Entity confirmed by budget. *Since 2 October 2026:* split into two rows, the Magazine's operating account and its managed investment account (kind not stated; Q-95), both ARFECF's (P24 §6, MG5) |
| ARFECF's operating account ("Education Fund checking") | ARFECF | Operating | ARFECF §10.1 (the Treasurer's duties) | — |
| General Fund | AFRP | Operating | AFRP By-Laws 7.2.3, 7.5, 8.7, 11.1 | — |
| Relief Fund | **AFRP (D83, 3 Oct 2026)**; until then not stated (F15; its budget page is the Federation's; P11) | Donor-restricted to relief; the budget funds "Ramallah charities" from it by a Convention decision | A Board vote of 2020, extended 2021; the host-agreement template sends a per-registrant amount to it | The entity is P11's first question. *Since 2 October 2026:* designed in P23 §3 (the fund row with the evidence attached, aliases, an opening balance entered once the entity is named, three paths with authoriser rows that have no value; RL1) — the entity is still Q-109. In practice (research, 2 Oct 2026): the account is titled in the Federation's name, the Educational Fund Treasurer reports it at every Board meeting, and ARFECF's books carry it; see Q-109. *Since 3 October 2026:* **D83** (David's decision for the design record) names **AFRP** as the holding entity; the deductibility and receipt text waits on the CPA (D9); the books carry the fund inside ARFECF, a reconciliation item in the Decisions Register's conflicts table (the books follow D83, or the Boards revisit). Who approves each transfer between the Board's votes, and whether D63's closing records apply, stay Q-109. |
| Medical Mission fund; Human Services Network fund | ARFHSN (D56, D62) | Donor-restricted purpose funds; a major donor's project fund is held in a dedicated brokerage account whose income follows the restriction (ARFHSN Board, 2023) | ARFHSN Art. III §5, §7; D63 | P11 |
| Women to Women | ARFHSN, as a sub-fund (D55) | A segregated account inside ARFHSN's books; restricted to its purposes | D55, D56, D63 | P11. In practice (research, 2 Oct 2026): money leaves from a US account to an account in Ramallah, and a contact there disburses against receipts; the committee, not ARFHSN's Board, approves projects; ARFECF's statements carry Women to Women gifts in one year; see Q-114, Q-212, Q-104. An endowed fund for it is Q-210; its tuition awards are a Care grant row on P11 (P26 §6.1; Q-211) |
| Senior Living campaign; the senior centre memorial fund | **Not stated** (Program Architecture names the Foundation; D55 does not name it) | Capital campaign, restricted, ring-fenced (JP-032). *Since 2 October 2026:* a pass-through purpose for an outside body, the Ramallah Foundation; the capital campaign is marked unoperated (P23 §9.2, §9.7) | None found | Open on the programme register. *Since 2 October 2026:* the receiving entity holds no value and the purpose does not publish until Q-204; gifts received before then are held as a liability to the entity to be named; transfers to the Foundation are dated acts against the "due to" liability (P23 §9.2, RL5); whether Senior Living is a Federation programme at all is Q-203 |
| Cook Book fund | ARFECF (a 2017 treasurer's report) | Historic sales fund | None | Whether it still exists is not stated. *Since 2 October 2026:* it exists. The Educational Fund Treasurer reports it at every Board meeting, reprints are paid from it, and it made one transfer to the Education Fund in 2025–26 (P24 §9; P26 §6.2; Q-173, Q-174). A transfer out refuses, naming Q-173. Nothing posts to or from it until its kind and governing text are set (rule 1; P24 §9; P26 §6.2). *Resolved 2 October 2026 in favour of rule 1: P24 §9 now follows it.* |
| Needy-families fund (the CRM's fund for the clubs' relief drive) | **Not stated** | Not stated | None | *Since 2 October 2026:* a separate row with a pointer to the Relief Fund row; neither merges the other (P23 §3; Q-180) |
| The Federation's Senior Living budget grant | ARFECF (the Educational Fund page of the budget) | A budget-line payment to an outside body, not a fund | The budget line voted with the budget (Q-234) | *Since 2 October 2026:* recorded in P23 §9.5 as a payment with By-Law 7.7.1's two signatories; listed here so it is not read as a fund |

**What the kind decides.** Under the Uniform Prudent Management of Institutional Funds Act as Michigan enacted it (Act 87 of 2009, MCL 451.921–451.931), an "endowment fund" is one the *donor* restricted as to spending; a fund the Board set aside on its own motion is not one, and the Board may spend or unwind it as it chooses. The statute's prudence factors and its release-of-restriction paths (§451.924, §451.926) therefore reach the camp endowment and any donor-restricted gift inside the two funds, and reach the Endowment Fund itself only if it holds donor-restricted principal. The 2017 audit note says the Endowment Fund is board-designated; the 2025 drafts would re-describe it as permanently restricted. The platform records the kind per fund, and per restricted gift within a fund, from the instrument that created it, and refuses to describe a fund as "permanently restricted" or "endowment" on a donor-facing page until that instrument is cited. *Q-95.* Which state's law governs each fund is also not in the record: the three entities are described as Michigan non-profit corporations (ARFHSN Art. I; the rulesets' entity table), which makes Michigan's act the likely one, but the Legal Advisor has not said so. *Q-96.*

---

## 3. The distribution rule

### 3.1 The formula, as the policies state it

For each of the Endowment Fund and the Scholarship Fund, in each fiscal year:

- *distribution to the fund's purposes* = **rate_programmes × assets**, where rate_programmes is the policy's 4%;
- *transfer to AFRP for administration* = **rate_admin × assets**, where rate_admin is the policy's 1%;
- *assets* = the value of the property and funds allocated to the fund **less its liabilities**;
- both are **mandatory** ("shall") within the year 1 June to 31 May.

The by-laws separately **limit** each fund's annual expenditure to **rate_cap**, the by-laws' 5%, "of all assets and income derived from the investment of the corpus … in that year" (6.3.3, 6.4.3). The two rates sum to the cap, which is why the record's "floor versus cap" framing was withdrawn on 1 October. The two bases are not worded identically: the policies say assets less liabilities; the by-laws say assets and the year's investment income. On any ordinary year the policy figure sits inside the by-law limit; the platform computes both bases, shows both, and flags a year in which the policy figure would exceed the by-law limit as a conflict for the ARFECF Board rather than silently taking the lower. *Design choice.*

### 3.2 The parameters, on the register

Every number in §3.1 is a register row, attested with a source, a date and the authority, in the pattern slice 4b set: the committee enters the number from the report it receives; the platform records, shows and warns; a developer never types the figure.

| Parameter | Value's source | Attested by | Not stated in any text |
|---|---|---|---|
| rate_programmes, rate_admin | The two policy statements | The ARFECF Board's reading of its policy, recorded once with the drive reference | — |
| rate_cap | ARFECF 6.3.3, 6.4.3 | The by-law text | — |
| valuation_date | **Practice only**: every budget and audit since 2012 uses 31 May | The ARFECF Board, as a register row | The policies say "assets" and name no date (EC-OV-6's gap, now a Board row rather than an override) |
| base_scope | **Practice only**: the Federation's budgets compute on the two funds together; the policies are written per fund | The ARFECF Board | *Q-97* |
| fiscal_year | 1 June to 31 May | The policies (the ARFECF by-laws state no fiscal year, EC-OV-5) | — |
| valuation_amount (per year) | The custodian's statements at the valuation date | The ARFECF Treasurer, with the statement reference and the as-of date | — |
| waiver_authority | **Not stated** | — | Who may reduce, waive or carry over a mandatory distribution (Q-35) |

A run cannot start while any row it needs is unset; the refusal names the row and the Board that fills it.

### 3.3 What the rule does not say, and the platform does not guess

- **Reduction or carry-over.** "Mandatory" leaves no room to spend less, yet the record shows a reduced year and a carried-over half-year. The platform records a distribution below the computed figure only as a dated act carrying the authority that approved the departure; with waiver_authority unset it refuses and names Q-35. A carried-over balance is a labelled line on the next year's run, never a silent addition to the base.
- **Within the cap but above the policy.** The by-laws permit up to 5% from each fund; the policies require exactly 4 + 1. Spending above 4% to purposes (for instance, programme spending plus the 1% exceeding 5%) breaches the by-law and refuses; spending between the policy's 4% and the cap is not contemplated by either text and refuses with the same question.
- **Per fund.** The by-laws and policies speak of each fund. A combined computation is the Federation's budget practice. The platform computes per fund and shows the total, so a per-fund breach (the Scholarship Fund spending 6% while the total stays under 5%) is visible. *Design choice, pending Q-97.*
- **The loan of 2017.** Neither text contemplates lending from a fund. A loan is not a distribution and not an expenditure; the platform has no object for it and records such a transaction only as an inter-entity agreement with its terms (D2-E), refusing to book it against the distribution.

### 3.4 The 1% transfer as an agreement line

The 1% to AFRP crosses an entity line and is therefore an agreement in the institution registry, not a setting (D2-E). On the ledger it is one line per fund per year: ARFECF (the fund) → AFRP (General Fund income, "administration"), raised by the distribution run, paid during the year by the ARFECF Treasurer, and shown on both entities' books with the policy cited. The AFRP by-laws do not mention it; the ARFECF by-laws say only that an annual fee is paid "as agreed to by the Board and AFRP" (Art. V §1); the policies fix it. The Federation's budget labels it income on the General Fund and an expense on the Educational Fund page, which is the same line seen from each side.

---

## 4. The annual valuation and distribution run, as a dated act

One act per fund per fiscal year, immutable once closed; a change is a new act naming the one it changes.

| Step | Who | What the platform does | Rule |
|---|---|---|---|
| 1. Valuation | ARFECF Treasurer | Enters each fund's valuation at valuation_date from the custodian statements, with the reference and the as-of date; liabilities entered separately | The policies' definition of assets; slice 4b's pattern |
| 2. Computation | Platform | Shows rate_programmes × assets, rate_admin × assets, the by-law cap on its own base, and the difference; per fund and the total | §3.1 |
| 3. Recommendation | Investment Committee and the fund committees | Records the committees' recommendation as practice (the archive shows it); not an approval | Observed practice; the 2012 Investment policy's annual report to the Board |
| 4. Approval per fund | The Endowment Fund Committee; the Scholarship Fund Committee | Each committee approves its fund's distribution as a vote with a date; a designated officer or the Board cannot stand in | 6.3.4, 6.4.4; the policies ("approve and distribute") |
| 5. The budget | ARFECF Board; the Annual General Meeting | The aggregate ARFECF budget adopted (Art. VII §3 and §7.3; EC-OV-21 harmonises the two); any purpose outside the budget above the President's limit goes to the Board or the AGM per §7.3 | EC-OV-21 |
| 6. The Federation's budget | The Federation's Budget or Finance Committee; the Convention General Assembly | The distribution appears as the transfer line into the Educational Fund page and the 1% as General Fund income; typed budget lines per programme carry their holding entity (H5) | AFRP By-Laws 8.6.1, 8.7.1; D55 |
| 7. Release | Platform | Each programme's budget line is released against the distribution for the year by holding entity; a line whose programme has no confirmed entity refuses to release and says so | D55; `AFRP-Program-Architecture.md` §3 |
| 8. The 1% transfer | ARFECF Treasurer | The agreement line is raised and marked paid when the transfer is made, with the countersignature the by-laws require (§10.1; AFRP By-Law 7.7.1 for the Educational Fund Treasurer) | §3.4 |
| 9. Close | Platform | The act closes; the year's distributions, carry-overs and departures are reportable; the 31 March report draws on it (§8) | — |

A mid-year revaluation does not change the act; a Board that wishes to re-base mid-year records a new act with its authority. The platform never recomputes a closed figure (R43's shape).

---

## 5. The emergency transfer

Only the Endowment Fund Policy Statement provides it: when the ARFECF Board confirms a deficit, the Endowment may transfer to AFRP **up to a fixed sum, at most once every three years**. The sum is a register parameter attested from the policy; it is not written here.

**As an act.** The ARFECF Board's confirmation of the deficit (a vote, a date, the deficit it confirms); the amount, capped at the parameter; the clock since the last such transfer, computed from the register and refusing inside three years; the entity line crossed, so an agreement in the institution registry (D2-E) and a line on both books; on AFRP's side income to the General Fund, labelled. The act is closed by the ARFECF Treasurer's payment with the by-laws' countersignature.

**What the text does not say.** Whether the transfer counts within the fund's 5% cap for the year (6.3.3) or stands outside it; whether the Endowment Fund Committee's exclusive authority (6.3.4) applies to it, since the policy gives the trigger to the Board; whether "the Board" is ARFECF's alone (the 2025 drafts would require a supermajority of both Boards, and are not adopted). The platform refuses to post the transfer while the cap question is unanswered unless the year's total including it stays under the cap, and records the committee's concurrence beside the Board's confirmation rather than choosing between them. *Q-98.*

**The 2011 debate and the 2017 loan** show two other shapes of money leaving the Endowment that the policy does not name: drawing on it for a shortfall, and lending. Neither is a distribution; neither is this transfer; the platform has no path for them and refuses with the policy cited.

---

## 6. Restricted gifts

### 6.1 The rules already held

- A restriction comes only from the donor's designation (S6); the purpose catalogue says what may be raised in which entity's name, and a new purpose goes to that entity's board and blocks publication (D8).
- The surplus and shortfall rules are **printed on the page before payment**, or the appeal cannot publish (D7; JM-067, JF-088, not built). Surplus to the receiving entity's general fund where one exists and the entity's own rules allow; within ARFECF the surplus stays in the fund it was given to, and the screen says why (D7's ARFECF exception; 6.3.8, 6.4.8).
- A gift is receipted by the entity that receives it (D9), with its exempt-status language; a ticket is a purchase and the gift beyond it is receipted separately (D9); four contributor moments then an annual statement (D10).
- Spending on the purpose releases the restriction (built); the fourth contributor notice says the restriction was released *because the money was spent on the thing it was given for*.

### 6.2 What this note adds

**Income on a restricted fund follows the restriction.** ARFHSN's Board upheld this in 2023 for a donor's project fund held in a brokerage account; the draft finance manual states it; the Michigan act's definition of an endowment fund assumes it. The ledger posts investment income and gains to the fund that earned them, and a restricted fund's income carries the same restriction as its principal unless the donor's instrument says otherwise. *Design choice, resting on the practice and the statute; the Boards should say it.*

**The "share of every restricted gift to operations" is not a rule yet.** The 2025 Donor Policy Manual, the gift-agreement template and the 2025 guide would allocate a share of each restricted gift, or of each restricted distribution, to general operations. None is adopted (approver blank). The platform carries the share as a register row with no value and **refuses to deduct anything from a restricted gift** until a Board adopts the policy, the rate is attested, and the deduction is **disclosed on the giving page before payment** in the same way as the surplus rule, because a donor who gave for a purpose and funded operations without being told is D7's own failure case. Within ARFECF the deduction would also have to clear 6.3.8 (it moves non-earmarked money out of a fund) and the committee's exclusive authority (6.3.4, 6.4.4); the platform shows that check beside the row. *Q-99.*

**Named and donor-restricted sub-funds.** A named scholarship, the camp endowment, or a donor's project fund is a sub-fund inside its parent fund: its own restriction, its own instrument cited, its own balance and income, reported on the parent's report. The 2018 proposal for named scholarships (a perpetual fund at a stated minimum, or a one-year sponsorship; the donor's criteria accepted by the committee as "reasonable"; a yearly donor list in the Magazine) is on file as a proposal; whether it was adopted is not shown, and the scholarship register carries the question. The minimums in the 2025 drafts for a named endowment are figures the record does not adopt and this note does not carry.

**An impracticable purpose.** The 2025 guide would let the Board redirect a gift whose purpose becomes impracticable to a closely related purpose. Michigan's act (§451.926) is stricter: a restriction is released or modified only with the donor's written consent, by a court on application with notice to the Attorney General, or by the institution alone for a small, old fund whose restriction has become unlawful or impracticable, and never for a purpose outside the institution's charitable purposes. The platform records a change of purpose on a restricted gift only as one of those three acts, with the instrument attached (D66), and refuses a plain Board redirection. *Design choice resting on the statute; the Legal Advisor confirms which state's act applies (Q-96).*

**Receipts and the missing letter.** ARFECF's exempt-status determination letter is not on file (Q-2; D2 item 3). A receipt in ARFECF's name carries no deductibility statement until the letter is on the registry; the policies' 48-hour thank-you letter "with the tax-deductibility statement" is therefore the first thing the letter unblocks (§9).

---

## 7. The campaign (H3), and the Investment Committee

### 7.1 What the record holds

An Endowment Fundraising Committee of the Federation, working from a committee overview sheet of the standard template, runs a five-year campaign toward an endowment goal: giving tiers defined by an annual amount for five years (a young-adult tier aimed at past scholarship recipients among others, a professional tier, a visionary tier, a legacy tier for corporate and major donors), each with a prospect list, an appeal-letter template, a pledge card with return envelope, a QR code and the website; pledges logged in a spreadsheet ledger; thank-you letters per major donor; follow-up on unpaid pledges; periodic transfer of campaign cash to the investment account (the first in 2025–26). The committee's 2026 minutes shift the strategy from a few large gifts to volume, ask the Board for full Board giving, propose opening ad-book sales to national markets with the out-of-town share to the endowment and a share back to the home club, and promise a joint session with the Convention Innovation Committee on an ad-book policy for 2028. The Federation Board (November 2025) resolved that gifts above a threshold may be designated to a programme. Naming opportunities beyond scholarships are undecided. A case statement (2024) and web copy (2025) exist; the case statement's own pyramid does not reach the goal and was superseded by the tiers.

### 7.2 What the platform does with it

- **A pledge is an object**: donor, tier as a *segment* (Program Architecture §3: the tiers are prospect segments, not products), schedule (annual instalments over the term), designation through the purpose catalogue (D8; the Board's threshold rule for programme designation as a register row), gift agreement linked on the drive (D66), status (pledged, instalment due, paid, lapsed), and the entity that will receipt each instalment. Pledge against cash is reported as JP-032's shape, with pledges never counted as money on the ledger until paid.
- **Which entity receipts an endowment gift is not settled by the record.** D2 puts the Endowment Fund in ARFECF, so D9 makes ARFECF the receipting entity. The pledge cards and letters are signed "AFRP Board of Directors", the gift-agreement template names AFRP and ARFECF jointly with AFRP officers as signatories, and the CRM carries the campaign as an AFRP fund. D56's pattern (the Federation collects as the affiliate's agent and forwards without delay) would resolve it exactly as it did for ARFHSN, but D56 is written for ARFHSN alone. Until a decision extends it, the platform collects a campaign gift on the Federation's page, holds it as a liability to ARFECF, and issues **ARFECF's receipt only once the determination letter is on file**, and before then a receipt that names the holding entity and makes no deductibility claim. *Q-100, with the CPA under Q-3.*
- **Board giving** is a count on the campaign page (Board members who have given this campaign, under the floor), never a list of who has not. *Design choice.*
- **The ad-book share** to the endowment and to the home club is the Convention Innovation Committee's policy for the Board (D59's path) and a club-statement line type (Club Experience Plan §5.2, "ad-book or sponsorship share") once decided; nothing is built for it before then.
- **Outcome reporting to donors** per branch follows D42 and D67.

### 7.3 The Investment Committee

The AFRP by-laws make the Investment Committee responsible for all AFRP investments and for supporting the budgets (8.6.1), composed per "the Board's established Investment Committee policy" (8.6.2), which is not on file. ARFECF's by-laws give its own Investment Committee the supervision of both funds' investments (Art. VI; EC-OV-19 notes the committee is otherwise hollow) and the 2012 Investment Committee Policy Statement sets a five-member committee, allocation bands, a return objective of the spending rate plus inflation, quarterly manager statements and an annual report to the ARFECF Board; the committee said in 2026 it is unadopted or superseded. The committee's 2026 plan is **one investment policy statement for every fund of both entities, to both Boards on 4 November 2026**, with allocation ranges, outside-range transactions needing a Board vote, a committee of seven to nine with qualification guidelines and term limits, and a liquidity plan for the camp fund.

For the platform: the investment policy statement is a text on the register when adopted, with the allocation ranges as parameters; the committee's seats are a committee register row (P1); and **pooling the investments does not pool the funds**. Each fund keeps its own balance, income and restriction on the ledger whatever account holds the securities; a pooled account is allocated to funds by units, and the allocation method is a parameter the CPA attests. Entity lines never net (Club Experience Plan §5.1's rule, applied to funds). *Design choice; Q-101 for the CPA on the pooling method and on reporting a pooled portfolio on two Forms 990.*

---

## 8. What each Board must do, and when

| When | Who | What | Rule |
|---|---|---|---|
| **4 November 2026** | AFRP Board; ARFECF Board | Receive the investment policy statement; adopt or not. On the same day or before, the ARFECF Board says which text governs the Endowment Fund's distribution: the 2012 statement as it stands, or an amendment. An amendment to a fund policy takes two-thirds of all voting Board members, at a meeting, not by poll | Q-35; Art. V §3, 6.3.6, 6.4.6; EC-OV-11 |
| Before the first run on the platform | ARFECF Board | Attest valuation_date, base_scope, waiver_authority (§3.2); confirm each ARFECF fund's kind (§2.1); confirm D55's holdings for its programmes; bring the regional club lists current (EC-OV-1) | §3.2; D55; `ARFECF-2015-and-the-fund-policies.md` |
| Before any receipt in ARFECF's name claims deductibility | ARFECF Board | Put the determination letter on the registry | Q-2; D2 item 3 |
| Before any share of a restricted gift is taken for operations | ARFECF Board (and the AFRP Board for its own funds) | Adopt or set aside the 2025 Donor Policy Manual and gift agreement; attest the rate; approve the disclosure wording | §6.2; D7 |
| When the Foundation seats are wanted | ARFECF Board | Amend the 2015 Scholarship Fund Policy by two-thirds | D58 |
| Each year, 31 May | ARFECF Treasurer; the two fund committees; the ARFECF Board | The valuation and the run (§4) | The policies; 6.3.4, 6.4.4 |
| Each year, July | The Federation's Finance or Budget Committee; the Convention | The budget pages carrying the distribution and the 1% | AFRP By-Laws 8.6.1, 8.7.1; D55 |
| Each year, 31 March | The two fund committees | The annual report of donations and distributions, assembled from the ledger by the platform; thank-you letters within 48 hours all year | The policies; not seen since 2013 |
| Each Convention | The Endowment and Scholarship Fund Committees | A full report at the Convention | The ARFECF by-laws' reporting clause (each fund committee submits a full report at the Convention), as the archive's reading records it |
| Each tax year | Each entity | Form 990 Schedule D Part V (endowment balances, earnings, distributions, and the split between board-designated, permanent and term endowment) and Schedule F where money goes abroad (P11) | IRS instructions, Sources |
| Open date | AFRP Board | The Investment Committee policy By-Law 8.6.2 presumes; the Relief Fund's holding entity (P11); whether the 1% should be written into the AFRP by-laws; whether the 2021 ARFECF amendment package is pursued | 8.6.2; F15; §3.4 |

---

## 9. The documents still missing, and what each unblocks

The register's "five documents" list is out of date: both policy statements are found. What is still missing, as `ARFECF-2015-and-the-fund-policies.md` §4 records it, with what each unblocks here:

| Document | Unblocks |
|---|---|
| ARFECF's IRS determination letter | The deductibility statement on ARFECF receipts, the 48-hour thank-you letter's wording, and the receipting of endowment campaign gifts (§6.2, §7.2) |
| The AFRP Board Rules and Regulations | The dues ladder (outside this note); here, whether any rule on the 1% or on fund transfers is written there |
| The ARFHSN trustee roster with seats and term dates | The ARFHSN Board as an authoriser in P11, and the seat-vote property in the leadership directory (P19) |
| The Scholarship application guidelines the 2015 policy says are published | The scholarship screen's citation of the published criteria (slice 4) |
| Any ARFECF by-law text later than the 2015 revision, and an adopted investment policy statement | Whether the 2015 text is operative; the allocation parameters in §7.3 |

A sixth document is awaited rather than missing: the Board-adopted text that resolves Q-35 on 4 November 2026. Until it exists, the 2012 Endowment Fund Policy Statement governs and the platform runs it.

---

## 10. Rules

1. A fund posts nothing until its holding entity, governing text and kind are set; the refusal names the gap (D55; §2; *design choice* for the refusal).
2. Each of the Endowment and Scholarship Funds distributes rate_programmes × assets to its purposes and rate_admin × assets to AFRP in each fiscal year, mandatorily (the 2012 and 2015 policy statements); annual expenditure from each never exceeds rate_cap on the by-laws' base (ARFECF 6.3.3, 6.4.3).
3. Every rate, date and base in rule 2 is a register row attested with a source and a date; no code computes a percentage from a constant (slice 4b; D41's prohibition on code as a rule).
4. Only the fund's committee authorises spending from it; no officer and no Board stands in (6.3.4, 6.4.4; D2-B, D3-A).
5. Non-earmarked money never moves between the two ARFECF funds (6.3.8, 6.4.8; D2-C); D7's surplus rule never reaches ARFECF (D7).
6. The 1% transfer and the emergency transfer cross an entity line and exist on the ledger only as recorded agreements (D2-E).
7. The emergency transfer requires the ARFECF Board's confirmation of a deficit, never exceeds the policy's sum and never recurs inside three years (the Endowment Fund Policy Statement); how it counts against the cap is open (*Q-98*).
8. A distribution below the mandatory figure, a carry-over, a loan from a fund or a drawing for a shortfall is recorded only with the authority that approved it, and refuses while that authority is unset (Q-35; *design choice* for the refusal).
9. A restriction comes only from the donor (S6); the surplus and shortfall rules are printed before payment (D7); the gift is receipted by the receiving entity (D9) and the contributor hears at four moments (D10).
10. Income on a restricted fund follows the restriction (*design choice* resting on ARFHSN's 2023 practice and the Michigan act's definition of an endowment fund).
11. No share of a restricted gift is taken for operations until a Board adopts the policy, the rate is attested, the deduction is disclosed before payment, and within ARFECF rules 4 and 5 are satisfied (*design choice* resting on D7, 6.3.8, 6.4.4; *Q-99*).
12. A restricted purpose changes only by the donor's written consent, a court's order, or the statute's small-old-fund release, with the instrument on the drive (MCL 451.926; D66; *design choice* pending *Q-96*).
13. Pooled investment never pools funds: each fund keeps its balance, income and restriction; entities never net (*design choice*; *Q-101*).
14. A pledge is not money until paid (JP-032's shape; *design choice*).
15. The valuation and distribution run, the emergency transfer and any departure are dated acts, immutable once closed; a change is a new act naming the old (R24's and R43's shape).
16. Figures in this note's subject are never in this note: every sum and balance lives on the register or the ledger (D54; the public-repository rule).

---

## 11. What this note raises

| Q | Question | Owner |
|---|---|---|
| Q-95 | The kind of each fund: is the Endowment Fund board-designated (as the audits say) or donor-restricted as to principal (as the 2025 drafts would make it), and which gifts within the two funds, the camp endowment and the Magazine's assets are donor-restricted? The answer decides whether the state's endowment statute governs spending from it | ARFECF Board · CPA · Legal Advisor |
| Q-96 | Which state's law governs each entity's funds; whether Michigan's Uniform Prudent Management of Institutional Funds Act (Act 87 of 2009) applies to ARFECF's and ARFHSN's restricted funds | Legal Advisor |
| Q-97 | Whether the distribution is computed per fund, as the policies are written, or on the two funds together, as the Federation's budgets do; and the valuation date, which the policies do not name | ARFECF Board |
| Q-35 | Who may reduce, waive or carry over a mandatory distribution, and by what vote; whether the reduced year and the carried-over half-year on record were authorised and by whom (a sub-question of Q-35) — numbered as the existing Q-35, whose detail gains this facet | ARFECF Board |
| Q-98 | Whether the emergency transfer counts within the fund's 5% cap, whether the Endowment Fund Committee's exclusive authority applies to it, and whether "the Board" is ARFECF's alone | ARFECF Board |
| Q-99 | Whether the 2025 Donor Policy Manual and gift agreement are adopted, and if so whether their share of restricted gifts to operations is lawful within ARFECF under 6.3.8 and 6.4.4, how it is disclosed to donors, and how it relates to the 1% | ARFECF Board · AFRP Board · CPA |
| Q-100 | Which entity receipts an endowment campaign gift collected on the Federation's pages, and whether D56's agency pattern extends to ARFECF's funds | AFRP Treasurer · ARFECF Board · CPA (with Q-3) |
| Q-101 | If both entities' funds are invested as one portfolio under the November 2026 policy, how units are allocated to each fund and entity and how the pooled portfolio is reported on two Forms 990 | Investment Committee · CPA |
| Q-102 | The named-scholarship proposal of 2018: adopted or not; which named scholarships exist, with what written donor criteria | ARFECF Board · Scholarship Fund Committee |
| Q-103 | Whether the 2021 ARFECF amendment package (the AFRP Board as the governing authority for ARFECF's budget) is pursued; if adopted it changes the authoriser in §4 step 5 | ARFECF Board · AFRP Board |

Open items carried, not new: Q-35 (the endowment's rules and entity, 4 November 2026); Q-2's remaining documents (§9); Q-3 (the CPA on agency); the Relief Fund's entity (F15, P11; now Q-109, with P23 §3's evidence); the Senior Living entity (programme register; *since 2 October 2026* Q-203 and Q-204, P23 §9); the Cook Book fund (Q-173) and the three per-meeting treasurer's reports as a report duty (Q-174); the named scholarships' instruments (Q-102; P26 §5).

---

## 12. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| FR1 The fund register | The fund object with its properties and aliases (§2); every fund §2.1 names (one row per fund, splitting the rows that hold two), each with its entity, text, kind and status as the record states them, "not stated" refusing to post; the register rows of §3.2 with no values; the institution-registry agreements for the 1% and the emergency transfer | §2, §3.2, §3.4 | None; values are the Boards' to attest |
| FR2 The valuation and distribution run | The nine-step act (§4): per-fund computation on both bases, the committee votes, the Board's budget, release to typed budget lines by holding entity, the 1% agreement line, the close; departures only with an authority; the 31 March report assembled from the run | §3, §4, §8 | valuation_date, base_scope attested by the ARFECF Board; waiver_authority may stay unset (the refusal is the behaviour) |
| FR3 The emergency transfer | The act of §5 with the Board's confirmation, the parameter, the three-year clock and the cap check; refusal paths for loans and shortfall drawings | §5 | None to build; posting waits on Q-98 only where the cap would be exceeded |
| FR4 Restricted gifts, completed | JM-067 and JF-088 (surplus and shortfall printed before payment; publication blocked without them); income following the restriction; sub-funds with their own instruments; the operations-share row with no value and its refusal; change of purpose only by the three statutory acts; receipts without a deductibility claim until the letter is on the registry | §6 | None |
| FR5 Campaign pledges | The pledge object and schedule, tiers as segments, pledge-against-cash reporting, designation through the catalogue with the Board's threshold row, the Board-giving count under the floor, the receipt path of §7.2 | §7.1, §7.2 | Q-100 for the receipting entity; the collection and holding path builds now |
| FR6 Pooled investment, separate funds | Unit allocation of a pooled account to funds with the method as a CPA-attested parameter; the investment policy statement as a register text with allocation ranges; the Investment Committee's seats as a committee register row until CW1 (P1) | §7.3 | The 4 November 2026 policy; Q-101 |

Order: FR1 first (everything else posts to it); FR2 and FR4 next, in either order; FR3 with FR2; FR5 when the campaign's first instalments are due on the platform; FR6 after 4 November 2026. P11 (`AFRP-Care-Grants-and-Partners.md`) builds the outbound side on FR1's fund objects and should not start before FR1.

What the Hub's record should take in the same pass: mark the two policy statements `cited-found` with the extract's drive references; retire EC-OV-1 as superseded by text; move EC-OV-6's valuation-date gap to a Board register row; record the two bases of §3.1 on the ARFECF rules rows; add the aliases of §1 to the fund rows.

---

## 13. Journeys proposed

Identifiers are provisional; the Hub's workbench assigns catalogue ids. Class is what the journey must reach for the slice that builds it to close.

| Journey | Tests | Must reach | Slice |
|---|---|---|---|
| P9-J01 A fund with no entity posts nothing | A gift to the Senior Living fund refuses to post and names D55 and the missing entity; a gift to the Relief Fund, whose entity is AFRP (D83), posts *(rewritten 3 Oct 2026 under D83; until then the Relief Fund was this journey's first case)* | meets | FR1 |
| P9-J02 The run computes from attested rows and never from a constant | With valuation_date unset the run refuses and names the ARFECF Board; once attested, the figures match the committee's entered valuation; no code path holds a rate | meets | FR2 |
| P9-J03 Two bases, both shown, the cap never silently wins | A year in which the policy figure would exceed the by-law limit flags a conflict rather than taking the lower | meets | FR2 |
| P9-J04 A distribution below the mandatory figure needs a name | Entering less than rate_programmes × assets refuses while waiver_authority is unset and names Q-35; with an authority attested it records the departure as a dated act | guarded until Q-35 (the refusal is the pass) | FR2 |
| P9-J05 The 1% is an agreement, not a setting | The transfer appears as one line on both entities' books citing the policy; deleting the agreement refuses the line | meets | FR1, FR2 |
| P9-J06 The committee alone approves | The ARFECF Board, a designated officer and the AFRP Board are each refused the Scholarship Fund's approval step by name (6.4.4); the committee's vote closes it | meets | FR2 |
| P9-J07 The emergency transfer keeps its clock | A second transfer inside three years refuses; a transfer without a recorded deficit confirmation refuses; a transfer that would carry the year over the cap refuses and names Q-98 | meets (the refusals) | FR3 |
| P9-J08 A loan is not a distribution | A loan from the Educational Fund can be recorded only as an inter-entity agreement with terms and never reduces or counts toward the year's distribution | meets | FR3 |
| P9-J09 Surplus printed before payment | An appeal without its surplus and shortfall rules cannot publish; an ARFECF appeal's surplus stays in the fund and the page says 6.3.8 | meets | FR4 |
| P9-J10 Income follows the restriction | Investment income on a donor's project fund posts to that fund and inherits its restriction; moving it to operations refuses | meets | FR4 |
| P9-J11 No operations share without adoption and disclosure | A restricted gift posts gross; the operations-share row with no value deducts nothing; with a value but no disclosure on the page, still nothing; within ARFECF the 6.3.8 check shows | meets | FR4 |
| P9-J12 A purpose changes only by a statutory act | A Board "redirection" of a restricted gift refuses; a donor's written consent linked on the drive records it | guarded until Q-96 | FR4 |
| P9-J13 No deductibility claim without the letter | An ARFECF receipt names the entity and makes no claim until the determination letter is on the registry; the day it is, the policy's statement appears | meets | FR4 |
| P9-J14 A pledge is not money | A five-year pledge shows on the campaign page and nowhere on the ledger until its first instalment is paid; the instalment is receipted by the holding entity on the path of §7.2 | guarded until Q-100 for the receipt entity; meets for the ledger | FR5 |
| P9-J15 Board giving is a count | The campaign page shows how many Board members have given, under the floor, and no list of who has not | meets | FR5 |
| P9-J16 Pooled securities, separate funds | Two funds in one custodial account keep separate balances and income by units; a report for one entity never includes the other's | guarded until Q-101 | FR6 |
| P9-J17 The 31 March report | The annual report of donations and distributions assembles from the closed run and the year's gifts, per fund, per entity, with the policy cited | meets | FR2 |
| P9-J18 A fund's kind is stated or absent | A donor-facing page calls a fund "endowment" or "permanently restricted" only where the instrument is cited; otherwise it shows the holding entity and the purpose and nothing more | meets | FR1 |

---

## 14. What changes in the site's data with this note

`workflows.yaml`: `giving-funds` gains the distribution run, the emergency transfer and the operations-share refusal as steps, drops the open item that says the two policy statements are not on file, keeps the determination letter and B3 as open items, and lists this note as a source; a new `fund-distribution` workflow is not needed if the run is a step there, which the owning agent decides. `programmes.yaml`: the `scholarship` entry's money line cites this note for the rule and Q-102 for named scholarships; `relief-fund` and `senior-living` keep "Not stated" and cite §2.1. `questions.yaml`: Q-35 and Q-95–Q-103 numbered by governance; Q-35 gains the 4 November date in its detail. `goals.yaml`: goal 6's open paragraph stops saying the endowment waits on its Policy Statement and says it waits on the 4 November Boards and the determination letter. The crosswalk: H3 updated from "Blocked on the Endowment Fund Policy Statement" to this note and Q-35; H5 and F16 point here; the P9 row marked written. `plan/MASTER-PLAN.md`: rows FR1–FR6 and the "Blocked until documents arrive" row's endowment item re-pointed at Q-35 and the determination letter. `AFRP-Decisions-Register.md`: the "Five documents" paragraph corrected to the list in §9 (an edit for governance, not this note).

---

## Sources

Record: `design/bylaws/ARFECF-2015-and-the-fund-policies.md`; `design/AFRP-Decisions-Register.md` D2, D3, D7–D10, D40, D41, D55–D58, D63; `design/AFRP-ARFECF-ARFHSN-Rulesets.md` Part 1 and EC-OV-1, -5, -6, -11, -19, -21; `design/AFRP-Multi-Entity-Ledger.md`; `design/AFRP-Rules-Register.md` (R20–R25, R43, S6); `design/AFRP-Delivery-Status.md` slices 4 and 4b and "Restricted funds"; `design/AFRP-Program-Architecture.md` §3; `design/AFRP-Strategic-Plan-Crosswalk.md` H3, H5, F16, P9; `site/data/workflows.yaml` (`giving-funds`, `remittance-ledger`), `programmes.yaml`, `questions.yaml` (Q-2, Q-3, Q-21, Q-35), `goals.yaml`; AFRP Constitution and By-Laws 2024, By-Laws 7.2.3, 7.5.1, 7.5.2, 7.7.1, 8.6.1, 8.6.2, 8.7.1, 8.7.2, 11.1.1–11.1.5; the intakes of September–October 2026 (private, in the planning Project), at role level.

Outside the record:
- Michigan, Uniform Prudent Management of Institutional Funds Act, Act 87 of 2009, MCL 451.921–451.931: the act text at https://www.legislature.mi.gov/documents/mcl/pdf/MCL-Act-87-of-2009.pdf (§451.924, the factors for appropriation or accumulation; §451.926, release or modification of restrictions; Michigan's text carries no 7% presumption). The former Uniform Management of Institutional Funds Act, Act 157 of 1976, was repealed by the 2009 act.
- Uniform Law Commission, Uniform Prudent Management of Institutional Funds Act (2006): https://www.uniformlaws.org/acts/upmifa (not confirmed; the Commission's site was not reachable at that path during drafting).
- IRS, Instructions for Schedule D (Form 990), Part V Endowment Funds: https://www.irs.gov/instructions/i990sd (balances, contributions, net investment earnings, grants or scholarships, other expenditures; the split between board-designated, permanent and term endowment).
- IRS, Instructions for Schedule F (Form 990), activities outside the United States: https://www.irs.gov/instructions/i990sf (cited for P11).
- IRS, Publication 1771, Charitable Contributions: Substantiation and Disclosure Requirements: https://www.irs.gov/pub/irs-pdf/p1771.pdf (the written acknowledgement and quid-pro-quo disclosure that D9 and the 48-hour letter rest on; not re-fetched during drafting).
