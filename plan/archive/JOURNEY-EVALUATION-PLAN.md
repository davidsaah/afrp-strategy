# The journey evaluation — does the Hub meet the needs the record describes?

**7 September 2026 · plan agreed · SLICE J1 IS BUILT** — the `journeys` app,
the runner, the table report, and the 16 canonical journeys are in the repo;
`python manage.py run_journeys` emits `journeys/report/latest.md`. First run:
7 MEETS · 1 GUARDED · 1 OPEN · 7 NOT BUILT · 0 FAILS. Slices J2–J5 remain.

The red-team rounds answer one question: *can this be broken?* Sixteen rounds
say yes, repeatedly, and the discipline in `ai-memory/` exists because of it.
This plan answers the **other** question, which no round has asked: *does the
Hub actually do what the design record promised the community?* A system can
refuse every attack and still not let a widow renew her late husband's
household, because nobody ever walked that path on purpose.

The instrument is a **journey corpus**: several hundred user journeys, derived
from the requirements record, instantiated with people from the 500-household
synthetic fixture, executed against the running Hub, and cross-referenced to
the Decisions Register — so every journey says which requirement it tests,
which decisions bind it, and whether the Hub honoured them.

---

## 1. Where journeys come from — nothing invented

Every journey cites its source. The record already contains four generations
of journey material; the corpus systematises it rather than inventing needs:

| Source | What it contributes | Journeys (target) |
|---|---|---|
| `AFRP-Platform-Experience.html` (mockups) | The 16 red-teamed canonical journeys (J1–J16) + Pathways | 16 canonical + ~48 variants |
| The five deep dives (mockups) | 117 paired moments — operator beside participant | ~117 seeds, one journey per moment, paired where both roles exist in the Hub |
| The 58-screen prototype (`prototype.html` data-routes) | Per-screen happy path + the refusal the screen names | ~110 |
| `AFRP-Decisions-Register.md` (Portal `docs/design/`) | Every lettered consequence row of Decisions 1–29 → at least one journey that would fail if the consequence were not implemented | ~60 |
| Binding rules R1–R9 (`ai-memory/01-BINDING-RULES.md`) + S1–S7 + R1–R45 (Complete Platform) | Journeys where the **correct outcome is a refusal that names its rule** | ~60 |
| Life-cycle arcs | Multi-session journeys: join → renew → lapse → grace → rejoin; birth → 18th-birthday refresh; death → record termination → condolence; club dormancy mid-year | ~30 |

**Target: ~400 journeys.** The number is an output of the derivation matrix,
not a quota — if the matrix yields 340 or 480, that is the honest count.

**Author from the record, not from the code.** The playbook's hardest lesson
(`03-RED-TEAM-PLAYBOOK.md`, the vault expiry): a test written from the same
misreading as the code confirms the misreading. Journeys are derived by reading
the mockups and the design documents **before** reading the implementation.
Where the record and the Hub disagree, the journey fails — that is the point.

## 2. What a journey is — data, not prose

One YAML file per journey under `journeys/specs/<lens>/<id>.yaml`:

```yaml
id: J-MEM-042
title: A lapsed member renews after April 30 and finds she cannot vote
persona:                      # a predicate, never a hardcoded fixture id
  select: member
  where: {standing: lapsed, lapse_reason: nonpayment, club: any-active}
lens: member
sources:
  - {doc: prototype.html, route: member/voting}
  - {doc: AFRP-Complete-Platform.html, rule: "By-Law 5.3"}
decisions: [D1-D]             # standing keys to collection date, not remittance
steps:
  - do: {signin: persona}
  - do: {visit: /renew/, pay: {tier: individual, channel: platform}}
    expect: {status: 200, contains: ["renewed"]}
  - do: {visit: /ballot/}
    expect:
      outcome: refusal
      names_rule: "By-Law 5.3"      # refusals name their rule — asserted, not hoped
outcome_class: refuses-correctly
```

Five outcome classes, all first-class:

| Class | Meaning |
|---|---|
| `completes` | The person achieves what they came for. |
| `refuses-correctly` | The Hub refuses **and names the rule** — a pass, not a failure. |
| `routes-open` | The screen flags OPEN and routes to the committee (R40) — correct where the record is silent. |
| `not-built` | The path's slice is not built. Recorded, never skipped silently: this is the gap register. |
| `fails` | The Hub did something the record says it must not. The only red class. |

**Personas are predicates over the fixture**, resolved at run time, so
reseeding never breaks the corpus, and a predicate with no match is itself a
finding (a coverage cell the fixture lacks). No real living person, ever; the
seeder's provenance-marker refusal stays in force.

## 3. The runner

A `journeys` Django app — the corpus ships **inside AFRP-Hub**, versioned with
the code it evaluates:

```
journeys/
  specs/<lens>/*.yaml        # the corpus
  schema.py                  # spec validation — a malformed journey refuses to load
  personas.py                # predicate → fixture person, deterministic (seeded)
  runner.py                  # executes steps via Django test client
  report.py                  # the conformance report
  management/commands/run_journeys.py
  tests/                     # tests of the runner itself — every assertion made to fail once
```

- **Tier A (all journeys):** Django test client against the seeded fixture —
  fast, deterministic, CI-runnable, no browser. Sign-in uses the passwordless
  flow with the staging code path, never a bypass.
- **Tier B (later, optional):** a Playwright pass over a subset for the 320px /
  accessibility gate — the CI overflow walk already covers routes; Tier B adds
  real interaction only where Tier A cannot see it.
- `python manage.py run_journeys [--lens member] [--decision D1] [--id J-MEM-042]`
  → console summary + `journeys/report/latest.md` + `latest.json`.
- CI: a separate job, **reporting, not blocking** at first — `fails` count is
  tracked per commit; it becomes blocking once the corpus is red-teamed (J5).

## 4. The conformance report — the deliverable David shows the Board

`run_journeys` emits one report answering the actual question:

1. **By lens and module:** completes / refuses-correctly / routes-open /
   not-built / fails, with counts and the journey ids behind each number.
2. **By decision:** every register decision with the journeys that exercise it —
   and, in red, **decisions no journey covers** and journeys resting on the
   reopened Decision 5, flagged rather than assumed.
3. **The gap register:** every `not-built`, grouped by the build-plan slice
   that would close it — this replaces guessing about what the community is
   still missing.
4. **The refusal audit:** every refusal encountered, with the rule it named —
   a refusal that names no rule is a `fails`, per binding rule 9.

## 5. The slices — same discipline as everything else

Each slice: build → red-team → fix → audit the fix layer → push → CI green.
One slice per session, per `10-WORKING-WITH-CLAUDE.md`.

| Slice | Work | Exit test |
|---|---|---|
| **J1** | Schema, persona resolver, runner, report skeleton. Seed corpus: the 16 canonical journeys as specs, run end to end. | 16 journeys execute; at least one lands in each outcome class; every runner assertion has been made to fail once. |
| **J2** | Derivation sweep, member lens + front door: prototype routes × deep-dive moments × decision consequences. ~140 specs. | Every member-lens route and every Decision 11–22/27–28 consequence has ≥1 journey; report renders. |
| **J3** | Club + federation lenses. ~140 specs, operator/participant paired where the deep dives pair them. | Every club/federation route covered; D1 consequences A–G each have a journey; the ledger journeys reconcile to the cent. |
| **J4** | Programme lens + life-cycle arcs + cross-lens handoffs (the Rails: rung-5-to-rung-1 journeys). ~100 specs. | Every programme in the register reachable by a journey; the four rails each walked end to end. |
| **J5** | **Red-team the corpus itself** — journeys that cannot fail, personas that silently match nobody, `contains` assertions satisfied by wrong output (`"40"` vs `$4000`), specs that test the code's misreading rather than the record. Fix, audit the fix layer, then flip CI to blocking on `fails`. | A mutation pass: deliberately break three known rules in a scratch branch; the corpus must catch all three. |

Estimated total: ~400 specs across J2–J4. Sized honestly: five sessions.

## 6. Rules this plan obeys

- **The record is the source of truth.** A journey the record does not support
  is deleted, not kept because it is interesting. Where the record is silent,
  the journey's expected outcome is `routes-open`, never a default.
- **Synthetic people only.** Persona predicates resolve against the fixture;
  journey specs carry no names, only predicates and resolved-at-runtime ids.
- **`not-built` is information, not embarrassment.** The corpus is written
  against the whole record now, so the gap register is complete on day one and
  shrinks as slices land — the same journey that reports `not-built` today is
  the acceptance test for the slice that builds it.
- **A journey that has never failed is a claim, not a check** (J5 exists
  because of this).
- **Keep the memory true:** J1 adds a section to `05-MODULE-MAP.md` and a row
  per slice to `09-SESSION-LOG.md`; confirmed corpus findings append to
  `04-FINDINGS-LEDGER.md`.

## 7. What David does

1. Review this plan; strike or add journey sources (§1) — the derivation
   matrix is the one thing worth your eyes before the work starts.
2. In a Claude Code session in `AFRP-Hub`, run the prompt at
   `ai-memory/prompts/derive-journeys.md` (slice J1 first).
3. Review the first conformance report on staging after J2 — one review per
   slice thereafter, same cadence as the build phases.
4. Push after each slice; the report's per-commit `fails` trend is the number
   to watch.

## 8. The catalogue — added 7 September 2026

The derivation of §1 is now DATA: `journeys/catalog.yaml` enumerates all 326
journeys (16 canonical + 310 specified) with lens, programme (two-axis:
the five lenses × the 19 programmes + platform), kind (canonical · screen ·
decision · rule · arc · deep · program), persona predicate, expected class,
decisions, sources, scenario and authoring slice. `run_journeys` reconciles
corpus ↔ catalogue on every run — an orphan spec refuses the run — and
writes `journeys/report/catalog.md`: every row with its rating where
runnable, `SPECIFIED · slice` where not. Staged scenarios (an open
election, a chargeback, a dormant club) build through the Hub's own
services inside the always-rolled-back run; `journeys/scenarios.py` holds
the registry, `open-election` is the worked example. Feature work
interacts with the catalogue in exactly two ways: author the specs for a
feature's SPECIFIED rows when building it, and add rows first when a new
requirement appears. The authoring prompts (`ai-memory/prompts/
derive-journeys.md`) are now catalogue-driven.
