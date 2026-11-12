# 操作紀錄

只能往下追加。格式：`## [日期] 操作 | 對象`

## [2026-11-12] setup | 建立 repo 骨架與 AGENTS.md
- 確定主題：特徵點偵測與描述入門
- 確定來源清單 S1–S6（使用者挑選）

## [2026-11-12] ingest | S1 OpenCV〈Understanding Features〉
- 先討論：提出 5 個重點與頁面計畫；使用者確認，並決定「匹配」先列待建，由 S2、S6 補
- 新建：sources/s1-opencv-features、concepts/feature-point、corner、feature-detection、feature-description

## [2026-11-12] schema 修改 | 新增來源 S7、新增「💡 白話詮釋」規則
- 原因：使用者要求簡報講公式，但 S1 沒有公式 → 依規則不能自行補，改為新增來源 S7
- 使用者同意：來源沒寫的白話比喻可以加，但必須標成「💡 白話詮釋（非來源原文）」

## [2026-11-12] ingest | S7 OpenCV〈Harris Corner Detection〉
- 先讀搜尋摘要討論，寫入前再完整讀一次全文核對公式（det=λ₁λ₂、trace=λ₁+λ₂、三種 R 判斷）
- 新建：sources/s7-opencv-harris、concepts/harris-corner；更新 corner、feature-detection

## [2026-11-12] lint #1
- 自動檢查（tools/lint.py）：0 個問題
- 驗證 lint 本身：故意放入錯誤頁，5 類錯誤全部被抓到，刪除後恢復 0
- 人工檢查 (e) 術語白話解釋：3 個問題（泰勒展開、det/trace、次像素未解釋）→ 已補 💡 白話詮釋
- 人工檢查 (b) 來源矛盾：S1 與 S7 對平坦／邊緣／角點的描述一致，無矛盾

## [2026-11-12] ingest | S2 Lowe (2004) SIFT
- 先討論：7 個重點、頁面計畫、新術語清單（流程修改 #1 首次實施）
- 使用者決定：物體辨識部分（Hough、BBF、仿射求解）不收錄；簡報只放 DoG 公式與比值檢驗；blob 從待建移除
- 新建：sources/s2-sift、concepts/sift、scale-space、feature-matching
- 更新：harris-corner（解除 ⚠，補縮放敏感）、feature-detection、feature-description

## [2026-11-12] lint #2
- 自動：0 個問題
- 人工術語：2 個問題（主曲率、Laplacian of Gaussian）→ 補 💡；討論時列的術語清單漏掉這兩個
- 人工矛盾：S2 對 Harris 的描述與 S7 一致

## [2026-11-12] ingest | S3 Rublee et al. (2011) ORB
- 取得：原論文 3 個線上來源都失敗 → 使用者從 IEEE Xplore 下載上傳；PDF 文字抽取弄亂公式 → 以頁面影像核對
- 先討論：8 個重點、術語清單，並在討論階段就發現 S2 與 S3 對 SIFT 抗雜訊的結論衝突
- 使用者決定：LSH 與 rBRIEF 演算法細節不收錄；簡報放二元測試 τ 與質心方向 θ；雜訊衝突做成一張「為什麼要看實驗條件」的投影片
- 新建：sources/s3-orb、concepts/orb、binary-descriptor、noise-robustness-conflict
- 更新：feature-matching（距離依描述子而定）、harris-corner、sift、feature-description、scale-space
- 版權：PDF 加入 .gitignore，不放進公開 repo

## [2026-11-12] lint #3
- 自動：第 1 次 5 個問題 → 3 個真錯誤（方法論句子無來源、表格資料列漏標、限制段落的推論句）＋ 2 個誤報（表頭列、導覽句）
- 修 lint：表頭列不檢查；另以刻意移除標記驗證修改後仍能抓到表格資料列
- 修正時一次替換字串沒對準原文，腳本的事前檢查擋下，未寫壞檔案，重做後通過
- 人工術語：3 個問題（數量級、SURF、暴力匹配）→ 補上；都出現在「實驗結果」段落

## [2026-11-12] ingest | S4 DeTone et al. (2018) SuperPoint
- 先討論：6 個重點、交叉檢查（ORB 重複率 vs 單應性估計、旋轉能力是設計 vs 學來、雜訊結果只在合成資料）；術語清單這次同時掃了「方法」與「實驗結果」段
- 使用者決定：架構只在 Wiki 簡記、簡報畫示意圖；損失函數不收；Homographic Adaptation 公式進簡報；「讀實驗的陷阱」拆成 2 張投影片
- 新建：sources/s4-superpoint、concepts/superpoint、homography、self-supervised-learning、metric-choice-pitfall
- 更新：orb、sift、feature-detection、feature-description、noise-robustness-conflict

## [2026-11-12] lint #4
- 自動：7 個問題，全部是「來源標在表頭、資料列被判無來源」→ 新增規則：整表同一來源可只標表頭（寫入 AGENTS.md 與 lint），並驗證表頭沒標時仍會抓
- 人工術語：2 個問題（插值、GPU）→ 補上；比 S2（2）、S3（3）持平或略少，且這次實驗段術語無漏網

## [2026-11-12] scope | 不納入 S6
- 使用者決定：已達 5 篇門檻，跳過綜述以節省時間

## [2026-11-12] ingest | S5 Liu et al. (2025) LiftFeat
- 先討論：8 個重點；交叉檢查發現論文內部 2 處不一致（夜間定位門檻與數值、「快 5 倍」只在 GPU 成立）
- 使用者決定：法向量公式進簡報；self-attention 與損失函數不收；不一致只記在 Wiki
- 新建：sources/s5-liftfeat、concepts/liftfeat、surface-normal；更新 feature-matching（MNN）、superpoint、homography

## [2026-11-12] lint #5
- 自動：0 個問題（第一次就通過）
- 人工術語：2 個問題（相對姿態估計、XFeat 等比較方法名）→ 補上；另修 1 處 ⚠ 區塊緊接清單的排版隱患
