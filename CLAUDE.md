# afrp-strategy: the strategy session

This repository is the design record, the build plan and the public site for the
American Federation of Ramallah, Palestine member platform. A Claude Code session
opened **here** is a *strategy session*. The build happens in
[`../AFRP-Hub`](../AFRP-Hub), in a separate *build session*, one slice at a time.

| | Strategy session (here) | Build session (`../AFRP-Hub`) |
|---|---|---|
| Does | Decisions, questions, design notes, programmes, workflows, the site | One slice: build, red-team, fix, audit the fixes, CI, staging |
| Writes | `design/`, `plan/`, `site/`, `docs/`; private working files in `../AFRP-Hub/ai-memory/cowork/` | The Hub's code, tests and `ai-memory/` |
| Hands over through | **`plan/MASTER-PLAN.md`**: a slice is ready when its decision is recorded, its design note is written and its gate and exit test are set | The Delivery Status and the findings ledger |

Nothing passes between the two sessions in chat. If it is not in a file in one of
the two repositories, a build session cannot see it.

## Start of every session

1. `git pull` here **and** in `../AFRP-Hub`. Work may have been pushed from the
   laptop or from a phone-driven session since this clone last moved.
2. Read `../AFRP-Hub/ai-memory/cowork/LEDGER.md` (the Passes table), the newest
   report in `../AFRP-Hub/ai-memory/cowork/review/`, and the top of
   `plan/MASTER-PLAN.md`.

## Passes run through the `afrp` skills

Any request about the strategy, the record or the site goes through the `afrp`
orchestrator skill: the owning agents, then `afrp-review`, then `afrp-publish`.
Never publish around a review FAIL.

The skills were written for the claude.ai Project, and name its folder `claude/`.
**In this setup that folder is `../AFRP-Hub/ai-memory/cowork/`**, which is private
and travels with git:

| A skill says | Read and write |
|---|---|
| `claude/intake/LEDGER.md` | `../AFRP-Hub/ai-memory/cowork/LEDGER.md` |
| `claude/<folder>/<file>` | `../AFRP-Hub/ai-memory/cowork/<folder>/<file>` |
| "save to the Project" | the path above; nothing is saved only to the Project |

A pass ends with:

1. `python site/build.py`, then `python site/check.py`, with 0 problems.
2. One commit here holding the sources **and** `docs/`, with a message naming the pass.
3. A row in the Passes table of the LEDGER, committed in `../AFRP-Hub`.
4. Both repositories pushed. A session that ends with something unpushed has
   left it on one machine.

## Rules that are never relaxed

- **This repository is public.** Role-only and figure-free. No living person who
  is not already public in a by-law role. Never member, donor, applicant or
  camper data. Research reports and anything naming people stay in
  `../AFRP-Hub/ai-memory/cowork/`, or in the Drive file they came from.
- **Precedence (D41)**, highest first: the by-law texts in `design/bylaws/`; the
  Decisions Register and the named design notes; the prototype, which evidences a
  story and never a rule; the Hub's code, which shows what is and never what
  should be. Where the record is silent, say what is missing. Never pick a default.
- **Only David or a Board decides.** A decision settled in a session is written
  into the Decisions Register or the design note before any build session acts on it.
- Never write `.github/workflows`. Never enter or look for credentials. Never send
  email; drafts are saved as files for David to send.
- A file ending in `-1.md` is a sync-conflict copy, never the record.
