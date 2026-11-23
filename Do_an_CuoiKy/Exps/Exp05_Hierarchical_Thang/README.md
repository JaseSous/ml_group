# THÍ NGHIỆM 05: Tinh Chỉnh Mô Hình Phân Cụm Thứ Bậc (Hierarchical Agglomerative Clustering) Trên Đặc Trưng RFM

## 1. Thông tin thí nghiệm
- **Mã thí nghiệm:** `Exp05_Hierarchical_Thang`
- **Người thực hiện:** **Nguyễn Mạnh Thắng** (Thang)
- **Mô hình / Thuật toán:** Hierarchical Agglomerative Clustering (`sklearn.cluster.AgglomerativeClustering`)
- **Siêu tham số tối ưu:**
  - `n_clusters = 4` (Xác định tự nhiên thông qua khoảng cách cắt trên cây phả hệ Dendrogram)
  - `linkage = 'ward'` (Tối thiểu hóa tổng phương sai nội cụm theo hệ thức Lance-Williams)
  - `metric = 'euclidean'`
- **Cơ chế suy luận trên tập mới:** `NearestCentroid` (Học tâm 4 cụm từ tập Train để gán nhãn cho Validation và Test, triệt tiêu hoàn toàn Data Leakage)
- **Tập dữ liệu đầu vào:**
  - `../../data/rfm_train.csv` (2,736 khách hàng - 64%)
  - `../../data/rfm_val.csv` (684 khách hàng - 16%)
  - `../../data/rfm_test.csv` (855 khách hàng - 20%)
- **Tiền xử lý:** Biến đổi Log-transform phi tuyến $\log(x + 1)$ khử lệch phải + Chuẩn hóa thang đo `StandardScaler` (chỉ fit trên Train).

---

## 2. Kết quả huấn luyện & Định lượng (Metrics)

### Bảng kết quả định lượng trên 3 tập dữ liệu
| Tập dữ liệu | Quy mô | Silhouette Score | Davies-Bouldin | Calinski-Harabasz | Phương thức suy luận | Đánh giá |
| :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Train** | 2,736 KH | **0.2976** | **1.0827** | **1,808.38** | Agglomerative (Fit) | Huấn luyện thành công trên 100% dữ liệu |
| **Validation** | 684 KH | **0.3093** | **1.0281** | **485.68** | `NearestCentroid` | Điểm Silhouette tăng **+3.92%** so với Train |
| **Test** | 855 KH | **0.3210** | **1.0485** | **621.10** | `NearestCentroid` | Tổng quát hóa xuất sắc (**+7.84%**), không Overfit |

### Phân bố 4 phân khúc khách hàng trên tập Train
- **Cụm 0 - Potential Loyalists (Tiềm năng):** 898 khách hàng (32.8%)
- **Cụm 1 - Champions (Khách hàng VIP):** 490 khách hàng (17.9%)
- **Cụm 2 - Lost / Hibernating (Rời bỏ):** 637 khách hàng (23.3%)
- **Cụm 3 - At Risk (Nguy cơ rời bỏ):** 711 khách hàng (26.0%)

---

## 3. Các Artifacts sinh ra trong thí nghiệm
1. `hierarchical_rfm_experiment.ipynb`: Toàn bộ mã nguồn thực nghiệm, khảo sát 7 kịch bản linkage và phân tích ANOVA F-score.
2. `hierarchical_model.pkl`: File mô hình đóng gói thông tin cấu hình và siêu tham số phục vụ tái sử dụng (pickle thuần).
3. `train_predicted_labels.csv`: Nhãn phân cụm 4 nhóm cho 2,736 khách hàng tập huấn luyện.
4. `metrics_result.json`: Chi tiết tham số, siêu tham số, phân bố cụm và định lượng metrics.
5. `metrics_summary.csv`: Bảng tổng kết số liệu đối chuẩn 3 tập Train - Validation - Test.
6. `dendrogram_ward.png`: Cây phả hệ Dendrogram chỉ rõ điểm cắt tự nhiên tại $K=4$.
7. `hierarchical_tuning_scenarios.png`: Đối chuẩn định lượng 7 kịch bản siêu tham số.
8. `hierarchical_scenarios_2d.png`: Trực quan hóa không gian phân cụm PCA 2D của các kịch bản.

---

## 4. Kết luận & Giá trị khoa học
- **Tính xác định (Determinism):** Khác với K-Means phụ thuộc vào điểm khởi tạo ban đầu (`random_state`), Hierarchical Clustering đạt tính xác định 100%, cho ra kết quả phân cụm hoàn toàn nhất quán giữa các lần chạy.
- **Tính tổng quát hóa tuyệt vời:** Điểm Silhouette tăng đều từ Train ($0.2976$) sang Validation ($0.3093$) và Test ($0.3210$), chứng tỏ cấu trúc cây học được phản ánh bản chất phân bổ khách hàng của Online Retail II.
- **Đóng góp của tác giả:** Thử nghiệm thành công cơ chế `NearestCentroid` để suy luận trên dữ liệu chưa biết, hoàn toàn khắc phục được nhược điểm thiếu hàm `predict()` của thuật toán Agglomerative Clustering truyền thống.
