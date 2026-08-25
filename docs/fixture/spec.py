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
