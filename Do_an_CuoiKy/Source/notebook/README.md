# Thư mục Source/notebook - Mô hình Baseline & Rút trích RFM

Thư mục này chứa toàn bộ các Jupyter Notebook phục vụ thực nghiệm mô hình phân cụm cơ sở (**Baseline Models**) trên dữ liệu giao dịch sạch cơ bản, notebook đối chuẩn tổng kết (**note_baseline**), và notebook rút trích đặc trưng chuyên sâu (**RFM Feature Engineering**).

---

## 1. Cấu trúc và Danh sách các Notebook

```text
Source/notebook/
├── KMeans_baseline.ipynb         # Mô hình 1: K-Means Baseline (K=3, data clean)
├── Hierarchical_baseline.ipynb   # Mô hình 2: Hierarchical Baseline (K=4, Ward, data clean)
├── DBSCAN_baseline.ipynb         # Mô hình 3: DBSCAN Baseline (eps=0.5, min_samples=10, data clean)
├── note_baseline.ipynb           # Báo cáo tổng kết, đối chuẩn số liệu & chọn model Baseline tối ưu
├── RFM.ipynb                     # Rút trích đặc trưng RFM, Skewness & chia tập RFM Train/Val/Test
├── KMeans_RFM.ipynb              # Mô hình K-Means nâng cao trên bộ đặc trưng RFM (Tuned K=4)
├── Hierarchical_RFM.ipynb        # Mô hình Hierarchical nâng cao trên bộ đặc trưng RFM (Ward, K=4)
├── DBSCAN_RFM.ipynb              # Mô hình DBSCAN trên bộ đặc trưng RFM (Tìm k & eps qua k-distance)
└── README.md                     # Tài liệu hướng dẫn chi tiết thư mục
```

### Bảng chi tiết chức năng từng Notebook:

| STT | Notebook | Nội dung chính | Dữ liệu đầu vào | Dữ liệu đầu ra |
| :---: | :--- | :--- | :--- | :--- |
| 1 | [KMeans_baseline.ipynb](file:///c:/Users/Quân/Desktop/ml_group/Source/notebook/KMeans_baseline.ipynb) | **Mô hình 1: K-Means Baseline:**<br>• Huấn luyện $K=3$ trên 3 thuộc tính giao dịch cơ bản (`Quantity`, `UnitPrice`, `TotalPrice`).<br>• Đánh giá trên cả 3 tập **Train (251K)**, **Validation (72K)**, **Test (74K)**.<br>• Phân tích thuộc tính chi phối (ANOVA F-Score) & trực quan PCA 2D. | `data/train.csv`<br>`data/valid.csv`<br>`data/test.csv` | Ghi log vào `Experiment_Log_Comparison.csv` |
| 2 | [Hierarchical_baseline.ipynb](file:///c:/Users/Quân/Desktop/ml_group/Source/notebook/Hierarchical_baseline.ipynb) | **Mô hình 2: Hierarchical Baseline:**<br>• Huấn luyện phân cụm thứ bậc $K=4$ (Ward Linkage) trên mẫu Train.<br>• Vẽ Dendrogram mẫu minh họa cây phân cấp.<br>• Dự đoán trên Validation và Test bằng `NearestCentroid`.<br>• Phân tích thuộc tính chi phối & trực quan PCA 2D. | `data/train.csv`<br>`data/valid.csv`<br>`data/test.csv` | Ghi log vào `Experiment_Log_Comparison.csv` |
| 3 | [DBSCAN_baseline.ipynb](file:///c:/Users/Quân/Desktop/ml_group/Source/notebook/DBSCAN_baseline.ipynb) | **Mô hình 3: DBSCAN Baseline:**<br>• Huấn luyện phân cụm mật độ `eps=0.5`, `min_samples=10` trên mẫu Train.<br>• Đồ thị $k$-distance khảo sát bán kính $\epsilon$.<br>• Tách lọc giao dịch ngoại lai (Noise); kiểm thử Validation và Test qua Core Samples.<br>• Phân tích thuộc tính chi phối & trực quan PCA 2D. | `data/train.csv`<br>`data/valid.csv`<br>`data/test.csv` | Ghi log vào `Experiment_Log_Comparison.csv` |
| 4 | [note_baseline.ipynb](file:///c:/Users/Quân/Desktop/ml_group/Source/notebook/note_baseline.ipynb) | **Notebook tổng kết & Đối chuẩn Baseline:**<br>• Tổng hợp bảng so sánh số liệu đối chuẩn 3 mô hình trên Train/Val/Test.<br>• Biểu đồ cột nhóm so sánh Silhouette và Davies-Bouldin.<br>• So sánh tỷ lệ % đóng góp của thuộc tính giữa 3 mô hình.<br>• Luận cứ khoa học lựa chọn **K-Means** là mô hình tốt nhất ở mức Baseline. | Toàn bộ 3 mô hình Baseline | Quyết định chọn mô hình tối ưu |
| 5 | [RFM.ipynb](file:///c:/Users/Quân/Desktop/ml_group/Source/notebook/RFM.ipynb) | **Rút trích đặc trưng RFM chuyên sâu:**<br>• Tính bộ 3 chỉ số Recency ($R$), Frequency ($F$), Monetary ($M$) theo từng `CustomerID`.<br>• Khám phá phân phối Skewness & biến đổi Log `np.log1p`.<br>• Phân chia Train 64% / Val 16% / Test 20% độc lập.<br>• Chuẩn hóa `StandardScaler` (fit duy nhất trên Train chống Data Leakage). | `data/data_clean.csv` | `data/rfm_data.csv`<br>`data/rfm_train.csv`<br>`data/rfm_val.csv`<br>`data/rfm_test.csv` |
| 6 | [KMeans_RFM.ipynb](file:///c:/Users/Quân/Desktop/ml_group/Source/notebook/KMeans_RFM.ipynb) | **K-Means trên bộ đặc trưng RFM (Tuned K=4):**<br>• Tìm $K$ tối ưu qua phương pháp Elbow và Silhouette ($K \in [2, 10]$).<br>• Huấn luyện $K=4$ trên Train, kiểm định trên Validation và Test.<br>• Phân tích mức độ chi phối thuộc tính (ANOVA F-Score: $F$ 39.1%, $R$ 30.5%, $M$ 30.4%).<br>• Xác lập chân dung 4 phân khúc (VIP, Tiềm năng, Nguy cơ, Rời bỏ) và chiến lược Marketing. | `data/rfm_train.csv`<br>`data/rfm_val.csv`<br>`data/rfm_test.csv` | Ghi log vào `Experiment_Log_Comparison.csv` và `Experiment_Log_Detailed.xlsx` |
| 7 | [Hierarchical_RFM.ipynb](file:///c:/Users/Quân/Desktop/ml_group/Source/notebook/Hierarchical_RFM.ipynb) | **Hierarchical trên bộ đặc trưng RFM (Ward, K=4):**<br>• Khảo sát cây phả hệ qua Dendrogram và các chỉ số Silhouette/DB trên $K \in [2, 8]$.<br>• Huấn luyện $K=4$ trên 100% dữ liệu RFM Train (không cần lấy mẫu).<br>• Đánh giá trên Validation và Test qua `NearestCentroid`.<br>• Phân tích ANOVA F-Score, chân dung 4 phân khúc và đối chiếu với K-Means. | `data/rfm_train.csv`<br>`data/rfm_val.csv`<br>`data/rfm_test.csv` | Ghi log vào `Experiment_Log_Comparison.csv` và `Experiment_Log_Detailed.xlsx` |
| 8 | [DBSCAN_RFM.ipynb](file:///c:/Users/Quân/Desktop/ml_group/Source/notebook/DBSCAN_RFM.ipynb) | **DBSCAN trên bộ đặc trưng RFM:**<br>• Tìm $k$ và bán kính $\epsilon$ tối ưu qua đồ thị $k$-distance (K-NN distances với $k \in \{4, 6, 10\}$).<br>• Huấn luyện DBSCAN với tham số tối ưu ($k=10, \epsilon=0.6$).<br>• Tách lọc khách hàng ngoại lai (Noise/Outliers gồm nhóm Siêu VIP và Dị biệt).<br>• Kiểm định trên Validation và Test qua Nearest Core Sample.<br>• Phân tích ANOVA F-Score, chân dung nhóm Noise và đối chiếu với K-Means. | `data/rfm_train.csv`<br>`data/rfm_val.csv`<br>`data/rfm_test.csv` | Ghi log vào `Experiment_Log_Comparison.csv` và `Experiment_Log_Detailed.xlsx` |

---

## 2. Phương pháp luận Mô hình Baseline trên Dữ liệu Sạch Cơ bản

### 2.1. Tại sao chỉ sử dụng `Quantity`, `UnitPrice`, `TotalPrice`?
- Thuật toán phân cụm (đặc biệt là K-Means và Hierarchical) dựa trên **khoảng cách hình học Euclid** trong không gian $n$ chiều:
  $$d(x, y) = \sqrt{\sum (x_i - y_i)^2}$$
- Phép tính này **chỉ có ý nghĩa trên các biến số thực đo lường được (Numerical Variables)** mang ý nghĩa về quy mô và giá trị.
- Các cột còn lại trong dữ liệu giao dịch:
  - `CustomerID`, `InvoiceNo`, `StockCode`: Là các mã định danh (Identifier/Key), không có ý nghĩa toán học về độ lớn hay thứ tự.
  - `Description`: Dạng văn bản tự do (Text), cần các kỹ thuật NLP phức tạp.
  - `InvoiceDate`: Dạng thời gian (Datetime), cần chuyển đổi thành số ngày (chính là $R$ trong RFM).
  - `Country`: Dạng phân loại (Categorical), hơn 90% là United Kingdom nên gây thưa thớt dữ liệu.
- Vì vậy, `Quantity`, `UnitPrice` và `TotalPrice` là **3 thuộc tính số cơ bản duy nhất** phản ánh quy mô giao dịch thô ban đầu để xây dựng mốc đối chuẩn (Benchmark).

### 2.2. Đánh giá mức độ chi phối của thuộc tính (Feature Importance)
Trong mỗi notebook baseline, chúng tôi tích hợp kiểm định **ANOVA F-Score (`f_classif`)** để xác định mô hình gom cụm dựa trên thuộc tính nào nhiều nhất:
- **K-Means Baseline:** `UnitPrice` (44.80%) $\rightarrow$ `Quantity` (38.48%) $\rightarrow$ `TotalPrice` (16.72%).
- **Hierarchical Baseline:** `TotalPrice` (39.86%) $\rightarrow$ `UnitPrice` (30.08%) $\rightarrow$ `Quantity` (30.06%).
- **DBSCAN Baseline:** `UnitPrice` (53.11%) $\rightarrow$ `Quantity` (29.91%) $\rightarrow$ `TotalPrice` (16.98%).

---

## 3. Bảng tổng hợp số liệu thực nghiệm Baseline trên 3 Tập dữ liệu

| Thuật toán | Cấu hình Baseline | Tập dữ liệu | Silhouette Score (↑) | Davies-Bouldin (↓) | Calinski-Harabasz (↑) | Tỷ lệ Nhiễu / Mẫu | Thời gian chạy |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **K-Means** | $K=3$, `init='k-means++'`, `seed=42` | **Train (64%)** | **0.6244** | **0.6626** | **150,925.86** | 0% (251,501 mẫu) | **~0.52s** |
| | | **Validation (16%)** | **0.6175** | **0.6215** | **46,703.92** | 0% (72,685 mẫu) | ~0.15s |
| | | **Test (20%)** | **0.6417** | **0.6040** | **46,310.08** | 0% (74,785 mẫu) | ~0.15s |
| **Hierarchical** | $K=4$, `linkage='ward'` | **Train (64%)** | 0.6258 | 0.6843 | 3,130.95 | 0% (5,000 mẫu) | ~0.34s (mẫu) |
| *(Agglomerative)* | | **Validation (16%)** | 0.6346 | 0.5358 | 2,633.77 | 0% (5,000 mẫu) | ~0.18s |
| | | **Test (20%)** | 0.6566 | 0.6074 | 2,903.95 | 0% (5,000 mẫu) | ~0.18s |
| **DBSCAN** | `eps=0.5`, `min_samples=10` | **Train (64%)** | 0.6440\* | 0.3666 | 963.99 | **1.71% nhiễu** | ~0.50s (mẫu) |
| *(Density-Based)* | | **Validation (16%)** | 0.6413\* | 0.3407 | 469.99 | **1.94% nhiễu** | ~0.20s |
| | | **Test (20%)** | 0.6600\* | 0.4015 | 473.31 | **0.94% nhiễu** | ~0.20s |

*\*Lưu ý: Chỉ số Silhouette và Davies-Bouldin của DBSCAN chỉ tính trên các cụm mật độ hợp lệ (loại trừ điểm nhiễu mang nhãn -1).*

---

## 4. Kết luận: Lựa chọn mô hình tối ưu ở mức Baseline

> ### 🏆 Mô hình chiến thắng ở mức Baseline: **K-MEANS CLUSTERING ($K=3$)**

**4 Lý do khoa học và thực tiễn:**
1. **Khả năng mở rộng và tốc độ (Scalability):** Xử lý trọn vẹn 100% dữ liệu (251,501 dòng) chỉ mất **0.52 giây**; trong khi Hierarchical bị quá tải bộ nhớ $O(N^2)$ (cần ~500 GB RAM nếu không down-sample).
2. **Độ ổn định và khả năng tổng quát hóa cao:** Điểm Silhouette giữ vững > 0.61 qua cả 3 tập (Train $\rightarrow$ Val $\rightarrow$ Test), chỉ số Davies-Bouldin trên tập Test đạt mức tối ưu nhất ($0.6040$).
3. **Chỉ số Calinski-Harabasz áp đảo:** Đạt trên **150,000 điểm** (vượt trội hoàn toàn so với 3,130 của Hierarchical và 963 của DBSCAN).
4. **Phân khúc kinh doanh cân đối:** Không bị hiện tượng một cụm nuốt chửng 98% dữ liệu như DBSCAN, mà phân tách rõ 3 nhóm giao dịch có ý nghĩa thực tiễn.

---

## 5. Quy trình thực thi logic giữa các Notebook

Để chạy lại toàn bộ quy trình một cách chuẩn xác trên VS Code:
1. **Bước 1:** Mở `EDA/EDA.ipynb` để làm sạch và xuất các file `data/data_clean.csv`, `data/train.csv`, `data/valid.csv`, `data/test.csv`.
2. **Bước 2:** Mở và chạy lần lượt 3 notebook baseline:
   - `Source/notebook/KMeans_baseline.ipynb`
   - `Source/notebook/Hierarchical_baseline.ipynb`
   - `Source/notebook/DBSCAN_baseline.ipynb`
3. **Bước 3:** Mở `Source/notebook/note_baseline.ipynb` để xem báo cáo so sánh đối chuẩn tổng thể và kết luận chọn model Baseline tốt nhất.
4. **Bước 4:** Mở `Source/notebook/RFM.ipynb` để tiến hành Feature Engineering bộ chỉ số RFM (chuẩn bị dữ liệu cho các mô hình phân cụm nâng cao).
5. **Bước 5:** Mở `Source/notebook/KMeans_RFM.ipynb` để tìm $K$ tối ưu (Elbow, Silhouette) và huấn luyện mô hình K-Means nâng cao trên bộ chỉ số RFM.
6. **Bước 6:** Mở `Source/notebook/Hierarchical_RFM.ipynb` để khảo sát Dendrogram, tìm số cụm tối ưu và huấn luyện phân cụm thứ bậc Agglomerative ($K=4$, Ward).
7. **Bước 7:** Mở `Source/notebook/DBSCAN_RFM.ipynb` để tìm $k$ và $\epsilon$ tối ưu qua đồ thị $k$-distance, huấn luyện DBSCAN và phân tích nhóm khách hàng dị biệt/ngoại lai (Noise).
