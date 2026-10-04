# AFRP Platform — the four lenses
### One system, four jobs: member · club ops · program ops · federation ops

**Date:** August 15, 2026
**Addendum 5.** Builds on the portal, Breeze replacement, life-events, and QuickBooks work.
**Since 2 October 2026:** the four lenses stand. Dated pointers mark the places where an object or a lens has moved since:
- the contact record (P21) puts non-members on the same person model, as a cross-cutting object (§0, §4, §6);
- the scholar is a member-lens experience (P26; §2);
- the family tree follows D68–D74 and P28 (§2, §6.1);
- the Convention is designed in P22 (§5, §8);
- the books' practice is recorded in the ledger and QuickBooks specs (§5, §12).

---

## 0. The organising idea

Everything AFRP does can be described as **one set of objects, seen four ways.**

An event is a thing a member registers for, a thing a club runs, a thing a
program owns, and a line in the federation's financials. It is one `event` row.
What differs is *the question each person brings to it.*

So the architecture is not four applications. It is one data model plus a
**role-scoped policy layer** that decides which slice of it you see and what you
may do. Get that layer right and the four lenses are mostly UI. Get it wrong and
you will build the same feature four times.

*Since 2 October 2026, one object cuts across all four lenses:* **the contact record** (P21). It is a person record with no membership on it, carrying dated roles: learner, applicant, referred, club prospect, giver, guest, subscriber, media or office contact, candidate and alumnus. Each role is owned by one scope (a programme, a club, an event, or a *desk*, which is a federation scope narrowed to the seats that hold it), and each has its own consent rows and retention row. Member 360 shows it whole, and each lens reads only the roles its scope owns (P21 §3, §5, §10). Only the learner is decided (D60) and the alumnus record is D61. The other roles are readings under **Q-70**, built switched off until it is answered (slices CR1–CR7).

---

## 1. Four decisions that shape everything

| Decision | Consequence |
|---|---|
| **Dual membership** — club and national are separate, with separate dues and independent lapse | "Member in good standing" stops being a fact about a person and becomes a fact about a person *in a scope*. Every eligibility question must name its scope |
| **Governance is bylaw-driven configuration** | Apportionment, quorum, thresholds and eligibility are versioned data. The bylaws govern; the code executes |
| **Secret and recorded ballots, per motion** | Officer elections secret with a verifiable receipt; bylaws and resolutions recorded and attributed. Two mechanisms, one engine |
| **Role-based access, not org hierarchy** | A grant is `(person, role, scope)` where scope is federation, club, or program. A program chair reaches their program across all 26 clubs; a club treasurer reaches only their own club |

### 1.1 Why dual membership is the expensive one

It is the decision with the longest tail. Concretely:

- **Two lapse states.** A member can be current nationally and lapsed locally, or
  the reverse. Every "is this person active?" check must say *active where*.
- **Two renewal cycles**, two dues amounts, two reminder sequences.
- **Voting eligibility splits.** Federation matters need national standing; club
  matters need standing in *that* club.
- **Money splits.** Club dues are the club's revenue. If clubs keep their own
  QuickBooks files, the ledger integration multiplies — the open question from
  the QuickBooks spec becomes load-bearing.
- **The wedding benefit needs a target.** It currently upgrades the **national**
  membership. Whether it should also cover club dues is a policy question AFRP
  has not answered.

The code makes the hazard structural rather than a matter of discipline: there
is no `isInGoodStanding(person)` function. That signature is the bug, so it does
not exist. Only `standingAt(memberships, { personId, scope, clubId, asOf })`.

---

## 2. Lens 1 — the individual member

**The question:** *What is mine, and what can I do next?*

| Domain | What a member gets |
|---|---|
| Membership | Both memberships on one screen with independent status and renewal. Digital card. Household coverage |
| Money | Giving history across dues, donations, store. Tax receipts. Stored cards and subscriptions |
| Events | One calendar — federation and their club. Register self and household. QR check-in |
| Governance | Ballots they are eligible for, with the reason if they are not. Cast a vote. Verify a receipt |
| Family tree | Their lineage, search, submit corrections, see their own provisional records. *Since 2 Oct 2026:* drawn in the book's plate grammar (D68); proposals by members in current national standing (D70); the living seen in full only inside one's own branch (D71); find-yourself at join and renewal (D73; P28 §4.4) |
| Life events | Announce a wedding or birth; see the benefit granted |
| Directories | Member directory and RBPN, members-only, their own fields under per-field control |
| Programs | Browse, apply, track application status. *Since 2 Oct 2026:* a Scholarship recipient also files after each semester and sees the next instalment's release or hold (the **scholar** experience; P26 §2). The "my path" page lists the member's own programmes and seats in date order, and only the member sees it (P25 §3; D39) |
| Communications | Preferences per channel with real consent |

**The design rule for this lens: never show a member something they cannot act
on.** A ballot they are ineligible for should say *why* — "your national
membership lapsed on 12 March" with a renew button — not silently vanish. The
eligibility engine returns a reason for exactly this.

---

## 3. Lens 2 — local club leadership and operations

**The question:** *Who are my people, and is my club healthy?*

This lens replaces Breeze, so it needs real depth.

| Domain | Club officer capability |
|---|---|
| Roster | Full club membership with dual status, groups/tags, households, bulk actions |
| Dues | Club dues collection, lapsed follow-up, remittance to national if applicable |
| Events | Create, publish, room and resource booking, check-in with name tags, child security codes |
| Communications | Email and SMS to segments, with the audience **consent-filtered before send** |
| Governance | Club elections, delegate selection, credentialing for convention |
| Reporting | Attendance and giving trends, membership growth, benchmark against federation aggregates |
| Programs | See which of their members are in Camp Ramallah, Project Hope, and so on |

**Two things this lens must show that Breeze cannot:**

1. **Dual status side by side.** A member current locally but lapsed nationally
   is a specific, actionable problem — and it is invisible in any single-scope
   system.
2. **Federation context.** "Your renewal rate is 78%, federation median 84%" is
   the kind of number that changes officer behaviour. It requires cross-club
   aggregates without exposing other clubs' members, which the policy layer
   handles by returning counts rather than rows.

---

## 4. Lens 3 — program leadership and operations

**The question:** *Who is in my program, across the whole federation?*

This is the lens that proves the access model. A Camp Ramallah chair is not
senior to a club president and not junior to a national officer — they have a
**different job**, and their scope cuts across all 26 clubs for one program and
stops dead at everything else.

| Domain | Program leadership capability |
|---|---|
| Applications | Federation-wide queue, rubric scoring, reviewer assignment, decisions |
| Participants | Roster across clubs, with the club context |
| Events | Program events — camp sessions, mission trips, Day of Action |
| Communications | Message applicants and participants, consent-filtered |
| Budget | Program spend against a restricted fund; net asset release when the restriction is met |
| Outcomes | Participation over time, retention into membership, alumni |

Programs in scope: Camp Ramallah · Project Hope · Medical Mission · Leadership
Ramallah · Scholarship Program · Day of Action · Arabic Course · Women to Women ·
RBPN · Educational and Cultural Exchange · Hathihe Ramallah · Preservation
Project · Family Tree.

*Since 2 October 2026:* a programme scope also owns its non-members' roles on the contact record (P21): the Arabic learner (D60), the applicant to a programme open to non-members, the AFRPWorks candidate and the Magazine subscriber (Q-239). The programme reads only those roles, never the person's other roles (P21 §3.2, §5). The Day of Action runs in one of two modes per cycle, application and selection or registration, set by the deciding body; a cycle with no mode does not open (P25 §5.3; Q-254). The Senior Award's status is in question (Q-163; *since 3 Oct 2026 it continues, D82*), and "Emerging Leaders" has no source (Q-178).

**The connection worth building deliberately:** program participation is the
strongest predictor of long-term membership. A teenager who goes to Camp
Ramallah is a future Patron. Nothing currently connects those two facts, and the
platform can — that link is arguably the most valuable analytic AFRP could own.

---

## 5. Lens 4 — federation leadership and operations

**The question:** *Is the federation healthy, and are we governed properly?*

| Domain | Federation capability |
|---|---|
| Membership | Federation-wide health, by club, tier, cohort, and trend |
| Money | Consolidated giving, fund balances, QuickBooks close, restricted-fund reporting. *In practice (research, 2 Oct 2026):* QuickBooks is already integrated with the current CRM for AFRP and ARFECF, with three processor accounts, one per entity (`AFRP-QuickBooks-Integration-Spec.md` §12); D1 and D56 stand |
| Governance | Convention, apportionment, credentialing, ballots, certification, minutes |
| Convention | Sessions, registration, housing, banquet, sponsors, delegate credentialing. *Since 2 Oct 2026:* designed in P22 (slices CV1–CV8) |
| Clubs | Health across 26 clubs; migration status; officer directory |
| Programs | Portfolio view, budget vs actual, participation |
| Communications | Federation-wide sends, per-club coordination, deliverability |
| Compliance | 990 support, restricted-fund attestation, audit trail |

**The number this lens exists to produce:** *who gave last year but has not
renewed* — federation-wide, by club, by tier. That question is unanswerable
today and it is the single clearest justification for the whole platform.

---

## 6. The permission model

A grant is `(person, role, scope)` where `scope` is `federation`, `club:<id>`, or
`program:<id>`. Implemented in `src/access/policy.ts`, 41 tests.

### 6.1 Roles

| Role | Typical scope | Reach |
|---|---|---|
| `member` | federation | Own record, public reads, voting |
| `club_president` / `secretary` / `treasurer` / `events` | club | One club |
| `program_chair` / `program_reviewer` | program | One program, **all clubs** |
| `national_officer` / `national_staff` / `national_treasurer` | federation | Everything in their domain |
| `genealogy_moderator` | federation | Tree moderation only. *Since 2 Oct 2026:* `tree:moderate`, held by committee members. One key applies a non-structural change and two different keys apply a structural one (D72). The second holder is a committee member the committee seats (D79, 3 Oct 2026; Q-262). Clan stewards recommend and never approve |
| `credentials_committee` | federation, **time-boxed** | Delegate credentialing |
| *(since 2 Oct 2026)* a desk seat | federation, narrowed to the seats that hold it | The contact roles that desk owns: the statement register's media contacts, Government Affairs' office contacts, a receipting entity's one-time givers (P21 §3.2). Exact-grant for any contact's fields (R39) |
| `elections_officer` | federation | Ballot creation, certification, unsealing |
| `platform_admin` | federation | Integrations, audit, role granting |

### 6.2 Two rules that keep it honest

**Scope containment is directional.** Federation satisfies club and program.
Club never satisfies another club. **Club and program are siblings** — a club
president is not implicitly a program reviewer, and a program chair is not
implicitly a club officer. That separation is the whole point of role-based
rather than hierarchical access.

**Sensitive permissions are never inherited.** `member:pii:read`,
`member:export`, `ballot:unseal`, `ledger:post` and `role:grant` require an
exact-scope grant. A federation elections officer cannot unseal a *club's*
ballot without being granted it for that club specifically. Tested.

### 6.3 Worked examples

| Person | Grants | Can | Cannot |
|---|---|---|---|
| Detroit treasurer | `club_treasurer @ club:detroit` | Read Detroit dues and roster | Read Chicago's dues; write Detroit's roster |
| Camp Ramallah chair | `program_chair @ program:camp` | Decide camp applications federation-wide | Decide Project Hope applications; edit a club roster |
| National staff | `national_staff @ federation` | Read every club roster | Export PII, post to the ledger, unseal a ballot |
| Credentials committee | `credentials_committee @ federation`, 1 Jun – 5 Jul | Credential delegates during convention | Anything after 5 July |

---

## 7. Governance

Implemented in `src/governance/`, bylaw rules supplied as versioned data.

### 7.1 The correctness property

**Eligibility is frozen at a record date into `ballot_electorate` and never
recomputed.** Tallies read the snapshot, not live membership.

Without this, someone paying dues mid-vote silently changes the electorate and
the result cannot be reproduced afterwards. **Every disputed election turns on
exactly this question.** Proven end-to-end: 25 people joined after the record
date and the frozen electorate did not move.

### 7.2 Worked convention

Real output from the engine against seeded data:

```
68TH ANNUAL CONVENTION — meeting 2026-11-15, record date 2026-10-16

APPORTIONMENT  (1 delegate per 5 members, major fraction, min 1 / max 8, floor 6)
club                eligible  seats
Chicago                   36      7
Houston                   32      6
San Francisco             30      6
Washington DC             32      6
Cleveland                 27      5
Detroit                   26      5
Jacksonville              27      5
Los Angeles               24      5
HOUSE                    234     45  seats

SECRET BALLOT — President
  N. Khoury        22 seats   62.9%
  S. Ajluni        13 seats   37.1%
  abstentions      10
  quorum met: true   decided: true   winner: N. Khoury (simple_majority)
  receipt check: found=true
  voter->token link stored anywhere? no

RECORDED BALLOT — Bylaw amendment (2/3 required)
  N. Khoury        35 seats   77.8%   decided: true (supermajority_0.667)

CERTIFIED  hash 51ba40cc84ecf673...
```

Apportionment shows its working — floors, caps and exclusions are reported with
a reason, because in a contested convention a credentials committee needs to
explain *why* a club got its seats, not just what the number is.

### 7.3 How the secret ballot works

```
ballot_participation  (ballot_id, person_id, voted_at)   ← WHO voted
sealed_vote           (ballot_id, token_hash, choice)    ← WHAT was chosen
```

Never joined. The voter↔token link is **never stored**. A random token is
generated at vote time, its hash stored with the choice, and the raw token shown
to the voter once.

**What this buys:** double voting impossible, turnout known, every voter can
verify their own ballot.

**What it costs, stated plainly:** a lost receipt cannot be recovered or
reissued. That is not a gap to fix later — reissuing would require storing the
link, which is the thing that makes the ballot secret. The UI must say so before
the voter closes the receipt.

**What it is not:** end-to-end-verifiable voting in the academic sense. An
administrator with database access could still alter sealed rows. Mitigations:
`ballot:unseal` requires an exact-scope grant, every action is audited, and
tallies are certified by a named officer against a result hash. For a membership
association that is the honest bar — anyone claiming more from a system like
this is overselling it.

### 7.4 Behaviours worth knowing

- **Ties are never broken silently.** The engine returns `decided: false,
  reason: 'tie'`. Breaking one is the chair's job.
- **Abstentions are reported but excluded from the threshold denominator.** An
  abstention is a deliberate refusal to take a side; counting it as a "no"
  misrepresents it. Whether AFRP agrees is a bylaw question — it is documented in
  the result rather than hidden.
- **Quorum failure blocks a decision regardless of the numbers.**
- **`majority_of_seats` uses the whole house**, not just those voting — 14 of 30
  seats loses even if it wins the room.

### 7.5 What I need from the bylaws

Send the document and these become configuration:

1. Delegate apportionment formula — divisor, rounding, floor, cap, minimum club size
2. Quorum — of seats, of credentialed delegates, or of members
3. Voting eligibility — which membership, minimum age, continuous-membership requirement
4. Record date — how many days before the meeting
5. Thresholds by motion type — officers, bylaws, dues changes, resolutions
6. Proxy voting — permitted? limits per delegate?
7. Tie-breaking — chair's casting vote, re-ballot, or lot
8. Who certifies a result

Items 6 and 7 are the two most likely to be in the bylaws and absent from the
current engine.

---

## 8. Convention — where all four lenses meet

The single most complex thing AFRP does, and every lens touches it.

| Lens | Convention view |
|---|---|
| Member | Register self and household, sessions, banquet, housing, digital badge, QR check-in |
| Club | Delegate selection, credentialing, group registration, club dinner |
| Program | Program sessions, awards, participant meetups |
| Federation | Full agenda, room and resource allocation, sponsors, ballots, minutes, financial close |

*Since 2 October 2026:* the Convention is designed as its own element in P22 (`AFRP-Convention-Operations.md`), alongside P8 (bids) and P13 (host agreements). It covers:
- the award and the 10.1.1 forfeiture reading (Q-240);
- a Federation-hosted Convention abroad as a template (Q-223);
- the unified registration with a membership-gate parameter per event (Q-225) and the desk;
- delegates from the certified roll to the floor, with each club's selection method recorded and none refused (Q-37);
- sponsors and the ad book (Q-242, Q-245);
- the host coordinator's access, narrower than today's practice (Q-127);
- the close as dated acts (Q-221, Q-241);
- the books (P22 §10).

A guest named by someone else is Q-238 on the contact record.

**Build order matters here.** Registration and check-in first, governance
second, housing and sponsorship last. Governance can run on paper for one more
convention; registration cannot.

---

## 9. Communications

Two senders, one consent model.

| | Club | Federation |
|---|---|---|
| Audience | Own roster | Any segment |
| Channels | Email, SMS | Email, SMS, push |
| Consent | Enforced | Enforced |
| Coordination | — | Sees club sends to avoid collisions |

**The rule: consent is checked when the audience is built, not at send time.**
The composer shows "1,284 recipients — 312 excluded, no SMS consent" *before* the
officer writes the message. Doing it at send time means someone has already
written to an audience that does not exist, and that is when people start
looking for workarounds.

---

## 10. Build order

Ordered by what unblocks the most, not by what is most exciting.

| # | Work | Weeks | Why here |
|---|---|---|---|
| 1 | **Role and scope model** | 3–4 | Everything else depends on it. Retrofitting authorisation is brutal |
| 2 | **Dual membership** | 4–5 | Changes every standing check in the system |
| 3 | Member lens — the four core screens | 6–8 | Earliest visible value |
| 4 | Club lens — roster, dues, events | 8–10 | Breeze parity begins |
| 5 | Communications with consent-filtered audiences | 4–5 | Blocked on 10DLC calendar time — **start registration now** |
| 6 | Convention: registration and check-in | 5–6 | Schedule against a real convention date |
| 7 | **Governance: apportionment, ballots, certification** | 6–8 | Needs the bylaws first |
| 8 | Program lens | 6–7 | |
| 9 | Federation analytics | 5–6 | Wants a year of clean data underneath it |

Roughly **48–60 weeks** of the governance-and-lenses work, overlapping the
integration phases already planned.

**If only one thing gets funded: the role and scope model.** It is unglamorous,
produces no demo, and every other item on this list is harder or impossible
without it.

---

## 11. What is in the code now

| Component | File | Tests |
|---|---|---|
| Role-scoped access policy | `src/access/policy.ts` | 41 combined |
| Dual membership + eligibility + apportionment | `src/governance/eligibility.ts` | |
| Ballots — secret, recorded, quorum, thresholds, certification | `src/governance/ballot.ts` | |
| Schema — role grants, bylaws, convocations, ballots, sealed votes | `src/db/schema.sql` | — |

**Schema now 57 tables. 163 tests passing, typecheck clean, portability guard clean.**

---

## 12. Open questions

1. **The bylaws.** Everything in §7.5. This is the blocker for governance.
2. **Do clubs set their own dues,** and do they remit a per-capita to national?
   Determines whether club dues touch the federation ledger at all.
3. **Do clubs keep their own QuickBooks files?** If yes, the ledger integration
   is 27 connections, not one. *In practice (research, 2 Oct 2026):* clubs keep their own books, some in Breeze and some in QuickBooks, and none is in the Federation's file (`AFRP-Multi-Entity-Ledger.md` §9).
4. **Should the wedding benefit cover club dues too,** or national only?
5. **Can someone be a national member with no club?** The model allows it; the
   bylaws may not.
6. **Is proxy voting permitted?** Common in federations, absent from the engine.
7. **Who breaks a tie** — chair's casting vote, re-ballot, or lot?
8. **Which convention is the target?** Registration and check-in should be
   scheduled against a real date; everything else can follow.

---

*Governance behaviour verified end-to-end against seeded data on 15 August 2026:
apportionment with floors and caps, a frozen electorate proof, a secret election
with receipt verification, a recorded two-thirds bylaw vote, and certification.
Bylaw parameters used in the worked example are illustrative and tuned to the
seed population — AFRP's actual bylaws will differ, which is why they are
configuration rather than code.*
