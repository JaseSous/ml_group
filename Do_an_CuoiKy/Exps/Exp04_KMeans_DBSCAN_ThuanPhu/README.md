# THÍ NGHIỆM 04: Kiến Trúc Mô Hình Học Máy Lai Nâng Cao (Hybrid Two-Stage Clustering: K-Means & DBSCAN Tuned)

## 1. Thông tin thí nghiệm
- **Mã thí nghiệm:** `Exp04_KMeans_DBSCAN_ThuanPhu`
- **Người thực hiện:** **Trương Thuận Phú** (ThuanPhu)
- **Kiến trúc mô hình:** Two-Stage Personalized Outlier Profiling Pipeline (Kết hợp phân vùng vĩ mô và bóc tách dị biệt vi mô)
  - **Tầng 1 (Macro Segmentation):** K-Means Clustering (`n_clusters = 4`, `init = 'k-means++'`, `n_init = 25`, `random_state = 42`)
  - **Tầng 2 (Micro Outlier Profiling):** DBSCAN cục bộ chạy độc lập trong từng phân khúc (`eps = 0.6`, `min_samples = 5`, `metric = 'euclidean'`)
- **Cơ chế suy luận trên tập mới:** `K-Means predict()` cho Tầng 1 + `Nearest Core Samples` (k-d tree bán kính $\epsilon=0.6$) cho Tầng 2, đảm bảo **Zero Data Leakage**.
- **Tập dữ liệu đầu vào:**
  - `../../data/rfm_train.csv` (2,736 khách hàng - 64%)
  - `../../data/rfm_val.csv` (684 khách hàng - 16%)
  - `../../data/rfm_test.csv` (855 khách hàng - 20%)
- **Tiền xử lý:** Biến đổi Log-transform phi tuyến $\log(x + 1)$ khử lệch phải + Chuẩn hóa thang đo `StandardScaler` (chỉ fit trên Train).

---

## 2. Kết quả định lượng & Bóc tách 8 Phân khúc Chuyên sâu

### Kiểm định khả năng tổng quát hóa trên 3 tập dữ liệu
| Tập dữ liệu | Quy mô | Số khách đặc biệt / Siêu VIP | Tỷ lệ đặc biệt | Macro Silhouette | Cơ chế suy luận | Đánh giá |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Train** | 2,736 KH | **31 KH** | **1.13%** | **0.3385** | Fit KMeans + DBSCAN cục bộ | Học ranh giới mật độ 4 vùng |
| **Validation** | 684 KH | **7 KH** | **1.02%** | **0.3193** | KMeans predict + Nearest Core | Suy luận ổn định cao |
| **Test** | 855 KH | **5 KH** | **0.58%** | **0.3253** | KMeans predict + Nearest Core | Tổng quát hóa xuất sắc |

### Chi tiết 8 phân khúc khách hàng chuyên biệt trên tập Train
| Mã | Tên phân khúc chuyên sâu | Số lượng | Tỷ lệ (%) | Recency TB | Frequency TB | Monetary TB | Monetary Max | Hành vi & Kịch bản kinh doanh |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1B** | **Champions Super Whales (Cá Voi B2B)** | **22** | **0.80%** | 7.4 ngày | 53.2 đơn | **£55,725.3** | **£323,860.0** | Doanh nghiệp mua buôn; chăm sóc Account Manager riêng |
| **1A** | Champions Regular (VIP Tiêu Dùng) | 476 | 17.40% | 12.8 ngày | 10.3 đơn | £5,120.4 | £28,000.0 | Khách VIP mua đều; tri ân khách hàng thân thiết |
| **0B** | Potential Rising Stars (Ngôi Sao Bứt Phá) | 3 | 0.11% | 21.0 ngày | 7.0 đơn | £4,020.0 | £6,200.0 | Khách mới giá trị đơn lớn; đẩy ưu đãi thăng hạng VIP |
| **0A** | Potential Regular (Tiềm Năng Chuẩn) | 743 | 27.16% | 42.1 ngày | 3.7 đơn | £1,690.2 | £7,500.0 | Khách hàng tiềm năng; upsell và cross-sell |
| **3B** | At Risk High-Loss (VIP Cũ Dừng Đột Ngột) | 4 | 0.15% | 182.0 ngày | 4.2 đơn | £783.5 | £1,800.0 | Khách cũ từng chi tiêu cao ngừng mua; CSKH gọi điện trực tiếp |
| **3A** | At Risk Regular (Nguy Cơ Rời Bỏ) | 590 | 21.56% | 164.2 ngày | 1.9 đơn | £551.4 | £2,100.0 | Khách hàng nguội lạnh; email remarketing kích hoạt lại |
| **2B** | Lost Anomalies (Tài Khoản Dị Biệt) | 2 | 0.07% | 328.0 ngày | 4.5 đơn | £92.4 | £150.0 | Đơn giá cực thấp; kiểm toán dữ liệu và loại trừ khỏi báo cáo |
| **2A** | Lost Regular (Rời Bỏ Phổ Thông) | 896 | 32.75% | 381.5 ngày | 1.3 đơn | £292.1 | £1,200.0 | Khách rời bỏ lâu; chạy chiến dịch dọn kho giảm giá sâu |

---

## 3. Các Artifacts sinh ra trong thí nghiệm
1. `kmeans_dbscan_hybrid_experiment.ipynb`: Notebook hoàn chỉnh quy trình kiến trúc lai 2 tầng và phân tích 8 phân khúc.
2. `hybrid_kmeans_dbscan_model.pkl`: File mô hình đóng gói thông tin siêu tham số của cả Tầng 1 (K-Means) và Tầng 2 (DBSCAN).
3. `train_predicted_labels.csv`: Bảng nhãn chi tiết với đầy đủ các cột: `KMeans_Cluster`, `DBSCAN_SubLabel`, `Is_Special`, `Micro_Segment`.
4. `metrics_result.json`: File JSON định lượng toàn diện kết quả thực nghiệm.
5. `metrics_summary.csv`: Bảng tổng kết số liệu đối chuẩn định lượng.
6. `hybrid_pca_and_whales_snake.png`: Không gian biểu diễn PCA 2D và biểu đồ Snake Plot bóc tách nhóm Cá voi B2B.
7. `comparison_kmeans_vs_hierarchical_dbscan.png`: Đối chiếu chi tiết kiến trúc lai K-Means + DBSCAN với Hierarchical + DBSCAN.

---

## 4. Kết luận & Đóng góp cốt lõi
- **Giải quyết triệt để điểm yếu của các mô hình đơn lẻ:** K-Means đơn lẻ thường làm phẳng các ngoại lai có giá trị cao, trong khi DBSCAN đơn lẻ dồn 98% khách hàng vào một cụm. Mô hình lai kết hợp hoàn hảo ưu điểm cấu trúc vùng lồi của K-Means và khả năng lọc mật độ của DBSCAN.
- **Phát hiện 22 siêu cá voi (Champions Super Whales):** Bóc tách chính xác 22 khách hàng đặc biệt với chi tiêu trung bình lên tới £55.7K (cực đại £323.8K), mang lại giá trị thực tiễn kinh doanh đột phá cho hệ thống bán lẻ Online Retail II.
- **Tính tổng quát hóa bền vững:** Nhờ cơ chế Nearest Core Samples, tỷ lệ khách ngoại lai duy trì ổn định quanh mức 0.6% - 1.1% qua cả tập Validation và Test độc lập.
