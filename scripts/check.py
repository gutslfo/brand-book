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


def check(brand, base=Path(".")):
    fail, note = [], []
    if not brand.get("name"):
        fail.append("name is missing")
    colors = brand.get("colors") or []
    if len(colors) not in (6, 8):
        fail.append(f"the palette has {len(colors)} colours, it needs 6 or 8")
    for c in colors:
        if not HEX.match(c.get("hex", "")):
            fail.append(f"{c.get('name', '?')}: hex {c.get('hex')!r} is not #RRGGBB")
        if c.get("role") not in ROLES:
            fail.append(f"{c.get('name', '?')}: role {c.get('role')!r} is not one of {', '.join(ROLES)}")
    names = [c.get("name", "").lower() for c in colors]
    if len(set(names)) != len(names):
        fail.append("two colours share a name")
    roles = [c.get("role") for c in colors]
    for r in UNIQUE:
        if roles.count(r) != 1:
            fail.append(f"exactly one colour must have the role {r!r} (found {roles.count(r)})")
    if roles.count("secondary") > 1:
        fail.append("at most one colour can be secondary")
    share = sum(c.get("share", 0) for c in colors)
    if share != 100:
        fail.append(f"colour shares add up to {share}%, they must add up to 100%")
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
            fail.append(f"contrast of {label} is {r:.2f}, needs {hard}")
        elif r < soft:
            note.append(f"contrast of {label} is {r:.2f}, {soft} would be safer")

    fonts = brand.get("fonts") or {}
    for role in ("display", "text"):
        if not (fonts.get(role) or {}).get("family"):
            fail.append(f"fonts.{role}.family is missing")
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
        "fonts": {"display": {"family": "X"}, "text": {"family": "Y"}}}
    assert check(ok)[0] == [], check(ok)[0]
    bad = json.loads(json.dumps(ok))
    bad["colors"][3]["hex"] = "#F0B0A0"
    assert any("button" in f for f in check(bad)[0])
    bad["colors"].pop()
    assert any("6 or 8" in f for f in check(bad)[0])
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
