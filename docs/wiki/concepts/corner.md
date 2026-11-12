---
title: 角點（Corner）
type: concept
sources: [S1, S7]
related: [feature-point, harris-corner, feature-detection]
updated: 2026-11-12
---
# 角點（Corner）

## 一句話定義
往任何方向稍微移動，周圍外觀都會明顯改變的位置。[S1]

## 直覺解釋
想像拿一個小窗格蓋在影像上，然後把窗格往各個方向推一點點，看窗格裡的內容變了多少：[S1]

| 區域 | 窗格移動後 | 能不能精確定位 |
|---|---|---|
| 平坦區 | 往哪移都一樣 | 不能 [S1] |
| 邊緣 | 只有垂直於邊緣移動才變，沿邊緣移動不變 | 只能定出大概位置 [S1] |
| 角點 | 往哪移都變 | 能，所以是好特徵 [S1] |

## 重點
- 邊緣比平坦區好，但還不夠當好特徵。[S1]
- 「各方向變化都大」的直覺，可以用 [Harris 角點偵測](harris-corner.md) 寫成數學。[S7]

## 限制／常見誤解
- 角點不是唯一的好特徵，有時 blob 也是。[S1]

## 相關頁面
[特徵點](feature-point.md)・[Harris 角點偵測](harris-corner.md)・[特徵偵測](feature-detection.md)
