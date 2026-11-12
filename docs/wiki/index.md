# Wiki 目錄

## 來源頁
| 頁面 | 一句話 |
|---|---|
| [S1 OpenCV〈Understanding Features〉](sources/s1-opencv-features.md) | 用拼圖比喻說明什麼是特徵、偵測與描述 |
| [S2 Lowe (2004) SIFT](sources/s2-sift.md) | 對縮放、旋轉不變的經典特徵 |
| [S3 Rublee et al. (2011) ORB](sources/s3-orb.md) | 快兩個數量級的二元特徵 |
| [S4 DeTone et al. (2018) SuperPoint](sources/s4-superpoint.md) | 自監督學習的偵測＋描述網路 |
| [S5 Liu et al. (2025) LiftFeat](sources/s5-liftfeat.md) | 把 3D 法向量融合進描述子 |
| [S7 OpenCV〈Harris Corner Detection〉](sources/s7-opencv-harris.md) | 把角點的直覺寫成數學 |

## 概念頁
| 頁面 | 一句話 | 來源 |
|---|---|---|
| [特徵點](concepts/feature-point.md) | 能在別張影像中重新找到的獨特位置 | S1 |
| [角點](concepts/corner.md) | 往任何方向移動外觀都會變的位置 | S1, S7 |
| [特徵偵測](concepts/feature-detection.md) | 找出特徵點在哪裡 | S1, S7, S2 |
| [特徵描述](concepts/feature-description.md) | 把特徵周圍記錄成可比對的形式 | S1, S2, S3 |
| [特徵匹配](concepts/feature-matching.md) | 最近鄰＋比值檢驗把特徵配對 | S1, S2, S3 |
| [Harris 角點偵測](concepts/harris-corner.md) | 用分數 R 判斷角點的經典方法 | S7, S2, S3 |
| [尺度空間與 DoG](concepts/scale-space.md) | 用多層模糊在所有尺度找特徵 | S2, S3 |
| [SIFT](concepts/sift.md) | 對縮放、旋轉不變的偵測＋描述方法 | S2, S3 |
| [ORB](concepts/orb.md) | FAST＋BRIEF 加上方向，快速替代 SIFT | S3 |
| [二元描述子](concepts/binary-descriptor.md) | 0/1 字串描述子與 Hamming 距離 | S3 |
| [SuperPoint](concepts/superpoint.md) | 神經網路同時做偵測與描述 | S4 |
| [單應性](concepts/homography.md) | 影像對影像的 3×3 變換 | S4 |
| [自監督學習](concepts/self-supervised-learning.md) | 讓系統自己產生訓練標籤 | S4 |
| [指標選擇的陷阱](concepts/metric-choice-pitfall.md) | ORB 重複率最高卻匹配最差 | S4 |
| [LiftFeat](concepts/liftfeat.md) | 2D 描述子＋3D 法向量的輕量網路 | S5 |
| [表面法向量](concepts/surface-normal.md) | 表面朝向，平移與尺度不變的 3D 線索 | S5 |
| [雜訊穩健性的衝突](concepts/noise-robustness-conflict.md) | S2 與 S3 結論不同，要看實驗條件 | S2, S3 |

## 待建頁面
（目前無）
