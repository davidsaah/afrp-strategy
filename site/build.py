#!/usr/bin/env python3
"""Build the AFRP strategy site (D47).

Sources: site/pages/*.md (prose), site/data/*.yaml (structured), and the design
record itself (design/AFRP-Decisions-Register.md, design/AFRP-Strategic-Plan-
Crosswalk.md, design/AFRP-Delivery-Status.md, plan/MASTER-PLAN.md) plus the
journey data embedded in docs/AFRP-Analyst-Dashboard.html, which AFRP-Hub
generates. Output: docs/ (GitHub Pages). Counts are never typed by hand.

    python site/build.py          # build into docs/
    python site/build.py --check  # build, then fail if docs/ differs from git
"""
import datetime, html, json, os, re, shutil, subprocess, sys
from collections import Counter, OrderedDict
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOCS = ROOT / "docs"
REPO = "https://github.com/davidsaah/afrp-strategy"
BLOB = REPO + "/blob/main/"

SECTIONS = [
    dict(key="home", label="Home", href="index.html"),
    dict(key="strategy", label="AFRP Strategy", href="strategy/index.html"),
    dict(key="history", label="Evolution", href="history/index.html"),
    dict(key="programmes", label="Branches & programmes", href="programmes/index.html"),
    dict(key="experiences", label="People", href="experiences/index.html"),
    dict(key="workflows", label="Workflows", href="workflows/index.html"),
    dict(key="prototype", label="Prototype", href="prototype/index.html"),
    dict(key="status", label="Status", href="status/index.html"),
    dict(key="library", label="Library", href="library/index.html"),
]

env = Environment(loader=FileSystemLoader(str(SITE / "templates")),
                  autoescape=select_autoescape(enabled_extensions=()))
MD = lambda text: markdown.markdown(text, extensions=["tables", "fenced_code", "attr_list", "md_in_html", "sane_lists"])
E = lambda x: html.escape(str(x))
WRITTEN = []


# --------------------------------------------------------------------------- data
def load(name):
    return yaml.safe_load((SITE / "data" / name).read_text(encoding="utf-8"))


def md_page(name):
    """A prose page: YAML front matter between --- lines, then Markdown."""
    text = (SITE / "pages" / name).read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---"):
        _, fm, body = text.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    return meta, body


def parse_crosswalk():
    text = (ROOT / "design/AFRP-Strategic-Plan-Crosswalk.md").read_text(encoding="utf-8")
    rows, section = [], None
    for line in text.splitlines():
        m = re.match(r"^## ([A-I])\. (.+)$", line)
        if m:
            section = (m.group(1), m.group(2))
        m = re.match(r"^\| ([A-I]\d+) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \|$", line)
        if m and section:
            rows.append(dict(id=m.group(1), element=m.group(2), source=m.group(3),
                             status=m.group(4), how=m.group(5), section=section[1], letter=section[0]))
    notes = re.findall(r"^\| (P\d) \| (.+?) \| (.+?) \| (.+?) \|$", text, re.M)
    return rows, [dict(id=a, note=b, covers=c, ready=d) for a, b, c, d in notes]


def parse_decisions():
    text = (ROOT / "design/AFRP-Decisions-Register.md").read_text(encoding="utf-8")
    out = OrderedDict()
    for line in text.splitlines():
        m = re.match(r"^\| (\d{1,2}) \| (.+?) \| (.+?) \|", line)
        if m and int(m.group(1)) not in out and not m.group(2).startswith("**By-Law") and "Amendment" not in m.group(2):
            n = int(m.group(1))
            if n > 60:
                continue
            out[n] = dict(n=n, title=m.group(2).strip("* "), answer=m.group(3))
    for m in re.finditer(r"^## Decision (\d+) — (.+)$", text, re.M):
        n = int(m.group(1))
        q = re.search(r"^> (.+(?:\n> .+)*)", text[m.end():], re.M)
        ans = re.sub(r"\s*\n>\s*", " ", q.group(1)) if q else ""
        out.setdefault(n, dict(n=n, title=m.group(2)[0].upper() + m.group(2)[1:], answer=ans))
    # the amendment-package table also numbers 1-4; keep the decision rows only
    return OrderedDict(sorted(out.items()))


def delivery_facts():
    text = (ROOT / "design/AFRP-Delivery-Status.md").read_text(encoding="utf-8")
    tests = re.findall(r"([\d,]{3,}) tests green", text)
    done = set(re.findall(r"^#{2,3} Slice ([0-9A-Za-z]+) ", text, re.M))
    return dict(tests=tests[-1] if tests else None, done=done)


def plan_slices(done_extra):
    text = (ROOT / "plan/MASTER-PLAN.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| (\S+) \| \*\*(.+?)\*\* \| (.+?) \|", text, re.M)
    return [dict(n=a, name=b, stream=re.sub(r"\*", "", c)) for a, b, c in rows]


def board_data():
    h = (DOCS / "AFRP-Analyst-Dashboard.html").read_text(encoding="utf-8")
    m = re.search(r'<script id="data" type="application/json">(.*?)</script>', h, re.S)
    return json.loads(m.group(1))


# --------------------------------------------------------------------------- helpers
STATUS_CLASS = [("not built", "st-notbuilt"), ("partly", "st-partly"), ("built", "st-built"),
                ("plan only", "st-plan"), ("designed", "st-designed"), ("queued", "st-queued"),
                ("proposed", "st-proposed"), ("gap", "st-gap"), ("outside", "st-outside"),
                ("retired", "st-retired"), ("done", "st-built")]


def status_tag(s):
    parts = [p.strip() for p in re.sub(r"\*", "", s).split("·")]
    out = []
    for p in parts:
        cls = next((c for k, c in STATUS_CLASS if k in p.lower()), "")
        out.append(f'<span class="tag {cls}">{E(p)}</span>')
    return " ".join(out)


def status_key(s):
    s = re.sub(r"\*", "", s).split("·")[0].strip().lower()
    return s


def inline(text):
    """Markdown for one line (bold, code, links) without a wrapping <p>."""
    return re.sub(r"^<p>(.*)</p>$", r"\1", MD(str(text)).strip(), flags=re.S)


def src_link(s):
    path = s.split(" ")[0]
    if (ROOT / path).exists():
        target = BLOB + path if not path.startswith("docs/") else None
        if path.startswith("docs/"):
            return f'<a href="{{root}}{E(path[5:])}">{E(s)}</a>'
        return f'<a href="{target}">{E(s)}</a>'
    return E(s)


def table(headers, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw {cls}"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def ulist(items, fn=lambda x: inline(x)):
    if not items:
        return '<p class="muted">Not stated in the record.</p>'
    return "<ul>" + "".join(f"<li>{fn(i)}</li>" for i in items) + "</ul>"


def jid(j):
    return "<b>" + E(j["id"]) + "</b> " + E(j["title"])


def journey_bar(j):
    t = j.get("total") or 0
    if not t:
        return '<span class="muted small">No journeys catalogued.</span>'
    seg = "".join(f'<span class="{c}" style="width:{100*j.get(k,0)/t:.2f}%"></span>'
                  for k, c in [("meets", "m"), ("guarded", "g"), ("open", "o"), ("not_built", "n"), ("fails", "f")])
    return (f'<div class="bar" title="{t} journeys">{seg}</div><span class="small muted">{t} journeys: '
            f'{j.get("meets",0)} meet · {j.get("guarded",0)} guarded · {j.get("open",0)} open · '
            f'{j.get("not_built",0)} not built · {j.get("fails",0)} fail</span>')


def write(rel, title, body, section, **kw):
    depth = rel.count("/")
    root = "../" * depth
    page = env.get_template("base.html").render(
        title=title, body=body.replace("{root}", root), section=section, root=root,
        sections=SECTIONS, built=BUILT, description=kw.pop("description", kw.get("lede", "") or title), **kw)
    out = DOCS / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    WRITTEN.append(rel)


def redirect(rel, target, title):
    depth = rel.count("/")
    href = "../" * depth + target
    out = DOCS / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={href}"><link rel="canonical" href="{href}">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(title)} has moved</title></head>
<body style="font-family:system-ui,sans-serif;padding:24px"><p>{E(title)} has moved to <a href="{href}">{href}</a>.</p></body></html>
""", encoding="utf-8")
    WRITTEN.append(rel)


# --------------------------------------------------------------------------- build
BUILT = ""  # no build date: a rebuild with unchanged sources must be byte-identical (--check)


def main():
    branches = load("branches.yaml")
    B = {b["key"]: b for b in branches}
    progs = sorted(load("programmes.yaml"), key=lambda p: ([b["key"] for b in branches].index(p["branch"]), p["order"]))
    P = {p["key"]: p for p in progs}
    goals = load("goals.yaml")
    G = {g["key"]: g for g in goals}
    questions = load("questions.yaml")
    workflows = load("workflows.yaml")
    W = {w["key"]: w for w in workflows}
    exps = load("experiences.yaml")
    timeline = load("timeline.yaml")
    library = load("library.yaml")
    documents = load("documents.yaml")
    alldocs = [d for g in documents["groups"] for d in g["docs"]]
    CODES = documents.get("codes", {})

    def srclinks(text):
        return re.sub(r"\b(" + "|".join(sorted(CODES, key=len, reverse=True)) + r")\b",
                      lambda m: f'<a href="{CODES[m.group(1)]}">{m.group(1)}</a>', E(text)) if CODES else E(text)
    rows, notes = parse_crosswalk()
    R = {r["id"]: r for r in rows}
    decisions = parse_decisions()
    facts = delivery_facts()
    board = board_data()

    # integrity: every crosswalk row belongs to exactly one goal (A1 = mission)
    seen = Counter(r for g in goals for r in g["rows"])
    missing = [r["id"] for r in rows if r["id"] not in seen and r["id"] != "A1"]
    dup = [k for k, v in seen.items() if v > 1]
    unknown = [k for k in seen if k not in R]
    assert not (missing or dup or unknown), f"goal mapping: missing={missing} dup={dup} unknown={unknown}"
    for r in rows:
        r["goal"] = next((g["key"] for g in goals if r["id"] in g["rows"]), "mission")

    # journey statistics
    runs, catalog = board["runs"], board["catalog"]
    RK = {5: "meets", 4: "guarded", 3: "open", 2: "not_built", 0: "fails"}

    def jstats(filter_fn):
        c = Counter()
        for row in catalog:
            if filter_fn(row):
                c["total"] += 1
                r = runs.get(row["id"])
                if r is not None:
                    c[RK.get(r["rating"], "open")] += 1
        return dict(c)

    all_j = jstats(lambda r: True)
    prog_branch = lambda k: P[k]["branch"] if k in P else "all"
    done = facts["done"] | {s["n"] for s in board["slices"] if s["status"] == "done"}
    slices = [s for s in plan_slices(done) if s["n"] not in ("—",)]
    for s in slices:
        s["status"] = "done" if s["n"] in done else ("design first" if s["n"].startswith("SP") else "queued")
    n_done = sum(1 for s in slices if s["status"] == "done")
    n_dec = len(decisions)
    open_q = [q for q in questions if not q.get("decided")]
    prog_status = Counter(status_key(p["status"]) for p in progs)

    def bcolour(k):
        return B[k]["colour"] if k in B else "#7a7260"

    def btag(k):
        if k == "all":
            return '<span class="br" style="--c:#7a7260">All branches</span>'
        return f'<a class="br" style="--c:{bcolour(k)};text-decoration:none" href="{{root}}programmes/{branch_href(k)}">{E(B[k]["name"])}</a>'

    def branch_href(k):
        return {"junction": "convention.html"}.get(k, f"{k}.html")

    def plink(k):
        return f'<a href="{{root}}programmes/{k}.html">{E(P[k]["name"])}</a>' if k in P else E(k)

    def wlink(k):
        return f'<a href="{{root}}workflows/{k}.html">{E(W[k]["name"])}</a>' if k in W else E(k)

    def glink(k):
        return f'<a href="{{root}}strategy/goals/{k}.html">{G[k]["n"]}. {E(G[k]["name"])}</a>' if k in G else "The mission"

    def durl(d):
        return (f"https://docs.google.com/document/d/{d['id']}/edit" if d["kind"] == "doc"
                else f"https://drive.google.com/file/d/{d['id']}/view")

    def dlink(d):
        return f'<a href="{durl(d)}">{E(d["title"])}</a>'

    def qlink(q):
        return f'<a href="{{root}}history/questions.html#{q["id"]}">{q["id"]}</a>'

    def dlinks(ds):
        out = []
        for d in ds:
            m = re.match(r"D(\d+)$", d)
            if m and int(m.group(1)) in decisions:
                out.append(f'<a href="{{root}}status/index.html#D{m.group(1)}">{E(d)}</a>')
            else:
                out.append(E(d))
        return " · ".join(out)

    def proto(routes):
        return " ".join(f'<a class="tag" href="{{root}}prototype.html{E(r)}">{E(r)}</a>' for r in (routes or []))

    # ------------------------------------------------------------- tree diagram
    def tree_svg():
        def node(x, y, k, anchor="middle"):
            b = B[k]
            href = "{root}programmes/" + branch_href(k)
            return (f'<a href="{href}"><circle cx="{x}" cy="{y}" r="9" fill="{b["colour"]}"/>'
                    f'<text x="{x}" y="{y-34}" text-anchor="{anchor}" font-size="17" font-weight="700" fill="{b["colour"]}">{E(b["name"])}</text>'
                    f'<text x="{x}" y="{y-16}" text-anchor="{anchor}" font-size="12.5" fill="#57503f">{E(b["shape"])}</text></a>')
        s = ['<svg viewBox="0 0 720 340" role="img" aria-label="The four branches, Education, Leadership, Heritage and Care, meet at the Convention">',
             '<path d="M360 330 C360 280 360 250 360 215" stroke="#2b2416" stroke-width="10" fill="none" stroke-linecap="round"/>',
             ]
        for (x, y) in [(120, 100), (270, 75), (450, 75), (600, 100)]:
            s.append(f'<path d="M360 215 C360 150 {x} {y+60} {x} {y}" stroke="#57503f" stroke-width="4" fill="none" opacity=".45"/>')
        s.append(node(120, 100, "education"))
        s.append(node(270, 75, "leadership"))
        s.append(node(450, 75, "heritage"))
        s.append(node(600, 100, "care"))
        s.append('<a href="{root}programmes/convention.html"><circle cx="360" cy="200" r="15" fill="#6d7a19" stroke="#fffdf6" stroke-width="3"/>'
                 '<text x="385" y="197" font-size="15" font-weight="700" fill="#6d7a19">The Convention</text>'
                 '<text x="385" y="214" font-size="12" fill="#57503f">the junction where the branches meet</text></a>')
        s.append('<a href="{root}programmes/family-tree.html"><text x="450" y="20" text-anchor="middle" font-size="12.5" font-weight="600" fill="#7a5a2e">with the family tree</text></a>')
        s.append("</svg>")
        return '<div class="tree">' + "".join(s) + "</div>"

    # ------------------------------------------------------------- HOME
    meta, body = md_page("home.md")
    cards = [
        ("strategy/index.html", "1 · AFRP Strategy", "The Federation's current strategy, and how the Hub implements it on the CRM.", f"8 <small>goals</small>"),
        ("history/index.html", "2 · Evolution", "How the strategy got here since 2018, what is still to develop, and the open questions.", f"{len(open_q)} <small>open questions</small>"),
        ("programmes/index.html", "3 · Branches & programmes", "Education, Leadership, Heritage and Care, and the Convention where they meet; nineteen programmes and what each needs.", f"{len(progs)} <small>programmes</small>"),
        ("experiences/index.html", "4 · People & experiences", "Who uses the platform and what each of them needs.", f"{len(exps)} <small>kinds of people</small>"),
        ("workflows/index.html", "5 · Workflows", "How the work moves, and how the pieces hand off to each other.", f"{len(workflows)} <small>workflows</small>"),
        ("prototype/index.html", "6 · Prototype", "The integrated prototype: five lenses, with guided tours by branch and by journey.", "5 <small>lenses</small>"),
        ("status/index.html", "7 · Development status", "Decisions, open questions, the build track and how the journeys fare.", f"{all_j.get('meets',0)}/{all_j.get('total',0)} <small>journeys meet</small>"),
        ("library/index.html", "Library", "The earlier reference documents, dated, and the archive.", f"{len(library['reference'])} <small>documents</small>"),
    ]
    cardhtml = '<div class="grid">' + "".join(
        f'<a class="card" href="{{root}}{h}"><b>{t}</b><p>{d}</p><div class="fig">{f}</div></a>' for h, t, d, f in cards) + "</div>"
    seq = ('<div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(150px,1fr))">' + "".join(
        f'<div class="card stripe" style="--c:{c}"><b>{a}</b><p>{b}</p></div>' for a, b, c in [
            ("Proposal", "Raised on the Strategy or Evolution pages", "#9a720d"),
            ("Discussion", "A Q-number, discussed on GitHub and in the committee's draft", "#9a720d"),
            ("Decision", "Recorded as a D-number in the Decisions Register", "#4c6414"),
            ("Design note", "Written into the design record", "#4c6414"),
            ("Build", "A slice in the master plan, built in AFRP-Hub", "#2f5a73"),
            ("Verified", "Walked by the journeys, shown under Status", "#2f5a73")]) + "</div>")
    home_body = MD(body).replace("<!--TREE-->", tree_svg()).replace("<!--SECTIONS-->", cardhtml).replace("<!--SEQUENCE-->", seq)
    write("index.html", "AFRP Strategy and Hub", home_body, "home", heading=meta["heading"], kicker=meta["kicker"], lede=meta["lede"],
          chips=[f"{n_dec} decisions recorded", f"{len(open_q)} open questions", f"{len(progs)} programmes on four branches",
                 f"{all_j.get('total',0)} journeys walked", (f"{facts['tests']} tests green" if facts["tests"] else "")])

    # ------------------------------------------------------------- STRATEGY
    meta, body = md_page("strategy.md")
    gcards = '<div class="grid two">' + "".join(
        f'<a class="card stripe" style="--c:{bcolour(g["branches"][0]) if g["branches"][0] in B else "#4c6414"}" href="{{root}}strategy/goals/{g["key"]}.html">'
        f'<b>{g["n"]}. {E(g["name"])}</b><p>{E(g["hub"])}</p>'
        f'<div class="meta">{" ".join(btag(b) for b in g["branches"])} <span class="tag">{len(g["rows"])} elements</span></div></a>' for g in goals) + "</div>"
    write("strategy/index.html", "AFRP Strategy", MD(body).replace("<!--GOALS-->", gcards), "strategy",
          kicker=meta["kicker"], lede=meta["lede"], crumbs=[("Home", "index.html")])

    for g in goals:
        grows = [R[i] for i in g["rows"]]
        c = Counter(status_key(r["status"]) for r in grows)
        body = (f'<div class="note">Distilled from the Federation\'s documents, for the Strategic Planning Committee to confirm (D52).</div>'
                f'<p>{" ".join(btag(b) for b in g["branches"])}</p>'
                f'<h2>What the Federation has committed to</h2><p>{E(g["committed"])}</p>'
                f'<h2>What is still open</h2><p>{E(g["open"])}</p>'
                f'<h2>How the Hub implements it, on the CRM</h2><p>{E(g["hub"])}</p>'
                f'<h2>What no software can do</h2><p>{E(g["outside"])}</p>'
                f'<h2>Every element of the strategy under this goal</h2>'
                f'<p class="small muted">{", ".join(f"{v} {k}" for k, v in c.most_common())}. Sources are the Federation\'s documents, abbreviated as on the <a href="{{root}}strategy/crosswalk.html">crosswalk</a>.</p>'
                + table(["#", "Element", "Source", "Platform", "How the platform fulfils it"],
                        [[r["id"], inline(r["element"]), srclinks(r["source"]), status_tag(r["status"]), inline(r["how"])] for r in grows]))
        gd = [d for d in alldocs if g["key"] in d.get("goals", [])]
        if gd:
            body += ('<h2>The Federation\'s documents behind this goal</h2><p class="small muted">Links open in the Federation\'s shared drive, for people with access.</p>'
                     + ulist(gd, lambda d: f'{dlink(d)} <span class="muted small">({E(d["date"])} · {E(d["status"])})</span>'))
        qs = [q for q in open_q if q["goal"] == g["key"]]
        if qs:
            body += "<h2>Open questions</h2>" + ulist(qs, lambda q: f'{qlink(q)} {E(q["title"])} <span class="muted small">({E(q["owner"])})</span>')
        write(f"strategy/goals/{g['key']}.html", f"{g['n']}. {g['name']}", body, "strategy", kicker="Strategic goal",
              crumbs=[("Home", "index.html"), ("AFRP Strategy", "strategy/index.html")], lede=f"Goal {g['n']} of eight, distilled from the Federation's documents: what was committed, what is open, and how the Hub carries it out.")

    meta, body = md_page("documents.md")
    dbody = MD(body) + "<h2>The folders</h2><ul>" + "".join(f'<li><a href="{f["url"]}">{E(f["name"])}</a></li>' for f in documents.get("folders", [])) + "</ul>" + "<p class=\"small\"><b>Goals:</b> " + " · ".join(f'{g["n"]} {E(g["name"])}' for g in goals) + "</p>"
    for g in documents["groups"]:
        dbody += f'<h2 id="{g["key"]}">{E(g["name"])}</h2><p>{E(g["intro"])}</p>' + table(
            ["Document", "Date", "Status", "What it holds", "Goals"],
            [[f'<b>{dlink(d)}</b><br><span class="tag">{srclinks(d["code"])}</span>', E(d["date"]), E(d["status"]), E(d["summary"]),
              " ".join(f'<a class="tag" title="{E(G[k]["name"])}" href="{{root}}strategy/goals/{k}.html">{G[k]["n"]}</a>' for k in d.get("goals", [])) or '<span class="muted">—</span>'] for d in g["docs"]])
    write("strategy/documents.html", meta["title"], dbody, "strategy", kicker=meta["kicker"], lede=meta["lede"],
          crumbs=[("Home", "index.html"), ("AFRP Strategy", "strategy/index.html")], chips=[f"{len(alldocs)} documents"])

    meta, body = md_page("on-the-crm.md")
    write("strategy/on-the-crm.html", meta["title"], MD(body), "strategy", kicker=meta["kicker"], lede=meta["lede"],
          crumbs=[("Home", "index.html"), ("AFRP Strategy", "strategy/index.html")])

    # crosswalk
    sts = sorted({status_key(r["status"]) for r in rows})
    trs = "".join(
        f'<tr data-goal="{r["goal"]}" data-status="{status_key(r["status"])}" data-sec="{r["letter"]}"><td>{r["id"]}</td><td>{inline(r["element"])}</td>'
        f'<td>{srclinks(r["source"])}</td><td>{status_tag(r["status"])}</td><td>{inline(r["how"])}</td><td class="small">{glink(r["goal"]) if r["goal"] in G else "Mission"}</td></tr>'
        for r in rows)
    filt = ('<div class="filters"><select id="fg"><option value="">Every goal</option>' +
            "".join(f'<option value="{g["key"]}">{g["n"]}. {E(g["name"])}</option>' for g in goals) +
            '</select><select id="fs"><option value="">Every status</option>' + "".join(f'<option>{s}</option>' for s in sts) +
            '</select><select id="fx"><option value="">Every section</option>' +
            "".join(f'<option value="{l}">{l}. {E(n)}</option>' for l, n in OrderedDict((r["letter"], r["section"]) for r in rows).items()) +
            '</select><input id="fq" placeholder="Search" aria-label="Search"></div><p class="count" id="fc"></p>')
    script = """<script>
(function(){var g=document.getElementById('fg'),s=document.getElementById('fs'),x=document.getElementById('fx'),q=document.getElementById('fq'),c=document.getElementById('fc');
function f(){var n=0;document.querySelectorAll('#xw tbody tr').forEach(function(r){var ok=(!g.value||r.dataset.goal==g.value)&&(!s.value||r.dataset.status==s.value)&&(!x.value||r.dataset.sec==x.value)&&(!q.value||r.textContent.toLowerCase().indexOf(q.value.toLowerCase())>-1);r.style.display=ok?'':'none';if(ok)n++;});c.textContent=n+' of %d elements';}
[g,s,x].forEach(function(e){e.onchange=f});q.oninput=f;f();})();
</script>""" % len(rows)
    meta, body = md_page("crosswalk.md")
    xw = (MD(body) + filt + f'<div class="tw" id="xw"><table><thead><tr><th>#</th><th>Element</th><th>Source</th><th>Platform</th><th>How the platform fulfils it</th><th>Goal</th></tr></thead><tbody>{trs}</tbody></table></div>' + script)
    write("strategy/crosswalk.html", meta["title"], xw, "strategy", kicker=meta["kicker"], lede=meta["lede"],
          crumbs=[("Home", "index.html"), ("AFRP Strategy", "strategy/index.html")])

    # ------------------------------------------------------------- HISTORY
    meta, body = md_page("history.md")
    tl = ('<div class="legend"><span><i style="background:#9a720d"></i>The Federation\'s strategy</span><span><i style="background:#4c6414"></i>The platform\'s design and build</span><span><i style="background:#8c2f21"></i>Where they meet</span></div><div class="tl">' +
          "".join(f'<div class="ev {t["strand"]}"><div class="when">{E(t["date"])}</div><div class="what"><b>{E(t["title"])}</b><p>{E(t["text"])}</p></div></div>' for t in timeline) + "</div>")
    write("history/index.html", "How the strategy evolved", MD(body).replace("<!--TIMELINE-->", tl), "history",
          kicker=meta["kicker"], lede=meta["lede"], crumbs=[("Home", "index.html")])

    meta, body = md_page("whats-next.md")
    nt = table(["#", "Design note", "Covers", "Ready to write?"],
               [[n["id"], E(n["note"]), ", ".join(f'<a href="{{root}}strategy/crosswalk.html">{E(x)}</a>' for x in [n["covers"]]), inline(n["ready"])] for n in notes])
    write("history/whats-next.html", meta["title"], MD(body).replace("<!--NOTES-->", nt), "history",
          kicker=meta["kicker"], lede=meta["lede"], crumbs=[("Home", "index.html"), ("Evolution", "history/index.html")])

    meta, body = md_page("questions.md")
    qrows = "".join(
        f'<tr id="{q["id"]}" data-goal="{q["goal"]}" data-branch="{q["branch"]}"><td><b>{q["id"]}</b></td><td><b>{E(q["title"])}</b><br><span class="small">{E(q["detail"])}</span></td>'
        f'<td class="small">{E(q["owner"])}</td><td class="small">{glink(q["goal"])}<br>{btag(q["branch"])}</td>'
        f'<td class="small">{E(q["source"])}<br><a href="{REPO}/discussions?discussions_q={q["id"]}">Discuss {q["id"]}</a></td></tr>'
        for q in open_q)
    qfilt = ('<div class="filters"><select id="qg"><option value="">Every goal</option>' +
             "".join(f'<option value="{g["key"]}">{g["n"]}. {E(g["name"])}</option>' for g in goals) +
             '</select><select id="qb"><option value="">Every branch</option><option value="all">All branches</option>' +
             "".join(f'<option value="{b["key"]}">{E(b["name"])}</option>' for b in branches) + '</select></div>')
    qscript = """<script>(function(){var g=document.getElementById('qg'),b=document.getElementById('qb');function f(){document.querySelectorAll('#qt tbody tr').forEach(function(r){r.style.display=(!g.value||r.dataset.goal==g.value)&&(!b.value||r.dataset.branch==b.value)?'':'none'})}g.onchange=f;b.onchange=f;})();</script>"""
    write("history/questions.html", meta["title"], MD(body) + qfilt +
          f'<div class="tw" id="qt"><table><thead><tr><th>ID</th><th>Question</th><th>Owner</th><th>Goal · branch</th><th>Source · discuss</th></tr></thead><tbody>{qrows}</tbody></table></div>' + qscript,
          "history", kicker=meta["kicker"], lede=meta["lede"], crumbs=[("Home", "index.html"), ("Evolution", "history/index.html")])

    # ------------------------------------------------------------- PROGRAMMES
    def pcard(p):
        return (f'<a class="card stripe" style="--c:{bcolour(p["branch"])}" href="{{root}}programmes/{p["key"]}.html"><b>{E(p["name"])}</b>'
                f'<p>{E(p["summary"])}</p><div class="meta">{status_tag(p["status"])}{" <span class=tag>Flagship</span>" if p.get("flagship") else ""}'
                f' <span class="tag">{E(p["shape"])}</span></div></a>')

    meta, body = md_page("programmes.md")
    blocks = ""
    for b in branches:
        ps = [p for p in progs if p["branch"] == b["key"]]
        blocks += (f'<h2 style="color:{b["colour"]}">{E(b["name"])} <span class="muted small">· {E(b["shape"])}</span></h2>'
                   f'<p>{E(b["summary"])} <a href="{{root}}programmes/{branch_href(b["key"])}">More about {E(b["name"])}</a></p>'
                   f'<div class="grid">{"".join(pcard(p) for p in ps)}</div>')
    write("programmes/index.html", "Branches and programmes", MD(body).replace("<!--TREE-->", tree_svg()) + blocks, "programmes",
          kicker=meta["kicker"], lede=meta["lede"], crumbs=[("Home", "index.html")],
          chips=[f"{v} {k}" for k, v in prog_status.most_common()])

    for b in branches:
        if b["key"] == "junction":
            continue
        ps = [p for p in progs if p["branch"] == b["key"]]
        jj = jstats(lambda r, k=b["key"]: prog_branch(r["program"]) == k)
        qs = [q for q in open_q if q["branch"] == b["key"]]
        wfs = [w for w in workflows if b["key"] in w["branches"] or "all" in w["branches"]]
        body = (f'<p>{E(b["summary"])}</p><h2>Programmes on this branch</h2><div class="grid">{"".join(pcard(p) for p in ps)}</div>'
                f'<h2>How people move along it</h2><p><b>{E(b["shape"])}.</b> ' + {
                    "education": "A milestone on one programme opens an invitation to the next, by age. The order follows a young person's life: camp, then Project Hope, the Scholarship and Leadership Ramallah.",
                    "leadership": "Entry is at Emerging Leaders. People move by what they are ready to take on, and the order is a suggestion, never a prerequisite.",
                    "heritage": "There is no next step and no milestone invitation. People take part in any of these at any point in life.",
                    "care": "People arrive by choice or by capacity to give. The Ramallah Foundation and the Endowed Fund are funds: shown here, not joined."}[b["key"]] +
                ' Inside every programme, people move through the same five rungs: <b>hear · show up · take part · give or serve · lead</b> (D25).</p>'
                f'<h2>Outcomes this branch reports</h2>{ulist(b["outcomes"], E)}'
                f'<p class="small muted">How outcomes are measured for each branch is itself an open question ({qlink(next(q for q in questions if q["id"]=="Q-19"))}).</p>'
                f'<h2>How its journeys fare</h2>{journey_bar(jj)}'
                f'<h2>Workflows it uses</h2>{ulist([w["key"] for w in wfs], wlink)}')
        if qs:
            body += "<h2>Open questions</h2>" + ulist(qs, lambda q: f'{qlink(q)} {E(q["title"])}')
        write(f"programmes/{b['key']}.html", b["name"], body, "programmes", kicker="Branch", lede=b["shape"],
              crumbs=[("Home", "index.html"), ("Branches & programmes", "programmes/index.html")])

    RUNG = [("hear", "Hear"), ("show_up", "Show up"), ("take_part", "Take part"), ("give_serve", "Give or serve"), ("lead", "Lead")]
    for p in progs:
        b = B[p["branch"]]
        extra = ""
        if p["branch"] == "junction":
            extra = f'<div class="note green"><p><b>The junction.</b> {E(b["summary"])}</p></div>'
        rung = (table(["Rung", "For this programme"], [[n, E(p["rungs"][k])] for k, n in RUNG if k in p["rungs"]])
                if p.get("rungs") else '<p class="muted">Not stated in the record for this programme. The five rungs are hear, show up, take part, give or serve, and lead (D25).</p>')
        pw = [w for w in workflows if p["key"] in w.get("programmes", [])]
        body = (extra + '<dl class="kv">'
                f'<dt>Branch</dt><dd>{btag(p["branch"])} · {E(b["shape"])}</dd>'
                f'<dt>Owning entity</dt><dd>{E(p["entity"])}</dd>'
                f'<dt>Shape</dt><dd>{E(p["shape"])}{" · flagship" if p.get("flagship") else ""}</dd>'
                f'<dt>Built in the Hub</dt><dd>{status_tag(p["status"])}</dd></dl>'
                f'<h2>Who it\'s for</h2><p>{E(p["who"])}</p>'
                f'<h2>The operating year</h2><p>{E(p["year"])}</p>'
                f'<h2>The five rungs</h2>{rung}'
                f'<h2>Who runs it</h2><p>{E(p["organiser"])}</p>'
                f'<h2>Money</h2><p>{E(p["money"])}</p>'
                f'<h2>Hand-offs</h2><p>{E(p["handoffs"])}</p>'
                f'<h2>What it needs</h2><div class="grid two"><div class="card"><b>From the Federation\'s strategy</b>{ulist(p.get("strategy_needs"), E)}</div>'
                f'<div class="card"><b>From the platform</b>{ulist(p.get("platform_needs"), E)}</div></div>'
                f'<h2>Open questions</h2>{ulist(p.get("questions"), E)}'
                f'<h2>How its journeys fare</h2>{journey_bar(p.get("journeys", {}))}'
                f'<h2>Workflows it uses</h2>{ulist([w["key"] for w in pw], wlink)}'
                f'<h2>In the prototype</h2><p>{proto(p.get("prototype")) or "<span class=muted>No screen of its own.</span>"}</p>'
                f'<h2>Sources</h2>{ulist(p.get("sources"), src_link)}')
        write(f"programmes/{p['key']}.html", p["name"], body, "programmes", kicker=b["name"] + " · programme", lede=p["summary"],
              crumbs=[("Home", "index.html"), ("Branches & programmes", "programmes/index.html"), (b["name"], "programmes/" + (branch_href(p["branch"]) if p["branch"] != "junction" else "index.html"))])

    # ------------------------------------------------------------- EXPERIENCES
    LENS = {"door": "Front door", "member": "Member", "club": "Club", "program": "Programme", "federation": "Federation"}
    meta, body = md_page("experiences.md")
    ecards = ""
    for lk, ln in LENS.items():
        es = [e for e in exps if e["lens"] == lk]
        if not es:
            continue
        lj = jstats(lambda r, lk=lk: r["lens"] == lk)
        ecards += f'<h2>{ln} lens</h2>{journey_bar(lj)}<div class="grid">' + "".join(
            f'<a class="card" href="{{root}}experiences/{e["key"]}.html"><b>{E(e["name"])}</b><p>{E(e["who"])}</p></a>' for e in es) + "</div>"
    write("experiences/index.html", "People and experiences", MD(body) + ecards, "experiences", kicker=meta["kicker"], lede=meta["lede"],
          crumbs=[("Home", "index.html")])
    for e in exps:
        cat = e.get("catalogue", {})
        body = (f'<dl class="kv"><dt>Lens</dt><dd>{LENS.get(e["lens"], e["lens"])}</dd></dl>'
                f'<div class="grid two"><div class="card"><b>What they need</b>{ulist(e.get("needs"), E)}</div>'
                f'<div class="card"><b>What the platform does for them</b>{ulist(e.get("platform"), E)}</div></div>'
                f'<h2>Rules that protect them</h2>{ulist(e.get("privacy"), E)}'
                f'<h2>The journeys that test it</h2>{ulist(e.get("journeys"), jid)}'
                f'{journey_bar(cat)}<p class="small muted">Catalogue rows counted with: {E(cat.get("filter", ""))}.</p>'
                f'<h2>Not built yet</h2>{ulist(e.get("not_built"), jid)}'
                f'<h2>Workflows</h2>{ulist(e.get("workflows"), wlink)}'
                f'<h2>Start in the prototype</h2><p>{proto(e.get("prototype"))}</p>'
                f'<h2>Sources</h2>{ulist(e.get("sources"), src_link)}')
        write(f"experiences/{e['key']}.html", e["name"], body, "experiences", kicker=LENS.get(e["lens"], "") + " lens", lede=e["who"],
              crumbs=[("Home", "index.html"), ("People", "experiences/index.html")])

    # ------------------------------------------------------------- WORKFLOWS
    meta, body = md_page("workflows.md")
    hand = table(["Workflow", "Status", "Hands to"], [[wlink(w["key"]), status_tag(w["status"]), " · ".join(wlink(h) for h in w.get("hands_to", []))] for w in workflows])
    svc = {"membership-standing": "Membership and standing", "family-tree": "Family tree", "magazine": "Magazine",
           "events": "Events", "funds-ledger": "Funds and ledger", "directory-comms": "Directory and communications"}
    svct = table(["Shared service", "Used by"], [[n, " · ".join(wlink(w["key"]) for w in workflows if k in w.get("services", []))] for k, n in svc.items()])
    write("workflows/index.html", "Workflows", MD(body).replace("<!--HANDOFFS-->", hand).replace("<!--SERVICES-->", svct), "workflows",
          kicker=meta["kicker"], lede=meta["lede"], crumbs=[("Home", "index.html")])
    for w in workflows:
        steps = "<ol class=\"steps\">" + "".join(f'<li>{E(s["step"])}<span class="who">{E(s["who"])}</span></li>' for s in w["steps"]) + "</ol>"
        body = (f'<dl class="kv"><dt>Built in the Hub</dt><dd>{status_tag(w["status"])} <span class="small">{E(w.get("status_note",""))}</span></dd>'
                f'<dt>Branches</dt><dd>{" ".join(btag(b) for b in w.get("branches", []))}</dd>'
                f'<dt>Shared services</dt><dd>{E(", ".join(svc.get(s, s) for s in w.get("services", [])))}</dd>'
                f'<dt>Governed by</dt><dd>{dlinks(w.get("decisions", []))}</dd></dl>'
                f'<h2>Steps</h2>{steps}'
                f'<h2>Hands off to</h2>{ulist(w.get("handoff_notes"), E)}'
                f'<h2>Programmes that use it</h2><p>{" · ".join(plink(k) for k in w.get("programmes", [])) or "<span class=muted>All, through the shared services.</span>"}</p>'
                f'<h2>Open</h2>{ulist(w.get("open"), E)}'
                f'<h2>Deep dives and prototype</h2><p>{" ".join(f"<a class=tag href={{root}}{E(d)}>{E(d)}</a>" for d in w.get("deep_dive", []))} {proto(w.get("prototype"))}</p>'
                f'<h2>Sources</h2>{ulist(w.get("sources"), src_link)}')
        write(f"workflows/{w['key']}.html", w["name"], body, "workflows", kicker="Workflow", lede=w["summary"],
              crumbs=[("Home", "index.html"), ("Workflows", "workflows/index.html")])

    # ------------------------------------------------------------- PROTOTYPE
    meta, body = md_page("prototype.md")
    tours = "<h2>Tours by branch</h2>"
    for b in branches:
        ps = [p for p in progs if p["branch"] == b["key"] and p.get("prototype")]
        tours += f'<h3 style="color:{b["colour"]}">{E(b["name"])}</h3><ol>' + "".join(
            f'<li>{E(p["name"])}: {proto(p["prototype"])}</li>' for p in ps) + "</ol>"
    tours += "<h2>Tours by person</h2><ol>" + "".join(
        f'<li><a href="{{root}}experiences/{e["key"]}.html">{E(e["name"])}</a>: {proto(e.get("prototype"))}</li>' for e in exps if e.get("prototype")) + "</ol>"
    write("prototype/index.html", "The integrated prototype", MD(body) + tours, "prototype", kicker=meta["kicker"], lede=meta["lede"],
          crumbs=[("Home", "index.html")])

    # ------------------------------------------------------------- STATUS
    meta, body = md_page("status.md")
    dec = table(["#", "Decision", "Answer"], [[f'<span id="D{d["n"]}">D{d["n"]}</span>', inline(d["title"]), inline(d["answer"])] for d in decisions.values()])
    qsum = table(["ID", "Question", "Owner"], [[qlink(q), E(q["title"]), E(q["owner"])] for q in open_q])
    sl = table(["Slice", "What", "Stream", "Status"], [[E(s["n"]), E(s["name"]), E(s["stream"]), status_tag(s["status"])] for s in slices])
    lens_rows = [[LENS[k], journey_bar(jstats(lambda r, k=k: r["lens"] == k))] for k in LENS]
    br_rows = [[B[k]["name"], journey_bar(jstats(lambda r, k=k: prog_branch(r["program"]) == k))] for k in B] + \
              [["Across the platform", journey_bar(jstats(lambda r: r["program"] not in P))]]
    pg = table(["Programme", "Branch", "Status", "Journeys"], [[plink(p["key"]), btag(p["branch"]), status_tag(p["status"]), journey_bar(p.get("journeys", {}))] for p in progs])
    blockers = ulist([re.sub(r"\bDavid('s)?\b", lambda m: "the project owner" + ("'s" if m.group(1) else ""), b) for b in board.get("blockers", [])], inline)
    st = (MD(body)
          .replace("<!--FACTS-->", table(["Measure", "Now", "Source"], [
              ["Decisions recorded", str(n_dec), '<a href="' + BLOB + 'design/AFRP-Decisions-Register.md">Decisions Register</a>'],
              ["Open questions", str(len(open_q)), '<a href="{root}history/questions.html">Questions</a>'],
              ["Build slices done", f"{n_done} of {len(slices)}", '<a href="' + BLOB + 'plan/MASTER-PLAN.md">Master plan</a>, <a href="' + BLOB + 'design/AFRP-Delivery-Status.md">Delivery Status</a>'],
              ["Tests green", facts["tests"] or "Not stated", "Delivery Status, latest entry"],
              ["Journeys walked", f'{all_j.get("total",0)}: {all_j.get("meets",0)} meet, {all_j.get("guarded",0)} guarded, {all_j.get("open",0)} open, {all_j.get("not_built",0)} not built, {all_j.get("fails",0)} fail',
               f'Build board, generated {E(board["generated"][:10])}']]))
          .replace("<!--DECISIONS-->", dec).replace("<!--QUESTIONS-->", qsum).replace("<!--SLICES-->", sl)
          .replace("<!--BLOCKERS-->", blockers)
          .replace("<!--LENSES-->", table(["Lens", "Journeys"], lens_rows)).replace("<!--BRANCHES-->", table(["Branch", "Journeys"], br_rows))
          .replace("<!--PROGRAMMES-->", pg).replace("<!--BOARDDATE-->", E(board["generated"][:10])))
    write("status/index.html", "Development status", st, "status", kicker=meta["kicker"], lede=meta["lede"], crumbs=[("Home", "index.html")])

    # ------------------------------------------------------------- LIBRARY
    meta, body = md_page("library.md")
    ref = table(["Document", "Dated", "What it holds", "Superseded in part by"],
                [[f'<a href="{{root}}{E(d["file"])}">{E(d["title"])}</a>', E(d["dated"]), E(d["what"]), E(d.get("superseded", "—"))] for d in library["reference"]])
    arc = table(["Document", "What it was"], [[f'<a href="{{root}}library/archive/{E(d["file"])}">{E(d["title"])}</a>', E(d["what"])] for d in library["archive"]])
    write("library/index.html", "Library", MD(body).replace("<!--REFERENCE-->", ref).replace("<!--ARCHIVE-->", arc), "library",
          kicker=meta["kicker"], lede=meta["lede"], crumbs=[("Home", "index.html")])

    # ------------------------------------------------------------- moves and redirects
    redirect("AFRP-Design-Status.html", "status/index.html", "Design Status")
    for d in library["archive"]:
        src, dst = DOCS / d["file"], DOCS / "library/archive" / d["file"]
        if src.exists() and "http-equiv=\"refresh\"" not in src.read_text(encoding="utf-8", errors="ignore")[:600]:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
        redirect(d["file"], "library/archive/" + d["file"], d["title"])
        WRITTEN.append("library/archive/" + d["file"])

    DOCS.joinpath("site").mkdir(exist_ok=True)
    shutil.copyfile(SITE / "static/site.css", DOCS / "site/site.css")
    WRITTEN.append("site/site.css")
    (SITE / "MANIFEST.txt").write_text("\n".join(sorted(set(WRITTEN))) + "\n", encoding="utf-8")
    print(f"built {len(set(WRITTEN))} files; {n_dec} decisions, {len(open_q)} questions, {len(progs)} programmes, "
          f"{len(workflows)} workflows, {len(exps)} experiences, {len(rows)} crosswalk rows")


if __name__ == "__main__":
    main()
    if "--check" in sys.argv:
        diff = subprocess.run(["git", "status", "--porcelain", "docs", "site/MANIFEST.txt"], cwd=ROOT, capture_output=True, text=True).stdout
        if diff.strip():
            print("docs/ is out of date with site/ — run python site/build.py and commit:\n" + diff)
            sys.exit(1)
