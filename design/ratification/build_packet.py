#!/usr/bin/env python3
"""Assemble the R6 ratification packet page on the AFRP design system."""
from pathlib import Path

CSS = Path("/home/claude/afrp_system.css").read_text(encoding="utf-8")
SPRITE = Path("/home/claude/afrp_sprite.svg").read_text(encoding="utf-8")

OVERLAY = """
/* ── packet overlay — a document, not a dashboard ──────────────────────── */
.pk{max-width:860px;margin:0 auto;padding:var(--s5) var(--gutter) 72px}
.pk .panel{margin-bottom:var(--s5)}
.pk .page-head{display:block}
.pk .page-head .ph-ico{margin-bottom:var(--s3)}
.pk .page-head h1{max-width:none;margin-bottom:6px}
.pk p{max-width:66ch}
.lede{font-size:var(--fs-lg);line-height:1.55;color:var(--ink-1)}
.routing{display:grid;gap:var(--s4);grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin:0}
.route{display:flex;flex-direction:column;gap:6px;padding:var(--s4);border:1px solid var(--line);
  border-radius:var(--r2);background:var(--surface-2);text-decoration:none;color:inherit}
.route:hover{border-color:var(--accent);}
.route__ic{width:26px;height:26px;color:var(--accent)}
.route__who{font-weight:700;font-size:var(--fs-md)}
.route__owns{font-size:var(--fs-sm);color:var(--ink-2);line-height:1.45}
.memo{scroll-margin-top:16px}
.memo__head{display:flex;align-items:flex-start;gap:var(--s3)}
.memo__ic{flex:0 0 auto;width:34px;height:34px;color:var(--accent);margin-top:2px}
.q{border-left:3px solid var(--line-2);padding:0 0 0 var(--s4);margin:var(--s5) 0}
.q__n{font-size:var(--fs-micro);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:700}
.q__t{font-size:var(--fs-lg);margin:2px 0 var(--s3);font-weight:700;text-wrap:balance}
.prop{background:var(--surface-2);border:1px solid var(--line);border-radius:var(--r2);
  padding:var(--s4);margin:var(--s4) 0}
.prop__k{font-size:var(--fs-micro);letter-spacing:.08em;text-transform:uppercase;
  color:var(--ink-3);font-weight:700;margin-bottom:6px}
.choices{display:flex;flex-direction:column;gap:8px;margin:var(--s4) 0 0}
.choice{display:flex;align-items:flex-start;gap:10px;font-size:var(--fs-sm)}
.box{flex:0 0 auto;width:15px;height:15px;border:1.5px solid var(--ink-3);border-radius:3px;margin-top:2px}
.box--on{border-color:var(--green-700);background:var(--green-700);position:relative}
.box--on::after{content:"";position:absolute;left:4px;top:1px;width:4px;height:8px;
  border:solid #fff;border-width:0 2px 2px 0;transform:rotate(42deg)}
.choice--on{font-weight:700;color:var(--ink-0)}
.choice--off{color:var(--ink-3)}
.fill{display:inline-block;min-width:150px;border-bottom:1px solid var(--line-2);margin-left:4px}
.retn{display:flex;flex-wrap:wrap;gap:var(--s4);align-items:baseline;
  font-size:var(--fs-sm);color:var(--ink-2)}
.verdict.why{margin-top:var(--s3)}
.tzrule{height:8px;margin:var(--s6) 0;opacity:.5}
blockquote.rec{margin:var(--s4) 0;padding:var(--s3) var(--s4);border-left:3px solid var(--accent);
  background:var(--surface-2);font-style:italic;color:var(--ink-1)}
blockquote.rec p{margin:0}
.foot-note{font-size:var(--fs-sm);color:var(--ink-2);line-height:1.55}
@media print{
  .topbar,.pk .noprint{display:none!important}
  .pk{max-width:none;padding:0}
  .panel{break-inside:avoid;box-shadow:none}
  .memo{break-before:page}
  a{text-decoration:none;color:inherit}
}
"""

MEMBERSHIP = """
<section class="memo" id="membership">
  <div class="panel">
    <div class="panel__head">
      <div class="memo__head">
        <svg class="memo__ic" aria-hidden="true"><use href="#i-people"/></svg>
        <div>
          <h2 style="margin:0">Membership Committee</h2>
          <div class="tiny" style="color:var(--ink-2)">The power set, and a minor who belongs to two households</div>
        </div>
      </div>
      <span class="c-pill c-pill--ok">ratified as drafted</span>
    </div>
    <div class="panel__body">
      <p>The platform has never held a stated rule for <b>who may act for a minor</b> &mdash;
      enrol them in a programme, pay for them, answer a consent question on their behalf. The
      rule was being <i>inferred</i> from how the software needed to behave, which is the
      platform legislating for families. Three pieces of work were stopped rather than built
      on an inferred rule about children.</p>
      <p>A document now states it, and four authority paths are settled: <b>a parent by
      household membership, a named guardian, either of two parents when separated, and a
      per-event delegate identified at event setup.</b> Two questions in it are yours.</p>

      <div class="q">
        <div class="q__n">Question 1</div>
        <div class="q__t">Is the power set right?</div>
        <p>The document treats &ldquo;act for&rdquo; not as one permission but as <b>seven named
        powers</b>, so that a parent and a chaperone on a day trip are not handed the same thing.
        A parent, a named guardian and either separated parent hold all seven. A per-event
        delegate holds <b>supervise only</b>, plus release or emergency where a parent has
        specifically named them for that event.</p>
        <div class="c-table-wrap">
          <table class="c-table">
            <thead><tr><th>Power</th><th>Permits</th><th>Event delegate</th></tr></thead>
            <tbody>
              <tr><td class="mono">see</td><td>View the minor&rsquo;s record</td><td><span class="c-pill c-pill--muted">no</span></td></tr>
              <tr><td class="mono">enrol</td><td>Register them for an event or programme</td><td><span class="c-pill c-pill--muted">no</span></td></tr>
              <tr><td class="mono">transact</td><td>Pay dues, fees or camperships for them</td><td><span class="c-pill c-pill--muted">no</span></td></tr>
              <tr><td class="mono">consent</td><td>Give or withdraw consent held for the minor</td><td><span class="c-pill c-pill--muted">no</span></td></tr>
              <tr><td class="mono">supervise</td><td>On-site responsibility during a named event</td><td><span class="c-pill c-pill--ok">yes</span></td></tr>
              <tr><td class="mono">release</td><td>Collect the minor, or authorise their departure</td><td><span class="c-pill c-pill--info">only if named</span></td></tr>
              <tr><td class="mono">emergency</td><td>Authorise treatment when no parent is reachable</td><td><span class="c-pill c-pill--info">only if named</span></td></tr>
            </tbody>
          </table>
        </div>
        <div class="prop">
          <div class="prop__k">The decision</div>
          <p style="margin:0">Is that division right &mdash; and in particular, should a per-event
          delegate ever be able to <i>see</i> a child&rsquo;s record or <i>enrol</i> them in
          something else? The document says no. That is the conservative reading, and the one
          the platform will enforce unless you say otherwise.</p>
        </div>
        <div class="choices">
          <div class="choice"><span class="box"></span><span>Approve as drafted</span></div>
          <div class="choice"><span class="box"></span><span>Approve with changes:<span class="fill"></span></span></div>
          <div class="choice"><span class="box"></span><span>Refer back</span></div>
        </div>
      </div>

      <div class="q">
        <div class="q__n">Question 2</div>
        <div class="q__t">A minor who belongs to two households</div>
        <p>Recorded in the platform&rsquo;s open-question register, verbatim:</p>
        <blockquote class="rec"><p>After a remarriage a minor belongs to two households with
        different clubs, different directory choices and different pickup authority.
        <b>By-Law 4.3.1 says nothing about minors in two households.</b></p></blockquote>
        <p>The question has three separable halves, and two are answered without needing you:</p>
        <ul>
          <li><b>Pickup</b> does not follow from household membership at all. It runs through a
          list a parent or guardian writes; both households&rsquo; parents can write to it.</li>
          <li><b>Directory visibility</b> resolves to the more protective of the two households&rsquo;
          settings wherever they differ. Minors are already excluded from every directory listing,
          so this is a narrow question of household-level display.</li>
        </ul>
        <div class="prop">
          <div class="prop__k">The half that is yours</div>
          <p style="margin:0"><b>Which club is the minor attached to?</b> That carries dues and,
          eventually, franchise consequences, and By-Law 4.3.1 is silent. Pending your decision
          the platform <b>holds both attachments and flags the person as an open question</b>
          rather than picking one &mdash; a silent pick would quietly move a child&rsquo;s dues
          and eventual vote from one club to another.</p>
        </div>
        <div class="choices">
          <div class="choice"><span class="box"></span><span>Hold both and flag, as now</span></div>
          <div class="choice"><span class="box"></span><span>Attach to:<span class="fill"></span></span></div>
          <div class="choice"><span class="box"></span><span>Refer to the Board</span></div>
        </div>
      </div>
    </div>
    <div class="panel__foot retn">
      <span><b>Returned by</b><span class="fill"></span></span>
      <span><b>Date</b><span class="fill"></span></span>
    </div>
  </div>
</section>
"""

CAMP = """
<section class="memo" id="camp">
  <div class="panel">
    <div class="panel__head">
      <div class="memo__head">
        <svg class="memo__ic" aria-hidden="true"><use href="#i-tent"/></svg>
        <div>
          <h2 style="margin:0">Camp Ramallah</h2>
          <div class="tiny" style="color:var(--ink-2)">Supervision, the pickup list, and a court-appointed guardian</div>
        </div>
      </div>
      <span class="c-pill c-pill--ok">ratified as drafted</span>
    </div>
    <div class="panel__body">
      <p>The camp screens &mdash; parent application, selection console, roster, camperships &mdash;
      are being built now. They need a stated rule for <b>who may act for a child</b>, and until
      this week the platform had none: it was inferring one, which is not something to infer about
      children. The parts that touch camp operations are yours to confirm, because you are the
      ones who run the gate at pickup time.</p>

      <div class="q">
        <div class="q__n">Question 1</div>
        <div class="q__t">The line between supervising a child and releasing one</div>
        <p>The document splits these deliberately, because they are not the same authority.</p>
        <div class="prop">
          <div class="prop__k">Supervising is designated by AFRP</div>
          <p style="margin:0">When you set up a session or a trip, you name the adults responsible
          &mdash; staff, chaperones, screened volunteers. Parents are <b>told</b> who those adults
          are, on the registration surface, before the event. They do not approve the list.
          Supervision is AFRP discharging its own duty of care, not a parent lending out their
          authority.</p>
        </div>
        <div class="prop">
          <div class="prop__k">Releasing a child is authorised only by a parent or guardian</div>
          <p style="margin:0">Only a parent, a named guardian, or either separated parent may put
          a person on the list of those permitted to collect a child. <b>Camp staff can never add
          anyone to that list &mdash; including themselves.</b></p>
        </div>
        <p>The specific case to think about is the awkward one: a session is ending, an adult
        presents themselves saying a parent sent them, and the parent cannot be reached. Under the
        document as drafted the child is <b>not released</b> &mdash; and the refusal is not a
        judgement about that adult, it is that the list is the only authority and the list does
        not name them.</p>
        <div class="c-alert c-alert--warn">
          <div><b>If you need an operational escape hatch for that case, say so now and say what
          it is</b> &mdash; a named on-call officer who may authorise, a second-parent
          confirmation, a documented exception log. The platform can build a controlled one. What
          it should not do is leave the list quietly writable by staff, which is the arrangement
          that ends with a child handed to the wrong adult.</div>
        </div>
        <div class="choices">
          <div class="choice"><span class="box"></span><span>Confirm as drafted</span></div>
          <div class="choice"><span class="box"></span><span>Confirm with changes:<span class="fill"></span></span></div>
          <div class="choice"><span class="box"></span><span>Discuss &mdash; we need an escape hatch</span></div>
        </div>
      </div>

      <div class="q">
        <div class="q__n">Question 2</div>
        <div class="q__t">A court-appointed guardian</div>
        <p>Recorded in the platform&rsquo;s open-question register, verbatim, and routed to you:</p>
        <blockquote class="rec"><p>Camp pickup authority reads the household and delegation model.
        <b>A court-appointed guardian is neither parent nor delegate.</b></p></blockquote>
        <div class="prop">
          <div class="prop__k">Proposed answer</div>
          <p style="margin:0">A court-appointed guardian is simply a <b>named guardian</b> &mdash;
          the second of the four paths &mdash; established by the appointing order instead of by
          the household record. Recorded by staff against the child, carrying a reference to the
          order and the date, never asserted by the person themselves. On that reading the question
          is a <b>recording procedure</b>, not a missing rule, and no new authority path is needed.</p>
        </div>
        <div class="choices">
          <div class="choice"><span class="box"></span><span>Agree</span></div>
          <div class="choice"><span class="box"></span><span>Camp needs something more:<span class="fill"></span></span></div>
        </div>
      </div>

      <div class="q">
        <div class="q__n">Question 3</div>
        <div class="q__t">Does camp need powers the document does not have?</div>
        <p>&ldquo;Acting for a child&rdquo; is broken into seven named powers: see, enrol,
        transact, consent, supervise, release, and emergency medical. <b>Is anything camp does
        missing from that list?</b> Medication administration and off-site activity consent are the
        two most likely gaps &mdash; if either is a distinct decision at camp rather than part of
        the general consent given at registration, it should be its own power rather than something
        staff infer.</p>
        <div class="choices">
          <div class="choice"><span class="box"></span><span>The seven are sufficient</span></div>
          <div class="choice"><span class="box"></span><span>Add:<span class="fill"></span></span></div>
        </div>
      </div>
    </div>
    <div class="panel__foot retn">
      <span><b>Returned by</b><span class="fill"></span></span>
      <span><b>Date</b><span class="fill"></span></span>
    </div>
  </div>
</section>
"""

LEGAL = """
<section class="memo" id="legal">
  <div class="panel">
    <div class="panel__head">
      <div class="memo__head">
        <svg class="memo__ic" aria-hidden="true"><use href="#i-scales"/></svg>
        <div>
          <h2 style="margin:0">Legal Advisor</h2>
          <div class="tiny" style="color:var(--ink-2)">The custody and consent provisions</div>
        </div>
      </div>
      <span class="c-pill c-pill--ok">approved as drafted</span>
    </div>
    <div class="panel__body">
      <p>The platform has never held a stated rule for who may act for a minor. It was inferring
      one from how the software needed to behave &mdash; the fault this project refuses everywhere
      else &mdash; so three pieces of work were stopped rather than built on it. A document now
      states the rule.</p>
      <p><b>Four authority paths are decided by AFRP</b> and are not in question here: a parent by
      household membership, a named guardian, either of two parents when separated, and a per-event
      delegate identified at event setup.</p>
      <div class="c-alert c-alert--warn">
        <div><b>The provisions below were drafted on general youth-protection practice by people
        who are not lawyers.</b> They are marked provisional in the document itself, and they are
        in front of you before anything is built on them rather than after.</div>
      </div>

      <div class="q">
        <div class="q__n">For review &middot; 1</div>
        <div class="q__t">Supervision disclosed, release consented</div>
        <p>The document treats two things differently that an operational reading would merge.
        <b>Supervision</b> is designated by AFRP at event setup &mdash; staff, chaperones, screened
        volunteers &mdash; and <b>disclosed</b> to the household; parents are told, not asked, on
        the reasoning that supervision is the organisation discharging its own duty of care rather
        than exercising delegated parental authority. <b>Release</b> &mdash; collecting a child, or
        authorising their departure &mdash; may be granted <b>only by a parent or guardian</b>; an
        event organiser cannot add anyone to a release list, including themselves.</p>
        <div class="prop">
          <div class="prop__k">The question</div>
          <p style="margin:0">Is disclosure sufficient for supervision, or should the platform
          capture an affirmative parental acknowledgement of the supervising adults? And is
          parental designation the correct and sufficient instrument for release, given AFRP
          operates across many states?</p>
        </div>
      </div>

      <div class="q">
        <div class="q__n">For review &middot; 2</div>
        <div class="q__t">Emergency medical authorisation</div>
        <p>Drafted as an <b>explicit authorisation given by a parent or guardian at
        registration</b>, event-scoped, permitting authorisation of treatment only when no parent
        or guardian is reachable. It is deliberately not inherited from supervising a child, and
        not held by a per-event delegate unless a parent named them for it.</p>
        <div class="prop">
          <div class="prop__k">The question</div>
          <p style="margin:0">Is a registration-time authorisation the right instrument, and what
          must it actually say to be relied on? This is the provision most likely to be drafted
          wrongly by non-lawyers, and the one most likely to be tested.</p>
        </div>
      </div>

      <div class="q">
        <div class="q__n">For review &middot; 3</div>
        <div class="q__t">Restrictions, and the posture when documents conflict</div>
        <p>A recorded restriction &mdash; a custody order, protective order or equivalent &mdash;
        <b>overrides every authority path, including &ldquo;either of two parents&rdquo;.</b> A
        restriction is entered by staff against the specific adult-and-child pair, never inferred
        from the family tree, the household record, or a member&rsquo;s own assertion; it carries a
        reference to the document relied on, who recorded it and when; and it is liftable only by
        the same route, with the history preserved.</p>
        <p><b>The platform does not adjudicate custody.</b> It records what it was shown and
        enforces that. Where documents conflict, are ambiguous, or are described but not produced,
        the platform refuses the action, says a restriction is on file that it cannot resolve, and
        routes the question to you &mdash; never stating the substance of the restriction to the
        person being refused.</p>
        <div class="prop">
          <div class="prop__k">The question I would most like answered</div>
          <p style="margin:0">Is &ldquo;refuse and route&rdquo; the correct posture? It is the
          conservative choice and consistent with how this platform handles every other silence in
          the record. But refusing a parent access to their own child&rsquo;s record is not a
          neutral act, and there may be a duty to act rather than to pause. If there is a category
          of case where the platform must do something other than refuse, it needs naming now.</p>
          <p style="margin:.6em 0 0">Related: is staff-entered, document-referenced recording an
          adequate standard for establishing a restriction, or does AFRP need a defined intake
          &mdash; who may record one, what must be seen, what is retained?</p>
        </div>
      </div>

      <div class="q">
        <div class="q__n">For review &middot; 4</div>
        <div class="q__t">A court-appointed guardian</div>
        <blockquote class="rec"><p>Camp pickup authority reads the household and delegation model.
        <b>A court-appointed guardian is neither parent nor delegate.</b></p></blockquote>
        <p><b>Proposed:</b> a court-appointed guardian is the <b>named guardian</b> path,
        established by the appointing order rather than by household membership &mdash; recorded,
        document-referenced, dated. On that reading the question resolves to a recording procedure
        and no new authority path is needed.</p>
        <div class="prop">
          <div class="prop__k">The question</div>
          <p style="margin:0">Does that hold, and does the order&rsquo;s own scope need to be
          carried onto the record? A guardianship may be limited in ways the platform&rsquo;s seven
          powers do not currently express.</p>
        </div>
      </div>

      <div class="panel panel--flag" style="margin-top:var(--s5)">
        <div class="panel__body">
          <p style="margin:0 0 .6em"><b>Two things worth knowing about how this will be used.</b></p>
          <p style="margin:0 0 .6em"><b>Nothing waits on you to start.</b> Work on the household
          and camp surfaces is proceeding against the document now, with everything derived from an
          unratified answer labelled a proposal on the screen itself. Your review changes rules and
          removes labels; it does not unblock a stalled project. But the sooner it arrives, the
          less is built on a reading you would have written differently.</p>
          <p style="margin:0"><b>Every exercise of authority is logged</b> &mdash; who acted, for
          whom, under which path, when, and which power. If that record needs a defined retention
          period, or needs shaping for a particular kind of later inquiry, that is worth telling us
          before it is built rather than after.</p>
        </div>
      </div>
    </div>
    <div class="panel__foot retn">
      <span><b>Reviewed by</b><span class="fill"></span></span>
      <span><b>Date</b><span class="fill"></span></span>
    </div>
  </div>
</section>
"""

def mark_ratified(html: str) -> str:
    """Every body approved the first option in each block — as drafted. Tick it,
    and grey the roads not taken so the page reads as a record of what was asked
    and what was chosen, not as a form still waiting."""
    import re

    def one(block: str) -> str:
        first = [True]

        def choice(m):
            if first[0]:
                first[0] = False
                return ('<div class="choice choice--on"><span class="box box--on"></span>'
                        '<span>' + m.group(1) + '</span></div>')
            return ('<div class="choice choice--off"><span class="box"></span>'
                    '<span>' + m.group(1) + '</span></div>')

        return re.sub(r'<div class="choice"><span class="box"></span><span>(.*?)</span></div>',
                      choice, block, flags=re.S)

    return re.sub(r'<div class="choices">.*?</div>\s*</div>',
                  lambda m: one(m.group(0)), html, flags=re.S)


FOOT = ('<div class="panel__foot retn"><span><b>Approved as drafted</b> '
        '&middot; 8 September 2026 &middot; recorded by David Saah</span></div>')

MEMBERSHIP = mark_ratified(MEMBERSHIP).replace(
    '<div class="panel__foot retn">\n      <span><b>Returned by</b><span class="fill"></span></span>\n'
    '      <span><b>Date</b><span class="fill"></span></span>\n    </div>', FOOT)
CAMP = mark_ratified(CAMP).replace(
    '<div class="panel__foot retn">\n      <span><b>Returned by</b><span class="fill"></span></span>\n'
    '      <span><b>Date</b><span class="fill"></span></span>\n    </div>', FOOT)
LEGAL = LEGAL.replace(
    '<div class="panel__foot retn">\n      <span><b>Reviewed by</b><span class="fill"></span></span>\n'
    '      <span><b>Date</b><span class="fill"></span></span>\n    </div>',
    '<div class="panel__foot retn"><span><b>Reviewed and approved as drafted</b> '
    '&middot; 8 September 2026 &middot; recorded by David Saah</span></div>')

PAGE = f"""<meta charset="utf-8">
<title>R6 Ratification Packet</title>
<style>
{CSS}
{OVERLAY}
</style>
<script>
(function(){{try{{var t=localStorage.getItem('afrp-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}
document.addEventListener('DOMContentLoaded',function(){{document.body.setAttribute('data-lens','fed');}});}})();
</script>
{SPRITE}

<header class="topbar">
  <div class="topbar__brand">
    <span class="topbar__mark" aria-hidden="true"><svg><use href="#i-olive"/></svg></span>
    <span>
      <span class="topbar__name">AFRP</span>
      <span class="topbar__sub">Ramallah, Palestine &middot; Est. 1952</span>
    </span>
  </div>
</header>

<main class="pk">
  <div class="page-head">
    <span class="ph-ico" aria-hidden="true"><svg><use href="#i-scroll"/></svg></span>
    <div>
      <h1>R6 Ratification Packet</h1>
      <div class="tiny" style="color:var(--ink-2)">Guardian and delegation authority &mdash; who may
      act for a minor &middot; drafted 8 September 2026 &middot; <b>ratified 8 September 2026</b></div>
    </div>
  </div>

  <div class="panel">
    <div class="panel__body">
      <p class="lede">The membership platform has never held a stated rule for who may act for a
      minor &mdash; enrol them in a programme, pay for them, answer a consent question on their
      behalf. It was <i>inferring</i> one from how the software needed to behave, so three pieces of
      work were stopped rather than built on an inferred rule about children.</p>
      <p>A document now states it. <b>Four authority paths are decided:</b> a parent by household
      membership, a named guardian, either of two parents when separated, and a per-event delegate
      identified at event setup. The rest &mdash; what &ldquo;acting for&rdquo; actually permits,
      how supervision differs from collecting a child, and what happens when a custody order is on
      file &mdash; was drafted on general youth-protection practice and <b>is not ratified by
      anyone.</b> This packet puts each unratified part in front of the body that owns it.</p>
      <div class="verdict verdict--allow">
        <span class="verdict__ic" aria-hidden="true"><svg><use href="#i-seal"/></svg></span>
        <div><b>Ratified 8 September 2026 &mdash; all three bodies, as drafted, without
        amendment.</b> The Membership Committee approved the power set and the two-households
        answer; Camp Ramallah approved the supervision and release model and the court-appointed
        guardian; the Legal Advisor approved the custody and consent provisions. R6 is graded
        <b>attested</b> in the rules register, the refusals that stood in its absence lift, and the
        surfaces built from it state ordinary rules rather than proposals. The sections below stand
        as the record of what each body was asked and what it approved.</div>
      </div>
    </div>
  </div>

  <div class="panel">
    <div class="panel__head"><h2 style="margin:0">Who answers what</h2></div>
    <div class="panel__body">
      <p>Each body has only its own section. Nobody needs to read the others to answer theirs.</p>
      <div class="routing">
        <a class="route" href="#membership">
          <svg class="route__ic" aria-hidden="true"><use href="#i-people"/></svg>
          <span class="route__who">Membership Committee</span>
          <span class="route__owns">The seven powers and who holds them &middot; which club a minor
          in two households belongs to</span>
        </a>
        <a class="route" href="#camp">
          <svg class="route__ic" aria-hidden="true"><use href="#i-tent"/></svg>
          <span class="route__who">Camp Ramallah</span>
          <span class="route__owns">Supervision versus release at the gate &middot; a
          court-appointed guardian &middot; whether camp needs powers the document lacks</span>
        </a>
        <a class="route" href="#legal">
          <svg class="route__ic" aria-hidden="true"><use href="#i-scales"/></svg>
          <span class="route__who">Legal Advisor</span>
          <span class="route__owns">Disclosure versus consent &middot; emergency medical
          authorisation &middot; custody restrictions and the refuse-and-route posture</span>
        </a>
      </div>
    </div>
    <div class="panel__foot foot-note">
      Full document: <span class="mono">AFRP-Portal/docs/design/AFRP-R6-Minor-Authority.md</span>.
      When all three have answered, R6 is graded <b>attested</b> in the rules register and the
      provisional labels come off the surfaces that carry them.
    </div>
  </div>

  <div class="tz" aria-hidden="true"></div>

  {MEMBERSHIP}
  {CAMP}
  {LEGAL}

  <div class="panel">
    <div class="panel__head"><h2 style="margin:0">What the platform does in the meantime</h2></div>
    <div class="panel__body">
      <div class="verdict verdict--allow">
        <span class="verdict__ic" aria-hidden="true"><svg><use href="#i-seal"/></svg></span>
        <div><b>Camp refuses applications and names this document.</b> Camp Ramallah serves ages 13
        to 17, so every applicant is a child and somebody else makes the application. Until R6 is
        ratified the platform will not take one &mdash; it publishes everything about the season
        that is not a fact about a child (the window, the seats, the age band, the whole selection
        rule) and refuses the application naming the rule and the three bodies it sits with.
        Applications are taken on paper until then.</div>
      </div>
      <p class="foot-note" style="margin-top:var(--s4)">A second refusal stands beside it on
      separate grounds and <b>does not lift when R6 is ratified</b>: a paid counsellor-in-training
      under eighteen is an employee, and employment-law confidentiality restricts what may be
      disclosed to their parents.</p>
    </div>
  </div>
</main>
"""

Path("/home/claude/r6-packet.html").write_text(PAGE, encoding="utf-8")
print(f"r6-packet.html {len(PAGE)} bytes")
