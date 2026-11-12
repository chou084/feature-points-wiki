---
title: S4 DeTone et al. (2018) SuperPoint
type: source
sources: [S4]
related: [superpoint, homography, self-supervised-learning, metric-choice-pitfall]
updated: 2026-11-12
---
# S4 DeTone et al. (2018)〈SuperPoint: Self-Supervised Interest Point Detection and Description〉

## 基本資訊
- 類型：會議論文（CVPR Workshop 2018），含附錄
- 連結：<https://arxiv.org/abs/1712.07629>

## 這篇在講什麼
用一個神經網路同時做特徵點偵測與描述，並以「自監督」方式解決「興趣點沒有人工標註」的問題。[S4]

## 重點
- 三階段：合成資料訓練 MagicPoint → Homographic Adaptation 產生真實照片的偽標籤 → 聯合訓練偵測與描述。[S4]
- 共用 encoder＋兩個 head，一次前向運算同時輸出點與描述子；GPU 上約 70 FPS。[S4]
- 單應性估計與 SIFT 相當，勝過 LIFT 與 ORB；極端平面內旋轉會失敗。[S4]

## 影響了哪些概念頁
[SuperPoint](../concepts/superpoint.md)、[單應性](../concepts/homography.md)、[自監督學習](../concepts/self-supervised-learning.md)、[指標選擇的陷阱](../concepts/metric-choice-pitfall.md)、[ORB](../concepts/orb.md)、[SIFT](../concepts/sift.md)、[特徵偵測](../concepts/feature-detection.md)、[特徵描述](../concepts/feature-description.md)

## 刻意不收錄的部分（與使用者討論決定）
損失函數公式（cross-entropy、hinge loss）與訓練超參數。

## 我的疑問
- 比較 SIFT、ORB 時用 OpenCV 預設參數，有沒有調參可能影響結果，原文未討論。
