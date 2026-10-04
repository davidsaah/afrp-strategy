# Bylaws — what the system needs you to say
### A drafting checklist for the revision

**Date:** August 2026
**For:** whoever is drafting the revised bylaws
**Why now:** you are rewriting them anyway. Saying these things precisely costs nothing at draft stage and saves an argument later.

---

## 0. The one structural thing

**Bylaws change. Past decisions must remain reproducible under the bylaws that
were in force when they were made.**

A 2026 election is forever evaluated under 2026 rules, even after a 2027
amendment. If someone asks in 2030 why Chicago had seven delegates in 2026, the
answer must be "because the 2026 bylaws said so", not "because the current
bylaws say so".

So the system stores **versioned rulesets with effective dates**, and every
convention, ballot and apportionment records which version governed it. That is
already built. What the bylaws need to supply is:

- An **effective date** for the revision.
- An explicit statement that amendments are **not retroactive** — decisions
  made before the effective date stand under the prior text.

Without that second sentence, every amendment reopens every past decision.

---

## 1. Say it as a rule, not as prose

The single most useful thing you can do: **write the operative clauses so a
formula can be read out of them.**

Compare:

> ❌ *"Each club shall be entitled to reasonable representation at the
> convention in proportion to its membership."*

> ✅ *"Each club shall be entitled to one delegate for each twenty-five members
> in good standing, or major fraction thereof, provided that no club shall seat
> fewer than one or more than fifteen delegates, and that no club with fewer
> than ten members shall seat a delegate."*

The second one is implementable, auditable, and arguable in advance. The first
one produces a fight at every convention.

---

## 2. The checklist

### 2.1 Membership and standing

- [ ] What memberships exist — **national and club are separate**, with separate dues and independent lapse. Confirm this in the text.
- [ ] What "**in good standing**" means, precisely: dues paid, and paid **by when**.
- [ ] Whether a **life member** is permanently in good standing regardless of term. *(Recommend: yes, explicitly.)*
- [ ] Whether **complimentary memberships** (the newlywed Family year, the scholarship student membership) count for standing and voting. *(They do in the current model — say so.)*
- [ ] Whether someone may hold a national membership with **no club affiliation**.

### 2.2 Voting eligibility

- [ ] Which membership must be current to vote on **federation** matters — national, club, or both.
- [ ] Which must be current to vote on **club** matters.
- [ ] **Minimum voting age.**
- [ ] Any **continuous membership** requirement before the record date, in days.
- [ ] Whether dues paid **after** the record date enfranchise. *(Recommend: no, explicitly — this is the most common dispute.)*

### 2.3 The record date

- [ ] How many **days before the meeting** the roll is frozen.
- [ ] A statement that the roll, once frozen, **is not recomputed**.

*This single clause prevents more election disputes than anything else in the
document.*

### 2.4 Apportionment

- [ ] **Members per delegate** (the divisor).
- [ ] **Rounding** — "or major fraction thereof" means round half up. Say which way, in words that cannot be read two ways.
- [ ] **Minimum** seats per club.
- [ ] **Maximum** seats per club, if any.
- [ ] **Minimum club size** to seat any delegate at all.
- [ ] Which membership counts toward apportionment — national, club, or either.

### 2.5 Quorum

- [ ] Quorum **of what**: total seats apportioned, delegates actually credentialed, or members.
- [ ] What **fraction**.
- [ ] Whether quorum is tested **once at the opening** or **continuously** through the session. *(These behave very differently late on the second day.)*

### 2.6 Thresholds, by kind of question

- [ ] **Officer elections** — plurality, or majority with a runoff?
- [ ] **Bylaw amendments** — two-thirds of *what*: votes cast, or all seats? These give different answers and both are called "two-thirds".
- [ ] **Dues changes** — often a higher bar; say so.
- [ ] **Ordinary resolutions.**

### 2.7 Abstentions — the clause most often missing

- [ ] Are abstentions **counted in the denominator**?

If yes, an abstention functions as a "no". If no, it is a deliberate refusal to
take a side and does not affect the outcome.

The system currently **excludes** abstentions from the threshold denominator,
which is the common convention. **Either answer is fine — but the bylaws should
say which, because otherwise the software is making a governance decision.**

### 2.8 Ties

- [ ] How a tie is broken: chair's casting vote, re-ballot, or lot.

The engine deliberately **never breaks a tie silently** — it reports the result
as undecided. Give it a rule to hand the chair.

### 2.9 Proxies

- [ ] Are proxies permitted at all?
- [ ] If so: limit per delegate, written form required, filed by when, revocable how?

*Currently not implemented, because it is genuinely unclear whether AFRP allows
it. If the revision permits proxies, this becomes a build item.*

### 2.10 Secret versus recorded ballots

- [ ] Which matters are decided by **secret ballot** (typically officer elections).
- [ ] Which are **recorded** and attributed (typically bylaws and resolutions).
- [ ] Whether a delegate may **demand** a recorded vote, and on what showing.

*Note for the drafters:* a secret ballot means the voter↔ballot link is never
stored. A voter gets a one-time receipt to verify their own vote, and **a lost
receipt cannot be reissued**. That is the price of secrecy, and it is worth the
bylaws acknowledging that verification is available but not recoverable.

### 2.11 Certification and challenge

- [ ] **Who certifies** a result.
- [ ] Within **what time**.
- [ ] How a result is **challenged**, by whom, and by when.
- [ ] Whether a certified result can be reopened, and on what grounds.

### 2.12 Committees

- [ ] Which membership scope is required to **hold a seat**.
- [ ] **Term lengths** and any term limits.
- [ ] What happens when a member's standing **lapses mid-term** — automatic suspension, or a vote?
- [ ] The **conflict of interest** standard.

*(Since David's correction of 8 September 2026, recorded in P26 §1.4 and §3.2 (built in slice 4b): the three-degree block below is replaced. Every relationship is disclosed by degree and acknowledged on the record, and only the same household refuses (P26 §3.2; **D84**, 4 Oct 2026, pending the Scholarship Fund Committee's adoption). The paragraph is kept as the August text.)*

On that last point: the scholarship committee currently blocks a reviewer
related to an applicant **within three degrees** in the family tree — parent,
child, sibling, grandparent, aunt/uncle, first cousin — and discloses anything
beyond that. In a federation descended from one ancestor, a stricter bar would
leave no committee at all. **Three degrees is a policy choice and the bylaws or
a committee charter should own it, not the software.**

- [ ] *(Added 2 Oct 2026)* The **composition and name** of the Young Leader Committee (the 8.10 paragraph against practice; Q-179), and whether **8.13 and 8.14** are seated (Q-251).
- [ ] *(Added 2 Oct 2026)* Whether the **Magazine's board** of 6.7.1 exists, and who the "Manager of the Magazine" of 9.5.2 is (Q-192, Q-250).

### 2.13 Amendment

- [ ] Notice period before a vote.
- [ ] Who may propose.
- [ ] Threshold to adopt.
- [ ] **Effective date rule**, and the non-retroactivity statement from §0.

### 2.14 Added from the research round (2 October 2026)

Places the 2024 text is silent or reads two ways, found by the research round and the notes P22–P25. Each is an open question; none is decided here.

- [ ] **How a club chooses its delegates** (9.1.3 is silent; Q-37).
- [ ] **The forfeiture sentence of 10.1.1**: who determines that a turn has passed (Q-240).
- [ ] **Who signs a payment** to a Convention host: 11.1.2 against 7.5.1–7.5.2 (Q-241).
- [ ] **The Annual Meeting without a Convention**: where elections, the budget and amendments are taken (Q-244).
- [ ] **The Federation's representative in Ramallah**, who has no text (Q-246).
- [ ] **The budget's approval path** (Q-234).

---

## 3. Flexibility without vagueness

You asked for flexibility. The way to get it is **not** vague language — vague
language produces arguments, not flexibility. It is:

1. **Put the numbers in a schedule**, not in the body. "Apportionment shall be
   as set out in Schedule A, amendable by the Executive Committee on notice."
   Then changing the divisor does not require a bylaw amendment.
2. **Name the mechanism, fix the parameters separately.** The body says there
   *is* a record date; the schedule says how many days.
3. **Let the system hold the schedule as data.** That is exactly how the engine
   is built — apportionment, quorum, thresholds and eligibility are versioned
   configuration, not code.

That gives you flexibility at the schedule level and certainty at the
constitutional level, which is the right split.

---

## 4. What happens when you send them

Once the revised bylaws exist, the operative clauses become a ruleset with a
version and an effective date. Concretely:

```
bylaws-2027.1  · adopted 12 Jul 2027 · effective 1 Sep 2027
  apportionment  divisor 25, major fraction, min 1, max 15, floor 10 members
  record date    30 days before the meeting
  quorum         one half of credentialed delegates
  eligibility    national membership, age 18, dues paid by the record date
  thresholds     officers simple majority · bylaws two-thirds of votes cast
  abstentions    excluded from the denominator
  ties           chair's casting vote
```

Anything the bylaws leave unsaid stays a **build decision by default**, which
is the situation worth avoiding. This checklist exists so that list comes out
empty.

---

*Design note only. The governance engine already reads rulesets as versioned
data; nothing here requires new code unless proxies are permitted.*
