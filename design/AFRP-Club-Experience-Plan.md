# The club experience plan

### How a chapter club lives on the platform, from the day it is read out of Breeze to the day the Federation sees it as one of all its clubs

**Design note P18 · opened and written 1 October 2026 · reviewed (PASS WITH CHANGES, applied) · the Hub builds from §13**

This note is the hand-off for everything a club does on the platform. It joins what the two Breeze documents already settled (`AFRP-Breeze-Club-Parity.md`, `AFRP-Addendum-2-Breeze-Replacement.md` §3) to what the intakes found about how clubs actually run (the club SOP, the 2009 club by-laws template, the affiliation rule, the club presidents' monthly meetings 2020–2026, the convention host agreements), and to the decisions taken on 30 September and 1 October 2026 (D54–D67, D57 and D59 above all). It was written in fourteen half-hour sprints on 1 October 2026; each sprint closed one section and was written back before the next opened. §0 is the record of them.

**Precedence (D41).** Where this note and a by-law text disagree, the text wins. Where it and the Decisions Register disagree, the register wins. The prototype's club screens (`#/club/*`) evidence a story and never a rule. The Hub's `clubs` module shows what is built and never what should be. Where the record is silent this note says so and raises a question; it picks no default.

**Public-repo rule.** No living person is named. No club's figures (dues, balances, member counts) appear. Clubs are named as organisations only where the record already names them.

---

## 0. The plan of the note

| Sprint | Section | What it settles | Status |
|---|---|---|---|
| 1 | §1 Sources and the shape of the problem; §2 the lens audit | What the record already holds; what the club lens is missing | done |
| 2 | §3 The people of a club | President, secretary, treasurer, membership secretary, ambassador, member-of-a-club, as experiences | done |
| 3 | §4 The club workflows | Running a club; club events; club giving (B3); the Breeze import (B4); texting (B5); forms (B6) | done |
| 4 | §5 The club–Federation statement | D57 designed: the one statement, its lines, its close, its disputes | done |
| 5 | §6 Club governance | Affiliation, the officers form by 1 August, delegates, the presidents' meeting, the Council — under the Q-33 gate | done |
| 6 | §7 Clubs inside the programmes | Rebates, travel shares, ambassadors, volunteers, co-funding, the host club | done |
| 7 | §8 The migration, club by club | Parity, the data that moves, the parallel run, cutover, the order of clubs | done |
| 8 | §9 Club communications and consent | What replaces the clubs' mail and text tools; what the Federation's newsletter shares | done |
| 9 | §10 The Federation's roll-up and the club view of the site | Counts under the floor; the club president's page | done |
| 10 | §11 Journeys for the club lens | The use cases, the journeys that test them, the corpus rows | done |
| 11 | §12 Strategy pages and the crosswalk | Goal rows J9 onward; One Federation; the history | done |
| 12 | §13 Slices and gates for the Hub | MASTER-PLAN rows; exit tests; what waits on a decision | done |
| 13 | §14 Review | The afrp-review verdict and what it changed | done |
| 14 | — | Publish; the report to David; the questions for the Boards | done (written to the desktop; David pushes) |

---

## 1. Sources and the shape of the problem

### 1.1 What the record already holds about clubs

| Document | What it gives this note | Rank |
|---|---|---|
| AFRP Constitution and By-Laws 2024 (`bylaws/`) | Chapter clubs, delegates, By-Law 3.2 (officers and affiliation), the club presidents on the Board, the host-city rotation | text |
| ARFECF By-Laws revised 2015 and the two fund policies (`bylaws/ARFECF-2015-and-the-fund-policies.md`) | Region seats on the ARFECF Board defined by lists of clubs; the four-member overlap cap | text |
| Decisions Register | D1 (club-collected national dues are custodial, remitted on the run), D6, D57 (one club-share statement; club attribution on any gift), D59 (the host agreement is the convention rule), D61 (historical records), D66 (the drive is the archive), R6 (minors' authority), S7 | register |
| `AFRP-Breeze-Club-Parity.md` | Breeze as it reads (§1, and the deep read of 1 October 2026 in §1a); the crosswalk; slices B1–B6; the rules the club objects obey; eight questions for David | design |
| `AFRP-Addendum-2-Breeze-Replacement.md` §3 | The parity matrix; the three hard things (texting, child check-in, twenty-odd migrations each a relationship); the six-step migration path per club | design |
| `AFRP-Four-Lens-Architecture.md` §3, §6 | The club lens as one of four; club and programme scopes are siblings | design |
| `AFRP-Multi-Entity-Ledger.md` §2.1, §3 | The club's ledger profile; agency against revenue treatment | design |
| Strategic Plan Crosswalk rows J1–J8 and P10 | Clubs in Care co-funding, one cost-share rule, one statement, the affiliates' regional seats, named shared services, the dues rule, the host agreement, club attribution | design |
| The intake findings (private, `claude/intake/AFRP-cards-events-clubs.md`) | The club SOP (2025), the 2009 club by-laws template, the affiliation rule (2021), the 2020 letters to club presidents, the presidents' monthly meeting notes 2020–2026, the convention MOU template and the host clubs' reports | practice |
| `site/data/experiences.yaml` (club-officer, club-treasurer), `workflows.yaml` (club-management, club-share, remittance-ledger, events, communications, convention) | What the site already says a club does | site |

### 1.2 What the intakes established about how clubs run today (role-level)

- About ten of the clubs run Breeze for membership, events, payments and texts; the rest are to onboard or use their own tools. Beside Breeze the clubs use a mailing tool (two different ones are named), a small-business accounting package, the Federation's institutional video-call account, and group messaging.
- The Federation's own operating list of clubs is a sheet of current presidents. It lists seventeen clubs; eighteen per-club voting lists exist; three edge cases (a Florida club, a Pennsylvania mention, the club in Ramallah) appear in other files. The register's "17, 18 or 19" question is still open (Breeze Parity §5 q8).
- The only written affiliation requirement is a 2021 rule: each chapter club files a form naming all officers with the Federation office by 1 August each year. Nothing in the 2009 club by-laws template states affiliation, delegates or per-capita dues to the Federation; only the dissolution clause points to the Federation.
- The 2020 letters to club presidents set working expectations: presidents sit on the Federation Board; attendance at the monthly presidents' meeting; at least one event or meeting a quarter; the Federation's video-call account for club events.
- The club SOP (2025) describes how a club is started or restarted: a founding core, state registration with the Federation's templates, a bank account, a membership database, a website and social channels, monthly meetings with a standard agenda, membership tiers for young adults, youth and children, club-set dues, and a five-year plan that may include hosting a Mid-Year or a Convention.
- Clubs take money on their own books: club dues, event income, sponsorships, co-funding of affiliate projects, and host-club income from Conventions and Mid-Years under a host agreement. The Federation's share of a Convention is fixed in the agreement; a committee has discussed a percentage split that does not match it (Q-34 → D59).
- Clubs share programme costs with the Federation: dabke travel to the Convention and the Mid-Year has been shared between the Federation and the club on terms minuted case by case; camp rebates and Leadership Ramallah travel shares are per-programme terms (J2, D57).
- The presidents' meeting in 2026 asked for: a shared club event playbook, a national "club night" on one day by video call, by-law templates to speed club tax-exempt applications, locally branded texting, a central programming guide, and a review of the CRM's cost.

### 1.3 The shape of the problem

Breeze gives a club officer one screen for one club. The platform must give the same officer the same screen, and then three things Breeze cannot: the member's national standing beside their club standing; one statement of what the club and the Federation owe each other; and the Federation's view of every club at once as counts under a suppression floor, never as names. The plan below is organised around those three gains, and around the one rule that governs all of them: the club's data is the club's, the member's record is the member's, and the Federation reads neither except as a count.

The hard parts are not the database (Addendum 2 §3.3): texting needs a provider and a carrier registration; child check-in is safeguarding, not convenience; and each migration is a relationship with officers who chose Breeze. This note therefore plans the migration as a programme of its own (§8) with a named owner per club, and treats B5 and B6 as gated until David answers Breeze Parity §5.

---

## 2. The lens audit (sprint 1)

What `experiences.yaml` holds for the club lens today, and what is missing.

| Lens entry | Holds | Missing |
|---|---|---|
| `club-officer` | Roster with dual status; groups, follow-ups, club events with check-in; counts for the Federation; three privacy rules; J08, J14; 36 catalogue rows; workflows club-management, events, communications | No officer year (the 1 August form, the hand-over); no president as distinct from secretary; no membership secretary's queue (JC-022 not built); no delegate selection; no club giving; no mailing or texting; no migration |
| `club-treasurer` | Split at capture; remittance statement with carry-forward; chargebacks as receivable; D1; J08; 14 rows; workflows remittance-ledger, club-management, join-renew-dues | No club-side money (club dues, events, gifts to the club, sponsorships); no D57 statement (rebates, travel shares, settlements, grants, co-funding); no club ledger profile; no hand-over of the books at year end |
| (none) | — | **Club president**: the affiliation and officers form, the Board seat, the presidents' meeting, the delegation, the host bid, the five-year plan |
| (none) | — | **Club ambassador / programme liaison**: the club's seat in a programme (camp families, scholarship outreach, Day of Action travel, Arabic volunteers) |
| (none) | — | **A member of a club** (the member lens seen from the club side): what the member sees of their own groups, attendance, club statement, club mailings and consent; what they never see of others |
| (none) | — | **A club in migration**: the officers during the parallel run (verify the roster, sign off, cutover) |

Decision for sprint 2: add `club-president`, `club-ambassador` and `club-member-view` as lens entries; extend `club-officer` with the secretary's and membership secretary's duties; extend `club-treasurer` with the club side and the D57 statement. The migration officer role is written into §8 and the club-management workflow, not as a lens of its own, because it exists for weeks, not years.

### 2.1 Questions the audit raises (for governance to number)

- Whether a club's membership secretary is a seat the record recognises, or a duty of the secretary. The Hub's `club_officer` seats and the 2009 template name president, vice-president, secretary and treasurer; the affiliation form "lists all officers" without naming them. *The record is silent on the seat list; a club sets its own under its by-laws.*
- Whether the 2021 affiliation rule (1 August) is a Board rule, an office practice, or By-Law 3.2's deadline restated. The site's workflow already cites By-Law 3.2; the 2021 file is the only text found.
- Whether a club's own tiers (young adult, youth, child, in the SOP) are the club's to define or follow the Federation's membership classes. *Silent.*

---

## 3. The people of a club (sprint 2)

Six kinds of person walk the club lens. For each: who they are in the text, what they need, what the platform does for them, the rule that protects them and the decision behind it, and what the record does not say. The by-law citations are to the AFRP Constitution and By-Laws approved 13 July 2024 (`bylaws/`), which outrank everything below them.

### 3.1 The club president

**In the text.** The president of a Chapter Club that has complied with Article III sits on the Council of Chapter Club Presidents, chaired by the Deputy President (By-Law 6.4.1), which meets at least twice a year including the Mid-Year and the Convention (10.5.1); every member of that Council is a voting member of the Federation Board (6.2.2) and, as a Board member, is "deemed an ambassador of the A.F.R.P. in his or her community" (6.2.3). The club president, or a representative, is the club's seat on the Membership Committee (8.12.1). The club files the affiliation form naming all officers with contact details by 1 August each year (3.2); affiliation itself is with the Federation's approval (3.1).

**Needs.** Know the club is affiliated and in good standing for the year; file the officers once and have every Federation list (the Council, the Board roster, the Membership Committee, the magazine's correspondents) read from it; see the club's health as the Federation will see it; bring the delegation to the Convention credentialed; bid to host; carry the club's five-year plan.

**The platform.** One officers form a year, started from last year's, which is the By-Law 3.2 filing and the source of every seat the by-laws derive from it; a standing pill for the club (affiliated for the year, filed on, approved on); the club's dashboard (roster counts, dues position, open follow-ups, next events, the D57 statement balance) as the president's first screen; the delegation selected from certified members (9.1.3, 9.1.4) and handed to the convention workflow; the host-bid form (P8) and the host agreement on the event (D59).

**Rules and their source.** The club president must be in good standing of both the club and the Federation, because every compliant president sits on the Board (6.2.2, 6.2.3, 4.3.1); the platform refuses the president's seat to a lapsed member by name. For every other seat the by-laws are silent and the club's own laws govern (3.1); the platform shows the standing beside each name and refuses nothing. *Design choice, not a by-law: whether a club may ask the platform to apply the same test to all its seats is a per-club switch, off by default.* The president reads the whole club and nothing of any other club (Four-Lens §3). The president's contact details on the form are the Federation office's to hold and the Council's to see; they are not the directory's (R27).

**Not in the record.** Whether "the approval of the A.F.R.P." for affiliation (3.1) is a Board vote, an officer's signature, or the office's acceptance of the form; who marks a club as having "complied with Article III" and when a late form costs the club its Council seat for the year. *A question for governance (§6).*

### 3.2 The club secretary, and the membership secretary's duties

**In the text.** The 2009 club by-laws template names a secretary; the affiliation form "lists all officers" and names none. The membership secretary is a duty the Hub's journey corpus describes (JC-022, not built), not a seat any text names.

**Needs.** Keep the roster true: who joined, who lapsed nationally and who lapsed at the club, which households moved; make groups and raise follow-ups; publish the club's events and take attendance; mail the club lawfully; keep the minutes somewhere the club can find them.

**The platform.** The roster with the two standings side by side, sorted by household (B1); groups and follow-ups, with the lapse rule the club switches on (Breeze Parity §4 r3); club events with check-in and the release list for children (B2, R6); the acting panel (mail this set, add this set to a group, open a follow-up for this set); the secretary's queue of things that need a human (JC-022: a join that names this club, a household split, a member who asks to move clubs, a death reported). Minutes do not enter the platform; the drive is the archive (D66) and the platform links to it. *Since 2 October 2026:* a person the club met who is not a member is a **club prospect**, a role on the contact record that only the person's own act at the club's door creates (P21 §2, §10; P20-A1, P20-A7). A secretary's entry is a queue item with no channel until the person acts. The club sees its own prospects, the people referred to it, its own events' guests and its own media contacts, and no other club's or programme's roles. The design is DRAFT under Q-70. A prospect nobody referred is Q-72.

**Rules and their source.** A follow-up is a task about a person, never a note about them, closed and never deleted (Breeze Parity §4 r2); there is no free-text note on a person anywhere in the club lens except a follow-up's one completion note (refusal by design, Breeze Parity §4 r2). A mailing reaches only the club's own roster, filtered by consent (R27, workflow communications). Minors are never listed outside the club's own officer screens (R7).

**Not in the record.** Whether a member may belong to two clubs at once, and who decides a move between clubs; the Hub's model allows several club memberships (J02, multi-club renewal) and the by-laws speak of "his/her Chapter Club" in the singular (6.2.3, 9.1.3). *A question for governance.*

### 3.3 The club treasurer

**In the text.** The 2009 template names a treasurer; the club SOP expects a bank account in the club's name; the Federation's dues rule is D1 (club-collected national dues are custodial on the club's books and are remitted on the run); D57 puts every amount between a club and a Federation or affiliate programme on one statement.

**Needs.** Two books that never mix: the Federation's money the club holds as agent, and the club's own money. Collect, close, remit and reconcile each month; see what the club is owed (camp rebates, travel shares, event reimbursements, the host settlement) and what it owes (dues remitted, co-funded grants) on one statement; take the club's own income (club dues, tickets, sponsorships, gifts to the club) without a second system; hand the books to a successor at year end.

**The platform.** Split at capture of national and club dues; the remittance statement with carry-forward and chargebacks after remittance as a receivable (built); the D57 statement (§5) with a line per programme term and a dated close; the club's ledger profile (agency against revenue, from the Multi-Entity Ledger §2.1, §3); club giving through the one payment door onto the club's books (B3, gated on David's answer to Breeze Parity §5 q3); the year-end hand-over as a dated change of seat with the statement balance carried, never a copy of the data.

**Rules and their source.** Collected national dues are never the club's revenue (D1). A gift to a club lands on the club's books and the member's statement for that club, and a purpose outside the club's entity refuses by name (B3 exit test). The treasurer reads only their own club's money. By-Law 11.1.4: a club may not solicit for a project the Federation has already undertaken without the Board's and Executive Committee's authority; the platform can show a club's appeal against the Federation's active projects, but who checks it is not written.

**Not in the record.** Whether the club's own accounting stays in its small-business package with the platform as the statement of what passed between club and Federation, or the platform becomes the club's books. The intakes show every club keeping its own books today. *This is the B3 question in another form; it stays David's.* Also unwritten: whether a club's accounts are ever seen by the Federation (the Executive Director "shall have access to all A.F.R.P. and Chapter Club records", By-Law 7.9.3; the clubs page as built reads counts, Breeze Parity §3, B1). Four-Lens §6.3 (August 2026) lets national staff read every club roster without export; Breeze Parity (September 2026) and slice B1 built the Federation's view as counts. The later design governs the clubs page; which of the two applies to a named-purpose read under 7.9.3 is part of the question. *The text wins over both; the platform needs a named purpose and an audit line for that access. For governance (P16 §3.2 gives the shape; Q-44 carries it).*

### 3.4 The club ambassador (the club's seat in a programme)

**In the text.** Every Board member, which includes every compliant club president, is "deemed an ambassador" (6.2.3). The programmes' own records name per-club roles the by-laws do not: the camp liaison who gathers the club's families, the scholarship outreach contact, the Day of Action travel coordinator, the Arabic volunteers, the dabke troupe lead, the club's sponsor-outreach lead for a Mid-Year.

**Needs.** See the programme from the club's side: which of this club's families, scholars, travellers or volunteers are in it, and what the club owes or is owed for them (J2); pass news both ways.

**The platform.** A programme seat scoped to one club (club and programme scopes are siblings, Four-Lens §6): the ambassador sees the programme's roster filtered to their own club and nothing of other clubs, and sees the club's D57 lines for that programme. The programme organiser sees all clubs within the programme. The seat is appointed by the club president on the officers form (or after it, dated) and expires with the officer year.

**Rules and their source.** A programme seat does not grant the club lens, and a club seat does not grant the programme lens (Four-Lens §6). Minors in a programme are seen by the ambassador only as a count unless the R6 authority model names them.

**Not in the record.** Whether a club names such seats at all, or the programme committee does; today both happen. *A question for governance; until answered the officers form offers the seat and the programme committee may also appoint it, each appointment named by who made it.*

*Since 2 October 2026, two club seats in particular:*

- **The Magazine correspondent.** A city correspondent named on the magazine's inside cover is how announcements and club news reach the editor today. The Magazine operations note gives the seat one act: an **assisted submission** made on a household's behalf, which lands as pending and prints nothing until the household's consent is recorded. The door builds as pending-only until Q-195 is answered (P24 §3.2, MG1; P20-D8).
- **The local action committee.** In practice (research, 2 Oct 2026), the Government Affairs Committee launched local action committees inside clubs in 2025–26. Nothing is seated: it is not a seat on the officers form and not a body on CW1 until Q-131 says who appoints it and to whom it reports (P25 §5.4; P14 §2.8; P20-D7).

### 3.5 A member, seen from the club's side

**In the text.** A member of a Chapter Club may be deemed a member of the Federation if they qualify and are in good standing (3.1, 4.3.1); a certified member may vote independently at the Convention, and their vote is deducted from their club's delegation (9.1.3).

**Needs.** See their own club standing beside their national standing; see their own groups and attendance; see their own statement with the club; control what the club may send them; move clubs or leave one.

**The platform.** The member lens already shows scoped standing (national and club lapse independently) and the two consents; B1 adds the member's own groups to their record and B2 their own attendance; B3 would add the club statement. A request to move clubs opens a secretary's-queue item in both clubs. The member never sees another member's groups, follow-ups or attendance.

**Rules and their source.** Display, contact and export are three separate consents (R27); a club mailing honours the contact consent; a follow-up about a member is not visible to the member (Breeze Parity §4 r2). The member's vote at the Convention is theirs to cast independently (9.1.3).

**Not in the record.** Whether a member may see that a follow-up exists about them (the register says it is the club's; privacy law in some states may say otherwise). *A question for the Legal Advisor.*

### 3.6 The officers of a club in migration

Written in §8. For a few weeks the president, secretary and treasurer of one club have a fourth duty: verify their own roster against what the import proposes, sign off, and cut over. It is a duty on the existing seats, not a lens.

### 3.7 What sprint 2 changes in the site's data

- `experiences.yaml`: new entries `club-president`, `club-ambassador`, `club-member-view`; `club-officer` extended with the secretary's queue, the lapse rule and the minutes rule; `club-treasurer` extended with the club side, the D57 statement and the year-end hand-over.
- Questions for governance to number (§3.1, §3.2, §3.3 twice, §3.4, §3.5): six, listed in §6.

## 4. The club workflows (sprint 3)

Six processes run a club on the platform. Four exist in the record already (running a club, club events, communications, the club statement); this sprint rewrites the first around the officer year, writes the migration as a workflow of its own, and places club giving, texting and forms where they belong with their gates. Each step names a role; every rule names its decision.

### 4.1 Running a club: the officer year

The club's year on the platform runs from the officers form to the hand-over. The steps, in order, with who does each:

1. **File the officers** (club president; by 1 August, By-Law 3.2). Started from last year's form; names every seat the club has under its own by-laws, with the four the 2009 template names (president, vice-president, secretary, treasurer), of which the by-laws derive Federation seats from the president alone, and any programme seats (§3.4). Submitting is the By-Law 3.2 filing; the office marks it received and the club's standing pill turns for the year. *Affiliation approval (3.1) is a separate dated act by whoever the Board names — open, §6.*
2. **Seat the Federation's lists from the form** (platform). The Council of Chapter Club Presidents, the Board roster (6.2.2), the Membership Committee seat (8.12.1), the magazine's correspondent, the programme seats. Each list is read, never retyped; a change of officer mid-year is a dated change on the form and flows the same way.
3. **Keep the roster** (secretary; continuous). The two standings, households, groups, follow-ups, the secretary's queue (§3.2).
4. **Run the events** (officers; as they come). §4.2.
5. **Run the treasurer's month** (treasurer; monthly). Collect, close, remit, reconcile (D1, built); review the club statement when a run is issued (D57, §5).
6. **Prepare the Convention** (president and officers; yearly). The delegation from certified members (9.1.3, 9.1.4), handed to the convention workflow; the host bid if the club is bidding (P8); the Mid-Year the same way.
7. **Report to the Council** (president; twice a year at least, 10.5.1). The club's dashboard counts are the report; nothing is retyped.
8. **Hand over** (outgoing and incoming officers; at the end of the officer year). A dated change of seat on the form; the statement balance, open follow-ups and the events calendar carry to the new seat; nothing is copied or exported. Grants to the old seat end the same day (a design choice: a grant is a dated (person, role, scope), Four-Lens §6; the hand-over ends the outgoing grant on the day of the change).

Rules: the president must be in good standing of club and Federation (6.2.2, 6.2.3, 4.3.1) and other seats follow the club's own laws (3.1); the Federation reads counts, never names (Breeze Parity §3, B1 as built; the clubs page in `reporting`), subject to the By-Law 7.9.3 question (§3.3); no free-text note on a person except a follow-up's one completion note (Breeze Parity §4 r2); nothing automatic without a named rule (Breeze Parity §4).

### 4.2 Club events

Built in B2 as the record describes (workflow `events`): one event row with one scope, published from the club lens; recurrence as a series; eligibility by group; a check-in screen for signed-up and walk-up; attendance per event and per person; "missed the last N" raises a follow-up by name; a child leaves only with a standing holder or someone on the R6 release list; volunteer roles per event (B2b, not built). What the clubs' own records add (the SOP, the presidents' meetings): a standard monthly meeting is an event with an agenda template; a club's annual event (a festival, a night out, a luncheon) is a ticketed event whose money is the club's (D1 treatment 3: taken on the platform it is held and remitted to the club on the statement; taken off the platform it never enters); a shared national club night on one day by video call is one Federation event cross-listed to every club, which the record already allows (cross-listing never moves the money). The club event playbook the presidents asked for is content the Federation publishes, not a platform object.

Open from Breeze Parity §5 q5: whether any club prints security codes for child check-in today. B2's release list is the platform's answer; if a club relies on printed codes the release list is their blocker, not a nicety.

### 4.3 Club giving (B3) — gated

The question (Breeze Parity §5 q3; §3.3 above): whether a gift to a club's own purposes is taken through the platform onto the club's books, or the club keeps its own processor and the platform holds only the club–Federation statement. The intakes show every club keeping its own books and processors today. Both answers are designable; neither is in the record.

If yes: the club's purposes are a caller of the one payment door, no fifth door (Payments architecture); the treasurer's giving desk; the member's statement per club; the club ledger profile's agency-against-revenue treatment applied; a purpose outside the club's entity refuses by name; pledges deferred to the campaign template. The receipt names the club and its own tax status, which the platform must hold per club (the SOP suggests 501(c)(7); some clubs are pursuing 501(c)(3)); a club with no status on file gets no receipt text, and the platform says so.

A yes has two shapes (Breeze Parity §1a, Giving). Breeze gives each club its own processor account under the club's own EIN and bank account. The one-door design can either (a) take the club's gifts on the Federation's account and hold and remit them as the club's, as D1 treatment 3 already does for platform-collected club event receipts, or (b) carry a per-club merchant account under the club's EIN, which the payments architecture does not contemplate and which would put each club's processor credentials and tax status in the platform. Shape (a) passes every club gift through a Federation account first and needs the CPA's view (Q-3); shape (b) is a design change. *Neither is chosen here.*

If no: the platform records club attributions on gifts to the Federation and the affiliates (D57, J8) and nothing of the club's own giving; the club statement (§5) is the only money object between them.

Either way By-Law 11.1.4 applies: a club's appeal for a project the Federation has already undertaken needs the Board's and Executive Committee's authority. The platform can list the Federation's active projects beside a club's appeal; who checks is not written.

### 4.4 Moving a club from Breeze (B4) — a workflow of its own

Written as `club-migration` in the site's workflows, from Addendum 2 §3.4 and Breeze Parity B4, with the intakes' finding that about ten clubs are on Breeze and the rest use other tools or none:

1. **Choose the club and name its owner** (Federation staff with the club president). One club at a time; a named owner on each side; the order of clubs in §8.
2. **Connect** (the club's Breeze Account Owner, the only holder of the key, gives read-only API access; the key is a secret held by the platform, never in the repo).
3. **Extract** (platform): people, families, tags, events, attendance, giving, and the custom fields as found, into staging rows. Nothing is written to Breeze. The extract reports which custom fields the club used (Breeze Parity §5 q2 is answered per club here, not in advance).
4. **Reconcile** (match-queue reviewer, then the club's secretary): identity resolution against the register; the review band goes to the merge queue; no pair is merged by software.
5. **Parallel run** (the club's officers; two to four weeks): both systems live, the platform read-only for the club; officers verify their own roster, groups and events and record what the resolution could not see.
6. **Sign off and cut over** (club president and treasurer; a dated decision): writes move to the platform; Breeze becomes read-only.
7. **Archive** (Federation staff): the final export is kept on the drive (D66); the subscription is the club's to cancel.

Rules: nothing is written to Breeze, ever; a club's Breeze data is seen by that club's officers and the reviewer, by nobody else; a person who exists in Breeze and not on the register enters as a contact record or a club member as the officers decide, never as a national member (membership is the Federation's to grant, Article IV); giving history from Breeze enters only if B3 is answered yes, and then as the club's history; attendance history enters as the club's record. Children in Breeze enter under R6 or not at all.

A club that is not on Breeze follows the same path from a spreadsheet: steps 3 to 7 with the extract replaced by an upload, and the same rules.

### 4.5 Texting (B5) — gated

Part of `communications`, not a workflow of its own. The consent model is built per channel; the provider, the budget, and who registers the Federation's brand for carrier registration are David's (Breeze Parity §5 q1). The presidents' meeting asked that texts be branded locally; that is a per-club sender name on one provider account, which the design can hold once a provider exists. Until then the platform refuses to text and says why. Breeze itself texts one way from a shared short code with no sender branding (Breeze Parity §1a, Communications), so a shared short code through a provider is the second route beside a registered brand on a long code, and whether either carries a per-club sender name is a question for the provider; the clubs' texting consent statuses (Enrolled, Blocked, Do Not Text) are consent evidence per channel and move with the club (§8.3).

### 4.6 Forms (B6) — a question, not a slice

What clubs built in Breeze forms beyond an event signup, a join and an application (Breeze Parity §5 q6) is unknown until the extract (§4.4 step 3) reports it club by club. Each form found is classified against the existing doors (event, join, application, consent, volunteer interest) and only a real remainder opens B6. The deep read of 1 October (Breeze Parity §1a, Forms) narrows the question: Breeze's own documented uses are event sign-ups, interest and join forms, and elections run on a form with no electorate. The first two are existing doors; a club vote belongs to the voting module, whose electorate is certified (By-Law 9.1.4; D4 for the channel), and never to a form.

### 4.7 What sprint 3 changes in the site's data

- `workflows.yaml`: `club-management` steps rewritten as the officer year; a new workflow `club-migration`; `events` gains the standard meeting, the club's ticketed event and the cross-listed national club night; `communications` gains the per-club sender name under B5; `club-share` unchanged until §5.
- The experiences `club-president`, `club-officer` and `club-treasurer` list `club-migration`.

## 5. The club–Federation statement (sprint 4)

D57 adopted the rule: one statement per club, every amount a club pays or receives through a Federation or affiliate programme, each programme setting its own terms, a club attribution on any gift. This section designs the object. It is the design note P10 promised; a build session takes it from here. No figures appear; every term is the programme's to set and the register's to hold.

### 5.1 What the statement is

One ledger account per club per holding entity, on the funds ledger, with the club as the counterparty. A statement is a dated run over those accounts: every line since the last close, the balance each way, and the carry-forward. It extends the D1 remittance statement (built) rather than replacing it: dues remitted are its first line type.

The statement is between a club and an entity. Because a club deals with AFRP (dues, convention, grants to clubs, advocacy travel), with ARFECF (camp rebates, Leadership Ramallah and Project Hope travel shares, Arabic volunteers) and with ARFHSN (Care co-funding, Medical Mission club gifts), a club has up to three accounts and sees them on one page, totalled per entity and never across entities. Money never nets between entities: a club owed by ARFECF and owing AFRP settles twice (a design choice of this note, following the one-account-per-entity shape of the Multi-Entity Ledger and D55's per-entity holding; no decision says it). That is the answer to the `club-share` open item "how an amount moves when the paying entity is ARFECF or ARFHSN": the same way, on that entity's account.

### 5.2 The line types

Each line carries: the programme, the term it arises under (a register row the programme committee sets, with a date and an authority), the direction, the holding entity, the trigger that raised it, who recorded it, the evidence link (drive, D66), and the member or event it concerns where one exists (held, never shown on the club's statement by name where the person is a minor or a donor).

| Line type | Direction | Entity | Raised by | Source of the term |
|---|---|---|---|---|
| National dues remitted | club → AFRP | AFRP | the treasurer's remittance run (D1) | D1; the remittance cadence and minimum are open (Ledger §8 q4) |
| Camp rebate or family aid passed through the club | ARFECF → club, or club → family through the programme | ARFECF | camp close: the attended list per club | the camp committee's term; today three clubs give rebates on their own and the committee wants pooled club funds (Q: the term is not written) |
| Leadership Ramallah travel share | club → participant, recorded against the club | ARFECF | acceptance of a participant from that club | the programme's rule: the Federation pays hotel and part of travel, the club about half of travel; a club that cannot contacts the Federation |
| Project Hope and exchange-mission travel share | club → participant | ARFECF | the same | the programme's rule, where one is written |
| Dabke and Mid-Year youth travel | AFRP → troupe, club → troupe | AFRP | the Convention or Mid-Year event | a split between the Federation and the club, minuted for the Convention dabke competition (2024), and a Mid-Year troupe fund with a ceiling (2020); neither is a written programme term (Q-47) |
| Day of Action travel | AFRP → first-time attendee | AFRP | acceptance | the programme's rule (first-timers' hotel and part of travel); recorded against the club for the count, no club money |
| RBPN and programme event reimbursement | AFRP → club | AFRP | the event's close | the programme's term |
| Convention settlement | AFRP → host club, after the Federation's share, the holdback and any breach costs | AFRP | the event's close under the host agreement (D59, By-Law 10.1.6); the final accounting within the agreement's period and never later than By-Law 10.1.7's 120 days | the host agreement, signed before the Convention |
| Mid-Year settlement | the same shape | AFRP | the same | the same |
| Ad-book or sponsorship share | AFRP → host club, or host club → AFRP | AFRP | the event's close | the host agreement; a percentage back to the local club has been proposed and not decided (`club-share` open item) |
| Grant to a club | AFRP → club | AFRP | a Board decision (the General Fund's club initiatives line) | the Board's decision, by number |
| Care co-funding | club → ARFHSN | ARFHSN | the club's gift or pledge against a grant (D63) | D57, D63; listed as the club's share on the grant |
| Club event receipts collected on the platform | AFRP → club (remitted) | AFRP | the event's close | D1 treatment 3: platform-collected receipts are federation-held and remitted; off-platform receipts never appear |
| Club funds raised for a Federation project | club → AFRP → the project (a conduit) | AFRP | the appeal's close | By-Law 11.1.5; D1 treatment 4: a conduit, neither club revenue nor agency |
| Club gift to a Federation or affiliate purpose | club → entity | any | the gift, receipted by the entity (D56; D55) | D57 (attribution) |
| Member gift attributed to the club | member → entity, attributed | any | the donor or the appeal names the club | D57, J8; counted on the club's statement as attribution, never as the club's money |

Sixteen line types. A line type the record does not hold does not exist on the statement; a programme that wants one asks its committee for a term and the register gets a row. That is "each programme sets its own terms" made concrete.

### 5.3 The run and the close

1. The programme coordinator or the treasurer records a line when it arises; the platform records the automatic ones (dues on the remittance run; attributions on gifts; the settlement from the event's close).
2. The Federation treasurer approves a statement run per entity on the cadence the Board sets (open: Ledger §8 q4 and q7 — monthly with a floor is modelled; nothing is decided).
3. Each club treasurer sees the run, confirms it or raises a query on a line. A query opens an item with an owner (the programme coordinator for a programme line, the Federation treasurer for a settlement) and a clock; the line is held, not removed; the rest of the statement settles.
4. Settlement is a payment each way per entity, recorded against the run; a balance under the floor carries forward.
5. A closed run is immutable; a correction is a new line on the next run that names the one it corrects.

### 5.4 Who sees what

- The club treasurer and president: their club's statement, every line, the evidence links.
- The club ambassador for a programme: that programme's lines on their club's statement.
- The programme coordinator: that programme's lines across all clubs.
- The Federation and affiliate treasurers: every club's statement for their entity.
- The Federation roll-up (§10): per club, the balance each way per entity and the count of open queries, under the floor like every count.
- A member: nothing of the club's statement. Their own gift with its attribution is on their own giving record.
- Nobody: a line that names a minor or a donor is shown on the statement by reference (the event, the count), with the name visible only where the R6 authority model or the donor's consent allows.

### 5.5 What this settles in the record, and what it leaves

Settled by design (no new decision needed): the shape of the object; that entities never net; that a query holds a line and not a statement; that attributions are counts, not money; that the host agreement is the source of a settlement line (D59).

Still a decision: the remittance cadence, minimum and sign-off (Ledger §8 q4, q7, to the Board or the Finance Committee); whether the Federation bears the processing fee or the club (q2); the camp rebate term (the camp committee); whether a share of the ad book goes to the host club (the Convention Innovation Committee to the Board); and B3 (David), which decides whether a club's own giving appears beside this statement or not at all.

### 5.6 What sprint 4 changes in the site's data

- `workflows.yaml`: `club-share` moves from "Proposed, not designed" to "Designed" with this section as its design; the entity question closes; steps gain the query hold and the immutable close; module named (`ledger`, `clubs`).
- The crosswalk's P10 row points here.

## 6. Club governance (sprint 5)

What the by-laws say a club is, and what the platform does with each clause. Everything in this section is built on the 2024 text and stands only while it does: the 2026 restatement (Q-33, deferred and under Board review) would drop the affiliation and weighted-delegate articles, seat five elected chapter representatives instead of every president, and define standing on AFRP dues alone. Each item below says what the restatement would change, so a build session can see the gate.

### 6.1 The club register

A club exists on the platform when the Board's list says so. The record holds three counts (seventeen on the Federation's operating list, eighteen per-club voting lists, nineteen with the edge cases); the Hub seeds eighteen. The platform's register carries, per club: its name and city; its state of incorporation and tax status as the club states them (the SOP suggests one status, some clubs pursue another; neither is verified by the platform); a link to its own by-laws on the drive (D66); its affiliation state for the year (§6.2); its region for ARFECF seats (§6.8); the 10.1.1 Convention region (one of the three the by-law lists by city, or "no region under 10.1.1" for an unlisted city — P8 §2, Q-89), beside the ARFECF region of §6.8; its ledger profile (§5); and its lifecycle state — active, dormant (D6), dissolved (15.1.1: assets revert to the Federation). The edge cases go on the register as rows with a note, not into code (Hub record item 9). In practice (research, 2 Oct 2026), public filings show the chapter clubs as **separate exempt organisations**: large clubs as 501(c)(7) social clubs, one revived club as a 501(c)(3), and at least one club with a sister 501(c)(3) foundation beside it. Whether the register records each club's state entity, federal subsection and any sister foundation, and who keeps them current, is Q-227 (P20-J4). The public annual report for 2024–25 counts fourteen active chapters, a fourth count beside the three above; which count is the Federation's is Q-229. *Open: the Board's list (Breeze Parity §5 q8).* The restatement would not change this.

### 6.2 Affiliation and the officers form

By-Law 3.1: a club "shall affiliate … with the approval of the A.F.R.P."; its laws must not conflict with the Federation's; it must stay in good standing with state and federal regulation. By-Law 3.2: the affiliation form, all officers with contact details, to the office by 1 August. By-Law 6.4.1: only clubs that have complied with Article III seat their president on the Council.

The platform: the officers form is the filing (§4.1 step 1); the office marks it received; the club's standing pill shows filed and approved with dates; the Council and the Board roster (6.2.2) read from it. What the platform refuses to guess: who gives the approval (a Board vote, an officer's signature, the office's acceptance), whether approval is once or yearly, and what a late or missing form costs (the Council seat for the year is the only consequence the text implies). The intakes found no affiliation forms on file for any year. *Q-40.* The restatement would drop the article; the form would become the office's practice, not a filing.

### 6.3 Standing at the club, and the conjunctive test

By-Law 4.3.1: good standing requires the Federation's dues and the club's (if any) for the current year. The platform already shows scoped standing (national and club lapse independently) and applies the conjunctive test where the by-laws use it (a seat, a vote), with D6's override for a dormant club and D1's rule that standing starts at collection. The club lens shows both standings on the roster; the member sees both on their home. What the platform does not decide: whether a member may hold two club memberships and which club's standing counts for 4.3.1 (the texts speak of one club: "his/her AFRP and Local Club (if any)" (4.3.1), "the Chapter Club … in his/her locality" (6.2.3), "his/her Chapter Club" (9.1.3); the Hub allows several); who decides a move between clubs; and the minor-in-two-households attachment (Rules Register R4, open to the Membership Committee). *Q-41.* The restatement would define standing on AFRP dues alone and this section would shrink to the display.

### 6.4 Delegates and the Convention

By-Laws 9.1.3 and 9.1.4: each club sends one or more delegates; each casts a share of the club's certified members' votes; a certified member present may vote independently and is deducted from the delegation; a club's votes are capped at its members certified by the Selection Committee. The platform: the delegation is selected by the club's officers from certified members (§4.1 step 6; *since 2 October 2026:* the text is silent on how delegates are chosen (9.1.3), and the Legal Advisor's description to the Board in May 2026 has the community's certified members vote on them. The Convention operations note therefore records each delegation as the club's dated act with its method stated, which may be officers' selection, a members' vote or the club's own by-laws, and refuses none. Presence is marked at the desk, and only a present delegate carries a weight (P22 §6, CV4; Q-37; P20-D6)); the weights are computed from certification, never typed; an independent voter extracts at the opening (D5, reopened: when weights fix is still undecided); the convention workflow credentials the delegation. What is not written: who certifies the per-club lists, the cut-off date, the quorum (Q-37, open; it waits on Q-33). The restatement would make Convention votes advisory and drop weighted delegates, which would retire this section.

### 6.5 The Council of Chapter Club Presidents and the Board

By-Laws 6.2.2, 6.4.1, 10.5.1 and 8.4.1: every compliant club president is a voting Board member and a Council member; the Council, chaired by the Deputy President, meets at least twice a year including the Mid-Year and the Convention, and works with the Executive Director on club programmes. In practice the Council meets monthly (the presidents' meeting, 2020–2026) and the 2020 letters set an attendance expectation that no record tallies. The platform: the Council roster derives from the officers forms; a Council meeting is a Federation event with attendance (B2), so attendance is a count the Deputy President can see; the agenda and minutes live on the drive. 8.4.1 seats all presidents on the Council and 6.4.1 only those of clubs that have complied with Article III; the platform follows 6.4.1 for the seat and shows a non-compliant club's president as "not seated: Article III" rather than omitting them (a drafting item for the Constitution Committee, added to Q-40). The platform does not enforce the 2020 attendance rule because no by-law or Board rule holds it. *Q-42: whether the attendance expectation is a Board rule.* The restatement would replace the presidents on the Board with five elected chapter representatives; the Council would remain a committee.

### 6.6 The club's own laws, and the templates

By-Law 3.1 lets each club adopt its own governing laws provided they do not conflict with the Federation's. The 2009 club by-laws template and the 2025 club SOP are the Federation's offers; the presidents asked in 2026 for by-law templates that speed club tax-exempt applications. The platform holds a link to each club's by-laws and the date they were last filed with the office, nothing more; drafting is the Constitution Committee's workbench, and conflict-checking a club's by-laws against the Federation's is a reading, not a computation. The SOP's membership tiers (young adult, youth, child) are the club's own classes; they do not map to the Federation's and the platform keeps them as club group memberships, not as standing. *Q-43: whether a club's tiers are the club's to define.* In practice (research, 2 Oct 2026), a club's 2026 by-laws draft admits adults who derive their origin from Ramallah *or* who consider themselves part of the Ramallah community and support the club. That is wider than By-Law 4.1.1. No club by-law found mentions affiliation, delegates or per-capita dues. What such a club member is on the platform, and whether such a law conflicts under 3.1, is Q-226.

### 6.7 Solicitation and dissolution

By-Law 11.1.4: no club or member solicits in their own capacity for a project the Federation has undertaken without the Board's and Executive Committee's authority. The platform can show a club's appeal against the Federation's active projects at the moment the appeal is created (B3, if yes) and record the authority as a Board decision number; it cannot police an appeal made outside the platform. By-Law 15.1.1: on dissolution a club's assets revert to the Federation; the platform records the lifecycle change and the D57 balance and holds the asset list as a drive link.

### 6.8 Clubs in ARFECF's governance

The 2015 ARFECF by-laws seat the Foundation's Board across three regions, each defined by a list of clubs, with a cap on overlap with the AFRP Board (J4; EC-OV-1 superseded). The club register carries each club's region as a register row the ARFECF Board sets; the composition check reads it. Nothing else of a club touches the affiliates' governance; ARFHSN's by-laws (2017) give clubs no part in its governance; their one mention of a club is the Detroit club's building as the office's location.

### 6.9 Under the Q-33 gate

If the restatement is adopted: §6.2 and §6.4 are retired, §6.3 shrinks to the display, §6.5 changes the Board roster, and D4, D5, scoped standing, Article XVII and By-Law 3.2 are outranked (Q-33). Until then the 2024 text is the law and every item above is built on it, labelled with its by-law. A build session should build §6.1, §6.6, §6.7 and §6.8 (unaffected) first, and §6.2–§6.5 as the 2024 text says with the gate in the slice row.

### 6.10 Questions this plan raises, numbered

Added to the site's questions as Q-40 to Q-47 by this sprint (the governance agent's numbering; the Hub record's own open items from `08-OPEN-QUESTIONS` are still to be numbered after these).

*Since 2 October 2026:* the research round raised five more club questions, Q-226 to Q-230, now on the site's question list. Q-226 asks about a club's membership rule that is wider than 4.1.1 (§6.6). Q-227 asks about the register's legal columns (§6.1). Q-228 asks about clubs that give directly to Ramallah projects (§7.1). Q-229 asks which count of clubs is the Federation's (§6.1). Q-230 asks whether the Breeze roll-out is a Federation programme. A sixth, Q-237, asks about the club president's view of members' contact details. The portal shows names and contact details today, while this plan's rule is counts and per-field consent (§9.2, §10.1); it joins Q-44 and Q-46.

| Q | Question | Owner | Raised in |
|---|---|---|---|
| Q-40 | Who approves a club's affiliation, how often, and what a late officers form costs; 8.4.1 (all presidents) against 6.4.1 (compliant clubs) on the Council | AFRP Board · Executive Director · Constitution Committee | §3.1, §6.2, §6.5 |
| Q-41 | Whether a member may hold two club memberships; which club's standing counts; who decides a move | Membership Committee · AFRP Board | §3.2, §6.3 |
| Q-42 | Whether the Council's monthly meeting and its attendance expectation are a Board rule | AFRP Board · Deputy President | §6.5 |
| Q-43 | Whether a club's own membership tiers are the club's to define | Membership Committee | §6.6 |
| Q-44 | The Executive Director's access to Chapter Club records (7.9.3) against the counts-only rule: a named purpose and an audit line | AFRP Board · Legal Advisor | §3.3 |
| Q-45 | Whether the club or the programme committee appoints a club's programme seats | AFRP Board · programme committees | §3.4 |
| Q-46 | Whether a member may know a follow-up exists about them; what a member who has never signed in is deemed to have consented to | Legal Advisor · Membership Committee | §3.5, §9.2 |
| Q-47 | The club statement's terms that no committee has written: the remittance cadence, minimum and sign-off; who bears the processing fee; the camp rebate term; the dabke travel term; an ad-book share for the host club | Finance Committee · camp committee · Convention Innovation Committee | §5.5 |

Breeze Parity §5's eight questions stay as they are (David's and the Board's) and are not renumbered.

## 7. Clubs inside the programmes (sprint 6)

Every programme page on the site already carries "the clubs' part" as the intakes found it. This section turns each into the three platform objects a club's part can be: a **seat** (the club ambassador in that programme, §3.4), a **line** on the club statement (§5), and a **count** in the Federation's roll-up (§10). Where a programme's record gives the club no part, the table says so and the platform offers nothing; a committee that wants one writes it. Nothing here adds a rule.

### 7.1 The table

| Programme (entity) | The clubs' part, as recorded | Seat | Statement line | Count per club | Missing |
|---|---|---|---|---|---|
| Camp Ramallah (ARFECF) | Several clubs give rebates or aid to families; the application records the camper's club; pooled funds and volunteer chaperones proposed, not adopted | Camp liaison: sees the club's campers and households, under R6 | Camp rebate (ARFECF → club, or through the club to the family) | Campers per club per year (D67's example) | The rebate term (Q-47); whether the liaison sees minors by name (R6: only if the authority model names them) |
| Arabic Program (ARFECF) | Presidents recruit native-speaking volunteers; no money through clubs | Volunteers' lead: sees the club's volunteers and their sessions | None | Volunteers and learners per club | Nothing; the committee's own decision |
| Scholarship (ARFECF) | None in selection | None | None | Scholars by club (the scholar's club at award) | Binding rule 2: applicant data never enters; the count is of recipients only (D61) |
| Project Hope (ARFECF) | Clubs nominated in 2013; now one recruitment channel among several | Outreach contact: sees applicants' count from the club, never the applications | Travel share, if the programme writes one | Participants per club per year | Whether the club co-funds travel as for Leadership Ramallah (not written) |
| Leadership Ramallah (entity to confirm) | The club covers about half of travel; a Young Leaders committee of club representatives | Travel coordinator: sees the club's accepted participants and the share due | Leadership Ramallah travel share (club → participant, against the club) | Participants per club | The holding entity (D55 silent); the Young Leaders seat is a committee seat, not a club seat |
| Emerging Leaders *(since 2 Oct 2026: no programme by this name is evidenced, Q-178; P25 §2.2)* | Not stated | None | None | None | Q-178 |
| RBPN (AFRP committee) | One ambassador per club for two years; hosting clubs reimbursed; regional gatherings through clubs | RBPN ambassador, the one seat the record names with a term | RBPN event reimbursement (AFRP → club) | Members listed, events hosted per club | Whether the two-year term is the committee's rule or the club's appointment (Q-45) |
| AFRPWorks (AFRP) | Not stated | None | None | None | The working group names it (D64) |
| Congressional Outreach (AFRP) | A club representative proposed in 2020, not adopted; clubs host district meetings | None adopted; a district host is an event role, not a seat | None (advocacy is AFRP's, D65) | District meetings hosted per club | Whether the 2020 representative is wanted |
| Day of Action (AFRP) | No club role in recruitment or logistics | None | Day of Action travel (AFRP → first-time attendee), recorded against the club for the count only | Attendees per club | Whether clubs recruit; the record says no |
| Exchange Mission (ARFECF) | Clubs host a yearly fundraising dinner with an alumnus speaker; no part in selection | A dinner is a club event cross-listed to the programme, not a seat | Club gift to the programme (club → ARFECF), attributed | Dinners held and gifts attributed per club | The gift's path if B3 is answered no (the club gives from its own books; the platform records only the receipt); By-Law 11.1.5: club-raised funds for a Federation project route through headquarters (D1 treatment 4) |
| Preservation Project (entity to confirm) | Presidents recruit volunteers and photographs; clubs cover the exhibit room at Conventions | Volunteers' lead | Exhibit cost, if the host agreement carries it (D59) | Items contributed per club | The entity; the exhibit term in the host agreement |
| Magazine (ARFECF-held) | Clubs promote subscriptions; a correspondent per club sends photos and reports | Magazine correspondent, from the officers form | None | Subscriptions and submissions per club | Nothing |
| Bookstore (AFRP) | Not stated | None | None | None | — |
| Medical Mission (ARFHSN) | Clubs run fundraisers and brief members for appeals; co-funded grants list each club's share | A club appeal is a club event; co-funding is a line | Care co-funding (club → ARFHSN); club gifts attributed | Gifts attributed per club | Whether a club appeal on ARFHSN's behalf needs 11.1.4 authority (it is a project the Federation has undertaken); By-Law 11.1.5: club-raised funds for a Federation project route through headquarters (D1 treatment 4) |
| Women to Women (ARFHSN sub-fund) | A representative in each city wanted (2025 SWOT), none written | None until written | Club gift, attributed | Gifts attributed per club | The seat, if the committee writes it |
| Senior Living (to confirm) | Not stated. *Since 2 October 2026:* in 2026 clubs were invited to promote memorial gifts and to consider a club legacy gift recognised by signage at the Foundation's home | None | A club gift made through the Federation's pass-through purpose, as a line with the recognition request (P23 §9.4, RL6), gated on Q-205; a gift made directly to the Foundation is outside the platform | None | The entity; whether Senior Living is a Federation programme at all (Q-203); Q-205 |
| Family Tree (AFRP) | Not stated | None | None | Members with tree links per club | Nothing: the tree is per person and per household, never per club |
| Convention (AFRP, host club under D59) | The host club runs it under the agreement (10.1.6, D59); bids in writing by the Mid-Year two years ahead (10.1.1); the host's share settled after (10.1.7) | Host committee seats are event roles on the Federation's event | Convention settlement, ad-book share, exhibit and other agreed terms | Registrations, delegates, and the settlement balance for the host | Q-34 → D59 done; the ad-book share (Q-47) |
| Relief Fund (*entity AFRP, D83, 3 Oct 2026; until then not stated, Q-109*) | Fundraising only through the Federation's procedure. *Since 2 October 2026:* in practice (research, 2 Oct 2026) the Young Leaders ran a needy-families drive across the clubs with a per-club tally and a winning club, and some clubs give directly to Ramallah projects | None | Club gift, attributed; a drive across the clubs as one catalogue purpose with an end date and a per-club tally of counts and amounts (P23 §5, RL4) | Gifts attributed per club | 11.1.4 applies by name; 11.1.5 routes club-raised funds through headquarters (D1 treatment 4). Which fund receives a drive, and whether it needs 11.1.4's authority, is Q-180. Whether "one channel" becomes a rule for a club's own giving is Q-228; nothing blocks or records it until then (P20-I7) |

### 7.2 What the table shows

- Only one programme names a club seat with a term today (RBPN's ambassador). Every other club seat is a practice the committee relies on and the by-laws do not know. Q-45 covers all of them with one answer.
- Five programmes move money with a club (camp, Leadership Ramallah, RBPN, the Convention and the Mid-Year, the Care funds); the rest move none. The statement (§5) has a line type for each, and no programme needs a new one.
- The counts are the first-year outcome baseline D67 asked for, taken per club: campers, scholars, participants, volunteers, gifts attributed, events hosted. They are the Federation's view of a club's part in the Federation's work, which no document today can produce.
- Three programmes still have no holding entity (Leadership Ramallah, Preservation, Senior Living), and until a Board confirms one the statement's entity column for their lines is blank and the line cannot settle. That is the right behaviour: the register is silent, the platform refuses to guess.

### 7.3 What sprint 6 changes in the site's data

- `programmes.yaml`: each programme's "clubs' part" gains one closing line naming the seat, the statement line and the count the platform offers it, or "none on the platform" where the record gives the club no part.

## 8. The migration, club by club (sprint 7)

Addendum 2 §3.3 said the hard half is not the code: each migration is a relationship with officers who chose Breeze. This section is the programme for those relationships, and the data rules each one follows. The workflow is `club-migration` (§4.4); this is the plan around it.

### 8.1 What has to be true before the first club moves

| Readiness item | State on 1 October 2026 | Who closes it |
|---|---|---|
| Parity for what the club uses daily: roster, households, groups, follow-ups, events, check-in, attendance | Built (B1, B2) | — |
| The second half of B2 (B2b): volunteer roles with assign, invite, reminders and blockout dates; kiosk self check-in; check-out times; headcount | Not built | build session |
| Email to a club's list through a real provider | Waits on slice 5 (provider) | David |
| Texting (B5) | Gated: provider, budget, carrier registration | David |
| Club giving (B3) | Gated: David's answer; needed only if the first club takes gifts in Breeze | David |
| The import path: connector, extract, staging, identity resolution, merge queue | Connector and extract from the Portal era; staging, resolution and the parallel-run report not built (B4) | build session |
| The secretary's queue (JC-022) | Not built | build session |
| The club's officers on the officers form (§4.1 step 1) | Not built (P18-1) | build session |
| A named owner on each side, and the club's Breeze key in the platform's secret store; only the club's Breeze Account Owner holds the key, and a club whose owner has left recovers ownership first by Breeze's paper process | — | David with the club president |

Nothing texts, nothing takes a gift, and no club should be asked to leave a system that does either until the gates above are answered. The first club should therefore be one whose Breeze use is roster, groups, events and email, and whose giving runs elsewhere.

### 8.2 The order of clubs

Addendum 2 proposed one enthusiastic mid-sized club first, then the clubs whose Breeze is already failing, then the rest; Addendum 2 reported three connector states as failing in the Portal era, and whether any real club's Breeze is failing today is not in the record and is for the Council to say. The intakes add that about ten clubs are on Breeze and the rest are on other tools or none. The plan:

1. **One pilot club**, chosen by David with its president (Breeze Parity §5 q4), that uses Breeze for roster, groups and events and not for giving or texting; the parallel run is the proof the rest will ask for.
2. **Any club whose Breeze is failing, as its president reports**, next: they lose nothing by moving.
3. **The clubs not on any system**, in parallel with 2, by spreadsheet upload: they have the least to reconcile and the most to gain.
4. **The remaining Breeze clubs**, in the order their presidents choose at the Council, after texting and giving are answered, because those clubs use them.
5. **The clubs on other tools**, with the same path as 3.

One club at a time in each stream; two streams at most. Each club gets a named Federation owner and a named club owner (usually the secretary), a start date, and a parallel-run end date set at the start. The Council sees the order and each club's state (not started, connected, reconciling, parallel, cut over, archived) as a Federation count on the clubs page (§10).

### 8.3 The data that moves, and the rules it obeys

| Breeze object | Enters as | Rule |
|---|---|---|
| People | A match to a person on the register, or a new club member or contact record as the officers decide (*since 2 October 2026:* a non-member enters only as a staging row, with no consent row created, and becomes a club prospect role only when Q-70's migration option and Q-76 allow; P21 §7.5, §10, CR7) | Never a national member by import: membership is the Federation's to grant (Article IV). The register's identity resolution proposes; the merge queue and the officers decide; no pair is merged by software. Breeze has no membership object: a "Status" or "expires" custom field is evidence for a standing proposal, never a standing. An archived person enters as an ended club membership, not as an absence. |
| Families | Household proposals | A household on the register is a stronger object than Breeze's (R4); the proposal is confirmed by the officers; a minor in two households stays OPEN (Rules Register R4). Breeze's "Child" role is not an age: the register's minor test is the birthdate under R6; a Breeze family is one per person and its data is the head's. |
| Custom fields | Reported per club at the extract; each field classified as standing, family, consent, a group, or a remainder | Standing, family and consent map to what the register holds; a list-like field becomes a group; anything that is a note about a person is **not imported** (no free-text notes, Breeze Parity §4 r2); a remainder is a question on the parallel-run report, not a new field. |
| Tags | Club groups (B1), with their folders | A tag whose name carries a leader's name loses the name (the leader seat is a field); a tag that is really a programme roster (the dabke troupe) becomes a group now and may become a programme seat later (§7). A Smart Tag (derived hourly from profile fields) imports as the filter that defined it, noted on the group, not as a frozen list; a locked tag that stood for "active members" is standing the register already holds. |
| Events and attendance | Club events and attendance records (B2) | History enters as the club's record; the member sees their own attendance. Attendance is not in Breeze's account export and moves only through the API per event or per-series reports, taken before anyone edits a series (an edit wipes future check-in data); anonymous headcounts enter as counts on the event, never as people. |
| Check-in security codes | Not imported | The release list under R6 replaces them. |
| Follow-ups | Open follow-ups enter as open follow-ups with their option and assignee; completed ones enter closed | A follow-up's free-text note is kept only if it is the completion note; nothing else. |
| Forms and entries | Reported per club; each form classified against the existing doors (§4.6) | Entries that are event signups or joins enter through those doors; a remainder is a question. |
| Giving | Only if B3 is answered yes, and then as the club's own giving history on the club's books | Never onto a Federation or affiliate ledger; never attributed after the fact. |
| Online Directory tag, opt field, private flags, Do Not Email / Do Not Text, texting status | Consent proposals, defaulting to **no** | A Breeze directory opt-in (the tag or the Yes/No field) is evidence of a display choice; a private flag on a phone or email is evidence of a contact choice for that item; a texting status of Enrolled is evidence for the text channel. Each imports unconfirmed and the member confirms display, contact and export separately (R27) on first sign-in. **Blocked (texted STOP), Do Not Email and Do Not Text import as a hard no** for that channel and are not reopened by sign-in. |
| Users and roles | Officer seats on the officers form | Admin, Standard, Limited and Check-In map to president or treasurer, secretary, read-only officer, and the `club_checkin` role; nothing maps to a Federation grant. The Account Owner is a contractual role, not a seat; it is recorded on the club's register row as the person who held the key. |
| Children | Under R6 or not at all | A child enters only through a household with an adult who holds authority; a child with no such adult in the extract is listed on the parallel-run report for the officers, never imported alone. |
| Notes, files, photos, email history, forms' structures, recurring gifts | Not imported | Notes are a case file the record has not decided to keep (Breeze Parity, refusals); files and photos stay with the archived export on the drive (D66); a recurring gift is re-authorised by the donor, never copied; the parallel-run report counts each so the officers know what will not move. |

The rows above that cite no decision — the hard noes for Blocked, Do Not Email and Do Not Text; the Account Owner recorded on the register row; headcounts as counts; a recurring gift re-authorised rather than copied; an archived person as an ended membership — are design choices of this note, each labelled so a build session can see it; none changes who a member is or what a member owes.

### 8.4 The parallel run

Two to four weeks, the platform read-only for the club. The club's officers receive the parallel-run report: every person matched and how (score band), every household proposed, every group, every custom field and its classification, every form and its door, every child and the adult through whom they entered, every remainder. They work it on the platform's screens, not on a spreadsheet, so that what they confirm is what cuts over. A weekly count of items still open goes to the Federation owner. The run ends on the date set at the start unless the officers ask for more time; it does not end early.

### 8.5 Cutover and after

Cutover is a dated decision by the club president and treasurer recorded on the club's register row. From that day writes go to the platform; Breeze is read-only to the club for a period the club chooses, then archived (the final export on the drive, D66). The club cancels its subscription only after the export is verified on the drive, because the vendor queues the account for deletion on cancellation (Breeze Parity §1a, Data policies). The club's statement (§5) opens with the dues position carried from the last remittance; nothing else carries a balance. The Federation owner closes the migration with a one-page note on the drive: what moved, what did not, what remains as a question. The Council sees one more club in the "cut over" count.

### 8.6 What a club gives up, and what it gets

The honest list, for the Council and the club presidents (goal row J5 asked for exactly this):

- Gives up: export to Excel, printed directories and mailing labels (refused by design, Breeze Parity §2; Q: §5 q7), free-text notes on people, deleting a person, a leader's name in a tag's name, texting until B5 is answered, online giving until B3 is answered.
- Gets: the member's national standing beside their club standing, the secretary's queue, follow-ups that cannot be lost, the release list instead of a printed code, the Federation's lists seated from one form, one statement of what the club and the Federation owe each other, and a club that is one among all the clubs in the Federation's view instead of alone in its own Breeze.

### 8.7 What sprint 7 changes in the site's data

- `workflows.yaml`: `club-migration` gains the readiness list and the order of clubs as its `open` and `status_note` detail; no new workflow.

## 9. Club communications and consent (sprint 8)

Clubs reach their people today through Breeze email and texting, two different mailing tools, the Federation's video-call account, group messaging, and the Federation's monthly newsletter. The record already settles the model (workflow `communications`: two senders, club and Federation, on one consent model; consent checked when the audience is built; the withheld stored by name; per-channel consent as dated rows, R27). This section says what that means for a club, what replaces each tool, and what the platform will not do.

### 9.1 What replaces what

| The club uses today | On the platform | Condition |
|---|---|---|
| Breeze email to a tag or a filtered list | A mailing to a group or a filtered roster from the acting panel, consent-filtered, with the withheld named | A real email provider (slice 5) |
| The mailing tools (two are in use) | The same mailing, with the club as sender; the list is the roster, never a copy of it | The same; a club that keeps its own tool keeps its own list and the platform does not feed it (no export) |
| Breeze texting | A text to the same audiences under the club's own sender name on the Federation's one provider account | B5: provider, budget, carrier registration (David) |
| Group messaging (chat apps) | Not replaced. A chat group is the club's own and outside the platform; the platform never posts to it and never reads it | — |
| The Federation's video-call account for club events | An event's call link on the club event (B2); the account stays the Federation's | — |
| The monthly Federation newsletter carrying club news | A club submits news to the newsletter through the magazine correspondent seat (§7); the newsletter is the Federation's send to the Federation's audience | — |
| Convention and Mid-Year mail from the host club | Sent by the Federation as the event's owner, with the host club named; the host committee drafts | D59: the Federation owns the event's registration data |
| A printed club directory or mailing labels | Refused by design (Breeze Parity §2) | Breeze Parity §5 q7: whether the Board wants a consented print purpose |

### 9.2 The consent a club works under

- Three consents per member, each a dated row: display (who may see me), contact (who may reach me, per channel), export (never granted to anyone; there is no export). A club mailing honours the contact consent for its channel; a club sees on the roster whether a member may be reached, not why.
- A member who joined through a club and has never signed in has no consent rows. The platform treats that as **no** for marketing and programme invitations and **yes** for operational messages a member must receive (a renewal notice, a receipt, a ballot) — the message classes the workflow already defines. *A design choice of this note: no decision sets the default for a member who has never signed in; added to Q-46 for the Legal Advisor and the Membership Committee.* A Breeze directory opt-in imported at migration is evidence, not consent (§8.3); the member confirms on first sign-in.
- A minor is never an audience member. A message to a household about a child goes to the adult who holds authority (R6), from the programme or the club, and the child's name is not in the subject line.
- The withheld are named to the sender and to nobody else; the count of withheld is a club count under the floor.
- A member mutes a club, or a channel, or the Federation, separately; each is a dated row and takes effect at the next audience build. A club cannot see who muted it beyond the withheld list for its own sends.

### 9.3 What the platform refuses, and why

- No export of a list to any tool, including the clubs' own mailing tools (the Four-Lens rule and the register's refusal by design). A club that wants its mailing tool keeps maintaining its own list by hand; the platform will not hand it the roster. This is the single hardest refusal for clubs and should be said plainly at the Council before the first migration, with the reason: a consent the member gave the Federation cannot travel to a tool the Federation does not control.
- No texting until the Federation holds a provider and a registered brand; a club cannot bring its own.
- No message to a person with no verified channel; "undeliverable" is reported as not tracked, never as zero.

### 9.4 What the clubs asked for that the record can give

- Locally branded texts: the per-club sender name on one account (§4.5), once B5 is answered.
- A shared club event playbook and a central programming guide: content the Federation publishes on the drive and links from the club dashboard, not a platform object.
- A national club night on one day: one Federation event cross-listed to every club (§4.2), with each club mailing its own roster about it.

### 9.5 What sprint 8 changes in the site's data

- `workflows.yaml`: `communications` gains the migrated-consent rule (an imported opt-in is evidence, not consent), the no-consent-rows default by class, the minor-never-an-audience rule, and the per-tool replacement list in its open items and sources.

## 10. The Federation's roll-up and the club view of the site (sprint 9)

### 10.1 The clubs page in the Federation lens

The Federation registry's clubs page (B1 built the first version) is the one place the Federation and the Council see every club. Every cell is a count under the suppression floor, composed so that no arithmetic across pages names a person (workflow `reporting`, S7, R43). Per club, in this order:

| Group | Counts | Source |
|---|---|---|
| Standing | Affiliated for the year (filed on, approved on); lifecycle state (active, dormant, dissolved) | §6.1, §6.2 |
| Membership | Members by national standing and by club standing; households; new this year; lapsed this year | built |
| Club life | Groups; members in groups; open and overdue follow-ups; events this year; attendance; mailings this year; withheld on the last mailing | B1, B2 |
| The Federation's work in the club | Campers, scholars, participants, volunteers, delegates, gifts attributed, events hosted — per programme, as §7's table lists them (the D67 baseline per club) | §7 |
| Money between us | The statement balance each way per entity; open queries; the last close | §5 |
| The move | Migration state (not started, connected, reconciling, parallel, cut over, archived); start and planned end dates | §8 |

Three views of the same table: the Executive Director's (every club, every column); the Council's (the same table, read at its meetings, with each president seeing their own row in full and other rows as counts); and a club's own row on its dashboard with the Federation's median beside it (the benchmark the reporting workflow already describes). A club president never sees another club's names anywhere on this page; the Executive Director's By-Law 7.9.3 access, if the Board confirms it for a named purpose (Q-44), is a separate screen with an audit line, not this one.

### 10.2 The year-one baseline, per club

D67 asked each branch for two or three counts that exist today. Taken per club they are the Federation's first honest picture of where its programmes reach: campers per club per year (Education), participants and RBPN members per club (Leadership), items contributed and tree links per club (Heritage), gifts attributed and co-funding per club (Care). The clubs page produces them; nothing is retyped from a committee's sheet. The frozen annual snapshot (`reporting`, step 5) carries the per-club table, suppressed.

### 10.3 The club view of the site

The site's audience includes the club presidents (David, 1 October 2026). A page written for them, `For club presidents` (`site/pages/for-clubs.md` → `strategy/for-clubs.html`), says in plain language what a club gets, what it gives up, the officer year, the move from Breeze, and the questions in the Council's lap with their Q-numbers. It is linked from the Strategy page's One Federation section. It carries no figures and no club's name; its detail lives in this note and the workflow pages.

### 10.4 What sprint 9 changes in the site's data

- `site/pages/for-clubs.md` (new), `site/build.py` (one page added), `site/pages/strategy.md` (one paragraph).
- `workflows.yaml`: `reporting` gains the clubs page's columns as a step.

## 11. Journeys for the club lens (sprint 10)

*Superseded in detail on 1 October 2026 by `AFRP-Club-Journeys.md` (P20), which starts each journey from what the officer does in Breeze today and absorbs the twenty below (its §M maps them). The use cases in §11.1 stand.*

The Hub tests itself with journeys: short stories rated meets, guarded, open, not built or fails, kept in `journeys/catalog.yaml` and run on CI. The club lens has two canonical journeys (J08, the treasurer's year; J14, Federation club management) and some thirty-six catalogue rows. This section derives the use cases §3–§10 imply and the journeys that would test them, as proposals for the Hub's workbench queue (the afrp-test rule: proposals, never direct edits to the catalogue). Each names the rule it tests and the class it must reach; a journey with no rule behind it is not proposed.

### 11.1 Use cases

| # | Who | Wants | So that | Rule | Lens |
|---|---|---|---|---|---|
| U1 | Club president | to file this year's officers from last year's form by 1 August | every Federation list reads from one filing | By-Law 3.2; §4.1 | club |
| U2 | Club president | to see the club affiliated for the year with the dates | I know the club's Council seat is secure | 3.1, 6.4.1; Q-40 | club |
| U3 | Club president | to select the delegation from certified members and hand it to the Convention | the weights are computed, not typed | 9.1.3, 9.1.4 | club |
| U4 | Club president | to report to the Council from the dashboard counts | nothing is retyped | 10.5.1; §10 | club |
| U5 | Club secretary | to work the queue of joins, splits, moves and reported deaths | nobody falls through and nothing is guessed | §3.2; JC-022 | club |
| U6 | Club secretary | to be refused a free-text note on a person, with the reason | the club keeps tasks, not opinions | Breeze Parity §4 r2 | club |
| U7 | Club treasurer | to see the club statement per entity with every line's term and evidence | I can confirm it or query one line | D57; §5 | club |
| U8 | Club treasurer | to query one line and see the rest settle | a dispute does not hold the club's money | §5.3 | club |
| U9 | Club treasurer | to see a line with no holding entity refuse to settle, by name | the platform does not guess an entity | D55; §7.2 | club |
| U10 | Outgoing treasurer | to hand over at year end as a dated change of seat | the balance and the open items carry and nothing is copied | §4.1 step 8; Four-Lens §6 (design choice) | club |
| U11 | Club ambassador (camp) | to see this club's campers and households and no other club's | I can gather our families | §3.4; Four-Lens §6; R6 | club |
| U12 | Club ambassador | to be refused the club lens from a programme seat, and the programme lens from a club seat | the scopes stay siblings | Four-Lens §6 | club |
| U13 | Member | to see my own club standing, groups, attendance and (if B3) statement | I know where I stand with my club | scoped standing; B1, B2 | member |
| U14 | Member | to ask to move clubs and see it land in both secretaries' queues | nobody moves me without my asking | §3.5; Q-41 | member |
| U15 | Member | to mute a club's mailings and still receive a renewal notice | operational messages reach me, marketing does not | the message classes; §9.2 (design choice, Q-46) | member |
| U16 | Federation staff | to see every club's standing, counts, balance and migration state under the floor | the Federation reads counts, never names | S7, R43; §10.1 | federation |
| U17 | Executive Director | to be refused a club's names without a named purpose and an audit line | 7.9.3 is honoured and bounded | By-Law 7.9.3; Q-44 | federation |
| U18 | Match-queue reviewer | to see a Breeze person in the review band and decide, with no pair merged by software | identity is a human decision | §8.3 | federation |
| U19 | Club officers in parallel run | to work the parallel-run report on the platform's screens | what we confirm is what cuts over | §8.4 | club |
| U20 | Club president and treasurer | to cut over as a dated decision and see Breeze become read-only | the move is one act, recorded | §8.5 | club |
| U21 | Club secretary | to have an imported directory opt-in shown as unconfirmed until the member signs in | evidence is not consent | §8.3, §9.2; R27 | club |
| U22 | Club officer | to have a child in the extract with no authority-holding adult listed for me and never imported alone | R6 holds at import | R6; §8.3 | club |
| U23 | Club officer | to be refused an export, a printed directory and labels, with the reason | the refusal is by design, not by omission | Breeze Parity §2; §9.3 | club |
| U24 | Club secretary | to text the roster under the club's own sender name | texts are local, the account is one | §4.5; B5 (gated) | club |

### 11.2 Journeys proposed for the workbench queue

Identifiers are provisional (`P18-Jnn`); the Hub's workbench assigns catalogue ids. Class is what the journey must reach for the slice that builds it to close.

| Journey | Tests | Use cases | Must reach | Slice |
|---|---|---|---|---|
| P18-J01 The officers form is the By-Law 3.2 filing | Filing from last year's; the standing pill turns; the Council, Board and Membership Committee rosters derive; a mid-year change flows | U1, U2 | meets | C1 (§13) |
| P18-J02 The president's seat is refused to a lapsed member by name | 6.2.2, 6.2.3 and 4.3.1 on the form; other seats shown, not refused | U1 | meets | C1 |
| P18-J03 The delegation is computed, not typed | Selection from certified members; weights; an independent voter extracts and is deducted | U3 | guarded until Q-37 and D5 settle | C1 |
| P18-J04 The secretary's queue | A join naming the club, a household split, a move request from both sides, a reported death; each lands, is owned, is closed | U5, U14 | meets | C2 |
| P18-J05 No free-text note anywhere in the club lens | Every surface other than a follow-up's completion refuses with the rule named | U6 | meets | C2 |
| P18-J06 The club statement per entity | Three accounts, never netted; a line per term with evidence; a query holds one line; the close is immutable; a correction is a new line | U7, U8 | meets | C3 |
| P18-J07 A line with no entity cannot settle | Leadership Ramallah's travel share before the Board confirms its entity | U9 | guarded (by design) | C3 |
| P18-J08 The year-end hand-over | A dated change of seat; balance, follow-ups and calendar carry; old grants end that day; nothing exported | U10 | meets | C1 |
| P18-J09 The ambassador sees one club in one programme | Camp liaison scope; minors as counts unless R6 names them; the sibling-scope refusals both ways | U11, U12 | meets | C4 |
| P18-J10 The member's club view | Scoped standing, own groups, own attendance; nothing of anyone else; a move request | U13, U14 | meets | C2 |
| P18-J11 Mute the club, keep the renewal notice | Message classes against a club mute | U15 | meets | C2 |
| P18-J12 The clubs page under the floor | Every column; the Council's view; a president's own row in full and others as counts; no arithmetic names a person | U16 | meets | C5 |
| P18-J13 By-Law 7.9.3 bounded | The Executive Director's access refused without a purpose; granted with purpose and audit line once Q-44 is answered | U17 | guarded until Q-44 | C5 |
| P18-J14 Nothing merged by software | The review band in the merge queue; a human decides each pair | U18 | meets | C6 |
| P18-J15 The parallel run on the platform's screens | The report's items worked and confirmed in place; a weekly open count | U19 | meets | C6 |
| P18-J16 Cutover is one dated act | Writes move; Breeze read-only; the statement opens with the dues position only | U20 | meets | C6 |
| P18-J17 Evidence is not consent | An imported opt-in shows unconfirmed; the member confirms three consents on first sign-in | U21 | meets | C6 |
| P18-J18 A child never enters alone | The extract lists the child for the officers; no import without an authority-holding adult | U22 | meets | C6 |
| P18-J19 Refused by design, with the reason | Export, printed directory, labels | U23 | meets | existing |
| P18-J20 Texting under the club's name | Per-club sender on one account; opt-out per channel | U24 | not built until B5 | B5 |

### 11.3 Coverage

Twenty-four use cases, twenty journeys, every one tied to a rule or a decision. Three are guarded (J03 until Q-37 and D5 settle; J07 by design until a Board confirms an entity; J13 until Q-44); one waits on B5. The canonical J08 and J14 stand; J14 should gain the clubs page's new columns as assertions when C5 builds. None of these journeys names a person or a club; the Hub's fixture (Test Fixture 500) supplies fictional ones.

### 11.4 What sprint 10 changes in the site's data

- `experiences.yaml`: the five club entries list the P18 journeys that test them under "not built" (ids provisional), replacing the four placeholders from sprint 2.

## 12. Strategy pages and the crosswalk (sprint 11)

What this plan changes in the strategy record, so the Strategic Planning Committee sees it where it reads.

- **Crosswalk section J (One Federation)** gains four rows: J9 the officer year; J10 the club's seat in each programme; J11 moving each club off Breeze and the clubs on no system onto the platform; J12 the Federation's view of its clubs and the year-one baseline per club. J3 now records the statement as designed. P10 and P18 point here.
- **Goal 2, Connect the clubs and the Federation** (`goals.yaml`): the Hub paragraph names the plan and its five parts; the open paragraph names Q-40 to Q-47 and the three Breeze gates; rows J9–J12 added.
- **The Strategy page's One Federation section** links the new page For club presidents.
- **What's next** records that one of the queued design notes is written (P18, carrying P10) and that it gives the Hub six club slices (§13).
- **The timeline** gains the 1 October 2026 entry.
- **History** is unchanged: nothing in the plan rewrites what the Federation did; it writes what it has never written down.

What the plan does not change: the mission, the four branches, the eight goals, the by-law status notice. It adds no decision; D57 and D59 remain the only club decisions of October 2026, and everything in the plan that reads as a rule is either a by-law cited by number, a decision cited by number, or a design choice labelled as such.

## 13. Slices and gates for the Hub (sprint 12)

Six slices, C1–C6, added to `plan/MASTER-PLAN.md` §2 after B6. Each cites the section of this note it builds from, names its exit journeys (§11.2) and carries its gate as a row condition, so a build session that cannot read this Project can still act from the plan alone.

| Slice | Builds | From | Gate |
|---|---|---|---|
| C1 The officer year | The officers form as the 3.2 filing; the standing pill; seats derived; the delegation; the hand-over | §4.1, §6.2, §6.4 | Built on the 2024 text; Q-33 flag; Q-40 is a register row |
| C2 The secretary's queue and the member's club view | The queue; no free-text notes; the member's own groups, attendance, standing; the club mute | §3.2, §3.5, §9.2 | None |
| C3 The club statement | Accounts per club per entity; the sixteen line types; the run, the query hold, the close | §5 | Q-47 terms are register rows; manual run until filled |
| C4 The club's seat in a programme | The scoped programme seat; both appointment paths; RBPN first | §3.4, §7 | Q-45 open; both paths offered, each appointment named |
| C5 The clubs page | The six column groups; three views; the baseline; the 7.9.3 screen | §10 | Q-44 for the 7.9.3 screen |
| C6 The migration path | Staging, resolution, the parallel-run report on screens, cutover, the spreadsheet path | §4.4, §8 | Which club first (Breeze Parity §5 q4); readiness B2b, slice 5, C1, C2 |

B4 is absorbed into C6. B3 (club giving), B5 (texting) and B6 (forms) are unchanged and stay gated on David's answers; nothing in C1–C6 depends on them, by design, so that the first club can move before they are answered.

Order: C1 and C2 first (they are what the pilot club's officers will touch daily); C3 next (the treasurer's statement is the second thing the Council will ask for); C6 once C1, C2, B2b and slice 5 are live; C4 and C5 in either order after that. Six sessions, one slice each, on the master plan's standing loop.

What the Hub's record should take from this note in the same pass (for the record slice R3 already suggested): the club register's edge-case rows and lifecycle states (§6.1); the regional seat row for ARFECF (§6.8); the by-law citations for the club lens (3.1, 3.2, 4.3.1, 6.2.2, 6.2.3, 6.4.1, 7.9.3, 8.12.1, 9.1.3, 9.1.4, 10.1.1, 10.1.6, 10.1.7, 10.5.1, 11.1.4, 11.1.5, 15.1.1) added to the rules register's club rows where they are not yet cited.

## 14. Review (sprint 13)

The afrp-review pass on 1 October 2026 (private report: `claude/review/2026-10-01-club-experience-plan.md` in the planning Project) returned **PASS WITH CHANGES** with twenty-one findings, none a privacy breach and none a rule resting on the prototype or Hub code. All twenty-one were applied in this note and the files it touches before publication. The ones that changed a rule or a source:

- The good-standing refusal reached only the president's seat (6.2.2, 6.2.3, 4.3.1); other seats follow the club's own laws (3.1) and are shown, not refused. A per-club switch to apply the test to all seats is a labelled design choice.
- The "counts, never names" rule is Breeze Parity §3 and slice B1 as built, not Four-Lens §3; Four-Lens §6.3 lets national staff read rosters, and the disagreement between the two design documents is now part of Q-44.
- The dabke travel term carried a split and a date from two different minutes; it is now stated without a figure and added to Q-47.
- Two D1 money treatments the statement had omitted are now line types (platform-collected club event receipts, held and remitted; club funds raised for a Federation project as a conduit under By-Law 11.1.5): sixteen line types, not fourteen.
- "One of twenty" was a figure the record does not hold; every instance now reads "one among all the clubs".
- Citations corrected: R16 (a rule about club migration, not grants) replaced by a labelled design choice; "never nets" labelled as design rather than D9/D55; the Council clause is 8.4.1 and disagrees with 6.4.1 (added to Q-40); 10.1.1, 10.1.6 and 10.1.7 cited on the bid, the host agreement and the 120-day accounting; 4.3.1 quoted exactly; ARFHSN's by-laws mention one club's building; the by-laws derive Federation seats from the president alone; the "three failing connectors" were Portal-era states, not real clubs; the no-consent-rows default is a design choice added to Q-46; the free-text-note refusal excepts a follow-up's one completion note; Multi-Entity Ledger §2.1 cited for the per-club treatment.
- Consistency: three guarded journeys, not two; P18-J08, J17 and J20 placed on the right lens entries; J11's slice is C2; the crosswalk P18 row spans J1–J12; workflow open items carry their Q-numbers.

What the review could not verify is listed in the report: whether any real club's Breeze is failing; the 2009 template's officer-eligibility clause; whether affiliation forms were looked for and not found; the Hub's seat list, read from the design record rather than the clone.

---

## Appendix A. Breeze Parity §5, where each question stands on 1 October 2026

| # | Question | Standing | Where this note takes it |
|---|---|---|---|
| 1 | Texting provider, budget, 10DLC | Open, David | §9; B5 stays gated |
| 2 | What clubs recorded in Breeze custom fields | Open, David (the intakes did not open any club's Breeze) | §8; the extract step reports the fields found per club |
| 3 | Club giving through the platform (B3) | Open, David; the intakes show clubs already take money on their own books | §4, §5 |
| 4 | Which club goes first; who holds its key | Open, David | §8 |
| 5 | Child check-in security codes in use today | Open, David | §4 (B2 built the release-list check-in) |
| 6 | Forms beyond signup, join, application | Open, David | §4; B6 |
| 7 | Printed directory and labels refused | Open, Board | §9 |
| 8 | 17, 18 or 19 clubs | Open, Board's list | §6 |
