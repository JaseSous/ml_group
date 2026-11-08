# BÁO CÁO GIỮA KỲ MÔN HỌC MÁY HỌC (MACHINE LEARNING)
## Đề tài: Phân Khúc Khách Hàng Bằng Mô Hình RFM và Hành Vi Mua Hàng Qua Các Thuật Toán Phân Cụm (Online Retail II)

---

### 🏫 THÔNG TIN HỌC PHẦN & NHÓM THỰC HIỆN
- **Cơ sở đào tạo:** Trường Đại học Sài Gòn (SGU) - Khoa Công nghệ Thông tin
- **Môn học:** Máy học (Machine Learning)
- **Lớp học phần:** DCT124C1
- **Giảng viên hướng dẫn:** TS. Đỗ Như Tài
- **Nhóm thực hiện:** Nhóm 05
  1. **Trương Thuận Phú** (MSSV: 3124411234) - *Nhóm trưởng*
  2. **Nguyễn Mạnh Thắng** (MSSV: 3124411283)
  3. **Nguyễn Hoàng Quân** (MSSV: 3124411250)
  4. **Phạm Minh Khôi** (MSSV: 3124411135)

---

## 📌 1. Giới Thiệu Đề Tài & Bộ Dữ Liệu
Trong kinh doanh bán lẻ trực tuyến (E-Commerce), việc thấu hiểu hành vi khách hàng là yếu tố sống còn để tối ưu hóa chi phí tiếp thị và gia tăng tỷ lệ giữ chân khách hàng (Customer Retention). Đề tài này ứng dụng kỹ thuật **Học không giám sát (Unsupervised Machine Learning)** kết hợp với mô hình định lượng hành vi **RFM (Recency - Frequency - Monetary)** để tự động phân nhóm tập khách hàng lớn thành các cụm đồng nhất, hỗ trợ doanh nghiệp đưa ra chiến lược kinh doanh chính xác.

- **Tập dữ liệu:** [Online Retail II Dataset (UCI Machine Learning Repository / Kaggle)](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- **Quy mô:** Hơn 400.000 giao dịch thương mại điện tử thực tế từ 2009 đến 2010.
- **Thuộc tính RFM:**
  - **Recency ($R$):** Số ngày kể từ lần giao dịch gần nhất của khách hàng đến ngày mốc phân tích.
  - **Frequency ($F$):** Tổng số hóa đơn/giao dịch mà khách hàng đã thực hiện.
  - **Monetary ($M$):** Tổng số tiền tích lũy khách hàng đã chi tiêu.

---

## 🏗️ 2. Kiến Trúc Cấu Trúc Thư Mục (Project Structure)

```text
G:\ml_group\
│
├── data/                                 # Thư mục chứa dữ liệu xử lý và kết quả
│   ├── online_retail_cleaned.csv         # Dữ liệu giao dịch đã làm sạch
│   ├── rfm_train.csv / rfm_val.csv / rfm_test.csv  # Bộ dữ liệu RFM phân tách Train/Val/Test
│   ├── RFM_Train_Segmented_Final.xlsx    # Kết quả phân cụm tập Train (kèm CustomerID & Phân khúc)
│   └── RFM_Test_Segmented_Final.xlsx     # Kết quả phân cụm tập Test độc lập
│
├── figures/                              # Toàn bộ hình ảnh & biểu đồ gốc của đồ án
│   ├── fig00_ml_pipeline_architecture.png# Sơ đồ quy trình tổng quan Pipeline Machine Learning
│   ├── fig01_eda_quantity_price_dist.png # Phân phối số lượng và đơn giá
│   ├── fig02_eda_boxplot_outliers.png    # Biểu đồ Boxplot phát hiện ngoại lai
│   ├── fig03_eda_monthly_revenue.png     # Biến động doanh thu theo tháng
│   ├── fig04_elbow_method_sse.png        # Biểu đồ đường cong Elbow tìm K tối ưu
│   ├── fig05_silhouette_scores_k.png     # Biểu đồ điểm Silhouette theo từng K
│   ├── fig06_model_comparison_metrics.png# So sánh Silhouette & Davies-Bouldin giữa các model
│   ├── fig07_pca_2d_train_clusters.png   # Trực quan hóa phân tách 4 cụm qua PCA 2D
│   ├── fig08_rfm_cluster_profiles.png    # So sánh các chỉ số R-F-M giữa 4 phân khúc
│   └── fig09_gantt_progress_chart.png    # Biểu đồ tiến độ thực hiện đề tài
│
├── saved_models/                         # Lưu trữ mô hình đã huấn luyện (Model Persistence)
│   ├── kmeans_k4_model.joblib            # Trọng số mô hình Tuned K-Means (K=4)
│   ├── scaler.joblib                     # Bộ chuẩn hóa StandardScaler fit trên Train Set
│   └── cluster_mapping.json              # Từ điển định danh phân khúc khách hàng
│
├── Source/                               # Mã nguồn module hóa theo hướng đối tượng (OOP)
│   ├── models/                           # Các lớp mô hình phân cụm kế thừa
│   │   ├── base_model.py                 # Baseline K-Means
│   │   ├── kmeans_model.py               # Tuned K-Means & hàm dò tìm K
│   │   ├── hierarchical_model.py         # Hierarchical Clustering (Ward linkage)
│   │   └── dbscan_model.py               # DBSCAN Clustering (Density-based)
│   ├── logger.py                         # Module ghi nhận log thực nghiệm tự động
│   └── init.py                           # Cấu hình đường dẫn thư mục
│
├── Notebook.ipynb                        # Jupyter Notebook chạy toàn bộ quy trình thực nghiệm
├── Notebook.html                         # Bản xuất HTML đầy đủ của Notebook
├── predict.py                            # Script chạy dự đoán phân cụm độc lập (CLI)
├── Experiment_Log_Detailed.xlsx          # Bảng nhật ký thực nghiệm chi tiết có nhận xét chuyên môn
├── Experiment_Log_Comparison.csv         # Nhật ký thực nghiệm dạng CSV
├── requirements.txt                      # Danh sách thư viện phụ thuộc của dự án
├── Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.docx # File Báo cáo giữa kỳ (.docx)
├── Slide_Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.pptx # Slide thuyết trình giữa kỳ (.pptx)
└── README.md                             # Hướng dẫn chi tiết dự án
```

---

## ⚙️ 3. Hướng Dẫn Cài Đặt & Chạy Lại Dự Án

### Bước 1: Khởi tạo môi trường ảo và cài đặt thư viện
Yêu cầu Python 3.10 trở lên. Mở Terminal / PowerShell tại thư mục gốc của dự án:

```bash
# Cài đặt toàn bộ thư viện cần thiết
pip install -r requirements.txt
```

### Bước 2: Chạy toàn bộ luồng thực nghiệm trên Notebook
Khởi chạy Jupyter Notebook hoặc JupyterLab:
```bash
jupyter notebook Notebook.ipynb
```
Chọn **Run All Cells** để tái lập lại toàn bộ quy trình từ Khám phá dữ liệu (EDA), Tính toán chỉ số RFM, Huấn luyện 3 mô hình, Tối ưu siêu tham số đến Trực quan hóa PCA 2D.

### Bước 3: Sử dụng Script dự đoán phân khúc độc lập (`predict.py`)
Mô hình tối ưu đã được đóng gói sẵn trong `saved_models/`. Bạn có thể sử dụng script `predict.py` để phân khúc khách hàng mới mà không cần train lại:

- **Dự đoán cho 1 khách hàng cụ thể:**
  ```bash
  python predict.py --recency 15 --frequency 8 --monetary 2500
  ```
  *Kết quả in trực tiếp phân khúc tương ứng (Ví dụ: Potential Loyalists).*

- **Dự đoán hàng loạt từ file dữ liệu CSV:**
  ```bash
  python predict.py --file data/rfm_test.csv --output data/predictions_test.csv
  ```

---

## 📊 4. Tóm Tắt Kết Quả Thực Nghiệm

Nhóm đã khảo sát và so sánh 3 thuật toán phân cụm chính: **K-Means**, **Hierarchical Clustering (Agglomerative)** và **DBSCAN** trên tập Train đã chuẩn hóa (`StandardScaler`), đồng thời kiểm định độ ổn định trên tập Validation:

| STT | Thuật toán / Mô hình | Cấu hình tham số | Silhouette Score | Davies-Bouldin | Calinski-Harabasz | Đánh giá & Kết luận |
| :-: | :--- | :--- | :-: | :-: | :-: | :--- |
| 1 | Baseline K-Means | $K=3$, untuned | 0.3298 | 1.0709 | 2199.32 | Tham chiếu cơ sở |
| 2 | Hierarchical Clustering | $K=4$, linkage='ward' | 0.2976 | 1.0827 | 1808.38 | Độ phân tách kém hơn K-Means |
| 3 | DBSCAN | $\varepsilon=0.6, min\_pts=10$ | 0.5254* | 0.4055* | 117.32 | Chỉ số ảo (gom 95% vào 1 cụm) |
| 4 | Tuned K-Means | $K=2$ | 0.4224 | 0.9119 | 2614.55 | Tối ưu toán học nhưng quá thô |
| **5** | **Tuned K-Means (CHỌN)** | **$K=4$** | **0.3385** | **0.9960** | **2090.80** | **Tối ưu nghiệp vụ bán lẻ (4 phân khúc rõ nét)** |
| 6 | Tuned DBSCAN | $\varepsilon=0.3, min\_pts=5$ | 0.0242 | 1.1821 | 341.22 | Phân mảnh 13 cụm và 224 điểm nhiễu |
| **7** | **Validation Test** | **$K=4$ trên 684 khách hàng** | **0.3193** | **1.0210** | **503.80** | **Độ ổn định cao, không bị Overfitting** |

> **Quyết định lựa chọn:** Nhóm thống nhất lựa chọn **Tuned K-Means ($K=4$)**. Mặc dù $K=2$ cho Silhouette Score cao hơn, nhưng $K=4$ là sự đánh đổi khoa học hợp lý để phân định 4 nhóm hành vi khách hàng phục vụ trực tiếp cho hoạt động kinh doanh.

---

## 👥 5. Định Danh 4 Phân Khúc & Chiến Lược Marketing Đề Xuất

| Cụm | Tên Phân Khúc (Segment Name) | Đặc trưng hành vi RFM | Tỷ lệ (%) | Chiến lược Marketing & Chăm sóc khách hàng |
| :-: | :--- | :--- | :-: | :--- |
| **1** | **Champions (Khách VIP)** | $R$ rất thấp (gần đây), $F$ cao vượt trội, $M$ lớn nhất. | ~18 - 27% | **Tri ân & Giữ chân đặc quyền:** Cấp thẻ hội viên VIP, quà sinh nhật cá nhân hóa, quyền truy cập trải nghiệm sớm sản phẩm mới; không spam giảm giá đại trà. |
| **3** | **Potential Loyalists (Tiềm năng)** | Mới mua gần đây, tần suất và chi tiêu ở mức khá. | ~21 - 25% | **Kích thích tần suất:** Gợi ý sản phẩm mua kèm (Cross-sell / Up-sell), cấp voucher giảm giá cho đơn hàng tiếp theo, mời gia nhập chương trình tích điểm. |
| **0** | **At Risk (Nguy cơ rời bỏ)** | Trước đây mua tốt nhưng $R$ rất cao (> 180 ngày chưa quay lại). | ~24 - 32% | **Chiến dịch tái kích hoạt (Win-back):** Gửi email cá nhân hóa *"Chúng tôi nhớ bạn"*, tặng mã giảm giá đặc biệt để lôi kéo quay lại trước khi chuyển sang đối thủ. |
| **2** | **Lost / Hibernating (Đã rời bỏ)** | Đã rất lâu không mua sắm, tần suất và giá trị đơn hàng rất thấp. | ~20 - 25% | **Tối ưu ngân sách:** Không dồn chi phí gửi SMS / Telesale riêng lẻ; chỉ tiếp cận thông qua quảng cáo mạng xã hội diện rộng với chi phí thấp. |

---

## 📦 6. Danh Mục Sản Phẩm Bàn Giao
1. `Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.docx` - Báo cáo khoa học chi tiết (20+ trang).
2. `Slide_Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.pptx` - Slide báo cáo thuyết trình.
3. `Notebook.ipynb` & `Notebook.html` - Toàn bộ mã nguồn thực nghiệm và trực quan hóa.
4. `Experiment_Log_Detailed.xlsx` - Bảng nhật ký thực nghiệm chi tiết theo quy chuẩn.
5. `figures/` - Thư mục chứa toàn bộ 10+ hình ảnh biểu đồ gốc độ phân giải cao.
6. `saved_models/` & `predict.py` - Trọng số mô hình đã huấn luyện và script dự đoán sẵn sàng triển khai.
