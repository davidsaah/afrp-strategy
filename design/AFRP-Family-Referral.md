# Family referral into club follow-ups

### A member refers a Ramallah household that is not a member; the club named gets a follow-up; the referred person hears from nobody until they say so

**Design note P4 · 1 October 2026 · for the Hub's `clubs`, `member`, `comms` and `reporting` modules**

This note answers crosswalk row D7 (MIN Sep 2023: clubs drive national sign-ups; families refer non-member Ramallah families). It rests on the club plan (`AFRP-Club-Experience-Plan.md` §3.2 the secretary's queue, §4.1 the officer year, §9 consent) and the club journeys (`AFRP-Club-Journeys.md` P20-A1 a new person joins, P20-G1 the welcome call); on Breeze Parity §4 (a follow-up is a task about a person; nothing automatic without a named rule); on D60 as the precedent for a contact record that is not a membership; on R27 and S1; on D30, D31, D36 and D53 for what the family tree may and may not supply; on Article IV (membership is the Federation's to grant); and on the intakes (D54). The Strategic Planning Committee's minutes of September 2023 are cited as the crosswalk carries them; the minutes themselves were not read for this note. The intake cards hold no member-referral or sponsor scheme: the "buddy system" in FED2 is the Deputy President's pairing of clubs (crosswalk B11), and the 2020–21 membership drive planned calls and letters to prospects by the committee, not referrals by members.

**Precedence (D41).** By-law text first, then the register and the named design documents, then the prototype as story, then the Hub as what is. Where the record is silent this note says so and raises a question; it picks no default.

**Public-repo rule.** No living person, no club beyond what the record names, no figures.

---

## 1. What the record already holds

**Built.** Club follow-ups as tasks with an option, an assignee, dates and one completion note, closed and never deleted, read by the club's officers only (B1; Breeze Parity §4 r2); the join wizard with channel verification before anything beyond a draft is stored (S1) and the club named at join; the comms desk with the three classes and per-channel consent (R27); the Federation's clubs page as counts under the floor (B1; S7, R43). **Designed, not built:** the secretary's queue receiving a join that names the club (C2; club plan §3.2); the rule-named follow-up option "new club membership" opening when a join lands (P20-G1, C2); a contact record for a club (name, one verified channel, consent) that is not a membership (P20-A1, a design choice for B2b and C2). **Decided.** D60: a non-member buying an Arabic class is kept as a contact record (name, verified channel, consent), never a membership. D36: the tree is not a mailing list; tree-driven communication goes to signed-in members about their own branch, and the platform never initiates contact with a person in the file who is not a member. D30: a node is never a lineage claim and no membership decision reads it. D31: life events queue. D53: the tree is on the Heritage branch. **In the by-laws.** Membership is open to those 4.1.1 or 4.2.1 describe and is the Federation's to grant (Article IV); a Board member "shall … encourag[e] A.F.R.P. membership" (6.2.3); the Membership Committee prepares applications and a signed letter identifying the applicant and household is accepted as one (8.12.2); dues count for voting only when paid from the applicant's own funds (8.12.4). **Historically (role-level).** The Federation's 2020 Board minutes recorded that large clubs have high club membership and low Federation membership; the 2023 committee minutes (per the crosswalk) asked clubs to drive national sign-ups and families to refer families; the 2020–21 drive planned a prospect list worked by the committee by letter and call. No referral object, incentive or scheme is written anywhere in the record.

**What is missing.** The referral as an object; the rule that opens the club's follow-up; what the referrer may see; the refusals; the counts; and the incentive question.

---

## 2. The referral as an object

A **referral** is a dated row with: the **referrer** (a signed-in member, any scope, any club or none); the **referred household**, held as a **contact record** for the club named — a household name and one channel the referred adult supplies, which becomes a verified channel only when that adult verifies it (S1), with the adult's own consent rows (R27) — and never a membership; the **club** the referrer names (or the club of the referred household's locality as the referrer states it; the platform does not infer a club from an address); the **follow-up** it opens on the club's desk; and its **state**: *received*, *awaiting the person*, *contact made* (the referred adult has verified and consented), *closed* (the club closed its follow-up, or the contact expired). *Since 2 October 2026:* the contact record note (P21, `AFRP-Contact-Record.md`) holds the referred adult as the *referred* role on one person record with dated, scoped roles (P21 §2, §4). The role's scope is the club named, and "tell the referrer" is one of its fields. Its retention row is P21 §9's, with no value. That design is DRAFT under Q-70 and is not adopted, so this paragraph stands until Q-70 is answered (CR5; RF1 creates its role on CR1).

**How the referred person is reached — what the record allows.** The platform sends nothing to a channel the referrer typed. D36's principle — the Federation does not initiate contact with a person who never agreed to hear from it — is decided for the tree and is the closest rule the record holds; D60's contact record exists only with the person's own verified channel and consent. So the referrer carries the invitation: the platform gives the referrer a one-use invitation (a link or code tied to the referral and the club) to pass on by their own means; the referred adult opens it, verifies a channel, reads what the club and the Federation may do with the record, and consents or not. Only then does the contact record exist and the club's follow-up name a person. Whether the platform may instead send **one** operational invitation to a channel the referrer supplied is not decided and is raised (Q-68); until answered the platform refuses to send it, naming D36.

**The club's follow-up.** When a referral is received the club's desk shows a count ("referrals awaiting the person") and no name. When the referred adult consents, the rule-named option **"referral received"** opens a follow-up on the club's desk (Breeze Parity §4 r3: a named rule, switched on per club; a club that has not switched it on sees the contact in the secretary's queue instead, club plan §3.2) with the club's default assignee and days; the welcome call (P20-G1) is the officer's act; the completion note is the one note (r2). A join that follows comes through the join wizard naming the club (P20-A1) and lands in the secretary's queue as any join does; the referral's state is unaffected by it (the outcome is the person's, §4).

**What the referred adult sees.** Before consent: the invitation page states who referred them (the referrer's name as the referrer chose to show it — a design choice: the referrer may be named or anonymous to the referred person, and the platform never tells the club the referrer withheld their name), the club, what consent means (contact by this club about membership; nothing else), and the refusal route. After consent: a contact's own page, with their consent rows to change or withdraw at any time (R27), the club's seat channel, and the join door. A withdrawal closes the follow-up and the contact; the referral row stays as a dated fact with no name (closed).

**What the referrer sees afterwards.** That the referral was *received*, and nothing more: not whether the person opened it, consented, was called, or joined. The outcome is the referred person's and reaches the referrer only if the referred person chooses to tell them, or chooses on their contact page to let the referrer be told (a consent row of the referred person's, off by default; *design choice*). A member who later joins through the club shows in the directory under their own consents like any member; the platform draws no line from a referral to a directory row.

**Households and minors.** A referral names a household through one adult. No child is named on a referral, in a contact record or in a follow-up (R6; R7); a referred adult adds their household at join (8.12.3), and a minor's record then runs under the household's authority. A referral whose only named person is a minor refuses by name.

**The family tree as a source.** A member sees their own branch (D36; D17 for the living in-platform) and may notice a relative who is not a member. The referral form may be reached from the member's own branch, because that is a member acting about their own branch, which D36 allows. Three things the record does not allow and this note does not add: the platform does not show "not a member" on a tree node or list non-member relatives for referral (D30: no membership reading of the node; D36); the platform does not take a channel from the file (the file holds none the person gave for this purpose); the contact record is not linked to a tree node (the record is silent on a non-member's node; the link is raised, Q-69, not made). The referrer types the name and hands the invitation on, exactly as from anywhere else.

---

## 3. The refusals

- No marketing or programme invitation to the referred person before their own consent (R27; the comms workflow; D36); the invitation is carried by the referrer, not sent (Q-68 may change this one send).
- No national membership created by a referral, a contact or a club (Article IV; P20-A1): the only door is the join wizard, and the Federation grants.
- No referral of a minor except through a household's adult (R6; R7).
- No contact record without a verified channel and consent (S1; D60).
- No note on the referred person beyond the follow-up's completion note (Breeze Parity §4 r2); no outcome shown to the referrer (§2).
- No inference of a club from an address, and no second club's view of a referral: the club named sees it; the Federation sees counts.
- No referral by a person who is not a signed-in member; a club officer recording a prospect uses the contact record in the secretary's queue (P20-A1), which is a contact, not a referral.
- A contact record that reaches no join expires on a parameter the record does not hold (the Arabic term raised the same for its contacts); until set, a contact persists only while its consent does, and the parameter row refuses to compute a purge (Q-70).

---

## 4. What the Federation sees

Counts, under the suppression floor, on the clubs page (club plan §10.1) and in the Membership Committee's year-one baseline (D67): referrals received per club per year; awaiting the person; contact made; joins by members whose first scope followed a referral to that club (counted, never listed); withdrawals. A referrer is never identified in any count; a club never sees another club's referrals; the Membership Committee sees the Federation's totals and the per-club counts, which is what "clubs drive national sign-ups" needs to be measured by. Nothing here names a person outside the club that holds the follow-up.

---

## 5. The incentive question

The record is silent on whether a referral earns anything. If the Board wants one, the by-laws bound it: a dues credit applied to the referrer, or dues paid for the referred person, touches 8.12.4 — dues count for voting only when paid from the applicant's own funds — so a credit that pays part of anyone's dues could cost a vote; recognition without money (a count on the referrer's own record, a mention on the recognition register's terms) does not. The platform offers no incentive until a decision says what it is and who bears it (Q-71). The referrer's own record may show the count of referrals they made (received only), as a fact about their own activity; whether that count is shown is itself the committee's (the same question).

---

## 6. Rules

1. Membership is the Federation's to grant; a referral creates no membership (Article IV; P20-A1).
2. A contact record exists only with the person's own verified channel and consent (S1; D60) (D60 is written for the Arabic term; its use for this person is a reading, raised as one question for governance — Q-70's cluster).
3. The platform initiates no contact with a person who has not agreed to it (D36 by analogy; *design choice* until Q-68 is answered).
4. A follow-up opens only under a rule-named option the club switched on; it is a task, closed and never deleted, with one completion note (Breeze Parity §4 r2, r3).
5. The referrer learns that the referral was received and nothing of the outcome unless the referred person consents (*design choice*; R27).
6. No minor is named on a referral or a contact (R6; R7); a household enters at join through its adult (8.12.3).
7. The club named sees the referral; the Federation sees counts under the floor (S7, R43; club plan §10.1).
8. No node on the tree is read for membership and no channel is taken from the file (D30; D36); the contact is not linked to a node (silent; Q-69).
9. No incentive until decided; a dues credit is bounded by 8.12.4 (Q-71).
10. Every refusal names its rule.

---

## 7. What this note raises

| Q | Question | Owner |
|---|---|---|
| Q-68 | Whether the platform may send one operational invitation to a channel a referrer supplied, or whether the referrer must carry the invitation; and the wording of either | Legal Advisor · Membership Committee |
| Q-69 | Whether a non-member contact may be linked to a family-tree node, and who may make the link | Family Tree Committee · Membership Committee |
| Q-70 | How long a contact record is kept after the last activity when no join follows (the same parameter the Arabic term's contacts need) — one question across notes, Q-70: the non-member contact record and its retention (P4, P6, P12, P14, P15, P17). Added by the research round (2 Oct 2026): the Federation today holds non-members in four shapes, none with a stated purpose, consent or retention. Q-70 now asks David whether to settle on one contact record per person with dated, programme-scoped roles. A DRAFT decision is in P21 §11, not adopted | Membership Committee · Legal Advisor |
| Q-71 | Whether a referral earns the referrer anything; if money, how 8.12.4 is kept; if recognition, on which register | AFRP Board · Membership Committee |
| Q-72 | Whether a club may record a prospect without a referrer (the secretary's contact record, P20-A1) and under what consent that contact is first reached | Membership Committee · Legal Advisor |

Carried, not new: Q-46 (what a person who has never signed in is deemed to have consented to); Q-41 (a member's club, where the referred household's locality has two); D5 (the at-large roll for a referred household with no club in its locality — today the referral must name a club, and a referral to "no club" is refused by name until D5 lands).

---

## 8. Slices for the Hub

| Slice | Builds | From | Gate |
|---|---|---|---|
| RF1 The referral | The referral row and its states; the one-use invitation the referrer carries; the referred adult's verification and consent page; the contact record for the club (shared with P20-A1's contact); the rule-named option "referral received" opening the club's follow-up; the referrer's "received" view and nothing more; the referred person's consent to be told; the refusals; the counts on the clubs page and the baseline; the expiry parameter as a row with no value | §2–§4 | C2 (the secretary's queue and the club contact) live; Q-68: no platform send until answered; Q-70: no purge until set; a referral to "no club" refused until D5 |
| RF2 The one invitation send | The single operational invitation from the platform, if Q-68 allows it, with its wording adopted | §2 | Q-68; slice 5 |
| RF3 The incentive | Whatever Q-71 decides, within 8.12.4 | §5 | Q-71 |

---

## 9. Journeys proposed

| Journey | Tests | Must reach | Slice |
|---|---|---|---|
| P4-J01 A referral creates nothing but a count | A member refers a household to a club; the club sees one more "awaiting" and no name; the Federation sees a count; no message leaves the platform | meets | RF1 |
| P4-J02 The invitation is the person's door | The referred adult opens the invitation, verifies a channel, consents; the contact exists; the club's "referral received" follow-up opens with the club's assignee; a club without the option switched on sees the contact in the secretary's queue instead | meets | RF1 |
| P4-J03 The referrer sees "received" and no more | After consent, after the call, after a join: the referrer's view is unchanged unless the referred person turned on "tell the referrer" | meets | RF1 |
| P4-J04 Withdrawal closes everything | The referred adult withdraws consent; the follow-up closes, the contact closes, the referral row stays with no name; the club cannot reopen it | meets | RF1 |
| P4-J05 No membership from a referral | The club's desk offers no "make member"; the join wizard is the only door; a join naming the club lands in the secretary's queue as any join (P20-A1) | meets | RF1 |
| P4-J06 A minor refuses by name | A referral naming only a child refuses citing R6 and R7; a household referral names its adult | meets | RF1 |
| P4-J07 From the tree, nothing is taken | The referral form opened from the member's own branch carries no name or channel from the file; the contact has no node link | meets | RF1 |
| P4-J08 The platform sends nothing until told it may | A request to message the referred channel before Q-68 refuses citing D36 | guarded until Q-68 | RF1 |
| P4-J09 No club, no referral | A referral to "no club" refuses by name until D5's at-large roll exists | guarded until D5 | RF1 |

---

## 10. What changes in the site's data with this note

`workflows.yaml`: `club-management` gains the referral as a step on the secretary's desk and this note as a source; `join-renew-dues` gains the referral as a way a join is reached, with the rule that it creates no membership. `experiences.yaml`: `member` gains "refer a family"; `club-officer` the "referral received" option and the awaiting count; `federation-staff` the referral counts. `questions.yaml`: Q-68–Q-72 for governance to number. The crosswalk: row D7 to "Designed" pointing here; the P4 row marked written. `plan/MASTER-PLAN.md`: rows RF1–RF3.
