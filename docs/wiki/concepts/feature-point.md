---
title: 特徵點（Feature Point）
type: concept
sources: [S1]
related: [corner, feature-detection, feature-description]
updated: 2026-11-12
---
# 特徵點（Feature Point）

## 一句話定義
影像中外觀獨特、能在別張影像裡被重新找到的位置。[S1]

## 直覺解釋
玩拼圖時，我們會找有特色的圖案去對照拼片該放哪裡。電腦想把多張照片拼成全景、或從多張照片重建 3D 模型，也需要同樣的能力：在不同照片中認出「同一個地方」。[S1]

## 重點
- 好特徵的三個條件：獨特、容易追蹤、容易比較。[S1]
- 人類憑直覺就能指出好特徵，難處在於把這種直覺變成電腦能執行的規則。[S1]
- 角點通常是好特徵；有些情況下 blob（斑點狀的區域）也算。[S1]
- 使用特徵分兩步：先[偵測](feature-detection.md)出位置，再[描述](feature-description.md)它的樣子。[S1]

## 限制／常見誤解
- 不是每個位置都適合當特徵點：平坦區和邊緣都無法精確定位。[S1]

## 相關頁面
[角點](corner.md)・[特徵偵測](feature-detection.md)・[特徵描述](feature-description.md)
