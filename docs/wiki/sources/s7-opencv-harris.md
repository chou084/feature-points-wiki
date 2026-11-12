---
title: S7 OpenCV〈Harris Corner Detection〉
type: source
sources: [S7]
related: [harris-corner, corner, feature-detection]
updated: 2026-11-12
---
# S7 OpenCV〈Harris Corner Detection〉

## 基本資訊
- 類型：官方教學文件（接續 S1）
- 連結：<https://docs.opencv.org/4.12.0/dc/d0d/tutorial_py_features_harris.html>
- 加入原因：S1 沒有公式，但簡報需要講公式（2026-11-12 與使用者討論後決定）

## 這篇在講什麼
把 S1「角點往各方向移動都會變化」的直覺寫成數學，介紹 Harris 角點偵測器與 OpenCV 用法。[S7]

## 重點
- 方法由 Harris 與 Stephens 於 1988 年提出。[S7]
- 定義窗格移動 (u,v) 後的亮度變化量 E(u,v)，用泰勒展開近似成由矩陣 M 決定的二次式。[S7]
- M 的兩個特徵值決定區域是平坦、邊緣還是角點；實務上用分數 R = det(M) − k·trace(M)² 判斷。[S7]
- OpenCV 函式為 `cv.cornerHarris()`，對 R 設門檻即得角點；另有 `cv.cornerSubPix()` 可做次像素精修。[S7]
- 推導細節原文略過，請讀者參考教科書。[S7]

## 影響了哪些概念頁
[Harris 角點偵測](../concepts/harris-corner.md)、[角點](../concepts/corner.md)、[特徵偵測](../concepts/feature-detection.md)

## 我的疑問
- k 值範例用 0.04，原文沒說明為何選這個值。
- 原文沒有談 Harris 的缺點（例如對縮放是否穩定）→ 待 S2 補。
