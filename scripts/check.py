"""Check brand.json before building. Stdlib only.

    python check.py path/to/brand.json
    python check.py --selftest

Prints FAIL lines (must be fixed, or explicitly accepted by the user) and NOTE lines
(worth a look). Exit code 1 when anything fails.
"""
import json, re, sys
from pathlib import Path

HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")
UNIQUE = ("dark", "light", "primary", "accent")
ROLES = UNIQUE + ("secondary", "support")
MISUSE = {"stretch", "rotate", "recolor", "effects", "busy", "contrast", "crowd", "small"}


def lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ratio(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + 0.05) / (y + 0.05)


def check_palette(colors, where=""):
    """Structure and contrast of one palette. `where` prefixes every message."""
    fail, note = [], []
    if len(colors) not in (6, 8):
        fail.append(f"{where}the palette has {len(colors)} colours, it needs 6 or 8")
    for c in colors:
        if not HEX.match(c.get("hex", "")):
            fail.append(f"{where}{c.get('name', '?')}: hex {c.get('hex')!r} is not #RRGGBB")
        if c.get("role") not in ROLES:
            fail.append(f"{where}{c.get('name', '?')}: role {c.get('role')!r} is not one of {', '.join(ROLES)}")
    names = [c.get("name", "").lower() for c in colors]
    if len(set(names)) != len(names):
        fail.append(f"{where}two colours share a name")
    roles = [c.get("role") for c in colors]
    for r in UNIQUE:
        if roles.count(r) != 1:
            fail.append(f"{where}exactly one colour must have the role {r!r} (found {roles.count(r)})")
    if roles.count("secondary") > 1:
        fail.append(f"{where}at most one colour can be secondary")
    share = sum(c.get("share", 0) for c in colors)
    if share != 100:
        fail.append(f"{where}colour shares add up to {share}%, they must add up to 100%")
    if fail:  # contrast checks need a valid palette
        return fail, note

    hexes = {r: next(c["hex"] for c in colors if c["role"] == r) for r in UNIQUE}
    hexes["secondary"] = next((c["hex"] for c in colors if c["role"] == "secondary"), hexes["primary"])
    name = {c["hex"]: c["name"] for c in colors}
    on = lambda bg: max((hexes["dark"], hexes["light"]), key=lambda fg: ratio(fg, bg))
    tests = [  # (label, ratio, fail below, note below)
        (f"body text, {name[hexes['dark']]} on {name[hexes['light']]}", ratio(hexes["dark"], hexes["light"]), 4.5, 7),
        (f"text on {name[hexes['primary']]} (cover, slides)", ratio(on(hexes["primary"]), hexes["primary"]), 3, 4.5),
        (f"button label on {name[hexes['accent']]}", ratio(on(hexes["accent"]), hexes["accent"]), 4.5, 4.5),
        (f"{name[hexes['accent']]} button on {name[hexes['light']]}", ratio(hexes["accent"], hexes["light"]), 3, 3),
        (f"{name[hexes['primary']]} logo and headlines on {name[hexes['light']]}", ratio(hexes["primary"], hexes["light"]), 3, 4.5),
        (f"text on {name[hexes['secondary']]} panels", ratio(on(hexes["secondary"]), hexes["secondary"]), 3, 4.5),
    ]
    for label, r, hard, soft in tests:
        if r < hard:
            fail.append(f"{where}contrast of {label} is {r:.2f}, needs {hard}")
        elif r < soft:
            note.append(f"{where}contrast of {label} is {r:.2f}, {soft} would be safer")
    return fail, note


def catalogue():
    path = Path(__file__).resolve().parent.parent / "assets" / "fonts.json"
    if not path.exists():
        return None
    return {r[0].lower(): r for r in json.loads(path.read_text(encoding="utf-8"))}


def check_font(font, where, cat, base):
    fail = []
    fam = (font or {}).get("family")
    if not fam:
        return [f"{where}.family is missing"]
    if font.get("file"):
        p = base / font["file"]
        if not p.exists():
            fail.append(f"{where}: font file {p} does not exist")
        elif p.suffix.lower() not in (".woff2", ".woff", ".otf", ".ttf"):
            fail.append(f"{where}: {p.name} must be WOFF2, WOFF, OTF or TTF")
    elif not font.get("local") and cat is not None:
        row = cat.get(fam.lower())
        if not row:
            fail.append(f"{where}: {fam!r} is not on Google Fonts (check the spelling, or mark it local)")
        else:
            missing = [w for w in font.get("weights") or [] if w not in row[2]]
            if missing:
                fail.append(f"{where}: {fam} has no weight {', '.join(map(str, missing))} (it ships {' '.join(map(str, row[2]))})")
    return fail


def check(brand, base=Path(".")):
    fail, note = [], []
    if not brand.get("name"):
        fail.append("name is missing")
    explore = brand.get("explore") or {}
    colors = brand.get("colors") or []
    for i, pal in enumerate(explore.get("palettes") or []):
        f, n = check_palette(pal.get("colors") or [], f"proposal {pal.get('name') or i + 1}: ")
        fail += f
        note += n
    if colors or not explore.get("palettes"):
        f, n = check_palette(colors)
        fail += f
        note += n
    names = [c.get("name", "").lower() for c in colors or (explore.get("palettes") or [{}])[0].get("colors", [])]

    fonts = brand.get("fonts") or {}
    cat = catalogue()
    if cat is None:
        note.append("assets/fonts.json is missing: font names were not checked (run fonts.py refresh)")
    for role in ("display", "text", "mono"):
        if role in fonts or role != "mono":
            fail += check_font(fonts.get(role), f"fonts.{role}", cat, base)
    for p in explore.get("pairings") or []:
        for role in ("display", "text", "mono"):
            if p.get(role) and cat is not None and p[role].lower() not in cat:
                fail.append(f"pairing {p.get('display')} + {p.get('text')}: {p[role]!r} is not on Google Fonts")
    for role, fams in (explore.get("shortlist") or {}).items():
        for fam in fams:
            if cat is not None and fam.lower() not in cat:
                note.append(f"shortlist {role}: {fam!r} is not on Google Fonts, the explorer will skip it")
    for lvl in (brand.get("type") or {}).get("scale") or []:
        if lvl.get("size", 12) < 12:
            fail.append(f"type level {lvl.get('level')} is {lvl.get('size')} px, the floor is 12 px")

    logo = brand.get("logo") or {}
    if logo.get("file"):
        p = base / logo["file"]
        if not p.exists():
            fail.append(f"logo file {p} does not exist")
        elif p.suffix.lower() not in (".svg", ".png", ".jpg", ".jpeg"):
            fail.append(f"logo file {p.name} must be SVG, PNG or JPEG")
    else:
        note.append("no logo file: the book will set the name as a wordmark in the display font")
    for n in logo.get("backgrounds") or []:
        if n.lower() not in names:
            fail.append(f"logo.backgrounds lists {n!r}, which is not in the palette")
    for m in logo.get("misuse") or []:
        if m not in MISUSE:
            fail.append(f"logo.misuse has {m!r}, known values are {', '.join(sorted(MISUSE))}")

    ess = brand.get("essence") or {}
    if not ess.get("purpose"):
        note.append("essence.purpose is empty: the Essence page will be thin")
    if len(ess.get("voice") or []) < 3:
        note.append("fewer than 3 voice pairs")
    if not brand.get("never"):
        note.append("the never list is empty")
    return fail, note


def selftest():
    assert abs(ratio("#000000", "#FFFFFF") - 21) < 1e-9
    assert abs(ratio("#FFFFFF", "#FFFFFF") - 1) < 1e-9
    assert round(ratio("#767676", "#FFFFFF"), 2) == 4.54  # the classic AA grey
    ok = {"name": "T", "colors": [
        {"name": "A", "hex": "#FFFFFF", "role": "light", "share": 60},
        {"name": "B", "hex": "#111111", "role": "dark", "share": 20},
        {"name": "C", "hex": "#123C69", "role": "primary", "share": 10},
        {"name": "D", "hex": "#A33A1A", "role": "accent", "share": 5},
        {"name": "E", "hex": "#DDDDDD", "role": "secondary", "share": 3},
        {"name": "F", "hex": "#888888", "role": "support", "share": 2}],
        "fonts": {"display": {"family": "Lora", "weights": [400, 700]}, "text": {"family": "Inter", "weights": [400, 600]}}}
    assert check(ok)[0] == [], check(ok)[0]
    bad = json.loads(json.dumps(ok))
    bad["colors"][3]["hex"] = "#F0B0A0"
    assert any("button" in f for f in check(bad)[0])
    bad["colors"].pop()
    assert any("6 or 8" in f for f in check(bad)[0])
    if catalogue() is not None:
        typo = json.loads(json.dumps(ok))
        typo["fonts"]["display"] = {"family": "Lorra"}
        typo["fonts"]["text"]["weights"] = [400, 1000]
        f = check(typo)[0]
        assert any("Lorra" in x for x in f) and any("no weight 1000" in x for x in f), f
        own = json.loads(json.dumps(ok))
        own["fonts"]["display"] = {"family": "House Serif", "local": True}
        assert check(own)[0] == [], check(own)[0]
    prop = json.loads(json.dumps(ok))
    prop["explore"] = {"palettes": [{"name": "A", "colors": ok["colors"]}, {"name": "B", "colors": bad["colors"]}]}
    del prop["colors"]
    f = check(prop)[0]
    assert f and all(x.startswith("proposal B: ") for x in f), f
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
        sys.exit(0)
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    fail, note = check(json.loads(path.read_text(encoding="utf-8")), path.parent)
    for f in fail:
        print("FAIL ", f)
    for n in note:
        print("NOTE ", n)
    print("ok" if not fail else f"{len(fail)} to fix")
    sys.exit(1 if fail else 0)
