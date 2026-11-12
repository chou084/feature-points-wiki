---
title: S3 Rublee et al. (2011) ORB
type: source
sources: [S3]
related: [orb, binary-descriptor, feature-matching, harris-corner, noise-robustness-conflict]
updated: 2026-11-12
---
# S3 Rublee et al. (2011)〈ORB: an efficient alternative to SIFT or SURF〉

## 基本資訊
- 類型：會議論文（ICCV 2011, pp. 2564–2571），8 頁
- 連結：<https://doi.org/10.1109/ICCV.2011.6126544>（全文由使用者從 IEEE Xplore 下載提供；PDF 不放入公開 repo）

## 這篇在講什麼
提出 ORB（Oriented FAST and Rotated BRIEF）：在 FAST 偵測器加上方向、把 BRIEF 二元描述子改成能處理旋轉，目標是在效果接近 SIFT 的前提下快很多，能在手機上即時執行。[S3]

## 重點
- SIFT 計算量大，對即時系統與低功耗裝置是負擔。[S3]
- 偵測：FAST + Harris 排序 + 影像金字塔；方向：強度質心。[S3]
- 描述：rBRIEF，256 位元的二元字串；匹配用 Hamming 距離。[S3]
- 640×480 影像每張：ORB 15.3 ms、SURF 217.3 ms、SIFT 5228.7 ms。[S3]
- ORB 沒有 SIFT、SURF 的授權限制，並以 BSD 授權放進 OpenCV 2.3。[S3]

## 影響了哪些概念頁
[ORB](../concepts/orb.md)、[二元描述子](../concepts/binary-descriptor.md)、[特徵匹配](../concepts/feature-matching.md)、[Harris 角點偵測](../concepts/harris-corner.md)、[SIFT](../concepts/sift.md)、[尺度空間](../concepts/scale-space.md)、[雜訊穩健性的衝突](../concepts/noise-robustness-conflict.md)

## 刻意不收錄的部分（與使用者討論決定）
第 5 節 LSH（Locality Sensitive Hashing，在大型資料庫中快速找最近鄰）與 rBRIEF 貪婪搜尋的演算法步驟，對入門太細，只保留概念。

## 我的疑問
- 雜訊實驗（Figure 8）沒有說明 SIFT 用哪一個實作與參數。
- 結論說尺度不變性「沒有充分處理」，但實驗資料集有尺度變化時 ORB 表現仍不差，原因原文未分析。
