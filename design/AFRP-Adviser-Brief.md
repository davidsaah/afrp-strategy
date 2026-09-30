# AFRP — questions for our accountant
### A one-time brief. Five questions, one meeting.

**Prepared:** August 2026
**For:** AFRP's CPA or tax adviser
**From:** AFRP platform project

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

---

## Question 2 — Membership dues: recognise on receipt, or defer?

**The situation.** A $1,000 Patron membership paid in March covers twelve months.
We currently recognise it in full when paid.

**Why it matters.** Deferring would recognise roughly $83.33 per month.
It affects timing and year-over-year comparability, not totals.

**The question.** Is recognising on receipt acceptable for an organisation of
our size and audit posture, or should we defer over the term?

☐ Recognise on receipt ☐ Defer monthly ☐ Defer, and split exchange vs contribution

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
   engagement — the 990 preparer already needs Question 1.
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

*Positions cited from IRS Topic 421 (scholarships and fellowship grants),
IRS guidance on withholding for non-resident aliens, and ASC 958 on
contributions held for others. This brief states our reading so it can be
corrected — it is not itself advice.*
