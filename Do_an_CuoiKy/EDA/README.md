# Thư mục EDA - Khám phá Dữ liệu, Tiền xử lý & Phân chia Dữ liệu Sạch

Thư mục này chịu trách nhiệm cho toàn bộ giai đoạn **Khám phá Dữ liệu (Exploratory Data Analysis - EDA)** và **Tiền xử lý & Làm sạch dữ liệu giao dịch (Data Cleaning & Preprocessing)** của đề tài **Phân khúc khách hàng bằng RFM và học máy (Online Retail II)**, hoàn toàn độc lập với phần rút trích RFM và huấn luyện mô hình.

---

## 1. Cấu trúc thư mục EDA

```text
EDA/
├── EDA.ipynb            # Notebook phân tích khám phá (EDA), tiền xử lý và phân chia data_clean
└── README.md            # Tài liệu giải thích chi tiết quy trình chuẩn bị dữ liệu
```

---

## 2. Quy trình thực hiện trong `EDA.ipynb`

### 1. Khám phá và mô tả dữ liệu (EDA):
- Khảo sát dữ liệu gốc `online_retail_cleaned.csv` với 405,714 giao dịch và 8 thuộc tính.
- Kiểm tra dữ liệu khuyết thiếu (Missing values), trùng lặp (Duplicate rows).
- Kiểm tra các giá trị âm bất thường của `Quantity` và `UnitPrice`.
- Phân tích phân phối và độ lệch phải (Skewness) bằng Histogram & KDE.
- Phát hiện ngoại lai bằng Boxplot và phương pháp khoảng tứ phân vị IQR.
- Phân tích tương quan giữa các biến số số học (`Quantity`, `UnitPrice`, `TotalPrice`).
- Phân tích doanh thu theo chu kỳ thời gian (Monthly Revenue Trend).
- Thống kê Top 10 sản phẩm bán chạy nhất và phân bố giao dịch theo quốc gia.

### 2. Tiền xử lý và làm sạch dữ liệu (Data Preprocessing):
- Khử trùng lặp và loại bỏ các dòng thiếu mã khách hàng (`CustomerID` rỗng).
- Chuẩn hóa tên cột (`InvoiceNo`, `UnitPrice`, `CustomerID`) và định dạng kiểu dữ liệu chuẩn (`InvoiceDate` sang datetime).
- Loại bỏ các đơn hàng hoàn trả hoặc đơn hủy (`Quantity <= 0` hoặc `UnitPrice <= 0`).
- Kiểm tra ngoại lai cực đại bằng phân vị $Q_{99}$ và thuật toán IQR.
- Tính toán lại giá trị thành tiền của từng giao dịch:
  $$\text{TotalPrice} = \text{Quantity} \times \text{UnitPrice}$$
- **Xuất tập dữ liệu sạch toàn diện:** `data/data_clean.csv` (398,971 dòng sạch).

### 3. Phân chia tập dữ liệu giao dịch sạch `data_clean` (Train / Validation / Test):
Nhằm **triệt để chống rò rỉ dữ liệu (Data Leakage)**, việc phân chia giao dịch được thực hiện dựa trên việc phân tách danh sách `CustomerID` độc lập (tỷ lệ 64% Train / 16% Validation / 20% Test với `random_state=42`):
- **`data/train.csv`**: Chứa 251,501 giao dịch sạch của tập khách hàng Train (~63.0%).
- **`data/valid.csv`** (và `val.csv`): Chứa 72,685 giao dịch sạch của tập khách hàng Validation (~18.2%).
- **`data/test.csv`**: Chứa 74,785 giao dịch sạch của tập khách hàng Test (~18.7%).

> [!NOTE]
> - Notebook `EDA.ipynb` **chỉ tập trung vào khám phá và làm sạch dữ liệu giao dịch cơ bản**.
> - Quá trình rút trích đặc trưng RFM chuyên sâu (Recency, Frequency, Monetary) được tách riêng sang notebook `Source/notebook/RFM.ipynb`.
> - Việc huấn luyện mô hình cơ sở (Baseline) được thực hiện trong thư mục `Source/notebook/`.

---

## 3. Danh sách các file dữ liệu được sinh ra trong thư mục `data/`

| STT | Tập tin dữ liệu | Kích thước | Mô tả chi tiết | Sử dụng tiếp theo ở đâu |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `data_clean.csv` | ~38.8 MB | Toàn bộ 398,971 dòng giao dịch bán lẻ đã làm sạch hoàn chỉnh | Đầu vào cho `Source/notebook/RFM.ipynb` |
| 2 | `train.csv` | ~24.5 MB | 251,501 giao dịch tập Train (thuộc 64% khách hàng Train) | Huấn luyện các mô hình Baseline (`KMeans_baseline`, `Hierarchical_baseline`, `DBSCAN_baseline`) |
| 3 | `valid.csv` / `val.csv` | ~7.0 MB | 72,685 giao dịch tập Validation (thuộc 16% khách hàng Val) | Kiểm định mô hình Baseline |
| 4 | `test.csv` | ~7.3 MB | 74,785 giao dịch tập Test (thuộc 20% khách hàng Test) | Kiểm thử độc lập mô hình Baseline |

---

## 4. Hướng dẫn chạy `EDA.ipynb`
Mở file `EDA/EDA.ipynb` trực tiếp trên VS Code và bấm **Run All** hoặc chạy từng cell theo thứ tự từ trên xuống dưới. Toàn bộ các bảng thống kê và biểu đồ trực quan sẽ được hiển thị đầy đủ và các file CSV sẽ được tự động xuất vào thư mục `data/`.
