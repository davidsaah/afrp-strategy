# -*- coding: utf-8 -*-
"""Fixes from the red team run against the frozen snapshot d3a8b6d."""
import io, sys
P = '/home/claude/afrp-mockups/docs/prototype.html'
s = io.open(P, encoding='utf-8').read()
if 'rt-fixed-1' in s:
    print('already applied'); sys.exit(0)
n = 0
def sub(old, new, label):
    global s, n
    if old not in s: raise SystemExit('ANCHOR MISSING: ' + label)
    s = s.replace(old, new, 1); n += 1; print('  fixed:', label)

# ── 1 · a fabricated citation was being ENFORCED ─────────────────────────────
# The platform says in three places that the ARFECF 4-member interlock cap is
# "absent from the 2013 text — carried visibly INACTIVE, never enforced silently".
# A working panel on the money lens then refused a fifth appointment and cited
# "ARFECF Art. V §4" as operative text. It is not operative text.
sub('<h3>Interlock cap, checked at appointment</h3>',
    '<h3 data-rt="rt-fixed-1">Interlock cap &mdash; recorded, not enforced</h3>',
    'interlock panel heading')
sub('<span>Cap &mdash; no more than four<small>ARFECF Art. V &sect;4 &middot; validated when '
    'the appointment is made, because it is invisible to whoever is making it</small></span>'
    '<span class="calc__n">&le; 4</span>',
    '<span>Cap of four &mdash; <b>not in the 2013 text</b><small>A four-member cap appears in '
    'prior analysis. It is <b>not</b> in the ARFECF 2013 by-laws, so there is no provision to '
    'cite and nothing here refuses an appointment. The count is surfaced at appointment time '
    'because it is otherwise invisible to whoever is making it.</small></span>'
    '<span class="calc__n">&le; 4?</span>',
    'interlock citation')
sub("note.innerHTML = 'Appointed — <b>4 of 4, at the cap exactly.</b> Permitted, logged with a "
    "warning to both boards.';",
    "note.innerHTML = 'Appointed — <b>4 shared members.</b> Recorded and shown to both boards. "
    "No provision is being applied: the cap is not in the 2013 text.';",
    'interlock 4th appointment')

# the refusal branch
i = s.find("function tryInterlock(btn){")
j = s.find("}\n", s.find("btn.disabled = true", i))
seg = s[i:j]
old_ref = seg[seg.find("} else {"):]
sub(old_ref,
    """} else {
      S.interlock += 1;
      note.innerHTML = '<b>Recorded — ' + S.interlock + ' shared members.</b> This is past the '
        + 'four named in prior analysis, and the platform still does not refuse it: <b>no '
        + 'operative text supports a refusal.</b> Both boards see the number and the Legal '
        + 'Advisor is notified. If the Board wants a cap, it has to enact one.';
    """,
    'interlock refusal removed')

# ── 2 · the Board denominator: 18 clubs minus 2 is 16, not 24 ────────────────
sub('<span>Chapter Club presidents<small>18 clubs; 2 excluded &mdash; affiliation form unfiled '
    '(3.2, 6.4.1)</small></span><span class="calc__n">24</span>',
    '<span>Chapter Club presidents<small>18 clubs; 2 excluded &mdash; affiliation form unfiled '
    '(3.2, 6.4.1)</small></span><span class="calc__n">16</span>',
    'club presidents 24 -> 16')
sub('<span>Voting members today<small>non-voting: Executive Director, Executive Assistant '
    '&middot; 2/3 of all members = 32.67 &rarr; 33 votes needed</small></span>'
    '<span class="calc__n">49</span>',
    '<span>Voting members today<small>9 + 16 + 4 + 9 + 3 &middot; non-voting: Executive Director, '
    'Executive Assistant &middot; 2/3 of all members = 27.33 &rarr; 28 votes needed</small></span>'
    '<span class="calc__n">41</span>',
    'board total 49 -> 41')

# ── 3 · the poll that was declared failed actually carries ───────────────────
sub('<span>Poll: adopt revised Board Rules<small>threshold 2/3 of all 49 members = 32.67 &rarr; '
    '33 (6.2.1)</small></span><span class="calc__n">49 polled</span>',
    '<span>Poll: adopt revised Board Rules<small>threshold 2/3 of all 41 members = 27.33 &rarr; '
    '28 (6.2.1)</small></span><span class="calc__n">41 polled</span>',
    'poll threshold')
sub('<div class="calc__r calc__r--sub"><span>No reply &mdash; counted as abstain<small>each '
    'functions as a No against the fixed denominator</small></span><span class="calc__n">15</span></div>',
    '<div class="calc__r calc__r--sub"><span>No reply &mdash; counted as abstain<small>each '
    'functions as a No against the fixed denominator</small></span><span class="calc__n">7</span></div>',
    'poll no-reply 15 -> 7')
sub('<div class="calc__r calc__r--tot is-fail"><span>Fails &mdash; 28 of 33 needed<small>carried '
    '28&ndash;6 among those who answered, and still fails. Probably unintended; question 5 to the '
    'drafting committee</small></span><span class="calc__n">28</span></div>',
    '<div class="calc__r calc__r--tot"><span>Carries &mdash; 28 of 28 needed<small>by exactly one '
    'vote. One more Board member failing to reply would have sunk a motion that 28 of the 34 who '
    'answered supported. That is the 6.2.4 abstention rule doing its work, and it is question 5 '
    'to the drafting committee. An earlier build of this screen computed the denominator as 33 '
    'and declared this motion <b>failed</b>.</small></span><span class="calc__n">28</span></div>',
    'poll result: fails -> carries')

io.open(P, 'w', encoding='utf-8').write(s)
print(f'\n{n} fixes applied')
