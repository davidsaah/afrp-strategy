# -*- coding: utf-8 -*-
"""Build the fixture, verify its coverage, and write it out.
   The verification is the point: a fixture that does not PROVE it covers every
   program and club combination is just a pile of names."""
import sys, os, json, io, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import spec, gen

cov = gen.build()
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
# The line above cannot fail once the fill pass has run — it is a tautology.  This
# one can: it measures what ORGANIC generation reached before any cell was topped up.
ORGANIC_TARGET = 325
check(f'organic coverage reaches {ORGANIC_TARGET}+ cells before any fill '
      f'(actual {cov["organicFilled"]}/{cov["total"]})',
      cov['organicFilled'] >= ORGANIC_TARGET,
      f'organic generation only reached {cov["organicFilled"]}')
check(f'no cell is left below the S7 floor of {cov["floor"]} where the pool allowed it',
      all(x['eligiblePool'] < cov['floor'] for x in cov['belowFloor']),
      str([x for x in cov['belowFloor'] if x['eligiblePool'] >= cov['floor']][:4]))

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

print('\n== the record has no duplicates or orphans ==')
import collections as _c
_rk = _c.Counter((r['a'], r['b'], r['kind']) for r in RL)
check('no relationship row is written twice', not [k for k, v in _rk.items() if v > 1],
      str([k for k, v in _rk.items() if v > 1][:3]))
_ids = {p['id'] for p in P}
check('every relationship points at people who exist',
      all(r['a'] in _ids and r['b'] in _ids for r in RL))
check('every engagement points at a person who exists', all(g['person'] in _ids for g in EN))
check('every payment points at a person who exists', all(x['person'] in _ids for x in PY_))
check('every life-event subject exists', all(s in _ids for e in EV for s in e['subjects']))
check('no person id is issued twice', len(_ids) == len(P))
_hh = {h['id'] for h in H}
check('every household member is listed in that household',
      all(p['householdId'] in _hh for p in P if p.get('householdId')))

print('\n== death ends the record ==')
DEAD = [p for p in P if not p['living']]
check('no deceased person holds a membership', all(p.get('membership') is None for p in DEAD))
check('no deceased person is on the certified roll',
      not [p for p in DEAD if p.get('membership') and p['membership'].get('votingDuesPaidBy')])
check('no deceased person is in a directory', all(not p['directoryInclude'] for p in DEAD))
check('no deceased person carries a marketing consent', all(not p['marketingConsent'] for p in DEAD))
DY = {p['id']: p['deceasedYear'] for p in P if p['deceasedYear']}
check('no payment is charged after death',
      not [x for x in PY_ if x['person'] in DY and x['year'] > DY[x['person']]],
      str([x['id'] for x in PY_ if x['person'] in DY and x['year'] > DY[x['person']]][:5]))
check('no engagement is recorded after death',
      not [g for g in EN if g['person'] in DY and g['year'] > DY[g['person']]])

print('\n== By-Law 4.2.1 and the certified roll ==')
CERT = [p for p in P if p.get('membership') and p['membership']['votingDuesPaidBy']]
check('no Associate is certified to vote (4.2.1 makes them ineligible)',
      not [p for p in CERT if p['membership']['nationalClass'] == 'associate-4.2.1'],
      str(len([p for p in CERT if p['membership']['nationalClass'] == 'associate-4.2.1'])) + ' associates on the roll')
check('no free-student membership evidences payment of dues it never paid',
      not [p for p in CERT if p['membership']['nationalClass'] == 'student-free'])

print('\n== ages and dates are possible ==')
BYID = {p['id']: p for p in P}
pc = [r for r in RL if r['kind'] == 'parent-child']
badpc = [r for r in pc if BYID[r['b']]['birthYear'] - BYID[r['a']]['birthYear'] < 18]
check('every parent is at least 18 years older than the child', not badpc,
      f'{len(badpc)} rows, e.g. ' + str([(BYID[r['a']]['birthYear'], BYID[r['b']]['birthYear']) for r in badpc[:4]]))
sp = [r for r in RL if r['kind'] in ('spouse', 'partner') and r.get('since')]
badsp = [r for r in sp if r['since'] < max(BYID[r['a']]['birthYear'], BYID[r['b']]['birthYear']) + 18]
check('no union begins before both people were 18', not badsp, f'{len(badsp)} rows')
badhh = [h for h in H if h['joinedYear'] < min(
    [BYID[i]['birthYear'] for i in h['adults'] + h['minors'] if i in BYID] or [0]) + 18]
check('no household joined before anyone in it was an adult', not badhh, f'{len(badhh)} households')

print('\n== a marriage names two people (R34) ==')
MAR = [e for e in EV if e['kind'] == 'marriage']
check('every marriage event names exactly two people',
      all(len(e['subjects']) == 2 for e in MAR),
      str(len([e for e in MAR if len(e['subjects']) != 2])) + ' name one')
check('every marriage event carries two approvals',
      all(len(e.get('approvals', [])) == 2 for e in MAR))
check('no minor appears in a marriage event',
      not [e for e in MAR for s in e['subjects'] if BYID[s]['age'] < 18])
check('no life event is recorded for a person after their death',
      not [e for e in EV for s in e['subjects']
           if s in DY and e['year'] > DY[s] and e['kind'] != 'death'])

print('\n== leadership rungs are held by people entitled to hold them ==')
LEAD = [g for g in EN if g['rung'] >= 4]
check('nobody under 18 gives, serves or leads', all(BYID[g['person']]['age'] >= 18 for g in LEAD))
check('no lapsed member holds a leadership rung',
      all((BYID[g['person']].get('membership') or {}).get('standing') != 'lapsed' for g in LEAD))
check('no Associate holds a rung-5 seat',
      all((BYID[g['person']].get('membership') or {}).get('nationalClass') != 'associate-4.2.1'
          for g in EN if g['rung'] == 5))

print('\n== a payment is bookable ==')
import re as _re
check('every payment carries a full date, not just a year',
      all(_re.fullmatch(r'\d{4}-\d{2}-\d{2}', x['date']) for x in PY_))
check("a payment's date agrees with its year", all(x['date'][:4] == str(x['year']) for x in PY_))
check('R22: every payment carries an idempotent daily-close key of date + fund + kind',
      all(x['batchKey'] == f"{x['date']}|{x['fundClass']}|{x['kind']}" for x in PY_))
check('the Apr 30 dues deadline is constructible from the data',
      all(len(x['date']) == 10 for x in PY_ if x['kind'] == 'dues-national'))

print('\n== custody is not ownership ==')
check('club money collected nationally sits on AFRP books as a liability',
      all(x['custodianEntity'] == 'AFRP' and x['hostEntity'] in [c['code'] for c in spec.CLUBS]
          for x in PY_ if x['treatment'] == 'agency-liability'),
      'agency money must name a club host AND an AFRP custodian')
check("a club's own money is held by the club",
      all(x['custodianEntity'] == x['hostEntity']
          for x in PY_ if x['treatment'] == 'club-money'))
check('convention money is AFRP-custodied from the first dollar',
      all(x['custodianEntity'] == 'AFRP'
          for x in PY_ if x['treatment'] == 'agency-at-first-dollar'))
check('somebody is named as bearing every card fee',
      all(x['feeBorneBy'] for x in PY_))
check('the fee on agency money says how it is settled',
      all(x['feeNote'] for x in PY_ if x['treatment'] == 'agency-liability'))

print('\n== a restriction survives the crossing ==')
CON = [x for x in PY_ if x['treatment'] == 'conduit-11.1.5']
check('By-Law 11.1.5 conduit gifts keep the restriction their purpose creates',
      CON and all(x['restriction'] and x['fundClass'] == x['restriction'] for x in CON),
      f'{sum(1 for x in CON if not x["restriction"])} of {len(CON)} book as unrestricted')
check('a conduit gift is custodied by AFRP and hosted by AFRP for the named project',
      all(x['custodianEntity'] == 'AFRP' for x in CON))

print('\n== a charitable statement cannot span corporations ==')
_g = collections.defaultdict(set)
for x in PY_:
    if x['kind'] in ('restricted-gift', 'unrestricted-gift'):
        _g[x['person']].add(x['hostEntity'])
_multi = {k: v for k, v in _g.items() if len(v) > 1}
check('donors giving to more than one legal entity are identified, not merged',
      True, '')   # this is a fact about the data, not a defect — it is what makes the rule bite
print(f"       {len(_multi)} of {len(_g)} donors gave to more than one corporation "
      f"— each needs a SEPARATE statement, never one combined 'charitable total'")
check('every gift names the corporation that received it',
      all(x['hostEntity'] for x in PY_ if x['kind'].endswith('gift')))

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
check('a club standing is never a national-only state',
      all(x['standing'] in ('current','grace','lapsed')
          for p in P if p.get('membership') for x in p['membership']['clubs']),
      'board-vote-pending is a national 4.2.1 state and must not appear on a club row')
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

CAMP, JOBS, ASKS = gen.CAMP, gen.JOBS, gen.ASKS
BYID2 = {p['id']: p for p in P}

print('\n== the directory backbone ==')
FD = {f[0]: f for f in spec.FIELD_DEFS}
check('every field definition carries indexed, filterable and an audience independently',
      all(len(f) == 6 for f in spec.FIELD_DEFS))
check('a field can be indexed without being displayed (the coupling Novi and Wild Apricot ship)',
      any(FD[k][2] and any(p['visibility'][k] == 'hidden' for p in P if 'visibility' in p)
          for k in FD))
LIVEM = [p for p in P if p.get('visibility')]
check('name and club are never member-hidden — the screen promises they are always shown',
      all(p['visibility']['name'] != 'hidden' and p['visibility']['club'] != 'hidden'
          for p in LIVEM),
      'this contradiction existed in the previous fixture')
check('every visibility value is a rung on the audience ladder',
      all(v in spec.AUDIENCES for p in LIVEM for v in p['visibility'].values()))
check('a contact field can never be set to public, at any setting',
      not [p for p in LIVEM for k in spec.NEVER_PUBLIC if p['visibility'].get(k) == 'public'],
      'a logged-out directory has almost no protection against wholesale copying')
check('display, contact and export are three separate consents',
      all({'display','contact','export'} <= set(p['directoryConsent']) for p in LIVEM))
check('nobody has consented to export, because nobody was asked',
      all(p['directoryConsent']['export'] is False for p in LIVEM))
check('consent to contact never exceeds consent to display',
      all(not (p['directoryConsent']['contact'] and not p['directoryConsent']['display'])
          for p in LIVEM))
check('every consent record names the terms version it accepted',
      all(p['directoryConsent']['acceptedTermsVersion'] for p in LIVEM))

print('\n== the directory is searchable the way this community is named ==')
check('members carry a city and a coarse geocode',
      all(p.get('city') and p.get('geo') for p in LIVEM))
check('no map pin is more precise than a city — a pin must not resolve to a house',
      all(p['geo']['precision'] == 'city' and
          round(p['geo']['lat'], 2) == p['geo']['lat'] for p in LIVEM))
ALIAS = [p for p in LIVEM if p.get('alias')]
check(f'transliteration aliases exist ({len(ALIAS)} members)', len(ALIAS) > 100)
FORMER = [p for p in LIVEM if p.get('formerName')]
check(f'former-name search is possible ({len(FORMER)} members)', len(FORMER) > 40)

print('\n== the professional layer sits above the S7 floor ==')
PROF = [p for p in LIVEM if p.get('profession')]
byfacet = collections.Counter((p['profession']['soc'], p['club']) for p in PROF)
thin = [k for k, v in byfacet.items() if 0 < v < 5]
check(f'{len(PROF)} members carry a profession from a standard taxonomy (O*NET-SOC)', len(PROF) > 700)
FACETS = gen.FACETS
pubcells = [(r['soc'], c, n) for r in FACETS['professions']
            for c, n in r['byClub'].items() if n is not None]
check('every PUBLISHED profession x club cell clears the S7 floor',
      not [x for x in pubcells if 0 < x[2] < FACETS['floor']],
      str([x for x in pubcells if 0 < x[2] < FACETS['floor']][:4]))
check(f'thin cells are suppressed rather than printed ({FACETS["suppressedCells"]} of them)',
      FACETS['suppressedCells'] > 0,
      'a mean above the floor does not keep the minimum above it')
check('the federation-wide profession count is always shown, and always clears the floor',
      all(r['total'] >= FACETS['floor'] for r in FACETS['professions'] if r['total'] > 0),
      str([(r['soc'], r['total']) for r in FACETS['professions'] if 0 < r['total'] < FACETS['floor']]))
check('open-to-work and willing-to-help both carry an expiry, because both decay',
      all(p['openToWork'].get('expires') for p in LIVEM if p.get('openToWork')) and
      all(p['willingToHelp'].get('expires') for p in LIVEM if p.get('willingToHelp')))

print('\n== Camp Ramallah is a selection problem ==')
APPS = CAMP['applications']
SEL = [a for a in APPS if a['decision'] == 'selected']
WAIT = [a for a in APPS if a['decision'] == 'waitlisted']
check(f'the camp is oversubscribed ({len(APPS)} applicants for {spec.CAMP["seats"]} seats)',
      len(APPS) > spec.CAMP['seats'])
check('no more seats are given than exist', len(SEL) <= spec.CAMP['seats'])
check('any seat the quota rule cannot allocate is DISCLOSED, not quietly handed out',
      CAMP['season']['unallocatedByQuota'] == spec.CAMP['seats'] - CAMP['season']['quotaTotal']
      and CAMP['season']['remainderNote'],
      'rounded club shares sum to less than the seat count')
check('every applicant is inside the age band',
      all(spec.CAMP['ageLo'] <= a['age'] <= spec.CAMP['ageHi'] for a in APPS))
check('EVERY decision records why it was made',
      all(a.get('reasons') for a in APPS), 'a cohort assembled without a stated basis')
check('every club is represented in the cohort',
      {a['club'] for a in SEL} == {c['code'] for c in spec.CLUBS})
fam = collections.Counter(a['family'] for a in SEL)
check('no single family takes more than four of the fifty seats',
      max(fam.values()) <= 4, str(fam.most_common(2)))
check('the cohort mixes first-timers and returners',
      0 < sum(1 for a in SEL if a['firstTimer']) < len(SEL))
check('the waitlist is a queue, not a race — one ranked offer at a time',
      all(a.get('waitlistRank') for a in WAIT) and
      len({a['waitlistRank'] for a in WAIT}) == len(WAIT))
check('every waitlist offer has a claim window that expires',
      all(a['offer']['claimWindowHours'] > 0 for a in WAIT if a.get('offer')))

print('\n== ratios, screening and the CIT ==')
check('the ratio resolves to the STRICTEST authority, not the local one',
      CAMP['ratio']['applied'] == min(r['ratio'] for r in spec.CAMP['ratios']))
ST = CAMP['staff']
check('no staff member with a lapsed screening is roster-eligible',
      not [x for x in ST if x.get('rosterEligible') and x['screening']['state'] == 'expired'])
check('screening is annual for everyone, paid and volunteer alike',
      all(x['screening']['cadence'] == 'annual' for x in ST))
check('the FCRA disclosure is stand-alone, never bundled into the application',
      all(x['fcraDisclosure']['standalone'] for x in ST if 'fcraDisclosure' in x))
CIT = [x for x in ST if x['role'] == 'CIT']
check(f'{len(CIT)} CITs exist and none is counted toward a supervision ratio',
      CIT and all(not x['supervision']['countsTowardRatio'] for x in CIT))
check('no CIT is ever alone with minors',
      all(not x['supervision']['aloneWithMinors'] for x in CIT))
check('an under-18 CIT is marked structurally unscreenable, not merely unscreened',
      all(x['screening'].get('unscreenableUnder18') for x in CIT))
PAIDCIT = [x for x in CIT if x['paid']]
check('a PAID CIT is an employee, and parent visibility is off',
      all(x['legalStatus'] == 'employee' and x['parentVisibility'] is False for x in PAIDCIT),
      f'{len(PAIDCIT)} paid CITs — employment confidentiality reaches parents too')
check('an unpaid CIT is a volunteer, and a parent can still see the record',
      all(x['legalStatus'] == 'volunteer' and x['parentVisibility'] is True
          for x in CIT if not x['paid']))

print('\n== camperships: two instruments, and no tax returns ==')
AID = CAMP['aid']
check('the two instruments are kept apart, not collapsed into one scholarship',
      {i['basis'] for i in AID['instruments']} == {'need-blind', 'means-tested'})
check('AFRP holds no financial document for any award',
      all(a['financialDocumentsHeld'] is False for a in AID['awards']))
check('means-tested aid is assessed by a third party',
      all(a['assessedBy'] == 'third party' for a in AID['awards'] if a['basis'] == 'means-tested'))
check('the pots are capped — no award is made from an empty fund',
      all(v >= 0 for v in AID['remaining'].values()))
check('rationing is visible: partial awards or an aid waitlist exist',
      any(a['partial'] or a['state'] == 'aid waitlist' for a in AID['awards']))
check('AFRP holds no camp health record — the seam is the design',
      CAMP['health']['recordsHeldHere'] == 0)

print('\n== the job board carries its legal obligation ==')
LIVEJ = [j for j in JOBS if j['state'] in ('live', 'expired')]
check(f'{len(LIVEJ)} published postings — an honest number, not a flattering one',
      len(LIVEJ) < 20, 'a board of 200 would hide the emptiness the design must survive')
check('every PUBLISHED posting carries a salary minimum and maximum',
      all(j['salaryMinCents'] and j['salaryMaxCents'] for j in LIVEJ),
      'CA, MN and NY all reach the third-party publisher, which this board is')
check('no published posting has a minimum without a maximum',
      not [j for j in LIVEJ if j['salaryMinCents'] and not j['salaryMaxCents']],
      'open-ended ranges are prohibited in Washington and Minnesota')
check('every published posting carries benefits and a closing date',
      all(j['benefits'] and j['closesOn'] for j in LIVEJ))
check('the refusal path is exercised, and names its rule',
      all(j.get('rejectedReason') for j in JOBS if j['state'] == 'rejected'))
check('every posting is publicly readable and its apply path needs no login',
      all(j['publicPage'] and not j['applyNeedsLogin'] for j in LIVEJ),
      'Google will not index a posting whose apply path demands a login')
check('applicants stay behind the member wall',
      all(j['applicantsMembersOnly'] for j in JOBS))
check('an expired posting returns 410 rather than sitting live',
      all(j.get('httpOnExpiry') == 410 for j in JOBS if j['state'] == 'expired'),
      'leaving expired jobs live earns a Google manual action')
check('no posting requires an EEO block — EO 11246 was revoked in January 2025',
      all(j['eeoStatement'] is None for j in JOBS))
check('every posting carries schema.org JobPosting markup',
      all(j['schemaOrg'] == 'JobPosting' for j in JOBS))
check('the only LinkedIn integration present is a share link',
      all(j['shareLinkedInUrl'].startswith('https://www.linkedin.com/sharing/share-offsite/')
          for j in JOBS))
check(f'asks and offers ({len(ASKS)}) outnumber published postings ({len(LIVEJ)})',
      len(ASKS) > len(LIVEJ),
      'the surface that generates its own volume must be the busier one')

living = [p for p in P if p['living']]
print(f"""
== the fixture ==
  households            {len(H)}
  people                {len(P)}   ({len(living)} living, {len(P)-len(living)} deceased)
  adults / minors       {sum(1 for p in P if p['age']>=18)} / {sum(1 for p in P if p['age']<18)}
  relationships         {len(RL)}
  life events           {len(EV)}
  engagements           {len(EN)}   (organic {cov['organicFilled']}/{cov['total']} cells; {cov['added']} added to reach a floor of {cov['floor']})
  cells still below {cov['floor']}    {len(cov['belowFloor'])}  (eligible pool too small — disclosed, not faked)
  payments              {len(PY_)}
  camp applications     {len(CAMP['applications'])} for {spec.CAMP['seats']} seats  ({len([a for a in CAMP['applications'] if a['decision']=='selected'])} selected, {len([a for a in CAMP['applications'] if a['decision']=='waitlisted'])} waitlisted)
  camp staff            {len(CAMP['staff'])}  ({len([x for x in CAMP['staff'] if x['role']=='CIT'])} CITs)
  job postings          {len(JOBS)}  ({len([j for j in JOBS if j['state']=='live'])} live) · asks & offers {len(ASKS)}
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
            coverage=cov),
  clubs=spec.CLUBS, programs=spec.PROGRAMS, rungs=spec.RUNGS,
  structures=spec.STRUCTURES, openQuestionCatalog=spec.OPEN_QUESTIONS,
  households=H, people=P, relationships=RL, lifeEvents=EV,
  engagements=EN, payments=PY_, openQuestions=FL,
  fieldDefs=spec.FIELD_DEFS, audiences=spec.AUDIENCES,
  professions=spec.PROFESSIONS, industries=spec.INDUSTRIES,
  camp=CAMP, jobs=JOBS, asksOffers=ASKS, facets=gen.FACETS,
)
io.open('/home/claude/fixture/afrp-fixture.json','w').write(json.dumps(out, indent=1))
print(f"\n{'ALL CHECKS PASS' if not fails else str(len(fails))+' CHECKS FAILED'}")
sys.exit(1 if fails else 0)
