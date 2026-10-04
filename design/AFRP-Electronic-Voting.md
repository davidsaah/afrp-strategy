# Electronic voting
### What it changes, what it must preserve, and what the bylaws have to say

**Date:** August 2026
**Decision recorded:** voting will be conducted electronically. Membership tiers and dues figures are provisional and will change.
**Mode:** design and planning. No buildout.
**Since 2 October 2026:** P22 §6 (`AFRP-Convention-Operations.md`) builds the bridge from the certified roll to the floor. Each club's delegation is a dated act with its method stated (the text, 9.1.3, is silent on how delegates are chosen; Q-37), and presence is marked at the desk. Where an Annual Meeting is held without a Convention is Q-244. The "CPA" of 9.2.1–9.2.3 is the by-law's custodian of mailed ballots. It is a different question from which of the Federation's four "CPA" roles the record means elsewhere (Q-231).

---

## 0. The short version

Electronic voting is the right call, and it makes one thing *better* that I had
recommended replacing. But it moves the hardest problem from **counting** to
**knowing who the voter is** — and that problem is currently sitting in a
different part of the project labelled "data quality."

Three things follow, in order of how much they matter:

1. **Identity resolution becomes election infrastructure.** On paper, a ballot
   goes to an address. Electronically it goes to an *identity*, and AFRP today
   has five to seven unlinked identities per member. A duplicate record is a
   double vote. A stale email is a disenfranchised member. The merge queue is
   now on the critical path to a lawful election.
2. **By-Law 9.2 has to be rewritten, not reinterpreted.** It mandates a
   physical process in detail — envelopes, postmarks, custody. None of it
   survives. I've set out below exactly which clauses fail and what has to
   replace them.
3. **The receipt design I proposed is wrong and would enable vote-buying.**
   Correction and fix in §4.

And one welcome consequence: **electronic voting rescues the weighted delegate
scheme.** I'd suggested replacing By-Law 9.1.3 with conventional apportionment
partly because fractional, continuously re-dividing vote weights are miserable
to run on paper. Electronically they're free. That argument for replacing 9.1.3
is now gone.

---

## 1. What the current bylaws require, clause by clause

By-Law 9.2 doesn't describe *an election*. It describes **a specific physical
procedure**, in a level of detail that leaves no room to substitute another
one. Each clause fails differently.

| Clause | What it requires | Under electronic voting |
|---|---|---|
| **9.2.1** | Within 30 days of the certified list, Election and Credentials Committees **jointly** send each certified member a ballot form and a pre-addressed return envelope, addressed to a CPA or independent agency chosen by the Election Committee | **Fails.** Replace with issuance of a voting credential. Keep the *joint* act and keep the independent agency — those are trust mechanisms, not clerical ones |
| **9.2.2** | Member marks one choice, inserts it in an envelope labelled "BALLOT", places that in a larger envelope, mails it to reach the CPA **postmarked no later than June 20**. Envelopes and inserts **numbered** as the Election Committee designates | **Fails entirely.** The double envelope is a secrecy mechanism — the outer carries identity, the inner carries the vote, and they are separated before opening. Its digital equivalent is not optional (§4) |
| **9.2.3** | Sealed envelopes kept **intact** with the CPA, turned over to the Election and Credentials **Chairpersons** on written request, **not opened until election day** at the Convention | **Preserve exactly.** This is the single most important property and the easiest to lose. See §5 |
| **9.2.4** | Highest number of votes wins **irrespective of percentage or number of candidates**. Tie broken by **a draw from a bag** under the Election Committee | Survives unchanged. Plurality, and a genuine physical lot — do **not** replace the bag with a random number generator (§6) |
| **9.2.5** | A ballot showing a vote for more than one candidate is **disqualified and not counted** | Becomes near-dead letter, because the interface should prevent it. But keep a deliberate **blank/abstain** path — see §7 |

**A drafting bug that electronic voting happens to fix.** As written, ballots
may lawfully be issued as late as 24 June (30 days after the 25 May certified
list, per 8.11.2) but must be returned postmarked by **20 June**. The election
is impossible to run inside its own rules. Electronic voting dissolves this,
because there is no mailing lag — but the revision should still replace the
"within 30 days of receiving the list" construction with **a fixed date**.
Anchoring one committee's deadline to another committee's act is how this
happened in the first place.

**What must be added, because paper made it implicit:**

- **When the poll opens and closes**, as a date *and time* with a stated time
  zone. "Postmarked by June 20" was doing this work; nothing replaces it
  automatically. A federation spanning Pacific to Eastern needs the time zone
  written down.
- **What happens if the system is unavailable** at the close. Paper had the
  postal service as a shared excuse; software needs a stated extension rule
  decided *before* anyone knows who is ahead.
- **Whether a cast vote can be changed** before the poll closes. Paper answers
  this implicitly — you posted it, it's gone. Electronic systems can allow
  re-voting (it's a real defence against coercion: vote again privately later).
  Either answer is defensible; silence is not.

---

## 2. Identity is now the franchise

This is the part I'd most want AFRP to sit with.

Under 8.11, the Credentials Committee certifies **who may vote**, and under
9.2.1 the ballot goes to that person **at an address**. If the address is
wrong, the member notices, complains, and it gets fixed — the failure is
visible and recoverable.

Electronic voting replaces the address with an **authenticated identity**, and
that changes the failure modes:

| Failure | On paper | Electronically |
|---|---|---|
| Duplicate member record | Two ballots to one household — usually noticed | **Two votes.** Silent |
| Stale contact detail | Returned mail, gets fixed | **Disenfranchisement.** A bounced email looks like a member who chose not to vote |
| Shared household email | Two ballots, two envelopes, two signatures | **One person votes twice**, which is precisely what 8.15.4 and 9.4.3 exist to prevent |
| Member changes email mid-cycle | Irrelevant | Credential delivery fails at the worst moment |

AFRP's members currently exist as separate, unlinked records across WordPress,
Dynamics/Power Pages, Mailchimp, Breeze at each club, Authorize.Net and the
Google-hosted family tree. The platform's identity resolution work — the
weighted matcher, the review queue at Ops 03 — was scoped as a data-quality
improvement with a nice payoff. **It is now an election-integrity control**,
and it should be treated, staffed and audited as one.

Three consequences for the design:

1. **The certified roll must be a roll of *resolved persons*, not of records.**
   Certification under 8.11 should not be possible while unresolved
   probable-duplicates remain in that person's cluster. The Credentials
   Committee gets a new refusal reason, and it should name the rule.
2. **Every certified member needs one verified, individually-controlled
   contact.** Not a household address — an address that belongs to *them*. This
   is a membership-data campaign that has to run **before** the first
   electronic election, and it's the kind of thing the magazine is unusually
   good at driving.
3. **Deliverability has to be measured and reported.** "We issued 3,100
   credentials, 2,840 were confirmed delivered, 260 could not be reached" is an
   election-integrity figure. It belongs in the certification report to the
   General Assembly under 8.11.3, not in an ops dashboard nobody reads.

---

## 3. Nobody is left behind, or it isn't legitimate

The Council of Past Presidents is, by construction, the oldest cohort in the
federation — and under 6.3.1 its members' voting status already depends on
attendance. An election that is difficult for them to participate in is not a
technical problem; it is a legitimacy problem, and it will be argued as one.

**Recommendation: electronic by default, paper on request, one tally.**

- A member may request a paper ballot by a published date, and the request
  itself is recorded on the certified roll so nobody can be issued both.
- Paper ballots are received by the same independent agency, and are entered
  into the same sealed box before opening. There is **one count**, not "the
  electronic result plus the paper ones."
- The request deadline is early enough to mail and return; that constraint
  should set the poll-open date, not the other way round.

**Assisted voting needs an explicit boundary.** Some members will need help.
By-Law 9.4.3 makes paying someone's dues in exchange for their vote grounds to
disqualify *the member, the votes and the candidate* — the bylaws already take
vote-influence seriously. The revision should say plainly: a person may assist
a member in operating the system; a person may **not** be given a member's
credentials to vote on their behalf. And the system should never build a
"vote for someone else" path, however convenient it looks — it institutionalises
exactly the thing 9.4.3 forbids.

---

## 4. The receipt design I proposed is wrong

**Correction.** Throughout the earlier work I described the voter getting *"a
one-time receipt to verify their own vote"*, with the note that a lost receipt
cannot be reissued. The non-reissuable part is right. The rest is a mistake.

**A receipt that proves *how you voted* is a vote-buying instrument.** If Nadia
can show someone a receipt reading "you voted for X", she can be paid — or
pressured — to produce it. On paper this was impossible, which is why nobody
had to think about it. Electronically it is the default unless designed out.
The property wanted is **receipt-freeness**, and it is not a detail.

**What the receipt must do instead:**

- Prove the ballot **is in the box** and has not been altered or dropped.
- Prove **nothing about its contents** — to the voter's family, to a candidate,
  to a committee member, or to anyone the voter might want to prove it to.

Concretely: the receipt is a token that lets the voter confirm inclusion
against the published ballot record after the count, and that is all. The voter
knows what they chose; the receipt doesn't corroborate it to a third party.

The double-envelope in 9.2.2 was doing this job all along — the outer envelope
carried identity for eligibility checking, the inner carried the vote, and the
two were separated before any envelope was opened. **The digital design has to
reproduce that separation, not merely promise it.** The engine already refuses
to store the voter↔token link; the receipt has to be held to the same standard.

---

## 5. Custody: keep the CPA, give them something real to hold

By-Law 9.2.3 gives the ballots to a CPA or independent agency, keeps them
sealed, and releases them only to the Election and Credentials **Chairpersons
jointly**, and only on election day. The instinct with electronic voting is to
drop the CPA as a relic of paper handling. That would be a mistake: their role
is **trust**, not arithmetic, and trust is the scarcer commodity.

**Proposal — joint custody, reproduced digitally:**

- Ballots are sealed to a key **split three ways**: Election Committee chair,
  Credentials Committee chair, and the independent agency. **Any two** can
  open; **no one alone** can. That mirrors 9.2.3's joint release and it means
  no single person — including whoever administers the platform — can look
  early.
- **Nothing is decryptable before the announced opening.** Not by staff, not by
  the Executive Director, not by me, not by a database administrator. If an
  interim tally is technically visible to *anyone*, it will eventually be
  visible to someone with an interest in it.
- **No interim counts of any kind.** Turnout is fine and useful; standings are
  not. The system should be incapable of producing a partial result, not merely
  configured not to.
- At the count, the agency **attests** to the sealed box: how many ballots, the
  seal intact, the roll matching the certification. The published result
  carries a **result hash** so the tally can be re-verified later by anyone —
  which the certification engine already produces.
- The audit trail records **who opened, when, and with which two keys.**

This gives the CPA a genuinely stronger role than counting envelopes, and it
gives a losing candidate something to check rather than something to allege.

---

## 6. Keep the bag

By-Law 9.2.4 and 8.12.1 break ties by **a draw from a bag**, under the Election
Committee Chairman. Every instinct in software says replace this with a seeded
random number and a published seed.

**Don't.** A tie is rare, consequential, and watched by a room full of people
who care. A physical draw in front of them is *verifiable by everyone present
without trusting anything* — which no random number generator can offer, however
sound the mathematics. The system should report the result as **undecided and
tied**, name the rule, and hand it to the chair. The engine already refuses to
break ties silently; that behaviour is correct and should stay.

---

## 7. Small things that stop being small

**Over-votes (9.2.5).** The interface should prevent selecting two candidates,
which makes the disqualification clause near-dead. But **do not remove the
voter's ability to cast a deliberate blank.** A member who turns up and
declines to choose is making a real statement, and on paper they could. If the
only paths are "pick someone" or "don't vote", the system has quietly abolished
a choice the bylaws allowed. That also matters for the abstention question — a
blank ballot and a non-voter must be distinguishable in the record even if they
are treated the same in the threshold.

**Weighted delegate voting (9.1.3) becomes practical.** *(Since 2 Oct 2026: P22 §6 reads "sent" as present at the desk's check-in, so only a present delegate carries a weight and only a present certified member may extract. When weights fix is still D5.)* Each delegate carries
`certified members ÷ delegates sent`, and any certified member present may
extract their own vote, re-dividing the rest. Chicago with 90 members and 5
delegates: 18.00 votes each; twelve members extracting drops it to 15.60. That
arithmetic is unpleasant on paper and trivial live on screen, with the current
weight shown to the room. **The bylaws must say when the weight is fixed** —
at the opening of each vote, or continuously until the poll closes. Continuous
re-division means a member extracting mid-vote changes the weight of ballots
already cast, which is not survivable. Recommend: **fixed at the opening of
each question**, extraction closing a stated interval before.

And the arithmetic must be **exact decimal, never floating point.** 90 ÷ 7 is
not representable in binary, and a certified result that fails to reconcile by
$0.000001 of a vote is a result somebody will litigate.

**Recorded votes.** The bylaws give no delegate the right to demand one. On
paper that was a cost decision — recorded votes are laborious. Electronically
they're free, so the revision can now afford to grant the right. Worth deciding
deliberately: officer elections stay secret (9.2), but bylaw amendments and
resolutions could reasonably become attributable, which is the ordinary
convention and improves accountability to clubs.

**Quorum in real time.** 10.1.5 sets a flat **25 paid members**. Electronically
that is continuously observable — which raises a question paper let everyone
avoid: is quorum tested **once at the opening**, or **continuously**? These
behave very differently late on the second day, and the answer should be in the
revision rather than discovered during a contested vote.

**The calendar compresses.** The Nov 1 → Dec 31 → Feb 28 → May 10 → May 25 →
Jun 20 sequence exists largely to accommodate postal lag and manual
list-keeping. Most of the slack can go. I'd keep **28 February** as the dues
deadline regardless — it is the substantive rule about who is a member, not a
processing artefact — and compress everything after it.

---

## 8. What must not be built

Stated explicitly, because each of these is the kind of thing that gets added
later as a convenience and is very hard to remove:

- **No administrator who can see interim results.** Not read-only, not "for
  monitoring", not for me during testing.
- **No reissuable receipts.** A receipt that can be regenerated is a receipt
  that can be regenerated *for someone else*.
- **No vote-on-behalf-of path.** See §3 and 9.4.3.
- **No content-revealing receipt.** See §4.
- **No email-only authentication for a contested office.** Email accounts are
  shared, forwarded and compromised more often than anyone admits, and in this
  federation they are frequently household accounts.
- **No silent handling of an unresolved duplicate.** It refuses, and it names
  the rule.

---

## 9. Dues and tiers are versioned data now

The second decision — that the figures will change — has been applied.

The ladder is no longer constants in code. It is a **versioned schedule with an
effective date**, exactly like the bylaw rulesets:

```
dues-2026.1 · effective 1 Sep 2026        (the membership year, By-Law 5.1)
  student $25 · individual $90 · family $150 · manar $500 · patron $1,000 · life $0
```

Three properties, each with a test behind it:

- **Changing a figure is a data edit, never a code change.** A repricing is a
  *new schedule with a later effective date*, and the old one stays.
- **A term keeps the price in force when it was sold.** The same wedding
  evaluated under the 2026 ladder and a 2028 ladder produces different amounts
  and *identical* grants — repricing changes what things cost, never who gets
  what.
- **Rank is derived from price, so it cannot go stale.** "Never downgrade
  someone as a reward" depends on which tiers outrank Family. If Manar were
  ever repriced below Family, it stops being protected automatically, with
  nobody having to remember to edit a list. Life stays protected regardless of
  its $0 price, because it is marked perpetual rather than expensive.
- **An unknown historic date refuses to guess.** Importing a 2011 membership
  throws rather than repricing it at today's rates. Historic terms carry the
  amount actually paid.

This matters more than it looks. By-Law 5.1 makes dues an **annual** decision —
recommended by the Board at the Mid-Year Meeting, approved by the General
Assembly at the Annual Meeting. A structure that requires a developer every
time the Assembly votes is a structure that will be worked around within two
years.

**Still open:** the Life and Student figures; whether Family is a per-household
or per-person rate (the wedding benefit's economics turn on it); and — the
larger question — **which document authorises the ladder at all**, since none of
these tiers appear in the Constitution or By-Laws, which know only Regular and
Associate membership.

---

## 10. What this changes in the build

| # | Change | Why |
|---|---|---|
| 1 | Rewrite By-Law 9.2 in the revision | The current text mandates envelopes and postmarks |
| 2 | Promote identity resolution to an election control, with certification blocked on unresolved duplicates | §2 |
| 3 | Verified individual contact for every certified member, with a delivery report into the 8.11.3 certification | §2 |
| 4 | Paper-on-request path, single tally | §3 |
| 5 | **Rebuild the receipt to prove inclusion, not content** | §4 — corrects an error in the earlier design |
| 6 | Three-way split custody, no interim tallies, agency attestation | §5 |
| 7 | Exact-decimal weighted delegate votes, weight fixed at question open | §7 |
| 8 | Deliberate blank distinct from non-voting | §7 |
| 9 | Poll open/close as datetime with time zone; stated outage rule; re-vote decision | §1 |
| 10 | Dues as versioned schedules | §9 — **done** |

Items 1–4 are prerequisites to a first electronic election. Item 5 is a
correction. Items 6–9 are design decisions the revision should settle.

---

## 11. For the Legal Advisor

By-Law 7.8.1 makes the Legal Advisor the Chief Legal Officer, available to the
Board and the General Assembly, and this is squarely their question. AFRP and
ARFECF are both **Michigan non-profit corporations** (Const. I §3; ARFECF Art.
I §3), so the governing statute and the bylaws together decide what's
permissible. Worth putting to them before the revision is drafted:

1. What does Michigan law require for **electronic voting and remote
   participation** by a non-profit's members, and what must the bylaws say to
   authorise it?
2. Does an electronic ballot satisfy the **secret ballot** requirement, and are
   there record-retention obligations for the sealed ballots and the audit
   trail?
3. Is **notice by email or website** sufficient? The Constitution currently
   requires amendment notice **published in the Magazine** and sent to Chapters
   (Const. XI §3), and convention notice printed in the Magazine (10.1.4).
   ARFECF already permits website notice (Art. IX §2) and AFRP does not — so
   the two entities differ today, at meetings held jointly.
4. Can the **two entities' different franchises** — AFRP amends by 2/3 delegate
   vote, ARFECF by 2/3 membership vote — be run in one electronic session
   without confusing the record?

---

*Design and planning only. Reflects two decisions taken: voting will be
electronic, and the dues ladder is provisional. §4 corrects an error in the
earlier design.*
