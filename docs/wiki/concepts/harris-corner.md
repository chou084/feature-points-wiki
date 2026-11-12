---
title: Harris 角點偵測（Harris Corner Detector）
type: concept
sources: [S7, S2, S3]
related: [corner, feature-detection, sift, orb]
updated: 2026-11-12
---
# Harris 角點偵測（Harris Corner Detector）

## 一句話定義
把「角點往各方向移動都變化大」寫成數學分數 R，用來判斷每個位置是不是角點的方法；1988 年由 Harris 與 Stephens 提出。[S7]

## 直覺解釋
延續[角點](corner.md)頁的小窗格實驗：把窗格移動 (u, v)，計算移動前後亮度差了多少。各方向都差很多的地方就是角點。[S7]

## 重點

**第 1 步：變化量** [S7]

$$E(u,v) = \sum_{x,y} w(x,y)\,\big[I(x+u,\,y+v) - I(x,y)\big]^2$$

| 符號 | 白話意思 |
|---|---|
| \(I(x,y)\) | 位置 (x,y) 的亮度 [S7] |
| \(I(x+u,y+v)\) | 窗格移動 (u,v) 後的亮度 [S7] |
| \(w(x,y)\) | 窗格函數，決定每個像素的權重；可用矩形或高斯 [S7] |

**第 2 步：近似成矩陣形式**（用泰勒展開，推導原文略過）[S7]

> 💡 白話詮釋（非來源原文）：泰勒展開是把複雜函數用簡單多項式「近似」的數學工具。這裡用它的目的，是把難算的 E(u,v) 變成只看一個 2×2 矩陣 M 就能判斷。

$$E(u,v) \approx \begin{bmatrix}u & v\end{bmatrix} M \begin{bmatrix}u\\ v\end{bmatrix},\qquad M = \sum_{x,y} w(x,y)\begin{bmatrix}I_x I_x & I_x I_y\\ I_x I_y & I_y I_y\end{bmatrix}$$

- \(I_x\)、\(I_y\)：影像亮度在 x、y 方向的導數，也就是亮度沿水平、垂直方向的變化，可用 `cv.Sobel()` 算出。[S7]

**第 3 步：看 M 的兩個特徵值 \(\lambda_1, \lambda_2\)** [S7]

| 情況 | 判斷 |
|---|---|
| 兩個都小 | 平坦區 [S7] |
| 一個遠大於另一個 | 邊緣 [S7] |
| 兩個都大且差不多 | 角點 [S7] |

> 💡 白話詮釋（非來源原文）：\(\lambda_1, \lambda_2\) 可以想成窗格往「最容易變化」和「最不容易變化」兩個方向移動時，變化各有多大。兩個都大，就代表「怎麼移都會變」。

**第 4 步：分數 R** [S7]

$$R = \det(M) - k\,\big(\operatorname{trace}(M)\big)^2,\qquad \det(M)=\lambda_1\lambda_2,\quad \operatorname{trace}(M)=\lambda_1+\lambda_2$$

> 💡 白話詮釋（非來源原文）：det（行列式）在這裡等於兩個特徵值相乘，trace（跡）等於兩個特徵值相加，所以不必真的解出特徵值，就能用 R 判斷「兩個是否都大」。k 是一個可調的小常數。

- \(|R|\) 小 → 平坦；\(R<0\) → 邊緣；\(R\) 大 → 角點。[S7]
- 對每個位置算出 R 後設門檻，超過的就是角點。[S7]

**後來的用途** [S3]
- [ORB](orb.md) 用 Harris 分數替 FAST 找到的點排序，只保留最像角點的前 N 個。[S3]

**OpenCV 用法** [S7]

```python
dst = cv.cornerHarris(gray, 2, 3, 0.04)   # blockSize=2, ksize=3, k=0.04
img[dst > 0.01 * dst.max()] = [0, 0, 255] # R 超過最大值 1% 的標成紅色
```

- 輸入要是灰階、float32 的影像。[S7]
- 需要更精確的位置時，可再用 `cv.cornerSubPix()` 做次像素精修。[S7]

> 💡 白話詮釋（非來源原文）：「次像素」指比一個像素還細的位置，例如 (10.3, 25.7)，而不只是整數格子 (10, 26)。

## 限制／常見誤解
- 對影像縮放非常敏感，不適合匹配大小不同的影像；這是 [SIFT](sift.md) 被提出的動機。[S2]
- 名稱叫「角點」偵測器，但實際選出的是「在某個預設尺度下、各方向梯度都大」的位置，不一定是真正的角。[S2]

## 相關頁面
[角點](corner.md)・[特徵偵測](feature-detection.md)・[SIFT](sift.md)・[ORB](orb.md)
