# -*- coding: utf-8 -*-
"""Build the fixture, verify its coverage, and write it out.
   The verification is the point: a fixture that does not PROVE it covers every
   program and club combination is just a pile of names."""
import sys, os, json, io, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import spec, gen

filled = gen.build()
P, H, RL, EV, EN, PY_, FL = (gen.PEOPLE, gen.HOUSEHOLDS, gen.RELS, gen.EVENTS,
                             gen.ENGAGE, gen.PAYMENTS, gen.FLAGS)
CLUB_CODES = [c['code'] for c in spec.CLUBS]
fails = []
def check(name, ok, detail=''):
    fails.append((name, detail)) if not ok else None
    print(('  ok   ' if ok else ' FAIL '), name, ('' if ok else '— ' + detail))

print('== shape ==')
check('500 households', len(H) == 500, f'{len(H)}')
check('every household has a club', all(h['club'] in CLUB_CODES for h in H))
check('every person is marked synthetic', all(p['synthetic'] for p in P))
check('no synthetic name collides with a real GEDCOM name',
      all(not gen.NP.collides(p['given'], p['family']) for p in P),
      str([f"{p['given']} {p['family']}" for p in P if gen.NP.collides(p['given'], p['family'])][:5]))

print('\n== coverage: every program x club x rung ==')
cells = collections.Counter((g['program'], g['club'], g['rung']) for g in EN)
want = [(pk, c, r) for pk in spec.PROGRAM_KEYS for c in CLUB_CODES for r in (1,2,3,4,5)]
empty = [w for w in want if not cells[w]]
check(f'all {len(want)} program x club x rung cells populated', not empty,
      f'{len(empty)} empty, e.g. {empty[:6]}')

print('\n== coverage: every program x club (any rung) ==')
pc = collections.Counter((g['program'], g['club']) for g in EN)
emptypc = [(pk,c) for pk in spec.PROGRAM_KEYS for c in CLUB_CODES if not pc[(pk,c)]]
check(f'all {len(spec.PROGRAM_KEYS)*4} program x club pairs populated', not emptypc, str(emptypc))

print('\n== coverage: household structures ==')
sc = collections.Counter(h['structure'] for h in H)
for s in spec.STRUCTURES:
    check(f"structure present: {s['key']}", sc[s['key']] > 0, '0 households')
check('every structure appears in every club',
      all(any(h['structure']==s['key'] and h['club']==c for h in H)
          for s in spec.STRUCTURES for c in CLUB_CODES),
      str([(s['key'],c) for s in spec.STRUCTURES for c in CLUB_CODES
           if not any(h['structure']==s['key'] and h['club']==c for h in H)][:8]))

print('\n== coverage: ages ==')
BANDS = [(0,7),(8,16),(14,15),(16,18),(17,24),(19,20),(21,35),(36,61),(62,79),(80,120)]
for lo,hi in BANDS:
    for c in CLUB_CODES:
        n = sum(1 for p in P if p['living'] and p.get('club')==c and lo <= p['age'] <= hi)
        check(f'club {c} has people aged {lo}-{hi}', n > 0, '0 people')

print('\n== the untraditional families are actually there ==')
for k in ('samesex-one-descent','samesex-both-descent','samesex-with-children',
          'divorced-remarried','divorced-marriedin-ex','unmarried-partners',
          'adoptive','guardianship'):
    check(f'{k}: {sc[k]} households', sc[k] >= 5, f'only {sc[k]}')

print('\n== open questions are FLAGGED, never decided ==')
fk = collections.Counter(f['key'] for f in FL)
for k in spec.OPEN_QUESTIONS:
    check(f'open question raised: {k}', fk[k] > 0, '0 flags')
check('no open question is marked decided', all(not f['decided'] for f in FL))

print('\n== rules the fixture must not break ==')
check('R7 no minor is in a directory',
      all(not p['directoryInclude'] for p in P if p['age'] < 18))
check('R7 no minor has a membership record',
      all(p.get('membership') is None for p in P if p['age'] < 18))
check('R28 no living person exposes dates without sign-in',
      all(not p['datesVisibleWithoutSignIn'] for p in P if p['living']))
check('R23 club class never routes money (host is an entity or a club, set independently)',
      all(x['hostEntity'] is not None for x in PY_))
check('R20 every payment posts gross with its own fee line',
      all(x['grossCents'] - x['processingFeeCents'] == x['netCents'] and
          x['journalLines'] == ['clearing','fee','revenue'] for x in PY_))
check('R21 club dues collected nationally are a liability',
      all(x['treatment'] == 'agency-liability'
          for x in PY_ if x['kind'] == 'dues-club-via-national'))
check('11.1.5 conduit present', any(x['treatment']=='conduit-11.1.5' for x in PY_))
check('R25 every restricted gift carries its restriction through',
      all(x['fundClass'] == x['restriction'] for x in PY_ if x['kind']=='restricted-gift'))
check('R16 every member has exactly one club of record',
      all(isinstance(p['membership']['clubOfRecord'], str) for p in P if p.get('membership')))
check('R2 multi-club standings are independent',
      any(len({c['standing'] for c in p['membership']['clubs']}) > 1
          for p in P if p.get('membership') and len(p['membership']['clubs'])>1))
check('R34 no relocation transfers a club automatically',
      all(e.get('automatic') is False for e in EV if e['kind']=='relocation'))
check('R34 every death is gated on family approval',
      all(e.get('gate')=='family-approval-required' for e in EV if e['kind']=='death'))
check('R33 approval and publication are separate',
      any(e.get('approved') and not e.get('published') for e in EV if e.get('claim')))
check('no rung without evidence', all(g['evidence'] for g in EN))
check('rung 5 is never a child', all(gen.BY_ID[g['person']]['age'] >= 25 for g in EN if g['rung']==5))
check('women-to-women has no men', all(gen.BY_ID[g['person']]['sex']=='F'
      for g in EN if g['program']=='w2w'))
# The band gates participation, not leadership — so assert BOTH halves of that rule,
# for every age-capped program, not just camp.
CAPPED = [p for p in spec.PROGRAMS if p['band'][1] is not None]
check('participation (rungs 1-3) stays inside every age band',
      all(p['band'][0] <= gen.BY_ID[g['person']]['age'] <= p['band'][1]
          for p in CAPPED for g in EN if g['program']==p['key'] and g['rung'] <= 3),
      str([(g['program'], gen.BY_ID[g['person']]['age'])
           for p in CAPPED for g in EN
           if g['program']==p['key'] and g['rung']<=3
           and not (p['band'][0] <= gen.BY_ID[g['person']]['age'] <= p['band'][1])][:5]))
check('leadership (rungs 4-5) is adult in every program, band or not',
      all(gen.BY_ID[g['person']]['age'] >= 16 for g in EN if g['rung'] >= 4))
check('every age-capped program still reaches rung 5 in every club',
      all(any(g['program']==p['key'] and g['club']==c and g['rung']==5 for g in EN)
          for p in CAPPED for c in CLUB_CODES))

living = [p for p in P if p['living']]
print(f"""
== the fixture ==
  households            {len(H)}
  people                {len(P)}   ({len(living)} living, {len(P)-len(living)} deceased)
  adults / minors       {sum(1 for p in P if p['age']>=18)} / {sum(1 for p in P if p['age']<18)}
  relationships         {len(RL)}
  life events           {len(EV)}
  engagements           {len(EN)}   ({filled} added by the coverage fill pass)
  payments              {len(PY_)}
  open questions raised {len(FL)} across {len(set(f['key'] for f in FL))} distinct by-law questions
""")
for c in spec.CLUBS:
    hh=[h for h in H if h['club']==c['code']]
    pp=[p for p in P if p.get('club')==c['code']]
    print(f"  {c['name']:22s} {len(hh):3d} households  {len(pp):4d} people   integration: {c['integration']}")

out = dict(
  meta=dict(generator='gen.py', seed=spec.SEED, asOf=spec.AS_OF,
            synthetic=True,
            statement=('Every person, household, event and dollar in this file is invented. '
                       'Family names come from the AFRP Clan Family Roster so clan and By-Law '
                       '4.1.1 lookups behave realistically; given names were checked against '
                       'the 21,677 real (given, surname) pairs in the Ramallah GEDCOM and '
                       'resampled on collision, so no synthetic person carries a real name.'),
            clubSizesSource='Azeez Shaheen, Ramallah: Its History and Its Genealogies (1982), p.11',
            coverageFillCount=filled),
  clubs=spec.CLUBS, programs=spec.PROGRAMS, rungs=spec.RUNGS,
  structures=spec.STRUCTURES, openQuestionCatalog=spec.OPEN_QUESTIONS,
  households=H, people=P, relationships=RL, lifeEvents=EV,
  engagements=EN, payments=PY_, openQuestions=FL,
)
io.open('/home/claude/fixture/afrp-fixture.json','w').write(json.dumps(out, indent=1))
print(f"\n{'ALL CHECKS PASS' if not fails else str(len(fails))+' CHECKS FAILED'}")
sys.exit(1 if fails else 0)
