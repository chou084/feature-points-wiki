"""事實回溯檢查：每張投影片的數字與來源，必須能在它標註的 Wiki 頁面找到。
用法：python tools/check_slides.py"""
import re, pathlib, sys
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "docs" / "wiki"
pages = {p.stem: p.read_text() for p in WIKI.rglob("*.md")}
html = BeautifulSoup((ROOT / "docs/slides/index.html").read_text(), "html.parser")
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?|\.\d+")
problems, checked = [], 0

for i, s in enumerate(html.select("section.slide"), 1):
    wiki = [w.strip() for w in s.get("data-wiki", "").split(",") if w.strip()]
    srcs = [x.strip() for x in s.get("data-src", "").split(",") if x.strip()]
    if not wiki:
        problems.append(f"[第 {i} 張] 沒有 data-wiki"); continue
    missing = [w for w in wiki if w not in pages]
    if missing:
        problems.append(f"[第 {i} 張] Wiki 頁不存在：{missing}"); continue
    corpus = "\n".join(pages[w] for w in wiki)
    for sid in srcs:
        if f"[{sid}]" not in corpus and f"{sid}" not in re.findall(r"S\d+", corpus):
            problems.append(f"[第 {i} 張] 標註來源 {sid}，但引用的 Wiki 頁沒有這個來源")
    for el in s.select("[data-nocheck]"):
        el.decompose()
    text = s.get_text(" ")
    for n in sorted(set(NUM.findall(text))):
        checked += 1
        if not re.search(r"(?<![\d.])" + re.escape(n) + r"(?![\d]|\.\d)", corpus):
            ctx = text[max(0, text.find(n) - 15): text.find(n) + len(n) + 10].replace("\n", " ")
            problems.append(f"[第 {i} 張] 數字「{n}」在 {wiki} 找不到　…{ctx.strip()}…")

print(f"檢查 {len(html.select('section.slide'))} 張投影片、{checked} 個數字，發現 {len(problems)} 個問題")
for p in problems: print(" -", p)
sys.exit(1 if problems else 0)
