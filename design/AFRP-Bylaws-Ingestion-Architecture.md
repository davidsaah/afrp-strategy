# Bylaws ingestion and the override register
### How the portal takes in a governing document and turns it into enforceable, citable rules — without a developer in the loop

**Date:** August 2026
**Decisions recorded (16 Aug 2026, David):** mockups-only remains in force — this is design, not buildout. AFRP 2012 and 2024 rulesets run in parallel with a divergence report before 2024 is declared governing. Overrides are entered by the design team, flagged provisional, pending Board adoption. Chapter-club bylaws are out of scope for now; the federation's three entities (AFRP, ARFECF, ARFHSN) are in scope.
**Mode:** design and planning. No buildout.

---

## 0. The shape of the problem

The Federation is governed by at least eight instruments: the AFRP Constitution & By-Laws (2024, superseding 2009/2012), the ARFECF By-Laws (2013), the ARFHSN By-Laws and Organizing Document (2015/2017), the ARFECF Scholarship Fund Policy Statement (2015), the Endowment Fund Policy Statement, the AFRP Board Rules & Regulations, the Convention Contract Guidelines, and the Strategic Planning Proposal now incorporated by reference at AFRP 17.1.4. Three are on file; five are cited as governing and unseen.

The existing design already established the principle: **bylaws are data; the code implements mechanisms and the ruleset chooses among them** (AFRP-Bylaw-Flexibility.md). What was missing is the front half — how a PDF approved at a convention becomes a versioned ruleset the engine can cite — and the honest half — what the system does where the text is silent, ambiguous, or contradictory. That is ingestion and the override register, and they are one pipeline.

---

## 1. The document registry

Every governing instrument is a first-class object:

```
document: afrp-bylaws-2024
  entity: AFRP
  class: constitution+bylaws        (or: policy-statement, rules-and-regulations,
                                     contract, external-proposal)
  adopted: 2024-07-13 (Jacksonville Convention)
  supersedes: afrp-bylaws-2012.2
  source-file: sha256 of the uploaded PDF, stored immutably
  canonical-text: the extracted text, verbatim — typos, OCR damage and all
  status: ingested | extraction-drafted | ratified | superseded
```

Three registry rules that matter:

1. **The source file is immutable and the canonical text is verbatim.** The 2024 text says "March 31th," "deemed to be have a quorum," and "reduced to four (2)." The ARFECF file carries a literal "Replace with" redline marker. These are preserved exactly; normalized readings live in the override register, not in the text. Amending the stored text would be manufacturing evidence.
2. **Incorporation by reference creates a registry row.** When 17.1.4 says "review the Strategic Planning Proposal," the system creates a `cited-but-missing` document row. Every rule that depends on a missing document is visibly marked incomplete — the system knows what it doesn't know.
3. **A document belongs to exactly one entity, but its rules may bind others.** ARFHSN's amendment rule binds the AFRP Board; AFRP's 7.1.1 seats ARFECF officers. Cross-entity bindings are recorded as edges, which is what makes the joint-convention franchise separation (§4) checkable.

---

## 2. The ingestion pipeline: agents extract, humans ratify

This is where "use agents to implement the bylaws" lands, and the division of labor is strict:

```
upload PDF ──► canonical text ──► AGENT EXTRACTION ──► draft ruleset + gap list
                                                              │
                                              human review (David / committee)
                                                              │
                                          ratified ruleset  +  override register entries
```

**Stage 1 — extraction.** One analysis agent per document (run in parallel across documents) reads the full text and produces: the ruleset inventory (every machine-relevant rule with its citation, load-bearing text quoted verbatim), a divergence report against the predecessor version if one exists, verification of any claims prior analyses made about this document, and a gap list — every silence, ambiguity, and internal contradiction, each with a *recommended* provisional interpretation and rationale. This ran for real on 16 Aug 2026: the AFRP-2024 and ARFECF-2013 extractions in AFRP-Bylaws-2024-Divergence.md and AFRP-ARFECF-ARFHSN-Rulesets.md are the pipeline's first outputs, and they caught two phantom rules a human summary had introduced (the ARFECF region map and interlock cap — cited in the earlier reconciliation, absent from the text).

**Stage 2 — adversarial verification.** A second agent, blind to the first's reasoning, spot-verifies the draft: every quoted passage against the canonical text, every citation, every claimed absence (the cheapest and most valuable check — "confirm the word 'electronic' appears nowhere"). Extraction that survives verification becomes a *draft* ruleset.

**Stage 3 — ratification.** No draft governs anything. A human — during the build phase, David; in operation, the body the override policy names — reviews the draft and the gap list, accepts or edits each override, and ratifies. Ratification stamps who, when, and on what authority. Only ratified rulesets feed the governance engine, and even then per the effective-date rules in AFRP-Bylaw-Flexibility.md §2.

**What agents never do:** decide an interpretation, resolve a conflict between documents, or write into the canonical text. Agents propose; the register records; humans adopt. The pipeline's product is not obedience to a PDF — it is a *legible draft* of what obedience would mean, with every judgment call surfaced instead of buried.

---

## 3. The override register

An override is the system's answer where the text has none, recorded as data with the same discipline as the rulesets:

```
override: AFRP-OV-03
  entity: AFRP
  ruleset: afrp-bylaws-2024.1
  gap: 9.2.1 mailing clock runs from an undefined certification event;
       9.2.2 return deadline Jun 10; lawful sequence yields a negative window
  citations: [9.2.1, 9.2.2, 8.12.6, 9.3.5]
  kind: gap-fill                     (or: conflict-resolution, normalization,
                                      cross-document, external-default)
  reading: certification due May 10 handoff + 7 days; ballots mail by May 17;
           later mailing surfaced as a rule violation
  rationale: only a fixed mailing date makes 9.2.2 satisfiable
  status: PROVISIONAL — entered by design team 16 Aug 2026,
          pending Board adoption
  ratified-by: —
```

**The lifecycle:** `provisional → ratified | rejected | superseded-by-amendment`. Per David's decision, the design team enters overrides during the build phase and every one is born provisional. The register currently holds **48 provisional entries**: 18 for AFRP-2024 (divergence doc §D), 22 for ARFECF (rulesets doc §1.3), 8 for ARFHSN (rulesets doc §2.2).

**Rules of the register:**

1. **Every override names its gap, its citations, and its rationale** — the same standard the refusal design already meets. A refusal that rests on an override says so: *"Not eligible… By-Law 4.3.1 · ruleset afrp-bylaws-2024.1 · reading per override AFRP-OV-xx (provisional)."* Nobody discovers years later that an outcome rested on an interpretation they never saw.
2. **Overrides interpret; they never contradict.** An override can fill a silence, resolve an ambiguity between plausible readings, or choose between two contradictory clauses (naming the loser). It cannot negate an unambiguous rule — that is an amendment, and the drafting workbench is the tool for it.
3. **The integrity floor is not overridable.** The Tier-4 properties (AFRP-Bylaw-Flexibility.md §1): no stored voter↔ballot link, no interim tallies, frozen record rolls, append-only audit, exact-decimal arithmetic, no silent tie-breaking. No override, ratified or otherwise, reaches them.
4. **Provisional overrides are loud.** Every screen, report, and refusal that depends on one carries the provisional badge, and the register produces the ratification agenda: the list of interpretations awaiting Board adoption, ordered by how many decisions have already leaned on them. That ordering is the clarity David asked for — it turns "the system made assumptions" into "here are the eleven sentences the Board should adopt, and here is everything each one has decided so far."
5. **An amendment retires its overrides.** When a revision answers a gap, the override moves to `superseded-by-amendment` with a pointer to the new text — the register doubles as a running list of exactly what the next revision should say, which is what the Constitution Committee actually needs from us.

---

## 4. Franchise separation — one room, three entities

The corpus now establishes three legally distinct decision mechanisms that can all be exercised in the same convention hall on the same day:

| Franchise | Who votes | Governing text |
|---|---|---|
| `afrp-delegate` | Weighted club delegations, fractional votes, member extraction; DP by mailed CPA ballot | AFRP 9.1.3, 9.2 |
| `arfecf-member` | Natural persons in good standing, one vote each (provisional EC-OV-3) | ARFECF Art. IX §1 |
| `arfhsn-board` | The AFRP Board of Directors, 60% of all members, mandatory full poll | ARFHSN Art. V |

Every motion in the system carries its franchise tag, and the ballot engine refuses a motion whose franchise doesn't match the body in session — the refusal naming, as always, the rule. ARFECF membership is a derived view of the AFRP roster (Art. V §2), so certification runs once and franchise eligibility is computed per entity; ARFHSN has no roster at all, only the AFRP Board's. This is the entity-scoped access model from the reconciliation doc, made concrete by the actual texts.

**Chapter clubs** (out of scope per David, 16 Aug): the design reserves a fourth franchise slot and a per-club ruleset chain with parent-conflict checking (Const. Art. IV: club documents "shall not conflict"), to be filled when club bylaws are collected. Nothing above depends on it.

---

## 5. Corpus status

| Document | Status | Ruleset |
|---|---|---|
| AFRP Constitution & By-Laws 2024 (Jacksonville) | Ingested, extraction drafted + verified | `afrp-bylaws-2024.1` — parallel with 2012, not yet declared governing |
| AFRP Constitution & By-Laws 2009/2012 | Superseded 13 Jul 2024; retained for non-retroactivity | `afrp-bylaws-2012.2` |
| ARFECF By-Laws 2013 | Ingested (OCR of marked-up copy — clean copy wanted), extraction drafted | `arfecf-bylaws-2013.1` |
| ARFHSN By-Laws 2015/2017 | Ingested, extraction drafted | `arfhsn-bylaws-2017.1` |
| Scholarship Fund Policy Statement 2015 | **Cited, not on file** | — |
| Endowment Fund Policy Statement | **Cited, not on file** | — |
| AFRP Board Rules & Regulations | **Cited, not on file** (source of the dues tier ladder) | — |
| Convention Contract Guidelines | Referenced at 10.1.6; 2009 contract previously analyzed | — |
| Strategic Planning Proposal (17.1.4) | **Cited, not on file** | — |
| 26 chapter-club bylaws | Out of scope (David, 16 Aug 2026) | reserved |

---

*Design and planning only. Companion documents: AFRP-Bylaws-2024-Divergence.md (the AFRP parallel-run report and its 18 overrides) and AFRP-ARFECF-ARFHSN-Rulesets.md (the sister-entity rulesets and their 30 overrides).*
