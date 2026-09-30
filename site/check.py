#!/usr/bin/env python3
"""Checks every generated page (the files listed in site/MANIFEST.txt).

1. Links: every relative link and #anchor resolves inside docs/.
2. Privacy (D50): no email address or phone number, and none of the surnames on a
   hashed deny-list (hashed so this public file does not itself list names).
3. Framing (D42, D46): "rails" and "pathway" appear only where a page explains
   that they were replaced.
Exit code 1 if anything fails.
"""
import hashlib, re, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DENY = {'0328a0ee3d2c8755', '16019fea43d823bf', '1a060fb491656c9a', '34953d15199f557d', '38e4001a27ab9a3a',
        '41b0fe9269c1111b', '42f9619553996b62', '4ef04f6a1edde0a0', '52d6497ca5403c3a', '5880260d9cbd2638',
        '5b1601b73d1b82c9', '61f72dd4215b80d3', '75e2c3daf84f48de', '7f1282974437f511', '833821d3971607c9',
        '8d9eb414226cc36c', '91ae85cc56d86beb', 'b8148c60c8b1ee22', 'c1f5b651a4788229', 'cb76446389d0f6a7',
        'd2e541f47b1a02db', 'd687aa910c47ea90', 'dbaf86dd80e3bcd5', 'dc9b51b9b7801d64', 'e13f17796e5a37f9',
        'e681426f7b2ae73e', 'e81ad089f4d9534a', 'e8f9cc6451de9148', 'ec51c88873f0e902', 'f799a3d29daab95f',
        'fa60414c1b5d6256'}
FRAMING_OK = re.compile(r"branch|D38|D42|D46|replaced|superseded|once called|disagree|older framing|prototype|shared services", re.I)


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.text, self.blocks, self._buf, self._skip = [], set(), [], [], [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in ("script", "style"):
            self._skip += 1
        if tag in ("p", "li", "td", "div", "h1", "h2", "h3"):
            self._flush()

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip -= 1
        if tag in ("p", "li", "td", "div", "h1", "h2", "h3"):
            self._flush()

    def handle_data(self, d):
        if not self._skip:
            self.text.append(d)
            self._buf.append(d)

    def _flush(self):
        t = " ".join(self._buf).strip()
        if t:
            self.blocks.append(t)
        self._buf = []


def parse(path):
    p = P()
    p.feed(path.read_text(encoding="utf-8", errors="ignore"))
    p._flush()
    return p


def main():
    manifest = [l for l in (ROOT / "site/MANIFEST.txt").read_text().split() if l.endswith(".html")]
    generated = [m for m in manifest if not m.startswith("library/archive/")]
    problems = []
    cache = {}
    for rel in generated:
        path = DOCS / rel
        p = cache.setdefault(rel, parse(path))
        for href in p.links:
            if re.match(r"^(https?:|mailto:|#/)", href) or href.startswith("prototype.html#") :
                continue
            target, _, frag = href.partition("#")
            if target == "":
                if frag and frag not in p.ids:
                    problems.append(f"{rel}: missing anchor #{frag}")
                continue
            tpath = (path.parent / target).resolve()
            if not tpath.exists():
                problems.append(f"{rel}: broken link {href}")
                continue
            if frag and not frag.startswith("/") and tpath.suffix == ".html":
                trel = str(tpath.relative_to(DOCS.resolve()))
                tp = cache.setdefault(trel, parse(tpath))
                if frag not in tp.ids:
                    problems.append(f"{rel}: missing anchor {href}")
        text = " ".join(p.text)
        if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text):
            problems.append(f"{rel}: email address")
        if re.search(r"\(?\b\d{3}\)?[ .-]\d{3}[ .-]\d{4}\b", text):
            problems.append(f"{rel}: phone number")
        for tok in set(re.findall(r"[A-Za-z]+", text)):
            if hashlib.sha256(tok.lower().encode()).hexdigest()[:16] in DENY:
                problems.append(f"{rel}: a name on the deny-list")
        for b in p.blocks:
            b = re.sub(r"#/\S+", "", b)
            if re.search(r"\brails?\b|pathways?\b", b, re.I) and not FRAMING_OK.search(b):
                problems.append(f"{rel}: old framing without explanation: {b[:90]}")
    for p in problems:
        print("FAIL", p)
    print(f"checked {len(generated)} pages: {len(problems)} problems")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
