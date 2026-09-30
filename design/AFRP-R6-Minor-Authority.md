# R6 — guardian and delegation authority: who may act for a minor

**Drafted 8 September 2026.** This document exists to close the gap the rules
register records at R6: *"Guardian and delegation authority — who may act for a
minor. **inferred** — 13 citations, none stating it. ❌ not modelled."*

Three build slices have refused work on this gap rather than infer a rule about
children — the member-lens household slice, the club-lens households row, and the
minor-authority half of camp. That was the right call and this document does not
retroactively make those refusals wrong. It makes them finishable.

**Status: RATIFIED, 8 September 2026.** The four authority paths in §1 were
decided by David Saah. Everything else — the power set in §2, the supervise /
release split in §3, the restriction model in §4, and the two answers in §6 —
was drafted on youth-protection practice and **has since been approved as
drafted, without amendment, by all three bodies it was routed to**: the
Membership Committee (§2, §6's two-households question), Camp Ramallah (§3, §6's
court-appointed guardian), and the Legal Advisor (§3, §4, §6). Recorded by David
Saah, 8 September 2026.

**This document is now the design record for minor authority, and binds like any
other.** The provisional-label convention that applied while it was unratified
**no longer applies**: surfaces derived from it are ordinary rules, stated
plainly, not proposals. The refusals that stood in its absence lift — see §7.

**Nothing here is legal advice, and ratification does not make it so.** §3, §4
and §6 were reviewed by AFRP's Legal Advisor, who approved them as drafted;
that is a review of AFRP's own policy, not a substitute for advice on a
particular case. Where a real case does not fit these provisions, §4's
refuse-and-route posture is the answer, not an extension by analogy.

> **A numbering note.** "R6" here is the *rules register's* R6. The Hub's
> `ai-memory/01-BINDING-RULES.md` numbers its own nine rules independently and
> its R6 is a different rule (death terminates the record at `save()`). The
> collision is recorded in the register and is not resolved here. Cite this one
> as **R6 (register)**.

---

## 1. Who may act — the four paths · **decided**

Authority to act for a minor arises on exactly four paths, and on no other:

| # | Path | How it is established |
|---|---|---|
| **P1** | **Parent by household membership** | The adult is a member of the minor's household in the parent relation. Derived from the household record; no separate grant. |
| **P2** | **A named guardian** | Recorded against the minor by staff, with a reference to the document establishing it and the date. Never self-asserted. |
| **P3** | **Either of two parents when separated** | Both parents hold authority independently. Neither needs the other's agreement, and separation does not by itself reduce either one's authority. |
| **P4** | **An event "act for", identified at event setup** | Scoped to one event, may name more than one person, and is made known to the household's standing holders. Expires with the event. |

P1–P3 are **standing authority**: they follow the person, are not event-bound,
and end as §5 describes. P4 is **event authority** and is a different kind of
thing — §3 is entirely about keeping the two apart.

---

## 2. What "act for" permits — enumerated powers · *proposed*

Authority is **a set of named powers, never a single flag.** A chaperone on a day
trip and a parent are both "acting for" the same child and must not hold the same
thing. Least privilege is the rule: a path grants the powers it needs and no
others, and a power not granted is refused by name.

| Power | What it permits |
|---|---|
| `see` | View the minor's record. |
| `enrol` | Register the minor for an event or programme. |
| `transact` | Pay dues, fees or camperships on the minor's behalf. |
| `consent` | Give or withdraw consent held for the minor — data, photograph, programme participation. |
| `supervise` | On-site responsibility during a named event: check-in, supervision, the roster. |
| `release` | Collect the minor, or authorise their departure from a supervised setting. |
| `emergency` | Authorise emergency medical treatment when no standing holder is reachable. |

**What each path holds:**

| | `see` | `enrol` | `transact` | `consent` | `supervise` | `release` | `emergency` |
|---|---|---|---|---|---|---|---|
| **P1** parent | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **P2** named guardian | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **P3** either parent, separated | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **P4** event act-for | — | — | — | — | ✅ | **only if §3** | **only if §3** |

The empty cells are the point. An event act-for cannot read the child's record,
cannot enrol them in anything else, cannot pay, and cannot answer a consent
question on their behalf. Those refusals name this document.

**This grants no directory visibility.** R7 — minors never appear in any
directory payload — is untouched by every path above, including P1. Acting for a
minor is not seeing them in a directory, and no implementation of this document
may widen `core.directory.directory_queryset`.

---

## 3. Designated, or consented — the split that matters · *proposed*

David's decision has event setup identify the act-for individuals and make them
known to the parents or guardians. Read literally that would let an event
organiser confer authority over another family's child with the family merely
told afterwards. **For `supervise` that is right and normal. For `release` and
`emergency` it is not**, and the platform should not treat them alike.

**`supervise` is designated.** It comes from the organisation's own role
assignment — the adult is staff, a chaperone, a screened volunteer — and is
scoped to the named event. The household is **told**: the standing holders see
who is supervising, before the event, on the registration surface. This is
disclosure, and disclosure is enough, because supervision is the organisation
discharging its own duty rather than exercising a parent's.

**`release` is consented.** Only a standing holder (P1–P3) may put a person on
the release list for a minor. **An event organiser can never add themselves or
anyone else to it.** This is the single most important control in the document:
across youth-serving practice the authorised-pickup list is family-supplied
without exception, and an organiser-writable one is the failure that gets
children handed to the wrong adult.

**`emergency` is consented, and narrow.** It comes from an explicit
authorisation given by a standing holder at registration — not from P4, and not
by inference from `supervise`. It permits authorising treatment when no standing
holder is reachable, and nothing else.

So P4's row in §2 reads: `supervise` always; `release` only where a standing
holder named that person; `emergency` only where a standing holder authorised it
for that event.

---

## 4. When authority is restricted · *proposed*

**A recorded restriction overrides every path in §1, including P3.** "Either of
two parents" is the default and not a guarantee: where a court order, protective
order or equivalent document restricts an adult's authority over a minor, the
restriction wins, on every power, until it is lifted.

A restriction is a record, not an inference:

- entered by staff against the (adult, minor) pair, never derived from the family
  tree, the household, or a member's own assertion;
- carrying a reference to the document relied on, who recorded it, and the date;
- dated, and liftable only by the same route, leaving the history intact.

**The platform does not adjudicate custody.** It records what it was shown and
enforces it. Where the documents conflict, are ambiguous, or are described but
not produced, the platform refuses the action, says a restriction is on file that
it cannot resolve, and routes to the Legal Advisor — R40, not a guess. A refusal
here names R6 (register) and R40, and never states the substance of the
restriction to the person refused.

---

## 5. When authority ends · *proposed*

**Standing authority (P1–P3) lapses automatically on the minor's eighteenth
birthday.** It is derived from age, so it ends by age, with no action by anyone.
Per the Hub's binding rule 7 the subject's consent is then **re-asked, not
revoked**: the record stays, the outstanding refresh is visible, and nothing is
assumed on the young adult's behalf. An adult may afterwards *delegate* specific
powers back to a parent — the opposite direction, and always withdrawable by the
adult.

**Event authority (P4) expires with its event**, whatever the minor's age, and is
not renewed by the next event.

**Every exercise of authority is logged** — who acted, for whom, under which
path, when, and on which power. An authority model with no audit trail cannot be
audited after an incident, which is the moment it will be asked about.

---

## 6. The two questions the register routes · *proposed answers*

Both are recorded verbatim in `openQuestionCatalog` in the fixture and in the
rules register. Each is answered here provisionally so the build can proceed;
neither answer is ratified.

**"Camp pickup authority reads the household and delegation model. A
court-appointed guardian is neither parent nor delegate."** → *Routes to Camp
Ramallah + Legal Advisor.*
**Proposed:** a court-appointed guardian is **P2**, established by the appointing
order rather than by household membership. This is what P2 is for — it is the
path that does not depend on the household record, and a guardianship order is
exactly the document §1 requires it to carry. No new path is needed, and the
question resolves to a recording procedure rather than a rule change.

**"After a remarriage a minor belongs to two households with different clubs,
different directory choices and different pickup authority. By-Law 4.3.1 says
nothing about minors in two households."** → *Routes to Membership Committee +
Camp Ramallah.*
**Proposed:** authority is held **per person, not per household**. A standing
holder in either household holds the §2 powers, subject to §4. The three
consequences separate, and are not decided together:

- **Pickup** never follows from household membership on its own — it runs through
  the release list of §3, which both households' standing holders can write to.
- **Directory choices** resolve to **the more protective of the two** wherever
  they differ. R7 already excludes the minor from every payload, so this bites
  only on household-level display, and the restrictive reading is the safe one.
- **Club attachment** is **not decided here.** It is a membership question with
  dues and franchise consequences and belongs to the Membership Committee under
  By-Law 4.3.1, which is silent. The platform should hold both attachments and
  flag the person OPEN rather than pick one — R40.

---

## 7. What a build slice may do with this

**May:** model the four paths and the seven powers; enforce the supervise /
release / emergency split; record and enforce restrictions; expire authority at
eighteen and at event end; log every exercise; build the household screens,
family event registration, and the minor-authority half of camp against it.

**Must:** cite **R6 (register)** by number at the enforcement site; leave R7 and
the directory gate untouched; log every exercise per §5; refuse and route under
R40 where §4 or §6 leaves a case open rather than defaulting.

**Must, now that it is ratified — the refusals lift, and their text goes with
them.** Every surface that refused for want of this document must stop saying so.
`camp/views.py` (`R6_REFUSAL` and the module docstring) states that the rules
register marks R6 *inferred* and that no design document states it; both clauses
were already false when the document landed and are now doubly so. The camp
application, the member-lens household screen, the club-lens households row and
family event registration are ordinary build work against §1–§5. **The
counsellor-in-training refusal is untouched** — employment-law confidentiality is
a separate ground and does not lift with R6.

**May not:** widen any power beyond §2; let an organiser write a release list;
infer a restriction or a guardianship from the family tree; decide the club
attachment of a minor in two households (§6 leaves it OPEN under R40 — that
half was *not* ratified into a rule, it was ratified as staying open); or grant
directory visibility through any path.

---

## Provenance

| Section | Grade |
|---|---|
| §1 the four paths, event act-for at setup, multiple, made known | **attested** — decided by David Saah, 8 September 2026 |
| §2 enumerated powers and the per-path grants | **attested** — Membership Committee, approved as drafted, 8 September 2026 |
| §3 supervise designated / release and emergency consented | **attested** — Camp Ramallah and the Legal Advisor, approved as drafted, 8 September 2026 |
| §4 restriction overrides, recorded not inferred | **attested** — Legal Advisor, approved as drafted, 8 September 2026 |
| §5 lapse at eighteen, event expiry, audit trail | **attested** — approved with the whole; consistent with Hub binding rule 7 |
| §6 court-appointed guardian as P2; minor in two households | **attested** — Camp Ramallah and the Legal Advisor on the guardian; Membership Committee on the two-households answer, **including that club attachment stays OPEN** |

**Ratified 8 September 2026**, all three bodies approving their own sections as
drafted, without amendment. Recorded by David Saah; this row is the platform's
provenance for the grade. Camp Ramallah was asked in terms whether it needed an
operational exception for the unreachable-parent case at pickup and **did not ask
for one**, so §3's release rule stands with no escape hatch — recorded here
because a silence relied on should be written down as deliberately as a sentence.

`AFRP-Rules-Register.md` grades R6 **attested** as of this date, and the two open
questions it routed are closed there.

**What ratification did not settle.** §6's club attachment for a minor in two
households remains OPEN by decision, referred to the Membership Committee under
By-Law 4.3.1; the platform holds both attachments and flags the person. That is a
ratified instruction to keep asking, not an answered question.
