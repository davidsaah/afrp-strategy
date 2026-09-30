# AFRP Test Fixture & the four new surfaces — status through 27 Aug 2026

**This doc carries everything after 21 Aug.** `AFRP-Delivery-Status.md` is accurate through
round 13; this document covers the fixture, the wiring, the camp/directory/network build, and
red-team rounds 14–16.

**Commits pending David's push:** seven, `6a47487 → 2992f00`, in `afrp-steps2to15.bundle` with
`push-afrp.ps1` (both delivered in conversation). origin/main still at `6a47487`.

## The fixture — 500 households, deterministic

Seed `19520000`, as-of 2026, no clock. `python3 emit.py` reproduces the file byte-for-byte and
runs **229 assertions**; the file is not written if one fails. 1,572 people (1,536 living),
1,049 members across SF / Detroit / Jacksonville / DC (Shaheen 1982 p.11's four largest
concentrations, all three club-integration doors represented). No synthetic person carries a real
name — given names checked against the 21,677 real (given, surname) GEDCOM pairs. Nothing derives
from the scholarship folder.

Wired into the prototype via `window.FIX` + `FIXQ` (single source for demo counts) with a console
at `#/fed/fixture`. The frozen "Certified 2026 · 971" roll is deliberately NOT wired (R12/R43);
the live figure shows separately. Coverage is stated honestly: organic 339/380 cells (a number
that can fail), fill pass tops every cell to the S7 floor of five.

## The four new surfaces (research → plan → build → red team)

Research: 9 lanes, 309 findings against primary sources (`AFRP-Camp-Directory-Network-Plan.md`
holds the plan and the four findings that changed the design). Built as steps 1–8 on one shared
backbone: field registry with independent indexed/filterable/audience flags; consent split into
display / contact / export; folding search index; brokered contact with in-portal replies; an
export gate that refuses AND logs; the family graph.

- **`fed/memberdir`** — 831 consenting members. Visibility resolves **when the payload is built**:
  a field the viewer may not see is not in the file (3,400+ values withheld at build; contact
  values never ship at all — the payload holds "(email on file)"). Two-tier search: exact matches
  rank above transliteration-folded ones (fold covers kh/gh/ph, q→k, ou/oo→u, ee/ie/y→i, doubled
  letters); alias and former-name fields carry the spellings. The 31 members whose family name
  sits under multiple clans on AFRP's roster carry that ambiguity onto the card. Contact-field
  visibility has a *ceiling* of members — never public.
- **`member/rbpn`** — the profession directory is **free** (349 members, O*NET-SOC taxonomy);
  the $150 subscription became a promoted **business** listing with a Marquette-style exclusion
  policy that demonstrably refuses (one MLM, one financial-solicitation, each naming its
  category). Warm introductions run only on relationships the person already published —
  family, clan, club; never programme membership, never "same household" — brokered only by
  members whose willing-to-help flag is visible AND who consented to contact, ≤3 offers per
  broker. RBPN search shares the directory's fold. LinkedIn's real limits are printed on the
  surface: a share link works; nothing else does; Hivebrite's sync is higher-ed-only.
- **`member/jobs`** — 10 live postings (the honest number for 3,000 members; asks-and-offers
  outnumber them at 25). Public posting page with complete schema.org markup (description,
  PostalAddress, validThrough, employmentType; directApply:false explained on-screen); applying
  is member-only. Salary min+max, benefits, pay period and closing date **required universally**
  — CA 432.3, MN 181.173 and NY 194-b reach the third-party publisher, which this board is. The
  form refuses negatives, zero, non-numbers, past dates and "banana", naming the rule each time.
  Expired postings 410 and stop advertising their markup and apply path. EEO block optional
  (EO 11246 revoked Jan 2025; VEVRAA/§503 survive for federal contractors, and the note says so).
- **`program/camp`** — a **selection console**: 76 applicants, 50 seats, ages 13–17. The rule is
  stated as it is: submission order within a largest-remainder club quota (summing to exactly 50)
  and a four-per-family cap — the shape rules bound first-come, they do not replace it. Per-club
  odds disclosed. The waitlist reconciles as a story: one family withdraws, the freed seat is
  offered one rank at a time with serialized 72h windows, rank 3 claims it and is seated.
  **Ratios are per-band, because the authorities do not share bands**: ACA publishes 9–14 (1:8)
  and 15–18 (1:10), Michigan 13–17 (1:12); a cabin is governed by the strictest row that reaches
  anyone sleeping in it, so a cabin holding a 13-year-old is a 1:8 cabin. Screening blocks on the
  check AND on credential expiry compared against the session's last day as a date. The CIT is
  three legal beings and sits in the screening table as structurally unscreenable; the **paid CIT
  is an employee whose parents cannot see the record**. Cabins are single-sex and ship as
  counts-and-bands — never a minor's person-id. Camperships: two instruments, capped pots, $250
  minimum award, no tax returns held; all rows render with the rationing evidence first. No
  camper named; ages banded; reasons stripped of serial numbers; k≥3 including the reason text.

## Red-team record, rounds 14–16

| Round | Target (frozen at) | Agents | Raised | Confirmed |
|---|---|---|---|---|
| 14 | fixture wired into prototype (`d3a8b6d`) | 175 | 56 | 25 |
| 15 | the four new surfaces (`9f71b68`) | 230 | 74 | 56, + 11 real from the split pile |
| 16 | **the round-15 fix layer itself** (`3fbb765`) | 109 | 53 | 46 (spot re-check: 27 of 28 real, 1 false) |

**Round 14 headlines:** the dead voted (23 deceased on the certified roll driving 9.1.3 delegate
weight); the coverage claim was a tautology; 189 one-sided marriages incl. a one-year-old; the
prototype *enforced* a fabricated ARFECF interlock citation; the Board denominator made a carried
motion show FAILED. All fixed at the root.

**Round 15 headlines:** the R7 guard was an allowlist and shipped **98 minors by full name** in an
array it had never heard of — it now walks the entire payload. **Withholding a name is not
anonymity**: 25 of 76 camp applications were unique on (age, club, first-timer, aid). Consent now
means consent everywhere. Facet chips counted a different population than the list returned. The
job form validated 3 of its claimed 7 fields via truthiness. RBPN's Board seat was cited to 6.6.1
with an MAL-only restriction attached — it is 6.2.2.

**Round 16 — the audit of the fixes, and it was deserved.** The narrow question: did the round-15
fixes fix, and what did they break. The honest answer: I had fixed the headliners and the commit
implied the set was handled — about half of round 15's 56 confirmed findings were never touched;
the same allowlist error the R7 guard made, made at the level of the work itself. The fix layer
had also introduced defects: k-suppression fed the quota bars so one screen disagreed with its own
totals; the comms fix wired one row of a four-row subtraction; the R7 walk matched name strings
while 49 minors shipped as cabin id-lists; 'club quota 3/19' serials made 45 of 64 published camp
rows unique through the k-check. All 46 remediated in `2992f00`, plus the invented ACA 13–17
ratio band that two "fix" commits had sailed past. One confirmed finding was false on re-run
(the past-dated live postings) — which is why every finding is re-verified by hand before a fix.

**Method, settled:** freeze the snapshot (md5-verified) before the attack; adversarial verifiers
defaulting to *refuted*; per-lens synthesis budgets; every confirmed finding re-verified by hand
before any fix; and after any fix batch, an audit round against the fix layer itself.

## Test surface

229 fixture assertions · 23 browser suites green (rt16test 37, rt15btest 15, rt15test 31,
camptest 35, jobtest 28, rbtest 22, dirtest 23, fixwiretest 29, rtfixtest 25, moneytest 13, plus
the 13 pre-existing suites) · on every payload build: the R7 whole-payload walk (names AND minor
person-ids), the k≥3 check including reason text, and complementary suppression on facets and
structures (a lone hidden cell takes the smallest visible cell with it).

## Open

- **Push**: seven commits waiting on David (`push-afrp.ps1`; bundle filename unchanged).
- Round 16's 7 split findings (1-of-2) unactioned — mostly assertion-strength critiques (several
  emit.py checks recompute the generator's own line and cannot fail) and the 66% of RBPN cards
  with no intro path.
- Camp facts unpublished: real capacity, criteria, fee, committee; governing state; ACA intent;
  the LinkedIn Page admin seat.
- Backlog unchanged from `AFRP-Delivery-Status.md` (scholarship aggregates workflow, Arabic
  section of Shaheen, missing governing docs).
