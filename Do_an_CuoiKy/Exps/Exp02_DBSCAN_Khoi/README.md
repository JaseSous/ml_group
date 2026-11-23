# THÍ NGHIỆM 02: Tối ưu hóa siêu tham số mô hình DBSCAN trên đặc trưng RFM

## 1. Thông tin thí nghiệm
- **Mã thí nghiệm:** `Exp02_DBSCAN_Khoi`
- **Người thực hiện:** **Phạm Minh Khôi**
- **Mô hình / Thuật toán:** DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- **Siêu tham số tối ưu:**
  - `eps = 0.6` (Xác định thông qua đồ thị đa đường $k$-distance với $k=10$)
  - `min_samples = 10`
  - `metric = 'euclidean'`
- **Tập dữ liệu đầu vào:**
  - `../../data/rfm_train.csv` (2,736 khách hàng)
  - `../../data/rfm_val.csv` (684 khách hàng)
  - `../../data/rfm_test.csv` (855 khách hàng)
- **Tiền xử lý:** Log-transform `log(x + 1)` + Chuẩn hóa thang đo `StandardScaler`.

---

## 2. Kết quả huấn luyện & Định lượng (Metrics)
Mô hình sử dụng cơ chế suy luận **Nearest Core Samples** để dự đoán phân cụm trên tập Validation và Test nhằm triệt tiêu hoàn toàn rò rỉ dữ liệu (Zero Data Leakage).

| Tập dữ liệu | Số mẫu | Silhouette Score | Davies-Bouldin | Calinski-Harabasz | Số điểm ngoại lai | Tỷ lệ ngoại lai | Đánh giá |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Train** | 2,736 | **0.5254** | **0.4055** | **117.32** | 43 | **1.57%** | Tách ngoại vi sắc nét |
| **Validation** | 684 | **0.5274** | **0.3382** | **17.46** | 10 | **1.46%** | Không suy giảm chỉ số |
| **Test** | 855 | **0.5298** | **0.4017** | **25.43** | 14 | **1.64%** | Tổng quát hóa xuất sắc |

---

## 3. Các biểu đồ kết quả (Artifacts sinh ra)
1. `kdistance_multiline.png`: Đồ thị $k$-distance với các giá trị $k \in \{4, 6, 10\}$ chỉ rõ điểm uốn tối ưu tại $\epsilon = 0.6$.
2. `dbscan_clusters_and_whales.png`: Biểu đồ không gian phân cụm PCA và hồ sơ phân tích nhóm khách hàng siêu VIP (B2B Whales).

---

## 4. Kết luận & Vai trò trong đề tài
- Thuật toán DBSCAN chứng minh năng lực vượt trội trong việc phát hiện các điểm dữ liệu dị biệt có mật độ thấp.
- Khoảng ~1.5% khách hàng ngoại lai được bóc tách chính là nhóm khách hàng doanh nghiệp / tổ chức mua buôn có quy mô đơn hàng khổng lồ (Whales), giúp mô hình K-Means ở bước phân cụm chính không bị méo tâm cụm.
- Đóng vai trò là **Tầng lọc ngoại lai (Level 1)** trong kiến trúc mô hình lai 2 tầng của nhóm.
