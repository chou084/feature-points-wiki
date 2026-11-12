---
title: S2 Lowe (2004) SIFT
type: source
sources: [S2]
related: [sift, scale-space, feature-matching, harris-corner, feature-description]
updated: 2026-11-12
---
# S2 Lowe (2004)〈Distinctive Image Features from Scale-Invariant Keypoints〉

## 基本資訊
- 類型：期刊論文（IJCV 60(2), 2004），28 頁
- 連結：<https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf>

## 這篇在講什麼
提出 SIFT：一種對影像縮放、旋轉不變，並對光照與視角變化有一定容忍度的特徵偵測與描述方法，並示範用它做物體辨識。[S2]

## 重點
- Harris 角點偵測器對影像縮放非常敏感，所以需要能在所有尺度上找特徵的方法。[S2]
- SIFT 分四步：尺度空間極值偵測、關鍵點定位、方向指定、關鍵點描述子。[S2]
- 描述子是 4×4 區塊 × 8 方向 = 128 維向量。[S2]
- 匹配用最近鄰＋比值檢驗（d₁/d₂ > 0.8 就丟掉）。[S2]

## 影響了哪些概念頁
[SIFT](../concepts/sift.md)、[尺度空間](../concepts/scale-space.md)、[特徵匹配](../concepts/feature-matching.md)、[Harris 角點偵測](../concepts/harris-corner.md)、[特徵描述](../concepts/feature-description.md)、[特徵偵測](../concepts/feature-detection.md)

## 刻意不收錄的部分（與使用者討論決定）
論文第 7 節之後的物體辨識流程（Hough 投票分群、Best-Bin-First 近似搜尋、仿射參數最小平方求解）對「特徵點入門」太深，不建概念頁、不進簡報。

## 我的疑問
- 論文的參數（σ=1.6、門檻 0.03、r=10、0.8）都是作者實驗選的，換資料集是否仍適用？原文未討論。
