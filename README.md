# AFRP Platform — design record and prototypes

The public design record for the American Federation of Ramallah, Palestine
member platform: the clickable prototypes, the narrative documents, and the
synthetic fixture the build runs against.

Everything here is a **design artefact**. The by-law citations are real; the
people, club counts and money figures are fictional demo data.

## Start here

**[Design Status](https://davidsaah.github.io/afrp-mockups/AFRP-Design-Status.html)**
— what has been decided, what is still open and who owns it, and how the design
has changed. Thirty-nine recorded decisions, twelve open questions. **This page
is current; where an older document on this site disagrees with it, it wins.**

**[The build board](https://davidsaah.github.io/afrp-mockups/AFRP-Analyst-Dashboard.html)**
— the evaluation the build runs against itself: the slice track, all 374 catalogued journeys, and
the verdict on the 271 walked so far, including the six it currently fails. AFRP-Hub is **not yet
in service** — no DNS, no live payments, no real member data.

**[The delivery hub](https://davidsaah.github.io/afrp-mockups/)** — everything
else, grouped: use it · for the board · deep dives · read it · archive.

**[The integrated prototype](https://davidsaah.github.io/afrp-mockups/prototype.html)**
— the platform, clickable, across **five** lenses: Front door, Member, Club,
Program, Federation. One self-contained file — no build, no server, no network
calls. Works on a phone.

## The three repositories

| Repo | What it holds |
|---|---|
| **`afrp-mockups`** (this one, public) | The prototypes, the narrative documents, the design status page, and `docs/fixture/` |
| **`AFRP-Portal`** (private) | The design record: the decisions register, the rules register, the by-law source texts, the design documents each module is cut from |
| **`AFRP-Hub`** (private) | The application — Django, server-rendered, passwordless |

## `docs/fixture/` is load-bearing — do not move it

`docs/fixture/afrp-fixture.json` is the 500-household synthetic population.
**AFRP-Hub's CI checks this repository out and reads that exact path**:

```
python manage.py seed_fixture ../afrp-mockups/docs/fixture/afrp-fixture.json
```

The journey corpus resolves its people as predicates over that fixture, so a run
against an empty database evaluates nothing. Reorganise around this path; moving
or renaming it silently stops another repository's evaluation from meaning
anything.

## Which by-laws are quoted

The **2024 Constitution & By-Laws (Jacksonville)** alongside the 2009/2012 text
it supersedes, the **2013 ARFECF By-Laws**, and the **2015/2017 ARFHSN
By-Laws** — held as versioned rulesets, with `bylaws-2012.2` in force and
`bylaws-2024.1` running in parallel under 48 provisional overrides pending
Board ratification.

This repository is public, and quoting real by-law text here is deliberate and
stated on the hub page. Internal planning documents — the by-laws
reconciliation, the electronic-voting deliberation, the decisions register —
are **not** here; they live in the private repositories above.

## The full set

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
| `AFRP-Design-System-v2.css` | The design system every prototype screen inlines byte-for-byte |
| `AFRP-Alumni-*.html` · `AFRP-Desktop-v2.html` · `AFRP-Mobile-v2.html` · `AFRP-Governance-*.html` · `AFRP-Portal-Screens.html` · `AFRP-Portal-Build-Spec.html` | Archive — superseded iterations, kept rather than deleted |

**Two design languages, on purpose.** The prototype screens inline
`AFRP-Design-System-v2.css` so they look like the application. The documents —
the hub, the platform map, design status — carry their own house style, because
they are documents about the platform rather than parts of it.

## Publishing

GitHub Pages: Settings → Pages → Branch `main`, folder `/docs`.
Live at **https://davidsaah.github.io/afrp-mockups/**
