# -*- coding: utf-8 -*-
"""AFRP synthetic fixture — the vocabulary.  Everything here matches the platform's
   own rules dossier (RULES.md) and the engagement ladder, so the fixture exercises
   the real invariants rather than a parallel invented model."""

AS_OF = 2026          # the fixture's "today" — fixed, never Date.now()
SEED  = 19520000      # AFRP est. 1952; deterministic

# ── The four clubs ───────────────────────────────────────────────────────────
# Sizes follow Shaheen 1982, p.11, which names exactly these four as the largest
# concentrations of Ramallah people in the United States.
CLUBS = [
    dict(code='SF',  name='San Francisco',       shaheen=3000, share=.375, tz='America/Los_Angeles',
         integration='platform-native'),      # R42 door 3
    dict(code='DET', name='Detroit',             shaheen=2000, share=.250, tz='America/Detroit',
         integration='live-feed'),            # R42 door 1
    dict(code='JAX', name='Jacksonville',        shaheen=1500, share=.1875, tz='America/New_York',
         integration='manual-roster'),        # R42 door 2
    dict(code='DC',  name='Greater Washington',  shaheen=1500, share=.1875, tz='America/New_York',
         integration='platform-native'),
]

# ── The nineteen programs ────────────────────────────────────────────────────
# host: which legal entity receives money for this program (R23 — money routes by HOST)
# band: (min_age, max_age) a person must fall in to take part at rung >= 3
PROGRAMS = [
 dict(key='camp',      name='Camp Ramallah',                        host='AFRP',   band=(8,16),  flagship=True),
 dict(key='leadership',name='Leadership Ramallah',                  host='AFRP',   band=(21,35), flagship=True),
 dict(key='scholarship',name='The Scholarship',                     host='ARFECF', band=(17,24), flagship=True),
 dict(key='medical',   name='Medical Mission',                      host='ARFHSN', band=(22,None),flagship=True),
 dict(key='rbpn',      name='RBPN',                                 host='AFRP',   band=(22,None),flagship=True),
 dict(key='convention',name='The Convention',                       host='AFRP',   band=(0,None), flagship=True),
 dict(key='arabic',    name='The Arabic Program',                   host='AFRP',   band=(5,None)),
 dict(key='hope',      name='Project Hope',                         host='ARFHSN', band=(18,None)),
 dict(key='w2w',       name='Women to Women',                       host='ARFHSN', band=(18,None), women_only=True),
 dict(key='ohss',      name='Outstanding High School Senior Award', host='AFRP',   band=(17,18)),
 dict(key='els',       name='Emerging Leaders Summit',              host='AFRP',   band=(16,24)),
 dict(key='doa',       name='Day of Action',                        host='AFRP',   band=(14,None)),
 dict(key='congress',  name='Congressional Outreach',               host='AFRP',   band=(18,None)),
 dict(key='tree',      name='The Family Tree',                      host='AFRP',   band=(0,None)),
 dict(key='preserve',  name='The Preservation Project',             host='AFRP',   band=(18,None)),
 dict(key='exchange',  name='Educational & Cultural Exchange',      host='AFRP',   band=(16,None)),
 dict(key='magazine',  name='The Magazine',                         host='AFRP',   band=(0,None)),
 dict(key='senior',    name='Senior Living',                        host='Foundation', band=(62,None)),
 dict(key='bookstore', name='The Bookstore',                        host='AFRP',   band=(0,None)),
]
PROGRAM_KEYS = [p['key'] for p in PROGRAMS]

RUNGS = {1:'Hear', 2:'Show up', 3:'Take part', 4:'Give or serve', 5:'Lead'}

# Evidence the platform can actually observe.  R: "No rung without evidence."
EVIDENCE = {
 1: ['on the club mailing list', 'opened the program announcement', 'named it on the interest form'],
 2: ['attended one session', 'opened the newsletter', 'came to the info night'],
 3: ['enrolled for the season', 'application submitted', 'completed the term'],
 4: ['recorded gift', 'volunteer shift logged', 'chaperone assignment', 'mentor match'],
 5: ['committee roster seat', 'chaired a meeting with minutes', 'trustee appointment'],
}

# ── Household structures ─────────────────────────────────────────────────────
# `open_q` names a by-law question the fixture FLAGS and refuses to decide.
STRUCTURES = [
 dict(key='married-both-descent',  w=.155, label='Married couple, both of Ramallah descent'),
 dict(key='married-one-descent',   w=.150, label='Married couple, one of descent, one married in'),
 dict(key='married-multigen',      w=.075, label='Three generations under one roof'),
 dict(key='single-never-married',  w=.075, label='Adult living alone, never married'),
 dict(key='widowed',               w=.070, label='Widowed member, adult children elsewhere'),
 dict(key='divorced-custodial',    w=.070, label='Divorced, children primarily with this parent'),
 dict(key='divorced-remarried',    w=.070, label='Divorced and remarried; blended household',
      open_q='minor-two-households'),
 dict(key='divorced-marriedin-ex', w=.045, label='Divorced; the member of descent was the EX',
      open_q='eligibility-survives-divorce'),
 dict(key='samesex-one-descent',   w=.045, label='Same-sex married couple, one of descent',
      open_q='samesex-married-to'),
 dict(key='samesex-both-descent',  w=.030, label='Same-sex married couple, both of descent'),
 dict(key='samesex-with-children', w=.030, label='Same-sex married couple raising children',
      open_q='samesex-parentage-on-tree'),
 dict(key='unmarried-partners',    w=.040, label='Long-term unmarried partners',
      open_q='partner-not-married-to'),
 dict(key='adoptive',              w=.035, label='Adoptive parents', open_q=None),
 dict(key='guardianship',          w=.025, label='Minor in the care of a non-parent guardian',
      open_q='guardian-pickup-authority'),
 dict(key='adult-child-at-home',   w=.035, label='Adult child living with a parent'),
 dict(key='senior-couple',         w=.030, label='Retired couple, one in assisted living'),
 dict(key='single-parent-never-married', w=.020, label='Single parent, never married'),
]

# ── The open by-law questions, stated as questions ───────────────────────────
OPEN_QUESTIONS = {
 'samesex-married-to': dict(
   bylaw='4.1.1',
   question='By-Law 4.1.1 admits a person "married to one having such origin". The text is '
            'gender-neutral and names no restriction. Does a same-sex spouse qualify?',
   fixture_does='Records the spouse as ELIGIBLE-BY-MARRIAGE and flags the record OPEN. '
                'It does not decide, and it does not refuse.',
   routes_to='Membership Committee'),
 'samesex-parentage-on-tree': dict(
   bylaw='4.1.1 / tree',
   question='Where two parents of the same sex raise a child, the GEDCOM pedigree qualifiers '
            '(_FREL/_MREL) assume a father slot and a mother slot. Which slot carries which '
            'parent, and does the child inherit descent through either?',
   fixture_does='Stores both parents with an explicit relation type (birth / adoptive / step) '
                'and no father/mother slot; flags the record OPEN.',
   routes_to='Family Tree Committee + Membership Committee'),
 'partner-not-married-to': dict(
   bylaw='4.1.1',
   question='4.1.1 says "married to". A long-term unmarried partner is not married to. '
            'Is the Associate route (4.2.1, "special circumstances") the intended home?',
   fixture_does='Records the partner as NOT eligible under 4.1.1 and proposes 4.2.1 Associate; '
                'flags OPEN because 4.2.1 requires a Board vote on recommendation.',
   routes_to='Membership Committee → Board'),
 'eligibility-survives-divorce': dict(
   bylaw='4.1.1',
   question='A member admitted under "married to one having such origin" divorces that spouse. '
            'The by-laws are silent on whether the membership survives the marriage.',
   fixture_does='Leaves the membership standing and flags OPEN; never lapses it silently.',
   routes_to='Membership Committee'),
 'minor-two-households': dict(
   bylaw='4.3.1 (silent) / R4, R40',
   question='After a remarriage a minor belongs to two households with different clubs, '
            'different directory choices and different pickup authority. By-Law 4.3.1 says '
            'nothing about minors in two households.',
   fixture_does='Records TWO household memberships for the child, each with its own consent '
                'and pickup list, and flags OPEN. Directory shows the child in neither (R7).',
   routes_to='Membership Committee + Camp Ramallah'),
 'guardian-pickup-authority': dict(
   bylaw='R40 / R6',
   question='Camp pickup authority reads the household and delegation model. A court-appointed '
            'guardian is neither parent nor delegate.',
   fixture_does='Records the guardian as a household adult with an explicit legal basis field '
                'left blank, and flags OPEN.',
   routes_to='Camp Ramallah + Legal Advisor'),
}


# ─────────────────────────────────────────────────────────────────────────────
# THE DIRECTORY / NETWORK / CAMP EXTENSION
# Added after the research pass of 26 Aug 2026.  Sizes are chosen to reproduce
# the REAL shape of each surface, not a flattering one — see CAMP and JOBS.
# ─────────────────────────────────────────────────────────────────────────────

# Cities, per club.  Coarse coordinates only: the map must never resolve to a house.
CITIES = {
 'SF':  [('San Francisco','CA',37.77,-122.42), ('Daly City','CA',37.71,-122.46),
         ('San Mateo','CA',37.56,-122.32), ('Oakland','CA',37.80,-122.27),
         ('Burlingame','CA',37.58,-122.36), ('South San Francisco','CA',37.65,-122.41)],
 'DET': [('Detroit','MI',42.33,-83.05), ('Livonia','MI',42.37,-83.35),
         ('Southfield','MI',42.47,-83.22), ('Dearborn','MI',42.32,-83.18),
         ('Sterling Heights','MI',42.58,-83.03), ('Troy','MI',42.61,-83.15)],
 'JAX': [('Jacksonville','FL',30.33,-81.66), ('Orange Park','FL',30.17,-81.71),
         ('Ponte Vedra','FL',30.24,-81.39), ('Jacksonville Beach','FL',30.29,-81.39),
         ('Fleming Island','FL',30.09,-81.71)],
 'DC':  [('Washington','DC',38.90,-77.04), ('Arlington','VA',38.88,-77.10),
         ('Alexandria','VA',38.80,-77.05), ('Silver Spring','MD',38.99,-77.03),
         ('Bethesda','MD',38.98,-77.10), ('Falls Church','VA',38.88,-77.17)],
}

# A real O*NET-SOC subset.  Twenty-four occupations, sized so that a facet stays
# above the S7 floor of five per club: 1,049 members / 4 clubs / 24 = ~11 each.
# Sixty occupations would put the mean at 4.4 per club and reproduce the exact
# small-cell problem the coverage matrix just had to fix.
PROFESSIONS = [
 ('11-1021','General & Operations Manager','54'), ('13-2011','Accountant or Auditor','52'),
 ('15-1252','Software Developer','54'),           ('17-2051','Civil Engineer','54'),
 ('19-1042','Medical Scientist','54'),            ('21-1093','Social & Human Service Assistant','62'),
 ('23-1011','Lawyer','54'),                       ('25-2021','Elementary School Teacher','61'),
 ('25-1099','Postsecondary Teacher','61'),        ('27-3031','Public Relations Specialist','54'),
 ('29-1051','Pharmacist','62'),                   ('29-1141','Registered Nurse','62'),
 ('29-1216','Physician, Internal Medicine','62'), ('29-1021','Dentist','62'),
 ('31-9091','Dental Assistant','62'),             ('33-3051','Police Officer','92'),
 ('35-1011','Chef or Head Cook','72'),            ('41-3091','Sales Representative, Services','44'),
 ('41-9022','Real Estate Sales Agent','53'),      ('43-6014','Administrative Assistant','54'),
 ('47-1011','Construction Supervisor','23'),      ('49-3023','Automotive Service Technician','44'),
 ('51-1011','Production Supervisor','31'),        ('53-3032','Heavy Truck Driver','48'),
]
INDUSTRIES = {                       # NAICS sectors, only those the list above reaches
 '23':'Construction', '31':'Manufacturing', '44':'Retail trade', '48':'Transportation',
 '52':'Finance & insurance', '53':'Real estate', '54':'Professional & technical services',
 '61':'Educational services', '62':'Health care & social assistance',
 '72':'Accommodation & food services', '92':'Public administration',
}

LANGUAGES = ['Arabic', 'English', 'Spanish', 'French', 'Hebrew', 'Greek', 'Armenian',
             'Portuguese', 'German', 'Italian', 'Russian', 'Turkish']
INTERESTS = ['Camp Ramallah', 'The Scholarship', 'Medical Mission', 'Family Tree',
             'The Convention', 'Arabic language', 'Preservation', 'Youth & leadership',
             'Women to Women', 'Congressional outreach', 'The Magazine', 'Senior living']
HELP_KINDS = ['career advice', 'a résumé review', 'an introduction', 'mentoring a student',
              'hosting a visitor', 'reviewing an application', 'speaking at an event']

# ── The field registry — the backbone the three surfaces share ───────────────
# Three flags, independent, because coupling them is the defect Novi and Wild
# Apricot both ship: Novi only indexes a field it displays; Wild Apricot only
# searches configured columns.  `audience` is a ladder, not a boolean.
AUDIENCES = ['hidden', 'club', 'members', 'public']
FIELD_DEFS = [
 # key            label                 indexed filterable member-controlled  default audience
 ('name',        'Name',                True,  False, False, 'members'),
 ('club',        'Club',                True,  True,  False, 'members'),
 ('family',      'Family name',         True,  True,  False, 'members'),
 ('clan',        'Clan',                True,  True,  False, 'members'),
 ('alias',       'Also known as',       True,  False, True,  'members'),
 ('formerName',  'Former name',         True,  False, True,  'club'),
 ('city',        'City',                True,  True,  True,  'members'),
 ('email',       'Email',               False, False, True,  'hidden'),
 ('phone',       'Phone',               False, False, True,  'hidden'),
 ('postal',      'Street address',      False, False, True,  'hidden'),
 ('photo',       'Photograph',          False, False, True,  'club'),
 ('profession',  'Profession',          True,  True,  True,  'members'),
 ('industry',    'Industry',            True,  True,  True,  'members'),
 ('languages',   'Languages',           True,  True,  True,  'members'),
 ('interests',   'Interests',           True,  True,  True,  'members'),
 ('willingToHelp','Willing to help',    True,  True,  True,  'members'),
 ('openToWork',  'Open to work',        True,  True,  True,  'members'),
 ('mapPin',      'Show me on the map',  False, False, True,  'hidden'),
]
# Name and club are NOT member-controlled.  The old fixture let
# fieldVisibility.name be false while the directory screen said name is always
# shown to signed-in members — the data contradicted the product.
ALWAYS_SHOWN = {'name', 'club'}
# A contact field's ladder tops out at 'members'. Not a default — a ceiling.
NEVER_PUBLIC = {'email', 'phone', 'postal', 'photo', 'formerName'}

# ── Camp Ramallah ────────────────────────────────────────────────────────────
# ~50 seats, ages 13-17, applications January-March, selection criteria, and
# Federation-member counsellors.  Deliberately NOT scaled to the 500 households:
# generating 500 campers would test a fill-the-beds camp, which this is not, and
# would make the selection console — the actual product — pointless.
CAMP = dict(
    year=AS_OF, seats=50, ageLo=13, ageHi=17,
    applyOpens=f'{AS_OF}-01-08', applyCloses=f'{AS_OF}-03-15',
    session=(f'{AS_OF}-07-05', f'{AS_OF}-07-18'),
    applicants=76,          # oversubscribed, which is the whole point
    counsellors=9, cits=3, directors=2, nurse=1,
    cabins=['Al-Bireh', 'Jifna', 'Birzeit', 'Ein Misbah', 'Surda', 'Abu Qash'],
    # Ratios keyed on authority: the software resolves to the STRICTEST.
    ratios=[dict(authority='ACA',      band=(13,17), kind='overnight', awake=True,  ratio=10),
            dict(authority='ACA',      band=(13,17), kind='overnight', awake=False, ratio=10),
            dict(authority='Michigan', band=(13,17), kind='overnight', awake=True,  ratio=12),
            dict(authority='Michigan', band=(13,17), kind='overnight', awake=False, ratio=12)],
    # Two instruments, kept apart. Collapsing them loses the acquisition lever.
    aid=[dict(key='first-timer', label='First-timer grant', basis='need-blind',
              pot=1200000, award=(70000, 150000), firstTimersOnly=True,
              note='need-BLIND acquisition grant, modelled on One Happy Camper'),
         dict(key='access', label='Access aid', basis='means-tested', pot=900000,
              award=(30000, 120000), firstTimersOnly=False,
              note='means-tested; assessed by a THIRD PARTY. AFRP never holds a tax return.')],
)
# Screening states, copied from UltraCamp because the split that matters is the
# one between waiting on the candidate and waiting on the org to spend money.
SCREEN_STATES = ['not started', 'app pending', 'app ready', 'submitted', 'clear', 'review', 'expired']
CREDENTIALS = ['First Aid', 'CPR', 'Lifeguard', 'Safeguarding', 'Food handler']

# ── The job board ────────────────────────────────────────────────────────────
# A member-posted board serving 3,000 people is EMPTY — that is the documented
# top cause of community job-board death.  Ten live postings is the honest
# number.  Generating two hundred would make every screen look healthy and hide
# the failure mode the design has to survive.
JOBS = dict(live=10, expired=4, pendingReview=3, rejected=2, asks=14, offers=11)
# Required on every posting, universally — CA Labor Code 432.3, MN 181.173 and
# NY 194-b all reach the THIRD-PARTY PUBLISHER, which is what this board is.
# Thresholds differ per state and key off where the work is performed, so a
# conditional rule would be wrong somewhere. WA and MN also require benefits;
# CO requires a closing date. Open-ended ranges are prohibited.
JOB_REQUIRED = ['title', 'employer', 'location', 'salaryMinCents', 'salaryMaxCents',
                'benefits', 'closesOn', 'applyUrl']
