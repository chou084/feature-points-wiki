---
title: S1 OpenCV〈Understanding Features〉
type: source
sources: [S1]
related: [feature-point, corner, feature-detection, feature-description]
updated: 2026-11-12
---
# S1 OpenCV〈Understanding Features〉

## 基本資訊
- 類型：官方教學文件（入門）
- 連結：<https://docs.opencv.org/4.x/df/d54/tutorial_py_features_meaning.html>

## 這篇在講什麼
用拼圖遊戲當例子，直覺說明什麼是「特徵」、為什麼角點是好特徵，以及「偵測」和「描述」的分別。全篇沒有公式。[S1]

## 重點
- 影像拼接、3D 重建等應用，都建立在「在不同影像中找到同一處」這個基本能力上。[S1]
- 好特徵要獨特、易追蹤、易比較。[S1]
- 用小窗格移動來判斷：平坦區怎麼移都一樣、邊緣只有垂直於邊緣移動才變、角點往哪移都變。[S1]
- 找出特徵位置叫偵測；把特徵周圍區域描述成可比對的形式叫描述。[S1]

## 影響了哪些概念頁
[特徵點](../concepts/feature-point.md)、[角點](../concepts/corner.md)、[特徵偵測](../concepts/feature-detection.md)、[特徵描述](../concepts/feature-description.md)

## 我的疑問
- 文中只提到「之後會匹配特徵」，沒有說明怎麼匹配 → 列為待建，等 S2、S6 補。
- 沒有角點的數學定義 → 由 S7 補上。
