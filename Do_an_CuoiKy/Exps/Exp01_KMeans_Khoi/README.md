# THÍ NGHIỆM 01: Huấn luyện K-Means trên đặc trưng RFM (K=4)

## 1. Thông tin thí nghiệm
- **Mã thí nghiệm:** `Exp01_KMeans_Khoi`
- **Người thực hiện:** **Khôi**
- **Mô hình / Thuật toán:** K-Means Clustering (`sklearn.cluster.KMeans`)
- **Siêu tham số:**
  - `n_clusters = 4`
  - `init = 'k-means++'`
  - `n_init = 10`
  - `random_state = 42`
- **Tập dữ liệu đầu vào:**
  - `../../data/rfm_train.csv` (2,736 khách hàng)
  - `../../data/rfm_val.csv` (684 khách hàng)
  - `../../data/rfm_test.csv` (855 khách hàng)
- **Tiền xử lý:** Biến đổi Log-transform `log(x + 1)` khử lệch phải + Chuẩn hóa thang đo `StandardScaler`.

---

## 2. Kết quả huấn luyện (Train Artifacts & Results)
Thí nghiệm tự động xuất các file kết quả sau khi train:
1. **File mô hình đã huấn luyện:** `kmeans_model.pkl` (Lưu trọng số mô hình để tái sử dụng).
2. **File nhãn phân cụm:** `train_predicted_labels.csv` (Gán nhãn 4 phân khúc cho 2,736 khách hàng).
3. **Bảng số liệu chi tiết:** `metrics_result.json` và `metrics_summary.csv`.

### Bảng kết quả định lượng (Metrics)
| Tập dữ liệu | Số mẫu | Silhouette Score | Davies-Bouldin | Calinski-Harabasz | Đánh giá |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Train** | 2,736 | **0.3385** | **0.9960** | **2,090.80** | Hội tụ ổn định |
| **Validation** | 684 | **0.3193** | **1.0210** | **503.80** | Độ suy giảm chỉ 5.6% |
| **Test** | 855 | **0.3253** | **1.0248** | **629.08** | Khả năng tổng quát hóa tốt |

---

## 3. Các biểu đồ kết quả (Artifacts sinh ra)
Thí nghiệm tự động xuất các biểu đồ trực quan hóa:
1. `elbow_method_sse.png`: Đường cong Elbow xác định điểm gập tại $K=4$.
2. `silhouette_scores_k.png`: So sánh điểm Silhouette giữa các giá trị $K \in [2, 10]$.
3. `pca_2d_clusters.png`: Không gian biểu diễn phân cụm 2D thông qua PCA.
4. `cluster_profiles.png`: Phân bố đặc trưng Recency, Frequency, Monetary trên 4 phân khúc.

---

## 4. Kết luận
- Mô hình phân tách khách hàng thành 4 nhóm rõ rệt:
  - **Cụm 0 - At Risk:** Khách hàng từng chi tiêu cao nhưng lâu chưa quay lại.
  - **Cụm 1 - Champions:** Khách hàng VIP mua thường xuyên, giá trị đơn lớn.
  - **Cụm 2 - Lost:** Khách hàng rời bỏ, mua ít và rất lâu không hoạt động.
  - **Cụm 3 - Potential Loyalists:** Khách hàng mới có tiềm năng gắn bó.
- Đạt chuẩn yêu cầu của đồ án và được chọn làm mô hình triển khai chính thức.
