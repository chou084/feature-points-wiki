# 特徵點 LLM Wiki

## 1. 主題與簡介

**特徵點偵測與描述入門：電腦怎麼在兩張照片裡找到「同一個點」？**

從 1988 年的 Harris 角點，到 SIFT、ORB 這些人工設計的方法，再到 SuperPoint、LiftFeat 這些從資料學習的方法。這個 Wiki 由 6 篇來源（2 篇 OpenCV 教學＋4 篇論文）以「先討論、後生成」的方式建立，每句事實都標有來源 ID，並由 AI 依 `AGENTS.md` 的規則維護。

## 繳交內容

| 項目 | 連結 |
|---|---|
| 1. 主題與簡介 | 本頁 |
| 2. LLM Wiki 成果 | [Wiki 目錄](wiki/index.md)（23 頁：6 來源頁、17 概念頁）・[操作紀錄](wiki/log.md) |
| 3. 教學 HTML 簡報 | [開啟簡報](slides/index.html)（20 張；鍵盤 ← → 或滑動切換） |
| 4. Loop / Graph | [流程圖與說明](workflow.md) |
| 5. 實際執行與檢查紀錄 | [執行與檢查紀錄](run-log.md)（48 列） |
| 6. 反思 | [反思](reflection.md) |

## 檢查工具

| 腳本 | 用途 |
|---|---|
| `tools/lint.py` | Wiki Lint：來源標記、連結、孤兒頁、frontmatter |
| `tools/check_slides.py` | 事實回溯：投影片上每個數字與來源都要能在 Wiki 找到 |
| `tools/check_render.py` | 渲染：溢出、公式、4 種螢幕尺寸 |
