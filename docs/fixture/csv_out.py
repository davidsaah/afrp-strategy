# -*- coding: utf-8 -*-
"""Flatten the fixture to CSV so it loads anywhere — Excel, pandas, a test harness."""
import json, csv, io, os
d = json.load(open('/home/claude/fixture/afrp-fixture.json'))
OUT = '/home/claude/fixture/csv'; os.makedirs(OUT, exist_ok=True)
HH = {h['id']: h for h in d['households']}

def w(name, rows, cols):
    with io.open(f'{OUT}/{name}.csv', 'w', newline='', encoding='utf-8') as f:
        c = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore'); c.writeheader()
        for r in rows: c.writerow(r)
    print(f'  {name}.csv  {len(rows)} rows')

people = []
for p in d['people']:
    m = p.get('membership') or {}
    hh = HH.get(p.get('householdId')) or {}
    people.append(dict(
        person_id=p['id'], given=p['given'], family=p['family'], clan=p['clan'] or '',
        clan_ambiguous=p['clanAmbiguous'], sex=p['sex'], birth_year=p['birthYear'], age=p['age'],
        living=p['living'], deceased_year=p['deceasedYear'] or '',
        household_id=p.get('householdId') or '', household_structure=hh.get('structure', ''),
        club=p.get('club') or '', eligibility_basis=p['eligibilityBasis'],
        membership_class=m.get('nationalClass', ''), standing=m.get('standing', ''),
        club_of_record=m.get('clubOfRecord', ''), club_count=len(m.get('clubs', [])),
        directory_include=p['directoryInclude'], marketing_consent=p.get('marketingConsent', ''),
        dates_public=p['datesVisibleWithoutSignIn'],
        two_households=p.get('twoHouseholds', False),
        second_household_club=p.get('secondHouseholdClub', ''),
        membership_note=p.get('membershipNote', ''),
    ))
w('people', people, list(people[0]))

w('households', [dict(household_id=h['id'], club=h['club'], structure=h['structure'],
                      structure_label=h['structureLabel'], adults=len(h['adults']),
                      minors=len(h['minors']), joined_year=h['joinedYear'],
                      open_questions='; '.join(h['openQuestions']))
                 for h in d['households']],
  ['household_id','club','structure','structure_label','adults','minors','joined_year','open_questions'])

w('relationships', [dict(rel_id=r['id'], person_a=r['a'], person_b=r['b'], kind=r['kind'],
                         relation=r.get('relation',''), status=r.get('status',''),
                         since=r.get('since',''), ended_year=r.get('endedYear',''),
                         legal_basis=r.get('legalBasis') or '')
                    for r in d['relationships']],
  ['rel_id','person_a','person_b','kind','relation','status','since','ended_year','legal_basis'])

w('life_events', [dict(event_id=e['id'], kind=e['kind'], year=e['year'],
                       subjects='; '.join(e['subjects']), approved=e.get('approved',''),
                       published=e.get('published',''), gate=e.get('gate',''),
                       automatic=e.get('automatic',''),
                       proposed_club_transfer=e.get('proposedClubTransfer',''),
                       note=e.get('note',''))
                  for e in d['lifeEvents']],
  ['event_id','kind','year','subjects','approved','published','gate','automatic',
   'proposed_club_transfer','note'])

PN = {p['key']: p['name'] for p in d['programs']}
w('engagements', [dict(engagement_id=g['id'], person_id=g['person'], club=g['club'],
                       program=g['program'], program_name=PN[g['program']], rung=g['rung'],
                       rung_name=g['rungName'], evidence=g['evidence'], year=g['year'],
                       source=g['source'])
                  for g in d['engagements']],
  ['engagement_id','person_id','club','program','program_name','rung','rung_name','evidence','year','source'])

w('payments', [dict(payment_id=x['id'], person_id=x['person'], kind=x['kind'], year=x['year'],
                    gross_usd=x['grossCents']/100, fee_usd=x['processingFeeCents']/100,
                    net_usd=x['netCents']/100, host_entity=x['hostEntity'],
                    treatment=x['treatment'], program=x['program'] or '',
                    fund_class=x['fundClass'], club_class_attribution_only=x['clubClass'],
                    note=x['note'])
               for x in d['payments']],
  ['payment_id','person_id','kind','year','gross_usd','fee_usd','net_usd','host_entity',
   'treatment','program','fund_class','club_class_attribution_only','note'])

w('open_questions', [dict(flag_id=f['id'], key=f['key'], bylaw=f['bylaw'],
                          subjects='; '.join(f['subjects']), decided=f['decided'],
                          question=f['question'], fixture_does=f['fixtureDoes'],
                          routes_to=f['routesTo'], note=f['note'])
                     for f in d['openQuestions']],
  ['flag_id','key','bylaw','subjects','decided','question','fixture_does','routes_to','note'])
