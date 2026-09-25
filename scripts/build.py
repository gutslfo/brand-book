"""Build the explorer or the brand book from brand.json.

    python build.py explorer path/to/brand.json [-o explorer.html]
    python build.py book     path/to/brand.json [-o brand-book.html]

File paths in brand.json (logo.file, imagery.images[].file) are resolved relative to
brand.json and embedded as data URIs, so the page is one self-contained file. The
logo's aspect ratio is measured. Stdlib only.
"""
import argparse, base64, json, re, struct, sys
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
TEMPLATES = {"explorer": "explorer.html", "book": "brand-book.html"}
MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}


def svg_ratio(text):
    vb = re.search(r'viewBox\s*=\s*["\']\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)', text)
    if vb:
        return float(vb.group(1)) / float(vb.group(2))
    w = re.search(r'<svg[^>]*\swidth\s*=\s*["\']([\d.]+)', text)
    h = re.search(r'<svg[^>]*\sheight\s*=\s*["\']([\d.]+)', text)
    if w and h:
        return float(w.group(1)) / float(h.group(1))
    raise ValueError("SVG has neither a viewBox nor width and height")


def raster_ratio(data):
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", data[16:24])
        return w / h
    if data[:2] == b"\xff\xd8":  # JPEG: walk the segments to the first SOF marker
        i = 2
        while i < len(data):
            marker, size = data[i + 1], struct.unpack(">H", data[i + 2:i + 4])[0]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack(">HH", data[i + 5:i + 9])
                return w / h
            i += 2 + size
    raise ValueError("unsupported image: use SVG, PNG or JPEG")


def data_uri(path, what):
    ext = path.suffix.lower()
    if ext not in MIME:
        sys.exit(f"{what}: {path.name} is not SVG, PNG or JPEG")
    data = path.read_bytes()
    return data, ext, f"data:{MIME[ext]};base64,{base64.b64encode(data).decode()}"


def embed_files(brand, base):
    logo = brand.get("logo") or {}
    if logo.get("file"):
        data, ext, logo["src"] = data_uri((base / logo["file"]).resolve(), "logo")
        logo["ratio"] = round(svg_ratio(data.decode("utf-8")) if ext == ".svg" else raster_ratio(data), 4)
    for img in (brand.get("imagery") or {}).get("images") or []:
        if img.get("file"):
            img["src"] = data_uri((base / img["file"]).resolve(), "image")[2]
    return brand


def build(kind, brand_path, out=None):
    brand_path = Path(brand_path).resolve()
    brand = embed_files(json.loads(brand_path.read_text(encoding="utf-8")), brand_path.parent)
    template = (ASSETS / TEMPLATES[kind]).read_text(encoding="utf-8")
    payload = json.dumps(brand, ensure_ascii=False).replace("</", "<\\/")
    if "/*__BRAND__*/null" not in template:
        sys.exit("template is missing the /*__BRAND__*/null placeholder")
    html = template.replace("/*__BRAND__*/null", payload)
    out = Path(out) if out else brand_path.parent / TEMPLATES[kind]
    out.write_text(html, encoding="utf-8")
    print(f"{kind}: {out}")
    return out


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("kind", choices=TEMPLATES)
    p.add_argument("brand")
    p.add_argument("-o", "--out")
    a = p.parse_args()
    build(a.kind, a.brand, a.out)
