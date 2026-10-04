# Building for a revision that hasn't been written yet
### How the app accommodates the new bylaws without being rebuilt

**Date:** August 2026
**Decision recorded:** the bylaws are being revised; the app must accommodate whatever they say.
**Mode:** design and planning. No buildout.

---

## 0. The principle, and its limit

**The bylaws are data. The code implements mechanisms; the bylaws choose among
them and set their parameters.**

That is the whole idea, and it works. But "make everything configurable" is a
failure mode of its own — a system where anything can be changed is a system
where nothing can be relied on, and a governance engine whose behaviour is
entirely a matter of settings cannot certify anything. So the honest answer has
**four** categories, not one:

| | | Cost of a change |
|---|---|---|
| **1. Parameters** | Numbers, dates, thresholds, names | **Free.** Edit a schedule |
| **2. Mechanism choices** | The system implements several behaviours; the ruleset selects one | **Cheap.** Enable and test |
| **3. Structural** | Genuinely new behaviour nobody has described | **Real work.** Weeks |
| **4. The integrity floor** | Properties that are not policy | **Not available**, at any price |

The design goal is to push as much as possible from 3 into 2, and from 2 into
1 — and to be explicit about the boundary, so that when the Constitution
Committee proposes a clause, **the answer to "what does that cost us?" is
known before the vote, not after.**

That last point is the practical payoff. §5 describes how the drafting
committee gets that answer from the system itself.

---

## 1. Everything the bylaws set, sorted

This is drawn from the actual documents, not from a generic template. It is
also the checklist for what the revision needs to be explicit about.

### Tier 1 — parameters. Change these freely, forever.

**Membership and money**

- Membership year (currently 1 Sep – 31 Aug, By-Law 5.1) and fiscal year (1 Jun – 31 May, 8.7.2)
- The dues ladder, per tier — **already versioned data**, see §7
- Dues deadline for voting (28 February, 5.3 / 8.15.5)
- Minimum age for membership (18, 4.1.1)
- Student dues waiver age (under 26, 5.2)

**The election calendar** — every one of these is a parameter

- Candidate intention deadline (1 November, 9.3.4)
- Board evaluation window (15 days), Credentials certification (31 December)
- Membership list to Credentials (10 May, 8.15.6); certified list out (25 May, 8.11.2)
- Poll close (currently 20 June postmark, 9.2.2)
- Chapter affiliation form (1 August, 3.2)

**Thresholds and counts**

- Quorum count (25 paid members, 10.1.5)
- Amendment threshold (2/3 delegate vote, Const. XI §2, By-Law 16.1.1)
- Board Rules and Regulations threshold (2/3 of all Board members, 6.2.1)
- Delegate-vote trigger (15% of polled delegation chairs, 9.1.1)
- Notice periods (60 days: amendments Const. XI §3, convention 10.1.4, bylaw submission 16.1.1)

**Terms, eligibility and committee sizes**

- Officer term limits (4 consecutive one-year terms; President three-year cooling-off, 9.3.3)
- Members At Large (4 seats, two-year staggered terms, 6.5.1)
- Deputy President prerequisites (3 years good standing, 4 years service, 9.3.4)
- Past President activity rule (3 of the preceding 5 conventions; not 3 consecutive Mid-Years missed, 6.3.1)
- Committee sizes — Credentials 7 (8.11.3), Fundraising 9 at 3 per region (8.5.1), ARFECF Board 15 at 5 per region
- SFC terms (two consecutive three-year terms, one calendar year out; chair two one-year terms)
- ARFECF/AFRP board interlock cap (**no more than 4**, ARFECF Art. V §4)

**Financial controls**

- President discretionary limit ($2,000, **twice per term**) and the budget threshold ($10,000) — 7.2.3, ARFECF §7.3
- Countersignature requirements, per entity and per fund
- Deposit window (2 weeks, ARFECF §10.1)

**Convention**

- Federation share by city tier ($20k / $30k / $40k), the 50/50 fallback, the $10,000 deviation assessment
- Relief Fund levy ($10 per registration) *(since 2 Oct 2026: a term of each host agreement, P13 §2.2; whether it continues is Q-126; in a unified registration it is Q-243; the fund's holding entity is Q-109; P22 §5.3; since 3 Oct 2026 the entity is AFRP, D83)*
- Keynote cost split ($5,000)
- Accounting deadline (**90 days** in the contract, **120 days** in By-Law 10.1.7 — pick one)
- Bid eligibility (50 paid members for 5 consecutive years, 10.1.1)
- Rotation (3 regions, no return within 3 years, selected 2 years ahead)
- Room block (3 days before and after at convention rate)

**Scholarship and endowment**

- Distribution rate (4% programme + 1% administration, or the 5% cap — 6.4.3 vs the Policy Statement)
- Valuation date and averaging basis — **currently unstated anywhere; must be added**
- Report deadline (31 March) and donation acknowledgement SLA (48 hours)

**Structure**

- The region map and the club→region assignment — **two incompatible maps are in force today** (By-Law 10.1.1 vs ARFECF §4.1), which the versioning handles by tagging each election with the map it uses

### Tier 2 — mechanism choices. The system implements several; the ruleset picks.

These are the ones worth building **now**, before the revision lands, because
each is a fork the drafting committee may plausibly take either way. Building
both sides is cheap today and expensive as a retrofit.

| Choice | Options to implement |
|---|---|
| **Vote weighting** | Weighted delegation (9.1.3) · one-delegate-one-vote with an apportionment divisor |
| **When weight is fixed** | At the opening of each question · continuously until the poll closes |
| **Quorum base** | Flat count of members present (current) · fraction of seats · fraction of credentialed delegates · fraction of members |
| **Quorum testing** | Once at opening · continuously through the session |
| **Abstentions** | In the denominator · out of it — **settable per motion type**, because Board polls (6.2.4) and Assembly votes plainly differ |
| **Threshold base** | Votes cast · all seats · all members |
| **Tie break** | Lot (current) · chair's casting vote · re-ballot |
| **Election method** | Plurality (current, 9.2.4) · majority with runoff · ranked |
| **Ballot type** | Secret · recorded and attributed · recorded on demand |
| **Standing across scopes** | Conjunctive — national **and** club (4.3.1 as written) · independent per scope |
| **Complimentary memberships** | Enfranchising · not (the 8.15.4 question) |
| **Dues test** | Postmark · receipt (5.3 and 8.15.5 currently disagree) |
| **Record date** | Fixed calendar date (current) · N days before the meeting |
| **Proxies** | None (current) · delegation weight only · written proxies with revocation |
| **Re-voting** | Permitted until the poll closes · one cast only |

### Tier 3 — structural. Costs real time; say so honestly.

- A voting method genuinely unlike any of the above
- Merging two entities' franchises into a single ballot — relevant, because AFRP amends by **2/3 delegate vote** and ARFECF by **2/3 membership vote**, at meetings held jointly
- A new class of entity in the ledger
- Full written proxies *with* assignment, limits, filing and revocation, if the revision introduces them

### Tier 4 — the integrity floor. Not configurable, deliberately.

These are not policy positions. They are the properties that make a result
defensible, and a system that lets them be switched off cannot certify
anything.

- **The voter↔ballot link is never stored.** No setting exposes it.
- **No interim tallies exist.** Not for administrators, not for testing.
- **The record-date roll is frozen and stored**, never recomputed at tally time.
- **Every governed decision records the ruleset version that governed it.**
- **Refusals name the rule** and the version that produced them.
- **Ties are never broken silently** — the engine reports undecided.
- **The audit trail is append-only.**
- **Vote arithmetic is exact decimal**, never floating point.

If the revision ever requires one of these to bend, that is a conversation, not
a configuration change — and it should be a loud one.

---

## 2. How versioning actually works

Three dates, not one, because they do different jobs:

```
bylaws-2027.1
  adopted    12 Jul 2027   the Assembly voted
  effective   1 Sep 2027   it starts governing
  supersedes bylaws-2012.2
```

**Adoption ≠ effect.** A revision adopted at the July convention that takes
effect with the new membership year gives the office six weeks to prepare and
gives members notice. The gap should be deliberate and stated.

**Non-retroactivity is the load-bearing clause.** Every convention, ballot,
apportionment, certification and disbursement stores the version that governed
it. A 2026 election is evaluated under 2026 rules forever. Ask in 2030 why
Chicago carried 15.6 votes per delegate in 2026 and the answer is *"because
`bylaws-2012.2` said so"* — reproducible from stored data, not reconstructed
from memory.

**The Constitution currently doesn't say this.** Article XI §1 revokes the
previous Constitution "upon adoption", with no effective date and no statement
about decisions already made. Without that sentence, every amendment reopens
every past decision. **This is the single most important thing the revision can
add for the app's sake**, and it is one sentence.

**Rulesets are immutable once anything has relied on them.** Fixing a typo in
a ruleset that has certified an election is not an edit; it is a new version
with a correction note. The old one stays.

**Each entity holds its own.** AFRP, ARFECF and every club get their own
ruleset chain. By-Law 3.1 requires a club's governing laws not to conflict with
the Federation's — so the system can *check* that, and flag a club rule that
contradicts a federation rule at the moment it's entered rather than at the
moment it's disputed.

---

## 3. Schedules, not prose

You asked for flexibility. The way to get it is **not** loose wording — vague
language produces arguments, not flexibility. It's separating the mechanism
from its parameters:

> The body says: *"Delegates shall be apportioned as set out in Schedule A,
> which the Executive Committee may amend on notice to the Chapters."*
>
> Schedule A says: *"One delegate per twenty-five members in good standing, or
> major fraction thereof; minimum one, maximum fifteen; no delegate for a club
> of fewer than ten members."*

Now changing the divisor is an Executive Committee decision on notice, not a
2/3 convention vote — and the constitutional principle that representation is
proportional stays hard to change, which is as it should be.

**Schedules the revision should consider creating:** dues and tiers · the
election calendar · apportionment or weighting parameters · quorum and
thresholds · committee sizes and terms · financial authorisation limits ·
convention shares and levies · the region map · scholarship distribution rates.

Every one of those is Tier 1 in §1. Put them in schedules and the app tracks
them as data, versioned, with no code change and no convention vote.

---

## 4. Refusals carry the citation

A practical detail that matters more than it sounds. Every refusal the system
produces names **the rule and the version**:

> **Not eligible to vote in this ballot.**
> Club membership lapsed 30 Jun 2026; federation standing requires both
> national and club dues current.
> *By-Law 4.3.1 · ruleset `bylaws-2012.2` · assessed at the record date, 28 Feb 2026.*

Three things follow. The member can argue with the *rule* rather than with the
software. The Credentials Committee can see instantly whether a refusal is
correct. And when the revision changes 4.3.1, every refusal that cited it can
be found — so you know exactly who is affected before the change lands.

---

## 5. The drafting workbench

This is the part that makes a revision safe, and it is the piece I'd most want
to build for you.

**The Constitution Committee drafts a ruleset and runs it against real
history.** Not a simulation with invented numbers — last year's actual
certified roll, actual delegations, actual ballots.

What it returns:

- **Delegate weights, before and after**, club by club. *"Under the proposed
  divisor of 25, Chicago goes from 5 delegates carrying 18.00 votes each to 4
  delegates carrying 1 vote each. San Jose loses its seat entirely."*
- **Every motion re-tallied** under both rulesets, with the outcomes that
  **change** highlighted. If a 2026 amendment would have failed under the
  proposed rules, the committee learns that before proposing them.
- **Quorum**, met or not, under each.
- **The members whose eligibility flips** — a count, and a list. *"Making 4.3.1
  conjunctive removes 340 members from the federal roll, of whom 90 are in
  Detroit."* That is the number that decides whether a clause is adopted, and
  today nobody can produce it.
- **A cost badge** on each proposed change: **green** (a parameter),
  **amber** (a mechanism that exists and needs enabling and testing), **red**
  (structural work, with an estimate).

The committee walks into the convention with the consequences quantified. That
is a different quality of debate than the one currently available, and it is
almost entirely a reporting feature over data the system already holds.

**Parallel run during transition.** For the first cycle after adoption, the
system evaluates both the outgoing and incoming rulesets and reports where they
diverge — without acting on the new one. Divergence that surprises people is
caught in a report rather than at a podium.

---

## 6. What I'd like the revision to be explicit about

*Since 2 October 2026:* the research round and P22–P25 found more places where the text is silent or reads two ways. Each is a question, and none is decided here:
- how a club chooses its delegates (9.1.3; Q-37);
- the forfeiture sentence of 10.1.1 (Q-240);
- who signs a payment to a Convention host (11.1.2 against 7.5.1–7.5.2; Q-241);
- the Annual Meeting without a Convention (Q-244);
- the Young Leader Committee's composition (the 8.10 paragraph; Q-179);
- whether 8.13 and 8.14 are seated (Q-251);
- the Magazine's board and the "Manager of the Magazine" (6.7.1, 9.5.2; Q-192, Q-249, Q-250);
- the Federation's representative in Ramallah (Q-246);
- the budget's approval path (Q-234).

Not because the app can't cope otherwise, but because **anything the bylaws
leave unsaid becomes a build decision by default** — and a build decision is a
governance decision made by whoever wrote the code. Which is me, and shouldn't
be.

The full list is in **AFRP-Bylaws-Checklist.md** and the discrepancies are in
**AFRP-Bylaws-Reconciliation.md**. The five that most need a sentence:

1. **Non-retroactivity and an effective date** (§2). One sentence.
2. **Abstentions** — in or out of the denominator, per motion type. Currently
   the software is making this governance decision.
3. **When delegate weight is fixed**, if weighted voting survives.
4. **Conflict of interest** for the scholarship committee — the three-degree
   kinship bar is mine, with no authority behind it, and in a federation
   descended from one community it *will* be challenged. *(Since David's correction of 8 September 2026, recorded in P26 §1.4 and §3.2 (built in slice 4b): the bar is out. Every relationship is disclosed by degree and acknowledged on the record, and only the same household refuses. P26 §3.2 carries it; it is not yet a D-number (Q-273).)*
5. **Whether complimentary memberships vote**, given 8.15.4.

---

## 7. What already works this way

Not a promise — this is built and tested.

- **The dues ladder** is a versioned schedule with an effective date. Changing
  a figure is a data edit; a term keeps the price in force when it was sold; an
  unknown historic date refuses to guess rather than repricing at today's
  rates. Rank is derived from price, so a repricing can't leave it stale.
- **`BylawRuleset`** already exists as versioned data covering eligibility,
  record date, apportionment and quorum — it now needs widening to the Tier 1
  and Tier 2 inventory above, which is the main piece of work this decision
  creates.
- **Certification** stamps a result hash, so a tally can be re-verified later.
- **Ties** already report as undecided rather than resolving silently.
- **Refusals** already carry their reason; adding the ruleset citation is small.

---

## 8. What this decision changes in the plan

| # | Work | Tier |
|---|---|---|
| 1 | Widen `BylawRuleset` to the full Tier 1 inventory | Parameters |
| 2 | Build both sides of every Tier 2 fork | Mechanisms |
| 3 | Ruleset chain per entity — AFRP, ARFECF, each club — with conflict checking against the parent | Structural |
| 4 | Stamp every governed decision with its ruleset version | Integrity |
| 5 | Add the ruleset citation to every refusal | Small |
| 6 | **The drafting workbench and the divergence report** | The valuable one |
| 7 | Parallel-run mode for the transition cycle | Transition |

Item 2 is the one with a deadline attached: each fork is cheap to build **now**
and expensive to retrofit once the other side is assumed everywhere. Item 6 is
the one the Constitution Committee will actually feel.

---

*Design and planning only. Nothing here requires the revision to be finished —
in fact most of it is more useful before it is.*
