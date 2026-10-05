"""Build, check and stage the strategy site in one step (D99 item 5).

Run from the repository root:  python site/publish.py

It runs site/build.py and site/check.py, stops on the first failure with that
step's exit code, then stages the sources and docs/ together so a commit can
never carry the sources without the pages they build. It does not commit or
push: the commit message names the pass, and the session writes it.

Two publishes on 4 October 2026 shipped without docs/ because a YAML error in
the build was hidden by a pipe to `tail`; this script reads the build's exit
code itself.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ["design", "plan", "site", "README.md", "docs"]
NEVER_STAGED = ["docs/site/afrp-logo-white.png"]  # rewritten by every build; byte-identical in content


def run(step: str, args: list[str]) -> str:
    proc = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True)
    out = (proc.stdout + proc.stderr).strip()
    if proc.returncode != 0:
        print(out)
        print(f"\npublish: {step} failed with exit code {proc.returncode}; nothing staged.")
        sys.exit(proc.returncode)
    last = out.splitlines()[-1] if out else ""
    print(f"{step}: {last}")
    return out


def main() -> None:
    run("build", ["site/build.py"])
    out = run("check", ["site/check.py"])
    if " 0 problems" not in out.splitlines()[-1]:
        print("\npublish: check reported problems; nothing staged.")
        sys.exit(1)
    exclude = [f":!{p}" for p in NEVER_STAGED]
    subprocess.run(["git", "add", "-A", *SOURCES, *exclude], cwd=ROOT, check=True)
    staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=ROOT,
                            capture_output=True, text=True, check=True).stdout.split()
    sources = [f for f in staged if not f.startswith("docs/")]
    pages = [f for f in staged if f.startswith("docs/")]
    if sources and not pages:
        # Some sources (MASTER-PLAN's prose sections, CLAUDE.md) render to no page.
        print("note: sources staged and no page under docs/ changed; the build passed, so these sources render nowhere.")
    print(f"staged: {len(sources)} source files, {len(pages)} pages. Commit with a message naming the pass.")


if __name__ == "__main__":
    main()
