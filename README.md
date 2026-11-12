# 特徵點 LLM Wiki ＋ 教學 HTML 簡報

課程作業：先以「先討論、後生成」建立 LLM Wiki，再只用 Wiki 當知識來源產生教學簡報。

- Wiki 規則：`AGENTS.md`（任何 AI 修改本 repo 前必讀）
- 來源清單：`raw/sources.md`（付費論文 PDF 只留本機，已列入 `.gitignore`）
- 網站內容：`docs/`（MkDocs Material，push 到 main 後由 GitHub Actions 部署到 GitHub Pages）

## 本機檢查

```bash
pip install mkdocs-material beautifulsoup4 playwright && playwright install chromium
python tools/lint.py            # Wiki Lint
python tools/check_slides.py    # 簡報事實回溯
python tools/check_render.py    # 簡報渲染（4 種螢幕）
mkdocs serve                    # 本機預覽
```
