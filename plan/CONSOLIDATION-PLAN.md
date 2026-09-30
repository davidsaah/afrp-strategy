# Consolidation plan — three repositories into two

**Drafted 29 Sep 2026.** Decisions by David, 29 Sep 2026:

| # | Question | Decision |
|---|---|---|
| 1 | Visibility of the plan repo | **Revised 29 Sep: afrp-mockups, renamed afrp-strategy, stays PUBLIC, design record included.** David: "there is no sensitive information in there". A scan found no personal contact details, account numbers or IDs. It names one living person (the family-tree project lead, in AFRP-Family-Tree-Design.md), and board deliberation becomes public; David approved publishing with both known ("publish it"). The first choice was private with a public site; it failed because the account is not on GitHub Pro. |
| 2 | What moves into the plan repo | **The design record and the plan** — Portal's `docs/design`, by-laws; the Hub's `MASTER-PLAN`, `QUESTIONS-FOR-DAVID`, `docs/archive` |
| 3 | AFRP-Portal afterwards | **Deleted** — GitHub repo and local folder, after a verified snapshot |
| 4 | claude.ai Project chats | **History only** — archive them; new Project instructions point at the two repos |

**Out of scope, not to be touched:** AFRP-FTB, AFRP-FamilyTree, AFRP-History, and the
family-tree files in `Projects\Claude outputs\`.

## The end state

**afrp-strategy (public; renamed from afrp-mockups): what to build, and why.**

```
afrp-strategy/
  README.md        front door: what is here, how the Hub uses it
  design/          ← AFRP-Portal/docs/design/*  (34 docs + ratification/)
    bylaws/        ← AFRP-Portal/docs/bylaws/*.pdf
    hosting-gcp/   ← AFRP-Portal/deploy/  (see "The GCP note" below)
  plan/            ← AFRP-Hub docs/MASTER-PLAN.md, QUESTIONS-FOR-DAVID.md, docs/archive/*
                     + this file
  docs/            GitHub Pages: only this folder is served; paths unchanged
    fixture/       LOAD-BEARING — Hub CI seeds from docs/fixture/afrp-fixture.json
    archive/       the 8 superseded prototype pages
```

**AFRP-Hub (private): how it is built, and what happened.**
Code, tests, `CLAUDE.md`, `README.md`, `ai-memory/` (tests read 01, 05, 09),
`docs/ARCHITECTURE.md`, `docs/DEPLOYING.md`, `docs/ADR-001`, `docs/audits/`.

The build session reads the design record at `../afrp-mockups/design/` and the slice
queue at `../afrp-mockups/plan/MASTER-PLAN.md`. Both repos must be cloned next to each
other, which they already are.

---

## Phase 0: Snapshot (nothing is deleted before this exists). DONE 29 Sep: 3 bundles verified, Portal test-cloned with 39 commits

- [x] Tag `pre-consolidation` in all three repos.
- [x] `git bundle create --all` for each repo → `Projects\_archive\2026-09-29\`.
- [x] Zip each working tree including untracked files. Exclude `.venv`, `staticfiles`
      and `node_modules`.
- [x] Run `git bundle verify` on every bundle.

## Phase 1: Save work that exists only on disk

- [x] **AFRP-Portal:** commit the Decisions Register edit, which adds Part 3 (D30–D40)
      and Decision 41. The Hub already cites these, and until now they existed only as an
      uncommitted file. *Done 29 Sep, `b81599d`, pushed.*
- [x] **AFRP-Hub:** commit the following (docs only, `[skip render]`, CI must go green).
      *Done 29 Sep, `110c6dd`, pushed; 1,573 tests green locally; CI run 36661352215
      green (test + journeys). For 4b, Portal's
      later and fuller revision was used.*
  - the BUILD-PLAN superseded stub
  - MASTER-PLAN row A1
  - the QUESTIONS-FOR-DAVID edits
  - the untracked slice prompts (4b, 4c, 6, 7, 7b, 8, R1, A1)
  - `ai-memory/reviews/2f9131a.md`
- [x] **AFRP-Hub:** delete the sync-conflict copies `MASTER-PLAN-1.md`,
      `QUESTIONS-FOR-DAVID-1.md` and `08-OPEN-QUESTIONS-1.md`. All three are stale, as
      `10-WORKING-WITH-CLAUDE.md` already says, and the repo-wide test scanners read
      them from disk. *Done 29 Sep; copies kept in the snapshot.*
- [x] **afrp-mockups:** compare the uncommitted edits to the Analyst Dashboard and Design
      Status against HEAD (14 Sep). *Checked 29 Sep: they are NOT superseded. They date
      from 8 Sep, after HEAD's content for these two files (which still shows 1,106
      tests; they show 1,226 and add D40 and D41), but before today (1,573). Left
      uncommitted as the starting point for Phase 5's regeneration, and not published
      while the repo is still public.*

## Phase 2: Rename to afrp-strategy, then make it private without breaking the Hub or the site

**Renamed 29 Sep 2026 at David's request:** `davidsaah/afrp-mockups` → `davidsaah/afrp-strategy`,
local folder `Projectsfrp-mockups` → `Projectsfrp-strategy`. The site moved to
https://davidsaah.github.io/afrp-strategy/. The old `/afrp-mockups/` address is gone,
because GitHub does not redirect Pages sites.

1. [ ] **David:** put the personal account `davidsaah` on **GitHub Pro**. *29 Sep: GitHub
       refused Pages on the private repo with "Your current plan does not support GitHub
       Pages for this repository", so the account is not yet on Pro, perhaps because
       Copilot Pro was bought instead. Check https://github.com/settings/billing/summary.*
2. [x] **David:** a fine-grained read-only *Contents* token on the repo, stored in AFRP-Hub
       as the Actions secret `MOCKUPS_READ_TOKEN`. *Done 29 Sep. The first value saved was
       empty; it was re-saved at 03:26 UTC. The name is kept after the rename, because the
       token is bound to the repository and not to its name.*
3. [x] **Claude:** CI checkout with the token, locked by
       `afrp.tests_deploy.test_the_ci_reads_the_private_strategy_repo_with_its_token`
       (seen red). *`075713a`, then the rename follow-up `d3e78fd`; CI green on both.*
4. [ ] Change afrp-strategy to Private. *Tried 29 Sep: Pages switched off. Reverted to
       public by David, Pages re-enabled from `main:/docs`, all pages 200, Hub CI green.
       Retry only after step 1 is confirmed. Then Claude re-enables Pages with
       `gh api -X POST repos/davidsaah/afrp-strategy/pages -f "source[branch]=main" -f "source[path]=/docs"`.*
5. [ ] **Claude:** confirm https://davidsaah.github.io/afrp-strategy/ serves `prototype.html`
       (the home page can come from a cache, so it proves nothing) and re-run Hub CI to green.

**Steps 1, 4 and 5 were dropped on 29 Sep 2026: the repo stays public (decision 1 revised).**

## Phase 3: Move the design record and the plan into afrp-mockups

- [ ] `AFRP-Portal/docs/design/**` → `design/`, keeping the file names so every
      citation keeps working by name.
- [ ] `AFRP-Portal/docs/bylaws/*.pdf` → `design/bylaws/`.
- [ ] `AFRP-Portal/deploy/` → `design/hosting-gcp/`.
- [ ] `AFRP-Hub/docs/MASTER-PLAN.md`, `QUESTIONS-FOR-DAVID.md` and `docs/archive/*` →
      `plan/`. Leave a superseded stub in the Hub for each, following the pattern already
      used for BUILD-PLAN.
- [ ] Not carried over:
  - `docs/brand/AFRP_Logo.png`, which is byte-identical to `docs/assets/`
  - Portal's old `fixture/`, which is older than `docs/fixture/`
  - Portal's `Claude outputs/`, whose prompts duplicate the Hub's and whose catalogues
    are retired
- [ ] Check every moved file by checksum against the Portal source. The commit message
      names the Portal commit it was taken from.

## Phase 4: Repoint and tidy the Hub (a normal slice: build, red-team, suite green in both postures, CI green)

- [ ] Rewrite every `AFRP-Portal/docs/design/…` path and every "update
      `AFRP-Delivery-Status.md` in AFRP-Portal" instruction to point at afrp-mockups.
      This touches:
  - `CLAUDE.md`
  - `README.md`
  - `ai-memory/` files 00, 02, 08, 10 and the README
  - `prompts/build-a-slice.md` and the `slice-*` prompts
- [ ] `ai-memory/06-ENVIRONMENT.md:56` points the fixture at the Portal copy. Point it
      at `../afrp-mockups/docs/fixture/afrp-fixture.json`.
- [ ] Code comments that credit ports from `AFRP-Portal/src/*.ts` stay as provenance.
      `00-ORIENTATION` says once that AFRP-Portal was retired on the date it happens,
      and that its full history is in `Projects\_archive\2026-09-29\AFRP-Portal.bundle`.
      Applied migrations are never edited.
- [x] Delete the leftover databases `t4c.sqlite3` and `t7.sqlite3` (ignored, about 4 MB).
      Keep `t.sqlite3`, the local test harness's `DATABASE_URL`; `volume.sqlite3`, the
      render fixture; and `dev.sqlite3`.
- [x] Delete the stale ref `from-claude/main`, which is fully merged and came from an
      old bundle.
- [x] Tag `scratch/slice-8-mutations` as `slice-8-mutation-proof`, then delete the
      branch.
- [ ] Update `09-SESSION-LOG` and the README status.

## Phase 5: Tidy afrp-mockups

- [ ] Remove the empty `Run` file.
- [ ] Move the 8 superseded pages into `docs/archive/` and fix the links in `index.html`.
      The superseded pages are Alumni Desktop and Mobile, Desktop-v2, Mobile-v2,
      Governance-Finance Desktop, Governance Mobile, Portal-Screens and Portal-Build-Spec.
- [ ] Regenerate the Analyst Dashboard and Design Status from the Hub's current report.
      They still show 1,226 tests; the suite has 1,573.
- [ ] Rewrite the README:
  - two repositories, not three
  - the new `design/` and `plan/` folders
  - drop the line "internal planning docs are deliberately not here"
  - keep the note that `docs/fixture/` is load-bearing

## Phase 6: Delete AFRP-Portal (irreversible, so every gate is checked first)

Gates, each verified and not assumed:
- [ ] Every Portal `docs/` file is present in afrp-mockups with a matching checksum.
- [ ] D30–D41 are in `design/AFRP-Decisions-Register.md`.
- [ ] `grep -r "AFRP-Portal/docs"` in the Hub finds only historical mentions.
- [ ] The Portal bundle verifies, and a scratch clone from it shows all commits.
- [ ] Hub CI is green and staging is live on the repointed commit.

Then:
- [ ] **David** confirms, and the GitHub repo `davidsaah/AFRP-Portal` is deleted.
- [ ] The local `Projects\AFRP-Portal` folder is deleted.
- [ ] From `Projects\Claude outputs\`, delete `AFRP-Hub.bundle`,
      `afrp-app-initial.bundle`, `push-afrp-app.ps1`, `push-afrp-hub.ps1` and
      `ADR-001-build-foundation.md`, an older draft of the Hub's `docs/ADR-001`. The
      family-tree files stay.

## Phase 7: Claude's side

- [ ] Pause the **AFRP Hub Code Build** session from Phase 3 until Phase 4 is done, so no
      slice commits against paths that are moving.
- [ ] Claude writes new claude.ai Project instructions and a knowledge-file list for the
      two-repo layout. David replaces the Project's contents and archives the old chats.
- [ ] Update Claude Code's memory so that it records the two repos, the design record in
      afrp-mockups, and that AFRP-Portal is gone.

---

## The GCP note

`ai-memory/08-OPEN-QUESTIONS.md` records two hosting records, both standing on purpose.
ADR-001 chose a managed PaaS (Render), while the GCP direction was deliberately kept open,
and `AFRP-Portal/deploy/` (Terraform and `PORTABILITY.md`, 20 KB) is that option.
Deleting Portal should not silently close a decision, so it moves to
`design/hosting-gcp/`. If the GCP option is dead, close the open question explicitly and
drop the folder.

The old Node/TypeScript app (`src/`, `test/`) is not carried forward. It survives only in
the snapshot bundle.
