# THÍ NGHIỆM 06: Kiến Trúc Học Máy Lai 2 Tầng Hierarchical (Ward K=4) & DBSCAN (eps=0.6, min_samples=5) Trên Đặc Trưng RFM

## 1. Thông tin thí nghiệm
- **Mã thí nghiệm:** `Exp06_Hierarchical_DBSCAN_Thang`
- **Người thực hiện:** **Nguyễn Mạnh Thắng** (Thang)
- **Mô hình / Thuật toán:** Mô hình lai 2 tầng kết hợp Phân cụm Thứ bậc (Hierarchical Clustering) và Mật độ không gian (DBSCAN).
- **Kiến trúc phân tầng chuyên sâu:**
  - **Tầng 1 (Vĩ mô - Macro Clustering):** `AgglomerativeClustering(n_clusters=4, linkage='ward', metric='euclidean')` phân rã không gian khách hàng thành 4 nhánh chiến lược tự nhiên dựa trên khoảng cách liên kết phương sai tối thiểu Ward.
  - **Tầng 2 (Vi mô - Micro Anomaly Profiling):** `DBSCAN(eps=0.6, min_samples=5, metric='euclidean')` áp dụng độc lập bên trong từng cụm thứ bậc để bóc tách các điểm dữ liệu dị biệt mật độ cục bộ.
- **Cơ chế suy luận 2 bước chống rò rỉ dữ liệu (Anti-Leakage Inference):**
  - Bước 1: Gán nhãn cụm vĩ mô $0, 1, 2, 3$ bằng mô hình `NearestCentroid` đã fit tâm từ tập Train.
  - Bước 2: Truy vấn khoảng cách Euclid tới tập điểm lõi gần nhất (`NearestNeighbors`) trong cụm đó với ngưỡng $\varepsilon = 0.6$. Nếu khoảng cách $\le 0.6 \rightarrow$ Khách cốt lõi; nếu $> 0.6 \rightarrow$ Khách dị biệt/Cá voi.
- **Tập dữ liệu đầu vào:**
  - `../../data/rfm_train.csv` (2,736 khách hàng - 64%)
  - `../../data/rfm_val.csv` (684 khách hàng - 16%)
  - `../../data/rfm_test.csv` (855 khách hàng - 20%)

---

## 2. Kết quả định lượng & Bóc tách 8 phân khúc chuyên sâu

### Bảng đối chuẩn định lượng khả năng tổng quát hóa
| Tập dữ liệu | Quy mô | Số khách dị biệt | Tỷ lệ dị biệt (%) | Macro Silhouette | Cơ chế suy luận | Đánh giá |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Train** | 2,736 KH | **30 KH** | **1.10%** | **0.2976** | Agglomerative + DBSCAN Fit | Nhận diện sắc nét 21 siêu cá voi (£58.1K) |
| **Validation** | 684 KH | **8 KH** | **1.17%** | **0.3093** | NearestCentroid + Nearest Core | Tỷ lệ dị biệt duy trì ổn định cao |
| **Test** | 855 KH | **5 KH** | **0.58%** | **0.3210** | NearestCentroid + Nearest Core | Tổng quát hóa xuất sắc trên tập Test |

### Chi tiết 8 phân khúc khách hàng chuyên sâu trên tập Train
| Mã | Tên phân khúc chuyên sâu | Số lượng | Tỷ lệ (%) | Recency TB | Frequency TB | Monetary TB | Monetary Max | Hành vi & Chiến lược kinh doanh |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1B** | **Champions Super Whales (Cá Voi B2B)** | **21** | **0.77%** | 28.6 ngày | 54.8 đơn | **£58,148.0** | **£323,860.5** | Doanh nghiệp mua buôn cực lớn; phân bổ Giám đốc quan hệ khách hàng (Account Manager) riêng |
| **1A** | Champions Regular (VIP Tiêu Dùng) | 469 | 17.14% | 13.6 ngày | 11.6 đơn | £5,159.5 | £47,111.2 | Khách hàng VIP chi tiêu đều đặn; chương trình tri ân khách hàng thân thiết |
| **0B** | Potential High Velocity | 3 | 0.11% | 5.3 ngày | 2.0 đơn | £1,011.6 | £2,904.8 | Khách mới mua rất gần với giá trị đơn hàng cao; thúc đẩy thăng hạng VIP |
| **0A** | Potential Loyalists Core | 895 | 32.71% | 30.1 ngày | 2.2 đơn | £660.1 | £3,386.3 | Nhóm tiềm năng cốt lõi số đông; kích hoạt bằng các chiến dịch cross-sell/upsell |
| **3B** | At Risk High Value | 5 | 0.18% | 118.0 ngày | 7.4 đơn | £2,447.7 | £11,230.0 | Khách VIP cũ đang nguội dần; CSKH gọi điện chăm sóc trực tiếp tái kích hoạt |
| **3A** | At Risk Core | 706 | 25.80% | 105.3 ngày | 4.0 đơn | £1,562.5 | £12,931.4 | Khách hàng rời xa dần; gửi email voucher giảm giá cá nhân hóa |
| **2B** | Lost Dead Accounts | 1 | 0.04% | 358.0 ngày | 1.0 đơn | £2.95 | £2.95 | Tài khoản không hoạt động, đơn giá cực thấp; kiểm toán hệ thống |
| **2A** | Lost / Hibernating Standard | 636 | 23.25% | 228.7 ngày | 1.2 đơn | £259.6 | £1,248.5 | Khách đã rời bỏ hoàn toàn; chạy chiến dịch dọn kho giảm giá sâu tự động |

---

## 3. Các Artifacts sinh ra trong thí nghiệm
1. `hierarchical_dbscan_hybrid_experiment.ipynb`: Notebook hoàn chỉnh quy trình kiến trúc lai 2 tầng và phân tích 8 phân khúc.
2. `hybrid_hierarchical_dbscan_model.pkl`: File mô hình đóng gói thông tin siêu tham số của cả Tầng 1 (Hierarchical) và Tầng 2 (DBSCAN).
3. `train_predicted_labels.csv`: Bảng nhãn chi tiết với đầy đủ các cột: `Hierarchical_Cluster`, `DBSCAN_SubLabel`, `Is_Special`, `Micro_Segment`.
4. `metrics_result.json`: File JSON định lượng toàn diện kết quả thực nghiệm.
5. `metrics_summary.csv`: Bảng tổng kết số liệu đối chuẩn định lượng 3 tập.
6. `hierarchical_dbscan_hybrid.png`: Không gian biểu diễn PCA 2D và biểu đồ Snake Plot bóc tách nhóm Cá voi B2B.
7. `comparison_kmeans_vs_hierarchical_dbscan.png`: Đối chiếu chi tiết 2 kiến trúc lai: K-Means + DBSCAN vs Hierarchical + DBSCAN.

---

## 4. Kết luận & Đóng góp cốt lõi
- **Ưu thế tuyệt đối về tính xác định (100% Deterministic):** Khác với mô hình lai KMeans + DBSCAN phụ thuộc vào điểm hạt giống ngẫu nhiên (`random_state`), kiến trúc Hierarchical + DBSCAN mang tính tiền định 100%, đảm bảo kết quả phân rã không gian luôn lặp lại tuyệt đối qua mọi lần thực thi.
- **Độ tinh chọn nhóm Siêu Cá Voi cao hơn:** Mô hình bóc tách 21 siêu cá voi với mức chi tiêu trung bình £58,148.0 (cao hơn £55,725.3 của KMeans + DBSCAN), loại bỏ bớt các trường hợp cá voi biên, giúp việc tiếp cận B2B của doanh nghiệp Online Retail II đạt tỷ suất hoàn vốn (ROI) tối ưu nhất.
- **Tính tổng quát hóa bền vững:** Nhờ cơ chế NearestCentroid và Nearest Core Samples, tỷ lệ khách ngoại lai duy trì ổn định quanh mức 0.58% - 1.17% qua cả tập Validation và Test độc lập.
