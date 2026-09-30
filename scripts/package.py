"""Package the skill as the ZIP the Claude apps accept: one brand-book/ folder holding SKILL.md,
references, assets and scripts. The output is byte-for-byte stable, so it only changes when the skill does.

    python scripts/package.py            # writes docs/brand-book.zip
    python scripts/package.py --check    # exits 1 if docs/brand-book.zip is out of date
"""
import argparse, io, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "brand-book.zip"
PARTS = ["SKILL.md", "LICENSE", "references", "assets", "scripts"]


def build() -> bytes:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    front = text.split("---")[1]
    name = re.search(r"^name: (.+)$", front, re.M).group(1).strip()
    desc = re.search(r"^description: (.+)$", front, re.M).group(1).strip()
    if len(desc) > 1024:
        sys.exit(f"SKILL.md description is {len(desc)} characters; the Claude apps accept 1024 at most")
    files = []
    for part in PARTS:
        p = ROOT / part
        files += [p] if p.is_file() else sorted(f for f in p.rglob("*") if f.is_file() and "__pycache__" not in f.parts)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            info = zipfile.ZipInfo(f"{name}/{f.relative_to(ROOT).as_posix()}", date_time=(2026, 1, 1, 0, 0, 0))
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, f.read_bytes())
    return buf.getvalue()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    data = build()
    if ap.parse_args().check:
        if not OUT.exists() or OUT.read_bytes() != data:
            sys.exit("docs/brand-book.zip is out of date: run python scripts/package.py")
        print("docs/brand-book.zip is up to date")
    else:
        OUT.write_bytes(data)
        print(f"{OUT.relative_to(ROOT)}: {len(data) // 1024} KB")
