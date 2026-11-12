---
title: SuperPoint
type: concept
sources: [S4, S5]
related: [self-supervised-learning, homography, sift, orb, feature-detection, feature-description, metric-choice-pitfall]
updated: 2026-11-12
---
# SuperPoint

## 一句話定義
2018 年提出、用一個神經網路同時輸出特徵點位置與描述子的方法，以自監督方式訓練。[S4]

## 直覺解釋
SIFT、ORB 的每個步驟都是人設計的規則；SuperPoint 則讓卷積神經網路從資料中學會「哪裡是好的點、怎麼描述它」。[S4] 卷積神經網路在幾乎所有以影像為輸入的任務上都勝過人工設計的表示。[S4]

> 💡 白話詮釋（非來源原文）：卷積神經網路（CNN）是一種很擅長處理影像的深度學習模型，由很多層小濾波器堆疊而成，能自己學出要看哪些圖案。

## 重點

**訓練三階段** [S4]
1. **MagicPoint**：在合成資料集 Synthetic Shapes（三角形、四邊形、線段、橢圓等，角點位置毫無歧義）上訓練偵測器。[S4]
2. **Homographic Adaptation**：把沒有標註的真實照片（MS-COCO）用隨機[單應性](homography.md)扭曲很多次，各自偵測後轉回原圖再平均，得到偽標籤。[S4]
3. **聯合訓練**：用扭曲前後的影像對，同時訓練偵測與描述。[S4]

$$\hat{F}(I; f_\theta) = \frac{1}{N_h}\sum_{i=1}^{N_h} \mathcal{H}_i^{-1}\, f_\theta\big(\mathcal{H}_i(I)\big)$$

| 符號 | 白話意思 |
|---|---|
| \(f_\theta\) | 原本的偵測器 [S4] |
| \(\mathcal{H}_i(I)\) | 用第 i 個隨機單應性扭曲影像 I [S4] |
| \(\mathcal{H}_i^{-1}\) | 把偵測結果轉回原圖座標 [S4] |
| \(N_h\) | 扭曲的次數 [S4] |

- 做 100 次比完全不做，[重複率](metric-choice-pitfall.md)提升 21%；做到 1000 次只提升 22%，超過 100 次效益很小。[S4]

> 💡 白話詮釋（非來源原文）：一個點如果不管照片怎麼歪、怎麼縮放都被找到，平均後分數就高；只在某個角度偶然被找到的點，平均後就被淡化。

**架構** [S4]
- 一個共用的 encoder 先縮小影像，接著分成兩個 head：偵測 head 和描述 head；大部分參數由兩個任務共用。[S4]
- 影像被切成 8×8 像素的格子（cell）；偵測 head 對每格輸出 65 個值：64 個代表格內每個位置、1 個代表「這格沒有點」（dustbin）。[S4]
- 描述 head 每 8 像素輸出一個 256 維描述子，再插值到需要的位置並正規化成長度 1。[S4]
- 一次前向運算同時輸出點與描述子；在 Titan X GPU 上處理 480×640 影像約 13 ms（約 70 FPS）。[S4]

> 💡 白話詮釋（非來源原文）：encoder 是負責「看懂影像、抽出特徵」的前半段網路；head 是接在後面、各自負責一項工作的小網路。「前向運算」就是把影像丟進網路算一次。「插值」是由已知格點的值推算中間位置的值。GPU 是擅長大量平行計算的顯示卡晶片，神經網路通常靠它加速。FPS 是每秒能處理幾張畫面。

**實驗結果**（HPatches 資料集，單應性估計正確率，ε 為容許誤差像素）[S4]

| 方法 [S4] | ε = 1 | ε = 3 | ε = 5 |
|---|---|---|---|
| SuperPoint | .310 | .684 | .829 |
| SIFT | .424 | .676 | .759 |
| LIFT | .284 | .598 | .717 |
| ORB | .150 | .395 | .538 |

- SuperPoint 勝過 LIFT 與 ORB，和 SIFT 相當；在光照變化下特別有效。[S4]
- SIFT 在最嚴格的 ε = 1 表現最好，作者認為是因為 SIFT 多做了次像素定位。[S4]
- 在合成圖形加雜訊時，MagicPoint 的 mAP 仍有 0.971，Harris 只剩 0.213、FAST 只剩 0.061。[S4]

> 💡 白話詮釋（非來源原文）：HPatches 是常用的公開測試資料集，有光照變化與視角變化兩類場景。mAP 是 0 到 1 的偵測準確度綜合分數，越高越好。LIFT 是另一個早期的深度學習特徵方法。

## 限制／常見誤解
- 遇到訓練時沒看過的極端平面內旋轉會失敗；SIFT、ORB 是刻意設計旋轉不變，SuperPoint 的能力則取決於訓練資料。[S4]
- 需要 GPU 才能達到論文中的即時速度。[S4]
- MagicPoint 抗雜訊的結果只在合成圖形上測得。[S4]
- 後來的 [LiftFeat](liftfeat.md) 沿用了 SuperPoint 的 65 通道關鍵點 head；在 LiftFeat 的比較中，LiftFeat 在行動 GPU 上比 SuperPoint 快約 4.9 倍（36 → 7.4 ms）。[S5]

## 相關頁面
[自監督學習](self-supervised-learning.md)・[單應性](homography.md)・[SIFT](sift.md)・[ORB](orb.md)・[特徵偵測](feature-detection.md)・[特徵描述](feature-description.md)・[指標選擇的陷阱](metric-choice-pitfall.md)・[LiftFeat](liftfeat.md)
