---
title: 特徵偵測（Feature Detection）
type: concept
sources: [S1, S7, S2, S4]
related: [feature-point, corner, harris-corner, feature-description]
updated: 2026-11-12
---
# 特徵偵測（Feature Detection）

## 一句話定義
在影像中找出特徵點「在哪裡」的步驟。[S1]

## 直覺解釋
尋找那些「稍微移動一下，外觀就變化最大」的區域。[S1]

## 重點
- 偵測只回答「位置」，不回答「長什麼樣」；後者是[特徵描述](feature-description.md)的工作。[S1]
- 經典做法之一是 [Harris 角點偵測](harris-corner.md)，用分數 R 判斷每個位置是不是角點。[S7]
- [SIFT](sift.md) 則在[尺度空間](scale-space.md)中找極值，使偵測結果對縮放不變。[S2]
- [SuperPoint](superpoint.md) 改用神經網路從資料中學習偵測，以自監督方式取得訓練標籤。[S4]

## 限制／常見誤解
- 只在單一尺度偵測（如 Harris）的方法，影像縮放後容易找不到同一個點。[S2]

## 相關頁面
[特徵點](feature-point.md)・[角點](corner.md)・[Harris 角點偵測](harris-corner.md)・[SIFT](sift.md)・[尺度空間](scale-space.md)・[特徵描述](feature-description.md)
