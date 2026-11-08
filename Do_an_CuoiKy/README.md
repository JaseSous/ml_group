# Báo cáo giữa kỳ Máy học: Phân khúc khách hàng bằng RFM và các thuật toán phân cụm (Online Retail II)

## Thông tin học phần và nhóm thực hiện

- Trường: Đại học Sài Gòn (SGU), Khoa Công nghệ Thông tin
- Môn học: Máy học (Machine Learning)
- Lớp học phần: DCT124C1
- Giảng viên hướng dẫn: TS. Đỗ Như Tài
- Nhóm thực hiện: Nhóm 05
  1. Trương Thuận Phú (MSSV: 3124411234), nhóm trưởng
  2. Nguyễn Mạnh Thắng (MSSV: 3124411283)
  3. Nguyễn Hoàng Quân (MSSV: 3124411250)
  4. Phạm Minh Khôi (MSSV: 3124411135)

---

## 1. Giới thiệu đề tài và bộ dữ liệu

Trong bán lẻ trực tuyến, hiểu được hành vi khách hàng giúp doanh nghiệp tiết kiệm chi phí marketing và giữ chân khách tốt hơn (customer retention). Nhóm dùng học không giám sát (unsupervised learning) kết hợp mô hình RFM (Recency - Frequency - Monetary) để chia tập khách hàng lớn thành các cụm có hành vi gần nhau, rồi đề xuất cách chăm sóc riêng cho từng cụm.

- Tập dữ liệu: [Online Retail II (UCI Machine Learning Repository / Kaggle)](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- Quy mô: hơn 400.000 giao dịch thương mại điện tử thực tế, giai đoạn 2009 đến 2010.
- Ba thuộc tính RFM:
  - Recency ($R$): số ngày từ lần mua gần nhất của khách đến ngày mốc phân tích.
  - Frequency ($F$): tổng số hóa đơn khách đã thực hiện.
  - Monetary ($M$): tổng số tiền khách đã chi.

---

## 2. Cấu trúc thư mục

```text
ml_group/
│
├── data/                                 # Dữ liệu đã xử lý và kết quả
│   ├── online_retail_cleaned.csv         # Dữ liệu giao dịch đã làm sạch
│   ├── rfm_train.csv / rfm_val.csv / rfm_test.csv  # Bộ RFM chia Train/Val/Test
│   ├── RFM_Train_Segmented_Final.xlsx    # Kết quả phân cụm tập Train (kèm CustomerID và phân khúc)
│   └── RFM_Test_Segmented_Final.xlsx     # Kết quả phân cụm tập Test độc lập
│
├── figures/                              # Hình và biểu đồ gốc của đồ án
│   ├── fig00_ml_pipeline_architecture.png# Sơ đồ tổng quan pipeline
│   ├── fig01_eda_quantity_price_dist.png # Phân phối số lượng và đơn giá
│   ├── fig02_eda_boxplot_outliers.png    # Boxplot phát hiện ngoại lai
│   ├── fig03_eda_monthly_revenue.png     # Doanh thu theo tháng
│   ├── fig04_elbow_method_sse.png        # Đường cong Elbow để chọn K
│   ├── fig05_silhouette_scores_k.png     # Điểm Silhouette theo từng K
│   ├── fig06_model_comparison_metrics.png# So sánh Silhouette và Davies-Bouldin giữa các mô hình
│   ├── fig07_pca_2d_train_clusters.png   # 4 cụm trên PCA 2D
│   ├── fig08_rfm_cluster_profiles.png    # So sánh R-F-M giữa 4 phân khúc
│   └── fig09_gantt_progress_chart.png    # Tiến độ thực hiện đề tài
│
├── saved_models/                         # Mô hình đã huấn luyện
│   ├── kmeans_k4_model.joblib            # Tuned K-Means (K=4)
│   ├── scaler.joblib                     # StandardScaler fit trên tập Train
│   └── cluster_mapping.json              # Ánh xạ cụm sang tên phân khúc
│
├── Source/                               # Mã nguồn chia module theo hướng đối tượng (OOP)
│   ├── models/                           # Các lớp mô hình phân cụm
│   │   ├── base_model.py                 # Baseline K-Means
│   │   ├── kmeans_model.py               # Tuned K-Means và hàm dò K
│   │   ├── hierarchical_model.py         # Hierarchical Clustering (Ward linkage)
│   │   └── dbscan_model.py               # DBSCAN (dựa trên mật độ)
│   ├── logger.py                         # Ghi log thực nghiệm tự động
│   └── init.py                           # Cấu hình đường dẫn thư mục
│
├── Notebook.ipynb                        # Notebook chạy toàn bộ quy trình thực nghiệm
├── Notebook.html                         # Bản xuất HTML của Notebook
├── predict.py                            # Script dự đoán phân khúc độc lập (CLI)
├── Experiment_Log_Detailed.xlsx          # Nhật ký thực nghiệm chi tiết, có nhận xét
├── Experiment_Log_Comparison.csv         # Nhật ký thực nghiệm dạng CSV
├── requirements.txt                      # Thư viện phụ thuộc
├── Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.docx        # Báo cáo giữa kỳ (.docx)
├── Slide_Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.pptx  # Slide thuyết trình giữa kỳ (.pptx)
└── README.md
```

---

## 3. Cài đặt và chạy lại dự án

### Bước 1: Tạo môi trường ảo và cài thư viện

Cần Python 3.10 trở lên. Mở Terminal hoặc PowerShell tại thư mục gốc của dự án:

```bash
python -m venv venv
venv\Scripts\activate        # Windows; trên Linux/macOS dùng: source venv/bin/activate
pip install -r requirements.txt
```

### Bước 2: Chạy Notebook

```bash
jupyter notebook Notebook.ipynb
```

Chọn Run All Cells để chạy lại toàn bộ quy trình: EDA, tính RFM, huấn luyện 3 mô hình, tối ưu siêu tham số và vẽ PCA 2D.

### Bước 3: Dự đoán phân khúc bằng `predict.py`

Mô hình tốt nhất đã được lưu trong `saved_models/`, nên có thể phân khúc khách hàng mới mà không cần huấn luyện lại.

Một khách hàng:

```bash
python predict.py --recency 15 --frequency 8 --monetary 2500
```

Kết quả in ra phân khúc tương ứng, ví dụ Potential Loyalists.

Nhiều khách hàng từ file CSV:

```bash
python predict.py --file data/rfm_test.csv --output data/predictions_test.csv
```

---

## 4. Kết quả thực nghiệm

Nhóm so sánh 3 thuật toán phân cụm là K-Means, Hierarchical Clustering (Agglomerative) và DBSCAN. Dữ liệu Train được chuẩn hóa bằng `StandardScaler`, độ ổn định được kiểm tra thêm trên tập Validation.

| STT | Mô hình | Tham số | Silhouette | Davies-Bouldin | Calinski-Harabasz | Nhận xét |
| :-: | :--- | :--- | :-: | :-: | :-: | :--- |
| 1 | Baseline K-Means | $K=3$, chưa tinh chỉnh | 0.3298 | 1.0709 | 2199.32 | Mốc tham chiếu |
| 2 | Hierarchical Clustering | $K=4$, linkage='ward' | 0.2976 | 1.0827 | 1808.38 | Phân tách kém hơn K-Means |
| 3 | DBSCAN | $\varepsilon=0.6$, $min\_pts=10$ | 0.5254* | 0.4055* | 117.32 | Chỉ số cao nhưng không đáng tin: 95% điểm nằm trong một cụm |
| 4 | Tuned K-Means | $K=2$ | 0.4224 | 0.9119 | 2614.55 | Chỉ số tốt nhất nhưng chỉ có 2 nhóm, quá thô |
| 5 | **Tuned K-Means (chọn)** | **$K=4$** | 0.3385 | 0.9960 | 2090.80 | Cho 4 phân khúc dễ diễn giải |
| 6 | Tuned DBSCAN | $\varepsilon=0.3$, $min\_pts=5$ | 0.0242 | 1.1821 | 341.22 | Vỡ thành 13 cụm và 224 điểm nhiễu |
| 7 | Validation | $K=4$, 684 khách hàng | 0.3193 | 1.0210 | 503.80 | Gần với kết quả trên Train, không thấy dấu hiệu overfit |

\* Hai chỉ số này cao vì gần như toàn bộ điểm bị gom vào một cụm, không phản ánh chất lượng phân cụm.

Nhóm chọn Tuned K-Means với $K=4$. $K=2$ có Silhouette cao hơn (0.4224 so với 0.3385) nhưng chỉ tách được hai nhóm lớn, không đủ để làm chiến lược marketing riêng. $K=4$ cho bốn nhóm hành vi đủ khác nhau để áp dụng cách chăm sóc khác nhau. Trên tập Validation, Silhouette chỉ giảm nhẹ xuống 0.3193.

---

## 5. Bốn phân khúc khách hàng và chiến lược đề xuất

| Cụm | Phân khúc | Đặc trưng RFM | Tỷ lệ | Chiến lược đề xuất |
| :-: | :--- | :--- | :-: | :--- |
| 1 | Champions (khách VIP) | $R$ rất thấp (mới mua), $F$ cao nhất, $M$ lớn nhất | ~18 - 27% | Giữ chân bằng đặc quyền: thẻ VIP, quà sinh nhật cá nhân hóa, được trải nghiệm sản phẩm mới sớm. Tránh giảm giá đại trà. |
| 3 | Potential Loyalists (tiềm năng) | Mới mua gần đây, $F$ và $M$ ở mức khá | ~21 - 25% | Tăng tần suất mua: gợi ý sản phẩm mua kèm (cross-sell, up-sell), voucher cho đơn kế tiếp, mời tham gia tích điểm. |
| 0 | At Risk (nguy cơ rời bỏ) | Trước đây mua tốt nhưng $R$ rất cao (hơn 180 ngày chưa quay lại) | ~24 - 32% | Kéo khách quay lại (win-back): gửi email cá nhân hóa kiểu "Chúng tôi nhớ bạn" kèm mã giảm giá riêng, trước khi khách chuyển sang đối thủ. |
| 2 | Lost / Hibernating (đã rời bỏ) | Rất lâu không mua, $F$ và $M$ rất thấp | ~20 - 25% | Tiết kiệm ngân sách: không tốn SMS hay telesale cho từng người, chỉ tiếp cận qua quảng cáo mạng xã hội diện rộng với chi phí thấp. |

---

## 6. Sản phẩm bàn giao

1. `Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.docx`: báo cáo chi tiết (20+ trang).
2. `Slide_Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.pptx`: slide thuyết trình.
3. `Notebook.ipynb` và `Notebook.html`: mã nguồn thực nghiệm và trực quan hóa.
4. `Experiment_Log_Detailed.xlsx`: nhật ký thực nghiệm chi tiết.
5. `figures/`: hơn 10 biểu đồ gốc.
6. `saved_models/` và `predict.py`: mô hình đã huấn luyện và script dự đoán.