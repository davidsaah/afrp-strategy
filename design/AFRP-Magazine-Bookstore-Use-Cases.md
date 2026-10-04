# Hathihe Ramallah + the bookstore
### Use cases and flows

**Date:** August 2026
**Mode:** design only — mockups and use cases, no buildout.

> *Since 2 October 2026:* how the Magazine and the Bookstore actually run is in **P24** (`AFRP-Magazine-Operations.md`, MG1–MG7). P24 covers the issue cycle as run (six issues a year), announcements as they arrive (the correspondent and the editor as assisted doors; obituaries as paid placements), the staff and the absent 6.7.1 board, the subscriber ledger, the Magazine's money, the back-issue register, the **two live stores** (a shop on afrp.org and the "Digital Store" on the CRM's portal), and the Cook Book. Where this note and practice differ, the passages below are kept and carry a dated pointer: the cadence (§0, §1), obituaries (UC-2; Q-193), the product lines and member price (UC-9; Q-199), and cook book sales as ARFECF income (UC-11; Q-197). The digital issue and back issues are Q-196.

---

## 0. The magazine is the forcing function

Nobody updates a membership database for its own sake.

Everybody wants their daughter's wedding in the magazine.

```
copy deadline  →  members want to appear  →  members record their events
                        ↓
              the data gets current, by itself
                        ↓
        better segmentation · better outreach · better everything
```

**This is the most valuable idea in the whole platform, and it costs nothing to
build.** Every other data-quality initiative AFRP could run — email campaigns
asking people to update their profile, staff phoning members, a form on the
website — competes for attention against everything else in a member's life.
The magazine doesn't compete. It creates its own demand, three times a year (*six in practice; P24 §2*), on
a schedule, because the alternative is not being in it.

**The design consequence, and it is not optional:** every printed section must
be generated from the live system, never assembled by hand in a document. The
moment an editor accepts a wedding notice by email, the loop breaks and the
magazine stops improving the data.

---

## 1. Decisions this design assumes

| Decision | Consequence |
|---|---|
| **Manar and Patron are membership tiers** | Recognition lists come from active memberships at a cut-off date, not from the ledger. Straightforward — but see UC-3 on name handling |
| **Print and digital, a few issues a year** (*six in practice; P24 §2*) | Hard deadlines. Copy freeze, proof, press, mail. The hard deadline is exactly what makes the forcing function work |
| **Professional listings sold by subscription** | Recurring revenue, no artwork production, and it doubles as the RBPN directory. **This is ASC 606 exchange revenue, not a contribution** |
| **Bookstore ships physical goods** | Inventory, shipping, and sales tax. See §5 — the tax position is the part most likely to be got wrong |

---

## 2. Issue lifecycle

```
plan  →  window opens  →  COPY FREEZE  →  edit  →  proof  →  press  →  mail + publish  →  archive
```

**The freeze is the mechanic that makes everything else work.** At the copy
deadline, every auto-generated section is snapshotted and stored with the
issue. Late submissions roll to the next issue automatically.

Same pattern as the ballot electorate, for the same reason: without a freeze,
"why wasn't my baby in issue 47?" has no answer, and the recognition list
silently changes between proof and press.

| Milestone | What happens |
|---|---|
| Window opens | Members can submit life events for this issue |
| **Copy freeze** | Sections snapshotted. Listings must be paid. Nothing further enters |
| Proof | Members can correct their **own** entries; nothing new is added |
| Press | Print file locked |
| Publish | Digital issue live, mail run generated, archive entry created |

---

## 3. Use cases — the magazine

Format: **Actor · Trigger · Main flow · Alternates · Rules · Success**

---

### UC-1 — Plan an issue

**Actor** Editor · **Trigger** Publication calendar

**Main flow**
1. Editor creates the issue: volume, number, season, page budget.
2. Sets the content window (life events between date A and date B), copy
   freeze, proof, press and mail dates.
3. Enables the five auto sections and sets a page allowance for each.
4. System projects section sizes from current data and warns if the projection
   exceeds the page budget.

**Rules**
- Content window and freeze cannot overlap the previous issue's window — an
  event appears in exactly one issue.
- Press date drives every upstream deadline; moving it moves them all.

**Success** The editor can see, weeks ahead, roughly how many pages the
automatic content will consume.

---

### UC-2 — Life events section (weddings, births, graduations, deaths)

*Since 2 October 2026:* in practice obituaries are family-submitted **paid placements** with a tribute. P24 §3.3 keeps the death as a life event under R34's family-approval gate and adds a placement order whose fee is held unposted until Q-193 is answered. Graduations are already a standing type, an announcement on the member's record (P24 §3.1). Submissions come through a city correspondent or the editor as pending assisted submissions (P24 §3.2; Q-195).

**Actor** System, editor · **Trigger** Copy freeze

**Main flow**
1. System collects every life event with `occurred_on` inside the window,
   status **verified**, and publication consent granted.
2. Groups by type; sorts by date.
3. Editor reviews, reorders, trims to the page allowance.
4. Section is frozen into the issue.

**Alternates**
- **A1 Unverified event** — excluded, listed in an exceptions report so the
  editor can chase it before freeze.
- **A2 Consent missing** — excluded. The member is prompted once during the
  window, never after freeze.
- **A3 Over the page allowance** — editor trims; trimmed entries are **flagged
  for the next issue**, not discarded.

**Rules**
- **Deaths are never auto-published.** They require explicit family approval,
  recorded against a named family contact. This is already a rule in the
  life-events engine and it applies here without exception.
- **Births name a minor.** Parental consent required; photo consent is separate
  and defaults off.
- **Graduations** are a new life-event type: institution, degree, year. For
  scholarship recipients, the award history can be shown *if they consent* —
  which is also a quiet recruiting moment.
- Every entry traces back to a life-event record. Nothing is typed straight
  into the magazine.

**Success** The section that members care most about assembles itself, and
appearing in it requires them to have told the system.

---

### UC-3 — Recognition list (active Manar and Patron members)

**Actor** System, editor · **Trigger** Copy freeze

**Main flow**
1. System lists members whose **national membership is active at the freeze
   date** and whose tier is Manar or Patron.
2. Names rendered using each member's **preferred display name**.
3. Grouped by tier, sorted by surname within tier.
4. Members with listing consent withheld are excluded silently.

**Rules — this section is where organisations embarrass themselves**

| Hazard | Handling |
|---|---|
| Misspelled or wrongly transliterated name | `preferred_display_name` on the person, set by them, never derived |
| A member who died since the last issue | Deceased flag excludes from the living list; a separate memoriam section |
| Someone who asked to be anonymous | Listing consent is per-member and honoured absolutely |
| Couples listed separately or wrongly joined | Household display preference: joint, separate, or one name only |
| Titles and maiden names | Part of preferred display name, not computed |

**The proof-and-confirm step (UC-4) exists entirely because of this table.**

**Success** The list is right, and when it is wrong it is wrong in a way the
member already had the chance to fix.

---

### UC-4 — Proof and confirm your own listing

**Actor** Member · **Trigger** Two weeks before copy freeze

**Main flow**
1. Every member due to appear — recognition, life event, professional listing —
   receives a link showing **exactly how they will appear in print**.
2. They confirm, correct the wording, or withdraw.
3. Corrections apply to their own entry only and are logged.
4. Unconfirmed entries still publish as generated; silence is not withdrawal.

**Rules**
- A member may always **withdraw** their own entry, up to the freeze.
- Corrections after freeze roll to the next issue — the print file is closed.

**Success** Complaints about the magazine drop to near zero, because everyone
who appears was shown their entry first.

**Why this earns its build cost:** it converts the single most common source of
member irritation into a moment of engagement — and it is another reason to
open the app.

---

### UC-5 — Professional directory section

**Actor** System, editor · **Trigger** Copy freeze

**Main flow**
1. System lists RBPN listings with a **paid, current subscription** at freeze.
2. Renders by tier — basic (name, profession, city), enhanced (+ company,
   contact), premium (+ logo, description).
3. Grouped by industry, then region.
4. Editor reviews; section frozen.

**Alternates**
- **A1 Subscription lapses before freeze** — excluded, and the member is warned
  at 30 and 7 days. Losing your listing because you forgot to renew is a
  support call nobody wants.
- **A2 Paid after freeze** — appears in the next issue; not backdated.

**Rules**
- Listing revenue is **exchange revenue (ASC 606)** — the member receives
  advertising value. It is not a contribution and must not be receipted as one.
- The printed section and the online directory come from **one record**. They
  cannot drift.
- Contact details appear only at the tier the member paid for.

**Success** A revenue line that also produces a member benefit, with no
artwork production and no separate sales pipeline.

---

### UC-6 — Family tree highlight

**Actor** Editor, genealogy moderator · **Trigger** Issue planning

**Main flow**
1. System suggests candidates: a clan with a documentation milestone, a newly
   reconciled line, a notable anniversary, a lineage with new provisional
   records now confirmed.
2. Editor picks one; moderator confirms the genealogy is canonical.
3. Editor writes the narrative; the system generates the lineage diagram.
4. Living individuals are **restricted by default** in the printed diagram.

**Rules**
- Only **canonical** tree records appear. Provisional records — anything
  submitted but not yet moderated — never reach print.
- Living people appear only with consent; names without dates by default.

**Success** The archive becomes a recurring editorial feature rather than a
thing people mean to look at one day.

---

### UC-7 — Upcoming activities

**Actor** System · **Trigger** Copy freeze

**Main flow**
1. System lists published events starting **after the mail date** whose
   registration is still open at the time readers receive the issue.
2. National and club events, grouped by month.
3. Each entry carries a short code or QR to register.

**Rules**
- **Nothing prints that will be over or closed before the reader sees it.** The
  filter uses the *mail* date plus a delivery allowance, not the freeze date —
  otherwise the magazine advertises events nobody can attend, which trains
  people to ignore the section.
- Registration links are trackable, so the magazine's contribution to
  attendance is measurable.

**Success** The magazine drives registrations, and AFRP can prove it did.

---

### UC-8 — Publish and archive

**Actor** Editor · **Trigger** Press

**Main flow**
1. Print file locked; mail run generated from current addresses.
2. Digital issue published to members; back issues open per policy.
3. Issue added to the **searchable archive** — full text, per-section.
4. Frozen sections retained exactly as printed.

**Rules**
- The archive stores what was **printed**, not what the data says today. A 2019
  recognition list must still show 2019's members.
- Mailing labels come from live addresses at the mail date — the only section
  that is deliberately not frozen.

**Success** Forty years of back issues become searchable, and the magazine
stops being the only thing AFRP cannot query.

---

## 4. Use cases — the bookstore

---

### UC-9 — Browse and buy

*Since 2 October 2026:* neither live store has back issues, clan books, merchandise, downloads or a member price. Both are US-only and show no stock (P24 §8.1). Which product lines and whether a member price exist is Q-199; the owner of the bookstore is Q-197; sales tax registration is Q-198. P24 §8 reconciles the Hub's catalogue with the two stores (MG7).

**Actor** Member or public · **Trigger** Shop link, or a magazine mention

**Main flow**
1. Catalogue: books, magazine back issues, clan books, merchandise, digital
   downloads.
2. **Member pricing** applied automatically when signed in.
3. Cart, address, shipping option.
4. **Sales tax calculated by destination** — see §5.
5. Pay via Authorize.Net.
6. Physical orders queue for fulfilment; digital delivered immediately as an
   entitlement on the member record.

**Rules**
- Digital goods are **entitlements, not files** — re-downloadable, revocable,
  never a dead link in an old email.
- Stock is decremented at payment, not at cart. Overselling a print run of
  clan books is a real risk.
- Order confirmation states clearly which lines are taxable and why.

---

### UC-10 — Fulfilment

**Actor** Staff or volunteer · **Trigger** Paid physical order

**Main flow**
1. Pick list grouped by item.
2. Packing slip; no card details anywhere on it.
3. Mark shipped with tracking; member notified.

**Alternates**
- **A1 Out of stock** — hold and notify, or refund the line. Never silently drop.
- **A2 Undeliverable** — returned to stock; address flagged, which also
  improves the magazine mailing list.

---

### UC-11 — Revenue to the ledger

*Since 2 October 2026:* in practice cook book sales are income of the Cook Book fund, which is ARFECF's on D55's evidence (P24 §9; Q-173, Q-197); on the platform nothing posts to or from the fund until its kind and governing text are set (P9 rule 1; P26 §6.2). Each title's holding entity is a row, and orders split by entity are never netted (P24 §8.2). The afrp.org cook book page carries "tax-deductible" donation text. That is practice to correct: a purchase is not a gift (this UC; P24 rule 13).

**Actor** System · **Trigger** Daily close

**Main flow**
1. Bookstore sales post as **exchange revenue (ASC 606)** — not contributions.
2. Sales tax collected posts to a **liability**, never revenue. It is the
   state's money held in trust.
3. Shipping charged posts separately from goods.
4. Fees booked gross, as everywhere else.

**Rules**
- **A donation and a purchase are different transactions** and must never be
  combined in one receipt. A member buying a $40 book has made no charitable
  contribution, and a receipt implying otherwise is a real problem.

---

## 5. Sales tax — assessed, as requested

### 5.1 The misconception worth correcting first

**Being a 501(c)(3) does not exempt AFRP from collecting sales tax on what it
sells.** Most states require nonprofits making retail sales to charge sales tax
exactly like any other seller. Exemption from *paying* tax on purchases is a
different thing entirely, granted separately, and it is the one people assume
covers both.

### 5.2 Where AFRP actually stands

| Kind of nexus | AFRP's position |
|---|---|
| **Physical (home state)** | **Certain.** AFRP is based in Michigan and must register and collect there from the first sale |
| **Economic (other states)** | **Unlikely at first, but must be watched.** Most states use $100,000 in annual sales; about half also count 200 transactions. California, Texas and New York are higher — $500,000 in several |

**The realistic assessment:** a community bookstore selling books and back
issues to members across 18 states is very unlikely to cross $100,000 in any
single other state. The threshold that could plausibly bite is the
**200-transaction count** in a state with a large, active club — dollar value
low, order count high.

### 5.3 The proportionate design

*Since 2 October 2026:* this is the note's proportionate design, not a decision. Whether the Federation is registered to collect sales tax anywhere is unconfirmed (Q-198).

**Do not register in 18 states on day one.** That is months of work and ongoing
filings for an obligation that probably does not exist.

Instead:

1. Register and collect in **Michigan** only.
2. **Track cumulative sales and order counts by destination state**, continuously.
3. **Alert at 75% of each state's threshold**, with enough lead time to register
   before crossing it.
4. Use a **tax rate service** rather than hand-maintaining rates. Rates change
   constantly and by locality, not just by state.
5. Keep a **taxability flag per product** — many states treat digital goods
   differently from physical, and some exempt books.

That converts an open-ended compliance problem into one registration plus a
monitor.

### 5.4 What needs a professional

- Michigan's treatment of nonprofit retail sales and any occasional-sale or
  fundraising exemption.
- Whether digital downloads are taxable in the states AFRP sells to.
- Whether magazine subscriptions or listing fees are taxable anywhere relevant.

These belong in the same conversation as the other adviser questions — one more
section on an existing brief, not a new engagement.

---

## 6. Screens

### Editorial and commerce (desktop)
1. Issue plan — milestones, page budget, section projections
2. Life events section builder — with the exceptions report
3. Recognition list — with the name-handling controls
4. Proof-and-confirm tracker — who has confirmed, who has not
5. Professional listings pipeline — subscriptions, renewals, lapses
6. Family tree highlight picker
7. Upcoming activities — with the mail-date filter
8. Bookstore catalogue and inventory
9. Order fulfilment
10. **Sales tax nexus monitor** — cumulative by state against thresholds

### Member (mobile)
11. Submit a life event
12. Confirm how you will appear in print
13. Manage your professional listing
14. Read the current issue / search the archive
15. Shop and checkout
16. Your digital library

---

## 7. Risks

| Risk | Mitigation |
|---|---|
| **The loop breaks** — an editor accepts a notice by email | Policy plus product: no manual entry path into an auto section |
| A recognition list error | Proof-and-confirm; preferred display names |
| A death published without family approval | Hard rule, no override in the UI |
| A listing lapses and the member is upset | 30- and 7-day warnings tied to the freeze date, not the renewal date |
| Sales tax under-collected | Home-state registration plus a threshold monitor |
| Overselling limited print runs | Stock decremented at payment |
| The archive drifts from what was printed | Sections frozen at press and never regenerated |

---

## 8. Open questions

1. **How many issues a year, and what are the real deadlines?** Everything keys off the press date.
2. **What page budget** does each auto section get?
3. **Listing tiers and prices** for the professional directory?
4. **Who is the editor** — staff, a volunteer committee, or a contractor? Determines how much editorial control the tool needs.
5. **Are back issues open to non-members**, or a member benefit?
6. **What is actually in the bookstore today**, and what stock exists?
7. **Is there a fulfilment volunteer**, or should print-on-demand be considered? It removes inventory and much of the tax problem at once.
8. **Should graduation announcements be added as a life-event type now?** It is new, and it is the one most likely to surface scholarship alumni.

---

*Sales tax positions from published guidance on post-*Wayfair* economic nexus
and nonprofit collection obligations, August 2026. Thresholds change; verify
against current state rules before relying on any figure here.*

**Sources:** [State-by-state economic nexus thresholds (Wolters Kluwer)](https://www.wolterskluwer.com/en/expert-insights/state-by-state-economic-nexus-thresholds-under-state-sales-tax-laws) ·
[What nonprofits need to know about sales tax (TaxJar)](https://www.taxjar.com/blog/nonprofits) ·
[Nonprofits and sales tax (Avalara)](https://www.avalara.com/us/en/learn/whitepapers/nonprofits-and-sales-tax.html)
