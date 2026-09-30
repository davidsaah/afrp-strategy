# The programs, complete — and how they fit together
### Every program on afrp.org, on the platform, as one lifecycle

**Date:** August 2026
**Sources:** afrp.org live navigation and program pages (verified 16 Aug 2026) · the bylaws corpus · the existing platform design.
**Mode:** design and planning. No buildout.

---

## 0. What the live site says

The Programs menu on afrp.org lists **seventeen entries**. The platform
previously modelled eight. The gap, with what the site says about each:

| Program | On platform? | What the site says |
|---|---|---|
| AFRP Arabic Program | ✅ | — |
| AFRP Day of Action | ✅ | — |
| Medical Mission | ✅ | — |
| Camp Ramallah | ✅ | — |
| **Congressional Outreach** | ❌ → added | Government Affairs Committee; hundreds of congressional office meetings; wins on COGAT travel rules and the Visa Waiver question; State/DHS briefings for members |
| **Educational & Cultural Exchange Mission** | ❌ → added | Since 2015; **850+ graduate students** supported via the Harvard PalTrek partnership; journalists, educators, clergy, political leaders; olive-harvest participation; partner orgs incl. Al Taawon, Bank of Palestine, UPA |
| Hathihe Ramallah Magazine | ✅ (as module) | Listed as a program on the site |
| Leadership Ramallah | ✅ | — |
| **Outstanding High School Senior Award** | ❌ → added | 3.5 GPA minimum; 500-word essay; recommendation + volunteer verification letters; **due 31 May annually**; two 1st prizes ($1,000 Apple gift cards), 2nd and 3rd ($500); **applicant and family must be members in good standing** |
| Project Hope | ✅ | — |
| RBPN | ✅ (as module) | — |
| Ramallah Family Tree | ✅ (as module) | Listed as a program on the site |
| Ramallah Foundation | ✅ (as entity) | Umbrella on the site for the four below |
| **Ramallah Preservation Project** | ❌ → added | Digital archive: photographs, documents, oral histories; convention exhibits; Arab American National Museum collaboration; site currently under maintenance; contributions via preservation@afrp.org |
| Scholarship | ✅ | — |
| **Senior Living Project** | ❌ → added | **$5M capital project**; 30,000 sq ft, 50+ residents; ground broken Oct 2023, cornerstone Jun 2024; the Foundation's largest project since Ramallah Hospital (1965); replaces a 1970s facility |
| Women to Women | ✅ | — |

Plus a separate **Endowed Fund** menu with a four-tier giving ladder: **Young
Adult Giving · Professional Giving · Visionary Giving · Legacy Giving** — a
life-stage structure, not an amount structure, which matters below.

**One reconciliation flag before anything else.** The site groups Scholarship,
Women to Women, Preservation and Senior Living under **"Ramallah Foundation"**.
The bylaws put the Scholarship Fund under **ARFECF** (the 2015 policy statement
is explicit), and recognise Ramallah Foundation, Inc. as a *different* separate
entity (Const. III §3 vs §4). Either the site's grouping is loose, or money is
moving somewhere the bylaws don't describe. **The platform models the entities
as the bylaws define them and tags each program with its owning entity — but
someone should confirm which entity actually operates Women to Women,
Preservation, and the Senior Living campaign.** It decides whose books the
money sits in, whose board approves the budget, and whose 990 reports it.

---

## 1. How they fit together: it's a lifecycle, not a list

Seventeen programs look like a pile. Arranged by the age of the person they
serve, they are a **pipeline that runs from childhood to legacy** — and the
platform's job is to keep a person moving along it without ever re-entering
their data:

```
  child ────────► teen ─────────► student ────────► young adult ──────► professional
  Camp Ramallah   Youth Program    Scholarship       Leadership Ramallah  RBPN
                  HS Senior Award  (+ free student   Exchange Mission     Congressional
                  (family must be   membership)      Arabic Program       Outreach
                   in good standing)                 Young Adult Giving   Professional Giving
                                                                              │
  legacy ◄──────── elder ◄────────────────── service years ◄──────────────────┘
  Legacy Giving    Visionary Giving           Medical Mission · Project Hope
  family tree      Senior Living (donor       Women to Women · Day of Action
  memoriam          or resident)              (any adult, any time)
  oral history
  (Preservation)
```

Each transition is a **handoff the platform can see coming**:

- A **Camp Ramallah** camper ages into the **HS Senior Award** cohort — the
  system knows their birthdate.
- An **Award** applicant is next year's **Scholarship** applicant — same
  transcript habits, same family, and the award already requires the family's
  membership to be in good standing, which is the standing engine's existing
  `standingAt()` check, reused verbatim.
- A **Scholarship** recipient gets the free student membership (existing
  design) and, at graduation, is a **Leadership Ramallah** and **Exchange
  Mission** candidate — and a **Young Adult Giving** prospect.
- An **Exchange Mission** alumnus who has stood in Ramallah is the natural
  recruit for **Congressional Outreach** — the site itself draws this line.
- A professional lands in **RBPN**, gives at the **Professional** tier, serves
  on a **Medical Mission** or **Project Hope**, and twenty years later gives at
  the **Visionary** tier.
- An elder records an **oral history** with **Preservation**, may live in or
  fund **Senior Living**, and gives through **Legacy Giving**. Their memoriam
  runs in the **Magazine**; their line persists in the **family tree**.

**The metric that matters is conversion between stages**, and today nobody can
measure it because each program keeps its own list. On one platform it's one
query: *how many of last decade's campers are members today? How many Award
applicants became Scholarship applicants? How many Exchange alumni joined
Outreach?* Those numbers are the program budget argument, annually, forever.

---

## 2. The six rails every program runs on

The reason one platform beats seventeen lists — each program consumes the same
six services, and each service gets stronger every time a program uses it:

| Rail | What every program takes from it | What it gives back |
|---|---|---|
| **Membership & standing** | Eligibility (Award: family in good standing · Scholarship: qualified members · committee seats: 8.1.2) | Program participation is the top driver of renewal |
| **Family tree** | Identity, kinship, COI checks | Preservation's oral histories and the Award's family links enrich it |
| **Magazine** | Announcements, recognition lists, statutory notices | Award winners, mission reports, campaign milestones — content that writes itself |
| **Events** | Sessions, registration, QR check-in, attendance | Attendance history (feeds 6.3.1-style eligibility everywhere) |
| **Funds & ledger** | A typed budget line per program (see §3) | Clean per-program cost, restricted-gift tracking, 990 lines |
| **Directory & comms** | Cohort rosters, consent-filtered sends | Alumni segments — the recruiting asset |

This is the four-lens thesis applied to programs: **one object model, seventeen
views.** A program is not an app; it is a cohort + a calendar + a budget line +
a story, all of which already exist as platform services.

---

## 3. The money map

Every program tagged with its funding mechanism and owning entity — the two
facts that decide everything operational:

| Program | Entity (per bylaws/site) | Money type |
|---|---|---|
| Camp Ramallah, Arabic, Day of Action, Youth | AFRP | Fee-funded / general fund |
| Leadership Ramallah, Project Hope | AFRP, **EFund-supported** (ARFECF 6.3.1 names them) | Endowment distribution (5% cap, 6.3.3) |
| Congressional Outreach | AFRP (Government Affairs Cmte) | General fund — likely the bylaws' "Internships in Washington" EFund purpose; confirm |
| Exchange Mission | AFRP + partners | Grant/partner-funded (PalTrek et al.) |
| Medical Mission, Women to Women | AFRP / *entity to confirm* | Restricted gifts + conduit (11.1.5 routing through HQ) |
| HS Senior Award | *site: Ramallah Foundation; confirm* | Small fixed awards (~$3,000/yr at current prizes) |
| Scholarship | **ARFECF** | Scholarship Fund, 4%+1% mandatory distribution |
| Preservation | *site: Ramallah Foundation; confirm* | Restricted gifts |
| **Senior Living** | Ramallah Foundation, Inc. | **Capital campaign — $5M goal, its own machinery** (below) |
| Magazine | Independent board (6.7.1) | AFRP-appropriated + subscriptions |
| RBPN | AFRP committee | Listing subscriptions (existing design) |
| Endowed Fund ladder | ARFECF EFund | The four tiers are **prospect segments**, not products — they map exactly to the lifecycle stages in §1 |

**Senior Living is the one program that needs machinery the platform doesn't
have yet: a capital campaign module.** Pledges (multi-year, with reminders),
pledge-vs-cash reporting, naming opportunities, milestone communications
(ground-breaking → cornerstone → progress photos — the site already tells this
story), and a restricted fund that must never leak into operations. It is also
the clearest demonstration of the multi-entity ledger: a Foundation project,
raised through AFRP channels, reported to donors of both.

---

## 4. Three integration wins worth calling out

**The Award is the retention hook nobody is using.** The Outstanding HS Senior
Award requires the *family's* membership in good standing at exactly the moment
a family's youngest is about to leave home — precisely when families lapse.
$3,000 a year in gift cards, positioned at the lifecycle's most fragile point,
is the cheapest retention programme AFRP runs. The platform should surface
"Award-age child in a lapsing household" as a signal, and the renewal
notice should say why it matters this year.

**Preservation and the family tree are one project wearing two names.** An oral
history is a tree record with audio; a photograph archive is the tree's media
layer; the "under maintenance" Preservation website should simply *be* the
tree's public face. And the §0 discovery playbook for scholarship history —
magazine back issues as the systematic record — is Preservation work by
another name. One archive, three funders, no duplication.

**Congressional Outreach runs on the directory.** Advocacy is organised by
congressional district; the member directory already holds addresses. "Which
members are constituents of this office" is one consented query, and it is the
single most useful thing software can do for an advocacy programme. The
existing per-field consent design covers it — advocacy contact becomes one more
consented channel, refusable like any other.

---

## 5. What changed in the prototype

The Program lens now renders **all seventeen site programs plus the giving
ladder**: the five new ones (Congressional Outreach, Exchange Mission, HS
Senior Award, Preservation, Senior Living) with their real published facts,
entity tags on every program with the two unconfirmed ones flagged, a
**lifecycle screen** drawing §1's pipeline with stage-conversion placeholders,
and the Senior Living screen shaped as a capital campaign (pledge ledger,
milestone timeline, $5M goal) rather than a cohort program.

---

## 6. Programmes are versioned data — turning off and installing

**Update, August 2026: AFRP has retired the Outstanding High School Senior
Award.** Which answers a question the design needed to face anyway: programmes
come and go, and the platform must handle that without a developer.

The answer is the fourth instance of the same pattern that governs bylaw
rulesets, dues schedules and region maps: **a programme is a registry row of
configuration, not code.**

**The status lifecycle:** `proposed → pilot → active → suspended → retired`.
Every transition is dated and attributed — who decided, citing what authority
(a Board resolution, a committee vote, an ARFECF policy). The Award's row now
reads *retired, effective 31 Aug 2026, Board resolution*.

**Retiring stops the future and preserves the past.** What stops immediately:
new applications, the budget line, the automated magazine section, comms
sends. What is preserved forever: every recipient in the alumni record, the
magazine archive, the ledger history, the criteria as they stood, and the
programme's place in past lifecycle analytics. Retirement is a status with a
date — never a deletion — for the same reason bylaws are versioned: past
decisions must remain reproducible.

**Installing a new programme** is creating a registry row from one of four
templates, then choosing which of the six rails (§2) it consumes:

| Template | Shape | Existing examples |
|---|---|---|
| **Cohort** | roster + sessions + outcomes | Camp, Leadership, Arabic, Exchange |
| **Award** | criteria + prizes + deadline + eligibility rule | the retired HS Award |
| **Campaign** | goal + pledge ledger + milestones + restricted fund | Senior Living |
| **Mission** | trip roster + partners + fundraising | Medical Mission, Project Hope |

No template fits? That's the signal it's genuinely new machinery — a
structural (tier 3) change, costed honestly, exactly as in the bylaw
flexibility model.

**One consequence worth acting on:** the Award was the teen-stage touchpoint,
and its retention signal — the award-age child in a lapsing household —
retires with it. The lifecycle now shows a visible gap between Camp Ramallah
and Scholarship. Whatever replaces the Award (the registry holds a *proposed*
successor row), it should keep the property that made the Award quietly
valuable: a reason for families to stay members while their youngest is
finishing high school.

---

## 7. Questions for AFRP

1. **Which entity operates** Women to Women, Preservation, and the Senior
   Living campaign — Ramallah Foundation, Inc., ARFECF, or AFRP? (Decides
   books, board, and 990.)
2. Is **Congressional Outreach** the bylaws' "Internships in Washington" EFund
   purpose, or separate money?
3. The **Award's "family in good standing"** — national dues, club dues, or
   both? (The same 4.3.1 question, in a friendlier costume.)
4. Does the **Exchange Mission** select participants, or take referrals from
   partners? (Decides whether it needs the application machinery or just a
   roster.)
5. Who owns the **Preservation archive's** copyright and takedown decisions —
   relevant before member-submitted photographs go on a public site.

---

*Design and planning only. Program facts are quoted from afrp.org as of 16
August 2026; funding attributions marked "confirm" are the site's grouping, not
verified against any ledger.*
