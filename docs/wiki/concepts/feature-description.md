---
title: 特徵描述（Feature Description）
type: concept
sources: [S1, S2, S3, S4]
related: [feature-point, feature-detection]
updated: 2026-11-12
---
# 特徵描述（Feature Description）

## 一句話定義
把特徵點周圍的區域記錄成可以拿來比對的形式，讓電腦能在別張影像中找到同一處。[S1]

## 直覺解釋
人在描述一個地方時會說「上面是藍天、下面是大樓、大樓上有玻璃」，再拿這段描述去別張照片找。電腦也需要對特徵周圍的區域做類似的描述。[S1]

## 重點
- 偵測找到位置之後，才進行描述。[S1]
- 有了位置和描述，就能在多張影像中找到同一個特徵，進而對齊、拼接影像。[S1]
- 例：[SIFT](sift.md) 的描述子是一個 128 維向量，統計關鍵點周圍各小區塊的梯度方向。[S2]
- 例：[ORB](orb.md) 的描述子是 256 位元的 0/1 字串，每一位元來自一次「兩點比亮度」，見[二元描述子](binary-descriptor.md)。[S3]
- 例：[SuperPoint](superpoint.md) 的描述子由神經網路學出，是長度正規化為 1 的 256 維向量。[S4]

## 限制／常見誤解
- 最直接的做法是拿周圍像素直接比相似度，但這對視角變化、變形非常敏感，所以好的描述子需要容忍小幅位移。[S2]

## 相關頁面
[特徵點](feature-point.md)・[特徵偵測](feature-detection.md)・[特徵匹配](feature-matching.md)
