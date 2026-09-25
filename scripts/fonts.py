"""Search the Google Fonts catalogue. Stdlib only.

    python fonts.py refresh                      # download the catalogue into assets/fonts.json
    python fonts.py search [--category serif] [--weights 2] [--query grot] [--skip-top 20] [--limit 40]
    python fonts.py check "Family Name" ["Other Family" ...]

The catalogue is a compact snapshot of fonts.google.com/metadata/fonts: every family with a
Latin subset, its category, the upright weights it ships between 100 and 900, and its
popularity rank (1 = most used on the web). `--skip-top N` leaves out the N most used
families, which is how a proposal avoids the fonts every generated site already uses.
"""
import argparse, json, sys, urllib.request
from pathlib import Path

CATALOGUE = Path(__file__).resolve().parent.parent / "assets" / "fonts.json"
SOURCE = "https://fonts.google.com/metadata/fonts"
CATEGORIES = {"serif": "Serif", "sans": "Sans Serif", "display": "Display",
              "handwriting": "Handwriting", "mono": "Monospace"}


def refresh():
    req = urllib.request.Request(SOURCE, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8")
    meta = json.loads(raw[raw.index("{"):])
    out = []
    for f in meta["familyMetadataList"]:
        if "latin" not in f["subsets"] or f.get("isBrandFont"):
            continue
        weights = sorted(int(k) for k in f["fonts"] if k.isdigit() and 100 <= int(k) <= 900)
        if not weights:
            continue
        out.append([f["family"], f["category"], weights, f.get("popularity") or 9999])
    out.sort(key=lambda r: r[3])
    CATALOGUE.write_text(json.dumps(out, separators=(",", ":")), encoding="utf-8")
    print(f"{len(out)} families written to {CATALOGUE}")


def load():
    if not CATALOGUE.exists():
        sys.exit(f"no catalogue at {CATALOGUE}: run `python fonts.py refresh`")
    return json.loads(CATALOGUE.read_text(encoding="utf-8"))


def search(category=None, weights=1, query=None, skip_top=0, limit=40):
    rows = load()
    if category:
        rows = [r for r in rows if r[1] == CATEGORIES[category]]
    rows = [r for r in rows if len(r[2]) >= weights and r[3] > skip_top]
    if query:
        rows = [r for r in rows if query.lower() in r[0].lower()]
    return rows[:limit]


def check(names):
    index = {r[0].lower(): r for r in load()}
    return {n: index.get(n.lower()) for n in names}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("refresh")
    s = sub.add_parser("search")
    s.add_argument("--category", choices=CATEGORIES)
    s.add_argument("--weights", type=int, default=1, help="minimum number of upright weights")
    s.add_argument("--query")
    s.add_argument("--skip-top", type=int, default=0)
    s.add_argument("--limit", type=int, default=40)
    c = sub.add_parser("check")
    c.add_argument("names", nargs="+")
    a = p.parse_args()
    if a.cmd == "refresh":
        refresh()
    elif a.cmd == "search":
        for fam, cat, w, pop in search(a.category, a.weights, a.query, a.skip_top, a.limit):
            print(f"{pop:>5}  {fam:<32} {cat:<11} {' '.join(map(str, w))}")
    else:
        missing = 0
        for name, row in check(a.names).items():
            print(f"ok       {row[0]} ({row[1]}, weights {' '.join(map(str, row[2]))})" if row else f"MISSING  {name}")
            missing += row is None
        sys.exit(1 if missing else 0)
