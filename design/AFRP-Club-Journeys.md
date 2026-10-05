# The club journeys

### What a club officer does in Breeze today, what the same person does on the platform, and the test each one becomes

**Design note P20 · 1 October 2026 · the corpus the clubs component is built from**

**David's direction, 1 October 2026:** *"make sure to have the user journeys that are club focused as they use Breeze built into the strategy hub in the appropriate places … get as much detail in there to build a built-for-purpose component in the final hub."*

This note is that detail. Every journey below starts from something a club officer, treasurer, member or volunteer actually does in Breeze — taken step by step from the deep read of 1 October 2026 (`AFRP-Breeze-Club-Parity.md` §1a and the private intake cards) — and says what the same person does on the platform, which rule or decision it tests, what the platform refuses and why, the class the journey must reach, and the slice that builds it (`plan/MASTER-PLAN.md`: B1, B2, B2b, B3, B5, C1–C6, DIR1–DIR2). The club experience plan (`AFRP-Club-Experience-Plan.md`, P18) is the design these journeys test; its §11 listed twenty; this note replaces that list with the full corpus and the plan points here.

**How a build session uses it.** Each journey is a proposal for the Hub's workbench queue (the afrp-test rule: proposals, never direct edits to `journeys/catalog.yaml`); the workbench assigns catalogue ids and the fixture (Test Fixture 500, D15) supplies fictional people and clubs. Identifiers here are provisional (`P20-A1` …), as P18's were. A slice closes when its journeys reach the class named here. "Guarded" means the platform refuses correctly until a named decision lands; a guarded journey that passes is not a gap.

**Precedence (D41).** A rule cited to a by-law or a D-number is a rule; a line marked *design choice* is the club plan's and may be changed by a build session that says why in the Delivery Status.

**What Breeze is, in one line, for the reader who has not seen it.** One profile per person with custom fields; families; tags for every list; events with check-in and attendance; volunteers on events; follow-ups as tasks; forms for sign-ups and payments; giving with statements; email and one-way texting; roles; a members' login and a directory tag; Excel in and out. No membership object, no club object: a club is a tag and a role.

---

## A. The roster: joining, standing, leaving

### P20-A1 · A new person joins the club at a meeting
- **Who:** club secretary (club lens); the new member (door, then member).
- **In Breeze:** People > Add Person: first name, last name, phones, email, address; mark a phone or email private; "+ Family Member" for spouse and children; tick the club's tag; Add. Or at the door: the check-in screen's "+" creates a profile with whatever fields the event asks.
- **On the platform:** the secretary cannot create a national member (Article IV: membership is the Federation's to grant). Two paths: the person joins through the join wizard on the door, naming the club, and the secretary sees the join land in the secretary's queue (C2) and confirms the club attachment; or the secretary records a **contact** for the club (name, one verified channel, consent) that is not a membership, and the queue carries an invitation to join. At the door, B2 as built admits a walk-up only from the eligible and adds nobody; a door that records a **contact** (never a member) for an unknown walk-up is a design choice of this note for B2b, routed to the secretary's queue (C2).
- **Tests:** Article IV; D1 (standing starts at collection); club plan §9.2 (no consent rows means no marketing — a design choice under Q-46); club plan §3.2; *since 2 October 2026* the contact is a club prospect role (P21 §2, §10; P20-A7).
- **Refuses:** "Add member" from the club lens, naming Article IV; a second profile for a person the register already knows (identity resolution proposes a match; the queue decides).
- **Must reach:** meets. **Slice:** C2 (the queue); B2 (the door).

### P20-A2 · The roster, both standings side by side
- **Who:** club officer.
- **In Breeze:** People > Filters > club tag; "Status" is a custom field the church defined; no dates unless another field holds them; results grouped by family.
- **On the platform:** the club roster (B1, built): every member of the club sorted by household, with national standing and club standing as two columns from the register, each with its date and reason where the register holds one (paid, grace, lapsed, dormant club under D6); filters by standing, household, group, adults/minors (minors never listed, R7).
- **Tests:** scoped standing as built on the member lens (the restatement would change it, Q-33); 4.3.1's conjunctive test displayed, not computed by the officer; D6; R7.
- **Refuses:** a free-text "status" of the club's own invention; export.
- **Must reach:** meets. **Slice:** B1.

### P20-A3 · A member lapses nationally and the club wants to act
- **Who:** club treasurer.
- **In Breeze:** nothing automatic; the officer runs a filter or an attendance "missed the last N" report, tags the result, and assigns a follow-up to the tag; or an event Alert emails the morning after a run of misses.
- **On the platform:** if the club has switched the lapse rule on, a follow-up opens on the treasurer's desk the day standing changes, naming the rule that raised it (B1, built); the member receives the renewal notice as an operational message whatever their marketing consent (the communications workflow's message classes; club plan §9.2).
- **Tests:** Breeze Parity §4 r3 (nothing automatic without a named rule); the message classes.
- **Refuses:** a follow-up raised on a club that has not switched the rule on.
- **Must reach:** meets. **Slice:** B1.

### P20-A4 · A member leaves the club, or dies
- **Who:** club secretary.
- **In Breeze:** Archive Person (reversible, drops from search and tags, keeps history); Delete needs archive first and relabels their gifts "Anonymous"; thirty-day recovery.
- **On the platform:** nothing is deleted. Leaving the club ends the club membership on a date (the national membership is untouched); a reported death goes to the secretary's queue and the register's verification path; a household split lands in the queue as a dated change of household with both adults told; and the condolence surface releases on verification, not review (JC-027, carried).
- **Tests:** refusal by design (no delete); D6 for the dormant-club case; the life-event pipeline.
- **Refuses:** delete, naming the rule; ending a national membership from the club lens.
- **Must reach:** meets. **Slice:** C2.

### P20-A5 · Two records for one person
- **Who:** club secretary; match-queue reviewer (federation).
- **In Breeze:** Bulk Tasks > Merge People: name-match only, Person 1 wins, irreversible.
- **On the platform:** identity resolution proposes; the review band goes to the merge queue; a human decides each pair; a merge closes one record with the map of what moved and is reversible by the map.
- **Tests:** the merge queue (slice 9); refusal by design.
- **Refuses:** a merge by name alone; a merge from the club lens.
- **Must reach:** meets. **Slice:** existing (slice 9) with C6 for imported pairs.

### P20-A6 · A member asks to move to another club
- **Who:** member; both clubs' secretaries.
- **In Breeze:** an admin removes one tag and adds another; no request exists to record (the Log records the admin's change).
- **On the platform:** the member asks from their own record; the request lands in both secretaries' queues; the move is dated and the old club membership ends on the date; which club's standing counts for 4.3.1 is Q-41 and the platform shows both until it is answered.
- **Tests:** club plan §3.5; Q-41 (guarded).
- **Refuses:** a move the member did not ask for.
- **Must reach:** guarded until Q-41. **Slice:** C2.

### P20-A7 · A prospect the club met becomes a contact role (added 2 October 2026)
- **Who:** club secretary (club lens); the person met at a meeting, who is not a member.
- **In Breeze:** People > Add Person with whatever the secretary knows; the person is on the club's lists the same day.
- **On the platform:** the person is a **club prospect**, a role on the contact record (P21 §2) scoped to this club. It is created only by the person's own act at the club's door. The secretary's entry is a queue item that holds no channel until the person acts. The club sees its own prospects and nobody else's (P21 §10). If the person later joins, the role is linked to the membership with the person's confirmation (P21 §7.2).
- **Tests:** P21 §2, §10; D60's shape; S1; Q-70 (the contact record's shape, DRAFT); Q-72 (a prospect nobody referred).
- **Refuses:** a channel typed by the secretary; the prospect in any other club's view or in a member audience; a prospect imported from Breeze becoming a role before Q-70's migration option (P21 §7.5).
- **Must reach:** guarded until Q-70 (and Q-72 for a prospect nobody referred). **Slice:** CR5 on CR1, with C2.

---

## B. Households and children

### P20-B1 · A household with children
- **Who:** club secretary; the household's adult (member).
- **In Breeze:** one family per person; roles Head, Spouse, Adult, Child, Unassigned; the household's address is the Head's; no article describes anything changing at eighteen; a child cannot be in two families.
- **On the platform:** the household on the register with R6 authority per adult; a child is a minor by birthdate, not by role; at eighteen the child's own record stands and the household link remains as history; a child of two households is OPEN for the Membership Committee (Rules Register R4) and both households see the child under R6.
- **Tests:** R6; R4; R7 (never listed).
- **Refuses:** a child without an authority-holding adult; a club officer reading a child's record outside the household and the event screens.
- **Must reach:** meets; the two-household case guarded. **Slice:** B1 (as built) with 2b.

### P20-B2 · An address changes
- **Who:** member.
- **In Breeze:** an admin edits one profile and ticks "apply to all family members"; deletions do not cascade.
- **On the platform:** the member changes their own address; the household's other adults are told and may adopt it; the club sees the change on the roster; nothing is typed by an officer.
- **Tests:** the member's own record (design choice: an officer raises a follow-up, never edits); R27 for the address's visibility.
- **Refuses:** an officer editing a member's address (design choice: the officer raises a follow-up asking the member to).
- **Must reach:** meets. **Slice:** existing member lens.

### P20-B3 · A parent manages the children's records
- **Who:** household parent.
- **In Breeze:** the Member role's "Access to My Family Members" lets a parent edit the family's profiles.
- **On the platform:** a parent with R6 authority sees and maintains the child's record, consents for the child (D22, D33), and the release list for events; the other adult with authority sees the same.
- **Tests:** R6; D22; D33.
- **Refuses:** a parent without authority; the child's own login before eighteen (design choice; camp logins are parents and staff only, Network Plan).
- **Must reach:** meets. **Slice:** 2b (built).

---

## C. Groups and lists

### P20-C1 · The club makes a group from a filtered roster
- **Who:** club secretary.
- **In Breeze:** People > Filters > Action Panel > Assign to Tags; a tag has no leader (the name carries it); folders hold tags only.
- **On the platform:** filter the roster, then the acting panel: add this set to a group (B1, built); a group has a leader seat or none; folders; a member is added singly or from the set; membership is dated and ended, never deleted.
- **Tests:** Breeze Parity §4 r1 (a group is the club's); the leader-in-the-name refusal.
- **Refuses:** a group name carrying a person's name as its leader (the platform offers the leader seat instead; Breeze Parity refusals, a design choice).
- **Must reach:** meets. **Slice:** B1.

### P20-C2 · A Smart Tag's list, derived from standing
- **Who:** club secretary.
- **In Breeze:** a Smart Tag assigns people hourly from a profile-field filter and can lock the tag against hand edits.
- **On the platform:** a derived list is a saved roster filter (by standing, household, group, age band), not a group; it is always current and never locks anything; at migration a Smart Tag imports as the filter that defined it, noted on the group (club plan §8.3).
- **Tests:** B1's filters; the migration rule.
- **Refuses:** a group that "locks" to a filter.
- **Must reach:** meets. **Slice:** B1; C6 for the import.

### P20-C3 · The dabke troupe becomes a programme seat
- **Who:** club dabke lead; programme coordinator (programme lens).
- **In Breeze:** a tag.
- **On the platform:** a club group today; when the Mid-Year's dabke competition opens, the club's ambassador seat for that programme (C4) sees the troupe as the club's participants and the travel line on the club statement (C3); the group and the seat are two objects. The same seat shape serves the camp liaison, who sees this club's campers and households and no other club's, minors as counts unless R6 names them (P18-J09).
- **Tests:** Four-Lens §6 (sibling scopes); D57.
- **Refuses:** the programme seat reading the club lens; the club group reading other clubs' troupes.
- **Must reach:** meets. **Slice:** C4.

---

## D. The officer year and the seats

### P20-D1 · The officers form is filed by 1 August
- **Who:** club president.
- **In Breeze:** Users & Roles: an admin creates users and roles by hand; nothing files anything with the Federation; the affiliation form is a document emailed to the office.
- **On the platform:** the form opens from last year's; the president names every seat the club has under its own by-laws and any programme seats; submitting is the By-Law 3.2 filing; the office marks it received; the club's standing pill turns; the Council, the Board roster (6.2.2) and the Membership Committee seat (8.12.1) derive from it.
- **Tests:** By-Laws 3.2, 6.2.2, 6.4.1, 8.12.1; club plan §4.1.
- **Refuses:** the president's seat to a member not in good standing of club and Federation (6.2.3, 4.3.1); other seats are shown with standing and not refused (club's own laws, 3.1).
- **Must reach:** meets. **Slice:** C1.

### P20-D2 · A treasurer resigns in March
- **Who:** club president; incoming treasurer.
- **In Breeze:** delete the user (irreversible) or change the role; the Account Owner stays whoever signed up.
- **On the platform:** a dated change on the form; the old grant ends that day (design choice, Four-Lens §6); the new treasurer sees the statement balance, open follow-ups and the remittance run exactly as left; nothing is copied; the Federation's lists update from the form.
- **Tests:** club plan §4.1 step 8; R16 is not the rule here (it governs a member's move).
- **Refuses:** two holders of one seat on one date (design choice).
- **Must reach:** meets. **Slice:** C1.

### P20-D3 · The delegation for the Convention
- **Who:** club president and officers; the credentials desk (federation).
- **In Breeze:** nothing; a spreadsheet of voting members from the office.
- **On the platform:** the delegation is selected from certified members (9.1.4) on the club lens; weights computed, never typed; handed to the convention workflow; an independent voter extracts at the opening and is deducted (9.1.3; D5 reopened on when weights fix).
- **Tests:** 9.1.3, 9.1.4; Q-37 (who certifies; *since 2 October 2026* also how delegates are chosen, P22 §6 and P20-D6).
- **Refuses:** a delegate who is not a certified member; a typed weight.
- **Must reach:** guarded until Q-37 and D5 settle. **Slice:** C1.

### P20-D4 · The president reports to the Council
- **Who:** club president; the Deputy President (federation).
- **In Breeze:** an officer exports people and attendance to Excel.
- **On the platform:** the club dashboard's counts are the report; the Council's clubs page shows every club under the floor; the president's own row in full, other rows as counts (C5).
- **Tests:** 10.5.1; S7 suppression (R43 for the frozen figures); club plan §10.
- **Refuses:** export; another club's names.
- **Must reach:** meets. **Slice:** C5.

### P20-D5 · The club's seats on the leadership directory
- **Who:** member; club officers.
- **In Breeze:** nothing; the printed Committee Directory.
- **On the platform:** the leadership directory (DIR2) shows the club's officers from the form, the president's Council and Board seats with whether they vote (6.2.2), the programme seats, and the delegates once selected; contact through the seat channel, never the officer's personal details.
- **Tests:** P19 §4; R27.
- **Refuses:** an officer's phone or email in the payload; the person's own franchise on the page.
- **Must reach:** meets. **Slice:** DIR2.

### P20-D6 · The delegation records how it was chosen (added 2 October 2026)
- **Who:** club president and officers; the credentials desk.
- **In Breeze:** nothing; a spreadsheet of voting members from the office.
- **On the platform:** the delegation is a dated act of the club with its **method** stated: *officers' selection*, *members' vote*, or *as the club's own by-laws provide*. Its evidence (minutes, a drive link) is attached. The desk marks each delegate present, and only a present delegate carries a weight, computed as certified members divided by present delegates (P22 §6's reading of 9.1.3's 'delegates sent'; Q-37). P20-D3 is unchanged; this journey adds the method and presence.
- **Tests:** 9.1.3 (silent on method); P22 §6; Q-37.
- **Refuses:** nothing on the method; a weight for a delegate not marked present (P22 §6's reading of 9.1.3's 'delegates sent'; Q-37); a typed weight.
- **Must reach:** meets for the record and presence; the weights stay guarded with P20-D3 until D5. **Slice:** CV4, with C1.

### P20-D7 · The club's local action committee (added 2 October 2026)
- **Who:** club president; members of the local action committee; the Government Affairs Committee.
- **In Breeze:** a tag or a group, if anything.
- **On the platform:** in practice (research, 2 Oct 2026) the committee launched local action committees inside clubs in 2025–26. The platform seats nothing for them: no officers-form seat and no body on CW1 until Q-131 says who appoints them and to whom they report. A meeting they hold with an office is recorded as a contact row against the office and the position, never a note about a person (P14 §2.2; P14-J16). A member's own contact is recorded under that member's consent (P14 §2.5).
- **Tests:** P25 §5.4; P14 §2.8, AD5; Q-131.
- **Refuses:** a "local action committee" seat on the officers form, naming Q-131; a free-text note about an office-holder or a staffer.
- **Must reach:** guarded until Q-131. **Slice:** AD5 (with YL5).

### P20-D8 · The correspondent sends in an announcement (added 2 October 2026)
- **Who:** the club's Magazine correspondent; the household; the Magazine's editor.
- **In Breeze:** nothing; an email to the editor with photos.
- **On the platform:** the correspondent's seat is filed on the officers form (§4.1 step 2) or appointed by the Magazine, naming who appointed it. The correspondent enters an announcement *on the household's behalf* as a **pending submission** naming who entered it and from what. It prints nothing until the household's consent is recorded: through the proof-and-confirm link for a member household, or through the channel the submission came on for a household with no member (P24 §3.2). A death goes through the family-approval gate (R34).
- **Tests:** P24 §3.2; D33; R34; R27; Q-195.
- **Refuses:** printing a pending submission; an announcement typed straight into a section.
- **Must reach:** guarded until Q-195 (the door builds pending-only). *Since 4 Oct 2026:* D89 answers Q-195; an entry with the correspondent's attestation recorded prints without the household being asked, so the journey meets once MG1 lands. **Slice:** MG1, with C1 for the seat.

---

## E. Events and the door

### P20-E1 · The monthly meeting as a series
- **Who:** club secretary.
- **In Breeze:** Add Event, Schedule = monthly on the second Tuesday; "2nd and 4th" is refused; editing the series later wipes future check-in and volunteer data.
- **On the platform:** a club event as a series with an agenda template (B2); eligibility by group; a change to the series keeps every past occurrence's attendance and volunteers and says what it changes ahead.
- **Tests:** B2; the club plan §4.2.
- **Refuses:** nothing here; the point is what Breeze refuses and the platform does not.
- **Must reach:** meets. **Slice:** B2.

### P20-E2 · The door with a laptop
- **Who:** club check-in volunteer (`club_checkin` role).
- **In Breeze:** List or Search mode; tick names; "+" for walk-ups; Headcount for the rest; name tags print.
- **On the platform:** the check-in screen (B2, built): signed-up and walk-up from the eligible; an unknown walk-up as a contact record is B2b (design choice), never a member (P20-A1); an anonymous headcount beside named attendance (B2b); name tags are not a goal.
- **Tests:** B2; Article IV at the door.
- **Refuses:** the check-in role reading anything but the door.
- **Must reach:** meets; the contact record and the headcount not built until B2b. **Slice:** B2 (built), B2b.

### P20-E3 · A child leaves the event
- **Who:** household parent; check-in volunteer.
- **In Breeze:** a 3- or 4-digit code printed on the child's and the parent's tag; the match is by eye; no article describes a check at pick-up; check-out records a time.
- **On the platform:** the child leaves only with a standing holder or someone on the R6 release list, confirmed on the screen; check-out time recorded (B2b); the release list is per household and per event.
- **Tests:** R6; the ratified release list (2b).
- **Refuses:** release to anyone not on the list, naming R6; a release list edited by anyone but an authority holder.
- **Must reach:** meets. **Slice:** B2 (built), B2b (check-out time).

### P20-E4 · A member checks in at a kiosk
- **Who:** member.
- **In Breeze:** Kiosk mode by phone number or barcode; names not browsable; settings password-locked.
- **On the platform:** the member's own QR on their record (JM-018) or their verified phone number at a kiosk screen that shows nothing but the member's own name on success; the family checks in together where the household allows.
- **Tests:** JM-018; R7 (a child never self-checks in).
- **Refuses:** a browseable list at a kiosk (design choice); a child's self check-in (R7).
- **Must reach:** meets once built. **Slice:** B2b.

### P20-E5 · Who stopped coming
- **Who:** club secretary.
- **In Breeze:** View Details > Reports > "missed the last N"; an Alert emails the morning after; tag the result; follow-up to the tag.
- **On the platform:** "missed the last N" is a report the officer reads and acts on by name, opening a follow-up per absentee through a club-defined option (B2, built); an automatic raise on attendance exists only where a club switches a named rule on (r3; a design choice for C2, not built); the member's own attendance is theirs to see.
- **Tests:** Breeze Parity §4 r3; B2.
- **Refuses:** an automatic follow-up with no switched-on rule.
- **Must reach:** meets. **Slice:** B2.

### P20-E6 · A ticketed club dinner
- **Who:** club treasurer; member.
- **In Breeze:** a Form with a Payment field to a non-deductible fund; Max Entries on the whole form; no per-option capacity; entries connect to profiles by hand; payments land in a batch grouped by form.
- **On the platform:** a club event with signups, waitlist and questions (B2, built); a price on a club event waits on B3, which gives the club its purposes on the one door; a money-taking event prints its surplus and shortfall rules first (D7); the money is the club's: taken on the platform it is held and remitted on the statement (D1 treatment 3; C3), taken off the platform it never enters.
- **Tests:** D7; D1 treatment 3; D9 (a ticket is non-deductible).
- **Refuses:** a ticket receipted as a gift.
- **Must reach:** meets for the free event; guarded until B3 for the priced one. **Slice:** B2; B3, C3.

### P20-E7 · The national club night
- **Who:** Federation staff; every club's secretary.
- **In Breeze:** each club makes its own event; nothing links them.
- **On the platform:** one Federation event cross-listed to every club without moving the money; each club mails its own roster about it; attendance per club rolls up.
- **Tests:** R23 (money routes by the host; a cross-listing is attribution only); the events workflow.
- **Refuses:** a cross-listing that moves money.
- **Must reach:** meets. **Slice:** B2.

---

## F. Volunteers

### P20-F1 · The gala team
- **Who:** club events officer.
- **In Breeze:** Teams and Roles on the event with a quantity and a leader; Assign mode (search by name, recent, tag; conflicts flagged; recurrence per person); Invite mode (sign-up sheets for up to 32 events, personal links); up to three reminders per role, optional SMS and RSVP.
- **On the platform:** volunteer roles and quantities per event with assign and invite (B2b); reminders as operational messages on the member's channels under consent; an RSVP recorded; a decline frees the slot and tells the leader (design choice: Breeze does not document what a decline does).
- **Tests:** B2b; the message classes.
- **Refuses:** an SMS reminder to a member who said no to texts (Breeze sends them anyway).
- **Must reach:** meets once built. **Slice:** B2b.

### P20-F2 · A volunteer's own blockout dates
- **Who:** member.
- **In Breeze:** My Profile > Volunteering > blockout dates; the scheduler cannot assign them on those days.
- **On the platform:** the member sets availability on their own record; a club cannot assign across it; the club sees availability as yes/no, never why (design choice).
- **Tests:** the member lens; B2b.
- **Refuses:** an assignment on a blocked date.
- **Must reach:** meets once built. **Slice:** B2b.

---

## G. Follow-ups and the things Breeze automates

### P20-G1 · The welcome call
- **Who:** club membership officer.
- **In Breeze:** a Follow Up Option "Welcome call", assigned on creation of the profile or by a Smart Tag plus automation; completion from the email without login; Follow Up Progression chains the next task.
- **On the platform:** a follow-up option per club with a default assignee and days (B1, built); the rule-named option "new club membership" opens one when a join lands (design choice for C2, Breeze Parity §1a Automations); a progression is a second option the officer opens on completion, not an automation.
- **Tests:** Breeze Parity §4 r2, r3.
- **Refuses:** a chain that runs without a person; a note on the person beyond the completion note.
- **Must reach:** meets. **Slice:** B1, C2.

### P20-G2 · A first-time attender
- **Who:** club secretary.
- **In Breeze:** "Follow Up with New Attenders" runs daily.
- **On the platform:** the rule-named option "first attendance at this club" the club switches on (C2); the follow-up names the rule.
- **Tests:** r3.
- **Refuses:** the same without the switch.
- **Must reach:** meets. **Slice:** C2.

### P20-G3 · The follow-ups desk
- **Who:** club officers.
- **In Breeze:** Assigned To Me / Assigned By Me / All; no bulk complete; the assignment email carries the member's contact details.
- **On the platform:** mine / all / overdue (B1, built); completion with one note; the assignment notice carries the person's name and the option, never contact details outside the platform.
- **Tests:** r2; R27.
- **Refuses:** contact details in an outbound notice.
- **Must reach:** meets. **Slice:** B1.

---

## H. Communications and consent

### P20-H1 · The club newsletter
- **Who:** club secretary.
- **In Breeze:** People > tag > Email; BCC; a design editor; delivery history per recipient; unsubscribes as "Group Unsubscribe".
- **On the platform:** the audience from a group or the filtered roster; consent checked when the audience is built; the withheld named to the sender; send gated on the grant; undeliverable shown as not tracked (built; a real provider waits on slice 5).
- **Tests:** R27; the communications workflow's message classes (club plan §9.2).
- **Refuses:** a send to a withheld member; an export of the audience.
- **Must reach:** meets; delivery waits on slice 5. **Slice:** B1, 5.

### P20-H2 · A meeting reminder by text
- **Who:** club secretary.
- **In Breeze:** a shared short code, one way, 160 characters, a consent checkbox before texting the un-enrolled, STOP handled.
- **On the platform:** the same audience and consent model per channel; the club's sender name where the route allows; refused with the reason until B5's provider and route exist.
- **Tests:** B5 gate; per-channel consent.
- **Refuses:** any text until B5; a text to a member whose status is Blocked (hard no, club plan §8.3).
- **Must reach:** guarded until B5. **Slice:** B5.

### P20-H3 · "Take me off the list"
- **Who:** member.
- **In Breeze:** Do Not Email / Do Not Text flags on every profile sharing the address; resubscribe is member-only.
- **On the platform:** the member mutes the club, a channel, or the Federation separately, each a dated row; operational messages still arrive; a club sees only its own withheld list.
- **Tests:** R27; the message classes.
- **Refuses:** a club reading who muted it beyond its own sends.
- **Must reach:** meets. **Slice:** C2.

### P20-H4 · The mailing list for the club's own tool
- **Who:** club secretary.
- **In Breeze:** Action Panel > Export > Excel, mailing labels, printed directory; the MailChimp extension pushes names and emails.
- **On the platform:** refused, naming the rule: a consent given to the Federation cannot travel to a tool the Federation does not control; the refusal is logged; the club mails through the platform.
- **Tests:** export refused by design; the Network Plan's export logging.
- **Refuses:** every export path, including the professional directory's and the roster's.
- **Must reach:** meets. **Slice:** existing (memberdir/export_refused), with logging.

---

## I. The treasurer's money

### P20-I1 · The month: collect, close, remit, reconcile
- **Who:** club treasurer.
- **In Breeze:** Giving > Add per gift into an auto-opened batch; close the batch; export the batch's three sheets for the deposit slip.
- **On the platform:** national dues split at capture; the remittance run with carry-forward; chargebacks after remittance as a receivable (D1 consequence F; the slice-3 scenario); the run attested by a named officer.
- **Tests:** D1; J08 (the treasurer's year).
- **Refuses:** national dues as club revenue.
- **Must reach:** meets. **Slice:** existing (slice 3; Delivery Status "Slice D1").

### P20-I2 · The club statement arrives
- **Who:** club treasurer; Federation treasurer.
- **In Breeze:** nothing of the kind.
- **On the platform:** one account per club per holding entity, never netted across entities (design choice, club plan §5.1); sixteen line types each tied to a programme term in the register; a run per entity approved by the Federation treasurer; confirm or query one line; the query holds the line and the rest settles; an immutable close (C3).
- **Tests:** D57; D55; D59 for the settlement line.
- **Refuses:** a line whose programme has no confirmed holding entity, by name (P20-I3); netting across entities.
- **Must reach:** meets. **Slice:** C3.

### P20-I3 · A line that cannot settle
- **Who:** club treasurer.
- **On the platform:** the Leadership Ramallah travel share before a Board confirms the programme's entity: the line shows, carries, and refuses to settle with the reason.
- **Tests:** D55's silence; "where the record is silent, refuse".
- **Must reach:** guarded by design. **Slice:** C3.

### P20-I4 · A gift to the club
- **Who:** member; club treasurer.
- **In Breeze:** the club's own online giving page through Breeze's processor under the club's own EIN and bank account; fund-level deductibility; statements by family; text giving; refunds.
- **On the platform:** not yet decided (B3). If yes, shape (a): the one door takes the gift on the Federation's account and holds and remits it as the club's, receipt in the club's name with the club's own tax status on file; shape (b): a per-club merchant account under the club's EIN. Until David answers, the platform refuses a gift "to the club" with the reason and records only attributions (D57).
- **Tests:** B3 gate; D57; D9; Q-3.
- **Refuses:** a club purpose on the door until B3; a receipt for a club with no tax status on file.
- **Must reach:** guarded until B3. **Slice:** B3.

### P20-I5 · The year-end statement
- **Who:** member; club treasurer.
- **In Breeze:** Giving > Statements, templates, grouped by family, emailed as PDF to the credited donor.
- **On the platform:** the member's own contribution statement on their record for every entity's receipts (the member lens; class to be confirmed by the workbench); a club's own giving statement only if B3 is answered yes.
- **Tests:** D9; the receipting entity (D56).
- **Must reach:** meets for the Federation's receipts; guarded for the club's. **Slice:** existing; B3.

### P20-I6 · Club funds raised for a Federation project
- **Who:** club treasurer.
- **In Breeze:** a fund on the club's giving page.
- **On the platform:** a conduit line on the club statement (By-Law 11.1.5; D1 treatment 4): club → AFRP → the project, purpose preserved; an appeal for a project the Federation has undertaken shows the authority of the Board and the Executive Committee, or refuses to open (11.1.4).
- **Tests:** 11.1.4, 11.1.5; D1; *since 2 October 2026* P23 §5 for relief money (P20-I7).
- **Refuses:** an appeal without that authority for a Federation-undertaken project.
- **Must reach:** meets. **Slice:** C3.

### P20-I7 · The clubs' relief drive (added 2 October 2026)
- **Who:** club treasurer and president; the drive's organisers (in 2025 the Young Leaders); the Federation.
- **In Breeze:** a fund on the club's giving page, or cash collected and sent on.
- **On the platform:** a drive across the clubs is **one catalogue purpose** in the receiving entity's name, with a published end date. Each gift carries the club's attribution (D57), and the tally is a count and an amount per club on the drive's page. Money a club raises for the Relief Fund passes through headquarters (11.1.5) and is never the club's money. A prize is the organisers' and is not modelled. A club's gift to its own project in Ramallah is outside 11.1.5's words, and the platform builds nothing that blocks or records it until Q-228 is answered (P23 §5).
- **Tests:** 11.1.4, 11.1.5; D8; D57; P23 §5; Q-180, Q-109, Q-228.
- **Refuses:** publishing the drive while its receiving fund has no entity (D8; Q-109, Q-180); a per-club tally that names a giver. *Since 3 Oct 2026:* the Relief Fund's entity is AFRP (D83); which fund receives a drive stays Q-180.
- **Must reach:** guarded until Q-180 (P23-J10). **Slice:** RL4, with C3.

### P20-I8 · A club's gift to the Foundation's senior home (added 2 October 2026)
- **Who:** club president and treasurer.
- **In Breeze:** a cheque from the club's account; nothing recorded beyond it.
- **On the platform:** a club gift made **through the Federation's pass-through purpose** is a line on the club's statement with the club as donor and the recognition request (signage) carried to the Foundation with the transfer. Recognition is the Foundation's to give (P23 §9.3–§9.4). A gift the club makes directly to the Foundation is outside the platform.
- **Tests:** P23 §9.4; D57; Q-205; Q-204 (the receipting entity); Q-248 (recognition and the receipt).
- **Refuses:** the line before Q-205 says it runs; publishing the purpose before Q-204.
- **Must reach:** guarded until Q-205 (and Q-204 for the purpose). **Slice:** RL6, with C3.

---

## J. Reports and the Federation's view

### P20-J1 · The club's own numbers
- **Who:** club president.
- **In Breeze:** People filters and Excel; attendance reports per event series; six fixed weekly digests.
- **On the platform:** the club dashboard: roster counts, dues position, open follow-ups, next events, attendance, the statement balance, with the Federation's median beside each (built in part; C5 completes it).
- **Tests:** the reporting workflow; S7.
- **Refuses:** export; another club's figures by name.
- **Must reach:** meets. **Slice:** C5.

### P20-J2 · The Federation's clubs page
- **Who:** Executive Director; the Council.
- **In Breeze:** nothing; about ten separate accounts, one per club (club plan §4.4).
- **On the platform:** per club, six column groups (standing, membership, club life, the Federation's work in the club per programme, money between us, the move), every cell under the floor; three views (C5).
- **Tests:** S7, R43; D67 per club; Q-44 for any named read under 7.9.3.
- **Refuses:** a name anywhere on the page; arithmetic across pages that would identify a person.
- **Must reach:** meets; the 7.9.3 screen guarded until Q-44. **Slice:** C5.

### P20-J3 · The year-one baseline
- **Who:** programme committees; the Board.
- **On the platform:** campers, scholars, participants, volunteers, gifts attributed and events hosted per club per year, from the registers, frozen in the annual snapshot (D67).
- **Tests:** D67.
- **Must reach:** meets. **Slice:** C5.

### P20-J4 · The club's legal shape on the register (added 2 October 2026)
- **Who:** the office; the club president.
- **In Breeze:** nothing; each club's filings are its own.
- **On the platform:** in practice (research, 2 Oct 2026), public filings show the clubs as separate exempt organisations: large clubs as 501(c)(7) social clubs, one revived club as a 501(c)(3), and at least one club with a sister 501(c)(3) foundation beside it. The club register (P18 §6.1) shows the tax status *as the club states it* and verifies nothing. Columns for each club's state entity, federal subsection and any sister foundation, and who keeps them current, wait for the Board.
- **Tests:** By-Law 3.1 (good standing with state and federal regulation); P18 §6.1; Q-227; Q-229 (which count of clubs).
- **Refuses:** a status the platform did not receive from the club or a public filing; treating a sister foundation's gifts as the club's.
- **Must reach:** guarded until Q-227. **Slice:** C1 (the register row).

---

## K. Migration

### P20-K1 · The key
- **Who:** the club's Breeze Account Owner; Federation staff.
- **In Breeze:** only the Account Owner sees the API key; a departed owner is replaced by a signed letter on letterhead.
- **On the platform:** the key is given once, held as a secret, named on the club's register row with who gave it; a club whose owner has left is "not ready" until ownership is recovered.
- **Tests:** club plan §8.1; Breeze Parity §1a.
- **Refuses:** a connection from anyone but the owner's key; a key in the repository.
- **Must reach:** meets. **Slice:** C6.

### P20-K2 · The extract, attendance first
- **Who:** platform; Federation owner.
- **In Breeze:** the API at twenty requests a minute, event listings cached; the account export omits attendance; editing a series wipes future check-in data.
- **On the platform:** attendance is pulled per event before anything else and before anyone edits a series; people, families, tags, events, form entries, volunteer roles, custom fields and consent flags follow; the account export is the fallback for everything but attendance; the extract reports what will not move (notes, files, photos, recurring gifts).
- **Tests:** club plan §8.3.
- **Refuses:** a write to Breeze; a second extract that overwrites a verified one (design choice).
- **Must reach:** meets. **Slice:** C6.

### P20-K3 · Nothing merged by software
- **Who:** match-queue reviewer; club secretary.
- **On the platform:** the review band in the merge queue; every pair decided by a person; a Breeze person unknown to the register enters as a contact or a club member as the officers decide, never as a national member.
- **Tests:** Article IV; slice 9.
- **Must reach:** meets. **Slice:** C6.

### P20-K4 · Evidence is not consent
- **Who:** member; club secretary.
- **In Breeze:** the directory tag, the Yes/No opt field, private flags on phones and emails, Do Not Email/Text, texting status Enrolled/Blocked.
- **On the platform:** each imports as an unconfirmed proposal shown to the member on first sign-in, who then sets display, contact and export (R27); Blocked, Do Not Email and Do Not Text are hard noes that sign-in does not reopen.
- **Tests:** R27; club plan §8.3 (design choice).
- **Refuses:** a mailing to an imported member before confirmation except operational messages.
- **Must reach:** meets. **Slice:** C6.

### P20-K5 · A child in the extract
- **Who:** club officers.
- **In Breeze:** a "Child" family role, not an age.
- **On the platform:** a child enters only through a household with an adult who holds authority; a child with none is listed for the officers on the parallel-run report and never imported alone; age is the birthdate under R6, never the role.
- **Tests:** R6; R7.
- **Must reach:** meets. **Slice:** C6.

### P20-K6 · The parallel run and the cutover
- **Who:** club president, secretary, treasurer; Federation owner.
- **On the platform:** the report worked on the platform's screens (every match and its band, every household proposal, every group, every custom field and its classification, every form and its door, every child and the adult through whom they entered, every remainder); a weekly open count; sign-off and cutover as a dated decision on the register row; Breeze read-only; the archived export on the drive verified before the club cancels, because the vendor queues deletion on cancellation.
- **Tests:** club plan §8.4–§8.5.
- **Refuses:** cutover before sign-off; cancellation advice before the export is verified.
- **Must reach:** meets. **Slice:** C6.

### P20-K7 · A club on no system
- **Who:** club secretary.
- **On the platform:** the same path from a spreadsheet upload: the same classification, the same queue, the same rules.
- **Tests:** club plan §4.4 (the spreadsheet path), §8.3 (the same classification and rules).
- **Must reach:** meets. **Slice:** C6.

---

## L. The member's own view of their club

### P20-L1 · What I can see of myself
- **Who:** member.
- **In Breeze:** My Profile: own fields the role allows, own giving, own attendance, own tags, volunteer schedule.
- **On the platform:** scoped standing; own groups (B1); own attendance (B2); own statement with the club if B3; own availability (B2b); the three consents.
- **Tests:** the member lens; R27.
- **Refuses:** anything about another member from the club side.
- **Must reach:** meets. **Slice:** B1, B2, B2b.

### P20-L2 · Is there a note about me?
- **Who:** member.
- **In Breeze:** private notes are author-only on screen and exportable by anyone with Export.
- **On the platform:** no notes exist; a follow-up's one completion note is the club's record; whether the member may know one exists is Q-46.
- **Tests:** r2; Q-46.
- **Must reach:** guarded until Q-46. **Slice:** C2.

### P20-L3 · The club's directory, from a member's side
- **Who:** member.
- **On the platform:** the members' directory filtered to the club shows only members who chose display; the roster never shows to a member; contact runs through the broker.
- **Tests:** P19; R27; D28.
- **Refuses:** the roster to a member; a signed-out view.
- **Must reach:** meets. **Slice:** DIR1.

---

## M. Coverage

Fifty-nine journeys: fifty-two of 1 October 2026 and seven added on 2 October 2026 (P20-A7, D6, D7, D8, I7, I8, J4) for the club's part in P21–P25 and the federation research. Every one names a by-law, a decision, a rules-register row, a design-document section, a slice gate or a labelled design choice. Seventeen are guarded by a named gate, which is the correct state until the gate lifts. The ten of 1 October are guarded by Q-41, Q-37/D5, Q-44, Q-46, B3 (three journeys), B5, D55's silence and the two-household case under R4. The seven of 2 October are guarded by Q-70, D5 (P20-D6's weights, with P20-D3), Q-131, Q-195, Q-180, Q-205 and Q-227. The canonical J08 and J14 stand; the twenty journeys the club plan listed in §11.2 are absorbed here (P18-J01→P20-D1, P18-J02→P20-D1, P18-J03→P20-D3, P18-J04→P20-A1/A4/A6, P18-J05→P20-L2, P18-J06→P20-I2, P18-J07→P20-I3, P18-J08→P20-D2, P18-J09→P20-C3, P18-J10→P20-L1, P18-J11→P20-H3, P18-J12→P20-J2, P18-J13→P20-J2, P18-J14→P20-K3, P18-J15→P20-K6, P18-J16→P20-K6, P18-J17→P20-K4, P18-J18→P20-K5, P18-J19→P20-H4, P18-J20→P20-H2).

What the corpus does not cover, on purpose: Breeze's worship, service-planning and song tools (not a federation's need, Addendum 2 §3.1); name-tag printing (not a goal); a free-form form builder (B6 stays a question); a case file on a person (the record has not decided to keep one).

**For the Hub's component.** Read together, A–L describe the clubs component: the roster and queue (A, B), groups (C), seats (D), events and the door (E), volunteers (F), follow-ups (G), communications (H), the treasurer's desk and the statement (I), the dashboard and the roll-up (J), the migration path (K) and the member's club view (L). The slices that build it are B1, B2, B2b, C1–C6, DIR1–DIR2, with B3 and B5 gated. Each journey here is the exit test for its slice; a slice is done when its journeys reach the class named and the Delivery Status says so. The seven journeys added on 2 October 2026 are also exit tests for slices of other notes: CR5 (P21), CV4 (P22), RL4 and RL6 (P23), MG1 (P24), and AD5 with YL5 (P14, P25).
