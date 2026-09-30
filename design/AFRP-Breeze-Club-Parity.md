# Breeze parity for the clubs — the crosswalk and the plan

### What Breeze does, what the Hub already does, what is built next, and what the Federation sees rolled up

**Written 14 September 2026** on David's direction of that day: *"we use breezechms.com for managing the clubs. Take a deep dive into what it is able to do and integrate it into the platform where each of the clubs has the same capability as this and the federation has the ability to see the roll up of it."* It extends, and does not replace, `AFRP-Addendum-2-Breeze-Replacement.md` §3 (August 2026), which established that a federation uses roughly 70% of a church management system and that three things are genuinely hard: texting, child check-in, and twenty-six migrations that are each a relationship.

**Sources, read 14 September 2026:** breezechms.com (home, pricing), the Breeze API reference (app.breezechms.com/api), and the support knowledge base articles *Setting Up Check In at Your Church*, *Follow Ups*, *Getting Started With People*, *Getting Started With Users & Roles*, *How To Use Tags*, *Volunteer Management — Getting Started*, *Getting Started with Events*, *Online Directory with Member Access*; GetApp's feature inventory for Tithely Church Management. Breeze is now sold as "Tithely Church Management" at a flat $72 a month with unlimited admin users and people, texting at 250 messages a month then $10 per 500, worship tools as a $29 add-on. The API is key-per-church, read and write, no webhooks, some responses cached up to fifteen minutes, wrappers "not necessarily created or maintained by Breeze".

---

## 1. Breeze, as it reads today

Breeze has one object at the centre — the **person profile** with families, custom profile fields and a status — and everything else hangs off it.

| Module | What it actually does (support documentation) |
|---|---|
| **People** | Profiles with configurable fields; families; filters as simple or compound as needed (wildcards, "has any data", "has no data", exact); saved searches; a default filter per user; the **Action Panel** on any filtered list — email, text, export (Excel, printed/PDF directory, mailing labels, name tags, mail-merge letter), save the search, assign/remove tags in bulk, update a field in bulk, archive, delete. |
| **Tags** | Folders of tags; a person in any number of tags; bulk assign from a filtered People list; tags drive event eligibility and reporting; a tag has no leader — the guidance is to put the leader's name in the tag's name. |
| **Events** | Calendars (several, with per-user permission and website publishing), recurring events, external calendar sync; per event: Overview (attendance total, comparison graph), Attenders (attended / eligible-but-absent, filterable), Reports (by date and event, consecutive misses, printable sheets), Check In, **Alerts** (email when someone has missed N events), Volunteers, Settings. |
| **Check In** | Eligibility "Everyone" or specific tags; modes incl. self check-in kiosk; name tags with profile fields, allergies, and a 3–4 digit **security code shared between child and parent** for secure pick-up; a check-out option; attendance is what check-in records. |
| **Volunteers** | Per event: Teams → Roles with a quantity needed and a leader (notifications sent from the leader); Assign mode (schedule people) or Invite mode (people choose); reminders; declined RSVPs; blockout dates in Member Access. |
| **Follow Ups** | **Options** (name, description, default assignee, days to complete) then **assignments** of an option to a person — from the profile, the Follow Ups menu, in bulk, or to a whole tag; a dashboard of assigned-to-me / all; complete from the email; weekly summary; bulk actions on the people behind a set of follow-ups. The stated purpose: "ensures people don't fall through the cracks, provides team accountability". |
| **Forms** | Public forms (link, embed) whose entries attach to a profile; field types text/essay/choice/dropdown/date/address/signature; used for registrations. |
| **Giving** | Online giving by web and by text; recurring; funds; batches of contributions entered by hand; associations of transactions with profiles; giving reports (top givers, year-to-date); statements members can print themselves; pledge campaigns. |
| **Communications** | Email to any list with a drag-and-drop editor; texting to any list; unsubscribe managed by the member. |
| **Users & Roles** | Account owner; default roles Admin (everything, incl. finance), Standard (people, tags, events, follow-ups, forms; no finance), Limited (view people), **Check In** (a volunteer who runs the kiosk and can add a person there), **Member** (own profile and family, own giving, online giving, the directory tag). Custom roles per area; the guidance is to keep roles broad. |
| **Member Access / Online Directory** | A tag named "Online Directory" plus a Member-role permission to view people in it; members then see a People section of exactly those; per-field visibility; an opt-out article. |
| **Reports** | People, contributions and attendance reports from filters, in table and graph form; Excel export. |
| **Move-in / API** | Excel import of people; the API for people, tags, events, attendance, volunteers, forms, contributions, families, account log. |

---

## 2. The crosswalk

Read each row as: what a club does in Breeze today → where the Hub does it, or does not.

| Breeze | A club uses it for | The Hub today | Gap | Slice |
|---|---|---|---|---|
| People profiles, families | The roster; who is in which household | `core.Person`, `Household`, `Membership` (club and national, two standings); the club roster (`/club/<code>/roster/`) with two status columns; households with R6 authority (`/club/<code>/households/`); Member 360 on the federation lens; the merge queue | **Custom profile fields per club** — none. Whether clubs need them, or used them only for what the Hub models properly (standing, household, consent), is a question below | B4 (question) |
| Search, saved searches, Action Panel | Find a set and act on it | The roster sorts and flags; mailings choose an audience by standing | **A filtered list a club acts on** — filter the roster by standing, household, group, age band; then mail it, tag it, or open a follow-up for it. No saved searches | **B1** (filter → act), saved searches later |
| Tags & folders | Committees, the dabke troupe, the youth, the sunshine list | Nothing at the club level (programme cohorts exist on the programme lens; federation tags do not exist) | **Club groups** — folders and groups, members added singly or from a filtered roster, a group as a mailing audience and later as event eligibility; officer-only, never in the directory; counts to the Federation under the floor | **B1** |
| Events & calendars | The club's calendar | `events.Event` is club-scoped, published, priced, with signups, waitlist and questions — **but created only from the Federation registry**; the member sees one calendar; no recurrence | **Club-created events**, recurrence, eligibility by group | B2 |
| Check In, attendance, alerts | Who came; who stopped coming | `event:checkin` is a permission with no screen and no record; camp's release list under R6 is the safeguarding model | **Attendance**: check-in at the door and after the fact, attendance per event and per person, "missed N" feeding a follow-up; **child check-in through the R6 release list**, not a printed code | B2 |
| Volunteers | Set-up, kitchen, ushers per event | Programme committee seats; camp staff screening; nothing per event | Volunteer roles and quantities per event; assign and invite | B2 (second half) |
| Follow Ups | Welcome the new family; call the lapsed; visit the bereaved | Nothing. The Hub has invitations (a milestone fired one) and operational notices, not tasks | **Follow-ups**: options per club, assignments to an officer with a due date, done with a note, a dashboard of mine and all, raised in bulk from a filtered roster; a lapse or a death raising one automatically where a rule names it | **B1** |
| Forms | Sign-ups, registrations | The join wizard; event questions; the camp application; the scholarship door | A generic form builder is real work (Addendum 2 §3.2) and most of what clubs used forms for is an event signup with questions | B6 (question) |
| Giving | Gifts to the club; year-end statements | Gifts to a **purpose** on an entity's books through the one payment door (`funds.services`); receipts and the contribution statement on `/me/payments/`; restricted funds; the ledger's `ClubLedgerProfile` already decides agency vs revenue per club | **Club purposes**: a club's own giving purposes on the club's books through the same door (a purpose parameter, not a fifth caller); statements per club; pledges are the campaign template, not built | B3 |
| Email | The newsletter | Club mailings, consent-filtered before send, the withheld kept by name (`/club/<code>/comms/`); operational notices to lapsed members | A group as an audience (B1); a drag-and-drop editor is not a goal | B1 |
| Texting | Reminders | None. Consent per channel exists | **SMS** needs a provider, a number, 10DLC registration — calendar time and a contract, a decision before a build | B5 (question) |
| Users & Roles | Who may do what | Grants (person, role, scope) at `club:<code>`: president, secretary, treasurer, events — exact, never inherited, ended never deleted | A **check-in volunteer** role at club scope (the permission exists) | B2 |
| Member Access / Online Directory | Members find each other | The member directory with per-field, dated consent (`memberdir`) — stronger than a tag; the member lens shows own payments, programmes, inbox | Own attendance and own groups on the member lens | B2 / B1 |
| Reports | Attendance, giving, people | The Federation dashboard with suppression; the club dashboard's counts | Attendance and follow-up reporting per club; the **Federation roll-up** of groups, follow-ups, events and attendance per club, every cell under the floor | **B1** (roll-up of B1 objects), B2 |
| Export, print directory, labels | Onboarding, the printed directory | Excel export and the printed directory are **refused by design**: directory consent covers display to signed-in members, not extraction (memberdir/export_refused) | Not a gap — a decision the record made. Said plainly below | — |
| Move-in / API | Getting the club's data in | Nothing reads Breeze. Identity resolution and the merge queue exist | **Breeze import**: read-only pull per club (people, families, tags, events, attendance, contributions) into staging rows, resolved against the register, merge queue for the review band, parallel run, cutover (Addendum 2 §3.4) | B4 |

### What the Hub will not copy from Breeze, on purpose

- **Export to Excel, printed directories, mailing labels of members.** Directory consent is a purpose; extraction is another purpose and needs its own basis. The refusal names its rule and is logged. A club that needs a mailing list mails through the platform, which keeps the withheld by name.
- **Delete a person.** A record anything points at is never deleted. Death terminates it; a merge closes it with the map of what moved.
- **A leader named inside a tag's name.** A group has a leader as a person on the roster, or none.
- **Notes on a person as free text everywhere.** A follow-up carries one note on completion, written by the officer, visible to officers of that club, never to the member's directory and never to another club. Anything more is a case file, and the record has not decided the platform keeps one.
- **Unlimited admin users with everything.** Every officer holds an exact grant at their club.

---

## 3. The plan

| Slice | Build | Exit |
|---|---|---|
| **B1 · Club groups, follow-ups, the acting roster, the roll-up** | `clubs.ClubGroup` (folder, name, leader seat optional, note) and `ClubGroupMember` (dated; ended, never deleted); the roster filters (standing national / club, household, group, adults / minors-never-listed) and the acting panel: mail this set, add this set to a group, open a follow-up for this set. `clubs.FollowUpOption` (name, description, default assignee = an officer seat, days to complete) and `FollowUp` (person, option, assigned officer, opened by, due, completed at, completion note); the club's follow-ups desk (mine / all / overdue); a rule-named automatic follow-up when a member of this club lapses nationally, if the club has switched the option on. The member lens shows a member their own groups. The Federation registry's clubs page rolls up per club: groups, members in groups, open and overdue follow-ups, mailings this year — each count under the floor. | A secretary opens a group from a filtered roster, mails it, and the withheld are named; a follow-up opened for a lapsed member lands on the treasurer's desk with its due date and is completed with a note; the member sees the group on their own record and no other club's officer can; the Federation sees the counts and not the names; the corpus rows flip; deploy live. |
| **B2 · Club events with attendance and check-in** | Events created and published from the club lens; recurrence as a series; eligibility by group; a check-in screen at the door (signed-up and walk-up), attendance per event and per person, "missed the last N" → a follow-up; child check-in through the R6 release list; a `club_checkin` role; volunteer roles and quantities per event with assign and invite; the member lens shows own attendance; the roll-up adds events and attendance per club. | The club calendar is the club's; a member's attendance is a record they can see; a child leaves with a named adult on the release list and nobody else; the Federation sees attendance per club under the floor. |
| **B3 · Club giving** | A club's own purposes on its books through the one payment door (no fifth caller); the treasurer's giving desk; the member's statement per club; the agency/revenue treatment already on `ClubLedgerProfile` applied; pledges deferred to the campaign template. | A gift to a club lands on the club's books and the member's statement; national and club money never mix; a purpose outside the club's entity refuses by name. |
| **B4 · Breeze import** | A read-only connector per club (API key held as a secret, never in the repo; 20 requests a minute); a pull into staging rows; identity resolution against the register with the merge queue for the review band; a parallel-run report the club's officers verify; cutover as a dated decision. | One club moved end to end with its officers signing off the roster; nothing written to Breeze; every unresolved pair in the queue, none merged by software. |
| **B5 · Texting** | A provider behind a port, per-channel consent already modelled, 10DLC registration, opt-out handling; decision first. | Gated on David: provider, budget, who registers the brand. |
| **B6 · Forms** | Only if B2's event questions and the existing doors leave a real gap — a question below. | — |

B1 and B2 are built in the session this document opens (B2's volunteer half is B2b). B3–B4 follow in the queue behind 7b, 8 and R1 unless David reorders.

---

## 4. Rules the new objects obey

1. **A group is the club's, not the member's.** Officers of that club read and write it; the member sees the names of their own groups on their own record; the directory never carries it; another club never sees it. Counts to the Federation under the suppression floor, composed like every other count.
2. **A follow-up is a task about a person, not a note about them.** It carries the option, the assignee, the dates and one completion note; it is closed, never deleted; it is read by the officers of that club and by nobody else, and it is not in any directory payload or export.
3. **Nothing automatic without a named rule.** A lapse raises a follow-up only if the club has switched that option on, and the follow-up names the rule that raised it.
4. **Minors are never listed** where a group or a follow-up is shown outside the club's own officer screens, and never in any count that could identify one (R7).
5. **Every refusal names its rule** — the wrong club, the missing seat, a minor where a minor may not be.

---

## 5. Questions for David

1. **Texting**: which provider, whose budget, and who registers the AFRP brand for 10DLC? Nothing texts until this is answered.
2. **Custom profile fields**: what did the clubs actually record in Breeze's custom fields? If it was standing, family and consent, the Hub already holds it properly; if it was something else (dietary, skills, clan), say what, and B1's groups may cover it.
3. **Club giving**: do clubs want gifts to the club taken through the platform onto their own books (B3), or do they keep their own processors? The ledger profile already knows each club's treatment.
4. **Which club goes first** for the Breeze import, and who holds its Breeze API key?
5. **Child check-in**: does any club use Breeze's printed security codes today? If so B2's release-list check-in is their blocker, not a nicety.
6. **Forms**: what did clubs build in Breeze forms that is not an event signup, a join, or an application?
7. **Printed directory and labels**: the platform refuses these by design. Is that accepted for the clubs, or does the Board want a consented print purpose?
8. **The club register itself**: 17, 18 or 19 clubs — the question already open from the Drive files.
