"""Fill planned image slots by reusing photos the site already has (docs/image-reuse.json).

For every slot whose source photo exists in src/static/images/, this crops the source to the
slot's size, saves it under the slot's file name, and rewrites the slot's alt text in the page
source so it describes what the photo actually shows. Slots whose source is not made yet are
skipped and filled on a later run. Run it, then `python3 build.py`.
"""
import glob, json, re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "src" / "static" / "images"
SOURCES = sorted(glob.glob(str(ROOT / "src/pages/**/*.html"), recursive=True)) + [str(ROOT / "src/data/site.json")]
reuse = {k: v for k, v in json.load(open(ROOT / "docs/image-reuse.json")).items() if not k.startswith("_")}

def alts_and_sizes():
    alts, sizes = {}, {}
    for f in SOURCES:
        s = open(f).read()
        for m in re.finditer(r"img\('([^']+)',\s*'((?:[^'\\]|\\.)*)',\s*(\d+),\s*(\d+)", s):
            alts.setdefault(m.group(1), m.group(2)); sizes.setdefault(m.group(1), (int(m.group(3)), int(m.group(4))))
        for m in re.finditer(r'image:\s*(\S+)\n\s*alt:\s*"([^"]*)"', s):
            alts.setdefault(m.group(1), m.group(2)); sizes.setdefault(m.group(1), (1920, 1080))
        for m in re.finditer(r'"card_image":\s*"([^"]+)",\s*"card_alt":\s*"([^"]*)"', s):
            alts.setdefault(m.group(1), m.group(2))
    return alts, sizes

alts, sizes = alts_and_sizes()
done = waiting = 0
for slot, src in reuse.items():
    if not (IMG / src).exists():
        waiting += 1
        continue
    W, H = sizes.get(slot, (1200, 800))
    im = Image.open(IMG / src).convert("RGB"); w, h = im.size
    sc = max(W / w, H / h); im = im.resize((round(w * sc), round(h * sc)), Image.LANCZOS)
    l, t = (im.width - W) // 2, (im.height - H) // 2
    im.crop((l, t, l + W, t + H)).save(IMG / slot, quality=86)
    new_alt = alts.get(src)
    if new_alt and alts.get(slot) != new_alt:
        for f in SOURCES:
            s = open(f).read(); o = s
            s = re.sub(r"(img\('" + re.escape(slot) + r"',\s*')(?:[^'\\]|\\.)*(')", lambda m: m.group(1) + new_alt.replace("'", "\\'") + m.group(2), s)
            s = re.sub(r'(image:\s*' + re.escape(slot) + r'\n\s*alt:\s*")[^"]*(")', lambda m: m.group(1) + new_alt.replace('"', "'") + m.group(2), s)
            s = re.sub(r'("card_image":\s*"' + re.escape(slot) + r'",\s*"card_alt":\s*")[^"]*(")', lambda m: m.group(1) + new_alt.replace('"', "'") + m.group(2), s)
            if s != o: open(f, "w").write(s)
    done += 1
print(f"{done} slots filled from existing photos, {waiting} waiting on a photo not made yet")
