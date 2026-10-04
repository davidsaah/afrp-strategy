# The directory, in its three formats

### The members' directory at Federation and club scale, the professional services directory, and the leadership directory

**Design note P19 · 1 October 2026 · for the Hub's `memberdir`, `network`, `clubs` and `authority` modules**

**David's direction, 1 October 2026:** *"We have historically published a Ramallah directory for the federation, allowing people to find other folks from Ramallah who are near them. The directory has a couple of different formats. 1. a full directory with membership identified; this is at the federation scale and at the club scale. 2. A professional services directory with people's places of business, doctors, lawyers, engineers, etc. 3. Leadership directory of all leadership and voting status, with committees that they are on; this is at the federation scale that also integrates with the club scale."* And his three answers the same day: all three formats live **on the platform only**, behind sign-in, nothing printed or exported; the professional services directory is **members only**; "voting status" in the leadership directory means **whether the seat carries a vote under the by-laws**, never the person's own franchise.

Those answers reaffirm rules the record already holds (the directory's ceiling is members, D28; export is refused by design; a seat's vote is By-Law 6.2.2's) and add no decision. This note says what each format is, what slice 10 already built of it, what is missing, and what a build session takes.

**Precedence (D41).** The by-law texts, then the register and the named design documents (`AFRP-Camp-Directory-Network-Plan.md`, the Rules Register's identity-and-directory rows, D6, D17, D22, D28, R7, R27), then the prototype's `#/directory`, then `memberdir` as built.

---

## 1. What the record already holds

**Built (the `memberdir` and `network` modules; slices 7b and 10 for the grace and the listings).** A members-only directory behind sign-in; nothing about a living person without sign-in (D28); minors never in any directory payload, and no birth date means possible minor (R7); per-field visibility as a dated consent, with display, contact and export as three separate consents (R27); contact through a broker so the address itself never ships; search with transliteration folding and aliases; browse axes name, club, city, interests, languages, volunteering, family and clan (Network Plan, decisions taken); a lapsed member stays visible for the 90-day grace attested on the register (D6's parameter, slice 7b) and then drops; the RBPN profession listing free to every consenting member and the promoted business listing as the paid product, each verified by the RBPN desk for membership and ownership and refused under a named line of the exclusion policy (slice 10); the Magazine's professional directory fed from the same listings, a lapsed listing dropping out; a living name printed in the Magazine only with the person's own print consent and the directory gate (slice 7b); bulk export refused for everyone; the Network Plan asks for export logging to complete that control.

**Historically (the intakes, role-level).** The Federation printed and sold a membership directory with a corrections process (the officer archive, 2010s); club-president directories for several years sit in the Federation's club folder (not opened; who produced them is not recorded); and the Federation printed an annual Committee Directory listing the Executive Committee, every club's president, "community contacts" for places with no club, and every committee with its chair and members, noting which Board seats were eligible to vote; who maintained it was not recorded. None of these is published today; the Committee Directory continued to 2026 as a file in the shared drive.

**What the three formats are, against that.** Format 1 is the built directory with two things made explicit: membership, and the club. Format 2 is the built RBPN listing, named for what it is. Format 3 does not exist yet: it is a directory of seats, not of people, and it depends on the officers form (club plan, slice C1) and on committee seats the Hub only partly holds.

---

## 2. Format 1 — the members' directory, with membership identified, at Federation and club scale

**What "membership identified" means here.** Presence in the directory is itself the Federation's assertion of membership: only a member in good standing, or within the grace window, is shown at all (D6, slice 7b). A row therefore carries a membership mark and the club or clubs the member belongs to, as facts the Federation states, not fields the member consents to; what the member consents to is every other field (R27). *Design choice:* a row within the grace window shows exactly as it did before the lapse; the directory never labels anyone "lapsed", because standing is shown to the member on their own home and to their club on the roster, and to nobody else.

**Federation scale.** The directory as built: every consenting member, searchable and browsable on the existing axes.

**Club scale.** The same directory filtered to one club, reachable from the club's page and from the club axis — not a second directory. Any signed-in member may filter by any club (the directory is a Federation object, Four-Lens §2). The club's officers have a different object for a different purpose: the roster (B1), which shows every member of the club including those who declined display, with both standings; the roster is never a directory and never leaves the club lens.

**"Near them."** Today a member finds people near them by city. The record is silent on anything closer: a metro area derived from the city or postcode already displayed under consent, or a radius search on a stored address, which is a new purpose nobody has consented to and which would reveal distance even when the address is withheld. The Network Plan's browse axes do not include distance. *Q-48.*

**Community contacts for places without a club.** The Committee Directory listed a contact person for communities with no chapter club. The platform has no such seat; the by-laws do not name one; the Membership Committee's composition (8.12.1: one member from each community that has a chapter) does not reach them. *Q-49: whether a community contact is a seat the Federation appoints, and what it is shown as.*

**What is missing to build.** The membership mark and the club filter on the directory row and search (small); the club's page linking to its filtered directory; nothing else. The grace rule, consents, broker and minors' exclusion all stand.

---

## 3. Format 2 — the professional services directory

**What it is.** The RBPN profession listing, free to every consenting member, and the promoted business listing, paid, both verified by the RBPN desk (slice 10). A listing carries the profession, the practice or business, and the place of business; **the place of business is listing data, shown under the listing's own consent, and is never the member's home address**, which stays under the member's field consents and the broker.

**Audience.** Members only, signed in (David, 1 October 2026; D28's ceiling). The Magazine's printed professional directory is the one printed surface, and it already runs on the person's print consent and the directory gate (slice 7b).

**Browse.** By profession and by city, as the directory's axes allow; the professions are the RBPN taxonomy the desk maintains (doctors, lawyers, engineers and the rest). "Near me" is the same open question as Format 1 (Q-48). Doctors, lawyers and other licensed professions: the platform states what the member listed and verifies membership and ownership; it does not verify a licence, and the listing says so. *Design choice, recorded here.*

**Money.** Paying for a listing on the platform is still not decided (workflow `directory-consent`, open item); the promoted listing's subscription is recorded as AFRP's receipt (slice 10). AFRPWorks sits beside the RBPN job board (D64) and does not touch this directory.

**What is missing to build.** Nothing structural; the page should be named "Professional services" on the member lens so that members find it as a directory and not only as RBPN, and a lapse must drop the listing on the same grace as the row (it does: `directory → magazine` hand-off).

---

## 4. Format 3 — the leadership directory

**What it is.** A directory of **seats**, each with the person who holds it today and the dates: the Executive Committee; the Board of Directors as By-Law 6.2.2 composes it (the Council of Past Presidents, the Council of Chapter Club Presidents, four members at large, the Executive Committee, one member each from RBPN, the Young Leader Committee, the Magazine and the Ramallah Foundation; the Historian the Board elects for three years; the Executive Director and the Executive Assistant as non-voting members); the Council of Chapter Club Presidents (6.4.1); every standing and special committee with its chair, co-chair and members (8.x); the affiliates' Boards where the record holds them (ARFECF's fifteen seats in three regions, 2015 by-laws); and, at club scale, each club's officers from the officers form and any programme seats the club holds (club plan §3.4).

**"Voting status."** A property of the seat: whether it carries a vote on its body under the text that composes the body (6.2.2 and 7.1.1 name which Board and Executive Committee members vote and that the two employees do not; a committee's by-law or charter names its own). Shown beside the seat, with the by-law cited. Never the person's franchise as a member: whether a leader is a certified voting member for the Convention (9.1.4) is a fact about the person's standing and is not in this directory (David, 1 October 2026).

**Where the seats come from.** The club officers and the Council and Board seats that derive from them: the officers form (club plan §4.1 step 2; slice C1). The Executive Committee and members at large: the election results the voting module records (D4). Committee seats: the committee workspace, which is the crosswalk's design note P1 and is not written; until it is, committee seats are a register the office keeps, dated, with the appointing authority named. (*Since 2 October 2026:* P1 is now written, and committee seats come from its register, CW1.) **The designated Board seats** each enter with their own appointing text. The RBPN, Magazine and Foundation members are each appointed for one year at the General Assembly by their body: the RBPN Committee (6.6.1, never a past President), the Magazine (6.7.1) and the Ramallah Foundation (6.8.1). The Young Leader Committee's member has no appointing text and enters as a register row naming who seated it (DIR2, corrected 2 Oct 2026). The Magazine's 6.7.1 board is not evidenced in practice, so its seat shows "appointing body not evidenced" beside 6.7.1 (P24 §4; Q-192). **The Young Leader Committee itself** is composed by the paragraph under By-Law 8.10: a chairman and four members, appointed by the President with the Board's approval, all alumni of Project Hope or Leadership Ramallah. The leadership directory shows those five seats, each with its alumni check (P25 §4; P12 §2.9). In practice (research, 2 Oct 2026), the committee has two co-chairs and members listed by club city, and goes by the names Young Leaders Committee and Youth Outreach Committee. The practice list is linked as a drive document, not seated; see Q-179, Q-175 and Q-51. Affiliate seats: the register rows the affiliates' Boards set (club plan §6.8). The Committee Directory on the drive is evidence for the first load and the archive of record afterwards (D66); the platform's page replaces the printed one.

**Contact.** A seat is reached through a **seat channel** the office sets (a role mailbox or the office itself), never through the officer's personal details, which the officers form holds for the office (the functional seat P16 §5 names) and the Council alone (club plan §3.1; R27). A member who is also in the members' directory can be reached as a member through the broker, by the member's own consent. *Design choice.*

**Audience.** Members, signed in. The Board and the Council read the same page; the office keeps the by-law roster (6.2.2) as a record it can print for a meeting as an office document, which is not a directory and is not member data beyond names and seats. *Design choice: the office's printable roster carries seats and names only, never contact details.*

**Club scale.** The same page filtered to one club shows its officers, its president's Council and Board seats, its programme seats, and its delegates once selected for a Convention (9.1.3). A club's officers see their own club's seats in full on the club lens as well.

**What is missing to build.** The page itself; the seat-vote property with its citation on each body; the seat channel; the committee register until P1's slice CW1 lands; the first load from the drive's Committee Directory as an office task with names typed by the office, never imported from the file.

---

## 5. Rules the three formats obey

1. The ceiling is members, signed in (D28). Nothing about a living person shows signed out, in any format.
2. Presence in the members' and professional directories follows standing and the grace window (D6, slice 7b); presence in the leadership directory follows the seat's dates.
3. Every personal field is the member's own dated consent (R27); membership, club and seat are the Federation's facts and are shown as such.
4. A minor never appears in any format (R7); a seat is never held by a minor.
5. Contact runs through the broker for members and through the seat channel for seats; no address, phone or email ships in any payload.
6. No printed or exported edition of any format (David, 1 October 2026; export refused by design). The Magazine's professional directory is the one print surface, on print consent. The office's meeting roster is an office record of seats and names.
7. A lapsed member's row and listing drop together after the grace; a seat ends on its date and the directory shows the successor.
8. Every refusal names its rule.

---

## 6. What this note raises

| Q | Question | Owner |
|---|---|---|
| Q-48 | "Near me": whether the directory may place members by metro area derived from what they already display, or by distance from a stored address, which is a new purpose needing its own consent | Membership Committee · Legal Advisor |
| Q-49 | Community contacts for places without a chapter club: whether it is a seat the Federation appoints, who appoints it, and what the directory shows it as | AFRP Board · Membership Committee |

Open items carried, not new: paying for a listing on the platform (`directory-consent`); the committee workspace note P1, on which committee seats depend; the club register's count (Breeze Parity §5 q8), which bounds the club-scale views.

---

## 7. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| DIR1 The members' directory, membership identified, at club scale | The membership mark and club(s) on the row; the club filter and the club page's link; the professional services page named and browsable by profession and city; a lapse dropping row and listing together on the grace | §2, §3 | None |
| DIR2 The leadership directory | The seats page from the officers form, the election results and a dated committee register kept by the office — the Council of Past Presidents and the Young Leader Committee's Board seat have no appointing text in the by-laws and enter as register rows naming who seated them; the other three designated Board seats are appointed for one year at the General Assembly by the RBPN Committee (6.6.1), the Magazine (6.7.1) and the Foundation (6.8.1), and enter with that dated act (corrected 2 Oct 2026); the seat-vote property with its citation per body; the seat channel; the club-scale filter; the office's printable meeting roster of seats and names | §4 | C1 (the officers form); P1 for committee seats, with the office register until then |
| DIR3 "Near me" | A metro or distance axis | §2 | Q-48 |

Journeys proposed for the workbench queue: **P19-J01** a lapsed member's row and listing drop on the same day after the grace, and never show "lapsed"; **P19-J02** a club's filtered directory shows only consenting members and the roster shows all, and no member sees the roster; **P19-J03** a business address shows under the listing's consent while the home address stays withheld and the broker still works; **P19-J04** a seat shows its vote with 6.2.2 cited, and the person's own franchise appears nowhere on the page; **P19-J05** a seat's holder is reached by the seat channel and the officer's personal details are not in the payload; **P19-J06** nothing in any format renders signed out, and no minor renders signed in.

---

## 8. What changes in the site's data with this note

`workflows.yaml`: `directory-consent` gains the three formats as steps and this note as a source. `experiences.yaml`: the member, club officer and committee member lenses name the format each uses. `questions.yaml`: Q-48, Q-49. The crosswalk: row D4 updated and a P19 row. `plan/MASTER-PLAN.md`: rows DIR1–DIR3.
