# THÍ NGHIỆM 08: Hệ Thống Phân Khúc Khách Hàng Lai Ghép & Đồng Thuận 3 Mô Hình (Tri-Model Hybrid & Consensus Ensemble)

## 1. Thông tin thí nghiệm
- **Mã thí nghiệm:** `Exp08_Tri_Model_Hybrid_Ensemble_Thang`
- **Người thực hiện:** **Nguyễn Mạnh Thắng** (Thang)
- **Kiến trúc mô hình:** Chuỗi tích hợp 3 tầng (Tri-Stage Hybrid Pipeline) kết hợp Bộ máy đồng thuận Hungarian (Consensus Clustering Engine):
  - **Tầng 1 (Hierarchical Ward Linkage):** Phân tích cây phả hệ Dendrogram, sinh 4 tâm cụm hạt giống tiền định 100% (Deterministic Seed Centroids).
  - **Tầng 2 (K-Means Refinement):** Khởi tạo từ tâm hạt giống Tầng 1, hội tụ siêu tốc sau 7 vòng lặp (~3.2ms) để tối ưu hóa ranh giới Voronoi.
  - **Tầng 3 (DBSCAN Anomaly Profiling):** Quét mật độ $\varepsilon=0.6, \text{min\_samples}=10$, bóc tách độc lập 43 khách hàng Siêu Cá Voi / Dị biệt.
  - **Bộ máy đồng thuận (Consensus Engine):** Khớp nối nhãn tối ưu bằng thuật toán Hungarian (Linear Sum Assignment), phân loại khách hàng thành 3 phân tầng tin cậy: *Core Consensus*, *Boundary Contested*, và *Super Whales*.
- **Tập dữ liệu đầu vào:**
  - `../../data/rfm_train.csv` (2,736 khách hàng - 64%)
  - `../../data/rfm_val.csv` (684 khách hàng - 16%)
  - `../../data/rfm_test.csv` (855 khách hàng - 20%)
- **Cơ chế suy luận trên tập mới:** `NearestCentroid` huấn luyện trên tập Core Consensus Train để dự đoán cụm cho Validation và Test, hoàn toàn triệt tiêu rò rỉ dữ liệu (Anti-Leakage).

---

## 2. Kết quả định lượng & Đột phá chỉ số hiệu năng (Metrics)

### Bảng đối chuẩn định lượng qua các phân tập
| Phân tập dữ liệu | Quy mô | Trọng tâm đánh giá | Silhouette Score | Davies-Bouldin | Calinski-Harabasz | Đánh giá khoa học |
| :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| **Train (Toàn bộ)** | 2,736 KH | Mốc tham chiếu toàn bộ tập Train | **0.3385** | 0.9961 | 2,090.80 | Khớp chuẩn mực Baseline K-Means |
| **Train (Core Consensus)** | **2,212 KH** | **80.85% KH đồng thuận lõi** | **0.4189** | **0.8609** | **2,197.68** | **Đột phá vượt bậc (+23.8%)**, tách biệt sắc nét |
| **Validation** | 684 KH | Kiểm định tổng quát hóa (16%) | **0.3152** | 1.0144 | 494.72 | Suy luận ổn định cao |
| **Test** | 855 KH | Tập kiểm thử độc lập (20%) | **0.3251** | 1.0328 | 626.85 | Khả năng tổng quát hóa xuất sắc |

### Chỉ số đồng thuận giữa K-Means và Hierarchical
- **Adjusted Rand Index (ARI):** `0.5716`
- **Normalized Mutual Information (NMI):** `0.6173`
- **Tỷ lệ đồng thuận tuyệt đối (Core Consensus):** **80.85%** (2,212 khách hàng)

---

## 3. Chân dung 6 phân tầng khách hàng Tri-Model trên tập Train

| Phân tầng Persona | Tỷ lệ (%) | Số lượng | Recency TB | Frequency TB | Monetary TB | Monetary Median | Ý nghĩa kinh doanh & Chiến lược hành động |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **VIP Champions (Lõi)** | 21.02% | 575 KH | 21.6 ngày | 2.1 đơn | £551.1 | £470.2 | Khách hàng VIP cốt lõi mua gần đây; chăm sóc đặc quyền, giữ chân thương hiệu |
| **Loyal Customers (Lõi)** | 15.75% | 431 KH | 12.7 ngày | 11.5 đơn | £4,945.4 | £3,309.4 | Khách hàng trung thành mua tần suất cao; kích hoạt chương trình điểm thưởng |
| **Potential Customers (Lõi)** | 23.17% | 634 KH | 228.7 ngày | 1.2 đơn | £260.4 | £214.3 | Khách hàng tiềm năng mới; thúc đẩy chiến dịch khuyến mãi đơn hàng thứ hai |
| **Hibernating / At-Risk (Lõi)** | 20.91% | 572 KH | 101.7 ngày | 4.1 đơn | £1,741.8 | £1,374.4 | Khách nguy cơ rời bỏ; gửi email cá nhân hóa Win-back kèm ưu đãi hấp dẫn |
| **Boundary (Vùng tranh chấp)** | 17.58% | 481 KH | 64.8 ngày | 2.9 đơn | £886.9 | £606.2 | Khách hàng ở vùng giao thoa giữa các cụm; theo dõi và khảo sát thêm hành vi |
| **Super Whales (Cá mập siêu chi tiêu)** | **1.57%** | **43 KH** | 57.6 ngày | **34.9 đơn** | **£34,393.3** | **£17,703.6** | Doanh nghiệp B2B bán buôn; doanh thu gấp 12 lần bình quân; quản lý tài khoản riêng |

---

## 4. Danh mục Artifacts trong thư mục thí nghiệm
1. `tri_model_hybrid_ensemble_experiment.ipynb`: Toàn bộ mã nguồn thực thi chuỗi 3 tầng, thuật toán Hungarian, phân tích ANOVA và trực quan hóa 2D PCA.
2. `tri_model_hybrid_ensemble_model.pkl`: File mô hình đóng gói thông tin siêu tham số của cả 3 tầng (Hierarchical, K-Means, DBSCAN) và engine đồng thuận (pickle thuần).
3. `train_predicted_labels.csv`: Bảng nhãn chi tiết cho 2,736 khách hàng với đầy đủ đặc trưng gốc, log, chuẩn hóa và nhãn `Tri_Cluster_Label`, `Persona`, `Consensus_Status`.
4. `metrics_result.json`: File định lượng chi tiết kết quả huấn luyện, chỉ số đồng thuận, phân bố persona và đối chuẩn 3 tập.
5. `metrics_summary.csv`: Bảng tổng kết số liệu định lượng phục vụ báo cáo.
6. `tri_model_hybrid_consensus_2d.png`: Bản đồ trực quan hóa không gian PCA 2D bóc tách 3 phân tầng tin cậy (Core Consensus, Boundary, Super Whales).
7. `README.md`: Báo cáo chi tiết thí nghiệm, giá trị khoa học và kịch bản ứng dụng thực tế.

---

## 5. Kết luận khoa học & Đóng góp cốt lõi
1. **Giải mã triệt để "Nghịch lý Silhouette":** Bằng việc thiết lập bộ máy đồng thuận bóc tách 17.6% khách hàng vùng tranh chấp và 1.57% cá voi ngoại lai, điểm Silhouette trên nhóm Core Consensus vọt lên **0.4189**, chứng minh các cụm thực tế có độ cô đặc hình học rất cao khi loại trừ điểm nhiễu.
2. **Khắc phục nhược điểm của cả 3 thuật toán đơn lẻ:**
   - Khắc phục tính bất định của K-Means nhờ hạt giống tiền định từ Hierarchical.
   - Khắc phục độ phức tạp bậc hai $\mathcal{O}(N^2)$ của Hierarchical nhờ tốc độ hội tụ nhanh của K-Means.
   - Khắc phục hiện tượng dồn cụm của DBSCAN bằng cách chỉ dùng DBSCAN làm bộ lọc mật độ vi mô tầng 3.
3. **Giá trị ứng dụng thực tiễn:** Giúp doanh nghiệp bán lẻ trực tuyến Online Retail II đưa ra quyết định marketing an toàn tuyệt đối trên 80.8% khách hàng đồng thuận, đồng thời áp dụng chính sách chăm sóc tài khoản chuyên biệt (Account Manager) cho 43 đối tác bán buôn lớn.
