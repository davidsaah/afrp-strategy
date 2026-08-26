# -*- coding: utf-8 -*-
"""AFRP synthetic fixture generator — 500 households across four clubs.

Deterministic: fixed seed, fixed AS_OF year, no clock and no system randomness.
Everything is synthetic.  Family names come from the AFRP Clan Family Roster so
clan and 4.1.1 lookups are meaningful; given names are checked against the real
GEDCOM so no synthetic person carries a real person's name."""
import sys, os, json, io, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '/home/claude/tree')
import spec, names as NP
import roster

R = random.Random(spec.SEED)
Y = spec.AS_OF

CLAN_OF = {}
for clan, fams in roster.ROSTER.items():
    for f in fams:
        CLAN_OF.setdefault(f, []).append(clan)
ALL_FAMS = sorted(CLAN_OF)

# ── id helpers ───────────────────────────────────────────────────────────────
_ctr = collections.Counter()
def nid(p):
    _ctr[p] += 1
    return f'{p}-{_ctr[p]:04d}'

PEOPLE, HOUSEHOLDS, RELS, EVENTS, ENGAGE, PAYMENTS, FLAGS = [], [], [], [], [], [], []
BY_ID = {}

def make_person(family, sex, birth_year, *, outside=False, deceased_year=None):
    for _ in range(60):
        given = R.choice(NP.pool(sex, birth_year, outside))
        if not NP.collides(given, family):
            break
    else:
        given = R.choice(NP.pool(sex, birth_year, outside)) + R.choice(['ah','een','a','o'])
    p = dict(
        id=nid('P'), given=given, family=family,
        clan=(CLAN_OF.get(family) or [None])[0] if not outside else None,
        clanAmbiguous=len(CLAN_OF.get(family, [])) > 1,
        sex=sex, birthYear=birth_year, age=(Y - birth_year),
        deceasedYear=deceased_year, living=(deceased_year is None),
        synthetic=True,
    )
    PEOPLE.append(p); BY_ID[p['id']] = p
    return p

def outside_person(sex, birth_year):
    return make_person(R.choice(NP.OUTSIDE_SURNAMES), sex, birth_year, outside=True)

def rel(a, b, kind, **kw):
    # A marriage or partnership cannot begin before both people were 18.  The first
    # build drew `since` independently and produced 133 rows where a partner was
    # under 16 at the date, 51 of them before a partner was born.
    if kind in ('spouse', 'partner') and 'since' in kw:
        floor = max(a['birthYear'], b['birthYear']) + 18
        if kw['since'] < floor:
            kw['since'] = min(floor, Y)
            # A union cannot end before it began; push the end out rather than
            # pulling the start back below the age floor.
            if kw.get('endedYear') is not None and kw['endedYear'] < kw['since']:
                kw['endedYear'] = min(kw['since'] + 1, Y)
    RELS.append(dict(id=nid('R'), a=a['id'], b=b['id'], kind=kind, **kw))

def flag(subject_ids, key, note=''):
    q = spec.OPEN_QUESTIONS[key]
    FLAGS.append(dict(id=nid('Q'), key=key, subjects=list(subject_ids), bylaw=q['bylaw'],
                      question=q['question'], fixtureDoes=q['fixture_does'],
                      routesTo=q['routes_to'], note=note, decided=False))

def event(kind, subjects, year, **kw):
    e = dict(id=nid('E'), kind=kind, subjects=list(subjects), year=year, **kw)
    EVENTS.append(e); return e

# ── club allocation ──────────────────────────────────────────────────────────
def club_plan(n=500):
    plan = []
    for c in spec.CLUBS:
        plan += [c['code']] * round(n * c['share'])
    while len(plan) < n: plan.append('SF')
    while len(plan) > n: plan.pop()
    R.shuffle(plan)
    return plan

def pick_structure():
    r = R.random(); acc = 0
    for s in spec.STRUCTURES:
        acc += s['w']
        if r <= acc: return s
    return spec.STRUCTURES[-1]

def descent_family():
    return R.choice(ALL_FAMS)

# ── household builders ───────────────────────────────────────────────────────
def build_household(club, struct, idx):
    """Returns the household dict.  Adults and minors are created here; every
       adult is a separate consent (R4) and every minor is out of directories (R7)."""
    hh = dict(id=nid('H'), club=club, structure=struct['key'], structureLabel=struct['label'],
              adults=[], minors=[], openQuestions=[], joinedYear=R.randint(1968, Y))
    k = struct['key']
    fam = descent_family()

    def adult(sex, by, outside=False, family=None, deceased=None):
        p = (outside_person(sex, by) if outside
             else make_person(family or fam, sex, by, deceased_year=deceased))
        p['householdId'] = hh['id']; p['club'] = club
        hh['adults'].append(p['id']); return p

    def child_by(parents, lo, hi):
        """A birth year for a child of these parents that respects the 18-year floor.
           Several branches used to draw the child's age straight from a range and
           produced parents thirteen years older than their children."""
        floor = max((pp['birthYear'] for pp in parents), default=Y - 60) + 18
        lo_by, hi_by = Y - hi, Y - lo
        lo_by = max(lo_by, floor)
        return R.randint(lo_by, hi_by) if lo_by <= hi_by else hi_by

    def minor(sex, by, family=None):
        p = make_person(family or fam, sex, by)
        p['householdId'] = hh['id']; p['club'] = club
        hh['minors'].append(p['id']); return p

    def kids(parents, n, minor_ok=True, floor_from=None):
        # A parent is at least 18 years older than a child.  The first build drew
        # the child's birth year independently of the parents' and produced 45
        # parent-child rows with a gap under 13 years, and birth-mother ages from
        # 3 to 76.
        out = []
        youngest_parent = max((pp['birthYear'] for pp in (floor_from or parents)),
                              default=Y - 60)
        for _ in range(n):
            lo_by, hi_by = (Y - 24, Y - 1) if minor_ok else (Y - 45, Y - 19)
            lo_by = max(lo_by, youngest_parent + 18)
            if lo_by > hi_by: continue
            by = R.randint(lo_by, hi_by)
            s = R.choice('MF')
            p = (minor(s, by) if (Y - by) < 18 else adult(s, by))
            for par in parents:
                rel(par, p, 'parent-child', relation='birth')
            out.append(p)
        return out

    ab = lambda lo, hi: R.randint(Y - hi, Y - lo)   # birth year for an age in [lo,hi]

    if k == 'married-both-descent':
        a = adult('M', ab(26, 78)); b = adult('F', ab(24, 76), family=descent_family())
        rel(a, b, 'spouse', since=R.randint(1965, Y - 1), status='married')
        kids([a, b], R.randint(0, 3))

    elif k == 'married-one-descent':
        a = adult(R.choice('MF'), ab(26, 78))
        b = adult('F' if a['sex'] == 'M' else 'M', ab(24, 76), outside=True)
        b['eligibilityBasis'] = 'marriage'
        rel(a, b, 'spouse', since=R.randint(1970, Y - 1), status='married')
        kids([a, b], R.randint(0, 3))

    elif k == 'married-multigen':
        g = adult(R.choice('MF'), ab(68, 94))
        a = adult('M', max(ab(38, 58), g['birthYear'] + 18)); b = adult('F', ab(36, 56), outside=True)
        b['eligibilityBasis'] = 'marriage'
        rel(g, a, 'parent-child', relation='birth')  # grandparent -> parent
        rel(a, b, 'spouse', since=R.randint(1988, Y - 5), status='married')
        kids([a, b], R.randint(1, 3))

    elif k == 'single-never-married':
        adult(R.choice('MF'), ab(19, 88))

    elif k == 'widowed':
        a = adult(R.choice('MF'), ab(58, 96))
        dyear = R.randint(Y - 12, Y)
        d = adult('F' if a['sex'] == 'M' else 'M', ab(60, 98), deceased=dyear)
        rel(a, d, 'spouse', since=R.randint(1960, dyear - 1), status='widowed', endedYear=dyear)
        e = event('death', [d['id']], dyear, familyApproved=(dyear < Y),
                  published=(dyear < Y - 1), gate='family-approval-required')
        if dyear >= Y: e['note'] = 'held pending family approval — R34'

    elif k in ('divorced-custodial', 'single-parent-never-married'):
        a = adult(R.choice('MF'), ab(30, 62))
        if k == 'divorced-custodial':
            ex = adult('F' if a['sex'] == 'M' else 'M', ab(30, 64), outside=True)
            ex['householdId'] = None; hh['adults'].remove(ex['id']); ex['club'] = club
            dy = R.randint(Y - 15, Y - 1)
            rel(a, ex, 'spouse', since=dy - R.randint(3, 20), status='divorced', endedYear=dy)
            event('divorce', [a['id'], ex['id']], dy, publishable=False,
                  note='never auto-published; not a magazine item')
            ex['eligibilityBasis'] = 'marriage'
            ex['membershipNote'] = 'admitted by marriage, marriage ended'
            flag([ex['id']], 'eligibility-survives-divorce')
            hh['openQuestions'].append('eligibility-survives-divorce')
            for c in kids([a], R.randint(1, 3), floor_from=[a, ex]):
                rel(ex, c, 'parent-child', relation='birth')
        else:
            kids([a], R.randint(1, 2))

    elif k == 'divorced-remarried':
        a = adult(R.choice('MF'), ab(34, 58))
        ex = make_person(R.choice(NP.OUTSIDE_SURNAMES), 'F' if a['sex'] == 'M' else 'M',
                         ab(34, 60), outside=True)
        ex['club'] = R.choice([c['code'] for c in spec.CLUBS])   # other household, maybe other club
        dy = R.randint(Y - 12, Y - 2)
        rel(a, ex, 'spouse', since=dy - R.randint(4, 18), status='divorced', endedYear=dy)
        new = adult('F' if a['sex'] == 'M' else 'M', ab(32, 58), outside=True)
        new['eligibilityBasis'] = 'marriage'
        rel(a, new, 'spouse', since=R.randint(dy + 1, Y), status='married')
        event('marriage', [a['id'], new['id']], R.randint(dy + 1, Y),
              approvals=[a['id'], new['id']], gate='two-approvals-required')
        shared = []
        for _ in range(R.randint(1, 2)):
            c = minor(R.choice('MF'), child_by([a, ex], 4, 17))
            rel(a, c, 'parent-child', relation='birth')
            rel(ex, c, 'parent-child', relation='birth')
            c['secondHouseholdClub'] = ex['club']
            c['twoHouseholds'] = True
            shared.append(c['id'])
        for _ in range(R.randint(0, 1)):
            c = minor(R.choice('MF'), child_by([a, new], 1, 9))
            rel(a, c, 'parent-child', relation='birth')
            rel(new, c, 'parent-child', relation='step')
        if shared:
            flag(shared, 'minor-two-households',
                 note=f'household club {club}; other household club {ex["club"]}')
            hh['openQuestions'].append('minor-two-households')

    elif k == 'divorced-marriedin-ex':
        # the person of Ramallah descent is the one who LEFT
        a = adult(R.choice('MF'), ab(32, 66), outside=True)
        a['eligibilityBasis'] = 'marriage'
        ex = make_person(fam, 'F' if a['sex'] == 'M' else 'M', ab(32, 68))
        ex['club'] = R.choice([c['code'] for c in spec.CLUBS])
        dy = R.randint(Y - 14, Y - 1)
        rel(a, ex, 'spouse', since=dy - R.randint(3, 22), status='divorced', endedYear=dy)
        a['membershipNote'] = ('the only Ramallah descent in this household left it; '
                               'this member holds standing solely through a marriage that ended')
        flag([a['id']], 'eligibility-survives-divorce',
             note='the descendant spouse is the one who departed')
        hh['openQuestions'].append('eligibility-survives-divorce')
        for c in kids([a], R.randint(1, 2), floor_from=[a, ex]):
            rel(ex, c, 'parent-child', relation='birth')
            c['descentThrough'] = ex['id']

    elif k in ('samesex-one-descent', 'samesex-both-descent', 'samesex-with-children'):
        sx = R.choice('MF')
        a = adult(sx, ab(28, 64))
        if k == 'samesex-one-descent':
            b = adult(sx, ab(28, 64), outside=True); b['eligibilityBasis'] = 'marriage'
        else:
            b = adult(sx, ab(28, 64), family=descent_family()); b['eligibilityBasis'] = 'descent'
        my = R.randint(2004, Y)
        rel(a, b, 'spouse', since=my, status='married')
        event('marriage', [a['id'], b['id']], my, approvals=[a['id'], b['id']],
              gate='two-approvals-required')
        if k == 'samesex-one-descent':
            flag([b['id']], 'samesex-married-to')
            hh['openQuestions'].append('samesex-married-to')
        if k == 'samesex-with-children':
            for _ in range(R.randint(1, 2)):
                c = minor(R.choice('MF'), child_by([a, b], 1, 17))
                rel(a, c, 'parent-child', relation=R.choice(['birth', 'adoptive']))
                rel(b, c, 'parent-child', relation='adoptive')
                c['parentSlotsUndefined'] = True
            flag([p for p in hh['minors']], 'samesex-parentage-on-tree')
            hh['openQuestions'].append('samesex-parentage-on-tree')

    elif k == 'unmarried-partners':
        a = adult(R.choice('MF'), ab(24, 70))
        b = adult(R.choice('MF'), ab(24, 70), outside=True)
        b['eligibilityBasis'] = 'none'
        b['membershipNote'] = 'not married; 4.1.1 "married to" does not reach an unmarried partner'
        b['proposedClass'] = 'associate-4.2.1'
        rel(a, b, 'partner', since=R.randint(1990, Y - 1), status='unmarried')
        flag([b['id']], 'partner-not-married-to')
        hh['openQuestions'].append('partner-not-married-to')
        kids([a, b], R.randint(0, 2))

    elif k == 'adoptive':
        a = adult('M', ab(32, 60)); b = adult('F', ab(32, 60), outside=True)
        b['eligibilityBasis'] = 'marriage'
        rel(a, b, 'spouse', since=R.randint(1992, Y - 3), status='married')
        for _ in range(R.randint(1, 3)):
            c = minor(R.choice('MF'), child_by([a, b], 2, 17))
            rel(a, c, 'parent-child', relation='adoptive')
            rel(b, c, 'parent-child', relation='adoptive')
            c['descentBy'] = 'adoption'

    elif k == 'guardianship':
        g = adult(R.choice('MF'), ab(46, 78))
        for _ in range(R.randint(1, 2)):
            c = minor(R.choice('MF'), child_by([g], 5, 17))
            rel(g, c, 'guardian', legalBasis=None, relation='guardian')
        flag(list(hh['minors']), 'guardian-pickup-authority')
        hh['openQuestions'].append('guardian-pickup-authority')

    elif k == 'adult-child-at-home':
        a = adult(R.choice('MF'), ab(54, 82))
        c = adult(R.choice('MF'), max(ab(19, 34), a['birthYear'] + 18))
        rel(a, c, 'parent-child', relation='birth')

    elif k == 'senior-couple':
        a = adult('M', ab(68, 95)); b = adult('F', ab(66, 93), family=descent_family())
        rel(a, b, 'spouse', since=R.randint(1955, 1995), status='married')
        R.choice([a, b])['residence'] = 'assisted-living'

    # A household cannot have joined before anyone in it was an adult.  53
    # households claimed a join year earlier than the birth of every member.
    born = [BY_ID[i]['birthYear'] for i in hh['adults'] + hh['minors'] if i in BY_ID]
    if born:
        hh['joinedYear'] = max(hh['joinedYear'], min(born) + 18)
        hh['joinedYear'] = min(hh['joinedYear'], Y)
    HOUSEHOLDS.append(hh)
    return hh

# ── memberships, consent, standing ───────────────────────────────────────────
CHANNELS = ['email', 'post', 'push', 'phone', 'sms']
FIELDS   = ['name', 'city', 'email', 'phone', 'postal', 'photo']

def finish_person(p):
    ad = p['age'] >= 18
    p.setdefault('eligibilityBasis', 'descent' if p['clan'] else 'none')
    # R28 living-date gate + R32: the living are restricted
    p['datesVisibleWithoutSignIn'] = (not p['living'])
    # R27 consent is per channel; R28 visibility per field; R7 minors never in directories
    p['consent'] = {c: (R.random() < .72 if ad else False) for c in CHANNELS}
    p['marketingConsent'] = ad and R.random() < .55          # R30, separate from operational
    p['fieldVisibility'] = {f: (R.random() < .6 if ad else False) for f in FIELDS}
    p['directoryInclude'] = ad and R.random() < .78          # R7: never for minors
    if not ad:
        p['membership'] = None
        return
    # DEATH ENDS EVERYTHING.  The first build let the deceased keep a current
    # membership, a place on the certified roll, a directory listing and a
    # marketing consent — 23 dead people were counted into the electorate that
    # By-Law 9.1.3 turns into delegate weight.  Death is not a status flag on a
    # live record; it terminates the record.
    if not p['living']:
        p['membership'] = None
        p['directoryInclude'] = False
        p['marketingConsent'] = False
        p['consent'] = {c: False for c in CHANNELS}
        return
    basis = p['eligibilityBasis']
    if p.get('proposedClass') == 'associate-4.2.1':
        cls, standing = 'associate-4.2.1', 'board-vote-pending'
    elif basis in ('descent', 'marriage'):
        cls, standing = 'regular-4.1.1', 'current'
    else:
        cls, standing = 'associate-4.2.1', 'current'
    if p['age'] <= 24 and R.random() < .30:
        cls = 'student-free'                                  # R9
    if R.random() < .11: standing = 'lapsed'
    elif R.random() < .06: standing = 'grace'
    # A CLUB standing is only ever current / grace / lapsed.  'board-vote-pending' is a
    # NATIONAL 4.2.1 state — the Board votes on national Associate admission, not on a
    # club's own roster — so it must not leak into a club row.
    def club_standing():
        return R.choices(['current', 'grace', 'lapsed'], weights=[.84, .05, .11])[0]
    cs = club_standing() if standing == 'board-vote-pending' else standing
    p['membership'] = dict(
        nationalClass=cls, standing=standing,
        # By-Law 4.2.1: "Associate Members are ineligible to vote on any A.F.R.P.
        # matter" — so an Associate never carries a voting-dues date.  A free
        # student membership (R9) pays no dues, so it cannot evidence payment of
        # them either.  Only a dues-paying Regular member can be certified.
        votingDuesPaidBy=('2026-04-30'
                          if standing == 'current' and cls == 'regular-4.1.1'
                          and R.random() < .85 else None),
        clubs=[dict(club=p['club'], standing=cs, duesPaid=cs == 'current')],
        clubOfRecord=p['club'],                               # R16 pointer, never a merge
    )
    # R2 multi-club: some members hold a second club membership with independent standing
    if R.random() < .09:
        other = R.choice([c['code'] for c in spec.CLUBS if c['code'] != p['club']])
        st2 = club_standing()
        p['membership']['clubs'].append(dict(club=other, standing=st2, duesPaid=st2 == 'current'))
    profile(p)


# ── the directory / network profile ──────────────────────────────────────────
def profile(p):
    """Everything the directory, the professional network and the print section
       read.  One field registry, three surfaces."""
    city, st, lat, lon = R.choice(spec.CITIES[p['club']])
    p['city'], p['state'] = city, st
    # Coarse coordinates ONLY, jittered to ~1km and rounded to 2dp. A directory
    # map pin must never resolve to a house; 360Alumni caps zoom for the same
    # reason, and for this community it is a safety control, not a nicety.
    p['geo'] = dict(lat=round(lat + R.uniform(-.05, .05), 2),
                    lon=round(lon + R.uniform(-.05, .05), 2), precision='city')

    # Transliteration: an Arabic name reaches an English directory by several
    # spellings. An explicit alias is what makes the search find them.
    if R.random() < .28:
        p['alias'] = R.choice([p['family'] + 'e', p['family'] + 'h', p['family'][:-1],
                               p['family'].replace('ou', 'u'), p['family'].replace('i', 'ee')])
    # A married woman's former name — Harvard carries it and it is how an older
    # cohort is actually found.
    if p['sex'] == 'F' and p['age'] > 30 and R.random() < .34:
        p['formerName'] = R.choice(roster.ROSTER[R.choice(list(roster.ROSTER))])

    if R.random() < .78:
        code, title, sector = R.choice(spec.PROFESSIONS)
        p['profession'] = dict(soc=code, title=title)
        p['industry'] = dict(naics=sector, label=spec.INDUSTRIES[sector])
        if p['age'] >= 62 and R.random() < .55:
            p['profession']['retired'] = True

    langs = ['English'] + (['Arabic'] if R.random() < .62 else [])
    for _ in range(R.choices([0, 1, 2], weights=[.6, .3, .1])[0]):
        l = R.choice(spec.LANGUAGES)
        if l not in langs: langs.append(l)
    p['languages'] = langs
    p['interests'] = R.sample(spec.INTERESTS, R.choices([0,1,2,3], weights=[.28,.34,.24,.14])[0])

    # Both flags decay, so both carry an expiry. LinkedIn's open-to-work has no
    # API field at all, so ours is authoritative rather than a mirror of theirs.
    if p['age'] < 70 and R.random() < .11:
        p['openToWork'] = dict(since=f'{Y}-{R.randint(1,8):02d}-{R.randint(1,28):02d}',
                               expires=f'{Y+1}-{R.randint(1,6):02d}-01',
                               kinds=R.sample(['full time','part time','contract','board seat'],
                                              R.randint(1, 2)))
    if R.random() < .41:                      # Harvard/Stanford expose this as a top facet
        p['willingToHelp'] = dict(kinds=R.sample(spec.HELP_KINDS, R.randint(1, 3)),
                                  expires=f'{Y+1}-{R.randint(1,12):02d}-01')

    # Visibility is an AUDIENCE, not a boolean — and name and club are not the
    # member's to hide. The old model let fieldVisibility.name be false while the
    # screen promised name is always shown.
    vis = {}
    for key, _lab, _idx, _flt, member_controlled, default in spec.FIELD_DEFS:
        if key in spec.ALWAYS_SHOWN or not member_controlled:
            vis[key] = default
        elif key in spec.NEVER_PUBLIC:
            # A contact field's ladder tops out at 'members'. Not a default the
            # member can raise — a ceiling. A logged-out directory has almost no
            # legal protection against wholesale copying (Feist, hiQ), so the
            # control has to be that the data never reaches the logged-out page.
            vis[key] = R.choices(['hidden', 'club', 'members'], weights=[.34, .20, .46])[0]
        else:
            vis[key] = R.choices(spec.AUDIENCES, weights=[.28, .18, .52, .02])[0]
    p['visibility'] = vis
    p['fieldVisibility'] = {k: (v != 'hidden') for k, v in vis.items()}   # legacy view
    # Consent to DISPLAY is not consent to CONTACT is not consent to EXPORT.
    # No membership product on the market separates these three.
    p['directoryConsent'] = dict(
        display=p['directoryInclude'],
        contact=p['directoryInclude'] and R.random() < .81,
        export=False,                     # nobody consents to export. Nobody is asked.
        acceptedTermsVersion='directory-2026.1',
        dated=f'{Y - R.randint(0,2)}-{R.randint(1,12):02d}-{R.randint(1,28):02d}')

# ── life moments ─────────────────────────────────────────────────────────────
# Weighted, because a uniform draw produced 124 ordinations in a population of 1,537
# — the kind of nonsense that makes a demo dataset unusable for judging a real screen.
# 'marriage' is NOT in this list.  R34: a marriage names two people and therefore
# needs two approvals.  Drawing it as a single-subject personal moment produced 189
# one-sided marriages, 54 of them for children — one aged one year old.  Marriages
# are emitted by the household builders, which know both parties.
LIFE_W = [('new-job',.22), ('relocation',.16), ('graduation',.12),
          ('first-home',.11), ('birth',.10), ('bereavement',.08), ('illness',.07),
          ('retirement',.06), ('award',.05), ('citizenship',.02), ('ordination',.01)]
LIFE = [k for k, _ in LIFE_W]
_LW  = [w for _, w in LIFE_W]

def life_moments():
    ADULT_ONLY = {'new-job', 'first-home', 'citizenship', 'ordination', 'retirement'}
    for p in PEOPLE:
        if not p['living']: continue
        n = R.choices([0, 1, 2, 3], weights=[.34, .38, .20, .08])[0]
        for _ in range(n):
            k = R.choices(LIFE, weights=_LW)[0]
            if k in ADULT_ONLY and p['age'] < 18: continue
            if k == 'retirement' and p['age'] < 60: continue
            if k == 'graduation' and not (16 <= p['age'] <= 30): continue
            if k == 'birth' and not (20 <= p['age'] <= 46): continue
            yr = R.randint(Y - 4, Y)
            e = event(k, [p['id']], yr, claim=True, approved=R.random() < .74)  # R33 claim ≠ announcement
            e['published'] = e['approved'] and R.random() < .7                   # R35 separate gate
            if k == 'relocation':
                e['proposedClubTransfer'] = R.choice(
                    [c['code'] for c in spec.CLUBS if c['code'] != p['club']])
                e['automatic'] = False                                           # R34
            if k == 'marriage':
                e['gate'] = 'two-approvals-required'

# ── engagement ladder, with guaranteed coverage ──────────────────────────────
def eligible(p, prog, rung=3):
    """A program's age band gates PARTICIPATION (rungs 1-3), never LEADERSHIP.
       Camp Ramallah's band is 8-16 because that is who goes to camp; the person
       who chairs its committee is an adult.  Applying the band to the whole ladder
       was a modelling error the coverage check caught: it left rung 5 unreachable
       for every age-capped program."""
    if not p['living']: return False
    if prog.get('women_only') and p['sex'] != 'F': return False
    if rung >= 4:
        # Correcting the band to allow adult leadership went too far and dropped
        # every OTHER gate: 108 leadership rows were held by lapsed members, minors
        # and people the UI itself flags "no 4.1.1 basis".  Giving or serving needs
        # an adult in good standing; carrying a seat needs a member entitled to hold
        # one.  The age floor was never the only rule.
        if p['age'] < (25 if rung == 5 else 18): return False
        m = p.get('membership')
        if not m or m['standing'] == 'lapsed': return False
        if rung == 5 and m['nationalClass'] == 'associate-4.2.1': return False
        return True
    lo, hi = prog['band']
    if p['age'] < lo: return False
    if hi is not None and p['age'] > hi: return False
    return True

def add_engagement(p, prog, rung, why='organic'):
    ENGAGE.append(dict(id=nid('G'), person=p['id'], club=p['club'], program=prog['key'],
                       rung=rung, rungName=spec.RUNGS[rung],
                       evidence=R.choice(spec.EVIDENCE[rung]), year=R.randint(Y - 5, Y),
                       source=why))

def engage_organic():
    for p in PEOPLE:
        if not p['living'] or p['age'] < 3: continue
        for prog in spec.PROGRAMS:
            if R.random() > .17: continue
            rung = R.choices([1, 2, 3, 4, 5], weights=[.34, .27, .21, .13, .05])[0]
            if not eligible(p, prog, rung): continue
            add_engagement(p, prog, rung)

def engage_fill(floor=5):
    """Guarantee coverage — and be honest about what guaranteeing it costs.

    The first build asserted "380 of 380 cells filled" after a pass whose whole job
    was to fill any empty cell.  That assertion is a tautology: it cannot fail.  It
    also left 63 cells resting on a single person, which tests nothing and, on a
    screen, publishes a count of one — under the platform's own S7 small-cell floor.

    So: record what ORGANIC generation achieved (that number can fail), then top each
    cell up toward a floor of five where the eligible pool allows, and record every
    cell where it does not."""
    have = collections.Counter((g['program'], g['club'], g['rung']) for g in ENGAGE)
    organic_filled = sum(1 for prog in spec.PROGRAMS for c in spec.CLUBS
                         for r in (1, 2, 3, 4, 5) if have[(prog['key'], c['code'], r)])
    added, short = 0, []
    for prog in spec.PROGRAMS:
        for c in spec.CLUBS:
            for rung in (1, 2, 3, 4, 5):
                key = (prog['key'], c['code'], rung)
                pool = [p for p in PEOPLE
                        if p.get('club') == c['code'] and eligible(p, prog, rung)]
                already = {g['person'] for g in ENGAGE
                           if g['program'] == prog['key'] and g['club'] == c['code']
                           and g['rung'] == rung}
                pool = [p for p in pool if p['id'] not in already]
                want = floor - have[key]
                if want <= 0: continue
                take = min(want, len(pool))
                for p in R.sample(pool, take):
                    add_engagement(p, prog, rung, why='coverage-fill')
                    have[key] += 1; added += 1
                if have[key] < floor:
                    short.append(dict(program=prog['key'], club=c['code'], rung=rung,
                                      n=have[key], eligiblePool=len(pool) + len(already)))
    return dict(organicFilled=organic_filled, total=len(spec.PROGRAMS) * len(spec.CLUBS) * 5,
                added=added, floor=floor, belowFloor=short)

# ── money ────────────────────────────────────────────────────────────────────
# R23: money routes by the event's HOST.  Class codes are attribution only.
TREATMENTS = {
 'dues-national':  dict(treatment='federation-revenue', host='AFRP',
    note='national dues — AFRP revenue'),
 'dues-club-via-national': dict(treatment='agency-liability', host='club',
    note='club dues collected nationally: a LIABILITY until remitted (R21, CPA signature pending)'),
 'dues-club-direct': dict(treatment='club-money', host='club',
    note="the club's own dues, collected by the club"),
 'hafli': dict(treatment='club-money', host='club',
    note='club social — club money by collection channel'),
 'club-gift-to-afrp-project': dict(treatment='conduit-11.1.5', host='AFRP',
    note='club funds for an AFRP project — pass-through under By-Law 11.1.5 (Dr/Cr 2500)'),
 'convention-registration': dict(treatment='agency-at-first-dollar', host='AFRP',
    note='convention money is AFRP agency from the first dollar'),
 'banquet-seat': dict(treatment='inventory', host='AFRP',
    note='a banquet seat is inventory, not a donation (R26)'),
 'restricted-gift': dict(treatment='restricted', host=None,
    note='restriction rides the gift through the ledger (R25); designation on the gift, never matched later'),
 'unrestricted-gift': dict(treatment='federation-revenue', host='AFRP', note='unrestricted'),
}
HOST_OF = {p['key']: p['host'] for p in spec.PROGRAMS}

_DIM = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def pay(person, kind, cents, *, program=None, restriction=None):
    if not person['living']:            # 77 payments were charged to the dead
        return
    t = dict(TREATMENTS[kind])
    host = t['host']
    if kind == 'restricted-gift':
        host = HOST_OF.get(program, 'AFRP')
    club_money = (host == 'club')
    if club_money:
        host = person['club']
    fee = max(30, round(cents * 0.029) + 30)          # R20: posts gross, fee is its own line

    # A full date, because R22 keys the daily-close batch on date+fund+kind and R10
    # sets an Apr 30 voting-dues deadline.  A year alone can construct neither.
    yr = R.randint(Y - 3, Y)
    mo = R.randint(1, 12) if yr < Y else R.randint(1, 8)
    dy = R.randint(1, _DIM[mo - 1])
    date = f'{yr:04d}-{mo:02d}-{dy:02d}'

    # Custody is not ownership.  Club dues collected nationally are the CLUB's money
    # (host) sitting on AFRP's books as a liability until remitted (custodian).  With
    # only a host field the agency liability never landed in anyone's ledger.
    custodian = 'AFRP' if t['treatment'] in ('agency-liability', 'conduit-11.1.5',
                                             'agency-at-first-dollar') else host

    # And somebody bears the card fee on money that is not theirs.  Under gross posting
    # AFRP books the fee as its own expense; on agency money that is a subsidy unless it
    # is deducted from the remittance.  Named either way rather than left implicit.
    fee_borne_by = 'AFRP' if custodian == 'AFRP' else host
    fee_note = ('deducted from the remittance to ' + host
                if t['treatment'] == 'agency-liability' else None)

    # A restriction rides the gift (R25).  The 11.1.5 conduit is club money passing
    # through AFRP FOR A NAMED PROJECT — the purpose restricts the destination, so it
    # must survive the crossing.  Twelve conduit gifts used to book as unrestricted.
    if restriction is None and program and t['treatment'] == 'conduit-11.1.5':
        restriction = program

    PAYMENTS.append(dict(
        id=nid('$'), person=person['id'], kind=kind, date=date, year=yr,
        grossCents=cents, processingFeeCents=fee, netCents=cents - fee,
        hostEntity=host, custodianEntity=custodian,
        feeBorneBy=fee_borne_by, feeNote=fee_note,
        treatment=t['treatment'], note=t['note'],
        program=program, restriction=restriction,
        fundClass=(restriction or 'unrestricted'),      # drives restricted reporting
        clubClass=person['club'],                       # ATTRIBUTION ONLY — never routes money
        # R22: the daily-close batch is idempotent on date + fund + kind
        batchKey=f'{date}|{restriction or "unrestricted"}|{kind}',
        journalLines=['clearing', 'fee', 'revenue'],
    ))

def money():
    for p in PEOPLE:
        m = p.get('membership')
        if not m: continue
        if m['standing'] in ('current', 'grace') and m['nationalClass'] != 'student-free':
            pay(p, 'dues-national', R.choice([3500, 5000, 7500]))
            pay(p, R.choice(['dues-club-via-national', 'dues-club-direct']),
                R.choice([2000, 2500, 4000]))
        if R.random() < .22:
            pay(p, 'hafli', R.choice([5000, 7500, 12000]))
        if R.random() < .18:
            prog = R.choice(spec.PROGRAMS)
            pay(p, 'restricted-gift', R.choice([2500, 10000, 25000, 100000]),
                program=prog['key'], restriction=prog['key'])
        if R.random() < .12:
            pay(p, 'unrestricted-gift', R.choice([5000, 20000, 50000]))
        if R.random() < .16:
            pay(p, 'convention-registration', R.choice([15000, 22500]))
            if R.random() < .6:
                pay(p, 'banquet-seat', 9500)
    # a handful of club→AFRP project transfers, the 11.1.5 conduit
    for c in spec.CLUBS:
        donors = [p for p in PEOPLE if p['club'] == c['code'] and p.get('membership')]
        for p in R.sample(donors, min(3, len(donors))):
            pay(p, 'club-gift-to-afrp-project', R.choice([50000, 150000]), program='camp')

# ── Camp Ramallah ────────────────────────────────────────────────────────────
CAMP = {}

def build_camp():
    """A selection problem, not an enrolment funnel: 76 applicants for 50 seats.

    What this generates is a decision RECORD — who applied, who was selected, on
    what stated basis, and who is on a waitlist that promotes one family at a
    time. The market default notifies every waitlisted family at once, which is a
    race rather than a queue."""
    C = spec.CAMP
    pool = [p for p in PEOPLE if p['living'] and C['ageLo'] <= p['age'] <= C['ageHi']]
    R.shuffle(pool)
    applicants = pool[:C['applicants']]
    CAMP['season'] = dict(year=C['year'], seats=C['seats'], session=C['session'],
                          applyOpens=C['applyOpens'], applyCloses=C['applyCloses'],
                          ageBand=[C['ageLo'], C['ageHi']])

    # Selection criteria, stated. A cohort assembled without a recorded basis is
    # indefensible in a community where every applicant is somebody's cousin.
    apps = []
    for i, p in enumerate(applicants):
        returner = R.random() < .38
        apps.append(dict(
            id=nid('CA'), person=p['id'], club=p['club'], age=p['age'], sex=p['sex'],
            family=p['family'], clan=p['clan'], returner=returner,
            firstTimer=not returner,
            submitted=f"{C['year']}-{R.choice(['01','02','03'])}-{R.randint(1,28):02d}",
            aidRequested=R.random() < .44,
            siblingApplying=R.random() < .18,
            householdId=p.get('householdId'),
        ))
    # Select for cohort SHAPE, not first-come: every club represented, a real mix
    # of first-timers and returners, no single family dominating.
    per_club = {c['code']: 0 for c in spec.CLUBS}
    per_family = collections.Counter()
    selected, wait = [], []
    quota = {c['code']: max(4, round(C['seats'] * c['share'])) for c in spec.CLUBS}
    for a in sorted(apps, key=lambda x: (x['submitted'], x['id'])):
        room_club = per_club[a['club']] < quota[a['club']]
        room_family = per_family[a['family']] < 4
        if len(selected) < C['seats'] and room_club and room_family:
            reasons = []
            if a['firstTimer']: reasons.append('first-timer')
            if a['returner']: reasons.append('returning camper')
            reasons.append(f"club quota {per_club[a['club']] + 1}/{quota[a['club']]}")
            if a['siblingApplying']: reasons.append('sibling applying')
            a['decision'] = 'selected'; a['reasons'] = reasons
            per_club[a['club']] += 1; per_family[a['family']] += 1
            selected.append(a)
        else:
            why = ('club quota full' if not room_club else
                   'four from this family already selected' if not room_family else
                   'seats full')
            a['decision'] = 'waitlisted'; a['reasons'] = [why]
            wait.append(a)
    # A sequential waitlist: ONE offer at a time, with a claim window that expires.
    for rank, a in enumerate(wait, 1):
        a['waitlistRank'] = rank
        a['offer'] = (dict(madeOn=f"{C['year']}-04-02", claimWindowHours=72,
                           state=R.choice(['claimed', 'expired', 'declined']))
                      if rank <= 3 else None)
    # Club quotas rounded from share sum to 49, not 50 — so one seat is
    # unallocated by the rule rather than given to whoever applied first. A
    # selection console must SHOW that remainder; silently handing it out is how
    # a fair rule becomes an unaccountable one.
    CAMP['season']['quota'] = quota
    CAMP['season']['quotaTotal'] = sum(quota.values())
    CAMP['season']['unallocatedByQuota'] = C['seats'] - sum(quota.values())
    CAMP['season']['seatsFilled'] = len(selected)
    CAMP['season']['remainderNote'] = (
        'Club quotas are rounded from each club\'s share and sum to %d of %d seats. '
        'The remaining %d is held, not awarded, until the committee decides where it '
        'goes and records why.' % (sum(quota.values()), C['seats'],
                                   C['seats'] - sum(quota.values())))
    CAMP['applications'] = apps

    # Cabins, and the ratio resolved to the strictest authority that applies.
    strictest = min(r['ratio'] for r in C['ratios'])
    cabins = []
    for i, name in enumerate(C['cabins']):
        members = [a['person'] for a in selected[i::len(C['cabins'])]]
        cabins.append(dict(name=name, campers=members,
                           counsellorsRequired=-(-len(members) // strictest)))
    CAMP['cabins'] = cabins
    CAMP['ratio'] = dict(applied=strictest, authorities=C['ratios'],
                         resolvedFrom=[r['authority'] for r in C['ratios']
                                       if r['ratio'] == strictest],
                         note='ACA and Michigan disagree; the roster resolves to the stricter.')

    # Staff. Screening is ANNUAL, and a lapsed date blocks a roster rather than
    # warning about it.
    staff = []
    adults = [p for p in PEOPLE if p['living'] and 21 <= p['age'] <= 68 and p.get('membership')]
    for role, n in [('director', C['directors']), ('nurse', C['nurse']),
                    ('counsellor', C['counsellors'])]:
        for p in R.sample(adults, n):
            st = R.choices(spec.SCREEN_STATES, weights=[.02,.06,.08,.06,.68,.05,.05])[0]
            checked = f"{C['year'] - (1 if st == 'expired' else 0)}-{R.randint(1,5):02d}-{R.randint(1,28):02d}"
            creds = [dict(kind=k, expires=f"{C['year'] + R.choice([-1,0,1,1,2])}-{R.randint(1,12):02d}-01")
                     for k in R.sample(spec.CREDENTIALS, R.randint(1, 3))]
            staff.append(dict(id=nid('CS'), person=p['id'], role=role, club=p['club'],
                              paid=(role != 'counsellor') or R.random() < .5,
                              screening=dict(state=st, lastCheckedOn=checked,
                                             cadence='annual', vendorAgnostic=True),
                              credentials=creds,
                              fcraDisclosure=dict(standalone=True, signedOn=checked),
                              rosterEligible=(st == 'clear')))
    # CITs. Three legal beings, not one badge — and the paid rung is an employee.
    teens = [p for p in PEOPLE if p['living'] and 16 <= p['age'] <= 17]
    for p in R.sample(teens, min(C['cits'], len(teens))):
        paid = R.random() < .34
        staff.append(dict(
            id=nid('CS'), person=p['id'], role='CIT', club=p['club'], paid=paid,
            # ACA's screening standard starts at 18, so an under-18 CIT is
            # structurally unscreenable. The control is supervision, encoded.
            screening=dict(state='not started', lastCheckedOn=None, cadence='annual',
                           unscreenableUnder18=True),
            supervision=dict(countsTowardRatio=False, aloneWithMinors=False,
                             supervisedBy='counsellor'),
            credentials=[],
            # A paid CIT is an employee. Employment confidentiality then restricts
            # disclosure to outside parties INCLUDING a parent.
            legalStatus='employee' if paid else 'volunteer',
            parentVisibility=not paid,
            rosterEligible=True))
    CAMP['staff'] = staff

    # Camperships: two instruments, kept apart, with capped pots and rationing.
    awards, pots = [], {a['key']: a['pot'] for a in C['aid']}
    askers = [a for a in selected if a['aidRequested']]
    for a in askers:
        inst = next((x for x in C['aid'] if not x['firstTimersOnly'] or a['firstTimer']), None)
        if a['firstTimer'] and R.random() < .6:
            inst = C['aid'][0]
        elif not a['firstTimer']:
            inst = C['aid'][1]
        want = R.randint(*inst['award'])
        got = min(want, pots[inst['key']])
        pots[inst['key']] -= got
        awards.append(dict(id=nid('CW'), application=a['id'], instrument=inst['key'],
                           basis=inst['basis'], requestedCents=want, awardedCents=got,
                           partial=got < want, state='awarded' if got else 'aid waitlist',
                           financialDocumentsHeld=False,
                           assessedBy='third party' if inst['basis'] == 'means-tested' else None))
    CAMP['aid'] = dict(instruments=C['aid'], awards=awards,
                       remaining={k: v for k, v in pots.items()},
                       note='AFRP holds the application, the award and the ledger. '
                            'A third party holds the financial documents.')
    # The health seam. AFRP owns "cleared to arrive"; it does not own the record.
    CAMP['health'] = dict(
        boundary='AFRP owns enrolment, clearance, ratios, incidents and parent notice. '
                 'The health record itself — medications, doses, allergies, immunisation, '
                 'the nurse\'s log — is held by a specialist vendor.',
        clearedToArrive=sum(1 for _ in selected if R.random() < .84),
        ofSelected=len(selected),
        recordsHeldHere=0)
    return CAMP


def build_facets(floor=5):
    """A mean above the small-cell floor does not keep the MINIMUM above it.

    24 occupations across 1,049 members averages ~11 per club — and still leaves
    a dozen profession x club cells holding one or two people, each of which
    names an individual. So the profession facet is published federation-wide,
    where every cell clears the floor, and the club cross-tab suppresses thin
    cells rather than printing them. Same rule as the coverage matrix."""
    prof = [p for p in PEOPLE if p.get('profession') and p.get('visibility', {}).get('profession')
            not in (None, 'hidden')]
    fed = collections.Counter(p['profession']['soc'] for p in prof)
    cross = collections.Counter((p['profession']['soc'], p['club']) for p in prof)
    published, suppressed = [], []
    for soc, title, sector in spec.PROFESSIONS:
        row = dict(soc=soc, title=title, industry=sector, total=fed[soc], byClub={})
        for c in spec.CLUBS:
            n = cross[(soc, c['code'])]
            if 0 < n < floor:
                row['byClub'][c['code']] = None          # suppressed, not zero
                suppressed.append(dict(soc=soc, club=c['code'], n=n))
            else:
                row['byClub'][c['code']] = n
        published.append(row)
    return dict(floor=floor, professions=published, suppressedCells=len(suppressed),
                note=('A profession x club cell holding fewer than %d people names an '
                      'individual, so it is suppressed rather than printed. The '
                      'federation-wide count is always shown.' % floor))


FACETS = {}

# ── the job board ────────────────────────────────────────────────────────────
JOBS = []
ASKS = []

TITLES = [('Staff Accountant','52','Detroit, MI'), ('Registered Nurse','62','Jacksonville, FL'),
          ('Software Engineer','54','San Francisco, CA'), ('Program Coordinator','54','Washington, DC'),
          ('Dental Hygienist','62','Southfield, MI'), ('Warehouse Supervisor','48','Oakland, CA'),
          ('Paralegal','54','Arlington, VA'), ('Line Cook','72','San Mateo, CA'),
          ('Grant Writer','54','Silver Spring, MD'), ('Field Service Technician','44','Livonia, MI'),
          ('Case Manager','62','Alexandria, VA'), ('Retail Store Manager','44','Ponte Vedra, FL'),
          ('Civil Engineer','54','Troy, MI'), ('Marketing Associate','54','Daly City, CA'),
          ('Pharmacy Technician','62','Bethesda, MD'), ('Truck Driver, Regional','48','Dearborn, MI'),
          ('Executive Assistant','54','Falls Church, VA'), ('Substitute Teacher','61','Burlingame, CA'),
          ('Construction Foreman','23','Orange Park, FL')]

def build_jobs():
    """Ten live postings, not two hundred.

    A member-posted board serving three thousand people is empty — that is the
    documented top cause of community job-board death. Generating a healthy-looking
    board would hide the exact failure mode the design has to survive, which is why
    the asks-and-offers surface carries more rows than the postings do."""
    J = spec.JOBS
    posters = [p for p in PEOPLE if p['living'] and p.get('membership') and p['age'] >= 25]
    pool = list(TITLES); R.shuffle(pool)
    def one(state, i):
        title, sector, loc = pool[i % len(pool)]
        lo = R.choice([48000, 55000, 62000, 71000, 84000, 96000, 112000])
        hi = lo + R.choice([9000, 14000, 21000, 30000])
        posted = f'{Y}-{R.randint(1,8):02d}-{R.randint(1,28):02d}'
        closes = f'{Y}-{R.randint(9,12):02d}-{R.randint(1,28):02d}'
        j = dict(id=nid('J'), title=title, employer=f'{title.split()[0]} employer {i+1}',
                 location=loc, industry=sector, postedBy=R.choice(posters)['id'],
                 postedOn=posted, closesOn=closes, state=state,
                 # Required universally. CA/MN/NY reach the third-party publisher,
                 # which is what this board is. A min without a max is rejected.
                 salaryMinCents=lo * 100, salaryMaxCents=hi * 100, salaryPeriod='year',
                 benefits='Health, dental, 401(k) with match, 15 days PTO',
                 applyUrl='https://example.org/apply/' + str(i + 1),
                 applyNeedsLogin=False,          # or Google will not index it
                 schemaOrg='JobPosting',
                 publicPage=True, applicantsMembersOnly=True,
                 shareLinkedInUrl='https://www.linkedin.com/sharing/share-offsite/?url=…',
                 reviewedBy='staff' if state in ('live', 'expired') else None,
                 eeoStatement=None)             # optional: EO 11246 revoked Jan 2025
        if state == 'expired':
            j['closesOn'] = f'{Y}-0{R.randint(1,6)}-{R.randint(1,28):02d}'
            j['httpOnExpiry'] = 410             # or Google issues a manual action
        return j
    i = 0
    for state, n in [('live', J['live']), ('expired', J['expired']),
                     ('pending review', J['pendingReview']), ('rejected', J['rejected'])]:
        for _ in range(n):
            JOBS.append(one(state, i)); i += 1
    # One rejected posting exists precisely to exercise the refusal path.
    JOBS[-1].update(salaryMaxCents=None, rejectedReason=(
        'No maximum on the salary range. An open-ended range is prohibited in '
        'Washington and Minnesota, and this board is the third-party publisher.'))
    JOBS[-2].update(rejectedReason=(
        'Salary given as "competitive, see our careers page". California requires '
        'the pay scale in the posting body — no links, no QR codes.'),
        salaryMinCents=None, salaryMaxCents=None)

    # Asks and offers: the surface that actually generates volume.
    kinds = [('ask', 'Looking for'), ('offer', 'Happy to')]
    for k, n in [('ask', J['asks']), ('offer', J['offers'])]:
        for _ in range(n):
            p = R.choice(posters)
            ASKS.append(dict(id=nid('AO'), kind=k, person=p['id'], club=p['club'],
                             text=(R.choice(['an introduction at a hospital system',
                                             'advice on switching into public health',
                                             'a résumé review before an interview',
                                             'a summer internship for my daughter',
                                             'someone who has done an SBA loan'])
                                   if k == 'ask' else
                                   R.choice(['review a résumé', 'make an introduction',
                                             'mentor a student this term',
                                             'talk to anyone thinking about dentistry',
                                             'host a visitor in my city'])),
                             postedOn=f'{Y}-{R.randint(1,8):02d}-{R.randint(1,28):02d}',
                             responses=R.randint(0, 5)))
    return JOBS, ASKS


# ── assemble ─────────────────────────────────────────────────────────────────
def build():
    plan = club_plan(500)
    # Reserve one household per (structure x club) so coverage is guaranteed rather
    # than hoped for: rare structures cannot go missing from a small club by luck.
    reserved = [(c, s) for s in spec.STRUCTURES for c in [x['code'] for x in spec.CLUBS]]
    slots = collections.defaultdict(list)
    for club, s in reserved: slots[club].append(s)
    for i, club in enumerate(plan):
        struct = slots[club].pop() if slots[club] else pick_structure()
        build_household(club, struct, i)
    for p in PEOPLE:
        p.setdefault('club', None)
        finish_person(p)
    # The reserved (structure x club) slots are placed first, which would make the first
    # screen of any browser unrepresentative.  Shuffle deterministically so the order on
    # screen looks like the population, not like the fill algorithm.
    R.shuffle(HOUSEHOLDS)
    life_moments()
    engage_organic()
    cov = engage_fill()
    money()
    build_camp()
    build_jobs()
    FACETS.update(build_facets())
    return cov
