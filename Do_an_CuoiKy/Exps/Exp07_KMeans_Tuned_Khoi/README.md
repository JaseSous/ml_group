# THÍ NGHIỆM 07: Tối Ưu Hóa Siêu Tham Số (Hyperparameter Tuning) Cho Mô Hình K-Means Trên Bộ Đặc Trưng RFM

## 1. Thông tin thí nghiệm
- **Mã thí nghiệm:** `Exp07_KMeans_Tuned_Khoi`
- **Người thực hiện:** **Phạm Minh Khôi** (RexCattus)
- **Mô hình / Thuật toán:** K-Means Clustering (`sklearn.cluster.KMeans`)
- **Bộ siêu tham số tối ưu:**
  - `n_clusters = 4` (Xác định qua phương pháp Khuỷu tay Elbow SSE & Silhouette Score tối ưu)
  - `init = 'k-means++'` (Thuật toán khởi tạo tâm cụm thông minh Arthur & Vassilvitskii, giải quyết triệt để bẫy cực tiểu địa phương)
  - `n_init = 25` (Tăng cường 25 lần khởi tạo độc lập để chọn nghiệm có hàm mục tiêu Inertia tối thiểu)
  - `max_iter = 300` (Giới hạn vòng lặp cực đại; thực tế hội tụ chỉ sau **11 vòng lặp**)
  - `algorithm = 'lloyd'` (Thuật toán lặp chuẩn Lloyd tường minh)
  - `random_state = 42` (Đảm bảo tính tái lập 100%)
- **Cơ chế suy luận trên tập mới:** `tuned_kmeans.predict()` (Khoảng cách Euclid tới 4 tâm cụm chuẩn hóa, chống rò rỉ dữ liệu)
- **Tập dữ liệu đầu vào:**
  - `../../data/rfm_train.csv` (2,736 khách hàng - 64%)
  - `../../data/rfm_val.csv` (684 khách hàng - 16%)
  - `../../data/rfm_test.csv` (855 khách hàng - 20%)
- **Tiền xử lý:** Biến đổi phi tuyến $\log(x + 1)$ khử độ lệch phải nặng (Skewness giảm từ 24.01 về 0.31) + Chuẩn hóa thang đo `StandardScaler` (chỉ fit trên tập Train).

---

## 2. Kết quả huấn luyện & Định lượng (Metrics)

### Bảng đối chuẩn định lượng hiệu năng trên 3 tập dữ liệu
| Tập dữ liệu | Quy mô | Silhouette Score (↑) | Davies-Bouldin (↓) | Calinski-Harabasz (↑) | Phương thức suy luận | Đánh giá |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Train (64%)** | 2,736 KH | **0.3385** | **0.9960** | **2,090.80** | Fit & Predict | Inertia: 2,490.39; hội tụ sau 11 iters |
| **Validation (16%)** | 684 KH | **0.3193** | **1.0210** | **503.80** | Predict tâm cụm | Ranh giới cụm phân tách rõ nét |
| **Test (20%)** | 855 KH | **0.3253** | **1.0248** | **629.08** | Predict tâm cụm | Tổng quát hóa xuất sắc, không Overfit |

### Phân bố 4 phân khúc khách hàng chuyên sâu trên tập Train
| Cụm | Tên phân khúc (Persona) | Số lượng KH | Tỷ lệ (%) | Recency TB | Frequency TB | Monetary TB | Đặc trưng & Chiến lược Marketing đề xuất |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Cụm 1** | **Champions (Khách hàng VIP)** | 498 | 18.20% | 14.3 ngày | 13.5 đơn | £7,362.2 | Rất gần, mua thường xuyên, chi tiêu khủng. Dịch vụ chăm sóc 1-on-1, tặng quà cá nhân hóa, không giảm giá đại trà. |
| **Cụm 3** | **Potential Loyalists (Tiềm năng)** | 594 | 21.71% | 22.2 ngày | 2.1 đơn | £552.3 | Khách mới mua gần đây, giá trị đơn khá. Gợi ý sản phẩm bổ trợ (Cross-sell/Up-sell), voucher có hạn cho đơn kế tiếp. |
| **Cụm 0** | **At Risk (Nguy cơ rời bỏ)** | 746 | 27.27% | 86.3 ngày | 4.1 đơn | £1,688.0 | Từng mua nhiều tiền nhưng đang nguội dần. Chiến dịch cứu vãn (Win-back), khảo sát ý kiến và tặng mã ưu đãi đặc biệt. |
| **Cụm 2** | **Lost / Hibernating (Rời bỏ)** | 898 | 32.82% | 189.4 ngày | 1.3 đơn | £291.3 | Mua từ rất lâu, tần suất và chi tiêu rất thấp. Tiếp cận chi phí thấp qua chiến dịch xả kho, hạn chế telesale tốn kém. |

### Đánh giá mức độ chi phối thuộc tính (ANOVA F-Score)
- **Frequency:** $F = 1,395.22$ (Đóng góp **35.8%**) – Thuộc tính phân tách cụm mạnh nhất.
- **Monetary:** $F = 1,391.07$ (Đóng góp **35.7%**) – Đóng vai trò quyết định trong việc bóc tách nhóm VIP và Nguy cơ.
- **Recency:** $F = 1,109.84$ (Đóng góp **28.5%**) – Hỗ trợ phân định khách hàng đang hoạt động và khách rời bỏ.

---

## 3. Các Artifacts sinh ra trong thí nghiệm
1. `kmeans_tuned_rfm_experiment.ipynb`: Toàn bộ notebook thực nghiệm tinh chỉnh siêu tham số, khảo sát 6 kịch bản khởi tạo và đánh giá 3 tập.
2. `kmeans_tuned_model.pkl`: File mô hình đóng gói thông tin siêu tham số tối ưu, tọa độ 4 tâm cụm Z-score và định nghĩa Persona.
3. `train_predicted_labels.csv`: Nhãn phân cụm và tên Persona của 2,736 khách hàng tập huấn luyện.
4. `metrics_result.json`: File JSON định lượng toàn diện siêu tham số, kết quả metrics, phân bố cụm và ANOVA F-score.
5. `metrics_summary.csv`: Bảng tổng kết số liệu đối chuẩn 3 tập Train - Validation - Test.
6. `kmeans_tuning_scenarios.png`: Biểu đồ so sánh định lượng 6 kịch bản siêu tham số K-Means.
7. `kmeans_scenarios_2d.png`: Không gian biểu diễn PCA 2D của 6 kịch bản tinh chỉnh.
8. `pca_2d_and_snake_plot.png`: Trực quan hóa ranh giới 4 cụm trên PCA 2D và biểu đồ chuẩn hóa Snake Plot thể hiện rõ nét hành vi từng phân khúc.
9. `kmeans_versions_comparison.png`: Biểu đồ đối chiếu toàn diện 3 phiên bản: K-Means Baseline vs K-Means Untuned vs Tuned K-Means.
10. `anova_fscore_rfm.png`: Biểu đồ cột thể hiện mức độ đóng góp phần trăm của 3 thuộc tính $R, F, M$.

---

## 4. Kết luận & Giá trị khoa học
- **Giải mã "Nghịch lý Silhouette":** Mô hình K-Means Baseline trên dữ liệu thô (Raw) có Silhouette tưởng chừng cao hơn (0.59) nhưng thực chất là "ảo ảnh toán học" do bị chi phối bởi ngoại lai (Outliers) dồn 98% khách hàng vào cụm 0. Bản Tuned K-Means trên RFM chuẩn hóa log-transformed tuy có Silhouette danh nghĩa là 0.3385 nhưng tạo ra các phân khúc thực chất, cân đối, mang giá trị kinh doanh thực tiễn cao nhất.
- **Tính ổn định tuyệt đối:** Với `n_init = 25` và thuật toán `k-means++`, mô hình hoàn toàn loại trừ nguy cơ rơi vào điểm cực tiểu địa phương nghèo nàn, đảm bảo 100% tái lập và độ tin cậy khi chuyển giao ứng dụng.
