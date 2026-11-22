# Thư mục EDA - Kiến trúc Mô-đun 3 Tầng: Khám phá, Tiền xử lý & Trích xuất Đặc trưng

Thư mục `EDA` được chuẩn hóa và tách biệt thành **3 phân hệ (folders) chuyên biệt**, tạo thành luồng pipeline xử lý dữ liệu hoàn chỉnh trước khi chuyển giao sang bước huấn luyện mô hình học máy:

---

## 1. Cấu trúc thư mục mới

```text
EDA/
├── 01_EDA/                           # Phân hệ 1: Khám phá & Mô tả dữ liệu
│   ├── EDA.ipynb                     # Notebook khảo sát phân phối, thiếu, trùng, ngoại lai, doanh thu
│   ├── figures/                      # Thư mục lưu toàn bộ biểu đồ EDA (PNG 300 DPI)
│   └── outputs/                      # Bảng thống kê mô tả, ngoại lai IQR, top sản phẩm/quốc gia
│
├── 02_Tien_xu_ly/                    # Phân hệ 2: Tiền xử lý & Làm sạch dữ liệu giao dịch
│   ├── Tien_xu_ly.ipynb              # Notebook làm sạch, khử đơn hủy, tính TotalPrice, chia Train/Val/Test
│   ├── figures/                      # Thư mục lưu biểu đồ phễu làm sạch & phân chia tập dữ liệu
│   └── outputs/                      # Báo cáo pipeline, bảng đối chiếu trước/sau làm sạch
│
├── 03_Dac_trung/                     # Phân hệ 3: Rút trích & Biến đổi đặc trưng RFM
│   ├── Dac_trung.ipynb               # Notebook trích xuất Recency, Frequency, Monetary, log1p & StandardScaler
│   ├── figures/                      # Thư mục lưu biểu đồ phân phối RFM, tương quan & không gian 3D
│   └── outputs/                      # Bảng thống kê skewness, ma trận tương quan RFM
│
├── EDA.ipynb                         # [Bản lưu trữ gốc] Notebook EDA tổng hợp trước khi tách
└── README.md                         # Tài liệu hướng dẫn chi tiết luồng xử lý
```

---

## 2. Chi tiết từng phân hệ và chức năng các Cell xuất file

Trong mỗi thư mục phân hệ đều có 1 file `.ipynb` tương ứng và được tích hợp sẵn:
1. **Cell xuất tất cả kết quả ra file**: Tự động kết xuất toàn bộ bảng số liệu thống kê, dữ liệu sạch / đặc trưng (`.csv`) và báo cáo tổng kết (`.txt`).
2. **Cell xuất tất cả các ảnh biểu đồ ra file**: Tự động kết xuất toàn bộ hình ảnh biểu đồ trực quan hóa chuẩn xuất bản (`.png`, 300 DPI) vào thư mục `figures/` của module và đồng bộ sang thư mục `figures/` dùng chung của đề tài.

### 📌 Phân hệ 1: `01_EDA` (`EDA.ipynb`)
- **Mục tiêu:** Khám phá cấu trúc dữ liệu ban đầu, kiểm tra tính toàn vẹn (Missing, Duplicates, Negative values), đo lường ngoại lai bằng IQR/Boxplot, phân tích xu hướng doanh thu theo tháng và thị trường.
- **Cell xuất kết quả ra file:** Xuất vào thư mục `01_EDA/outputs/`:
  - `eda_descriptive_statistics.csv`: Bảng thống kê mô tả toàn diện các cột.
  - `eda_missing_and_duplicates.csv`: Thống kê giá trị thiếu và trùng lặp.
  - `eda_outliers_iqr.csv`: Bảng ngưỡng phân vị Q1, Q3, IQR và số lượng ngoại lai.
  - `eda_correlation_matrix.csv`: Ma trận tương quan giữa Quantity, Price, TotalPrice.
  - `eda_monthly_revenue.csv`: Doanh thu tổng hợp theo từng tháng.
  - `eda_top10_products.csv`: Top 10 sản phẩm bán chạy nhất.
  - `eda_top10_countries.csv`: Top 10 thị trường có lượng giao dịch lớn nhất.
  - `eda_summary_report.txt`: Báo cáo tóm tắt tổng hợp các phát hiện chính từ EDA.
- **Cell xuất ảnh biểu đồ ra file:** Xuất vào `01_EDA/figures/` và `figures/`:
  - `fig01_eda_quantity_price_dist.png`
  - `fig02_eda_boxplot_outliers.png`
  - `fig03_eda_monthly_revenue.png`
  - `fig_eda_correlation_heatmap.png`
  - `fig_eda_top_products.png`
  - `fig_eda_top_countries.png`

---

### 📌 Phân hệ 2: `02_Tien_xu_ly` (`Tien_xu_ly.ipynb`)
- **Mục tiêu:** Khử trùng lặp, lọc bỏ dòng thiếu `CustomerID`, chuẩn hóa định dạng ngày giờ và tên cột, loại bỏ đơn hủy/hoàn (`Quantity <= 0` hoặc `UnitPrice <= 0`), tính toán `TotalPrice`, và **phân chia giao dịch theo tập CustomerID duy nhất (Train 64% / Val 16% / Test 20%)** nhằm triệt để chống rò rỉ dữ liệu (Anti-Data Leakage).
- **Cell xuất kết quả ra file:** Xuất vào `data/` và `02_Tien_xu_ly/outputs/`:
  - `data/data_clean.csv`: Tập dữ liệu 398,971 dòng sạch hoàn chỉnh.
  - `data/train.csv`, `valid.csv`, `val.csv`, `test.csv`: Các tập dữ liệu giao dịch sạch đã phân chia.
  - `outputs/preprocessing_pipeline_summary.csv`: Bảng đối chiếu số lượng dòng qua từng bước lọc.
  - `outputs/split_summary.csv`: Bảng tỷ lệ khách hàng và giao dịch trong từng tập Train/Val/Test.
  - `outputs/preprocessing_report.txt`: Báo cáo chi tiết toàn bộ pipeline làm sạch dữ liệu.
- **Cell xuất ảnh biểu đồ ra file:** Xuất vào `02_Tien_xu_ly/figures/` và `figures/`:
  - `fig01_clean_quantity_price_dist.png`
  - `fig02_clean_boxplot_outliers.png`
  - `fig03_train_val_test_split.png`
  - `fig04_preprocessing_funnel.png`

---

### 📌 Phân hệ 3: `03_Dac_trung` (`Dac_trung.ipynb`)
- **Mục tiêu:** Rút trích 3 chỉ số hành vi khách hàng RFM (Recency, Frequency, Monetary) theo mốc `snapshot_date`, phân tích độ lệch phân phối Skewness, phân chia Train/Val/Test cho tập khách hàng, áp dụng phép biến đổi log (`log1p`) để triệt tiêu skewness và chuẩn hóa dữ liệu (`StandardScaler`) chỉ fit trên Train set.
- **Cell xuất kết quả ra file:** Xuất vào `data/` và `03_Dac_trung/outputs/`:
  - `data/rfm_data.csv`: Bảng chỉ số RFM toàn bộ khách hàng.
  - `data/rfm_train.csv`, `rfm_val.csv`, `rfm_test.csv`: Bộ đặc trưng RFM đã biến đổi và chuẩn hóa cho từng tập.
  - `outputs/rfm_descriptive_stats.csv`: Thống kê mô tả bộ 3 chỉ số RFM thô.
  - `outputs/rfm_skewness_comparison.csv`: Bảng so sánh độ lệch trước và sau biến đổi log1p.
  - `outputs/rfm_correlation_matrix.csv`: Ma trận tương quan giữa các biến RFM.
  - `outputs/rfm_report.txt`: Báo cáo chi tiết về bộ đặc trưng RFM.
- **Cell xuất ảnh biểu đồ ra file:** Xuất vào `03_Dac_trung/figures/` và `figures/`:
  - `fig01_rfm_raw_distribution.png`
  - `fig02_rfm_log_distribution.png`
  - `fig03_rfm_correlation_and_scatter.png`
  - `fig04_rfm_3d_feature_space.png`

---

## 3. Hướng dẫn chạy

Cả 3 notebook đều được thiết lập cơ chế **tự động định vị thư mục gốc `Do_an_CuoiKy`**, do đó bạn có thể:
1. Mở bất kỳ notebook nào (`EDA.ipynb`, `Tien_xu_ly.ipynb`, `Dac_trung.ipynb`) trực tiếp từ VS Code / Jupyter Lab.
2. Bấm **Run All** (hoặc chạy tuần tự từng cell từ trên xuống dưới).
3. Toàn bộ kết quả số liệu sẽ tự động xuất vào thư mục `outputs/` (và `data/`), và toàn bộ ảnh biểu đồ sẽ tự động xuất vào thư mục `figures/`.
