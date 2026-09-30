# The design record

The documents AFRP-Hub is built from. Every module in the Hub is cut from a named
document here, and where the record is silent the Hub refuses rather than guess
(see AFRP-Hub `CLAUDE.md`).

**Precedence, highest first (Decision 41):** the operative by-law texts (`bylaws/`) ·
the decisions register (`AFRP-Decisions-Register.md`) and the named design documents ·
the prototype and narrative pages in `../docs/`, which evidence a *story* and never a
*rule* · the Hub's code, which is evidence of what *is* and never of what *should be*.

| Start with | What it holds |
|---|---|
| `AFRP-Decisions-Register.md` | Every human decision the design waits on: the answer, the date, and who decided (D1–D42) |
| `AFRP-Delivery-Status.md` | The running build record, updated by each Hub slice |
| `AFRP-Rules-Register.md` | By-law parameters reconciled from source |
| `AFRP-Strategic-Plan-Crosswalk.md` | Every element of the Federation's strategic plans (2019–2026) and what the platform does about each |
| `ratification/` | The R6 decision memos and the packet that builds them |
| `bylaws/` | AFRP Constitution & By-Laws 2024, ARFECF 2013, ARFHSN 2017 |
| `hosting-gcp/` | The GCP deployment option, kept open on purpose (AFRP-Hub `ai-memory/08-OPEN-QUESTIONS.md`); the Hub runs on Render |

**Provenance.** Moved here on 29 Sep 2026 from `davidsaah/AFRP-Portal` (`docs/design/`,
`docs/bylaws/`, `deploy/`) at commit `b81599d`, byte for byte. AFRP-Portal is being
retired. Its full history is kept in the snapshot bundle
`Projects/_archive/2026-09-29/AFRP-Portal.bundle`.

This repository is public, and so is this record: David decided on 29 Sep 2026 to
publish it.
