---
title: ORB（Oriented FAST and Rotated BRIEF）
type: concept
sources: [S3, S2, S4]
related: [binary-descriptor, harris-corner, sift, feature-matching, scale-space, noise-robustness-conflict]
updated: 2026-11-12
---
# ORB（Oriented FAST and Rotated BRIEF）

## 一句話定義
2011 年提出的快速特徵偵測＋描述方法，由「加上方向的 FAST」和「能處理旋轉的 BRIEF」組成，目標是效果接近 SIFT 但快很多。[S3]

## 直覺解釋
[SIFT](sift.md) 很準但很慢，手機等低功耗裝置跑不動。[S3] ORB 改用兩個本來就很快的零件（FAST 偵測、BRIEF 描述），再補上它們缺少的「方向」能力。[S3]

## 重點

**偵測：oFAST** [S3]
- FAST 只比較中心像素與周圍一圈像素的亮度差，因此很快；ORB 用的是半徑 9 的 FAST-9。[S3]
- FAST 沒有「多像角點」的分數，而且在邊緣上反應也很大，所以 ORB 先多抓一些點，再用 [Harris](harris-corner.md) 分數排序，只留前 N 個。[S3]
- FAST 本身不處理尺度，所以在影像金字塔的每一層各做一次（論文用 5 層、每層縮小 √2 倍）。[S3]

**方向：強度質心（intensity centroid）** [S3]

$$m_{pq} = \sum_{x,y} x^p y^q I(x,y),\qquad C = \left(\frac{m_{10}}{m_{00}},\, \frac{m_{01}}{m_{00}}\right),\qquad \theta = \operatorname{atan2}(m_{01},\, m_{10})$$

- 從角點中心 O 指向質心 C 的向量方向，就是這個特徵的方向 θ。[S3]
- 計算範圍限制在半徑 r 的圓形區域內，以提升旋轉不變性。[S3]
- 和兩種梯度式方法（其中一種類似 SIFT 的方向直方圖）相比，質心法在雜訊下估出的方向最準。[S3]
- SIFT 一個點可能有多個方向，質心法只給一個主方向。[S3]

> 💡 白話詮釋（非來源原文）：把區塊裡每個像素的亮度當成「重量」，質心 C 就是這塊區域的重心。角點通常一邊亮一邊暗，所以重心會偏向亮的那一側，指向重心的箭頭就成了這個點的「方向」。atan2 只是「由座標算角度」的函數。

**描述：rBRIEF** [S3]
- 先把 BRIEF 的比較點對依 θ 旋轉（steered BRIEF），角度以 12 度為一格預先建表，以節省計算。[S3]
- 但旋轉後各位元變得比較好預測、彼此也更相關，鑑別力下降。[S3]
- 因此從 205,590 組候選比較中，挑出 256 組「平均值接近 0.5（最難預測）」且「彼此相關性低（不重複）」的比較，稱為 rBRIEF（詳見[二元描述子](binary-descriptor.md)）。[S3]

**實驗結果** [S3]

| 每張 640×480 影像的時間 | ORB | SURF | SIFT |
|---|---|---|---|
| 毫秒 [S3] | 15.3 | 217.3 | 5228.7 |

- SURF 是另一個為了降低計算量而提出的 SIFT 替代方法，S3 認為它是當時這類方法中最好的。[S3]
- ORB 比 SURF 快一個數量級，比 SIFT 快超過兩個數量級。[S3]

> 💡 白話詮釋（非來源原文）：「快一個數量級」約等於快 10 倍，「兩個數量級」約等於快 100 倍。
- 在人工旋轉＋雜訊的測試中，ORB 正確配對比例超過 70%，表現最好。[S3]
- 真實影像：戶外場景 ORB 最好（45.8%，SIFT 30.2%）；室內雜誌場景三者差不多。[S3]
- 在 1 GHz ARM 處理器的手機上，能以每秒 7 張處理 640×480 影像。[S3]

## 限制／常見誤解
- 作者自己承認尺度不變性沒有充分處理：只用金字塔，沒有為每個點估計尺度。[S3]
- 在 S4 的 HPatches 實驗中，ORB 重複率最高，但點容易擠在一起，單應性估計反而最差，見[指標選擇的陷阱](metric-choice-pitfall.md)。[S4]
- 「ORB 比 SIFT 抗雜訊」需要看實驗條件，與 S2 的說法有落差，見[雜訊穩健性的衝突](noise-robustness-conflict.md)。[S2][S3]

## 相關頁面
[二元描述子](binary-descriptor.md)・[Harris 角點偵測](harris-corner.md)・[SIFT](sift.md)・[特徵匹配](feature-matching.md)・[尺度空間](scale-space.md)・[雜訊穩健性的衝突](noise-robustness-conflict.md)・[指標選擇的陷阱](metric-choice-pitfall.md)・[SuperPoint](superpoint.md)
