# THÍ NGHIỆM 09: Kiến Trúc Học Máy Lai 2 Tầng Hierarchical (Ward K=4) & DBSCAN (eps=0.6, min_samples=5) Trên Đặc Trưng RFM

## 1. Thông tin thí nghiệm
- **Mã thí nghiệm:** `Exp09_Hierarchical_DBSCAN_ThuanPhu`
- **Người thực hiện:** **Trương Thuận Phú** (ThuanPhu)
- **Mô hình / Thuật toán:** Mô hình lai 2 tầng kết hợp Phân cụm Thứ bậc (Hierarchical Clustering) và Mật độ không gian (DBSCAN).
- **Kiến trúc phân tầng chuyên sâu:**
  - **Tầng 1 (Vĩ mô - Macro Clustering):** `AgglomerativeClustering(n_clusters=4, linkage='ward', metric='euclidean')` phân rã không gian khách hàng thành 4 nhánh chiến lược tự nhiên dựa trên khoảng cách liên kết phương sai tối thiểu Ward.
  - **Tầng 2 (Vi mô - Micro Anomaly Profiling):** `DBSCAN(eps=0.6, min_samples=5, metric='euclidean')` áp dụng độc lập bên trong từng cụm thứ bậc để bóc tách các điểm dữ liệu dị biệt mật độ cục bộ.
- **Cơ chế suy luận 2 bước chống rò rỉ dữ liệu (Anti-Leakage Inference):**
  - Bước 1: Gán nhãn cụm vĩ mô $0, 1, 2, 3$ bằng mô hình `NearestCentroid` (được fit từ các tâm cụm thứ bậc tập Train).
  - Bước 2: So sánh khoảng cách Euclid tới các điểm **Core Samples** của cụm tương ứng thông qua cấu trúc cây k-d tree (`NearestNeighbors`). Nếu khoảng cách $\le 0.6$, khách hàng là **Regular (Tiêu chuẩn)**; ngược lại gán nhãn **Special / Whale (Dị biệt)**.
- **Tập dữ liệu đầu vào:**
  - `../../data/rfm_train.csv` (2,736 khách hàng - 64%)
  - `../../data/rfm_val.csv` (684 khách hàng - 16%)
  - `../../data/rfm_test.csv` (855 khách hàng - 20%)
- **Tiền xử lý:** Biến đổi phi tuyến $\log(x + 1)$ khử lệch phải + Chuẩn hóa thang đo `StandardScaler` (chỉ fit trên tập Train).

---

## 2. Kết quả định lượng & Bóc tách 8 Phân khúc Chuyên sâu

### Bảng kiểm định tính tổng quát hóa trên 3 tập dữ liệu
| Tập dữ liệu | Quy mô | Số khách đặc biệt / Siêu VIP | Tỷ lệ đặc biệt | Macro Silhouette | Cơ chế suy luận | Đánh giá |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Train** | 2,736 KH | **30 KH** | **1.10%** | **0.2976** | Fit Hierarchical + DBSCAN cục bộ | Học ranh giới mật độ 4 nhánh |
| **Validation** | 684 KH | **8 KH** | **1.17%** | **0.3093** | NearestCentroid + Nearest Core | Suy luận ổn định cao |
| **Test** | 855 KH | **5 KH** | **0.58%** | **0.3210** | NearestCentroid + Nearest Core | Tổng quát hóa xuất sắc (+7.84%) |

### Chi tiết 8 phân khúc khách hàng chuyên biệt trên tập Train
| Mã | Tên phân khúc chuyên sâu | Số lượng | Tỷ lệ (%) | Recency TB | Frequency TB | Monetary TB | Monetary Max | Hành vi & Kịch bản kinh doanh |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1B** | **Champions Super Whales (Cá Voi B2B)** | **21** | **0.77%** | 28.6 ngày | 54.8 đơn | **£58,148.0** | **£323,860.5** | Khách mua buôn cực lớn; tài khoản VIP cần Account Manager riêng |
| **1A** | Champions Regular (VIP Tiêu Dùng) | 469 | 17.14% | 13.6 ngày | 11.6 đơn | £5,159.5 | £47,111.2 | Khách VIP mua thường xuyên; chăm sóc duy trì lòng trung thành |
| **0B** | Potential High Velocity (Bứt Phá) | 3 | 0.11% | 5.3 ngày | 2.0 đơn | £1,011.6 | £2,904.8 | Khách mới mua rất gần đây với giá trị tốt; kích cầu lên VIP |
| **0A** | Potential Loyalists Core (Tiềm Năng Chuẩn) | 895 | 32.71% | 30.1 ngày | 2.2 đơn | £660.1 | £3,386.3 | Phân khúc tiềm năng đông đảo; cross-sell và upsell |
| **3B** | At Risk High Value (VIP Cũ Cần Cứu Vãn) | 5 | 0.18% | 118.0 ngày | 7.4 đơn | £2,447.7 | £11,230.0 | Khách từng chi tiêu rất cao nhưng có dấu hiệu rời bỏ; CSKH gọi điện |
| **3A** | At Risk Core (Nguy Cơ Rời Bỏ Phổ Thông) | 706 | 25.80% | 105.3 ngày | 4.0 đơn | £1,562.6 | £12,931.4 | Khách hàng nguội lạnh; email remarketing kích hoạt lại |
| **2B** | Lost Dead Accounts (Tài Khoản Rác / Ảo) | 1 | 0.04% | 358.0 ngày | 1.0 đơn | £3.0 | £3.0 | Đơn hàng 0đ hoặc tài khoản thử nghiệm; IT kiểm toán loại bỏ |
| **2A** | Lost Standard (Rời Bỏ Lâu Ngày) | 636 | 23.25% | 228.7 ngày | 1.2 đơn | £259.6 | £1,248.5 | Khách hàng không còn hoạt động; chiến dịch dọn kho giảm giá sâu |

---

## 3. Các Artifacts sinh ra trong thí nghiệm
1. `hierarchical_dbscan_hybrid_experiment.ipynb`: Toàn bộ notebook cài đặt kiến trúc lai 2 tầng và phân tích 8 phân khúc.
2. `hybrid_hierarchical_dbscan_model.pkl`: File mô hình đóng gói thông số cấu hình và siêu tham số của cả 2 tầng.
3. `train_predicted_labels.csv`: Bảng nhãn chi tiết với đầy đủ các cột đặc trưng RFM, `Hierarchical_Cluster`, `DBSCAN_SubLabel`, `Is_Special`, và `Micro_Segment`.
4. `metrics_result.json`: File JSON ghi nhận toàn bộ kết quả định lượng chi tiết.
5. `metrics_summary.csv`: Bảng tổng kết số liệu đối chuẩn định lượng.
6. `hierarchical_dbscan_hybrid.png`: Không gian biểu diễn phân cụm lai PCA 2D và cấu trúc bóc tách nhóm cá voi.
7. `comparison_kmeans_vs_hierarchical_dbscan.png`: Đối chiếu chi tiết hiệu năng giữa 2 kiến trúc lai: KMeans+DBSCAN vs Hierarchical+DBSCAN.

---

## 4. Kết luận & Giá trị đóng góp
- **Tính xác định tuyệt đối (100% Deterministic):** Không giống như K-Means phụ thuộc vào `random_state`, mô hình Hierarchical + DBSCAN hoàn toàn ổn định và cho kết quả gán nhãn giống hệt nhau trên mọi môi trường chạy.
- **Bóc tách 21 Siêu Cá Voi tinh chọn (£58,148 TB):** Nhờ cơ chế liên kết Ward bảo toàn phương sai, nhóm cá voi bóc tách được ở mô hình này có mức chi tiêu trung bình cao hơn mô hình KMeans + DBSCAN (£58.1K vs £55.7K), mang tính tinh gọn và chính xác hơn cho bài toán bán sỉ B2B.
- **Tính tổng quát hóa bền vững:** Tỷ lệ khách dị biệt duy trì từ 0.58% đến 1.17% trên cả Validation và Test độc lập, chứng minh tính khả thi cao khi ứng dụng vào hệ thống CRM sản xuất.
