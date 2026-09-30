# My AFRP portal — mobile UX review

**Source:** screenshots of `my.afrp.org` on iOS, August 2026
**Scope:** what is observable in the screenshots. Not a full audit.

> **Note on data:** the screenshots contain real member names, emails, phone
> numbers, birth dates, an address, and card metadata. None of it is reproduced
> here. If these screenshots get shared with vendors or a board, redact them
> first — several show a minor's full name and date of birth.

---

## First, a correction to my earlier documents

Two things I previously reported were wrong, and both mattered.

**1. Payments are Authorize.Net, not Square.** I claimed Square based on 14
occurrences of the string "square" in the donations page HTML. Every one of
them was the Astra WordPress theme's CSS class `.square .posted-on`. Members
manage saved cards through Authorize.Net, and the "My Subscriptions" screen
indicates Automated Recurring Billing is in use. All Square references in the
architecture, schema, and seed data have been replaced.

**2. The portal is more complete than I said.** I reported events, club
details, and transaction history as missing, based on unauthenticated URL
probes returning 404. Those probes were unreliable — the pages exist behind
login at slugs I did not guess. The app's own tile grid is the authoritative
module list:

> Donations · Transaction History · Manage My Household · Become a Member ·
> Event Registration · Local Club Details · Hathihe Ramallah Magazine ·
> Hathihe Ramallah Online · Publications · AFRP Digital Store ·
> My Subscriptions · My Payment Methods

**This changes the diagnosis.** The problem is not missing modules. It is that
a capable Dynamics/Power Pages portal is delivering a poor experience on
phones, and its household model actively fights how families work. That is a
better problem to have and a cheaper one to fix.

---

## What this actually is

Not a native app. It is `my.afrp.org` — the Power Pages portal — in a mobile
browser. Tells: `Home > Profile` breadcrumbs, a hamburger menu, browser-chrome
overlap, and desktop form layouts that have not reflowed.

This matters for planning: **the fastest win is not building a native app. It
is making the existing portal work on a phone.** That is CSS and form layout
work measured in weeks, not a mobile build measured in months. The native app
still earns its place later — offline member card, push, convention QR check-in
— but it should not be the first thing funded.

---

## Defects

Severity: **P1** blocks or actively loses data · **P2** significant friction ·
**P3** polish.

### P1 — Form fields overflow the viewport

On the profile address form, the input fields extend past the right edge of the
screen. Line 1, City, State, and ZIP are all cut off, and there is a horizontal
scrollbar. On the "How may we contact you?" section the heading text is clipped
mid-word.

Members cannot see what they are typing into their own address. This is the
single worst defect in the set, and it sits on the form most likely to be
edited by the oldest members.

**Fix:** the form container has a fixed width or a min-width wider than the
viewport. Constrain to `max-width: 100%` and let inputs be fluid. Hours, not days.

### P1 — Household model ejects adult children

The Manage Household page states:

> "Only couples and their children under the age of 18 should be added to the
> household. All young adults (18+) must be in their own household, even if
> they still live in the same physical home."

The screenshots show a household containing a 22-year-old, a 20-year-old, and a
15-year-old. Per the stated rule, two of those three should not be there.

This is not a copy problem. The model conflates three different things:

| Question | Type of fact |
|---|---|
| Who lives together? | address |
| Who may register/pay/consent for whom? | authority |
| Who does a family membership cover? | benefit |

Because they are one field, a member is silently ejected from their family on
their eighteenth birthday and a parent loses the ability to register them —
while everyone still lives in the same house. In this community, parents
routinely register adult children for convention. The system says no.

**Fix:** separate authority from membership. Age sets the *default*; an
explicit, revocable grant sets the *rule*. Implemented and tested in the
backend prototype (`src/households/rules.ts`, 14 tests) — including the case
the current portal cannot express: an adult child delegating to a parent.

### P1 — No consent record for SMS

The SMS signup is a marketing panel: *"Add your cell phone to your profile to
receive instant text alerts… Click here to add or update your number now!"*

Adding a phone number to a profile is not consent to be texted. There is no
visible capture of when consent was given, what wording was shown, or from
where. TCPA statutory damages run $500–$1,500 **per message**, and a convention
blast to a few thousand members is not a small number.

**Fix:** an explicit opt-in checkbox with retained evidence. Modelled as
`contact_consent` in the prototype — channel, granted, source, wording version,
IP, timestamp.

### P2 — Header overlaps the status bar

On several screens the page title renders underneath the iOS status bar —
"Manage Payment Methods" collides with the clock, and elsewhere an "Update"
button is clipped at the top. Safe-area insets are not being respected.

**Fix:** `viewport-fit=cover` plus `env(safe-area-inset-top)` padding.

### P2 — Tile grid is cut off on the right

The home tile grid renders two columns, but the right column is clipped —
"Become a Member", "Local Club Details", "Hathihe Ramallah Online" and "AFRP
Digital Store" all lose their right edge. Same root cause as the form overflow.

### P2 — "Fax" is offered as a contact preference

The contact preferences are Email, Fax, Phone, Mail — all four checked by
default. Fax is a Dynamics 365 default field, not an AFRP decision. It makes
the org look dated to exactly the younger members it is trying to recruit, and
**there is no SMS option** despite SMS being actively promoted elsewhere in the
same app.

**Fix:** remove Fax, add SMS, and stop defaulting everything to checked —
pre-checked consent is not consent.

### P2 — Household invitation flow is too long

Adding a family member takes: fill their details → they receive an email → they
claim the account → *or* you open a red dropdown → Send Invitation → but only
if they have never registered → and an email address is mandatory → and if
there is no email you must first add one via "View Details" in the same
dropdown.

That is at least six steps with three conditional branches, explained in a wall
of prose. The instructions being that long is itself the evidence.

**Fix:** one flow. Add member → optionally invite → system decides whether
that means a claim link or an account link. Do not make the member run the
decision tree.

### P3 — Inconsistent typography and empty labels

Font sizes vary widely between screens; some headings render far larger than
others. The Publications tile shows an icon with its label pushed to the
bottom, misaligned against neighbours. Household cards show "Cell Phone" with
an empty value rather than hiding the row.

### P3 — Payment screen is visibly a third-party embed

"Manage Payment Methods" is styled differently from the rest of the app —
serif-ish labels, blue links, a "POWERED BY Authorize.Net" bar. Functionally
fine and arguably good for trust, but it reads as leaving the app.

---

## What is working

Worth saying, because a defect list reads bleaker than the product is:

- Saved cards, subscriptions, and transaction history all exist and work.
  That is real membership infrastructure many peer organisations lack.
- The household concept exists at all — the model is wrong, not absent.
- Federated login (Google/Microsoft/Facebook) is already configured.
- The module set is broad: donations, events, clubs, store, publications.
- Someone has clearly thought about the member journey. The problems are
  layout and data-model, not neglect.

---

## Recommended sequence

| Priority | Work | Effort | Why first |
|---|---|---|---|
| 1 | Fix mobile overflow: forms, tile grid, safe areas | 1–2 wk | Members cannot read their own address. Cheapest, most visible win available |
| 2 | Add SMS consent capture with evidence | 1 wk | Legal exposure, and it is small |
| 3 | Remove Fax, add SMS, stop pre-checking consent | 2 days | Trivial, embarrassing to leave |
| 4 | Redesign household: separate authority from membership | 3–4 wk | Structural. Design in the prototype; needs a Dynamics data-model change |
| 5 | Simplify the invitation flow | 1–2 wk | Depends on 4 |
| 6 | Expiring-card notifications | 3 days | Silent auto-renew failure; the query already exists |

**Items 1–3 are roughly three weeks of work** and would materially change how
the portal feels, with no new platform, no migration, and no vendor change.
That is the argument to make to the board before asking for anything larger.

The native app, the family tree, and the Breeze integration all remain worth
building. None of them should jump this queue.

---

*Based on screenshots supplied 15 August 2026 plus public inspection of
afrp.org and my.afrp.org. Nothing here required authenticated access.*
