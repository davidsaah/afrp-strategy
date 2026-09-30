# Setting up the claude.ai "AFRP-Hub" Project after the consolidation

The Project's old chats and uploaded files predate the move to two repositories.
Uploaded copies go stale the day they are uploaded; that is how a session came to
work from a sync-conflict copy missing weeks of decisions. So the Project should
**point at the repositories, not hold copies of them**.

## 1. Replace the Project knowledge

1. Remove every uploaded file from the Project's knowledge: old plans, registers,
   prompts and exports.
2. **Add from GitHub → `davidsaah/afrp-strategy`**, then choose `design/` and `plan/`.
   The repository is public, so this needs no special access, and GitHub-synced
   knowledge can be refreshed rather than re-uploaded.
3. Optionally add **`davidsaah/AFRP-Hub`** as well, choosing `CLAUDE.md`, `README.md` and
   `ai-memory/`. This needs the Claude GitHub app to have access to that private repo.

## 2. Paste this as the Project instructions

```
This Project is the planning and review side of the AFRP member platform for the
American Federation of Ramallah, Palestine.

There are two repositories, and only two:
- davidsaah/afrp-strategy (public): what to build and why.
  design/ is the design record (the Decisions Register D1-D41, the Delivery
  Status, the Rules Register, the by-law analysis and texts). plan/ holds
  MASTER-PLAN.md, the slice queue. docs/ is the prototype site at
  https://davidsaah.github.io/afrp-strategy/.
- davidsaah/AFRP-Hub (private): the Django build. It is built by Claude Code
  sessions working in C:\Users\David\Projects\AFRP-Hub with afrp-strategy
  cloned beside it.

AFRP-Portal and afrp-mockups no longer exist; both were folded into
afrp-strategy on 29 Sep 2026. If an old chat or file mentions them, the content
is now in afrp-strategy/design/ or afrp-strategy/plan/.

Precedence (Decision 41), highest first: the by-law texts; the Decisions
Register and the named design documents; the prototype, which evidences a story
and never a rule; the Hub's code, which shows what is and never what should be.
Where the record is silent, say what is missing. Do not pick a default.

A build session cannot read this Project. Any decision made in a chat here must
be written into afrp-strategy (the Decisions Register or the relevant design
document) before a build session can act on it. When a conversation here
settles something, end by giving David the exact text to add, and the file it
goes in.

afrp-strategy is public. Nothing about a real living person that is not already
public, and never real member data.
```

## 3. Archive the old chats

After the knowledge and instructions are replaced, archive the Project's old chats.
David decided on 29 Sep 2026 that they are history only: everything that mattered
had been written to files. Archiving keeps them searchable without them being
mistaken for current guidance.
