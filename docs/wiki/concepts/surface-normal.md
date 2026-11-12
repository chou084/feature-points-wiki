---
title: 表面法向量（Surface Normal）
type: concept
sources: [S5]
related: [liftfeat]
updated: 2026-11-12
---
# 表面法向量（Surface Normal）

## 一句話定義
描述物體表面上某一點「朝向哪裡」的向量，是一種 3D 幾何資訊。[S5]

## 直覺解釋
深度圖記錄每個像素離相機多遠，但單張影像估出的深度有尺度模糊，不適合直接拿來匹配；法向量則同時具有平移不變與尺度不變的性質，比較適合。[S5]

> 💡 白話詮釋（非來源原文）：想像在牆面上插一根垂直於牆的牙籤，牙籤指的方向就是法向量。不管你站多遠看這面牆、牆被搬到哪裡，牙籤和牆的夾角都不變。「尺度模糊」是指只看一張照片，分不出是「小模型放很近」還是「大房子放很遠」。

## 重點

**從深度圖算出法向量** [S5]

$$\frac{\partial Z}{\partial u} \approx Z(u+1,v) - Z(u-1,v),\qquad \frac{\partial Z}{\partial v} \approx Z(u,v+1) - Z(u,v-1)$$

$$\mathbf{n} = \frac{\left(-\frac{\partial Z}{\partial u},\; -\frac{\partial Z}{\partial v},\; 1\right)}{\left\|\left(-\frac{\partial Z}{\partial u},\; -\frac{\partial Z}{\partial v},\; 1\right)\right\|}$$

- \(Z(u,v)\) 是像素 (u,v) 的深度；先用相鄰像素的深度差估計深度梯度，再組成向量並正規化成長度 1。[S5]
- LiftFeat 的深度圖由預訓練的單目深度估計模型 Depth Anything v2 產生，因此不需要額外的標註成本。[S5]

> 💡 白話詮釋（非來源原文）：「單目深度估計」是只用一張普通照片就猜出每個像素有多遠的模型。這裡和 [Harris](harris-corner.md) 的 \(I_x, I_y\) 很像，只是差分的對象從「亮度」換成了「深度」。

## 限制／常見誤解
- 法向量標籤是由模型預測的深度推算的偽標籤，品質取決於深度模型。[S5]

## 相關頁面
[LiftFeat](liftfeat.md)・[Harris 角點偵測](harris-corner.md)
