# The bylaws, read against the design
### What the documents actually say, what conflicts, and what I need from you

**Date:** August 2026
**Sources:** AFRP Constitution & By-Laws (approved 28 Jun 2009 San Francisco, amended 5 & 7 Jul 2012 Orlando) · ARFECF By-Laws (clean version, 12 Jan 2013) · ARFECF Scholarship Fund Policy Statement & Guidelines (revised 2015 Chicago Convention) · Final Convention Contractual Agreement (BOD approved 24 Jun 2009)
**Mode:** design and planning. No buildout.

---

## The headline

**The voting model I built is wrong, and the bylaws are clear about it.**

I built one-delegate-one-vote with an apportionment divisor, rounding, a floor
and a cap — the standard federated-convention pattern. By-Law 9.1.3 describes
something quite different:

> *"Each club or community shall have the right to send to the Convention a
> delegation consisting of one or more delegates. Each delegate will
> independently cast a proportionate number of votes equaling the total number
> of certified members from his/her Chapter Club divided by the number of
> delegates sent to the Convention; However, any certified member attending the
> Convention shall have the option to cast his/her vote independently in which
> case, his/her vote shall be deducted from the number of votes cast by the
> delegates representing his/her community."*

That is **weighted, fractional delegate voting with member extraction**. There
is no divisor, no rounding rule, no minimum club size, and no cap on
delegates — a club sends as many delegates as it likes and the weight simply
divides across them. Worked example:

```
Chicago · 90 certified members · sends 5 delegates
  each delegate carries          90 / 5      = 18.00 votes
12 Chicago members attend and vote independently
  delegate pool                  90 − 12     = 78
  each delegate now carries      78 / 5      = 15.60 votes
  Chicago total voting power     78 + 12     = 90   (capped by 9.1.4)
```

Three consequences for the build:

1. **Vote weights are fractional.** Tallies cannot be integers. The engine
   currently counts ballots; it needs to sum weights, and the bylaws say nothing
   about rounding, so the arithmetic must be exact (decimal, not float) and the
   rounding question has to be answered.
2. **The delegate weight is not fixed until the floor closes.** Every member who
   walks up and votes independently re-divides the delegation's weight. The
   credentialing screen I designed (Ops 04) shows a static seat count; it needs
   to show a live weight that moves.
3. **`apportionSeats()` has no basis in the bylaws** and should be deleted or
   rewritten unless the revision introduces apportionment.

There are also **three distinct voting modes**, not one:

| Mode | When | By-Law |
|---|---|---|
| Voice vote or show of hands | everything not listed below | 9.1.2 |
| Weighted delegate vote | 15% of polled delegation chairs request it · contested elective offices and convention city · Constitution and By-Law amendments | 9.1.1 |
| Mailed secret ballot to every certified member, counted by an outside CPA | Deputy President only | 9.2 |

**Deputy President is not a floor election at all.** Ballots are mailed to each
certified member individually, returned to a Certified Public Accountant or
independent agency, held sealed, and opened on election day at the Convention.
Plurality wins "irrespective of the percentage of votes or the number of
candidates" (9.2.4). Over-votes are disqualified (9.2.5). Ties are broken **by
a draw from a bag** under the Election Committee Chairman (9.2.4, and 8.12.1
for other offices).

So there are two electorates operating at the same convention: one member one
vote by mail for Deputy President, and weighted club delegations on the floor
for everything else. The platform currently models neither.

---

## The election calendar is the real governance engine

The bylaws don't have a record date in the "N days before the meeting" sense I
assumed. They have a fixed annual calendar with seven hard dates:

| Date | What | By-Law |
|---|---|---|
| **Nov 1** | Deputy President candidates postmark written intention to Credentials. Later = not considered | 9.3.4(3) |
| **+15 days** | Board at Large evaluates and approves the applicant by simple majority | 9.3.4(3) |
| **Dec 31** | Credentials certifies candidate eligibility | 9.3.4(3) |
| **Feb 28** | Dues **received** by General Treasurer to vote for Deputy President (5.3) · applications **postmarked** to the Membership Committee, else not certified for Deputy President, Board at Large, Scholarship Committee or Executive Committee (8.15.5) | 5.3, 8.15.5 |
| **May 10** | Membership Committee furnishes alphabetical lists per community to Credentials, Election Committee, Executive Assistant; applications handed to Credentials | 8.15.6 |
| **May 25** | Credentials sends certified lists to Election Committee and Executive Secretary | 8.11.2 |
| **Jun 20** | Ballots postmarked to the CPA | 9.2.2 |
| Aug 1 | Chapter Clubs file the annual affiliation form | 3.2 |

**These dates contain a genuine contradiction.** By-Law 9.2.1 says ballots go
out "within 30 days after receiving the list of certified membership." The
certified list arrives 25 May (8.11.2), so ballots may lawfully be mailed as
late as **24 June** — four days *after* the 20 June return postmark deadline.
The election can be conducted entirely within the rules and still be
impossible. If ballots are keyed to the 10 May membership list instead, the
window is 11 days, which is tight but workable.

**This should be fixed in the revision.** I'd suggest anchoring the mailing
deadline to a date, not to a duration after another committee's act.

A second, smaller one: 5.3 says dues must be **received** by 28 February;
8.15.5 says applications must be **postmarked** by 28 February. Software has to
apply one test. Postmark and receipt routinely differ by a week, and the
difference decides who votes.

---

## Good standing is conjunctive — and it breaks my demo narrative

By-Law 4.3.1:

> *"A member in Good Standing is one that adheres to and complies with the
> Constitution and By-Laws of the A.F.R.P., and has paid his/her AFRP **and
> Local Club (if any)** current membership year Annual Dues."*

Federation good standing therefore **requires local club dues to be current**
wherever a club exists. That is not what I built, and it is not what the
mockups show. The member document follows Nadia Khoury, a national Patron in
good standing and a lapsed Detroit Club member, and lets her vote federally
while paying the non-member rate at her own club's dinner. **Under 4.3.1 she
would not be in good standing at all**, and would not vote federally either.

The two-scope independent-lapse model is still right as *data* — the
memberships genuinely are separate, with separate money and separate lapse
dates. What changes is the *derived* answer: good standing is an AND across
scopes, not a per-scope property. That is a contained change to
`standingAt()`, but it changes the story every screen tells.

Related: the membership year runs **1 September – 31 August** (5.1) while the
fiscal year runs **1 June – 31 May** (8.7.2). The two are offset by three
months and the 28 February voting deadline sits in the middle of both. Any
"members in good standing" number depends on which calendar the question means.

---

## Membership categories: the bylaws know only two

Constitution VII and By-Laws Article IV recognise **Regular Membership** (age
18+, Ramallah ancestry as defined in Aziz Shaheen's book *Ramallah*, or married
to someone with such ancestry) and **Associate Membership** (special
circumstances, Board majority on Membership Committee recommendation,
**non-voting**).

That's it. There is no Life, Patron, Manar, Family, Student or complimentary
tier anywhere in the Constitution, the By-Laws, or the ARFECF documents. The
whole tier structure in the design presumably lives in Board Rules and
Regulations under 6.2.1 — which I have not seen.

This matters because of **By-Law 8.15.4**:

> *"The only dues to be accepted as valid for purposes of voting are those that
> are paid by credit card, check or money order from the applicant's personal or
> business fund…"*

reinforced by 9.4.3 and 9.5.5, which prohibit paying dues on behalf of others
outside one's own family and treat dues-for-votes as grounds for disqualifying
the membership, the votes and the candidate.

**A comped membership pays no dues from the applicant's own funds.** So the
free newlywed Family year and the free scholarship student membership — both of
which I designed to confer standing and therefore a vote — appear to be
unenfranchising under a plain reading. Either they don't vote, or the revision
needs a clause saying complimentary memberships granted by the Federation are
deemed validly paid.

Note also **5.2**: convention registration includes annual dues for qualifying
registrants, and **dues are waived for full-time college students under 26 with
photo college ID**. That's a fourth path to membership I hadn't modelled, and
it collides with the same 8.15.4 question.

Two conflicting family definitions sit in the same document:

- **8.15.8** — "Household is defined as husband and/or wife and unmarried children over the age of 18."
- **9.5.5** — "families to mean husband and wife, their children and their spouses."

The first excludes married children and (as literally written) children under
18; the second includes children's spouses. `canActFor()` currently permits
household adults to act for one another on a consent model. It needs a
**payment-source rule** it doesn't have: who may lawfully pay whose dues, which
is a narrower question than who may act for whom.

---

## Attendance is a voting qualification

By-Law 6.3.1 — to remain an **active voting** member of the Council of Past
Presidents, a Past President must attend **three of the preceding five
Conventions** and must not miss **three consecutive Mid-Year Meetings**. The
President compiles the eligible list annually; it is printed in the Annual
Committee Directory under "Board members eligible to vote." Removal is
automatic; reinstatement requires a petition and **2/3 Board approval**.

This is the first place in the documents where **event attendance history is a
governance input**. The platform will hold convention and mid-year check-in
data (Member 09, Ops 13) — so it can compute this list exactly, which today is
compiled by hand and is the sort of thing that gets argued about. Good feature;
it just needs the attendance record to go back five years, which means historic
convention attendance is worth importing alongside the scholarship history.

---

## The Board's size is derived, and that makes "2/3 of the Board" hard

By-Law 6.2.2 composes the Board as: all **active** Past Presidents + all
Chapter Club Presidents *from clubs that filed their affiliation form* (6.4.1,
3.2) + 4 Members At Large + the Executive Committee + 1 RBPN + 1 Magazine + 1
Ramallah Foundation. Non-voting: Executive Director, Executive Assistant.

So the denominator floats with the number of active Past Presidents and the
number of compliant clubs. That matters because several thresholds are **2/3 of
all members of the Board**, not two-thirds of votes cast:

- Board Rules and Regulations — 6.2.1
- Past President reinstatement to active voting — 6.3.1
- ARFECF Rules and Regulations — ARFECF Art. V §3
- Amendments to EFund and Scholarship Committee policies — ARFECF 6.3.6, 6.4.6

Combined with 6.2.4 — *"Board members who do not reply to the poll within the
time prescribed shall be considered to abstain"* — **a non-reply functions as a
No** on any 2/3-of-all-members question. That is a real and probably
unintended effect, and it's exactly the abstention question the checklist
flagged. The engine currently excludes abstentions from the denominator
globally; it needs to be **per motion type**, because the Board polls and the
Assembly votes behave differently.

One more: 10.3.1 sets no Board quorum at all — *"A majority of those present
(in person or otherwise) shall be needed to discuss and transact Federation
business."* Three people present can transact business by two votes. Meanwhile
"or otherwise" and the ARFECF's explicit electronic-attendance clause (Art. VII
§4) mean **remote attendance counts as presence**, which the platform should
record as such.

And the Annual Meeting quorum (10.1.5) is a **flat 25 paid members**, expressly
"regardless of the percentage of members present, or delegates holding votes of
absentee members." My engine models quorum as a fraction of a base. It should
be a fixed count.

Worth noticing what that combination permits: 25 people in a room, casting
weighted delegate votes on behalf of the entire certified membership, can amend
the Constitution by 2/3. That may be intentional. It may also be worth the
revision looking at.

---

## Two region maps are in force at once

**AFRP By-Law 10.1.1** (used for convention rotation and for the 9-member
Fundraising Committee, 3 per region on staggered 3-year terms):

- Region 1 — San Francisco, San Jose, San Diego, Los Angeles, **Houston**
- Region 2 — Detroit, Chicago, Cleveland, New York, Louisville/Lexington
- Region 3 — Jacksonville, Birmingham, **Knoxville**, Washington D.C.

**ARFECF §4.1** (used to seat 5 board members per region):

- West — San Diego, LA, San Jose, San Francisco, **Santa Rosa** + Pacific-time individual members
- Central — **Houston**, Chicago, Detroit, Cleveland, Louisville, Lexington, **Knoxville** + Central-time individual members
- East — NY, Washington, Jacksonville, Birmingham, **Atlanta** + Eastern-time individual members

Houston and Knoxville are in different regions depending on which election you
are running. Louisville/Lexington is one unit federally and two in ARFECF.
Santa Rosa and Atlanta exist in ARFECF and not in the AFRP list. And both lists
are stale against the 26 clubs you have today.

The ARFECF map also assigns **unaffiliated individual members to a region by
time zone**, which the AFRP map does not — so an unaffiliated member has a
region for one purpose and none for another.

The platform can hold both maps as versioned data and tag each election with
the map it uses. That works. But it should be a deliberate choice, not a
silent one.

---

## The convention contract is a module I haven't designed

The Convention Contractual Agreement is operationally dense and almost none of
it is in the mockups.

**Money.** The Federation's share is fixed by city tier — **$20,000** from San
Jose, Cleveland, San Diego, Knoxville, Birmingham, New York; **$30,000** from
Chicago, Houston, Washington D.C.; **$40,000** from Detroit, San Francisco,
Jacksonville. If that breakdown isn't adhered to, Federation and host **split
net income 50/50**. Membership dues and Relief Fund collected at the convention
are **separate and additional**. **$10 of every registration** goes to the
Relief Fund. Deviation from the agreement without written consent is a
**$10,000** assessment. The host runs its **own checking account** and must not
use the AFRP Federal ID. A **host-city CPA** certifies the final report and the
finding is **binding on both parties**, with the Federation free to retain its
own auditor. Los Angeles and Louisville/Lexington appear in the region list but
**not in the tier schedule**.

**Agency, stated explicitly.** The host city "is acting as an **agent of the
Federation** and as such, all records and other documentation pertaining to the
membership, registration and Relief Fund are the **property of the
Federation**." Separately, By-Law 11.1.5 requires that all funds raised by a
club for a sponsored project be routed **through Federation headquarters** and
then forwarded on.

That's clean agency language and it settles part of the ledger question — but
it points the *opposite* way from club dues. Convention dues and Relief Fund
collected by a host are Federation property held by an agent; project funds
routed through HQ are a pure conduit; club dues, on your instruction, belong to
the club. The multi-entity ledger needs all three treatments, distinguished at
the fund level rather than assumed per entity.

**Deadlines conflict.** By-Law 10.1.7 requires final accounting to the AFRP
office **no later than 120 days** after the Convention. The contract requires
all financial records **within 90 days**. Both are in force.

**Operations the platform would have to run.** Numbered tickets for every paid
function, accounted for. Professional security restricting admission to
registered persons, with the signed contract filed with the Federation and the
hotel fire alarm verified active one week prior. A hotel block covering **3
days before and 3 days after** at convention rate. Early-bird registration with
a 30-day cutoff and a post-deadline penalty. Ad book sales, one copy per
registered family plus a copy to every half-page-and-up advertiser not
attending, and a bar on soliciting ads outside the host community. Mandatory
youth program. Head table and reserved table seating with a named list.
Entertainment capped at four nights, banquet program at 60 minutes. Keynote
costs split at **$5,000** — host below, Federation above. Duplicate receipts
for all monies. And **30 days before the Convention the General Treasurer sends
the host a list of members whose dues are paid** (5.2), which is a
reconciliation handshake between two systems on a fixed clock.

**Bidding is checkable from data you'll already hold.** A bidding city needs
**at least 50 paid members for at least 5 consecutive years** (10.1.1), the bid
must be in writing by the Mid-Year Meeting, the site is chosen **two years in
advance** by the general membership, rotation runs through the three regions, a
convention **cannot return to a region within three years**, and a region that
declines its turn **forfeits until the next rotation**. That is a constraint
solver over membership history, and the platform can answer "who is eligible to
bid for 2030" exactly.

---

## The scholarship documents change the spending model

**The spend rate is not what I built.** The Scholarship Fund policy is:

> **4%** of all Assets annually for scholarships and educational purposes, plus
> **1%** of all Assets to AFRP as compensation for administering ARFECF —
> together the "Annual Distributions", which are **mandatory** and made between
> 1 June and 31 May.

ARFECF By-Law 6.4.3 states the same 5% differently: annual expenditures
"limited in each year only to five (5%) percent of all assets and income
derived from the investment of the corpus." **One document sets a mandatory
floor, the other sets a cap.** They agree on 5% in total but not on whether it
must be spent, and not on the basis — "all Assets" versus "all assets and
income derived from the investment of the corpus."

My `endowedSpendable()` applies a spending rate to a trailing average of fund
value, which is standard endowment practice and **is not what either document
says**. Neither document states a valuation date or an averaging period. That
is a real gap: 4% of assets on 31 May and 4% of assets on 1 June can differ by
a lot, and nothing says which one governs.

The same 5% limit applies to the Endowment Fund (6.3.3), whose named purposes
include **Ramallah Charitable Institutions, Project Hope, the Leadership
Program, and Internships in Washington** — programs still on my open list.

**Committee composition doesn't reconcile.** Three mechanisms describe the same
seats:

- The Policy Statement body: at least 9 members — Chairman selected by the ARFECF President, the ARFECF Executive Director, and **8 at-large chosen by the ARFECF Board** (that totals 10).
- The Policy Statement's own parenthetical note: *"Three (3) Scholarship Committee Members are now elected at the Annual Convention since 2015."*
- ARFECF Art. V §4: the ARFECF President appoints each Committee Chairman and **the Board appoints the other members**.

And AFRP 8.15.5 lists "Scholarship Committee" among the positions for which
members must be certified to vote — consistent with election, inconsistent with
appointment. Someone needs to say how many are elected, how many appointed, and
by whom.

**Terms and disqualifications are clear and buildable:** up to two consecutive
three-year terms, then **a full calendar year off** before returning; the
Chairman is limited to two consecutive one-year terms; **paid employees of
ARFECF or AFRP may not vote**; all actions by majority of members eligible to
vote. Geographic spread is directed but not quantified — "particular
consideration" to representing all regions and avoiding concentration in one
city, which is a soft preference the software can surface but not enforce.

**Conflict of interest: the documents are silent.** Not a word, in any of the
four. My three-degrees-of-kinship rule — blocking a reviewer related to an
applicant within three degrees via the family tree, disclosing beyond that — is
**entirely a build decision with no governing authority**. In a federation
descended from one ancestral community, that is precisely the rule that will be
challenged the first time someone doesn't get an award. It needs to be adopted
by the SFC or written into the revision.

**Two duties in the policy are software requirements I hadn't designed:**

1. **Thank-you letters within 48 hours** of receiving any donation, stating tax
   deductibility **and any conditions imposed by the donor**. That's an
   automation with a hard SLA, and it means donor restrictions must be captured
   structurally at the moment of the gift, not written in a memo field.
2. **An annual report of all donations for the previous year published by 31
   March**, with a statement listing distributions made. A fixed reporting
   deadline the system can produce rather than assemble.

Plus: *"The SFC shall follow up on students to ensure that they are maintaining
the required academic credentials"* — which is the verification loop I built,
now with a mandate behind it. The required credentials themselves are not
stated anywhere.

---

## The entity map is bigger than I modelled

I built AFRP plus separately incorporated clubs. The documents describe at
least five kinds of entity:

| Entity | Status | Relationship |
|---|---|---|
| **AFRP** | Michigan non-profit, IRS-recognised | The Federation |
| **ARFECF** | *Separate* Michigan non-profit (Const. III §4, amended 5 Jul 2012) | Day-to-day management by AFRP staff for an annual fee; **1% of assets** paid to AFRP |
| **Ramallah Foundation, Inc.** | *Separate* legal entity, own mission and constitution (Const. III §3) | Appoints 1 member to the AFRP Board |
| **Hathihe Ramallah Magazine** | Operates **independently**, own editorial staff, own board, own subscription management (Const. III §2, By-Law 6.7.1) | AFRP "shall appropriate the necessary funds to guarantee its publication"; appoints 1 member to the AFRP Board |
| **26 Chapter Clubs** | Separately incorporated, own governing laws | Must not conflict with AFRP documents; file an affiliation form by 1 August |

Two things follow.

**ARFECF membership is derived, not separate.** Art. V §2: *"All Regular Members
in good standing of AFRP and all Associate Members of AFRP shall also be Regular
Members and Associate Members, respectively, of ARFECF."* So there is one
roster with a derived view — which simplifies things considerably. But ARFECF
amends its bylaws by **2/3 membership vote** (Art. IX §1) while AFRP amends by
**2/3 delegate vote** (Const. XI §2, By-Law 16.1.1), and the two Annual General
Meetings are held jointly (ARFECF Art. VII §1). **Two different franchises, in
the same room, on the same day.** The ballot engine needs to know which one it
is running.

**Roles cross entity boundaries ex officio.** The AFRP Executive Committee
(7.1.1) includes the **ARFECF Scholarship Fund Secretary**, the **Educational
Fund Treasurer**, and the **President of ARFECF** — and 7.1.2 expressly
excludes ARFECF officials from election at the AFRP General Assembly. So
holding a role in one entity *confers* a seat in another. My access model is
`(person, role, scope)` where scope is federation / club / program. **Scope
needs to become entity**, and grants need to be able to derive across entities.

There's also a constraint to enforce: **no more than four members of the ARFECF
Board may also sit on the AFRP Board** (ARFECF Art. V §4). That's an
interlocking-directorate cap the system should validate at appointment time,
because it is invisible to whoever is making the appointment.

The Magazine's independence has a further consequence I'd assumed away:
**subscription revenue and subscription policy belong to the Magazine's board**,
not AFRP's. I modelled the magazine as an AFRP function with its money in AFRP's
books.

---

## The Magazine is a statutory notice channel

This is the strongest argument yet for the publication-calendar work, and it
changes the design.

- **Constitution XI §3** — a proposed Constitutional amendment may not be voted on unless, **not less than 60 days** before the Annual General Meeting, notice was sent to all Chapters **and published in the Magazine**.
- **By-Law 10.1.4** — the convention date **printed in the Magazine** is deemed sufficient notice, provided it appears at least **60 days** prior.
- **By-Law 6.5.2** — the Magazine publicises Members At Large candidacies in advance.
- **ARFECF Art. IX §2** — amendment notice published in the Magazine **and** on the ARFECF website, or mailed to members in good standing.

So the magazine is not only a forcing function for data quality. **If an issue
slips, a Constitutional amendment fails and a convention notice fails.** Some
sections aren't editorial content at all — they are legal notices with
deadlines counted backwards from the Convention date. The copy-freeze model
needs a notice-obligation layer: which statutory notices must appear in which
issue, computed from the convention date, with the issue blocked from close if
a required notice is missing.

Note also that ARFECF permits notice by **website** where AFRP does not.

---

## Financial controls the documents specify and the platform should enforce

These are unusually precise, and they're the kind of rule that is enforced
inconsistently by humans and perfectly by software.

| Control | AFRP | ARFECF |
|---|---|---|
| President discretionary spend outside budget | ≤ **$2,000**, **max twice per term** (7.2.3) | ≤ $2,000, max twice per term (§7.3) |
| Above that | Board majority | Board majority |
| Above **$10,000** | Only via the budget approved at the Annual General Meeting | Same |
| Cheque signature | Treasurer, **countersigned** by a senior Executive Committee officer of the home office (11.1.2); General Treasurer co-signs with the Financial Secretary (7.5.1–7.5.2) | Treasurer, countersigned by President, VP or Board designee (§10.1) |
| Educational Fund | Treasurer's signature countersigned by an ARFECF Board designee (7.7.1) | — |
| Deposit timing | — | Within **2 weeks** of receipt (§10.1) |

The "**maximum of twice during their term of office**" counter is worth calling
out: it is a stateful limit across a whole year that nobody currently tracks,
and it is trivial for the system to hold.

**Removal on lapse is automatic.** By-Law 13.2 — an elected officer who loses
good standing in the AFRP *or their Chapter Club* "shall be removed and
replaced by one appointed by the President." That answers a checklist question
directly: standing lapse mid-term is **automatic removal plus presidential
appointment**, not a vote. Given that good standing is conjunctive (4.3.1),
**an officer whose local club dues lapse is removed from federal office** — a
consequence that should probably be surfaced loudly and early rather than
discovered.

**Challenge and certification.** The Credentials Committee (7 members, one of
whom is the General Treasurer) certifies or denies voting eligibility; a denied
member's **dues are not refundable** (8.11.1); major certification problems go
to the Board, **whose decision is final** (8.11.3). Campaign violations: written
complaint → investigation by Credentials and/or Election Committee → the
Chairpersons request the President call a Board meeting → majority of the Board
**by secret ballot** → immediate disqualification (9.4.2).

**Parliamentary authority.** Robert's Rules govern anything not covered (Const.
IX §4, By-Law 12.1), and the President appoints a Parliamentarian — **not the
Legal Advisor** — whose decision on questions of order **is final** (12.2).

---

## What the documents do *not* say

The checklist asked for thirteen things. Here is the honest scorecard.

| # | Needed | Status |
|---|---|---|
| 1 | Membership and standing | ✅ Clear — Regular / Associate, and standing is conjunctive (4.3.1) |
| 2 | Voting eligibility | ⚠️ Partial — certification via Credentials, but no minimum voting age beyond the age-18 membership floor, and no continuous-membership requirement |
| 3 | Record date | ⚠️ Fixed calendar dates rather than a record date; **receipt vs postmark conflict**; **ballot window is internally impossible** |
| 4 | Apportionment | ❌ **No apportionment exists.** Weighted delegate votes instead (9.1.3) |
| 5 | Quorum | ✅ Flat 25 paid members at the Annual Meeting (10.1.5); ❌ no Board quorum at all (10.3.1) |
| 6 | Thresholds by motion | ✅ Mostly — 2/3 delegate for amendments; plurality for offices; 2/3 of **all** Board members for Rules and Regulations |
| 7 | **Abstentions** | ⚠️ Only for Board polls, where non-reply = abstain = effectively No. **Silent for Assembly votes** |
| 8 | Ties | ✅ **Draw from a bag**, Election Committee Chairman presiding |
| 9 | Proxies | ⚠️ No written proxies; but weighted delegation *is* de facto proxy, and remote attendance counts as presence |
| 10 | Secret vs recorded | ✅ Deputy President by mailed secret ballot; Members At Large by secret ballot at the Assembly; Board disciplinary votes by secret ballot; everything else voice or hands. ❌ No right to demand a recorded vote |
| 11 | Certification and challenge | ✅ Credentials certifies, Board decides finally |
| 12 | Committees | ⚠️ Composition and terms are clear; **conflict of interest is entirely absent** |
| 13 | Amendment | ⚠️ Notice and threshold clear; **no effective-date rule and no non-retroactivity clause** |

**The single most important omission is #13.** Constitution XI §1 says the new
Constitution "supersedes in all respects" the previous one, which is revoked
"upon adoption" — with no effective date and no statement about decisions made
under the prior text. Without a non-retroactivity clause, every amendment
reopens every past decision, and the versioned-ruleset design has nothing to
anchor to. One sentence fixes it.

---

## Questions

Ordered by how much the answer changes the build.

### Voting

1. **Is the revision keeping weighted delegate voting (9.1.3), or moving to
   one-delegate-one-vote?** This is the largest single change in the platform.
   If weighted stays: how are fractional votes rounded, and at what precision?
   And does a member who votes independently have to declare it before the vote
   opens, or can they do it at any point while the floor is open?
2. ~~**Does Deputy President stay a mailed ballot counted by an outside CPA?**~~

   *Answered — **voting will be electronic.** By-Law 9.2 therefore has to be
   rewritten rather than reinterpreted: it mandates envelopes, numbering,
   postmarks and physical custody, and none of that survives. Full treatment in
   **AFRP-Electronic-Voting.md**, including a correction to the receipt design
   I'd proposed, which as described would have enabled vote-buying. Two
   headlines: identity resolution stops being a data-quality project and
   becomes an election-integrity control, and electronic voting makes the
   weighted delegate scheme in 9.1.3 practical for the first time — so the
   argument for replacing it with apportionment is weaker than it was when I
   wrote question 1 above.*
3. **How should the June 20 / June 24 impossibility be resolved?**
4. **Postmark or receipt** for the 28 February deadline?
5. **Abstentions on the floor** — in or out of the denominator for a 2/3
   amendment vote? And should a non-reply to a Board poll continue to count
   toward the "all members of the Board" denominator, given it currently
   operates as a No?

### Membership

6. **Where do Patron, Manar, Life, Family and Student memberships come from?**
   Board Rules and Regulations? If so, can I see them — they're evidently
   load-bearing and I've been designing against tiers that appear in no
   governing document.

   *Partly answered — **Patron is $1,000 and Manar is $500**, and **all of
   these figures will change.** Applied throughout: the tier formerly called
   "Sustaining" is now **Manar**, and the ladder is no longer constants in code
   but a **versioned schedule with an effective date**, the same pattern as the
   bylaw rulesets. Changing a figure is now a data edit; a term keeps the price
   in force when it was sold; and rank is derived from price so it cannot go
   stale. This matters because By-Law 5.1 makes dues an annual Assembly
   decision — a structure needing a developer each time the Assembly votes
   would be worked around within two years.*

   *Still needed: the Life and Student figures, whether Family is a
   per-household rate or a per-person one, and the document that authorises the
   ladder — none of these tiers appear in the Constitution or By-Laws, which
   know only Regular and Associate.*
7. **Do complimentary memberships vote?** By-Law 8.15.4 says only dues paid from
   the applicant's own funds count for voting. That appears to disenfranchise
   the newlywed free year, the scholarship student membership, and the under-26
   student waiver in 5.2. Which is intended?
8. **Is 4.3.1 enforced as written** — does a lapsed club membership actually
   cost someone their federal vote today? If yes I'll rebuild standing as an
   AND across scopes and reshoot the member narrative. If it's honoured in the
   breach, the revision should say what's actually done.
9. **Which household definition governs** — 8.15.8 (spouse and unmarried
   children over 18) or 9.5.5 (spouses, children and children's spouses)? They
   are used for different purposes but the system needs one rule for who may
   pay whose dues.

### Structure

10. **Which region map should the platform treat as authoritative**, and can I
    get the current 26-club list mapped into it? The AFRP and ARFECF maps
    disagree on Houston and Knoxville, split Louisville/Lexington differently,
    and neither includes all your clubs.
11. **Is the Ramallah Foundation, Inc. in scope?** It's a separate entity with
    a Board seat and I have no documents for it.
12. **Does the Magazine keep its own books?** The Constitution makes it
    independent with its own subscription management. I modelled it inside
    AFRP.
13. **Are Board Rules and Regulations written down**, and can I see them? Along
    with the Investment Committee policy referenced at 8.6.2 and the Endowment
    Fund Policy Statement referenced at 6.3.1 — both are cited as governing and
    neither is in what you sent.

### Scholarships

14. **4% mandatory floor or 5% cap?** The Policy Statement and ARFECF 6.4.3
    describe the same money two incompatible ways.
15. **On what date are "all Assets" valued**, and is there an averaging period?
    Nothing in either document says, and it materially changes every award
    budget.
16. **Who adopts the conflict-of-interest rule?** Nothing in any of the four
    documents addresses it. My three-degree kinship bar is a build decision with
    no authority behind it, and it should have one.
17. **How many SFC members are elected versus appointed?** Three mechanisms
    describe the same seats.
18. **What are the "required academic credentials"** students must maintain?
    The policy mandates follow-up without stating the standard.
19. **Is the 1% administration fee to AFRP actually being paid**, and is it
    booked as revenue in AFRP and expense in ARFECF? It's mandatory under the
    policy and it's a real related-party transaction.

### Convention

20. **Is the tier schedule current** — $20k / $30k / $40k, with Los Angeles and
    Louisville/Lexington missing entirely, against 26 clubs?
21. **90 days or 120 days** for the final convention accounting?
22. **How much convention operations should the platform run?** Ticketing with
    accountability, ad book sales and fulfilment, seating, security rosters,
    room blocks, the Relief Fund levy and the 30-days-prior dues reconciliation
    are all specified in the contract and none of it is designed. It's a
    substantial module and it may be the one with the clearest annual payoff.

### Amendment mechanics

23. **Will the revision include an effective date and a non-retroactivity
    clause?** One sentence, and it's what lets the whole versioned-ruleset
    design work.
24. **Will the numbers move to a schedule** amendable without a bylaw
    amendment? You asked for flexibility. This is how to get it without
    vagueness — the body says there *is* a threshold, the schedule says what it
    is, and the platform holds the schedule as versioned data.

---

## What I'd change in the build, once you answer

Ranked by size.

1. **Replace apportionment with weighted delegation.** Delete
   `apportionSeats()`. Add exact-decimal vote weights, live re-division on
   member extraction, and the 9.1.4 cap.
2. **Add the three voting modes** — voice/hands, weighted delegate, mailed
   secret ballot — with the mode selected per motion type per 9.1.1.
3. **Rebuild the election calendar** as a first-class object with the seven
   fixed dates, driving eligibility, certification and notice obligations.
4. **Make `standingAt()` conjunctive** across federation and club.
5. **Make quorum a fixed count**, not a fraction, and make abstention handling
   per-motion-type.
6. **Turn scope into entity** in the access model, with cross-entity ex officio
   derivation and the four-member interlock cap.
7. **Add attendance-derived eligibility** for the Council of Past Presidents.
8. **Rework the endowment spend** to percent-of-assets with a stated valuation
   basis, splitting 4% program and 1% administration.
9. **Add the notice-obligation layer** to the magazine issue plan.
10. **Add the financial control gates** — the $2,000 twice-per-term counter, the
    $10,000 budget requirement, and the countersignature rules.
11. **Design the convention operations module**, if you want it in scope.

Items 1–5 are corrections to things I built wrong. 6–11 are additions.

---

*Read against: AFRP Constitution & By-Laws (2009, amended 2012) · ARFECF
By-Laws (2013) · ARFECF Scholarship Fund Policy Statement & Guidelines (2015) ·
Final Convention Contractual Agreement (2009). Design and planning only.*
