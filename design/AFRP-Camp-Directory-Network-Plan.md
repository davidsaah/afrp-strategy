# Camp, Directory, Network — the design plan

**Status:** plan only, nothing built · 26 Aug 2026
**Plan:** https://claude.ai/code/artifact/66775b12-0bc2-482c-bb8a-0017ea7656ad
**Research:** 9 lanes, 309 findings, primary vendor docs / standards bodies / regulators

## Decisions taken

| Question | Decision |
|---|---|
| Camp logins | Parents and staff only. Campers are minors with no account; a CIT gets a limited one. |
| Camp scope | All four: registration/health/cabins/staff, camperships and store, promotion and re-enrolment, the camper→counsellor ladder. |
| Directory browse axes | Name, club, city · interests, languages, volunteering · **family and clan** (added back after initial exclusion) |
| LinkedIn | Design honestly and show the real limit on screen. |
| RBPN model | Profession directory **free** to every consenting member; the $150 listing becomes a **promoted business listing**. |
| Camp health records | Design the **boundary**, not the module. Buy the health record (CampDoc, $4/participant/year). |
| Job board | **Hybrid** — public posting page for Google indexing, member-only applying and referrals. |

## The four findings that change the design

**1 · Camp Ramallah is a selection problem, not an enrolment funnel.** ~50 seats, ages 13–17,
applications Jan–March, stated selection criteria, Federation-member counsellors; 37 campers in
2018 → 50 in 2019. The entire camp-software market solves the opposite problem. The two mature
heritage-camp comparators (Camp Haiastan, Ionian Village) publish no early-bird, referral, sibling
or member-tier pricing at all. **The centrepiece is a selection console and a fairness record**, not
a registration funnel.

**2 · A paid CIT is legally an employee, and that flips parent visibility off.** Paying participant,
unpaid volunteer and paid junior counsellor are three different legal beings. Employment-law
confidentiality restricts disclosure to outside parties "including parents and guardians". And
ACA's background-check standard starts at 18, so a 16-year-old CIT is structurally unscreenable —
the control has to be supervision rules in the roster (never counted in ratios, never alone with
minors), not a screening record.

**3 · LinkedIn will not do any of it.** No read API for jobs at any tier. The Job Posting API is
"not accepting new partnerships". Sign In returns eight fields, none professional. "Open to Work"
has no API field. Hivebrite's LinkedIn profile sync is *higher-education only*. Buying from a broker
violates the terms AFRP itself would sign; hiQ lost, paid $500k and deleted its data; Proxycurl was
shut down at $10M ARR. **A share-to-LinkedIn link works. That is the complete list.**

**4 · On a job board the salary range is AFRP's legal obligation, not the employer's.** California
Labor Code 432.3, Minnesota 181.173 and New York 194-b all reach the **third-party publisher** —
which is what AFRP's board would be. California requires the range in the posting body, not behind
a link. Thresholds differ (NY 4, CA 15, WA 15, MA 25, MN 30) and key off where the work is
performed, so **salary range is a required structured field universally**, with benefits and a
closing date. Open-ended ranges are prohibited in WA and MN.

*Stale requirement to drop:* EO 11246 was revoked in January 2025 and OFCCP ceased enforcement.
EEO blocks are optional template text, never a required field.

## Other constraints worth recording

- **Ratios disagree between authorities; resolve to the strictest.** Ages 6–8 day camp: ACA 1:8, NY
  1:12, TX 1:10, MI 1:10. Encode as a rule set keyed on
  `{authority, age band, day/overnight, activity, awake/asleep}`.
- **ACA standards text is proprietary** and the whole set was renumbered in Nov 2025. Store a
  standard reference as editable data with an edition field, never as shipped copy.
- **FCRA disclosure must be stand-alone** — bundling it into the volunteer application is the
  most-litigated defect in this area (whether unpaid volunteer screening is "employment purposes" is not confirmed — P7 Q-86).
- **California AB 506 binds youth-service organisations**, not just licensed camps. A club running a
  youth programme in CA is in scope with no camp licence.
- **HIPAA and FERPA are red herrings** for a camp. Building to them spends budget on the wrong
  controls.
- **CCPA/CPRA does not apply to non-profits**; the four non-exempting states all have resident
  thresholds AFRP is far below. **GDPR very likely does not bite** — but a European chapter page or
  euro dues brings GDPR *and* an Article 27 representative. Record it as a decision.
- **Erasure does not require recalling printed directories** (ICO) — only amending future editions.
- **No product models consent-to-export.** With 18 club admins that is AFRP's most likely breach.
  The prototype already refuses bulk export; it needs export *logging* to finish the control.
- **No biometrics on minors.** Face-matching photo galleries are sold across this market with no
  documented camp-side disable. Default off, Federation-level kill switch.

## Expectations to set with the Board now

Vendors' own best-case showcase numbers: ~40% of the base ever registers, ~60% of those tick
"willing to help", and a large *university* generates ~500 mentoring relationships a year. Scaled to
AFRP: **~1,200 registered and mentoring relationships in the dozens.** That is success.

Also: **do not build an engagement score.** Weights are set by consensus rather than statistics, the
construct is not directly measurable, and the model must be frozen forever to allow year-over-year
comparison. The evidenced rung ladder is honest; a score would not be.

And: **report first-year and veteran camp retention separately.** Overall retention conflates them
and will mislead. Year-1→2 is the leaky step (85–89%); year-2→3 runs 90–95%.

## The shared backbone

One substrate read by the directory, RBPN, the camp staff directory and the magazine's print
sections:

- **Field definitions** carrying `indexed`, `displayed`, `filterable` and an audience tier —
  independently. Custom fields get the same controls as system fields.
- **The consent store** — display, contact and export as three separate consents, per field, per
  channel, dated and versioned.
- **The search index** — diacritic folding, wildcards, alias and former-name fields, clan folding
  with its known over-merges disclosed.
- **The broker** — contact without disclosure, with replies held inside the portal. (Wild Apricot's
  own docs admit a recipient can just reply from their email client, which defeats it.)
- **The export gate** — refuses, names the rule, and logs who/when/what for.
- **The rate limiter** — profile views per member per day (Harvard caps at 100).
- **The graph** — family, clan, club, cohort. Already built. Powers relatedness search, warm
  introductions and camp selection fairness.

## Build order

1. Extend the fixture (city, profession via O*NET-SOC, languages, interests, willing-to-help,
   open-to-work, camp applications, staff records, job postings) + fix the
   `fieldVisibility.name = false` contradiction
2. The backbone
3. The directory that is actually there
4. RBPN as a layer on it
5. The job board
6. Camp: selection console and roster
7. Camp: staff, screening and the ladder
8. Camp: camperships
9. Red team against a **frozen** snapshot

## Still unknown

- Camp Ramallah's current capacity, selection criteria, fee and committee — four camp facts were
  already on the open-questions list before this.
- Which state's camp regulation governs (changes what the software must refuse).
- Whether AFRP is ACA-accredited or wants to be (sets the ratio floor).
- Who holds the LinkedIn Page admin seat — every developer app must attach to a Page.
- One research lane lost its search budget partway through; IL/NJ/VT/MD/HI/DC pay-transparency law
  is unverified. The universal salary-range field makes this moot for the design, but it needs a
  second pass before the board ships.
