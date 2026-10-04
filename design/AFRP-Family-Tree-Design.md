# The Ramallah Family Tree in the platform
### Lineage as evidence — design decisions of 20 August 2026

**2 October 2026:** D68–D74 (Decisions Register, Part 5) change what follows: D69 supersedes D11's staging, D71 amends D17, D72 amends D14's mitigations, D70 confirms D13 and D68 supersedes D27. The design built on them is `AFRP-Family-Tree-Module.md` (P28); the text below is left as written.

**Source file:** `Ramallah Family Tree_20260813.ged` — a desktop-genealogy export dated 13 Aug 2026,
submitted by the project's volunteer lead. **28,226 individuals · 10,399 families ·
nine clans · earliest recorded birth 1500.**

**The project itself:** begun in 2003 at the San Jose Convention. It documents the descendants of
**Rashed El-Haddadeen**, who settled Ramallah around 1517 — a Ghassanid line that came by way of
Karak in Jordan. Its source of record is **Azeez Shaheen, *Ramallah, Its History and Its
Genealogies* (1982)**, carrying data from the mid-1970s onward. Today it runs on a Google Group:
apply, await approval, access a members-only area, submit corrections on a form or directly to the project's lead.

---

## The fact that makes this the most load-bearing program in the federation

**By-Law 4.1.1** admits a Regular Member of origin from ancestral Ramallah *"as defined within Aziz
Shaheen's book entitled 'Ramallah'."*

The book underneath the family tree **is the by-law's own eligibility test.** The Scholarship then
requires "direct lineage to original Ramallah families." The Outstanding High School Senior Award
sits in the same family. So the genealogy is not a heritage sideline — it is the evidence layer
under membership itself, and three programs already depend on it without any of them being able to
see it.

That is also exactly why it has to be handled with care.

---

## The four decisions

### 1 · Deceased real, living synthetic — in the public build
The mockups repository is **public**. The file contains roughly 27,000 people with no death
recorded, including children.

- **Deceased ancestors render real.** They are already published in Shaheen 1982; they are
  historical record and the shared heritage the project exists to preserve.
- **Every living person in the public build is a synthetic stand-in** occupying the exact structural
  position, so the demo teaches the same lesson without publishing anybody.
- **The GEDCOM never enters the repository.** It stays in the session workspace and on David's
  machine. Verified: no identifier, name or date from the real living layer appears anywhere in
  `docs/`.

The worked example is David Saah's own line — his real ancestors, a stand-in for him.

### 2 · The tree is evidence for a human decision, never the decider
A verified path **does not** auto-satisfy 4.1.1, and the absence of one **never** denies.

> *A genealogy database must never become the gatekeeper of who is Ramallah.*

The platform renders the claimed path with each link's source and confidence, and hands it to the
**Membership Committee**, who decide. The reason is arithmetic: **5,819 people in the file have no
recorded parents** and 3,870 carry no clan reference at all. If the file were authoritative, every
one of those gaps would become an eligibility denial — and the by-law's own escape hatch, the
**4.2.1 Associate route**, exists precisely for people the genealogy cannot reach.

**The file's silence is not evidence of absence.**

### 3 · Inside the platform, all members see everything — recorded as a decision
*Since 2 October 2026:* D71 amends this decision (D17). A signed-in member sees the living in full only inside their own branch: blood relatives sharing an ancestor no further back than a great-great-grandparent, and their spouses. Outside it, a living person shows a name and a position on the plate only. D28 is unchanged. The premise below, that open visibility "matches how the Google Group works today", was also wrong about practice. In practice (research, 2 Oct 2026), access is by approval of each request, not by membership; see Q-200 (P27 §1.3).

This matches how the Google Group works today, so the platform does not quietly change it. It is
recorded here so it is a decision rather than an accident:

> Open visibility puts roughly 27,000 living people's names, dates and family structure in front of
> anyone who pays to join.

That is a plausible targeting and identity surface. It is **the one setting in this design worth
revisiting before launch**, and it is a single parameter, not a rebuild. The alternative already
designed elsewhere in the platform — per-field, per-audience consent — drops in without structural
change.

### 4 · First job: lineage verification for 4.1.1 and the Scholarship
Heritage browsing and the corrections pipeline both come later. Verification is first because two
programs are already blocked on it.

---

## What is built

**`member/family`** — a working simulation:

- **Find your line.** Search by your own name or the oldest ancestor you can name — because most
  people cannot get past a great-grandparent, and the search is built for that, not against it.
- **The path, with its sources.** Fifteen generations rendered with a confidence chip on every link:
  **record** (civil registration and family papers), **Shaheen 1982**, **tradition**. Confidence
  visibly degrades as you go back rather than one uniform line implying uniform certainty.
- **The evidence packet** — `10 links documented · 4 links traditional · 0 links assumed` —
  attachable to a membership or a scholarship application. **Verified once, reused everywhere**,
  instead of lineage being re-argued at every door that asks.
- **The gap case**, walked in full: a claimant whose line stops at a great-grandmother born in
  Ramallah about 1905 with no recorded parents. The platform reports what it found, what it did not,
  and routes her to the Committee and the Associate route. It issues no refusal.
- **The nine clans** — YSF 3,593 · SHAR 3,356 · IBR 3,337 · AWD 3,335 · JAG 3,176 · SHAK 3,057 ·
  JIR 2,955 · HAS 966 · AZZ 581 — with the claimant's own clan identified from the path.

**29 verification assertions pass**, including four that specifically assert no real living person
appears.

---

## The worked example — fourteen generations

Ramallah to California, 1500 to now. Real, from the file, all deceased:

| | | |
|---|---|---|
| g1 | Sama'an Daoud Samman Nakhleh Saah | 1936 Jerusalem – 2006 |
| g2 | Daoud Sama'an Nakhleh Ibrahim Saah | d. 1992, Ramallah |
| g3 | Sama'an Nakhleh Ibrahim Saah | b. abt 1852, Ramallah |
| g4 | Nakhleh Ibrahim Elias Salameh Saah | b. abt 1826 |
| g5 | Ibrahim Elias Saah | b. abt 1797 |
| g6 | Elias Salameh Saah | b. abt 1769 |
| g7 | Salameh Ibrahim Saah | — |
| g8 | **Sa'ah Ibrahim Awwad** | *the surname begins here* |
| g9 | Ibrahim Awwad I | — |
| g10 | **Awwad Bin-Haddad** | b. 1556 — founder of the Awwad clan |
| g11 | Haddad Bin-Rashed El-Haddaddeen | b. abt 1529 |
| g12 | **Rashed Bin Saqqer Bin Issa El-Haddaddeeni** | b. abt 1500, **Shoubak, Jordan** |
| g13 | Saqqer Bin Issa El-Haddadeen Al-Ghassani | Karak |
| g14 | Issa El-Haddadeen Al-Ghassani | Arabian Peninsula |

Two details worth keeping. **At g8 the surname is born** — "Sa'ah Ibrahim Awwad" is a man's given
name becoming a family's name, which is why every name in this file reads as a patronymic chain and
why *the name itself encodes the lineage*. And **Awwad Bin-Haddad has 8,952 descendants in the file
alone** — nearly a third of the whole record from one man born in 1556.

---

## What comes next
1. **Corrections and submissions** — rebuild the project lead's pipeline: request access, propose an
   addition or correction, review, publish, version. *(Since 2 Oct 2026: members in current national standing propose (D70); the committee applies with one key or two (D72); the Hub becomes the record after a parallel run (D69); slices T2b, T2c and T2d in P28 §14.)* Today it is a Google Group, a form, and one
   person, and that is the maintainer's real bottleneck.
2. **Heritage browsing** — walk your line, and find how you are related to another member. The most
   emotionally compelling surface in the entire platform, and the strongest reason a young person
   would ever create an account.
3. **Reconciliation with `AFRP-History`** — the Ottoman-era defter work already in the repo
   (a name register from the 1550s) overlaps the top of this tree exactly where confidence is
   weakest. That is where g11–g14 could stop being tradition and start being record.

---

*Design and planning only; build remains on hold. The real GEDCOM is not in the repository and must
not be committed to it.*
