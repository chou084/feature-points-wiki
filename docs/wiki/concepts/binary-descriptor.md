---
title: 二元描述子（BRIEF 與 Hamming 距離）
type: concept
sources: [S3]
related: [orb, feature-description, feature-matching, sift]
updated: 2026-11-12
---
# 二元描述子（BRIEF 與 Hamming 距離）

## 一句話定義
用一連串「兩個像素誰比較亮」的比較結果（0 或 1）組成的描述子，BRIEF 是代表。[S3]

## 直覺解釋
[SIFT](sift.md) 的描述子是 128 個數字，二元描述子則只是一串 0 和 1：在平滑過的區塊裡挑兩個點比亮度，前者較暗記 1，否則記 0，重複很多次。[S3]

## 重點

**二元測試** [S3]

$$\tau(\mathbf{p};\mathbf{x},\mathbf{y}) = \begin{cases}1 & \mathbf{p}(\mathbf{x}) < \mathbf{p}(\mathbf{y})\\ 0 & \mathbf{p}(\mathbf{x}) \ge \mathbf{p}(\mathbf{y})\end{cases},\qquad f_n(\mathbf{p}) = \sum_{i=1}^{n} 2^{\,i-1}\,\tau(\mathbf{p};\mathbf{x}_i,\mathbf{y}_i)$$

- \(\mathbf{p}(\mathbf{x})\)：平滑後的區塊 p 在點 x 的亮度；ORB 取 n = 256，即 256 位元。[S3]
- 比較前一定要先平滑影像；ORB 的做法是讓每個比較點其實是 31×31 區塊中的一個 5×5 小窗。[S3]
- BRIEF 在光照、模糊、透視變形上的表現和 SIFT 相近，但對平面內旋轉非常敏感，旋轉超過約 10 度效果就大幅下降。[S3]

> 💡 白話詮釋（非來源原文）：\(f_n\) 的公式只是把 256 個 0/1 依序排成一個二進位數字。「平面內旋轉」指相機繞著鏡頭軸轉，就像把照片在桌上轉個角度。

**Hamming 距離** [S3]
- 二元描述子之間用 Hamming 距離比較，也就是兩串位元中「有幾位不同」。[S3]

> 💡 白話詮釋（非來源原文）：例如 1011 和 1001 只有第 3 位不同，Hamming 距離就是 1。電腦算這種距離非常快。

**好的二元測試要「難預測」又「不重複」** [S3]
- 每個位元的平均值接近 0.5 時變異數最大、鑑別力最好；各測試彼此不相關時，每一個測試才都有貢獻。[S3]

> 💡 白話詮釋（非來源原文）：如果某個比較幾乎永遠回答 1，它就像一個永遠答「是」的問題，問了等於沒問；兩個比較若總是給相同答案，其中一個就是多餘的。

## 限制／常見誤解
- 原始 BRIEF 沒有方向，ORB 的 rBRIEF 才補上旋轉能力，見 [ORB](orb.md)。[S3]

## 相關頁面
[ORB](orb.md)・[特徵描述](feature-description.md)・[特徵匹配](feature-matching.md)・[SIFT](sift.md)
