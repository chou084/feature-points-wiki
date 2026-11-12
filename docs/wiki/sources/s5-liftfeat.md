---
title: S5 Liu et al. (2025) LiftFeat
type: source
sources: [S5]
related: [liftfeat, surface-normal, superpoint]
updated: 2026-11-12
---
# S5 Liu et al. (2025)〈LiftFeat: 3D Geometry-Aware Local Feature Matching〉

## 基本資訊
- 類型：會議論文（ICRA 2025）
- 連結：<https://arxiv.org/abs/2505.03422>；程式碼：<https://github.com/lyp-deeplearning/LiftFeat>

## 這篇在講什麼
在輕量的特徵網路中加入「表面法向量」這個 3D 幾何資訊，讓描述子在光照劇變、低紋理、重複圖案等極端場景下更好分辨。[S5]

## 重點
- 法向量的訓練標籤由 Depth Anything v2 預測的深度圖推算，不需額外人工標註。[S5]
- 3D-GFL 模組把 2D 描述子與法向量特徵融合成「升級版」描述子。[S5]
- 在相對姿態估計、單應性估計、視覺定位三個任務上，勝過 ORB、SuperPoint、ALIKE、SiLK、XFeat 等輕量方法。[S5]

## 影響了哪些概念頁
[LiftFeat](../concepts/liftfeat.md)、[表面法向量](../concepts/surface-normal.md)、[SuperPoint](../concepts/superpoint.md)、[特徵匹配](../concepts/feature-matching.md)

## 刻意不收錄的部分（與使用者討論決定）
self-attention 公式與三種損失函數的公式。

## 我的疑問／論文內部不一致
> ⚠ 待確認：內文說夜間在 (0.25m/1°) 門檻下由 77.6% 提升到 82.4%，但表 III 的門檻是 (0.25m, 2°)、LiftFeat 數值為 82.1。Wiki 一律採用表格數值。

> ⚠ 待確認：內文說比 SuperPoint 快 5 倍；依表 V，GPU 上 36 → 7.4 ms（約 4.9 倍）成立，CPU 上 227 → 62 ms 只約 3.7 倍。
