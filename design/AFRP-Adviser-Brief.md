# AFRP — questions for our accountant
### A one-time brief. Five questions, one meeting.

**Prepared:** August 2026
**For:** AFRP's CPA or tax adviser
**From:** AFRP platform project
**Since 2 October 2026:** "AFRP's CPA" is four roles, not one (Q-231): the outside firm that reviews or audits and files the returns; the General Fund Treasurer, a CPA in practice; a volunteer financial adviser, also a CPA; and the bookkeeper. This brief's five questions are for **the outside firm**, which signs the 990, unless the Board names another role under Q-231. The questions the record now holds for the accountants and for the Legal Advisor are listed by Q-number at the end ("Waiting on the accountants and the Legal Advisor").

---

## Why you are reading this

AFRP is building a system to run membership, giving, club finances and the
scholarship program. Most of it is engineering. **Five things are accounting
judgements that only you can make**, and each one is a position we take *once*
and then apply automatically.

We are not asking you to review transactions. We are asking you to write down
five positions with your name and a date on them. The system records which
position authorised each payment, so an auditor can trace anything back to your
determination rather than to somebody's best guess.

Each position has an **expiry date** — deliberately. We would rather come back
to you in two years than have a 2026 opinion quietly governing 2031.

---

## Question 1 — Club dues we collect: liability or revenue?

**The situation.** AFRP national collects membership dues on one merchant
account and remits the local-club portion to each club. The clubs are
separately incorporated.

**Why it matters.** If we are holding that money *for* the clubs, it is a
liability and never touches our income statement. If we may recognise it, it is
revenue and the remittance becomes a grant expense. On one recent month across
five clubs that was **$3,360** — across 26 clubs and a year it is materially
different on our Form 990.

**Our reading, for you to confirm or correct.** Because the clubs are separate
legal entities and we cannot redirect their dues elsewhere, we have modelled
this as an **agency transaction**:

```
On collection    Dr Gateway clearing      Cr Due to local clubs   (liability)
On remittance    Dr Due to local clubs    Cr Cash
```

**The judgement we cannot make.** Under ASC 958 a recipient may recognise
revenue instead if it holds **variance power** or is **financially
interrelated** with the beneficiary. A federation and its chartered clubs might
meet that test. **Do we?**

☐ Agency (liability) ☐ Revenue ☐ Varies by club — see notes

*Since 2 October 2026:* this is Q-3 (D1's countersignature, to be put together with D56's agency treatment of ARFHSN's gifts). In practice (research, 2 Oct 2026) the Federation now runs one card-processing account per entity rather than one merchant account, and its chart books every affiliate purpose it collects as a "due to" liability. No account yet carries club dues in either direction. How often and on whose approval each "due to" is settled is Q-232. See `AFRP-Multi-Entity-Ledger.md` §9.

---

## Question 2 — Membership dues: recognise on receipt, or defer?

**The situation.** A $1,000 Patron membership paid in March covers twelve months.
We currently recognise it in full when paid.

**Why it matters.** Deferring would recognise roughly $83.33 per month.
It affects timing and year-over-year comparability, not totals.

**The question.** Is recognising on receipt acceptable for an organisation of
our size and audit posture, or should we defer over the term?

☐ Recognise on receipt ☐ Defer monthly ☐ Defer, and split exchange vs contribution

*Since 2 October 2026:* this is Q-233, for the outside firm with the General Treasurer. In practice dues are recognised when paid, and the chart already has an unused deferred-dues account. ARFECF moves from a review to an audit from the year to May 2026, so the answer is now needed for an audited entity.

*If deferral is needed, the system already supports it — it is a setting, not a
rebuild.*

---

## Question 3 — Scholarships paid abroad: are they US-source?

**The situation.** Our scholarship program pays students **directly** after
proof of enrolment. Some study in the United States; some study in Palestine,
Jordan and elsewhere.

**Why it matters.** If a grant is US-source and the student is a non-resident
alien, we must withhold and file Form 1042-S. If it is foreign-source, we must
not.

**Our reading, for you to confirm.** Scholarship income is generally sourced to
where the study takes place, so a grant to a student at Birzeit is
foreign-source and outside US withholding — while the same grant to a student
at Michigan is not.

**Please confirm and give us the country list** you are comfortable covering.

☐ Confirmed as written ☐ Confirmed with changes ☐ Different position — see notes

**Countries this determination covers:** ______________________________

*Since 2 October 2026:* the Scholarship is ARFECF's (D3, D55). Which account pays the cheques and in whose name the letters go is Q-158. How the Ramallah track is paid (channel, currency, payee) is Q-255. Both come before this question can be applied to a payment (P26 §2.3, §4).

---

## Question 4 — Withholding rates for non-resident students in the US

**The situation.** Some recipients are non-resident aliens studying in the US.

**Our reading.** The taxable portion (room, board, travel — not tuition or
required fees under IRC §117) is subject to withholding at **14%** for F, J, M
or Q visa holders and **30%** otherwise, reported on Form 1042-S. Treaties may
reduce this.

**The questions.**

- Confirm the rates and the qualified/non-qualified split we apply.
- Should treaty cases route to you individually, or do you want to write a
  standing position for specific countries?
- Do you want to see every 1042-S case, or only those outside the rates above?

☐ Confirmed ☐ Route treaty cases to me ☐ See notes

---

## Question 5 — What do you want to see, and how often?

We can route to you: every flagged payment, only cases outside your written
positions, or a periodic summary.

**Our recommendation:** you write the positions above, we apply them
automatically, and you see **only what falls outside them** — plus a summary at
year end. In a typical year we expect that to be a handful of cases, not a
stream.

☐ Only exceptions ☐ Exceptions + quarterly summary ☐ Every flagged payment

**Renewal.** Positions expire. We suggest **two years**, with a reminder at
60 days. Longer or shorter?

☐ 2 years ☐ Other: __________

---

## What we will do with your answers

Each answer becomes a **standing determination** in the system, recorded with
your name, the date, and an expiry. From then on:

- Matching payments clear automatically and cite your determination.
- Anything outside them **stops** and comes to you with a specific question —
  for example, *"no standing determination covers a non-resident alien on an
  H-1B studying in the US."*
- A payment where we do not yet have a W-9 or W-8BEN **never** clears, whatever
  the determinations say. Missing facts are not a judgement call.

You will not be asked to approve routine payments.

---

## What we are not asking

- We are not asking you to compute any individual's tax liability.
- We are not asking you to review our books transaction by transaction.
- We are not asking for anything urgent. Nothing is blocked *today* — but
  Question 1 should be settled before the first club remittance, and
  Questions 3–4 before the first scholarship paid to a non-resident student.

---

## For AFRP: how to use this

1. **Your existing CPA is probably the right person.** These are the same
   engagement — the 990 preparer already needs Question 1. *Since 2 Oct 2026:* "the existing CPA" could mean any of four roles (Q-231). The 990 preparer is the outside firm.
2. **One meeting.** Send this ahead; the answers are positions they likely
   already hold.
3. **If you do not have a CPA**, look for a firm with nonprofit and
   international-payments experience. Questions 3 and 4 are the specialised
   ones; many general practitioners will not have a settled view.
4. **Interim posture, if nobody is appointed yet.** Scholarship payments to US
   students at US institutions flow normally today. Payments to students abroad
   and to non-resident students queue rather than fail — nobody is left
   unpaid without someone knowing about it.

---

## Waiting on the accountants and the Legal Advisor (2 October 2026)

These are the open questions from the research round and the notes P21–P28 (Q-158 to Q-273) whose owner names an accountant or the Legal Advisor. Each is in `site/data/questions.yaml` with its detail and full owner list. The accountant questions say "CPA" as the record wrote it. Which of the four roles answers each is Q-231, for the Board with the General Treasurer.

**For the accountants**

- Q-158 — Which account pays scholarship cheques, and in whose name the letters go
- Q-168 — May a Care sub-fund pay an Education programme's fees?
- Q-173 — The Cook Book fund, the cook book's copyright and the pending trademark (also the Legal Advisor)
- Q-177 — Does the Endowment transfer fund Leadership Ramallah, and is ARFECF its holding entity?
- Q-180 — Club relief drives run by a committee or an officer
- Q-182 — The Washington internships: which entity pays, and is a stipend advocacy? (also the Legal Advisor)
- Q-193 — What an obituary placement fee is
- Q-194 — By-Law 6.7.1's funding duty against "magazine money kept apart"
- Q-198 — Sales tax on the stores
- Q-204 — Which entity receipts a senior-home gift made through the Federation
- Q-210 — An endowed fund for Women to Women inside ARFHSN
- Q-212 — Women to Women gifts in ARFECF's books
- Q-215 — "All donations go to programmes" against the books (also the Legal Advisor)
- Q-222 — The payment channel for a host settlement (the outside firm)
- Q-224 — Why part of the Convention host fee runs through ARFECF's books (the outside firm)
- Q-232 — Settling the affiliates' accounts on AFRP's books (the outside firm)
- Q-233 — Dues recognition: when paid, or deferred (the outside firm; Question 2 above)
- Q-238 — A guest named by someone else (also the Legal Advisor)
- Q-242 — The tax character of sponsorships, ad-book pages and booths (the outside firm; also the Legal Advisor)
- Q-243 — The per-registration Relief Fund amount in a unified registration (the outside firm)
- Q-248 — Recognition at the Foundation's home and the receipt (the outside firm)
- Q-255 — The Scholarship's Ramallah track

**For the Legal Advisor**

- Q-160 — Is "committee sponsorship approved by the Board" a lineage exception?
- Q-161 — Does the Board approve the year's scholarships, or receive the committee's decision?
- Q-165 — Does the camp hold a written abuse-prevention and reporting policy?
- Q-170 — The summer pilot's learning platform and its learner records
- Q-173, Q-182, Q-215, Q-238, Q-242 — shared with the accountants (above)
- Q-184 — Constituent stories on a committee website
- Q-186 — Guests from other village and town associations at the Day of Action
- Q-189 — What consent an oral-history recording needs
- Q-191 — May minors serve on a programme's volunteer team?
- Q-202 — Do the clan-book PDFs carry living persons' dates?
- Q-219 — Images from a mission
- Q-220 — ARFHSN's revised by-laws and the day the Hub seats the Care lens
- Q-223 — A Federation-hosted Convention abroad, and the rotation
- Q-226 — A club's own membership rule wider than By-Law 4.1.1
- Q-236 — Outreach by a profile field before consent rows exist
- Q-237 — The club's view of its members' contact details
- Q-239 — A Magazine subscriber who is not a member
- Q-240 — The forfeiture sentence of By-Law 10.1.1
- Q-241 — Who signs the payment to a Convention host
- Q-244 — The Annual Meeting without a Convention
- Q-257 — An appeal route for a declined, suspended or cancelled scholar
- Q-261 — Living third parties named in an oral history
- Q-271 — Recruitment through the family tree for scholarship alumni

Earlier open questions with the same owners are Q-3 (Question 1 above), Q-76, Q-81, Q-88, Q-92, Q-95, Q-99–Q-101, Q-109, Q-111, Q-119, Q-121, Q-132, Q-134, Q-148 and Q-156 for the accountants. For the Legal Advisor they are Q-44, Q-46, Q-48, Q-52, Q-53, Q-66, Q-68, Q-70, Q-72, Q-76, Q-78–Q-81, Q-86, Q-89, Q-93, Q-95, Q-96, Q-107, Q-112, Q-113, Q-117, Q-120, Q-122, Q-124, Q-127, Q-132–Q-134, Q-138–Q-140, Q-146, Q-148, Q-151, Q-152 and Q-157.

---

*Positions cited from IRS Topic 421 (scholarships and fellowship grants),
IRS guidance on withholding for non-resident aliens, and ASC 958 on
contributions held for others. This brief states our reading so it can be
corrected — it is not itself advice.*
