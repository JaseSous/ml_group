# Thư mục EDA - Khám phá Dữ liệu, Tiền xử lý & Rút trích đặc trưng (Feature Engineering)

Thư mục này chịu trách nhiệm cho toàn bộ giai đoạn chuẩn bị dữ liệu (Data Preparation & Feature Engineering) của đề tài **Phân khúc khách hàng bằng RFM và học máy (Online Retail II)**, hoàn toàn độc lập với phần huấn luyện mô hình.

---

## 1. Cấu trúc thư mục EDA

```text
EDA/
├── EDA.ipynb            # Notebook phân tích khám phá (EDA), tiền xử lý, phân chia data_clean và rút trích đặc trưng RFM
└── README.md            # Tài liệu giải thích chi tiết quy trình chuẩn bị dữ liệu
```

---

## 2. Quy trình thực hiện trong `EDA.ipynb`

### 1. Khám phá và mô tả dữ liệu (EDA):
- Khảo sát dữ liệu gốc `online_retail_cleaned.csv` với 405,714 giao dịch và 8 thuộc tính.
- Kiểm tra dữ liệu khuyết thiếu (Missing values), trùng lặp (Duplicate rows).
- Kiểm tra các giá trị âm bất thường của `Quantity` và `Price`.
- Phân tích phân phối và độ lệch lệch phải (Skewness) bằng Histogram & KDE.
- Phát hiện ngoại lai bằng Boxplot và phương pháp khoảng tứ phân vị IQR.
- Phân tích tương quan giữa các biến số (`Quantity`, `UnitPrice`, `TotalPrice`).
- Phân tích doanh thu theo chu kỳ thời gian (Monthly Revenue Trend).
- Thống kê Top 10 sản phẩm bán chạy nhất và phân bố giao dịch theo quốc gia.

### 2. Tiền xử lý và làm sạch dữ liệu (Data Preprocessing):
- Khử trùng lặp và loại bỏ các dòng thiếu `CustomerID`.
- Chuẩn hóa tên cột (`InvoiceNo`, `UnitPrice`, `CustomerID`) và định dạng kiểu dữ liệu.
- Loại bỏ các đơn hàng hoàn trả hoặc đơn hủy (`Quantity <= 0` hoặc `UnitPrice <= 0`).
- Kiểm tra ngoại lai cực đại bằng phân vị $Q_{99}$ và thuật toán IQR.
- Tính toán lại giá trị doanh thu dòng `TotalPrice = Quantity * UnitPrice`.
- **Tập tin đã xuất:** `data/data_clean.csv` (398,971 dòng sạch).

### 3. Rút trích đặc trưng RFM & Chuẩn hóa (Feature Engineering):
- Xác định mốc thời gian chốt `Snapshot Date` (ngày giao dịch cuối + 1).
- Trích xuất 3 chỉ số RFM cho từng `CustomerID`:
  - **Recency ($R$)**: Số ngày từ lần mua gần nhất đến mốc chốt.
  - **Frequency ($F$)**: Tổng số đơn hàng thực hiện.
  - **Monetary ($M$)**: Tổng số tiền tích lũy đã chi tiêu.
- **Tập tin đã xuất:** `data/rfm_data.csv` (4,275 khách hàng).
- **Phân chia tập dữ liệu RFM**: Train (64%), Validation (16%), Test (20%) để tránh rò rỉ dữ liệu (Data Leakage).
- Xử lý lệch Skewness bằng biến đổi Log `np.log1p` và chuẩn hóa `StandardScaler` (chỉ fit trên tập Train).
- **Tập tin đã xuất:**
  - `data/rfm_train.csv` (2,736 khách hàng)
  - `data/rfm_val.csv` (684 khách hàng)
  - `data/rfm_test.csv` (855 khách hàng)

### 4. Phân chia tập dữ liệu giao dịch sạch `data_clean` (Train / Valid / Test):
- Dựa trên danh sách `CustomerID` đã phân tách độc lập (chống Data Leakage giữa các tập):
  - **`data/train.csv`**: Chứa toàn bộ 251,501 giao dịch sạch của tập khách hàng Train (~63.0%).
  - **`data/valid.csv`** (và `val.csv`): Chứa toàn bộ 72,685 giao dịch sạch của tập khách hàng Validation (~18.2%).
  - **`data/test.csv`**: Chứa toàn bộ 74,785 giao dịch sạch của tập khách hàng Test (~18.7%).

> **Lưu ý**: File này hoàn toàn **không chứa phần huấn luyện mô hình** (Baseline K-Means, Hierarchical, DBSCAN...). Quá trình huấn luyện, tối ưu tham số và đánh giá mô hình được tách biệt ở giai đoạn mô hình hóa.

---

## 3. Cách sử dụng

Mở và thực thi trực tiếp các cell trong Jupyter Notebook:
```bash
jupyter notebook EDA/EDA.ipynb
```
Hoặc mở trực tiếp file `EDA/EDA.ipynb` trên VS Code / Cursor / JupyterLab và chọn **Run All Cells**. Notebook sẽ tự động thực hiện toàn bộ phân tích, vẽ biểu đồ và xuất các file dữ liệu làm sạch, RFM và các tập train/valid/test vào thư mục `data/`.

---

## 4. Danh sách các file được sinh vào thư mục `data/`

| STT | Tập tin | Kích thước | Mô tả |
| :---: | :--- | :---: | :--- |
| 1 | `data_clean.csv` | ~38.8 MB | Dữ liệu giao dịch bán lẻ đã làm sạch hoàn chỉnh (398,971 dòng) |
| 2 | `train.csv` | ~24.5 MB | Tập giao dịch Train đã làm sạch (251,501 dòng) |
| 3 | `valid.csv` / `val.csv` | ~7.0 MB | Tập giao dịch Validation đã làm sạch (72,685 dòng) |
| 4 | `test.csv` | ~7.3 MB | Tập giao dịch Test độc lập đã làm sạch (74,785 dòng) |
| 5 | `rfm_data.csv` | ~89.2 KB | Bảng chỉ số RFM đầy đủ của 4,275 khách hàng |
| 6 | `rfm_train.csv` | ~57.1 KB | Tập Train RFM (64% - 2,736 khách hàng) |
| 7 | `rfm_val.csv` | ~14.3 KB | Tập Validation RFM (16% - 684 khách hàng) |
| 8 | `rfm_test.csv` | ~17.8 KB | Tập Test độc lập RFM (20% - 855 khách hàng) |
