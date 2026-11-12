"""Wiki Lint：依 AGENTS.md 第 5 節檢查 docs/wiki/。用法：python tools/lint.py"""
import re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "docs" / "wiki"
SRC_IDS = set(re.findall(r"^\| (S\d+) \|", (ROOT / "raw/sources.md").read_text(), re.M))

pages = [p for p in WIKI.rglob("*.md") if p.name not in ("index.md", "log.md")]
problems = []

def fm(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""

# (d) 斷掉的連結 + 收集被連到的頁面
linked = set()
for p in list(WIKI.rglob("*.md")):
    for target in re.findall(r"\]\(([^)#]+\.md)\)", p.read_text()):
        t = (p.parent / target).resolve()
        if not t.exists():
            problems.append(f"[斷連結] {p.relative_to(ROOT)} → {target}")
        else:
            linked.add(t)

for p in pages:
    text = p.read_text()
    rel = p.relative_to(ROOT)
    meta = fm(text)
    if not meta:
        problems.append(f"[缺 frontmatter] {rel}")
    # 來源 ID 必須存在於 raw/sources.md
    for sid in set(re.findall(r"\[(S\d+)\]", text)) | set(re.findall(r"S\d+", meta)):
        if sid not in SRC_IDS:
            problems.append(f"[未知來源 ID] {rel}: {sid}")
    # frontmatter sources 要涵蓋內文用到的 ID
    declared = set(re.findall(r"S\d+", re.search(r"sources: \[(.*?)\]", meta).group(1))) if meta else set()
    used = set(re.findall(r"\[(S\d+)\]", text))
    if used - declared:
        problems.append(f"[frontmatter 漏列來源] {rel}: {sorted(used - declared)}")
    # (a) 無來源 ID 的事實句（只檢查概念頁「一句話定義／直覺解釋／重點」段落）
    if "/concepts/" in str(p):
        section = None
        in_code = in_math = False
        table_src = False
        lines = text.splitlines()
        for idx, line in enumerate(lines):
            s = line.strip()
            nxt = lines[idx+1].strip() if idx + 1 < len(lines) else ""
            if s.startswith("|") and nxt.startswith("|---"):  # 表頭列
                table_src = bool(re.search(r"\[S\d+\]", s)); continue
            if not s.startswith("|"): table_src = False
            if s.startswith("|") and table_src: continue  # 表頭已標來源，資料列繼承
            if s.startswith("```"): in_code = not in_code; continue
            if s.startswith("$$"):
                if not (s.endswith("$$") and len(s) > 2): in_math = not in_math
                continue
            if in_code or in_math: continue
            if s.startswith("## "): section = s[3:]; continue
            if section not in ("一句話定義", "直覺解釋", "重點"): continue
            if not s or s.startswith((">", "**", "|---")): continue
            if not re.search(r"\[S\d+\]", s):
                problems.append(f"[無來源事實句] {rel} ({section}): {s[:40]}")
    # (c) 孤兒頁
    if p.resolve() not in linked:
        problems.append(f"[孤兒頁] {rel}")

print(f"檢查 {len(pages)} 頁，發現 {len(problems)} 個問題")
for x in problems: print(" -", x)
sys.exit(1 if problems else 0)
