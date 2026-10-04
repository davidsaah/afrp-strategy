# AFRP delivery status — 5 September 2026

## Where the project stands, in one paragraph
**The design layer is complete and the build has started.** The mockups-only hold was lifted on
**4 September 2026**; ADR-001 records the stack, and sixteen Django modules now stand in
`davidsaah/AFRP-Hub` with **485 tests green on PostgreSQL under the production settings**. Six of
the seven items on the build handoff's "what remains" are done — payments, the by-laws layer, the
member lens, the fixture, deployability and reporting. **Item 2, the family tree, is blocked**: its
design record is not on the build machine, and the identity substrate the rest of the platform
queries is not something to invent. Everything below the build section still describes the design layer
and remains current. See **The build** for what has been written, and **What is actually left**,
which is unchanged: the build is not waiting on any of it.

## Where the design layer stands
**The design layer is complete.** Every element on the Platform Map is designed — no Missing rows
remain — and the core flows are **working in-browser simulations** rather than static screens.
Thirteen adversarial red-team rounds have attacked the design; the breaks confirmed in rounds 1–2
settled into **seven platform principles (S1–S7)**. Rounds 7 onward changed character: they stopped
finding screen defects and started finding defects in **code, data and our own claims** — a
fabricated by-law citation, step-parents walked as blood ancestors, a fabricated table row, a
statistic pointed at the wrong population, and three mutually inconsistent clan censuses on one
tab. Two headline findings have been **withdrawn on the screen** rather than in a footnote. The Board has approved **full digital voting**; the bylaw amendment awaits
convention ratification and everything is labelled honestly meanwhile. **All six blocking
decisions were answered on 20 August 2026, though Decision 5 was reopened on 21 August as recorded
in error** — see `AFRP-Decisions-Register.md`. What remains is not
decision-making: one CPA countersignature, five governing documents that have never been produced,
one unset parameter, and a **four-amendment package** for the convention floor. The build hold
("mockups-only") was **lifted on 4 September 2026**.

## The organising principle — THE RAILS
Everything below is downstream of `claude/AFRP-Program-Architecture.md`, which is the canonical
statement of **the Rails**: the four progression pathways a person can travel (youth pipeline,
advocacy, heritage, Palestine-direct), the **seven-station shared shape** every program takes, and
the **six platform services** each program draws on. Programs hand off to one another along the
rails; the Convention convenes them annually and the clubs convene them continuously. If a new
surface cannot be placed on a rail, that is the signal to stop and ask why it exists.

## Live and verified
**https://davidsaah.github.io/afrp-mockups/** — the design hub (Pages from `main /docs`);
28 documents. Route count, verification figures and red-team totals in this document are computed, not remembered.

### The reference layer
- `AFRP-Complete-Platform.html` — the definitive reference: nine sections, every module,
  S1–S7, the entity map, the round-3 register.
- `AFRP-Platform-Map.html` v1.1 — module cards + element matrix; **no Missing rows remain**.
- `AFRP-Platform-Experience.html` v1.1 — 16 red-teamed journeys + the integrated progression
  (Pathways) + the breaks register for rounds 1–2.
- `AFRP-Programs.html` v2.0 — 19 programs in six sections, each with a full charter, built from
  real afrp.org content.
- Convention, Community & Life Events, Institutions, Ruleset Workbench, Unified Member/Operations v3.1.

### The deep dives (new, 20 Aug) — each surface treated whole, every moment paired
Each document shows every moment twice — **the person running it beside the person living it** —
because the gap between those two views is where the design has failed under attack. 117 paired
moments in total.
- `AFRP-Deep-Convention.html` — **four dimensions**: the year-long timeline (bid → handoff, with
  the governance calendar and the room block), nine roles walked separately, hour by hour on-site
  (including the election, the memorial service and the wifi outage), and the money & contract
  lifecycle.
- `AFRP-Deep-Programs.html` — one shared shape (now seven stations), a representative program
  walked in each of the six sections, the rest tabulated against the same template.
- `AFRP-Deep-Club-Activities.html` — a club's year: meetings, hafli season, youth, holidays,
  fundraisers, the convention delegation — and the **condolence surface**, handled with care.
- `AFRP-Deep-Club-Management.html` — the officer year, the treasurer's month, the membership
  secretary's queue, migration, and the states nobody designs for.
- `AFRP-Deep-Federation.html` — five queues with owners and clocks, the board year, four
  institutions administered without being merged, and the appeals path.

### The prototype
`prototype.html` — **60 routes across five lenses** (Front door, Member, Club, Program,
Federation), vanilla JS, works on a phone. It began at 99. Thirty-nine routes have been
retired **without losing a screen**: the duplicates were one object seen from different
chairs, so they were folded into tabbed surfaces that carry every original panel verbatim.

| Merged surface | From | Tabs |
|---|---|---|
| `convention` | 8 routes | operations · command · on the ground · desk & store · attending · live · help · store |
| `money` | 7 routes | multi-entity ledger · daily close · controls · QuickBooks · programme budget · disbursement · club remittance |
| `institutions` | 4 | registry · one institution · ARFHSN · charter a fifth |
| `people` | 3 | member 360 · identity & merge · support desk |
| `directory` | 3 | directory · as a member sees it · your household's inclusion |
| `governance` | 3 | board & officers · committees · workspace |
| `clubs` | 3 | the eighteen · health & integration · onboarding & migration |

Earlier in the same pass, `fed/lifeevents` folded into the family-tree queue (release became
a **step on an item** rather than a second queue), `member/lifeevent` into `member/family`,
and `program/conflicts` into `program/applications`.

### The family tree — the identity substrate
Not a feature bolted on; the graph the rest of the platform asks questions of.
- **28,226 people, 10,399 families** imported from the record keeper's GEDCOM. The parser
  **round-trips the 5.5MB file byte-identically** — md5 `7c37ec49bbd5faf1247076ccb87a6bc6`,
  321,312 lines, 0 unparsed — proven, not asserted, and independently reproduced.
- **Kinship engine** on the real graph: lowest common ancestor, civil-law degree, blood
  links only. **98% of random member pairs are related**, which is what makes a naive
  conflict-of-interest rule useless and turns the threshold into a Board decision with a
  measured cost (4° flags 0.4% of pairs, 6° 1.4%, 8° 5.5%, 10° 14.6%, 12° 26.1%).
- **Hourglass viewer** with draft branches, bundle submission and pending nodes drawn in place.
- **Fun Facts from the Book**, recomputed from the master file rather than transcribed:
  **19 of 21 testable tiles and all three computable charts reproduce the printed book
  exactly**, including all ten given names with all ten counts.

### Shaheen 1982 — the book By-Law 4.1.1 delegates the membership test to
Read on 21 August from AFRP's own Drive folder, where it had been sitting all along.
Full record: **`claude/AFRP-Shaheen-1982-Eligibility-Source.md`**.
- The founder structure from **p. 22**, read from the page image because the OCR of the
  two-column pages interleaves them into nonsense. **Eight clans in two groups** — El Hadadeh
  and El Hamayel — stated three separate times in the book.
- **The Azzouz question, closed.** 'Azzouz was one of Haddad's five sons and headed a clan; the
  clan merged into Jaghab after the killings on p. 33. So AFRP's roster is right that Azzouz is a
  family under Jaghab, and the database is right to give the line its own reference series. But
  the database **never re-coded the merger**: of 3,303 people with a Jaghab reference, exactly one
  is surnamed Azzouz. Three sources, three time horizons, none of them wrong.
- **Chapter 2, "Outsiders Who Settled in Ramallah"** — four sentences attach six families to three
  clans, verified from the page images of pp. 25–26. This raises a live governance question with
  **two defensible readings**, and the platform puts both to the Membership Committee and the Legal
  Advisor rather than choosing.
- **The 1944 ration-card clan census** against the record: mean difference in share **0.80 points**
  across eight clans; Hassaan 4.1% then, 4.1% now.
- **The marry-out rule, measured where it applies.** A daughter's line is recorded as continuing
  86.8% of the time if her husband is also in a line and **34.9%** if he is not — against 91.2% and
  81.1% for sons. 2,243 daughters; about 1,164 lines that stop. Computed at build time from the
  28,226-person file, not typed in.
- **The by-law's test cannot be automated and is not.** Absence from Shaheen is why By-Law 4.2.1
  exists.

### Restricted funds — where the money goes
An event that takes money must name a **purpose**; a purpose belongs to an entity; only that
entity may authorise raising in its name; the money reaches that entity's restricted account;
and spend releases the restriction. Publishing is gated on three rules and the refusal names
each one. Four contributor notices run the lifecycle, ending with the restriction released
*because the money was spent on the thing it was given for*.

## The working simulations (all in-memory; nothing stored or charged)
1. **Join** — four paths: individual end-to-end, newlywed family (+minor), $0 student, and the
   unhappy paths (typo attack, expired code, declined household). Verified-channel-first (S1).
2. **Sign-in & recovery** — passwordless and **existence-blind** (identical screen for a real and
   a nonsense channel), sessions revoke, the 72-hour undo, the 7-day both-channels-lost path with
   a "try to rush it" refusal naming its rule.
3. **Digital voting** — eligibility gated with the rule named → secret ballot → seal → one-time
   inclusion receipt → results; plus **M-3, a live weighted floor vote** where opening the vote
   visibly freezes the extraction controls (S4) and closing it reopens them.
4. **Renewal** — rejoin the Detroit Club and the standing engine reacts everywhere (the ballot
   reopens under 4.3.1); then simulate a post-remittance chargeback and watch S3 create a
   receivable, revert standing with an effective date, and leave frozen rolls annotated.
5. **My Pathway + inbox** — the four program rails walkable; milestones fire program-invitation
   notices into a working inbox; accepting is a dated enrollment, declining is recorded nowhere
   a committee can see; handoffs chain (RBPN → mentor).
6. **The event builder** — a six-step wizard on both the club and program lenses; cross-listing;
   co-host split agreements (publish **refuses** without one, naming the rule); two live examples:
   the $100/person Christmas party (household signup, S3 cancel) and a free lecture (RSVP,
   waitlist, ask-a-question with per-field attribution consent).
7. **Institution management** — a registry of the four entities plus a charter-a-fifth wizard, a
   nine-tab record per entity, and a **live bylaws adoption**: adopt afrp-bylaws-2024.1 and the
   governed-by chip and live rules move, while the frozen 971-member roll does not.

## Governance posture
- **Digital voting is the Board-approved direction** for elections, referenda and the convention
  floor. Labelled "amendment ratification pending" everywhere; the mailed CPA ballot is designed
  in full and labelled the **transitional channel** until ratification.
- `afrp-bylaws-2012.2` in force; `afrp-bylaws-2024.1` ratified but **not yet governing**.
- **Override register is per entity-lineage: 18 AFRP-2024 · 22 ARFECF-2013 · 8 ARFHSN-2017 —
  48 across the federation.** (Correction: earlier notes attributed all 48 to AFRP's 2024 text.
  Ruleset IDs are now entity-prefixed to prevent that collision recurring.)
- The ruleset stamp binds to a **process at its first freeze**; every later gate in that process
  runs under the text it began in. No mixed-ruleset election; frozen snapshots are never recomputed.
- The two 9.1.3 amendment drafts (weights fix at opening; at-large roll) remain for the floor.

## Red-team record
| Round | Target | Agents | Attacks | Confirmed | Reconciliations |
|---|---|---|---|---|---|
| 1 | 12 journeys | 90 | 72 | 16 → S1–S6 | — |
| 2 | J13–J16 + Pathways | 67 | 30 | 3 → **S7** | 15 |
| 3 | 9 new elements (front door, mailed ballot, boardroom, inbox, desk, migration, endowment, ARFHSN) | 67 | 30 | 0 | 16 |
| 4 | Event builder | 28 | 12 | 0 | 15 |
| 5 | Institution management | 41 | 18 | 0 | 16 |
| 6 | The five deep dives | 41 | 18 | 0 | 16 |
| 7 | Six flagship programs | 13 | 18 | 1 | ladder drift reconciled |
| 8 | Family-tree integration | 13 | 18 | 1 | efficiency sweep — 5 rebuilds |
| 9 | Kinship engine & round-trip | 9 | 12 | 3 | + independent data audit |
| 10 | Restricted funds | 9 | 12 | 8 | conduit, purpose-as-routing-key, ticket revenue |
| 11 | Shaheen 1982, round 1 | 2 | 6 | 9 | quotation, circularity, page numbers |
| 12 | Shaheen 1982, round 2 | 2 | 6 | 11 | the statistic, the attachment reading, Kaddoura |
| 13 | Shaheen 1982, round 3 | 2 | 6 | 13 | three clan censuses, Azzouz coding, build order |
| — | **The nine-module build** — first round against shipping application code, frozen at `73976ba` | 7 lenses + verifiers | 7 lenses | **35** (3 refuted) | the receipt hash that *was* the voter↔ballot join; vote content leaking by ciphertext length; the relay bypassing the directory gate |
| — | **That fix layer** | 6 lanes | 6 lanes | **10** (0 refuted) | three of the five worst were regressions the round's own fixes had introduced |
| 14 | **Payments slice** — first round against code that moves money | 2 + 1 fix-layer audit | 2 lanes | **22 + 11** | the 12/1970 vault expiry, the double-charged renewal, duplicate-as-decline |
| 15 | **By-laws layer** | 1 | 9 claims | **19** | ratification from a dropdown, the franchise check failing open, a spelling variant dropping the 4.1.1 question |
| | **Total** | **429+** | **287+** | **162+** | **94+** |

**Two corrections to this table, made 5 September 2026.** The payments
fix-layer audit found **11**, not the 4 previously recorded here — the commit
(`da44b5a`) and the twenty tests in `payments/tests_fixaudit.py` are the
authority. And the two **unnumbered** rows are rounds that ran against the
nine-module build: they were recorded in their commits (`379ab0d`, `fc44eba`)
and never entered in this table, which is why the numbering jumps from design
round 13 to "round 14, payments". Renumbering now would falsify references
already written into pushed commit messages, so they are carried unnumbered.
Their agent counts were not recorded at the time — hence `429+`.

Round 14 is the first against **shipping application code that moves money**, and it behaved like
rounds 7–9 rather than 1–6: nothing it found was a screen defect. Two of the three worst — a vaulted
card stored with a 1970 expiry so no member could ever pay, and a duplicate-transaction answer
booked as a decline so a member is charged and told they were not — were **invisible from every
test in the suite**, because the suite's own fixtures asserted the shape the code expected rather
than the shape the processor returns. The lesson generalises past this slice: *a test written from
the same misreading as the code confirms the misreading.*

Rounds 7–9 were the first to find defects in **code and data** rather than in screens: a
fabricated by-law citation, step-parents walked as blood ancestors (12.3% of the file), a
non-deterministic common-ancestor pick, understated clan counts, a dead search box, and book
entries duplicated across two consoles that had already drifted apart.

**A method note, because the number lies.** Rounds 11–13 ran as one background workflow of 63
agents: six breakers, then an adversarial verify pass instructed to default to *refuted*. It
returned **57 findings and 0 confirmed** — and that headline is worthless. I was editing the
prototype while the verify pass was running, so 57 of 57 refutations reduce to "the defect
describes a state that no longer exists"; several say outright that the reviewer's reading of the
book was correct. The findings were real and every one of them was fixed. The lesson is the
method's, not the finding's: **do not mutate the target while the verify pass is in flight.**
Freeze the artifact, or verify against the commit the breakers read. Confirmed counts in the table
above are my own verification of each finding against the primary sources, not the workflow's.

**Rounds 11–13 attacked our own claims**, and this is the class that matters most. A “10 of 10”
corroboration table contained a **fabricated row** whose value could only have come from the
document it claimed to be testing, and the check as a whole **had no power to fail**. A statistic
offered as evidence for a rule about daughters was measuring women who married *in*. The clans tab
carried **three different headcounts of the same clans**, one of them larger than the number of
people the file has placed. None of this was visible from the screen; all of it came from
re-reading the source and re-running the query.

Notable settlements from the later rounds: **complementary suppression (S7)** after an award-stage
subtraction attack; a **third club integration door** (platform-native, post-cutover);
**board-confidential as a sixth exact-grant permission**; the ruleset stamp binding to the
**process at its first freeze** (so an election cannot be counted under two texts);
**convention money is federation money at the first dollar** with the Convention Contract's agency
treatment scoped to off-platform receipts; club money split by **collection channel, not occasion**;
a **bereavement notice type** inside the operational class; and By-Law 6.3.1 attendance scoped to
**conventions and Mid-Year meetings only**.

## The six decisions — all answered 20 August 2026
Full record, with adopted wording and consequences: **`claude/AFRP-Decisions-Register.md`**.

| # | Decision | Answer | What remains |
|---|---|---|---|
| 1 | Club-collected AFRP dues | **Agency** — AFRP's money at the first dollar; clubs hold in trust, never book as revenue | CPA countersignature |
| 2 | Endowment Fund entity | **ARFECF** | Endowment Fund Policy Statement |
| 3 | Scholarship's legal home | **ARFECF** — same entity as the endowment, so no money crosses an entity line | Conforming amendment (no AFRP by-law constitutes a Scholarship Committee) |
| 4 | Digital voting | **Approved as the direction** — settled, not reopened | Calendar the 9.2 ratification |
| 5 | The two 9.1.3 drafts | ⚠ **REOPENED 21 Aug** — recorded in error; “the option for both” meant a *member’s* two options under 9.1.3, not two amendments | Needs an answer |
| 6 | Dormant-club prepaid dues | **Stay valid for the remainder of the membership year** | The directory grace parameter — 90 days proposed |

**Consequences worth carrying forward.** Decision 1 makes standing begin at **collection, not
remittance**, so a slow-remitting club cannot disenfranchise its members; unremitted collections are
an AFRP receivable and reversals run against AFRP under S3. Decisions 2 and 3 put both funds in one
entity, which removes the inter-entity agreement burden but makes the **4% floor vs 5% cap** conflict
govern both funds instead of one. Decision 6 pairs with Decision 5: a member whose club stays dormant
past year end lands on the **at-large roll** that Decision 5 is building. The Ramallah Foundation
remains a **partner** — agreements and contacts, no governance surfaces.

## The conforming-amendment package
Four amendments, best put as a package because three touch Article IX:

1. **By-Law 9.2** — digital voting *(Decision 4)*.
2. **By-Law 9.1.3** — weights fix when voting opens, closing the mid-count weight shift *(S4, Decision 5)*.
3. **By-Law 9.1.3** — the at-large roll *(Decision 5)*.
4. **Scholarship Committee** — constitute it and write down the cross-entity election *(Decision 3)*.

All four are 2/3 delegate-vote matters under 16.1.1 and 9.1.1(3) — so 9.1.3's weighted fractional
voting applies to the amendments that fix 9.1.3. Submissions are due 60 days before the General
Assembly; the Constitutional Committee's review distributes 45 days before.

## The build — `davidsaah/AFRP-Hub` (private)

The mockups-only hold was lifted **4 September 2026**; `docs/ADR-001-build-foundation.md` records
the stack, hosting, sign-in and repository decisions. Sixteen Django modules now stand: `core`,
`accounts`, `join`, `memberdir`, `dues`, `clubs`, `voting`, `programs`, `events`, `funds`, `camp`,
`network`, `payments`, `bylaws`, `member`, `reporting`.

### 5 September 2026 — CI made honest, and payments wired

**CI had been red on every push, and the recorded "234 tests green" was true only in a dev shell.**
Two defects, both real:
- `cryptography` is imported by `voting/crypto.py` (X25519 + ChaCha20-Poly1305 sealing, the Shamir
  split) and was never added to `requirements.txt`. Any environment that did not already happen to
  have it — CI, and every future deploy — skipped the **entire voting module** without failing.
- CI sets `DEBUG=0`, which turned on `SECURE_SSL_REDIRECT`, and `SecurityMiddleware` answers 301 to
  the Django test client *before any view runs*. That single cause produced all 22 failures — the
  301s, the `0 != 1` mail counts, the `KeyError: 'city'`, the `'lapsed' != 'current'`; every one of
  them a POST that never reached its view. The suite had never once run under the posture it ships
  with.

Found while fixing the second, not reported by it: `SECURE_SSL_REDIRECT` had no
`SECURE_PROXY_SSL_HEADER` beside it. ADR-001 decision 2 deploys behind a managed PaaS that
terminates TLS at its edge, so Django would have seen every proxied request as plain http and
redirected it forever — **the site would have failed on its first deploy**, at a point where
nothing in the suite could have caught it.

**Payments for real** (item 1 of the build handoff's "what remains"). Authorize.Net behind a
`PaymentGateway` port, a vault and charge ledger, and the four money paths — `join.checkout`,
`dues.renew`, `events`, `funds` — wired through one function. Card data cannot enter the process:
the browser posts to the processor via Accept.js and only an opaque token crosses the boundary,
which is what keeps AFRP in **SAQ A-EP** rather than SAQ D. Widening that stays a board decision.

### Red-team round 14 — the payments slice

Two adversarial verifiers, refute-first, in two lanes (the PCI boundary and the vendor adapter; the
service layer and the four wired money paths). **22 confirmed, 0 stylistic.** The class that
matters most, again, was **our own claims** — docstrings asserting properties the code did not have:

- **Nobody could ever have paid by card.** `vault()` read a `card` key that Authorize.Net's
  create-profile response does not contain, so every stored card fell back to **12/1970** and was
  then refused as expired *before the network was reached*. Both verifiers found this
  independently. The suite was green because its own test invented the `card` key the API does not
  return — the same shape of error as the fabricated corroboration row in round 11.
- **A double-clicked renewal charged twice and granted two membership years** — $180 for a $90
  renewal, membership through 2028. The key was built from a `uuid4` *and* from `paid_through`,
  which the first renewal moves; the dedup it appeared to provide did not exist.
- **The processor saying "I already took this money" was booked as a decline** (responseCode 3 /
  errorCode 11) — the member charged and told their card had failed. So was a *held-for-review*
  transaction, which may still settle, and so was a successful authCapture whose `responseCode`
  arrived as the integer `1` rather than the string.
- **A read timeout escaped as `TimeoutError`** — not a `URLError`, so neither handler caught it —
  in precisely the case where the money may already have moved. A wrong transaction key (HTTP 401)
  was classified *retryable* and would have been hammered forever instead of alerting anyone.
- **The card-shape guard refused about one legitimate payment in 175.** Shape alone matched a
  `uuid4`-derived key, and because the key is deterministic per intent, every retry failed
  identically: that member could never pay for that thing.
- **A PAN in Arabic-Indic or fullwidth digits passed the guard**, because the check ran on the
  `json.dumps` output, where those digits are escaped to `\uXXXX` and the digit run is broken.
- **Reversing a cash payment posted a real refund to the processor** — either wiring money out for
  cash taken in person, or failing and locking a treasurer out of correcting their own ledger.
  Reversals also went through whatever gateway was configured *now*, not the one holding the money.
- **A stale in-memory `Person` charged a deceased member.** `renew` took the row lock and threw the
  locked row away, then consulted the caller's argument — granting a membership year to an estate.
- **Waitlist promotion charged a member with no card on file**, and the refusal came out of a
  *different* member's cancellation, blocking their refund. Under the simulator it was worse: the
  promoted person was silently recorded as having paid money nobody had asked them for. A promoted
  seat is now **offered**, not sold, and paid for when the person confirms it.
- **Club-collected cash named nobody.** The only real call site passed no collector, so every
  club-collected renewal in the product was an anonymous claim that money exists, with no processor
  record to reconcile against. An offline tender now refuses without one.

**The fix layer then had to be audited, and that found eleven more** — two of them fixes that were
*weaker than what they replaced*. The rewritten card guard dropped **Mastercard's 2-series BINs**
(2221–2720, live worldwide since 2017) and stopped recognising a PAN written with its expiry beside
it, which is how a card is most often actually written down. And one idea that looked obviously
right — *"if this intent already has an approved charge, hand it back"* — produced four: it is true
only while the charge is still money in hand, and only after the request has been validated, and it
was neither. A charged-back member clicking Renew was handed the reversed charge and told
"renewed through next September" while nothing was taken; an event signup cancelled and re-made the
same day was free. Deduplicating the *charge* also turned out not to deduplicate the *renewal* or
the *gift*: the second submit correctly took no money, and then wrote a second membership year and
a second restricted contribution anyway — inflating the balance `funds.spend` authorises against.
That is the round-16 lesson exactly: **a fix batch is not done until its own layer has been
attacked.**

*(This paragraph read "four more" until 5 September 2026. The commit and the twenty tests in
`payments/tests_fixaudit.py` say eleven; the full list is in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`.)*

### 5 September 2026 — the by-laws layer

Item 3 of the build handoff: the corpus as data. `AFRP-Bylaws-Ingestion-Architecture.md`,
`AFRP-ARFECF-ARFHSN-Rulesets.md` and `AFRP-Shaheen-1982-Eligibility-Source.md` are now code.

- **The document registry**, wider than the documents we hold: the four instruments on file plus
  the **five cited as governing that have never been produced**, each as a row naming the citation
  that summoned it. Every rule standing on one carries INCOMPLETE in its own citation string.
- **The canonical text is verbatim and sealed.** "March 31th", "deemed to be have a quorum",
  "reduced to four (2)", the ARFECF "Replace with" redline — all preserved. Corrected readings
  live in the register.
- **All 48 provisional overrides**, 18 + 22 + 8, each naming its gap, citations and rationale. The
  **ratification agenda** orders them by how many decisions have leaned on each, which is the
  clarity the register was asked for: not "the system made assumptions" but "here are the
  sentences the Board should adopt, heaviest first."
- **Three franchises**, so one room on one day does not merge three electorates.
- **By-Law 4.1.1**: the engine returns **UNDETERMINED** for the six contested families, carries
  both readings with their page numbers, and refers to the **Membership Committee and the Legal
  Advisor**. The platform does not choose who is a Regular Member.

### Red-team round 15 — the by-laws layer

**19 confirmed**, and the verifier's summary is the finding worth keeping: they were not nineteen
independent defects but **one architectural fact with nineteen faces**. Every guarantee lived in a
service function, and none lived in the model layer, the database or the admin — so `.update()`,
a plain `.save()`, and above all *the admin forms a registrar actually uses* went straight past
all of it.

- **A ruleset could be set to "Ratified" from an admin dropdown** and would govern the Federation
  with no verification pass, no ratifier and no timestamp. That defeats the claim the module
  exists to make. It is a database constraint now: the row cannot exist.
- **The franchise check failed open.** It compared primary keys, and two unsaved rows both have
  `pk = None`; `None != None` is False, so the one check standing between three legally distinct
  electorates admitted *every* mismatched pair it was handed as unsaved objects — silently, and in
  the permissive direction.
- **A spelling variant rerouted a live membership question away from the Legal Advisor.**
  `'Ajlouny` returned both readings, both pages and the referral; `Ajlouni` returned none of it.
  Both said "undetermined", so the divergence was invisible at the verdict level. That is the
  module's stated failure mode arriving by the back door: not choosing a reading, but quietly
  dropping the question the two readings are about. And `'Awwaad` — *this project's own spelling* —
  was told the book does not name it.
- **A reading the Board had REJECTED was quoted to members exactly like an adopted one**, because
  only PROVISIONAL was badged.
- **Two ratified rulesets both governed**, and which one won was decided by database row order — a
  silent tie-break on the most consequential question the module answers, and the integrity floor
  forbids silent tie-breaks.
- **Four tests could not fail.** The worst asserted that every member of the eight-clan tuple is
  eligible, while the function under test decides by membership in that same tuple. It survived
  putting the wrong spelling in — the exact defect above.

**One finding was answered by withdrawing a claim rather than by writing code**, which is the same
move as the two headline findings withdrawn on the screen in round 13. The docstrings said *"no
override, ratified or otherwise, reaches the integrity floor — not by unanimous vote."* That is a
claim about all overrides. The code made a claim about overrides that *volunteer* the declaration,
via an optional argument that was not even stored. The floor is enforced in the ballot engine,
where those properties live; what this layer can honestly offer is that the declaration is
checked, recorded and auditable. It now says that, and no more.

### 5 September 2026 — the member lens, the fixture, deployability, reporting

Items 4–7 of the build handoff. Item 2, the family tree, is **blocked**:
`AFRP-Family-Tree-Design.md` is not on the build machine, and the identity
substrate the rest of the platform queries is not something to invent.

**The member lens** (`/me/`) — seven of the prototype's sixteen member routes.
Every one behind sign-in, and **no route takes "which member" as a parameter**,
so there is nothing to enumerate and no id to tamper with; that is asserted as
a test over the urlconf rather than left as a convention. The screens show the
states a member can actually be in rather than a rounded summary: standing per
scope, a card about to stop working *before* it does, a seat held rather than
sold, cash an officer took labelled as cash, and a reversal as a reversal.

**One defect found by opening the page, not by the suite.** `$40.00` rendered
as `$4000` and `$1,500.00` as `$150000`, and every `assertContains` passed —
they were substring checks that a wrong number satisfies. This is the same
species as round 14's vault expiry and round 15's eight-clan tuple, in a third
medium: *a test written from the same assumption as the code confirms the
assumption.* It is the argument for running the thing.

**The fixture now reaches nine modules**, not six. From the 500 households:
2,704 charges, 1,838 dues payments, 18 restricted purposes, 190 contributions,
1,201 programme enrolments, 32 events with 357 signups. Nothing is invented —
the fixture says a member paid for a hafli seat at a named club in a named
year, so the event is what that payment implies. It carries no professional
data, camp applications or elections, so `network`, `camp` and `voting` are not
seeded **and the command says so**, because a thin module should never be
mistaken for a broken one.

Three of its refusals are the fixture testing the code rather than the reverse,
all reported rather than swallowed: a **partner cannot own a restricted
purpose** (the Ramallah Foundation hosts gifts in the fixture and
`create_purpose` refuses); **money does not move after a death** (78 payments
skipped); and **the two ledgers part company for the dead** — which surfaced by
crashing the seeder. The charge ledger keeps a since-deceased member's payment,
because it must be able to record a chargeback on their card; the membership
record does not, because a membership row for someone who has died is not a
fact about the past but a claim they are still a member.

**Deployability**, as far as it can honestly go. `whitenoise` was in
`requirements.txt` and not in `MIDDLEWARE` — the app would have come up and
served 404 for every stylesheet, since a managed PaaS has no web server in
front of it. Same family as the missing `SECURE_PROXY_SSL_HEADER`: latent,
invisible in development, fatal on the first deploy. Added a Procfile with a
release phase, a `/healthz` that checks the **database** (gunicorn answers 200
perfectly well with an unreachable one), and `docs/DEPLOYING.md`. The two
irreversible HSTS settings are **opt-in**, because they are about AFRP's DNS
rather than this application. Nothing is deployed: choosing a provider and
pointing DNS is the Board's, and `AUTHORIZE_NET_SANDBOX=0` is the single most
consequential environment variable in the system.

**Federation operations** (`/operations/`) — membership by scope, money by
tender, giving by fund, open items across every module, one call list.
Aggregates by default, minors in no figure, and small cells suppressed **in
pairs**: a row with exactly one suppressed cell suppresses a second, because a
visible total makes the hidden one recoverable by subtraction. That is S7,
reached in an earlier round by an award-stage subtraction attack, applied here
to operations rather than to the directory.

The reports refuse to round three things off: there is **no single "members in
good standing" figure**, because the by-laws do not define one; the **grace
window is labelled a proposal**, because the Board has not set it; and
**reversed money is shown rather than netted away**, because a fund report that
omits it cannot be reconciled against the bank.

The lens was gated on Django's `is_staff` flag, and the refusal text said so.
**The exact-grant model is now built (5–6 September 2026, `access/`)**: a club
officer never satisfying another club, sensitive permissions never inherited,
grants ended never deleted, ex officio grants following their office. The one
decorator it was to land in is `access.services.requires`, and every federation
view names the permission it is. The staff flag opens only the Django admin.

### 5 September 2026 — the method, written down

The application was recoverable from git. **The method that produced it was
not** — it lived in one conversation, and the handoff that set it existed
nowhere on disk: the path it names, `claude/AFRP-Hub-Build-Handoff.md`, is
inside the Claude Project's knowledge, which a build session cannot read. A
fresh session was starting by re-deriving a worse version of the discipline and
repeating defects already paid for.

`AFRP-Hub/ai-memory/` now carries it, and `CLAUDE.md` at the repository root
loads the rules into every session automatically. It is a **boot pack** —
orientation, the nine binding rules each with its enforcement site and locking
test, the four-step discipline, the environment, the conventions, the open
questions — and an **archive**: all 97 confirmed findings against shipping
code, with the fix and the test for each, plus four reusable prompts (build a
slice · red-team it · audit the fix layer · verify one claim).

The handoff itself was **recovered verbatim from the session transcript** and
committed to `ai-memory/sources/`, with its two false statements corrected in a
header rather than in the text: it said to expect 234 tests green at `8a77474`
(they were green in a dev shell; CI was red), and it named five design
documents as source of truth that are not on the machine.

Two corrections to *this* document came out of writing it, both recorded above:
the payments fix-layer audit found **eleven**, not four; and two red-team
rounds against the nine-module build — 35 findings and 10 — had never been
entered in the red-team table at all, which is why its numbering jumps from 13
to 14.

`docs/ARCHITECTURE.md` was added to the Hub for the human-facing version of the
module map, and the README now opens with a pointer to all of it.

## What is actually left
**One signature** — the CPA on the agency treatment.
**Five documents** cited as governing and never produced — Endowment Fund Policy Statement;
Scholarship Fund Policy Statement (2015), which settles 4% vs 5% for both funds; ARFECF's
exempt-status determination letter, now load-bearing for donor receipting on both funds; Board Rules
& Regulations (the dues-ladder authority); a clean ARFECF 2013 copy and the ARFHSN trustee roster.
**One number** — the directory grace parameter.

Board-flagged from the deep dives: **exhibitor/press credentials** are modelled as non-attendee
credentials so the membership-mandatory rule stays absolute — worth confirming rather than leaving
as practice; and **convention deficit responsibility** is read from the Convention Contract, with
the screen saying so where the text is silent.

## Document register — every project doc, certified 20 August 2026
All thirteen project docs were reviewed and refreshed on 20 Aug 2026. Read this column before
trusting any figure in an older paragraph.

| Doc | What it is | State |
|---|---|---|
| `AFRP-Program-Architecture.md` | **THE RAILS** — the organising principle | **Rewritten 20 Aug.** Canonical. Start here. |
| `AFRP-Decisions-Register.md` | **The six decisions** — adopted wording, dates, consequences | **New 20 Aug, corrected 21 Aug.** Decision 5 reopened; 23 further decisions in Part 2. |
| `AFRP-Shaheen-1982-Eligibility-Source.md` | **The book 4.1.1 names** — what it says, what it does not contain, and what we got wrong about it | **New 21 Aug.** Red-teamed three times. |
| `AFRP-Family-Tree-Design.md` | The tree as identity substrate | Current. |
| `AFRP-Delivery-Status.md` | This document — status, decisions, register | **Rewritten 20 Aug.** Current. |
| `AFRP-Transfer-Handoff.md` | Signpost to everything else | **Rewritten 20 Aug.** Retired as a package; useful as an index. |
| `AFRP-Bylaws-Ingestion-Architecture.md` | How texts become rules | **Updated 20 Aug** — lineage states, process-level stamp, 18 clubs. |
| `AFRP-Bylaws-2024-Divergence.md` | AFRP-lineage extraction, 2012 → 2024 | **Refresh block added 20 Aug.** Extraction sound; the region-map "conflict" is withdrawn; 18 AFRP overrides, not 48. |
| `AFRP-ARFECF-ARFHSN-Rulesets.md` | The two sister entities | **Refresh block added 20 Aug.** Extraction sound; this is the doc that verified the phantom rules out. 22 + 8 overrides. |
| `AFRP-Bylaws-Reconciliation.md` | The earliest analysis | **⚠ Correction block added 20 Aug.** It originated the two phantom rules and the 26-club figure. Read the block before the body. |
| `AFRP-Bylaw-Flexibility.md` | Four tiers of what can change | **Updated 20 Aug.** Model intact; phantom rules corrected in place; S4 settled; workbench built. |
| `AFRP-Electronic-Voting.md` | The digital-voting design | **Updated with the Board decision.** Adopted direction; amendment ratification pending. |
| `AFRP-Integrated-Prototype.html` | Prototype snapshot | **Refreshed from the live site 20 Aug.** |
| `AFRP-Unified-Member.html` | Member-side reference | **Refreshed from the live site 20 Aug.** |
| `AFRP-Unified-Operations.html` | Operations-side reference | **Refreshed from the live site 20 Aug.** |

**Corrections that supersede older text wherever it still appears:** 18 chapter clubs (not 26);
48 overrides across **three** lineages (18/22/8), not 48 against AFRP-2024; entity-prefixed ruleset
IDs; the ARFECF region map and 4-member interlock cap do not exist in the operative text and are
carried visibly INACTIVE; By-Law 6.3.1 attendance is scoped to conventions and Mid-Year meetings
only.

## Standing constraints
- ~~**Mockups-only / build on hold**~~ — **lifted 4 September 2026.** The recorded plan was
  followed: ADR-001 in AFRP-Portal, then the join slice first as the best-specified piece.
- Demo people and money are fictional; programs, the real 18 clubs, committees and by-law
  citations are real and sourced.
- Public repo quotes operative by-law text plainly; deliberation stays in AFRP-Portal (private).
- Push workflow: Claude builds in the cloud workspace → writes to David's laptop via the device
  bridge → David pushes from `C:\Users\David\Projects\afrp-mockups` → Claude verifies
  byte-for-byte against origin/main and confirms the Pages redeploy.

## Backlog
1. ~~**Board packet**~~ — **built 21 Aug** (`AFRP-Board-Packet.html`): the six decisions, six
   missing documents, four unpublished facts.
2. Scholarship history discovery Phase 1 (time-critical, no software needed).
3. Still-missing governing docs: Scholarship Fund Policy Statement 2015, EFund Policy Statement,
   Board Rules & Regulations (dues-ladder authority), clean ARFECF copy, ARFHSN trustee roster.
4. Teen-stage successor programme (registry "proposed" row).
5. **Read the Arabic section of Shaheen 1982** — the genealogies themselves, still unread; and
   `1982_Shahin_family_index.json`, which maps 105 Arabic family names to page numbers and would
   let the platform answer *"is this family in the book, and on what page"* — the literal text of
   By-Law 4.1.1 — instead of inferring it from the GEDCOM.
6. **The scholarship committee workflow from aggregates only.** Offered, not started. Counts,
   trends and timing; no applicant name leaves that Drive folder.

### 5 September 2026 — the member lens and the club lens, on the design system

Phase 2 of the build plan (member lens) is complete except the household
authority model, which is refused: R6 is inferred, stated by no document.
Ported or built onto the prototype's design system: home, membership &
household, payments & giving, programmes, club, professional network,
events, the ballot (choose / confirm / sealed, receipt once), directory &
disclosure, the inbox (invitations answered for real) and the pathway (four
rails over the programme register). Phase 3a–b: club dashboard, roster,
consent-filtered communications with the withheld stored by name, and
officers & affiliation (the filing recorded; the form's content is not
specified and not held).

One defect in core from this round, now fixed and locked: a consent
withdrawal recorded in the same instant as the grant it replaced could be
read as the grant (`latest_consent` ordered by time alone). Hub commit
range a300728–0fad931 and after; 581+ tests.

### 6 September 2026 — overnight: the federation lens, the registry, the admin, the September fixture

Phase 4a–c: the federation dashboard, directory at scale, the election
console (certify / open / close / count under split custody), and the
registry — clubs, programmes, officer terms, events, people, entities —
with one rule: delete tells the truth. The Django admin hardened to the
same rules. The seeder reads the September fixture from `afrp-mockups/
docs/fixture/`: dated consents, exact payment dates, jobs, asks and offers,
a camp season, all through the services. Red-team round 17 found seven
defects in the night's work, all fixed with tests. Questions for David are
in `AFRP-Hub/docs/QUESTIONS-FOR-DAVID.md`. 723 tests.

### 6 September 2026 — before dawn: the federation lens finished as far as the record allows

Phase 4d–i, in order: the live voting floor (exact fractions, S4 freeze, the
two-thirds bar shown without ruling); the ruleset workbench (the truth that
no ruleset is ratified for any entity, verification and ratification
recorded with a person and a date, the 48-override agenda, rule-by-rule
divergence with the cost tiers of AFRP-Bylaw-Flexibility §1); roles &
permissions (`src/access/policy.ts` ported verbatim — the exact-grant model
R39 now gates every federation view; the staff flag opens only the admin);
People (`src/identity/resolve.ts` ported — Member 360, the merge queue as a
certification gate, a merge that closes the loser and never deletes it);
the communications centre at federation scope (one consent filter, two
scopes); and money (`src/ledger/posting.ts` and `remittance.ts` ported —
the daily close with fees gross, the remittance run as a statement, payout
refused until the CPA's agency answer and the sign-off policy are on file).

Red-team rounds 18–21 found twelve defects in the night's own work and one
in an older fix (`Ruleset.governs` ignored a future effective date), all
fixed with tests that failed first: a dead person's grants still opened
the lens; a merge during an open election disenfranchised the voter; a
parent and a child on one email could merge, and so could twins; every
club's journal batch slugged to RAMALLAH and two clubs on one day crashed
the close; money a club collected itself was booked as national's and would
have been paid back. Full detail in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`.

Not built, and said so: the board workspace (no design document on disk —
`src/governance/` holds the ballot and eligibility engines, already
ported), the Convention (after the twenty), the ledger's controls,
QuickBooks connection and endowment tabs. Questions 10–21 for David are in
`AFRP-Hub/docs/QUESTIONS-FOR-DAVID.md`; the two the ledger waits on are the
CPA's agency-or-revenue answer in writing and who signs off a remittance
run. Hub commits 1052e06–72abcd3; 806 tests, serial, CI green on each.

## Slice T1a — the branches (7 Sep 2026)

D38-D40 of `AFRP-Family-Tree-Integration.md`, built. `programs/rails.py` is
gone; `programs/branches.py` carries the four branches, re-cut in the same
move: Education (ladder by age), Leadership (ladder by capacity, the order a
suggestion), Heritage (cluster, no next step and no milestone), Care
(destinations, with the Ramallah Foundation and the Endowed Fund shown and not
joinable). The family tree is the roots beneath all four; the Convention is the
junction where they meet. The route `/me/pathway/` is now `/me/branches/`.

Two defects found and fixed, in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`
round 23: three journey specs still walked the removed route, so the corpus
reported a working screen as not built; and a programme on the register that no
branch carried vanished from the screen that walks the register.

A finding about this document's own family: §7 of the Family Tree Integration
note puts the rename at eleven files, but three unrelated senses of "rail" live
in the Hub and only one is D38's. Six files carried D38's sense and changed;
the six shared services of `AFRP-Program-Architecture` §2 and the UI sidebar
rail keep the word, because their own records still use it.

1106 tests green under both postures. Journey corpus: 271 runnable, 173 meet,
43 guarded, 9 open, 40 not built, 6 rated 0 — the same six standing findings as
before the slice (JD-009, JD-010, JF-040, JM-042, JM-050, JM-055).

## Slice T1b — the node and the life events (8 Sep 2026)

D30-D37, built. **JD-009 and JD-010 clear** — the two door rows rated 0 since
slice 1. A 4.1.1 lineage claim is evidence for the Membership Committee and
never a verdict, said on the tree; 4.2.1's Associate route is offered on the
join screen itself.

Every member has a node (1,049 backfilled), it may be unattached and that is a
complete state, and no membership decision reads it — asserted by revoking one
and finding standing, dues, eligibility and the franchise unchanged. Software
never picks the match: the member gets a fresh unattached node at once, the
platform offers candidates, the member proposes, the committee decides, and the
backfill proposes nothing. One audited link per person, revocable with a reason,
never duplicated at the database.

A step or adoptive link stops the lineage walk and says why, so a marriage can
never manufacture a 4.1.1 path. Adoption has no decision and none was invented.
The life-event pipeline queues to the committee with R6 as its gate and the
fan-out offers rather than fires, because dues authority is the Board's under
By-Law 5.1. D35 resolves two disagreeing holders protectively in both write
orders, and a recorded restriction now reaches backwards over a grant already
given.

Four defects found and fixed, one in the slice's own fix layer — round 24 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,174 tests green under both
postures. Journey corpus: 295 runnable, 193 meet, 45 guarded, 13 open, 40 not
built, 4 rated 0 — the standing findings JF-040, JM-042, JM-050 and JM-055.

**Still open and not answered here:** By-Law 4.1.1's three spouse questions (a
same-sex spouse, an unmarried partner, and a membership admitted through a
spouse after a divorce), the club attachment of a minor in two households, and
adoption's own decision. Each is routed to the Membership Committee on the
surface where it arises rather than inferred.

## Slice T1c — the committee and the mailings (8 Sep 2026)

D32, D36 and §6's committee table, built. A third decision state that stays
open and keeps aging; a diff preview before any GEDCOM import applies anything;
an import missing people deleting nobody; a second import from a stale export
refused by name, with what changed since; a committee direct edit audited and
D12 flagging — never revoking — the decisions on the corrected line. Mailings
go to members about their own branch through the consent filter, and the
audience builder cannot express a non-member. The book is organised from the
tree and carries no eligibility force: an assessment cites Shaheen 1982 and
never the platform's edition, and the screen derives that from the citations
rather than asserting it. Clan composition by club is aggregated, adults only,
under the k≥3 floor with the reason printed.

Seven defects found and fixed — three in the slice's own fix layer, two in the
journey runner — round 25 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. The
one that matters most: after any import, every member's node link still
pointed at the superseded version, so their own branch read an old tree and
their person page 404ed. 1,226 tests green under both postures. Journey
corpus: 311 runnable, 206 meet, 48 guarded, 13 open, 40 not built, 4 rated 0 —
the standing findings, unchanged.

Adoption still has no decision; the link is recorded as non-lineage and
nothing is inferred from it.

## Slice 4 — the scholarship committee engine (8 Sep 2026)

Built from AFRP-Scholarship-Program-Spec.md and AFRP-ARFECF-ARFHSN-Rulesets.md
with Decisions 2, 3, 7, 8 and 9. The Hub holds an application's existence,
state, scores and an opaque reference to the committee's packet — never the
packet — and a check walks the schema and the repository at every command to
say so from the running system (JP-069, proven able to fail). Conflicts are
detected by degree over the family tree, the median ranks with the spread
surfaced, the cap is 5% of a recorded valuation under 6.4.3 with the 2015
Policy Statement's figures shown unsourced and inactive, and encumbrance is
computed in whole cents. The Fund boundaries refuse by name: a designated
officer cannot stand in for the Scholarship Fund Committee (6.4.4), money never
moves between the Funds (6.3.8 / 6.4.8), Decision 7 cannot reach ARFECF, award
receipts are ARFECF's. Two rows route OPEN by design — the floor-versus-cap
question and the cross-entity election of a committee no AFRP by-law
constitutes. A sixth cited-but-missing instrument is now on the registry:
ARFECF's exempt-status determination letter, load-bearing for receipting.

5 defects found and fixed — round 26 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,323 tests green under both
postures. Journey corpus: 320 runnable, 214 meet, 50 guarded, 15 open,
37 not built, 4 rated 0 — the standing findings, unchanged.

Still the committee's to set, not the platform's: the rubric (spec §11 q.2)
and the conflict bar (§11 q.3, three degrees as the register's parameter).
Still David's: the Policy Statement, the determination letter.
\n
## Slice 4b — get staging back, then the four corrections (8 Sep 2026)

Staging had been down since 8 Sep 00:23 across twenty deploys and eight
slices while CI stayed green: the boot chain's last link refused correctly —
a grant ended by exec order is never re-granted from the environment — and
exited non-zero ahead of gunicorn. The refusal is kept; its exit code is not:
release work may refuse and may not prevent the site from serving. The chain
is named once and the blueprint is tested against it; the audited break-glass
is the way back from a lockout; a slice is not done until the deploy is live
on the pushed commit, and this one was — Part 1 on `10496d5`, the whole on
deploy (id pending: the Render workspace was not confirmed in-session, so the deploy is verified from outside — `/healthz` answering `ok` on the pushed commit — and its id is recorded in the follow-up line below) (`this commit`).

David's four corrections of 8 September, built: the award budget is the
committee's entered figure (source, as-of date; warn, never block; no code
computes 5% of anything; EC-OV-6 superseded by decision); the three-degree bar
is out and every relationship is disclosed by degree and acknowledged on the
record, only same household refusing; refusals keep their refusal — the
general override mechanism deliberately not built, the non-overridable list
written and asserted; dev moves to PostgreSQL with a check that refuses the
two shapes SQLite let past. The report of record is one artifact in two
shapes.

4 defects found and fixed — round 27 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,356 tests green under both
postures. Journey corpus: 320 runnable, 214 meet, 50 guarded, 15 open,
37 not built, 4 rated 0 — the standing findings, unchanged.

### Slice 4c — the boot, properly (8 September 2026)

`seed_bylaws`'s guard now expresses its invariant — born provisional, out of
that state only through a recorded transition naming what moved it — and no
longer refuses the register's own correct state; every release step is in
exactly one classification and a test provokes each step's real failure
against its list; `render.yaml`'s single-instance claim is corrected from the
deploy logs (a stale instance of the previous release ran its chain during the
overlap); a two-character reason can no longer end a grant; the break-glass
was rehearsed end to end on a database in staging's shape, and its run on
staging is the operator's; the staging database's 5 October expiry is on the
open-questions register with what is lost and what a boot rebuilds.

6 defects found and fixed, plus one in the fix layer — round 28 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,362 tests green under both
postures. Journey corpus: 320 runnable, 214 meet, 50 guarded, 15 open,
37 not built, 4 rated 0 — the standing findings, unchanged.

### Slice 6 — J4: the programme corpus, and the four branches end to end (8 September 2026)

The last 54 catalogue rows — all programme lens — are authored and run: every
catalogue row is now runnable. The eighteen named programmes are each reachable
from the programme lens; the platform-level rows hold with their figures staged
(suppression composes across tabs, the three stage conversions computed from
staged data, a cohort's names behind roster:read at that programme, a small
programme's rung counts under the floor); the four branches walk end to end
with each shape asserted as a shape, JM-104's absence proven able to fail, the
roots beneath all four and the Convention on none, the two funds without a join
affordance. JP-067 flips: first-year and veteran camp retention are two
figures, never one. Five rows that claimed `completes` over nothing built are
corrected to `not-built`; one persona that could never be refused is replaced.
The break-glass can no longer cut its own audit string.

6 defects found and fixed, two catalogue corrections and one fix-layer note —
round 29 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,376 tests green
under both postures. Journey corpus: 374 runnable, 246 meet, 52 guarded, 16
open, 56 not built, 4 rated 0 — the standing findings, unchanged.

### Slice 7 — magazine operations (9 September 2026)

Hathihe Ramallah is built as the record describes it: the issue on its dated
rail; five auto sections generated from the live system at the copy freeze
with no manual entry path — refused at the model, the admin, the desk and the
command, and a test tries all four; proof and confirm where approving confirms
the record and silence still publishes; a death held until the named family
contact approves, refused by name to an officer holding everything; the
statutory notice clock computed from the register's period, the last
qualifying issue refusing to close while a notice is missing; the magazine's
own authority, which no federation grant confers; the archive searched by
family name through the directory gate; the ads desk with the paid state
modelled and the platform payment path refusing, naming what is undecided.
The nine magazine rows land — six complete, three refuse by name — and the
open questions (cadence, back issues, five sections or six, 6.5.2's period,
Manar) are on the register, not decided.

5 defects found and fixed and one set of questions routed open — round 30 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,408 tests green under both
postures. Journey corpus: 374 runnable, 250 meet, 57 guarded, 16
open, 47 not built, 4 rated 0 — the standing findings, unchanged.

### Slice P1 — programme plans & strategy (13 September 2026)

On David's direction — afrp.org the source of truth — every programme on the
register carries its plan and strategy on the record's own shape: the eight
headings of the Program Experience record's Part 4 and the strategy layer of
the Program Architecture (stage and shape, the six rails, whose books and
what money with the record's "confirm" flags carried rather than resolved,
the handoffs resolved to programmes, the conversion that is the budget
argument). Texts on file, one per programme, every section naming its
afrp.org page and fetch date or the record document; a section without a
source refuses the seed. Six at full depth, thirteen visibly thin — the
Bookstore's and the Summit's say under every heading that the site has no
page and the record is silent. The four money treatments Part 4 names are
found defined nowhere and said so; the site and the register disagree on
four age bands and on the Award, which the register retired and afrp.org
still offers, and each plan says which source says what. A committee's
revision is attributed and survives the re-seed; the reviewer at one
programme is refused another's plan by name; rule 1 holds against a site
that names its coordinators.

7 defects found and fixed and two in the fix layer — round 31 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,440 tests green under both
postures. Journey corpus: 377 runnable, 254 meet, 58 guarded, 16
open, 45 not built, 4 rated 0 — the standing findings, unchanged.

### Slice P2 — the commentary comes off the screens (14 September 2026)

David, on the Federation dashboard in the preview: the footers explaining
why each panel is shaped as it is were build-time guidance, not officer
information. Every explanatory line on the templates was inventoried (616
across 121 files) and given a verdict: a rule citation, a refusal naming its
rule or a state line stays; design rationale goes; a line carrying both is
cut to the citation. 32 stripped, 54 rewritten, 530 kept, the inventory
committed under `docs/audits/`. Three stale claims found on the way (three
member screens still said the authority model was not built). Nineteen
journey rows and nine tests had been asserting the commentary rather than
the behaviour and were re-pointed.

4 defects found and fixed and two in the fix layer — round 32 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,440 tests green under both
postures. Journey corpus: 377 runnable, 254 meet, 58 guarded, 16 open, 45
not built, 4 rated 0 — the standing findings, unchanged.

### Slice B1 — Breeze parity 1: club groups, follow-ups, the acting roster, the roll-up (14 September 2026)

From `AFRP-Breeze-Club-Parity.md`, written the same day from breezechms.com,
its API reference and eight support articles and set against everything the
Hub holds. Breeze's tags are the club's own groups — folders, a leader on
the roster or none, members added by name or from a ticked roster, a group
as a mailing audience through the same consent filter, ended never deleted.
Breeze's Follow Ups are the club's follow-ups — options the club defines,
tasks about a person assigned to an officer, due, completed with one note,
a desk of mine, all, overdue and done; a lapse raises one only where the
club switched it on, and the follow-up names the switch. The roster filters
by group and acts on the ticked set. The member sees their own groups on
their own record and no other member. The Federation's club registry rolls
up groups, people in groups and follow-ups per club, every count of people
under the floor, never a name. B2 (events, attendance, check-in), B3 (club
giving), B4 (the Breeze import), B5 (texting) and B6 (forms) are queued,
three of them gated on David's answers, recorded in the crosswalk's §5.

4 defects found and fixed and two in the fix layer — round 33 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,451 tests green under both
postures. Journey corpus: 382 runnable, 258 meet, 59 guarded, 16
open, 45 not built, 4 rated 0 — the standing findings, unchanged.

### Slice B2 — Breeze parity 2: the club's events, the door, attendance (14 September 2026)

From `AFRP-Breeze-Club-Parity.md` §3. A club creates and publishes its own
events from its lens — free until B3 gives a club its own purposes — a
series of up to twelve at a time, weekly or monthly, open to a group of the
club or the whole roster. The door checks the signed-up in, takes a walk-up
from the eligible only and never adds anyone to the roster, records
attendance afterwards, and voids with a reason rather than deleting. A
minor leaves only with a standing holder or a person the R6 release list
names — a holder's collection logged as their exercise, a restriction
beating the list, never a printed code. "Missed the last N" is a report an
officer reads and acts on by name: a follow-up per absentee through an
option the club defined, each naming the rule, never doubled. A
`club_checkin` role opens the door and nothing else. The member sees their
own attendance as a record, never a score. The Federation's registry adds
events, check-ins and people per club, under the floor. Volunteer roles and
quantities per event are B2b, not built.

5 defects found and fixed and two in the fix layer — round 34 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,461 tests green under both
postures. Journey corpus: 387 runnable, 262 meet, 60 guarded, 16 open, 45 not built, 4 rated 0 — the standing findings, unchanged.

### Slice 7b — the magazine review: two corrections, four answers, five confirmations (14 September 2026)

The review of slice 7's ten decisions, applied. Two corrections: the family
tree highlight is the line the Family Tree Committee accepted most recently
inside the issue's content window — an editorial event, never the surname
with the most deceased, which would have printed the same line in every
issue — absent and saying so when nothing was accepted; and a living name in
it prints only with the person's own print consent and the directory gate
both, since a print run is a new purpose that cannot be withdrawn after the
fact. Four answers from David, 10 September: Manar is a real recognition
tier, on the register attested by David Saah with its date and carried
INCOMPLETE against the Board Rules & Regulations until they are produced,
and the section prints both tiers with the count derived; the
five-versus-six section count is an open register row with both prototype
citations on the screen, the magazine committee's question; the delivery
allowance is a register row with no value, and the activities section
refuses to compute until it is set, naming what is missing and who sets it;
no embargo on the archive, closed with its reasoning. From the record: the
three print consents on the member's disclosure screen, each off until
turned on and dated, never inferred; consent read when the freeze fires,
proven as a sequence. Five decisions confirmed and not reopened.

7 defects found and fixed and two in the fix layer — round 35 in
`AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,476 tests green under both
postures. Journey corpus: 391 runnable, 266 meet, 60 guarded, 16 open, 45 not built, 4 rated 0 — the standing findings, unchanged.

### Slice 8 — J5: the corpus attacked, then made to block (14 September 2026)

The journey corpus gates CI. A committed baseline holds every row's class;
the build is red on a regression — a row that drops class, a rise nobody
recorded, a new row landing anything but not-built with no baseline row, or
a fifth rated-0 row — and never red for the rows honestly not built. The
gate refuses a run whose provenance is not CI, PostgreSQL and the commit
under test, naming what it saw. Three binding rules were broken on a scratch
branch and run against the whole suite and the whole corpus, the verdicts
recorded separately in round 36; the gate itself was attacked with a drop,
a rise, a new row, a fifth rated-0 row, a vanished row, a laptop's stamp and
a stale commit, each made to fail once; and CI was proven both ways on
pushed commits — red on a planted regression naming the row and both its
classes, green on the revert.

Round 36 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,490 tests green
under both postures. Journey corpus: 393 runnable, 267 meet, 61 guarded, 16 open, 45 not built, 4 rated 0 — the standing findings, now the accepted baseline.

### Slice D1 — the blockers David moved (14 September 2026)

David annotated the plan's §1d in the chat and each answer is recorded as his
attestation before it is applied. The CPA's countersignature on Decision 1 is
not required: remittance approval completes on a named officer and the CPA's
answer informs each club's treatment. The grace parameter works: the 90-day
window is attested on the register over the seeded proposal, the screens
print the register's own words, and a lapsed member's directory visibility
runs on it as the record always said. The five documents never produced
inform and do not block: every refusal that rested on one now names the
figure or decision actually missing, while a receipt's exempt-status claim
still waits on the determination letter because that is a fact, not a rule.
Credentials stay on hold. Two of the four standing rated-0 rows rose with
these answers, and the baseline moved with them in the same commit.

Round 37 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,494 tests green
under both postures. Journey corpus: 393 runnable, 269 meet, 61 guarded, 16 open, 45 not built, 2 rated 0 — two standing findings remain.

### Slice R1 — the record audit (14 September 2026)

The Cowork audit of 10 September applied, and a new category for the ledger:
defects in the record rather than the code. The agent-facing module map had
frozen at sixteen apps and named none of `magazine`, `scholarship`,
`authority`, `tree` or `access`; it is rebuilt for all twenty-eight with what
each owns, refuses and where to enter, and the architecture doc changed with
it. The session log's preamble no longer carries a count; the test count
lives in two places that a test verifies against the suite itself, so a
slice that forgets the record is red on the pushed commit. The environment
note now says what is true about which run is the run of record. How a sync
conflict copy arrives is written down. The public build board's figures are
brought to today's report and dated.

Round 38 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,500 tests green
under both postures. Journey corpus untouched: 393 runnable, 269 meet, 61 guarded, 16 open, 45 not built, 2 rated 0.

### Slice H1 — one today: the date convention sweep (14 September 2026)

`TIME_ZONE` is America/New_York, the services took today from New York's date
and the views from UTC's, which between 8 pm and midnight Eastern is tomorrow.
The first night CI ran in that window it found two tests (round 38.7) and then
turned the journeys gate red on a renewal dated tomorrow. Swept: 100 sites in
57 files, every date from the clock now `timezone.localdate()`. Seven
defects in the product, the first of them a binding-rule boundary — the
directory served a seventeen-year-old's row the night before their eighteenth
birthday, because the gate's adult cutoff was computed on tomorrow's date; the
camp window closed four hours early; the year's giving report was empty on New
Year's Eve; a club's platform collection at 8 pm fell outside the run that
closed the day. Four locking tests pin the clock to ten in the evening Eastern
and were red before the sweep; a hygiene test refuses the wrong-clock forms in
every first-party Python file, tests included.

Round 39 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,507 tests green
under both postures. Journey corpus: 393 runnable, 269 meet, 61 guarded, 16 open, 45 not built, 2 rated 0 — the baseline untouched.

### Slice 4d — the release chain moves to preDeploy (18 September 2026)

The release chain — migrations, the nine seeds, the first officer — runs in
Render's pre-deploy phase now: once per deploy, after the build and before
traffic switches. Boot is gunicorn alone. Until now the chain ran on every
instance start, so a restart replayed it and a member arriving during one
waited most of a minute, and a step that failed took the site down rather
than the deploy; now an integrity failure fails the deploy and the previous
release keeps serving, while a governance refusal still reports and lets the
deploy proceed. The blueprint, the release module, `CLAUDE.md` and the
deploying guide are held to each other by tests, and the switch window is
written down: a migration is additive, a destructive change is two releases.

Round 40 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,508 tests green
under both postures. Journey corpus: 393 runnable, 269 meet, 61 guarded, 16 open, 45 not built, 2 rated 0 — the baseline untouched.

### Slice H2 — one date format (18 September 2026)

Every date a person reads is now formatted in one place: `1 Oct 2026`, the day
unpadded as the templates print it, and a stored timestamp read in New York
before its day is named. Before this, fifty-nine Python sites printed
"01 Oct 2026" beside rows printing "1 Oct 2026", and twenty-nine stored
timestamps were formatted in UTC — a grant ended at ten in the evening was
reported as ended tomorrow, and the poll window was printed in UTC's clock and
labelled America/New_York. Eighty sites in thirty-two files moved to the
helper; the hygiene scanner refuses the old spellings in every first-party
Python file, tests included; two locking tests were red before the sweep.

Round 41 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,512 tests green
under both postures. Journey corpus: 393 runnable, 269 meet, 61 guarded, 16 open, 45 not built, 2 rated 0 — the baseline untouched.

### Slice 9 — alumni matching: the match queue (18 September 2026)

The first screen of the alumni programme, from the use cases on file: a
historic scholarship recipient — a name and a year in a binder — resolved to
a person on the register through the same matcher the merge queue uses, with
every rule that fired showing. A transliterated name with the same date of
birth lands in the review band; the same name with a different date of birth
is blocked outright, because that is a father and a son; anyone the name
resembles is shown and never picked. Every link records who made it and can
always be undone with both records restored. A deceased alumnus is linked and
marked and never contacted; an alumnus who asks not to be contacted closes
every path, the family-tree path included, and no channel is offered for
them. Nothing links itself. Import, tree tracing, campaigns and the claim
path are later slices; who reviews the queue is the record's own open
question and is on the register.

Round 42 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,526 tests green
under both postures; twenty-nine first-party apps. Journey corpus: 393 runnable, 271 meet, 61 guarded, 16 open, 43 not built, 2 rated 0 — two rows risen from not built.

### Slice 10 — RBPN ops and the job board port (18 September 2026)

The sponsorship desk under the programme lens and the job board on the
public site, both from the network plan and the fixture document. A member
asks for a listing from their own record; the desk verifies membership and
ownership before it exists, refuses under a named line of the exclusion
policy, and records the $150 subscription AFRP received — paying for a
listing on the platform is not decided, and the desk says so rather than
charging. A lapsed listing drops out of the magazine's directory. Every
posting carries its salary range, benefits, pay period, closing date and an
apply path, universally, with the laws named when one is missing; the posting
page is public with complete schema.org markup and applying starts at
sign-in; an expired posting is gone, 410, its markup and apply path with it.
The browser found the fixture seeder publishing postings the fixture holds
back, with their review state as their US state; it is fixed and locked.

Round 43 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,550 tests green
under both postures; twenty-nine first-party apps. Journey corpus: 393 runnable, 273 meet, 63 guarded, 16 open, 39 not built, 2 rated 0 — four rows risen from not built.

### Round 44 — the fix layers of slices 9 and 10, attacked (18 September 2026)

The discipline's own step, run against the frozen build: six defects in the
two fix layers, each reproduced before its fix. The alumni prefilter parted
Kassis from Cassis while claiming to keep transliterations; the alumni queue
printed birth dates in full where the merge queue prints an age; a dead
owner crashed the sponsorship desk; the employer's counts disagreed with the
410; the posting was dated by the machine's clock through Django's own
field option, which the hygiene scanner now refuses; the seeder relabelled
an expired fixture row. Nine mutations against the fixes, all caught.

Round 44 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,561 tests green
under both postures. Journey corpus: 393 runnable, 273 meet, 63 guarded, 16 open, 39 not built, 2 rated 0 — the baseline untouched.

### Slice R2 — the record audit's second pass (18 September 2026)

Three defects in the record, none in the code: the module map's per-app test
counts had drifted and are now derived by the suite for every row; the
architecture document still described a release phase that slice 4d had
replaced with the pre-deploy chain, and a test now holds it to the chain;
the README's hand-kept route counts are gone. The clock sweep that followed
round 44's finding found no second entry point, and round 44's own fixes
held against seven attacks.

Round 45 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,572 tests green
under both postures. Journey corpus unchanged: 393 runnable, 273 meet, 63 guarded, 16 open, 39 not built, 2 rated 0.

### Slice 10b — LinkedIn's real limits on the surface (18 September 2026)

The corpus's accepted rated-0 row that was not a Board question: the network
plan decided to show LinkedIn's real limit on screen, and the member's
network page never did. One sentence now, named once and printed on the
member's page and beneath the posting page's share link; the row rises from
0 to 5 and the baseline moves with it. The other rated-0 row, JM-042, stays
by the register's own decision until the Board answers the suspension
question (Q-10).

Round 46 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,573 tests green
under both postures. Journey corpus: 393 runnable, 274 meet, 63 guarded, 16 open, 39 not built, 1 rated 0 — one row risen from 0.

### Slice A1 — the abstraction pass (30 September 2026)

Four of the six concepts the review found the platform implementing four to
six times each, each collapsed to one primitive with its callers migrated
and a rule that keeps a new module from writing the fault again: deciding
from the database at the moment of decision (`core.decision`, thirteen rule
sites including standing and the living guard), the register's refusal as a
value that names who may set an unset parameter (and the scholarship's
encumbrance warning found silencing itself), one small-cell floor, and every
count the record states derived by the suite. The snapshot and the refusal
object are deferred to A2 with reasons. The plan and the evaluation strategy
were pushed first, and the round reports against them.

Round 47 in `AFRP-Hub/ai-memory/04-FINDINGS-LEDGER.md`. 1,595 tests green
under both postures. Journey corpus unchanged: 393 runnable, 274 meet, 63 guarded, 16 open, 39 not built, 1 rated 0.

### Site S1 — the site becomes the staging area (30 September 2026)

`plan/SITE-OVERHAUL-PLAN.md` approved and recorded as D43–D52. The site is now
generated from `site/` by `site/build.py`: a new home page on the four
branches; **AFRP Strategy** (the Federation's current strategy, eight goals,
building on the CRM, the crosswalk); **Evolution** (timeline, what's next, twenty
open questions with Q-numbers); **Branches & programmes** (four branch pages and
nineteen programme pages); **People** (twelve); **Workflows** (sixteen, with the
hand-offs and the six shared services); **Prototype** (tours by branch and by
person); **Development status** (replacing Design Status, which now redirects);
and the **Library**, with the eight archive pages moved under it behind
redirects. Every count is computed from its source; `site/check.py` checks links,
privacy (D50) and framing, and the `site` workflow fails if `docs/` is stale.
The crosswalk's programme rows F2, F4, F5 and F7 were corrected to the build.
Not done: re-framing `prototype.html` onto the branches (D48) and the design
record's old "rails" wording (plan Phase 7).

### Site S2 — the family tree joins Heritage (30 September 2026)

D53 recorded: the tree moves from the roots beneath the four branches onto the
Heritage branch; every member keeps a node on it (D30). The site was rebuilt on
that frame (home diagram, Heritage page, the tree's programme page, timeline,
questions). AFRP-Hub follows in slice T1d.

### Site S3 — corrections from the intake of the Federation's working files (1 October 2026)

Four sources read through the intake process (ARFHSN, ARFECF, the Federation's own folder, the officer archive, about 900 documents; the full reports are private). Applied here, corrections only: the 2015-revised ARFECF by-laws and the two fund policy statements found and extracted (`design/bylaws/ARFECF-2015-and-the-fund-policies.md`); EC-OV-1 superseded; D2 marked challenged and D3 annotated; Q-2 updated and Q-21 to Q-39 added; programme holding entities corrected pending Q-27; the master plan's blockers updated with the restatement gate; the governing texts listed on the documents page; a by-law status notice on the Status page. The proposals (new workflows, programme rewrites, a "One Federation" crosswalk section, history entries) wait for the project owner's review.

### Site S4 — fourteen decisions from the question walk-through (1 October 2026)

The project owner went through the open questions one by one. D54 (the intake process) and D55–D67 are recorded in the Decisions Register: programme holding entities follow the approved budget (D55); ARFHSN receipts the gifts it holds (D56); one club-share statement (D57); D3 amended so the Ramallah Foundation may hold Scholarship Committee seats once the 2015 policy is amended (D58); the host agreement as the convention rule (D59); non-members may buy an Arabic class (D60); historical records per programme, with no minor's medical, consent or travel document ever stored in the platform (D61); the Medical Mission is ARFHSN's (D62); Care grants: vote with a ceiling, two signatories, safeguarding, the six-monthly report (D63); AFRPWorks on Leadership (D64); AFRP alone carries advocacy (D65); the shared drive is the archive of record (D66); a year-one outcome baseline (D67). Twenty-two questions closed; seventeen stay open, Q-33 (the restatement) and Q-35 (the endowment, after the 4 November boards) among them. The questions page now keeps answered questions under their numbers. AFRPWorks joins the programme register. The Hub follows in the slices the master plan lists.

### Site S5 — the programmes, the workflows and the strategy brought up to the intakes (1 October 2026)

The proposals held from the four intakes and the review applied as one pass (D54). Programmes: all twenty entries corrected from the Federation's and the affiliates' records, with eight new fields on each (what runs today outside the Hub, the entity's evidence, the clubs' part, partner agreements, where records live, sensitive data, what the committee decided, and use cases by lens); the Relief Fund added as a programme. Workflows: six found in the records written up (Care grants, partner agreements, selection programmes, the Arabic term, advocacy, the club share), the Convention's host-agreement and settlement steps, and owner, could-share, module and rule-against-practice on all twenty-two. Strategy: a One Federation section and crosswalk section J, Care rows F13–F17, the design notes P9–P17 queued, the history traced back to 2009, the four folders listed. The generator renders the new fields; the crosswalk parser reads sections A–J. Reviewed (pass with changes, made in the pass); 0 check problems on 90 pages.

### Site S6 — the club experience plan, design note P18 (1 October 2026)

`design/AFRP-Club-Experience-Plan.md` written in fourteen sprints and reviewed (PASS WITH CHANGES, twenty-one findings applied). It joins the two Breeze documents to the intakes' club findings and the 2024 by-law text, and designs: the people of a club (five club-lens entries on the site: president, officer, treasurer, ambassador in a programme, a member seen from the club); the officer year as the `club-management` workflow; a new workflow `club-migration`; the D57 statement (one account per club per holding entity, sixteen line types, a run with a query hold and an immutable close; design note P10 is inside it); club governance clause by clause under the Q-33 gate; the club's seat, line and count in each of the twenty-one programmes; the migration programme club by club; communications and consent; the Federation's clubs page; twenty-four use cases and twenty journeys proposed for the workbench queue; crosswalk rows J9–J12; six Hub slices C1–C6 in the master plan (B4 absorbed into C6); a public page for the Council of Chapter Club Presidents (`strategy/for-clubs.html`); questions Q-40 to Q-47. No decision was taken; D57 and D59 remain the club decisions of October 2026. Build and checks clean: 105 files, 95 pages, 25 open questions, 23 workflows, 15 experiences, 103 crosswalk rows.

### Site S7 — Breeze read in depth (1 October 2026)

About a hundred and ninety support-centre articles, the API reference, the pricing page and the vendor's terms read through the intake process (D54) by three readers; the private report and three card files are in the planning Project. Public changes, reviewed (PASS WITH CHANGES, eleven findings applied): `AFRP-Breeze-Club-Parity.md` §1a, the module-by-module findings and what each changes in the plan; the club plan's B3 shapes, B5 routes, forms answer, migration data rules and cancellation timing; `club-migration`, `communications` and `events` workflows; MASTER-PLAN rows B2b (new), B3, B5 and C6. No decision taken; B3 now has two shapes to choose between, with the CPA under Q-3.

### Site S8 — the directory in three formats, design note P19 (1 October 2026)

`design/AFRP-Directory-Formats.md` written on David's request and his three answers (on-platform only; the professional services directory members only; voting status as the seat's vote under the by-laws): the members' directory with membership and club identified at Federation and club scale, the professional services directory, and the leadership directory of seats, each against what slices D1, 7b and 10 built. The `directory-consent` workflow carries the three formats and moves to Partly built; the member, club officer and committee lenses name them; crosswalk D4 updated and P19 added; MASTER-PLAN rows DIR1–DIR3; questions Q-48 ("near me") and Q-49 (community contacts). No decision taken. The strategy pages were brought up to both passes the same day: goals 1 and 2, the timeline, what's-next, the One Federation section, For club presidents, and crosswalk rows J5 and J11.

### Site S9 — the club journeys, design note P20 (1 October 2026)

`design/AFRP-Club-Journeys.md` written on David's request: fifty-two journeys in twelve groups (the roster, households and children, groups, the officer year and seats, events and the door, volunteers, follow-ups, communications, the treasurer's money, reports and the Federation's view, migration, the member's own view), each from what a club officer does in Breeze today (the deep read's cards) to what the same person does on the platform, the rule tested, the refusal expected, the class and the slice. It absorbs the club plan's twenty journeys and is the exit-test corpus for B1, B2, B2b, B3, B5, C1–C6 and DIR1–DIR2 (MASTER-PLAN row CJ); crosswalk P20; what's-next updated. Proposals for the workbench queue, never direct catalogue edits.

*Since 2 October 2026:* seven journeys were added (P20-A7, D6, D7, D8, I7, I8, J4) for the club's part in P21–P25 and the federation research; P20 now holds fifty-nine journeys, seventeen of them guarded by named gates.

### Site S10 — the design record completed and readable on the site (1 October 2026)

On David's request ("write all the outstanding plans from what's-next and make the md readable from the site") the sixteen design notes the crosswalk still listed as proposed were written in one pass — P1 committee workspace and reporting, P2 planning survey, P3 letters and onboarding, P4 family referral, P5 Selection Committee workflow, P6 press, P7 volunteer interests, P8 Mid-Year host bids, P9 fund rules, P11 Care grants and partner agreements, P12 selection programmes and the Arabic term, P13 host agreements, P14 advocacy, P15 incident response and retention, P16 the Executive Director, P17 AFRPWorks — each researched from the record, the intake cards and primary outside sources, then cross-checked against each other (objects defined twice, rules silent in a sibling, slice-id collisions, by-law citations, privacy, reserved decisions) and corrected. Governance numbered what they raised: 126 raised, 108 new questions Q-50 to Q-157 after merging duplicates and attaching the rest to existing questions. The master plan gained seventy-seven slice rows in dependency order; the crosswalk's design-notes table reads Written for all twenty; what's-next rewritten. The site gained a Design notes section rendering every document in `design/` (seventeen older documents the privacy scan flags are listed with a repository link instead). No decision taken; every note stops where a Board or David must act. Build: 145 files; 135 pages; 0 problems.

### Site S11 — the second research round, and design notes P21 to P27 (2 October 2026)

Record only; no decision taken. Five research-and-intake reports (education, leadership, heritage, care, the Federation; private, in the planning Project) read the Federation's own files, mail and public pages and comparable bodies against the record. Applied to the public record as evidence of practice, never as rules (D41): questions Q-158 to Q-237, with findings that only re-asked an existing question added to that row; a dated section of practice-against-record conflicts in the Decisions Register; all programme entries, thirty workflows (seven new; five now Designed by P22–P27) and sixteen experience lenses (the scholar added) brought up to the reports; crosswalk evidence on thirty-five rows and six new rows (D23, F18, G6, H7, H8, I3), with a section setting the committee's Doc against the record. Seven design notes followed the same day: P21 the contact record (`AFRP-Contact-Record.md`, CR1–CR7; its decision is DRAFT under Q-70), P22 Convention operations (`AFRP-Convention-Operations.md`, CV1–CV8), P23 the Relief Fund and Senior Living (`AFRP-Relief-Fund-and-Senior-Living.md`, RL1–RL6), P24 the Magazine and the Bookstore in operation (`AFRP-Magazine-Operations.md`, MG1–MG7), P25 the leadership pipeline in practice (`AFRP-Leadership-Pipeline.md`, YL1–YL6), P26 scholarship awards and renewal (`AFRP-Scholarship-Awards.md`, SA1–SA7) and P27 the family tree in practice (`AFRP-Family-Tree-In-Practice.md`, FT1–FT6). Governance numbered what they raised: twenty-five questions, twenty-four new as Q-238 to Q-261 and one added to Q-204. The master plan gained forty-seven slice rows before SP0, in the notes' dependency order; the crosswalk's design-notes table reads Written for P21 to P27, D23 moves to Designed, and F18 and G6 to Outside · Designed (the home and the amendment are outside; the Federation's part and the template are designed). Citation fixes made in the same pass: the convention-close payment step cites By-Law 11.1.2 and 7.5.1–7.5.2; the club pass-through rule is cited as 11.1.5 (11.1.4 is the no-solicitation clause); the magazine's death hold as R34; the register's Senior Living row as Program Architecture §3; P19's DIR2 row now gives the RBPN, Magazine and Foundation seats their appointing texts (6.6.1, 6.7.1, 6.8.1); the register's conflicts table gains a Q-237 row; the research round's eighteen placeholder journeys take the notes' ids where a note owns them, and the five that no note owns are numbered under P7, P11 and P14 (P7-J13, P7-J14, P11-J19, P11-J20, P14-J16). Nothing in the Hub changes until a slice is taken.

**Added the same day: D68–D74 and P28.** David decided D68 to D74 on the family tree (Decisions Register, Part 5): the plate grammar on every surface (D68, superseding D27), the Hub as the tree's record after a parallel run of 30 to 60 days (D69, superseding D11's staging), members in current national standing propose (D70, confirming D13), the living in full only inside one's own branch (D71, amending D17), committee approval in tiers with clan stewards (D72, amending D14's mitigations), membership and join first (D73), the print pipeline after the January 2027 Mid-Year (D74). The design note P28 (`AFRP-Family-Tree-Module.md`) is written from them, with slices T2-0, T2-R and T2a–T2h before SP0 in the master plan and questions Q-262 to Q-270 (additions to Q-201 and Q-260; Q-258 and Q-259 marked decided by D69 and D70). P27 is amended to follow them: its handover is D69's parallel run, FT4 is folded into T2h and FT6 into T2d. The Family Tree Design and Integration notes carry a dated pointer. Record only; nothing in the Hub changes until T2-R is taken.

**The fold-in, the same evening.** The older documents were brought into step with the round, P21–P28 and D68–D74, record only, with dated pointers ("*Since 2 October 2026:* …") beside every passage that has moved and the text otherwise left as written:
- the Program Architecture: the Senior Award's retirement not shown in any source (Q-163); Senior Living as the Foundation's building, with its capital-campaign machinery marked never operated (P23 §9.7; Q-203); Emerging Leaders without a source (Q-178); the Day of Action's two modes (P25 §5.3); the Bookstore, Cook Book, Convention and Relief Fund rows in the money map;
- the Program Experience and Four-Lens architectures and the Unified spec: the contact record as a cross-cutting object (P21; Q-70) and the scholar's experience (P26);
- the Element Index and the Consolidated Platform Map: P21–P28 with their modules;
- the Multi-Entity Ledger (§9) and the QuickBooks spec (§12): the Federation's books as practice, never as a decision, with D1 and D56 standing. That practice is accounts retitled per entity, three processor accounts, QuickBooks already integrated with the current CRM, the Convention account and "Due to Convention Host City", the Relief Fund as an ARFECF bank account (Q-109), and ARFECF's audit from FY2026;
- the Adviser Brief: "the CPA" as four roles (Q-231), and the questions waiting on the accountants and the Legal Advisor;
- the Rules Register: T2-0's rows for the D71 radius, the D72 tiers and the unset structural-kinds list (Q-264);
- `plan/QUESTIONS-FOR-DAVID.md`: pointers on answers 22 and 31, and the questions in David's own lap;
- MASTER-PLAN §1 and §1d.

**Counts at the close of 2 October 2026:**
- **74 decisions** (D1–D74);
- **270 question ids** (Q-1–Q-270), of which **246 are open** and 24 carry a decision; *since the fold-in cleanup the same evening:* Q-271 and Q-272 added, so **272 ids, 248 open**; *since the review of that work:* Q-273 added, so **273 ids, 249 open**; *since the record's own gaps were numbered (2 October, late):* Q-274 to Q-278 added and JM-042 cited to Q-10, so **278 ids, 254 open**;
- **177 slice rows** in MASTER-PLAN §2, plus the blocked row (B4, now C6, is counted; until the review of 2 October the build's count skipped it and gave 176); *since the record's own gaps were numbered:* the DRAFT record-only row R3 added before SP0, so **178**.

Two Hub-record items for the next build session:
- inventory the `store` module against P24 §8.1 and write its entry here;
- say whether slice 4 built named-award matching (P26 §1.3).

**Added 3 October 2026: D75–D79.** David answered seven questions in the walk-through (Decisions Register, Part 6). Five are decisions: the build-ready slices go first, and LT1 waits on slice 5 only for a send (D75, Q-278 in part; where R3 sits stays open); D71's radius reaches third cousins (D76, Q-272); the plate is the default view and the hourglass stays as an alternative view (D77, Q-270, limiting D68 as applied to D19); magazine and life events is the next tree integration (D78, Q-265 in part; the order of T2g and T2h stays open); the second holder of `tree:moderate` is a committee member the committee seats (D79, Q-262). Two are not decisions and leave their questions open: the hold on slice 5's credentials is kept (Q-276), and the contact record's shape and consent basis go to the Membership Committee and the Legal Advisor (Q-70). MASTER-PLAN §3.2, LT1, T2-R, T2a, T2c, T2f–T2h and SP0, P3 §9's order line, P28 and the Rules Register's tree rows follow them. Record only; nothing in the Hub changes until a slice is taken.

**Added later on 3 October 2026: D80–D83.** David answered four more questions (Decisions Register, Part 6). The hourglass kept by D77 is drawn in the plate grammar (D80, Q-279). P28 §6's list becomes the Rules Register's *Structural kinds* row, which the Family Tree Committee may amend by a dated act (D81, Q-264); P28 §6's proposal and DRAFT-interim labels come off, and T2c's gate is no longer held by Q-264. The Outstanding High School Senior Award was not retired and continues (D82, Q-163); the programme register's status is corrected, YL6 switches on but still waits on the body (Q-164) and a budget line (D55), and Q-20 falls away. AFRP holds the Relief Fund (D83, Q-109 in part), as David's decision for the design record; the deductibility and receipt text waits on the CPA (D9); the books' ARFECF booking is a reconciliation item in the conflicts table; Q-109 stays open on who approves each transfer between the Board's votes and whether D63's closing records apply. P9, P11 §4, P22, P23, P25 §5.1, P28, the `relief-fund` and `ohss-award` programme entries, and MASTER-PLAN §1d, CG5, CV7, RL1, RL3, RL4, YL6, T2a and T2c follow. Record only; nothing in the Hub changes until a slice is taken.

**Counts at the close of 3 October 2026:** **79 decisions** (D1–D79); **279 question ids** (Q-1–Q-279), of which **252 are open** and 27 carry a decision (Q-262, Q-270 and Q-272 newly decided; Q-265 and Q-278 answered in part and still open; Q-279, the hourglass's drawing, raised); **178 slice rows** in MASTER-PLAN §2, unchanged.

**Counts after D80–D83 (3 October 2026):** **83 decisions** (D1–D83); **279 question ids** (Q-1–Q-279), of which **248 are open** and 31 carry a decision (Q-279, Q-264, Q-163 and Q-20 newly decided; Q-109 answered in part by D83 and still open); **178 slice rows** in MASTER-PLAN §2, unchanged.

**Added 4 October 2026: D84.** David answered Q-273 in the walk-through (Decisions Register, Part 7). The scholarship conflict-of-interest rule of his correction of 8 September 2026 (P26 §1.4, §3.2) is recorded in D58's conditional form: every relationship is disclosed by degree and acknowledged, only the same household refuses, and the spec's three-degree block is withdrawn, conditional on the Scholarship Fund Committee adopting it as its conflict policy (ARFECF 6.4.4; 6.4.6 if a rules amendment). No build change: slice 4b applies the rule. One Hub-record item for the next build session: slice 4b's conflict screen labels the rule *pending adoption (D84)* until the committee's act is on file.

**Counts after D84 (4 October 2026):** **84 decisions** (D1–D84); **279 question ids** (Q-1–Q-279), of which **247 are open** and 32 carry a decision (Q-273 newly decided); **178 slice rows** in MASTER-PLAN §2, unchanged.
