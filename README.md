# AFRP Platform — strategy, design record and prototypes

What to build for the American Federation of Ramallah, Palestine member
platform, and why: the design record every module is cut from, the build plan,
the clickable prototypes, and the synthetic fixture the build runs against.
**[AFRP-Hub](https://github.com/davidsaah/AFRP-Hub)** (private) is the build
itself.

The by-law citations and the design record are real. The people, club counts
and money figures in the prototypes and the fixture are fictional demo data.

## Start here

**[The site](https://davidsaah.github.io/afrp-strategy/)** lays the Federation's
strategy and the member platform side by side, on the four branches (Education,
Leadership, Heritage, Care), with the family tree as the roots and the
Convention as the junction. Seven sections:

1. **[AFRP Strategy](https://davidsaah.github.io/afrp-strategy/strategy/index.html)**: the Federation's current strategy, eight goals, and how the Hub implements each on the CRM.
2. **[Evolution](https://davidsaah.github.io/afrp-strategy/history/index.html)**: how the strategy got here, what still has to be developed, and the [open questions](https://davidsaah.github.io/afrp-strategy/history/questions.html).
3. **[Branches & programmes](https://davidsaah.github.io/afrp-strategy/programmes/index.html)**: the nineteen programmes and what each needs.
4. **[People](https://davidsaah.github.io/afrp-strategy/experiences/index.html)**: who uses the platform and what they need.
5. **[Workflows](https://davidsaah.github.io/afrp-strategy/workflows/index.html)**: how the work moves and hands off.
6. **[Prototype](https://davidsaah.github.io/afrp-strategy/prototype/index.html)**: the integrated prototype, with guided tours.
7. **[Development status](https://davidsaah.github.io/afrp-strategy/status/index.html)**: decisions, questions, the build track and the journeys.

The site is generated from `site/` (D47); see [`site/README.md`](site/README.md).
AFRP-Hub is **not yet in service**: no DNS, no live payments, no real member data.

## What is where

| Folder | What it holds | Published on the site? |
|---|---|---|
| [`design/`](design/) | **The design record.** The decisions register (D1–D53), the delivery status, the rules register, by-law analysis, the design documents each Hub module is cut from, the R6 ratification memos, the by-law texts (`design/bylaws/`), and the GCP hosting option (`design/hosting-gcp/`) | No, it is in the repository only |
| [`plan/`](plan/) | **The build plan.** `MASTER-PLAN.md` (the slice queue AFRP-Hub takes work from), `QUESTIONS-FOR-DAVID.md` (answered questions, kept as provenance), the archived earlier plans, and the consolidation plan | No, it is in the repository only |
| [`site/`](site/) | **The site's sources**: prose, data files, template, build and checks (D47) | Generates `docs/` |
| [`docs/`](docs/) | **The site.** Generated section pages, the prototype, the build board, the Library | Yes, GitHub Pages |
| [`docs/fixture/`](docs/fixture/) | The 500-household synthetic population and its generator | Yes |

**Precedence (Decision 41), highest first:** the by-law texts · the decisions
register and the named design documents · the prototype and narrative pages,
which evidence a *story* and never a *rule* · AFRP-Hub's code, which is
evidence of what *is* and never of what *should be*.

**Until 29 September 2026 there were three repositories.** This one was
`afrp-mockups`, and the design record lived in a private `AFRP-Portal`. They
were consolidated into this one. The old site address
`davidsaah.github.io/afrp-mockups/` no longer resolves.

## `docs/fixture/` is load-bearing: do not move it

`docs/fixture/afrp-fixture.json` is the 500-household synthetic population.
**AFRP-Hub's CI checks this repository out and reads that exact path**:

```
python manage.py seed_fixture ../afrp-strategy/docs/fixture/afrp-fixture.json
```

The journey corpus resolves its people as predicates over that fixture, so a
run against an empty database evaluates nothing. Reorganise around this path:
moving or renaming it silently stops another repository's evaluation from
meaning anything. The same applies to `plan/MASTER-PLAN.md`, which AFRP-Hub's
`journeys/workbench/build_page.py` reads to build the build board.

## Which by-laws are quoted

The **2024 Constitution & By-Laws (Jacksonville)** alongside the 2009/2012 text
it supersedes, the **2013 ARFECF By-Laws**, and the **2015/2017 ARFHSN
By-Laws** — held as versioned rulesets, with `bylaws-2012.2` in force and
`bylaws-2024.1` running in parallel under 48 provisional overrides pending
Board ratification.

**This repository is public, including the design record** (David, 29 Sep
2026). The by-laws reconciliation, the electronic-voting design and the
decisions register are here on purpose. Nothing about a real living person
beyond what is already public, and never real member data.

## The site's pages

| File | What it is |
|---|---|
| `AFRP-Design-Status.html` | **Decisions, open questions, and how the design changed** — the current page |
| `AFRP-Analyst-Dashboard.html` | **The build board** — the slice track, the journey corpus and its verdict, generated from the build's own report |
| `prototype.html` | The integrated clickable prototype, all modules, five lenses |
| `index.html` | The delivery hub |
| `AFRP-Platform-Map.html` | The platform map and element matrix. **Its build badges are a 19 Aug 2026 snapshot**, not a live reading — Design Status carries the current figures |
| `AFRP-Board-Packet.html` | Six decisions as they would be minuted, and the documents nobody has produced |
| `AFRP-Deep-*.html` | Deep dives: flagship programmes, the Convention, club activities, club management, federation operations |
| `AFRP-Complete-Platform.html` | Everything, as one reference |
| `AFRP-Platform-Experience.html` | Sixteen user-journey narratives |
| `AFRP-Unified-Member.html` / `-Operations.html` | Member and staff experience, static screens |
| `AFRP-Programs.html` | The programmes, with real content |
| `AFRP-Institutions.html` | ARFECF and ARFHSN |
| `AFRP-Ruleset-Workbench.html` | The by-law drafting workbench |
| `AFRP-Convention.html` · `AFRP-Community-LifeEvents.html` | Convention; community and life events |
| `AFRP-Design-System-v2.css` | The design system every prototype screen inlines byte for byte |
| `AFRP-Alumni-*.html` · `AFRP-Desktop-v2.html` · `AFRP-Mobile-v2.html` · `AFRP-Governance-*.html` · `AFRP-Portal-Screens.html` · `AFRP-Portal-Build-Spec.html` | Archive: superseded iterations, kept in place because live pages link to them |

**Two design languages, on purpose.** The prototype screens inline
`AFRP-Design-System-v2.css` so they look like the application. The documents
(the hub, the platform map, design status) carry their own house style, because
they are documents about the platform rather than parts of it.

## Publishing

GitHub Pages: Settings → Pages → Branch `main`, folder `/docs`.
Live at **https://davidsaah.github.io/afrp-strategy/**
