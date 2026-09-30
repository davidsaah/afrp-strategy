# AFRP Scholarship Alumni — recruiting
### Use cases and flows

**Date:** August 2026
**Deliverable mode:** design only. Mockups and use cases; no buildout.

---

## 0. Why this is the highest-value list AFRP owns

A scholarship recipient from 1998 is now around 48. Mid-career. Possibly
affluent. Quite likely with children of their own approaching college.

**AFRP paid for their education.** There is no warmer list in the federation —
not lapsed members, not event attendees, not donor prospects. Nobody converts
better than someone whose degree you helped fund.

And most of them are almost certainly not in any system today, because the
program ran on paper and spreadsheets for decades.

The framing that follows from that: **this is not an archiving project with a
recruiting side-effect. It is a recruiting project that happens to need
historic data.** Every design decision below follows from that, and it is why
"load everything perfectly" is the wrong instinct — reaching people is the
point, and a 1998 award with a name, a year and an amount is enough to start a
conversation.

### 0.1 The capability nobody else has

Most organisations lose alumni to stale addresses and give up.

**AFRP has the family tree.** An alumnus whose 2003 address is dead but whose
mother, brother or cousin is a current member in Detroit is *reachable* — not
by better data hygiene, but through their family. No CRM can do that. It is
the single most distinctive thing in this whole platform, and alumni tracing is
where it earns its keep.

### 0.2 The generational loop

The outcome worth designing for:

```
1998  scholar receives an award
2026  reconnects, joins, gives
2029  funds a named scholarship
2031  their child applies
```

That loop is the program's real return, and today nothing in AFRP can even see
it. Every screen below is in service of closing it.

---

## 1. Actors

| Actor | Interest |
|---|---|
| **Scholarship staff / committee** | Load history, resolve identities, run outreach |
| **Alumnus** | Reconnect, claim their record, decide whether to engage |
| **Club officer** | Recognise alumni in their own club; help trace |
| **Federation leadership** | Measure the program's long-run return |
| **Genealogy moderator** | Confirm tree links used for tracing |

---

## 2. Data tiers — load tier 1 for everything and stop

| Tier | Fields | Effort | Recruiting value |
|---|---|---|---|
| **1** | Name, award year, amount, scholarship name | Low | **~90%** |
| 2 | + institution, field of study, graduation year | Medium | Adds segmentation |
| 3 | + applications, scores, committee minutes | High, often unrecoverable | Almost none |

**Tier 1 alone gives the alumni list, the named-award history, and total
program impact.** Tier 3 is worth it only where the paperwork genuinely
survives and someone is writing a history of the program.

**Design consequence:** a historic award must be storable with *no application,
no reviews, no institution, and no contact details.* A record that requires
those fields cannot hold 1998, and a program that waits for perfect data never
loads any.

---

## 3. Use cases

Format: **Actor · Trigger · Preconditions · Main flow · Alternates · Rules · Success**

---

### UC-1 — Import a historic recipient list

**Actor** Scholarship staff · **Trigger** A spreadsheet of past awards surfaces

**Preconditions** File in any tabular format; columns unknown in advance.

**Main flow**
1. Staff upload the file and name the source ("Scholarship binder 1994–2008").
2. System previews rows and proposes a column mapping.
3. Staff correct the mapping; only *name* and *award year* are required.
4. System validates: plausible years, positive amounts, non-empty names.
5. Preview shows what will be created, what will be matched to existing people,
   and what will be flagged.
6. Staff confirm. Rows import as `is_historic`, provisional until reviewed.

**Alternates**
- **A1 Ambiguous columns** — mapping left blank; import proceeds without them.
- **A2 Duplicate rows within the file** — grouped, not silently merged; a person
  with four award years is one alumnus with four records, and that distinction
  matters for the impact number.
- **A3 Unreadable file** — reject with the specific row and column.

**Rules**
- Import is **idempotent** on (source, source row). Re-running a file never
  duplicates.
- Every imported row keeps its **raw original** alongside the parsed version, so
  a mapping mistake is recoverable without going back to the binder.
- Nothing imported is published or contacted until reviewed.

**Success** A decade of awards loaded in an afternoon, with a reviewable
exception list rather than silent failures.

---

### UC-2 — Resolve imported recipients to existing people

**Actor** Scholarship staff · **Trigger** Import completes

**Main flow**
1. System scores each imported name against existing people using the same
   matcher as everywhere else — email, fuzzy name at ≥0.80, DOB, phone, postal.
2. Confident matches (≥0.95) link automatically.
3. The 0.60–0.95 band goes to a review queue showing both records side by side
   with the reasons for the score.
4. Below 0.60, a new person record is created, marked `historic_alumnus`.
5. Staff work the queue: link, create new, or merge.

**Alternates**
- **A1 One name, several candidates** — all shown ranked; staff pick or defer.
  Never auto-picked.
- **A2 Match is wrong** — unlink restores both records; the award returns to the
  queue rather than vanishing.
- **A3 Alumnus is deceased** — linked and marked; excluded from outreach,
  retained for impact.

**Rules**
- **Transliteration matters here more than anywhere.** Khoury/Khouri,
  Yacoub/Yakoub, Mogannam/Muqannam — a 1998 typist and a 2026 database will not
  agree, and the 0.80 fuzzy gate exists for exactly this data.
- A conflicting date of birth **blocks** a match. Same name, different DOB in a
  family is a father and son.
- Every link records who made it and why.

**Success** Most alumni resolved automatically; the ambiguous minority reviewed
by someone who knows the families.

---

### UC-3 — Trace an unreachable alumnus through the family tree

**Actor** Scholarship staff · **Trigger** An alumnus has no usable contact

**Preconditions** The alumnus is linked to a tree person, or their surname and
club suggest a clan.

**Main flow**
1. Staff open the alumnus; system shows **no reachable contact**.
2. System searches the family tree for relatives within 3 degrees who *are*
   contactable members.
3. Results ranked: closest relation, most recently active, same club.
4. Staff choose a **warm-introduction** path — a message to the relative asking
   them to pass it on, never handing over the alumnus's details.
5. Relative forwards; alumnus arrives via a claim link.

**Alternates**
- **A1 No tree link** — offer surname + club search; route to the genealogy
  moderator to establish the link.
- **A2 Relative declines** — recorded; next candidate offered.
- **A3 Alumnus later asks for no contact** — see UC-9; the tree path is closed
  along with everything else.

**Rules**
- **The relative is never given the alumnus's contact details**, and the
  alumnus is never told which relative was asked unless they ask.
- Tracing is logged. "How did you get my number?" must have an answer.
- Deceased relatives are excluded.

**Success** People AFRP would otherwise have written off are reached through
the community that already knows them.

**Why this is the standout capability:** it converts the genealogy from an
archive into an outreach asset, and it is the only thing here a commercial CRM
simply cannot do.

---

### UC-4 — Segment alumni for a campaign

**Actor** Scholarship staff · **Trigger** Planning outreach

**Main flow**
1. Staff filter alumni by award decade, scholarship, club, institution, field,
   graduation, current membership status, giving history, and contactability.
2. System shows the count and a breakdown by segment.
3. Staff save the segment for a campaign.

**Segments that matter**

| Segment | Why |
|---|---|
| **Never a member** | The core recruiting target |
| **Lapsed after their award** | Warmest — they engaged once |
| **Current member, never given** | Giving conversion |
| **Named-scholarship recipient** | Best candidates to fund one themselves |
| **Graduated 15+ years ago** | Peak earning, peak capacity |
| **Has a child aged 15–18** | The generational loop, from the family tree |
| **Unreachable** | Feeds UC-3 |

**Rules**
- Consent is applied **when the segment is built**, not at send time — the
  count shown is the count that can actually be contacted.
- Deceased and no-contact are excluded everywhere, silently and always.

**Success** A staffer can answer "how many 2005–2012 scholars are not members
and are reachable by email?" in one screen.

---

### UC-5 — Run a reconnection campaign

**Actor** Scholarship staff · **Trigger** A segment is ready

**Main flow**
1. Staff choose a template. The strongest is **"here is your record"** — the
   award, the year, the named scholarship, the amount.
2. Each message carries a personal **claim link**.
3. Send, respecting consent and channel preference.
4. Track: opened, claimed, joined, gave.

**Alternates**
- **A1 Bounce** — marked unreachable, routed to UC-3.
- **A2 Wrong person claims** — see UC-8.
- **A3 Reply "please stop"** — UC-9, immediately and permanently.

**Rules**
- **Cold contact after twenty years is a first impression, not a follow-up.**
  Lead with what AFRP did for them, not with an ask. No donation request in the
  first message — that is the difference between a reunion and a solicitation.
- Frequency capped; one campaign per alumnus per quarter.

**Success** Reconnection measured in claims and joins, not opens.

---

### UC-6 — Alumnus claims their record

**Actor** Alumnus · **Trigger** They follow a claim link

**Main flow**
1. Landing page shows **their own scholarship history** — years, amounts,
   named scholarship, and a line on what the program has done since.
2. They confirm identity by matching two facts (award year and institution, or
   date of birth).
3. Account created or linked; contact details updated by them.
4. They set consent per channel.
5. Offered, in this order: **see the program today** → **connect with their
   club** → **join** → **give**.

**Alternates**
- **A1 Details are wrong** — a correction request routed to staff. The record is
  never silently overwritten by an unverified claimant.
- **A2 Cannot verify** — falls back to a staff-reviewed request.
- **A3 Claims a record that is not theirs** — see UC-8.

**Rules**
- Verification is required **before** any personal data beyond their own name
  and award is shown.
- The claim link is single-use and expires.

**Success** The alumnus feels recognised rather than solicited.

---

### UC-7 — Alumnus joins

**Actor** Alumnus · **Trigger** They choose to join after claiming

**Main flow**
1. Tier options, with their club pre-selected from award history or family.
2. Household offered if relatives are already members.
3. Join, pay, receive a digital card.
4. Their scholarship history appears permanently on their member record.

**Rules**
- **Prior scholarship recipients are never charged a joining fee**, if one
  exists. AFRP already invested in them.
- Award history is visible to them and to staff — never in the public directory
  without explicit consent.

**Success** A person who was a line in a 1998 binder is a member of record.

---

### UC-8 — A wrong match or a false claim

**Actor** Staff · **Trigger** A mismatch is suspected

**Main flow**
1. Staff open the alumnus and see the match provenance — score, rule, who
   confirmed it.
2. Unlink. Both records are restored intact.
3. The award returns to the resolution queue.
4. If contact was made under the wrong identity, it is logged and the person is
   told plainly.

**Rules**
- **Unlinking is always possible.** A merge that cannot be undone is a merge
  that should not be automatic.
- No award record is ever deleted by a mismatch; only the link is removed.

**Success** The system recovers from being wrong without losing history — which
matters, because with forty years of transliterated names it *will* be wrong
sometimes.

---

### UC-9 — Alumnus asks not to be contacted

**Actor** Alumnus · **Trigger** Any channel, any time

**Main flow**
1. Request honoured immediately across every channel.
2. Excluded from all segments permanently, not for a cooling-off period.
3. Their award history is **retained** for program impact, with contact
   suppressed.
4. One acknowledgement, then silence.

**Rules**
- Suppression outranks every campaign, template and segment.
- **The family-tree tracing path is closed too.** Reaching someone through their
  cousin after they asked AFRP to stop would be worse than the original
  contact, not a clever workaround.

**Success** Someone who wants to be left alone is left alone, and AFRP keeps
its reputation.

---

### UC-10 — The generational loop

**Actor** Staff · **Trigger** An alumnus has a child of application age

**Main flow**
1. System identifies alumni with children aged 15–18 **from the family tree**.
2. Staff run a targeted campaign about the current cycle.
3. If the child applies, the application shows the parent's award history.
4. **Conflict rules apply.** If the alumnus parent is now on the committee, they
   are blocked from scoring their own child.

**Rules**
- Parental award history is context for the committee, **never a scoring
  factor.** Legacy preference in a needs-based program is a governance problem
  and should be a deliberate board decision, not an accident of a screen layout.

**Success** The loop closes, visibly, with a number attached to it.

---

### UC-11 — Measure the program

**Actor** Federation leadership · **Trigger** Board reporting

**Reported**
- Total awarded, by decade and by named scholarship
- Alumni located, reconnected, joined, giving
- **Conversion from scholar to member** — the number that justifies the program
- Alumni who became donors, and those who funded a named award
- Second-generation applicants
- Cost per reconnection

**Success** "What did forty years of scholarships do for AFRP?" has an answer
with evidence behind it.

---

## 4. Screens

### Staff (desktop)
1. Import wizard — upload, map, validate, preview
2. Match review — side-by-side, scored, with reasons
3. Alumnus record — awards, match provenance, contactability, tree links
4. Family-tree tracing — relatives ranked, warm-introduction request
5. Segment builder — filters, counts, consent-aware
6. Campaign — template, audience, tracking
7. Program impact — the board view

### Alumnus (mobile)
8. Claim landing — "we funded your education"
9. Verify identity
10. Their scholarship history
11. The program today
12. Join
13. Give back / fund a named award
14. Mentor or volunteer

---

## 5. Risks

| Risk | Mitigation |
|---|---|
| **Wrong-person outreach** after decades of drift | Conservative auto-match, human review band, always-reversible links |
| **It reads as a fundraising trawl** | Lead with recognition; no ask in the first contact |
| Historic data too thin to match | Tier 1 is enough to start; tracing does the rest |
| Reaching people through relatives feels intrusive | Never share contact details; log everything; suppression closes this path too |
| Deceased alumni contacted | Explicit flag; excluded everywhere |
| Effort spent on unreachable records | Cap tracing attempts; measure cost per reconnection |

---

## 6. Open questions

1. **How far back does the paperwork go, and in what form?** Determines tier 1 volume.
2. **Roughly how many recipients, total?** Changes whether match review is an afternoon or a project.
3. **Is there any existing alumni contact list**, however informal?
4. **Who reviews the match queue?** It needs someone who knows the families — this is not a data-entry job.
5. **Is a joining-fee waiver for alumni acceptable** to the board?
6. **Should award history appear in the member directory** if the alumnus consents?
7. **Is legacy status ever a factor in current scholarship decisions?** Currently modelled as context only, deliberately.

---

*Design only. No implementation in this deliverable.*
