# Questions for David

Every place the design record was silent and a slice needed an answer.
Where I proceeded, the choice is named so it can be overturned. David
answered 1–10 and 12–21 on 6 September 2026; each answer is recorded here
verbatim in substance, with what it changed or scheduled.

## Open

**None here.** Q11 (extracting the 2012 by-law text into rules) moved to
`ai-memory/08-OPEN-QUESTIONS.md` on 8 September 2026, because that file is in
`CLAUDE.md`'s boot pack and this one is not — an open question a build session
never reads is not open, it is lost. *(Since 2 October 2026: numbered Q-274 in `site/data/questions.yaml`.)*

## In David's own lap, 2 October 2026

These are the open questions from the research round and the notes P21–P28 (Q-158 to Q-273), and the record's own unnumbered questions numbered later that day (Q-274 to Q-278), whose owner names David, alone or with others. Each is in `site/data/questions.yaml` with its detail. Q-258 is answered by D69 and is not listed. *Since 4 October 2026:* Q-273 and Q-164 are answered by D84 and D85, Q-265 in full by D86, Q-201 by D87, Q-195 by D89 and Q-178 by D90; none is listed. Q-260 is answered for now by D88 and stays listed. *Since 3 October 2026:* Q-262, Q-270 and Q-272 are answered by D79, D77 and D76 and are no longer listed; Q-278 and Q-265 are answered in part by D75 and D78 and stay listed for what remains. Later the same day Q-279, Q-264 and Q-163 were answered by D80, D81 and D82 and are no longer listed (with D82, Q-20 fell away); D83 answered Q-109 in part (AFRP holds the Relief Fund), and Q-109, whose owner field names the three Boards and the CPA rather than David, stays open on who approves each transfer between the Board's votes and whether D63's closing records apply.

**David alone**
- Q-274 — Should the 2012 by-law text be extracted into rules? (numbered 2 Oct 2026; was Q11 above)
- Q-276 — The email provider and the payment account for slice 5 (numbered 2 Oct 2026; MASTER-PLAN §1d.6; 3 Oct 2026: David keeps the hold for now)
- Q-278 — Where the record-only slice R3 sits (numbered 2 Oct 2026; the rest is answered by D75, 3 Oct 2026: the build-ready slices first, and LT1 waits on slice 5 only for a send)

**David named first**
- Q-275 — Which club moves from Breeze first, and who holds its Breeze account key (with the first club's officers; numbered 2 Oct 2026; gates C6)
- Q-162 — The public site says the Scholarship is managed by the Ramallah Foundation (with the ARFECF Board)
- Q-171 — When the public page carries the non-member rate (with the programme director)
- Q-175 — Are the Leadership Ramallah committee and the Young Leader Committee one body or two? (with the AFRP Board)
- Q-190 — A second archive-and-tree site built by volunteers (with the Preservation committee, the Family Tree committee and the AFRP Board)
- Q-203 — Is Senior Living a Federation programme at all? (with the AFRP and ARFECF Boards)
- Q-205 — A club's gift to the Foundation's home, recognised by signage (with the Council of Chapter Club Presidents)
- Q-208 — Should the Relief Fund be a purpose on the public giving page now? (with the General Treasurer; since D83, 3 Oct 2026, the fund is AFRP's, so under D8 the purpose is for AFRP's Board)
- Q-214 — Who convenes the monthly ARFHSN meeting (with the ARFHSN Board)
- Q-217 — The grants register's states and the earmark shape ARFHSN uses (with the ARFHSN Board)
- Q-218 — The purpose wording of every appeal, as published (with the ARFHSN Board)
- Q-235 — The committee's draft against the record (with the Strategic Planning Committee)
- Q-260 — Serving a drive-held document inside the sign-in boundary (with the Digital Infrastructure Committee and the Executive Director; answered for now by D88, 4 Oct 2026: not served)
- Q-268 — Minors' dates inside one's own branch (with the Family Tree Committee and the Membership Committee)

**David with others named first**
- Q-189 — What consent an oral-history recording needs (the Preservation committee, the Legal Advisor)
- Q-197 — Who owns the bookstore (the AFRP and ARFECF Boards)
- Q-200 — Who approves access to the clan books and the interactive tree, under what test (the AFRP Board, the Family Tree committee)
- Q-216 — A club's closed branch account held by ARFHSN (the ARFHSN Board, the club)
- Q-230 — Is the Breeze roll-out a Federation programme or each club's choice? (the Deputy President, the AFRP Board)
- Q-266 — Arabic-script names on the tree (the Family Tree Committee)

## Answered 6 September 2026

1. **"The active site" — which address?** *Answer:* https://afrp.org/,
   every page and programme, as a source of truth — and the public site
   is to be recreated as the front-facing application, with a CRM the
   admins update through a standard, customisable template.
   *Consequence, as written on 6 Sep:* a new phase on the plan (Phase 6,
   the public site and its CMS), a separate and larger build needing its
   own design document.
   **DELIVERED — 6–7 September 2026, and the phase was never needed.**
   Work began the same night this answer was recorded: the `website` app,
   afrp.org fetched page by page into 33 seeded pages each carrying its
   source URL and fetch date, every line naming a living person stripped
   with a test that greps the seed so a re-fetch cannot let them back in;
   the Executive Committee page rendered from role grants rather than
   seeded names; news and announcements written on the desk; the Website
   desk under `site:edit` giving admins the standard template's variables,
   each edit attributed; then the public design layer — tatreez rule,
   full-bleed hero, programme cards, dark mode. Covered by the corpus:
   **JD-001, JF-063, JF-064, JF-065, JF-093 pass and JF-094 refuses
   correctly.** Four programme pages remain unspecified (JP-022, JP-027,
   JP-035, JP-036) and are already catalogued into slice 6. What is left
   is **launch, not build** — recorded as blocker 8 in
   `docs/MASTER-PLAN.md` §1d.

2. **Real officers on a public site.** *Answer:* enter them by an admin,
   from https://afrp.org/about-us/executive-committee/. *Consequence:*
   nothing is seeded — the no-real-living-person rule holds for fixtures
   and tests. David or another officer enters the Executive Committee on
   the People registry and grants them on the Roles screen; the role
   titles themselves (see 9) are seeded.

3. **"Suspend" a member.** *Answer:* it is about voting. *Consequence:*
   suspension is an eligibility act, not a record act: the person stays
   on the register and their standing is unaffected; what a suspension
   removes is the franchise, for a stated period, under a stated authority.
   Built 6 September 2026 (evening): `voting.Suspension`, read by
   `eligible_people` at the record date; the People registry withholds
   and lifts the vote, and refuses without an authority or a reason.

4. **Delete versus retire.** *Answer:* yes — and a vote set up wrong must
   be deletable as well as retirable, and the same for transactions.
   *Consequence:* an election in draft (nothing certified) can be deleted
   from the console; once a roll is certified it can be **cancelled** with
   a reason, recorded, never deleted. A transaction that moved money is
   **voided by a reversal** naming the error (R24: a reversal is its own
   entry, the ledger is never rewritten); only a charge that never moved
   money — pending or declined — can be deleted. Built this round.

5. **Minors in the admin.** *Answer:* staff and admin see everyone and
   adjust. *Consequence:* as built; R7 stays on payloads only.

   **Also asked:** membership fees and incentive structures (a free
   student year on graduation) soft-coded so an admin can change them.
   *Consequence:* built 6 September 2026 (evening): the dues ladder is
   versioned rows on the Money screen (prospective, with an authority; a
   term keeps the price in force when it was sold), and the incentives
   the platform knows — the free year after a student year, the
   newlywed year — are switched on or off there with an authority. The
   graduation incentive is seeded **off**: David named it as an example,
   and switching it on is a decision with a minute behind it. The first
   schedule row is the prototype's figures, labelled as such; the
   Assembly's real figures replace it with a new row.

6. **The session named.** *Answer:* it is the AFRP-Portal cloud deployment,
   with the mockups repo at https://github.com/davidsaah/afrp-mockups.
   *Consequence:* the mockups repo is on disk and is the prototype every
   slice is cut from; nothing further needed.

7. **Programme hosts.** *Answer:* the record's hosts are right, and host,
   entity and shape must be soft-coded so an admin can change, grow or
   modify a programme. *Consequence:* built 6 September 2026 (evening):
   the programme's record page amends the charter (name, host, template,
   stage, mission, band, flags, metrics) under program:manage at that
   programme, each changed field its own attributed row. The programme
   descriptions from the Drive overview sheets (question 26) can now be
   entered there, one by one.

8. **The seven committees.** *Answer:* yes, under the federation lens.
   *Consequence:* seeded when the governance slice is built (committee
   seats exist on programmes; a federation committee model does not yet).

9. **Executive Committee titles.** *Answer:* for AFRP the site's page is
   authoritative: https://afrp.org/about-us/executive-committee/. The two
   sub-entities have their own. *Consequence:* the role vocabulary becomes
   data an admin edits (see 12), seeded with the site's titles.

10. **Who ratifies a ruleset, and from when.** *Answer:* an admin should be
    able to ratify rulesets from governing documents on the platform; and
    it would be great to upload governing documents and have a language
    model help draft the rulesets, with admin input and the ability to
    modify and delete. *Consequence:* ratification stays as built (a
    person, an authority, a date). Upload-and-draft is scheduled as a
    workbench slice; note that under the register's own rule a rule's
    verbatim quote is never rewritten and a ratified ruleset is never
    deleted — a draft ruleset can be discarded, and that is the "delete".

12. **The roles vocabulary.** *Answer:* work out a consistent logic and
    build something an admin can update. *Consequence:* the role
    vocabulary moves from a frozen table to editable rows — each role a
    name and a list of permissions — seeded from the policy file plus the
    Executive Committee titles and every committee chair; the exact-scope
    permissions remain exact whatever a role carries.

13. **role:grant exact-scope.** *Answer:* not sure; pick the most flexible,
    changeable later. *Consequence:* role:grant held at `entity:afrp` now
    reaches clubs, programmes and elections; the policy keeps the switch
    in one named place so the literal reading can be restored.

14. **Permissions the record does not name.** *Answer:* the Executive
    Committee at a minimum, plus any committee, and all committee chairs.
    *Consequence:* board-confidential is carried by the Executive
    Committee roles and committee chairs in the seeded vocabulary; the
    workbench stays on audit:read.

15. **Staging's first grant.** *Answer:* name the Executive Committee
    staff and allow them access; David Saah is one. *Consequence:* the
    people are real and are entered by an admin (see 2); once entered,
    the roles screen grants them. David's own bootstrap grant exists.

16. **Office implies grant.** *Answer:* sounds good. *Consequence:* built —
    an officer term appointed on the registry carries its club grant for
    the term, ending when the term ends.

17. **No auto-merge.** *Answer:* keep it; and vote results should be
    produced in a human-readable form. *Consequence:* kept. The result
    panel on the election console gets a plain-language sentence beside
    the arithmetic.

18. **What the merge keeps.** *Answer:* no idea; make it consistent with
    the rest. *Consequence:* kept as built — frozen rolls and existing
    one-to-ones stay on the closed record, two accounts refuse.

19. **Meeting notices and consent.** *Answer:* notices go to every member
    by email and are not filtered by consent. *Consequence:* built — a
    notice reaches every verified address; only the marketing-class
    newsletter runs the consent filter.

20. **The ledger's two blocking answers.** *Answer:* for now, give the
    Executive Committee the ability and record who made the decision or
    approval. *Consequence:* built — a remittance run can be approved by a
    holder of ledger:post, recording who; a club's treatment can be
    confirmed with a name. The CPA's answer in writing is still the right
    record to obtain; the screen says so.

21. **The processor's fee.** *Answer:* make it part of the system when the
    real connection exists; let the admin adjust it; use the simulated
    values as defaults for now. *Consequence:* built — a fee schedule
    (percent and fixed cents) the admin edits; a charge with no fee
    reported is booked at the schedule's estimate, marked estimated, and
    the close says how many were estimated.

## Answered 6 September 2026, afternoon — after the five design documents arrived

22. **Decision 17 against rule R7 in the tree.** *Answer:* paid members see
    everything. *Consequence:* recorded as David's decision, scoped to the
    tree: a member in current national standing, signed in, sees every
    person in the tree — living and deceased, minors included — with dates.
    R7 keeps governing directory payloads, which the tree is not; the
    tree's payload is its own class, named as such, and the whole-payload
    walk that refuses directory payloads with minors does not run on it.
    It is one setting (`tree.policy.LIVING_VISIBLE_TO`) and the design doc
    calls it the one setting worth revisiting before launch. Signed out,
    nothing about the living (Decision 28).
    *Since 2 October 2026:* amended by **D71**. A signed-in member sees the living in full only inside their own branch (blood relatives sharing an ancestor no further back than a great-great-grandparent, and their spouses), and outside it a name and a position only. D28 is unchanged. Whether relatives inside one's own branch see minors' dates, as this answer says today, is Q-268.

23. **Where the tree's data lives.** *Answer:* a GEDCOM file, updated with
    the new membership, protected so nobody but the Family Tree Committee
    can reach it. *Consequence:* the file is imported into the platform's
    own tables and stored in private media outside the repository; the
    raw file and its export are reachable only by holders of the
    `family_tree_committee` role; individuals link to member records so
    new members join the tree through the committee's pipeline. The
    format is the Family Tree Maker export David pointed at
    (`Awwad_Clan_20070310.GED`, GEDCOM 5.5, lineage-linked): the module
    reads and writes exactly that shape, and its tests run on a synthetic
    file of the same shape. No real person from the file enters the
    repository, a fixture or a test.

24. **The Program Experience document's blocked source.** *Answer:* David
    will find it. Meanwhile the AFRP Management folders on Google Drive
    are the source: `p_<programme>` folders with an overview sheet
    (mission, committee, outcomes, timeline), minutes, protocols and
    forms. Read for rules and descriptions only; people in them are real.

25. **Camp facts.** *Answer:* the camp folder. *Consequence:* from it —
    ages 13–17, one week in June, applications January–March, capacity
    about 64 campers bounded by the site and volunteers, a committee of
    fourteen with a chairman since 2018, a 2020 SOP ratified by the
    Federation President, ACA standards used as a benchmark without
    formal accreditation, a college-age successor programme in design,
    registration and counsellor applications opening January–February.
    Fee and governing state still not stated in the folder.

27. **One file or one file per clan?** *Answer (6 Sep 2026, night):* one
    file. *Consequence:* as built — one current tree, each import a
    version of it. And: "have a place in the family tree section for an
    admin to approve changes" — the committee console (the queue, the
    sittings, import and export) is now on the federation lens too, as
    "Family tree", for holders of tree:moderate; the platform admin
    carries it.

33. **The public site's look, the bookstore and donations, Past
    Presidents.** *Answers (6 Sep 2026, night):* the platform's look
    stays, then: "add more of the imagery and graphic design including
    the tatreez layout … take the imagery from afrp.org"; the bookstore
    and donations move here for this site; make the Past Presidents
    prototype. *Consequence:* built — a bookstore (catalogue, member
    pricing by standing, orders on a card token, sales in the daily
    close, inventory on the federation lens); a Donate page that gives to
    an authorised purpose from the member's card on file (a visitor signs
    in or joins first: verified channel first, and the receipt lands on
    their record); Past Presidents as rows an admin enters on the Website
    desk — name, years, deceased marker — never seeded; the public site
    redesigned with afrp.org's own imagery and a tatreez motif.

28. **Who is on the Family Tree Committee?** David is. The role
    `family_tree_committee` exists and is granted by name from the Roles
    screen; nobody holds it until an admin grants it. *Needed:* the other
    members' names, entered by an admin, never seeded.

29. **What the committee counts as "documented".** The file carries no
    source records. The module calls a link *documented* when the
    person's own note names a record or a page of Shaheen 1982, and *in
    the file only* otherwise; it does not infer "tradition" from how far
    up the tree a person sits. If the committee has a different rule
    (a list of accepted sources, a page range), the words in
    `tree/services.py:confidence` are the place.

30. **Rules as data.** *Answer (6 Sep 2026, evening):* "Do not hardcode
    rules — have them all soft-coded so they can be updated with new
    by-laws or executive orders." *Consequence:* built — the register of
    rules (`/operations/rules/`), every Tier 1 parameter and Tier 2
    mechanism choice from AFRP-Bylaw-Flexibility §1 as versioned rows, set
    under a citation, a Board minute or an executive order; the engines
    read the register. Four parameters the text leaves silent or
    self-contradicting stay "not set" until the revision speaks:
    the convention accounting deadline (90 vs 120 days), the dues test
    (postmark vs receipt), standing across scopes (4.1.1's two readings),
    and the endowment valuation date.

31. **The Family Tree Committee.** *Answer:* "David Saah for now; [the
    project's lead] later." *Consequence:* the bootstrap command grants roles named in
    `BOOTSTRAP_OFFICER_ROLES` to the first officer on deploy; set to
    `family_tree_committee` on staging. The project's lead is entered on
    the Roles screen by name when David says who.
    *Since 2 October 2026:* **D72** needs two different committee members to apply a structural change. Who holds `tree:moderate` beside David is **Q-262**, and until then a structural item records its first key and waits. Steward appointment is Q-263.
    *Since 3 October 2026:* **D79** answers Q-262: the second holder is a Family Tree Committee member seated by the committee's own act (FT2), chosen over the project's lead (answer 31).

32. **The public site.** *Answer (6 Sep 2026, evening):* "have as much
    from the afrp.org website in the public-facing site." *Consequence:*
    built as a first cut — afrp.org's structure and texts on the
    platform's template, editable on the Website desk. *Still needed
    from David:* (a) the pages that name people — the Executive
    Committee page fills itself from the grants an admin makes; Past
    Presidents is a page an admin writes; news posts are written, never
    seeded; (b) whether the site should look like afrp.org (its colours,
    photographs, fonts) or like the platform — today it is the
    platform's design system; (c) the bookstore and donations links
    still point at my.afrp.org until those modules exist here.

26. **The programmes' descriptions.** *Answer:* the same Drive folder for
    every programme. *Consequence:* the programme charters can be filled
    from the overview sheets (mission, outcomes, timeline) one by one,
    each edit attributed; scheduled with the charter-edit slice.
