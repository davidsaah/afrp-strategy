# -*- coding: utf-8 -*-
"""Wire the 500-household fixture into the prototype.

Three things, in the order that matters:
  1. ONE data layer (window.FIX) + selectors, so every demo number has one source.
  2. Rewire the hardcoded counts that used to drift, to read from that layer.
  3. Add the fixture console at fed/fixture — the coverage proof, in the product.

Idempotent: guarded in both directions."""
import io, json, re, sys

PROTO = '/home/claude/afrp-mockups/docs/prototype.html'
s = io.open(PROTO, encoding='utf-8').read()
if 'window.FIX=' in s or 'window.FIX =' in s:
    print('already wired — nothing to do'); sys.exit(0)

payload = io.open('/home/claude/fixture/payload.json', encoding='utf-8').read()
D = json.loads(payload)

# ── 1 · the data layer ───────────────────────────────────────────────────────
DATA = '<script>window.FIX=' + payload + ';</script>\n'

FIXJS = r'''<script>
/* ── FIXQ · the only place a demo number comes from ──────────────────────────
   Before the fixture, counts were typed into each screen by hand and drifted
   apart: 3,184 member records on one screen, 148 club members on another, 971
   certified on a third, none of them derivable from each other.  Everything a
   screen wants to COUNT now comes through here. */
(function(){
  var F = window.FIX; if (!F) return;
  var mem = null;
  function members(){
    if (mem) return mem;
    mem = [];
    F.households.forEach(function(h){
      h.people.forEach(function(p){ if (p.a >= 18 && p.d) mem.push({p:p, club:h.club, hh:h}); });
    });
    return mem;
  }
  var Q = {
    clubCodes: F.clubs.map(function(c){ return c.code; }),
    clubName: function(c){ var x = F.clubs.filter(function(k){return k.code===c;})[0];
                           return x ? x.name : c; },
    households: function(c){ return c ? F.households.filter(function(h){return h.club===c;})
                                      : F.households; },
    /* Standings come from the fixture's own derived roll-up so the screen and the
       file can never disagree; if it is absent the screen says so rather than
       inventing a number. */
    roll: F.derived || null,
    n: function(x){ return (x==null) ? '—' : Number(x).toLocaleString('en-US'); },
    coverageCells: function(){
      var filled = 0, total = 0;
      F.programs.forEach(function(p){ Q.clubCodes.forEach(function(c){
        F.matrix[p.key][c].forEach(function(n){ total++; if (n) filled++; }); }); });
      return {filled:filled, total:total};
    },
    openCount: function(){ return F.flags.length; },
    memberRows: function(club, limit){
      return members().filter(function(m){ return m.club === club; }).slice(0, limit || 8);
    }
  };
  window.FIXQ = Q;

  /* ── 2 · rewire the counts.  Each target is an id planted in the markup. ── */
  function put(id, val){ var e = document.getElementById(id); if (e) e.textContent = val; }
  function html(id, val){ var e = document.getElementById(id); if (e) e.innerHTML = val; }
  window.FIXWIRE = function(){
    var R = Q.roll; if (!R) return;
    put('fx-members', Q.n(R.members));
    /* NOT wired: the "Certified 2026" card is a FROZEN electorate with a record date
       of 25 May 2026.  R12 freezes an electorate and R43 says a snapshot is read and
       never recomputed, so painting a live fixture count over it would have put two
       different numbers under one label and one record date.  The live figure is
       shown separately, and labelled as live. */
    put('fx-certified-live', Q.n(R.certified));
    put('fx-households', Q.n(F.households.length));
    put('fx-people', Q.n(F.stats.people));
    html('fx-nat-d', '<b>' + Q.n(R.nat.current) + ' current</b> &middot; <i>' +
         Q.n(R.nat.grace) + ' in grace</i> &middot; <em>' + Q.n(R.nat.lapsed) +
         ' lapsed</em> &middot; ' + Q.n(R.nat['board-vote-pending']) +
         ' awaiting a Board vote on 4.2.1');
    put('fx-members2', Q.n(R.members));
    put('fx-optin', Q.n(R.directoryOptIn));
    var det = R.clubs.DET;
    if (det) {
      put('fx-DET-rows2', Q.n(det.rows));
      put('fx-DET-rows3', Q.n(det.rows));
      html('fx-DET-breeze', Q.n(det.rows + 3) + ' Breeze records &rarr; ' + Q.n(det.rows) +
           ' members after identity resolution; 3 were duplicates');
    }
    Q.clubCodes.forEach(function(c){
      var k = R.clubs[c]; if (!k) return;
      put('fx-' + c + '-rows', Q.n(k.rows));
      put('fx-' + c + '-record', Q.n(k.record));
      put('fx-' + c + '-hh', Q.n(k.households));
      put('fx-' + c + '-also', Q.n(k.alsoNational));
      html('fx-' + c + '-d', '<b>' + Q.n(k.current) + ' current</b> &middot; <i>' +
           Q.n(k.grace) + ' in grace</i> &middot; <em>' + Q.n(k.lapsed) + ' lapsed</em>');
    });
  };
})();
</script>
'''

# ── 3 · the fixture console ──────────────────────────────────────────────────
CONSOLE = r'''<section class="screen" data-route="fed/fixture" data-lens="fed">
  <div class="page-head">
    <div><h1>The fixture</h1>
      <p>Five hundred synthetic households behind the counts on this prototype. This is where
         you check what it actually covers, and where it is thin.</p></div>
    <div class="page-head__end"><span class="c-pill c-pill--danger mono">every person invented</span></div>
  </div>

  <div class="panel" style="margin-bottom:var(--s4)">
    <div class="statbox">
      <div class="stat"><span class="stat__k">Households</span><span class="stat__v" id="fx-households">—</span><span class="stat__d">across four of the eighteen clubs</span></div>
      <div class="stat"><span class="stat__k">People</span><span class="stat__v" id="fx-people">—</span><span class="stat__d">the living membership layer; ancestors come from the GEDCOM</span></div>
      <div class="stat"><span class="stat__k">Coverage, before any fill</span><span class="stat__v" id="fx-organic">—</span><span class="stat__d" id="fx-organic-d">19 programs &times; 4 clubs &times; 5 rungs</span></div>
      <div class="stat"><span class="stat__k">Certified today, live</span><span class="stat__v" id="fx-certified-live">—</span><span class="stat__d">not the frozen roll &mdash; the federation dashboard's <b>Certified 2026 &middot; 971</b> is a snapshot frozen 25 May 2026 and is never recomputed (R12, R43)</span></div>
      <div class="stat"><span class="stat__k">By-law questions open</span><span class="stat__v" id="fx-open">—</span><span class="stat__d" id="fx-open-d">flagged, never decided</span></div>
    </div>
  </div>

  <div class="px-tabs" data-tabs="fed/fixture">
    <button class="px-tab is-on" data-t="0" onclick="FIXUI.tab(0)">Coverage</button>
    <button class="px-tab" data-t="1" onclick="FIXUI.tab(1)">Open questions</button>
    <button class="px-tab" data-t="2" onclick="FIXUI.tab(2)">Households</button>
    <button class="px-tab" data-t="3" onclick="FIXUI.tab(3)">What is invented</button>
  </div>

  <div class="px-tp" data-t="0">
    <div class="panel">
      <div class="panel__head"><div><h3>Nineteen programs, four clubs, five rungs</h3>
        <p>The number in each tick is how many people sit at that rung.</p></div></div>
      <div class="c-table-wrap"><table class="c-table c-table--dense" id="fx-mx"></table></div>
      <div class="why" id="fx-mxkey" style="display:flex;gap:var(--s3);flex-wrap:wrap;align-items:center"></div>
      <p class="why" id="fx-honest"></p>
      <p class="why"><b>A program's age band gates participation, not leadership.</b> Camp
         Ramallah's band is 8&ndash;16 because that is who goes to camp; the person who chairs its
         committee is forty-five. The first build applied the band to the whole ladder and left
         rung 5 unreachable in every age-capped program. Any screen that filters a program's
         people by its band will hide that program's own committee.</p>
    </div>
  </div>

  <div class="px-tp" data-t="1" hidden>
    <div class="panel"><div class="panel__head"><div><h3>Six questions the fixture refuses to answer</h3>
      <p>Each untraditional household lands where the by-laws are silent or untested. The record
         is marked open and routed &mdash; the same posture the tree takes toward 4.1.1.</p></div></div>
      <div id="fx-qs"></div></div>
  </div>

  <div class="px-tp" data-t="2" hidden>
    <div class="panel">
      <div class="toolbar">
        <select class="c-input" id="fx-club" onchange="FIXUI.render()" aria-label="Filter by club"></select>
        <select class="c-input" id="fx-struct" onchange="FIXUI.render()" aria-label="Filter by structure"></select>
        <select class="c-input" id="fx-q" onchange="FIXUI.render()" aria-label="Filter by by-law question"></select>
        <div class="toolbar__end"><span class="toolbar__count mono" id="fx-count">&mdash;</span></div>
      </div>
      <div class="c-table-wrap" style="border:0;border-radius:0">
        <table class="c-table c-table--dense" id="fx-hh"></table></div>
    </div>
  </div>

  <div class="px-tp" data-t="3" hidden>
    <div class="panel"><div class="panel__head"><div><h3>What is invented and what is not</h3></div></div>
      <div class="why">
        <p><b>Every person, household, event and dollar here is invented.</b> Two things anchor
           the fixture to reality so lookups behave the way they will in production:</p>
        <p><b>Family names</b> are the 164 on the AFRP Clan Family Roster, under Shaheen's eight
           clans in their two groups, so clan resolution and By-Law 4.1.1 checks are meaningful.</p>
        <p><b>Given names</b> were checked against the 21,677 real
           <span class="mono">(given, surname)</span> pairs in the Ramallah GEDCOM and resampled
           on collision, so <b>no synthetic person carries a real person's name</b>.</p>
        <p>The fixture is deterministic: fixed seed, fixed as-of year, no clock. The same command
           reproduces the same 500 families, and 99 assertions run on every build &mdash; the file
           is not written if one fails.</p>
        <p><b>Four clubs of the eighteen carry fixture data</b> &mdash; San Francisco, Detroit,
           Jacksonville and Greater Washington. The other fourteen have none. Any club figure
           outside those four on this prototype is a hand-built worked example, not fixture data.</p>
        <p><b>The fixture is not wired into every screen</b>, and an earlier draft of this page
           said it was. It drives the counts listed on the federation dashboard, the Detroit club
           dashboard and roster, the directory and the communications desk. Every other screen
           still carries its own hand-built demo figures, which is why some of them will not
           reconcile with these.</p>
        <p><b>Minors and the deceased are not listed here.</b> R7 keeps a minor out of every
           directory, so the household browser shows a count and no names. A death is a life event
           with a family-approval gate (R34), so the deceased are withheld too.</p>
        <p><b>Nothing here derives from the scholarship applicant files.</b></p>
      </div></div>
  </div>
</section>
'''

UIJS = r'''<script>
(function(){
  var F = window.FIX, Q = window.FIXQ; if (!F || !Q) return;
  function esc(x){ return String(x).replace(/[&<>"]/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
  var law = function(b){ return /^\d/.test(b) ? 'By-Law ' + b
    : /^R\d/.test(b) ? 'Platform rule ' + b : b; };

  function mx(){
    var t = document.getElementById('fx-mx'); if (!t) return;
    var h = '<thead><tr><th>Program</th>' + Q.clubCodes.map(function(c){
      return '<th class="num">' + esc(Q.clubName(c)) + '</th>'; }).join('') + '</tr></thead><tbody>';
    F.programs.forEach(function(p){
      var band = p.band[1] === null ? p.band[0] + '+' : p.band[0] + '–' + p.band[1];
      h += '<tr><td><b>' + esc(p.name) + '</b>' + (p.flagship ? ' <span class="mono" style="color:var(--c-accent)">&#9670;</span>' : '') +
           '<div class="why">host ' + esc(p.host) + ' &middot; ages ' + esc(band) + '</div></td>';
    Q.clubCodes.forEach(function(c){
        h += '<td class="num"><span class="fx-rungs">' + F.matrix[p.key][c].map(function(n,i){
          return '<span class="fx-rg fx-rg--' + (n ? (i+1) : 0) + '" title="' + esc(p.name) +
                 ' &middot; ' + esc(Q.clubName(c)) + ' &middot; rung ' + (i+1) + ' ' +
                 esc(F.rungs[i+1]) + ' &middot; ' + n + '">' + (n || '0') + '</span>';
        }).join('') + '</span></td>';
      });
      h += '</tr>';
    });
    t.innerHTML = h + '</tbody>';
    var k = document.getElementById('fx-mxkey');
    if (k) k.innerHTML = [1,2,3,4,5].map(function(r){
      return '<span><span class="fx-rg fx-rg--' + r + '" style="cursor:default">&nbsp;</span> rung ' +
             r + ' &middot; ' + esc(F.rungs[r]) + '</span>'; }).join('') +
      '<span><span class="fx-rg fx-rg--0">0</span> empty &mdash; none in this fixture</span>';
  }

  function qs(){
    var el = document.getElementById('fx-qs'); if (!el) return;
    var count = {}, people = {};
    F.flags.forEach(function(f){ count[f.key] = (count[f.key]||0)+1;
                                 people[f.key] = (people[f.key]||0)+f.who.length; });
    el.innerHTML = Object.keys(F.questions).map(function(k){
      var q = F.questions[k];
      var ex = F.flags.filter(function(f){ return f.key===k && f.who.length; })[0];
      var who = ex ? ex.who.slice(0,2).map(function(w){
        return w.name + ' (' + w.age + ', ' + Q.clubName(w.club) + ')'; }).join(', ') : '';
      return '<div class="qrow"><div class="qrow__main">' +
        '<b>' + esc(q.question) + '</b>' +
        '<span class="mono">' + esc(law(q.bylaw)) + ' &middot; ' + (count[k]||0) +
        ' records &middot; ' + (people[k]||0) + ' people</span>' +
        '<div class="why" style="margin-top:var(--s2)"><b>What the fixture does:</b> ' +
        esc(q.fixture_does) + (who ? '<br><span class="mono">e.g. ' + esc(who) + '</span>' : '') +
        '<br>routes to <b>' + esc(q.routes_to) + '</b></div></div>' +
        '<div class="qrow__end"><span class="c-pill c-pill--danger">open</span></div></div>';
    }).join('');
  }

  function fills(){
    var c = document.getElementById('fx-club'), st = document.getElementById('fx-struct'),
        q = document.getElementById('fx-q');
    if (!c || c.options.length) return;
    c.innerHTML = '<option value="">All four clubs</option>' + F.clubs.map(function(k){
      return '<option value="' + k.code + '">' + esc(k.name) + '</option>'; }).join('');
    st.innerHTML = '<option value="">All 17 structures</option>' + F.structures.map(function(k){
      return '<option value="' + esc(k.key) + '">' + esc(k.label) + '</option>'; }).join('');
    q.innerHTML = '<option value="">Any by-law question</option>' + Object.keys(F.questions).map(function(k){
      return '<option value="' + esc(k) + '">' + esc(k) + '</option>'; }).join('');
  }

  function chip(p){
    if (!p.d) return '<span class="c-pill c-pill--muted">deceased</span>';
    if (p.a < 18) return '<span class="c-pill c-pill--muted">minor</span>';
    if (p.e === 'descent')  return '<span class="c-pill c-pill--ok">4.1.1 descent</span>';
    if (p.e === 'marriage') return '<span class="c-pill c-pill--ok">4.1.1 marriage</span>';
    return '<span class="c-pill c-pill--danger">no 4.1.1 basis</span>';
  }

  function rows(){
    var t = document.getElementById('fx-hh'); if (!t) return;
    var c  = (document.getElementById('fx-club')||{}).value || '';
    var st = (document.getElementById('fx-struct')||{}).value || '';
    var q  = (document.getElementById('fx-q')||{}).value || '';
    var list = F.households.filter(function(h){
      return (!c || h.club===c) && (!st || h.structure===st) && (!q || h.q.indexOf(q)>=0); });
    var cn = document.getElementById('fx-count');
    if (cn) cn.textContent = list.length + ' of ' + F.households.length +
      ' households · showing ' + Math.min(list.length, 40);
    t.innerHTML = '<thead><tr><th>Household</th><th>Club</th><th>People</th><th>Raises</th></tr></thead><tbody>' +
      list.slice(0,40).map(function(h){
        return '<tr' + (h.q.length ? ' class="is-flag"' : '') + '><td><b>' + esc(h.label) +
          '</b><div class="why mono">' + esc(h.id) + ' &middot; joined ' + h.joined + '</div></td>' +
          '<td>' + esc(Q.clubName(h.club)) + '</td><td>' +
          (h.minors ? '<div class="why">' + h.minors + ' minor' + (h.minors>1?'s':'') +
            ' in this household &mdash; not listed (R7)</div>' : '') +
          (h.deceased ? '<div class="why">' + h.deceased + ' deceased &mdash; withheld pending family approval (R34)</div>' : '') +
          h.people.map(function(p){
            return '<div style="display:flex;gap:var(--s2);align-items:center">' +
              '<span>' + esc(p.n) + '</span><span class="mono why">' + p.a + '</span>' + chip(p) + '</div>';
          }).join('') + '</td><td>' + (h.q.length ?
            h.q.map(function(x){ return '<span class="c-pill c-pill--danger mono">' + esc(x) + '</span>'; }).join(' ')
            : '<span class="why">&mdash;</span>') + '</td></tr>';
      }).join('') + '</tbody>';
  }

  window.FIXUI = {
    tab: function(i){
      var sec = document.querySelector('[data-route="fed/fixture"]'); if (!sec) return;
      sec.querySelectorAll('.px-tab').forEach(function(b,j){ b.classList.toggle('is-on', j===i); });
      sec.querySelectorAll('.px-tp').forEach(function(p,j){ p.hidden = (j!==i); });
    },
    render: rows
  };

  function boot(){
    var S = F.stats;
    var e1 = document.getElementById('fx-organic');
    if (e1) e1.textContent = S.organic + ' / ' + S.cells;
    var e1d = document.getElementById('fx-organic-d');
    if (e1d) e1d.innerHTML = '19 programs &times; 4 clubs &times; 5 rungs &middot; <b>' +
      S.added + ' more records added</b> to bring every cell to a floor of ' + S.floor;
    var e2 = document.getElementById('fx-open');
    if (e2) e2.textContent = S.questions;
    var e2d = document.getElementById('fx-open-d');
    if (e2d) e2d.innerHTML = 'six distinct questions across <b>' + S.flags +
      ' flagged records</b> &mdash; flagged, never decided';
    var h = document.getElementById('fx-honest');
    if (h) h.innerHTML = '<b>What this grid does and does not prove.</b> Organic generation ' +
      'reached <b>' + S.organic + ' of ' + S.cells + '</b> cells on its own. A fill pass then ' +
      'added <b>' + S.added + '</b> records to bring every cell to at least ' + S.floor +
      ' people. Saying &ldquo;' + S.cells + ' of ' + S.cells + ' filled&rdquo; after a pass whose ' +
      'job is to fill empty cells proves nothing &mdash; that assertion cannot fail. The number ' +
      'that can fail is the organic one, and it is the one on the card above. ' +
      (S.belowFloor ? '<b>' + S.belowFloor + ' cells</b> are still under the floor because the ' +
        'eligible pool is too small; they are listed rather than padded.'
       : 'No cell is under the floor, so no cell on this grid publishes a count small enough to ' +
         'identify one person (S7).');
    mx(); qs(); fills(); rows();
    if (window.FIXWIRE) window.FIXWIRE();
  }
  var prev = window.renderAll;
  window.renderAll = function(){ if (prev) prev.apply(this, arguments); try { boot(); } catch(e){} };
  if (document.readyState !== 'loading') boot();
  else document.addEventListener('DOMContentLoaded', boot);
})();
</script>
'''

CSS = '''<style>
.fx-rungs{display:inline-flex;gap:2px}
.fx-rg{width:22px;height:26px;border-radius:3px;display:inline-grid;place-items:center;
  font:500 10.5px/1 var(--f-mono,monospace);font-variant-numeric:tabular-nums;border:1px solid transparent}
.fx-rg--1{background:color-mix(in srgb,var(--c-accent) 12%,transparent);color:var(--c-ink-2)}
.fx-rg--2{background:color-mix(in srgb,var(--c-accent) 26%,transparent);color:var(--c-ink-2)}
.fx-rg--3{background:color-mix(in srgb,var(--c-accent) 46%,transparent);color:var(--c-ink)}
.fx-rg--4{background:color-mix(in srgb,var(--c-accent) 68%,transparent);color:var(--c-bg)}
.fx-rg--5{background:var(--c-accent);color:var(--c-bg)}
.fx-rg--0{background:color-mix(in srgb,var(--c-danger,#9B3A3A) 14%,transparent);
  color:var(--c-danger,#9B3A3A);border-color:currentColor;font-weight:700}
</style>
'''

# ── splice ───────────────────────────────────────────────────────────────────
def must(old, new, label):
    global s
    if old not in s:
        raise SystemExit('ANCHOR MISSING: ' + label)
    s = s.replace(old, new, 1)

# CSS into head
must('</head>', CSS + '</head>', 'head')

# console section before the sitemap screen
m = re.search(r'<section class="screen"[^>]*data-route="sitemap"', s)
if not m: raise SystemExit('ANCHOR MISSING: sitemap section')
s = s[:m.start()] + CONSOLE + s[m.start():]

# nav link in the fed lens
must('<nav data-lens-nav="fed"',
     '<nav data-lens-nav="fed"', 'fed nav probe')
mnav = re.search(r'(<nav data-lens-nav="fed"[^>]*>)', s)
navlink = ('<a class="l-nav-item" href="#/fed/fixture">The fixture '
           '<span class="l-nav-item__badge l-nav-item__badge--violet">data</span></a>')
# place it right after the first nav group inside the fed nav
after = s.find('</div>', mnav.end())
s = s[:after+6] + navlink + s[after+6:]

# rewire the counts
must('<span class="stat__k">Member records</span><span class="stat__v">3,184</span>',
     '<span class="stat__k">Member records</span><span class="stat__v" id="fx-members">3,184</span>',
     'fed member records')
must('<span class="stat__k">Certified 2026</span><span class="stat__v">971</span>',
     '<span class="stat__k">Certified 2026</span><span class="stat__v">971</span>',
     'fed certified — deliberately left frozen')
must('<span class="stat__k">Club members</span><span class="stat__v">148</span>'
     '<span class="stat__d"><b>121 current</b> &middot; <i>9 in grace</i> &middot; <em>18 lapsed</em></span>',
     '<span class="stat__k">Club members</span><span class="stat__v" id="fx-DET-rows">148</span>'
     '<span class="stat__d" id="fx-DET-d"><b>121 current</b> &middot; <i>9 in grace</i> &middot; <em>18 lapsed</em></span>',
     'detroit club members')
must('<span class="stat__k">Also national members</span><span class="stat__v">116</span>',
     '<span class="stat__k">Also national members</span><span class="stat__v" id="fx-DET-also">116</span>',
     'detroit also national')
# Every other Detroit number on the club lens, so the lens cannot disagree with itself.
must('<span class="toolbar__count">148 members &middot; showing 6 &middot; sorted by household</span>',
     '<span class="toolbar__count"><span id="fx-DET-rows2">148</span> members &middot; '
     'showing 6 &middot; sorted by household</span>',
     'detroit roster toolbar')
must('151 Breeze records &rarr; 148 members after identity resolution; 3 were duplicates',
     '<span id="fx-DET-breeze">151 Breeze records &rarr; 148 members after identity resolution; '
     '3 were duplicates</span>',
     'detroit breeze line')
must('of the 148 &middot; the two scopes lapse independently',
     'of the <span id="fx-DET-rows3">148</span> &middot; the two scopes lapse independently',
     'detroit also-national caption')

# The federation member count appears on the directory and the comms desk too.
must('Of 3,184 members, 1,842 opted into the directory at all.',
     'Of <span id="fx-members2">3,184</span> members, <span id="fx-optin">1,842</span> opted '
     'into the directory at all.',
     'directory opt-in line')

# data + logic at the end of body
must('</body>', DATA + FIXJS + UIJS + '</body>', 'body close')

io.open(PROTO, 'w', encoding='utf-8').write(s)
print('wired · bytes now', len(s))
