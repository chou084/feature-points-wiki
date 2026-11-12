---
title: 自監督學習（Self-Supervised Learning）
type: concept
sources: [S4]
related: [superpoint, homography]
updated: 2026-11-12
---
# 自監督學習（Self-Supervised Learning）

## 一句話定義
不靠人工標註，而是由系統自己產生訓練用的標籤（偽標籤）來訓練模型。[S4]

## 直覺解釋
要訓練神經網路找特徵點，最直接是請人標註；但「什麼是興趣點」沒有明確定義，不像嘴角、腳踝那樣能讓人一致地標。[S4] 所以 SuperPoint 讓偵測器自己替真實照片產生標籤。[S4]

> 💡 白話詮釋（非來源原文）：「偽標籤」就是機器自己猜、再當成標準答案拿來練習的標籤；它不保證完全正確，但數量可以很大，又不用花人力。

## 重點
- 第一步先在答案明確的合成圖形上訓練，得到基礎偵測器。[S4]
- 第二步用 [Homographic Adaptation](superpoint.md) 在沒有標註的真實照片上產生偽標籤。[S4]
- 這個過程可以重複，用改良後的偵測器再產生更好的偽標籤。[S4]

## 限制／常見誤解
- 合成圖形只涵蓋真實世界興趣點的一小部分；只在合成資料上訓練的 MagicPoint，在真實照片的視角變化下重複率反而不如傳統偵測器。[S4]

## 相關頁面
[SuperPoint](superpoint.md)・[單應性](homography.md)
