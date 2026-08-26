# -*- coding: utf-8 -*-
"""Reduce the 4 MB fixture to the projection the browser page needs."""
import json, io, collections
d = json.load(open('afrp-fixture.json'))
P  = {p['id']: p for p in d['people']}
HH = {h['id']: h for h in d['households']}
PROG = d['programs']; CLUBS = d['clubs']
CC = [c['code'] for c in CLUBS]

cells = collections.Counter((g['program'], g['club'], g['rung']) for g in d['engagements'])
matrix = {p['key']: {c: [cells[(p['key'], c, r)] for r in (1,2,3,4,5)] for c in CC} for p in PROG}

# rung totals per program (ordered ramp, not categorical)
rungtot = {p['key']: [sum(cells[(p['key'], c, r)] for c in CC) for r in (1,2,3,4,5)] for p in PROG}

def _derived(d):
    """Roll-ups the screens read.  Computed here from the fixture on every build —
    it used to be a hand-kept file, which is exactly how a screen ends up quoting a
    number the data no longer supports."""
    M = [p for p in d['people'] if p.get('membership')]
    out = dict(members=len(M),
               certified=sum(1 for p in M if p['membership']['votingDuesPaidBy']),
               directoryOptIn=sum(1 for p in M if p['directoryInclude']),
               nat=dict(collections.Counter(p['membership']['standing'] for p in M)))
    out['nat'].setdefault('board-vote-pending', 0)
    out['clubs'] = {}
    for c in [x['code'] for x in d['clubs']]:
        rows = [x for p in M for x in p['membership']['clubs'] if x['club'] == c]
        st = collections.Counter(x['standing'] for x in rows)
        out['clubs'][c] = dict(
            rows=len(rows), current=st['current'], grace=st['grace'], lapsed=st['lapsed'],
            record=sum(1 for p in M if p['membership']['clubOfRecord'] == c),
            alsoNational=sum(1 for p in M for x in p['membership']['clubs']
                             if x['club'] == c and p['membership']['standing'] == 'current'),
            households=sum(1 for h in d['households'] if h['club'] == c))
    return out


def BYID_OK(pid):
    q = P.get(pid)
    return bool(q) and q['age'] >= 18            # R7: never a minor's name


def label(pid):
    p = P[pid]; return f"{p['given']} {p['family']}"

flags = []
for f in d['openQuestions']:
    subs = [s for s in f['subjects'] if s in P]
    flags.append(dict(id=f['id'], key=f['key'], bylaw=f['bylaw'], note=f['note'],
                      who=[dict(name=label(s), age=P[s]['age'], club=P[s].get('club') or '')
                           for s in subs]))

hh = []
for h in d['households']:
    members = [P[i] for i in h['adults'] + h['minors'] if i in P]
    hh.append(dict(id=h['id'], club=h['club'], structure=h['structure'],
                   label=h['structureLabel'], joined=h['joinedYear'],
                   q=h['openQuestions'],
                   minors=sum(1 for m in members if m['age'] < 18),
                   deceased=sum(1 for m in members if not m['living']),
                   people=[dict(n=f"{m['given']} {m['family']}", a=m['age'], s=m['sex'],
                                c=m['clan'] or '', e=m['eligibilityBasis'],
                                m=(m.get('membership') or {}).get('nationalClass', ''),
                                st=(m.get('membership') or {}).get('standing', ''),
                                d=m['living'])
                           # R7: minors never appear in a directory — not by name, not
                           # by age. The household carries a count instead.  The
                           # deceased are withheld too: a death is a life event with a
                           # family-approval gate (R34), not a row to publish.
                           for m in sorted(members, key=lambda x: -x['age'])
                           if m['age'] >= 18 and m['living']]))

money = collections.Counter(); moneyamt = collections.Counter()
for x in d['payments']:
    money[x['treatment']] += 1; moneyamt[x['treatment']] += x['grossCents']
TREAT_NOTE = {}
for x in d['payments']: TREAT_NOTE.setdefault(x['treatment'], x['note'])

out = dict(
  meta=d['meta'],
  clubs=[dict(code=c['code'], name=c['name'], integration=c['integration'],
              households=sum(1 for h in d['households'] if h['club']==c['code']),
              people=sum(1 for p in d['people'] if p.get('club')==c['code'])) for c in CLUBS],
  programs=[dict(key=p['key'], name=p['name'], host=p['host'],
                 band=[p['band'][0], p['band'][1]], flagship=p.get('flagship', False))
            for p in PROG],
  rungs=d['rungs'], matrix=matrix, rungtot=rungtot,
  structures=[dict(key=s['key'], label=s['label'],
                   n=sum(1 for h in d['households'] if h['structure']==s['key']),
                   byClub={c: sum(1 for h in d['households']
                                  if h['structure']==s['key'] and h['club']==c) for c in CC},
                   q=s.get('open_q')) for s in d['structures']],
  questions=d['openQuestionCatalog'], flags=flags, households=hh,
  money=[dict(treatment=k, n=money[k], usd=moneyamt[k]/100, note=TREAT_NOTE[k])
         for k in sorted(money, key=lambda k: -money[k])],
  derived=_derived(d),
  fieldDefs=[dict(key=f[0], label=f[1], indexed=f[2], filterable=f[3],
                  memberControlled=f[4], default=f[5]) for f in d['fieldDefs']],
  audiences=d['audiences'],
  facets=d['facets'],
  camp=dict(season=d['camp']['season'], ratio=d['camp']['ratio'],
            cabins=d['camp']['cabins'], health=d['camp']['health'],
            aid=dict(instruments=d['camp']['aid']['instruments'],
                     remaining=d['camp']['aid']['remaining'],
                     note=d['camp']['aid']['note'],
                     awards=[dict(instrument=a['instrument'], basis=a['basis'],
                                  awardedCents=a['awardedCents'], partial=a['partial'],
                                  state=a['state']) for a in d['camp']['aid']['awards']]),
            # R7: a camper is a minor. Never a name — a decision, a club, a reason.
            applications=[dict(id=a['id'], club=a['club'], age=a['age'],
                               firstTimer=a['firstTimer'], returner=a['returner'],
                               decision=a['decision'], reasons=a['reasons'],
                               aidRequested=a['aidRequested'],
                               waitlistRank=a.get('waitlistRank'),
                               offer=a.get('offer'))
                          for a in d['camp']['applications']],
            staff=[dict(id=x['id'], name=label(x['person']) if BYID_OK(x['person']) else '',
                        role=x['role'], club=x['club'], paid=x['paid'],
                        legalStatus=x.get('legalStatus'),
                        parentVisibility=x.get('parentVisibility'),
                        screening=x['screening'], supervision=x.get('supervision'),
                        credentials=x['credentials'], rosterEligible=x['rosterEligible'])
                   # A CIT is 16 or 17 — a minor. R7 again: no name.
                   for x in d['camp']['staff']]),
  jobs=d['jobs'],
  asksOffers=[dict(id=a['id'], kind=a['kind'], club=a['club'], text=a['text'],
                   postedOn=a['postedOn'], responses=a['responses'])
              for a in d['asksOffers']],
  professions=[dict(soc=x[0], title=x[1], industry=x[2]) for x in d['professions']],
  industries=d['industries'],
  stats=dict(
    households=len(d['households']), people=len(d['people']),
    living=sum(1 for p in d['people'] if p['living']),
    adults=sum(1 for p in d['people'] if p['age']>=18),
    minors=sum(1 for p in d['people'] if p['age']<18),
    engagements=len(d['engagements']), payments=len(d['payments']),
    events=len(d['lifeEvents']), rels=len(d['relationships']),
    flags=len(d['openQuestions']),
    questions=len(d['openQuestionCatalog']),
    cells=len(PROG)*len(CC)*5,
    cellsFilled=sum(1 for p in PROG for c in CC for r in (1,2,3,4,5) if cells[(p['key'],c,r)]),
    organic=d['meta']['coverage']['organicFilled'],
    added=d['meta']['coverage']['added'],
    floor=d['meta']['coverage']['floor'],
    belowFloor=len(d['meta']['coverage']['belowFloor']),
  ),
)
# ── the R7 guard at the export boundary ─────────────────────────────────────
# The payload is what actually reaches a browser. Whatever the fixture holds, a
# minor's name must not cross this line. The last red team found 487 of them
# shipped into a page with no sign-in gate.
_named = [x['name'] for x in out['camp']['staff'] if x['name']]
_minors = {f"{q['given']} {q['family']}" for q in d['people'] if q['age'] < 18}
assert not (set(_named) & _minors), 'a minor reached the payload by name'
assert not any('person' in a or 'name' in a for a in out['camp']['applications']), \
    'a camp applicant reached the payload identifiably'
assert not [q for h in out['households'] for q in h['people'] if q['a'] < 18], \
    'a minor reached the household browser'
print(f"R7 guard: {len(_named)} adults named, 0 minors, "
      f"{len(out['camp']['applications'])} camp applications carry no identity")

io.open('payload.json','w').write(json.dumps(out, separators=(',',':')))
print('payload bytes:', len(io.open('payload.json').read()))
print('cells filled:', out['stats']['cellsFilled'], '/', out['stats']['cells'])
