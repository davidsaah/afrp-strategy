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
        city=p.get('city',''), state=p.get('state',''),
        alias=p.get('alias',''), former_name=p.get('formerName',''),
        profession=(p.get('profession') or {}).get('title',''),
        profession_soc=(p.get('profession') or {}).get('soc',''),
        industry=(p.get('industry') or {}).get('label',''),
        languages='; '.join(p.get('languages') or []),
        interests='; '.join(p.get('interests') or []),
        open_to_work=bool(p.get('openToWork')),
        open_to_work_expires=(p.get('openToWork') or {}).get('expires',''),
        willing_to_help='; '.join((p.get('willingToHelp') or {}).get('kinds') or []),
        vis_city=(p.get('visibility') or {}).get('city',''),
        vis_email=(p.get('visibility') or {}).get('email',''),
        vis_phone=(p.get('visibility') or {}).get('phone',''),
        vis_profession=(p.get('visibility') or {}).get('profession',''),
        consent_display=(p.get('directoryConsent') or {}).get('display',''),
        consent_contact=(p.get('directoryConsent') or {}).get('contact',''),
        consent_export=(p.get('directoryConsent') or {}).get('export',''),
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

PN2 = {p['id']: p for p in d['people']}
def nm(pid):
    q = PN2.get(pid); return f"{q['given']} {q['family']}" if q else pid

CAMP = d.get('camp') or {}
if CAMP:
    w('camp_applications', [dict(
        application_id=a['id'], camper=nm(a['person']), age=a['age'], club=a['club'],
        family=a['family'], clan=a['clan'] or '', first_timer=a['firstTimer'],
        returner=a['returner'], submitted=a['submitted'], aid_requested=a['aidRequested'],
        decision=a['decision'], reasons='; '.join(a.get('reasons') or []),
        waitlist_rank=a.get('waitlistRank',''),
        offer_state=(a.get('offer') or {}).get('state',''))
        for a in CAMP['applications']],
      ['application_id','camper','age','club','family','clan','first_timer','returner',
       'submitted','aid_requested','decision','reasons','waitlist_rank','offer_state'])

    w('camp_staff', [dict(
        staff_id=x['id'], person=nm(x['person']), role=x['role'], club=x['club'],
        paid=x['paid'], legal_status=x.get('legalStatus',''),
        parent_visibility=x.get('parentVisibility',''),
        screening_state=x['screening']['state'], last_checked=x['screening'].get('lastCheckedOn') or '',
        cadence=x['screening']['cadence'],
        unscreenable_under_18=x['screening'].get('unscreenableUnder18',''),
        counts_toward_ratio=(x.get('supervision') or {}).get('countsTowardRatio',''),
        alone_with_minors=(x.get('supervision') or {}).get('aloneWithMinors',''),
        roster_eligible=x['rosterEligible'],
        credentials='; '.join(f"{c['kind']} exp {c['expires']}" for c in x['credentials']))
        for x in CAMP['staff']],
      ['staff_id','person','role','club','paid','legal_status','parent_visibility',
       'screening_state','last_checked','cadence','unscreenable_under_18',
       'counts_toward_ratio','alone_with_minors','roster_eligible','credentials'])

    APPBY = {a['id']: a for a in CAMP['applications']}
    w('camp_camperships', [dict(
        award_id=a['id'], camper=nm(APPBY[a['application']]['person']),
        instrument=a['instrument'], basis=a['basis'],
        requested_usd=a['requestedCents']/100, awarded_usd=a['awardedCents']/100,
        partial=a['partial'], state=a['state'],
        assessed_by=a['assessedBy'] or '', financial_documents_held=a['financialDocumentsHeld'])
        for a in CAMP['aid']['awards']],
      ['award_id','camper','instrument','basis','requested_usd','awarded_usd','partial',
       'state','assessed_by','financial_documents_held'])

JOBS = d.get('jobs') or []
if JOBS:
    w('job_postings', [dict(
        job_id=j['id'], title=j['title'], employer=j['employer'], location=j['location'],
        state=j['state'], posted_on=j['postedOn'], closes_on=j['closesOn'],
        salary_min_usd=(j['salaryMinCents'] or 0)/100, salary_max_usd=(j['salaryMaxCents'] or 0)/100,
        benefits=j['benefits'], apply_needs_login=j['applyNeedsLogin'],
        public_page=j['publicPage'], applicants_members_only=j['applicantsMembersOnly'],
        http_on_expiry=j.get('httpOnExpiry',''), rejected_reason=j.get('rejectedReason',''),
        posted_by=nm(j['postedBy']))
        for j in JOBS],
      ['job_id','title','employer','location','state','posted_on','closes_on',
       'salary_min_usd','salary_max_usd','benefits','apply_needs_login','public_page',
       'applicants_members_only','http_on_expiry','rejected_reason','posted_by'])

    w('asks_and_offers', [dict(id=a['id'], kind=a['kind'], person=nm(a['person']),
        club=a['club'], text=a['text'], posted_on=a['postedOn'], responses=a['responses'])
        for a in d['asksOffers']],
      ['id','kind','person','club','text','posted_on','responses'])

w('open_questions', [dict(flag_id=f['id'], key=f['key'], bylaw=f['bylaw'],
                          subjects='; '.join(f['subjects']), decided=f['decided'],
                          question=f['question'], fixture_does=f['fixtureDoes'],
                          routes_to=f['routesTo'], note=f['note'])
                     for f in d['openQuestions']],
  ['flag_id','key','bylaw','subjects','decided','question','fixture_does','routes_to','note'])
