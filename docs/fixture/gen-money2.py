# -*- coding: utf-8 -*-
"""Money fixes from the split pile of red-team round 14, verified against the fixture."""
import io, sys, json
P = '/home/claude/afrp-mockups/docs/prototype.html'
s = io.open(P, encoding='utf-8').read()
if 'rt-money-1' in s:
    print('already applied'); sys.exit(0)
n = 0
def sub(old, new, label):
    global s, n
    if old not in s: raise SystemExit('ANCHOR MISSING: ' + label)
    s = s.replace(old, new, 1); n += 1; print('  fixed:', label)

# ── one annual statement cannot span three corporations ─────────────────────
# The receipt moment already names the receiving entity ("Your receipt — ARFHSN,
# EIN on file"). The annual statement did not: it was described as ONE statement,
# which would merge AFRP, ARFECF and ARFHSN gifts under a single EIN.
sub("<p>Four moments, then one annual statement &mdash; enough to close the loop, few enough "
    "that people keep opening them</p>",
    "<p data-rt=\"rt-money-1\">Four moments, then <b>one annual statement per corporation</b> "
    "&mdash; enough to close the loop, few enough that people keep opening them</p>",
    'annual statement is per corporation')

sub("""['Purpose fulfilled','ambulance in service at the Ramallah clinic \u00b7 restriction released on spend',
  'The ambulance is in service. Here is a photograph, and the total your gift was part of.']
]""",
    """['Purpose fulfilled','ambulance in service at the Ramallah clinic \u00b7 restriction released on spend',
  'The ambulance is in service. Here is a photograph, and the total your gift was part of.'],
 ['Year end','a separate annual statement from <b>each corporation</b> that received a gift. AFRP, ARFECF and ARFHSN are three taxpayers with three EINs, so one combined &ldquo;charitable total&rdquo; would not be a substantiation document for any of them. In the 500-household fixture <b>8 of 300 donors</b> gave to more than one.',
  'Your statements &mdash; one from each organisation you gave to, each with its own EIN.']
]""",
    'year-end statement stage added')

sub("+Math.min(S.stage,4)+' of 4</span>", "+Math.min(S.stage,5)+' of 5</span>",
    'stage counter 4 -> 5')

io.open(P, 'w', encoding='utf-8').write(s)
print(f'\n{n} fixes applied')
