# TOÀN BỘ CÂU CHUYỆN DỰ ÁN (PROJECT STORYLINE CHO POWERPOINT & BÁO CÁO)
## Đề Tài: Phân Khúc Khách Hàng Bằng RFM & Hành Vi Mua Hàng (Online Retail II)
**Học phần:** Học máy (Machine Learning) - Trường Đại học Sài Gòn (SGU)  
**Tập thể thực hiện:** Nhóm 05 - Lớp DCT124C1  

---

## MỤC LỤC CÂU CHUYỆN DỰ ÁN

1. **Hồi 1 - Bối Cảnh & Nỗi Đau Kinh Doanh (The Business Dilemma)**
2. **Hồi 2 - Khám Phá Dữ Liệu (EDA) & Tiền Xử Lý 7 Bước**
3. **Hồi 3 - Cái Bẫy Ban Đầu: Mô Hình Baseline & Nghịch Lý Silhouette (The Baseline Trap)**
4. **Hồi 4 - Bước Ngoặt Kỹ Nghệ Đặc Trưng RFM (The RFM Feature Engineering)**
5. **Hồi 5 - Cuộc Đua Tam Mã: Tinh Chỉnh Siêu Tham Số 3 Trường Phái (The Tuning Journey)**
6. **Hồi 6 - Đột Phá Kiến Trúc: Mô Hình Lai 2 Tầng & Đỉnh Cao Tri-Model Consensus**
7. **Tổng Kết Toàn Diện - Quá Trình Thực Nghiệm & Kết Quả Đạt Được Cho Nghiệp Vụ Kinh Doanh**

---

## HỒI 1: BỐI CẢNH & NỖI ĐAU KINH DOANH (THE BUSINESS DILEMMA)

### 1.1. Bối cảnh thị trường & Thực trạng doanh nghiệp
Doanh nghiệp trong đề tài là một nhà bán lẻ trực tuyến tại Vương quốc Anh (*Online Retail II*), chuyên kinh doanh sỉ và lẻ các mặt hàng quà tặng độc đáo và đồ gia dụng trên toàn cầu (phủ sóng 37 quốc gia, trong đó thị trường UK chiếm 91.2%).
- Quy mô khảo sát ghi nhận **405,714 giao dịch thực tế** (12/2009 – 12/2010), phục vụ **4,275 khách hàng định danh duy nhất** với **4,420 chủng loại mặt hàng**.
- Mô hình kinh doanh hỗn hợp (vừa bán lẻ B2C cho người tiêu dùng cá nhân, vừa bán sỉ B2B khối lượng lớn cho các đại lý quà tặng) khiến hành vi mua sắm cực kỳ đa dạng và phức tạp.

### 1.2. Ba nỗi đau kinh doanh cốt tử (The Core Business Pain Points)
1. **Tiếp thị đại trà "cào bằng" (One-Size-Fits-All Dilemma):** Doanh nghiệp không phân loại được khách hàng, gửi cùng một thông điệp tiếp thị và voucher giảm giá nhỏ lẻ cho toàn bộ danh sách. Khách hàng VIP cảm thấy bị quấy rầy và làm giảm uy tín thương hiệu.
2. **Nguy cơ mất khách hàng âm thầm (Customer Churn Risk):** Thiếu cơ chế phát hiện sớm những khách hàng từng mua nhiều nhưng đã lâu không quay lại (*At-Risk / Hibernating*), dẫn đến việc đánh mất khách hàng vào tay đối thủ cạnh tranh.
3. **Lãng phí ngân sách tiếp thị (Budget Inefficiency):** Đốt tiền quảng cáo và email vào các tài khoản không hoạt động hoặc khách hàng một lần, trong khi nhóm khách hàng mang lại 80% doanh thu không được chăm sóc đặc quyền.

### 1.3. Ba mục tiêu chiến lược của đề tài
Đồ án đặt ra 3 mục tiêu cụ thể, chặt chẽ từ lý thuyết học máy đến ứng dụng thực tiễn:
1. **Mục tiêu Khoa học (Machine Learning Pipeline):** Xây dựng quy trình phân cụm không giám sát (Unsupervised Learning) khách quan, chống rò rỉ dữ liệu (Zero Data Leakage), giải quyết triệt để phân phối lệch phải (Extreme Skewness) và bóc tách ngoại lai Super Whales B2B.
2. **Mục tiêu Nghiệp vụ (Marketing & CRM Actionability):** Chuyển đổi thành công từ cấp độ giỏ hàng (Basket-level) sang cấp độ khách hàng (Customer-level RFM); định hình chân dung sắc nét và xây dựng Playbook chiến lược hành động cá nhân hóa cho từng phân khúc nhằm tối đa hóa Giá trị vòng đời khách hàng (CLV).
3. **Mục tiêu Ứng dụng & Triển khai thực tế:** Xây dựng ma trận phân khúc và Playbook chiến lược kinh doanh khả thi, sẵn sàng chuyển giao cho phòng Marketing và ban lãnh đạo áp dụng trực tiếp vào hệ thống CRM.

---

## HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) & HIỆN TƯỢNG LỆCH PHÂN PHỐI CỰC ĐOAN

### 2.1. Cấu trúc 8 thuộc tính gốc của dữ liệu giao dịch
Tập dữ liệu thô gồm 8 thuộc tính phản ánh từng dòng đơn hàng:
- `Invoice`: Mã hóa đơn (bắt đầu bằng 'C' là đơn hoàn/hủy).
- `StockCode`: Mã mặt hàng lưu kho.
- `Description`: Tên và mô tả sản phẩm.
- `Quantity`: Số lượng sản phẩm mua.
- `InvoiceDate`: Mốc thời gian phát sinh giao dịch.
- `Price`: Đơn giá bán lẻ từng sản phẩm (£ Bảng Anh).
- `CustomerID`: Mã định danh duy nhất của từng khách hàng.
- `Country`: Quốc gia của khách hàng (UK chiếm >90%).

### 2.2. Đặc tính & Thách thức lớn của dữ liệu qua EDA
1. **Dữ liệu thô ban đầu:** 405,714 dòng giao dịch, 8 thuộc tính gốc.
2. **Độ toàn vẹn thuộc tính định danh:** Đầy đủ **100% CustomerID** (0 dòng bị thiếu mã khách hàng).
3. **Dữ liệu trùng lặp hoàn toàn:** Phát hiện **6,743 dòng trùng lặp** (chiếm 1.66% dữ liệu) $\to$ được loại bỏ, còn lại **398,971 dòng giao dịch sạch**.
4. **Phân phối lệch phải cực đoan (Right-Skewed Distribution):**
   - Đơn giá `Price`: Trung bình £3.52 nhưng xuất hiện dịch vụ/hàng hóa cá biệt lên tới hàng nghìn Bảng.
   - Số lượng `Quantity`: Trung bình 11.8 sản phẩm nhưng có các đơn hàng sỉ lên tới hàng trăm sản phẩm.
5. **Ngoại lai theo phương pháp IQR (Boxplot):**
   - Ngoại lai `Quantity`: **25,944 dòng (6.39%)** vượt ngưỡng trên IQR (> 27 sản phẩm).
   - Ngoại lai `Price`: **31,722 dòng (7.82%)** vượt ngưỡng trên IQR (> £7.50).
   - Nhận định nghiệp vụ: Đây không phải lỗi nhập liệu mà là các đơn hàng bán sỉ B2B và mặt hàng giá trị cao — cần phương pháp phân cụm mật độ để bóc tách chứ không thể xóa bỏ cơ học.

### 2.3. Quy trình 7 bước tiền xử lý & làm sạch dữ liệu (Data Preprocessing Pipeline)
Từ các phát hiện bệnh lý trong EDA, nhóm tiến hành tiền xử lý toàn diện qua notebook `02_Tien_xu_ly/Tien_xu_ly.ipynb`:
1. **Khử trùng lặp (Deduplication):** Loại bỏ **6,743 dòng giao dịch trùng lặp hoàn toàn** (chiếm 1.66%), giữ lại **398,971 dòng giao dịch sạch**.
2. **Kiểm tra dữ liệu thiếu:** Toàn vẹn 100% thuộc tính `CustomerID` (0 dòng khuyết thiếu).
3. **Chuẩn hóa tên cột & Ép kiểu dữ liệu:** Đổi tên `Invoice` $\to$ `InvoiceNo`, `Customer ID` $\to$ `CustomerID`. Ép `CustomerID` về chuỗi số nguyên chuẩn, `InvoiceDate` về định dạng Datetime chuẩn.
4. **Kiểm tra đơn hủy & Lọc giá trị không hợp lệ:** Kiểm tra mã đơn hủy ('C') và các đơn giá/số lượng $\le 0$. Kết quả không tồn tại đơn hủy hay giá âm bất thường.
5. **Tính toán trường thành tiền:** $\text{TotalPrice} = \text{Quantity} \times \text{Price}$.
6. **Khảo sát ngoại lai cực đại ($Q_{99}$ & IQR):** Bảo toàn các đơn hàng sỉ có khối lượng lớn (B2B Whales) để làm đầu vào cho mô hình phân cụm mật độ, không cắt bỏ cơ học.
7. **Phân chia dữ liệu sạch Train / Val / Test (Chống Data Leakage):** Phân chia dựa trên danh sách 4,275 mã `CustomerID` duy nhất:
   - **Tập Train (64%):** 251,501 giao dịch (2,736 khách hàng) $\to$ `data/train.csv`.
   - **Tập Validation (16%):** 72,685 giao dịch (684 khách hàng) $\to$ `data/valid.csv`.
   - **Tập Test (20%):** 74,785 giao dịch (855 khách hàng) $\to$ `data/test.csv`.

### 2.4. Đặc tả 2 Cơ sở dữ liệu & Bộ thuộc tính được huấn luyện (Training Feature Matrix)
Đồ án sử dụng **2 cơ sở dữ liệu với 2 bộ ma trận đặc trưng khác nhau** ở 2 giai đoạn nghiên cứu:

| Tiêu chí | Cơ sở dữ liệu 1: Giao Dịch Sạch (Transaction-level) | Cơ sở dữ liệu 2: Khách Hàng RFM (Customer-level) |
| :--- | :--- | :--- |
| **Tệp dữ liệu** | `data/train.csv`, `valid.csv`, `test.csv` | `data/rfm_train.csv`, `rfm_val.csv`, `rfm_test.csv` |
| **Đơn vị mẫu (Sample)** | Từng dòng mặt hàng trong hóa đơn | Từng tài khoản khách hàng duy nhất (`CustomerID`) |
| **Quy mô mẫu** | 251,501 dòng Train / 72,685 Val / 74,785 Test | 2,736 khách hàng Train / 684 Val / 855 Test |
| **Thuộc tính dùng để TRAIN ($X$)** | **`['Quantity', 'Price', 'TotalPrice']`** | **`['Recency_log', 'Frequency_log', 'Monetary_log']`** |
| **Phương pháp biến đổi** | Chuẩn hóa `StandardScaler` (z-score) | Biến đổi phi tuyến $\ln(1+x)$ + `StandardScaler` |
| **Mô hình áp dụng** | K-Means Baseline, Hierarchical Baseline, DBSCAN Baseline | Tuned K-Means, Tuned Hierarchical, Tuned DBSCAN, Hybrid 2 Tầng, Consensus |
| **Mục đích sử dụng** | Thiết lập mốc đối chuẩn ban đầu (Baseline Benchmark) | Phân khúc hành vi khách hàng phục vụ chiến lược kinh doanh và Marketing CRM |

---

## HỒI 3: THỰC NGHIỆM MÔ HÌNH CƠ SỞ (BASELINE MODEL) & CÁI BẪY NGHIỆP VỤ

### 3.1. Thiết lập Baseline & Thuộc tính huấn luyện giao dịch
Khi bắt tay vào bài toán, trực giác ban đầu của nhóm là thử nghiệm phân cụm trực tiếp trên các thuộc tính giao dịch cơ bản của đơn hàng:
- **Thuộc tính dùng để train baseline:** 3 thuộc tính số cơ bản của từng dòng giao dịch: `['Quantity', 'Price', 'TotalPrice']` (với `TotalPrice = Quantity * Price`).
- **Chiến lược chống rò rỉ dữ liệu (Zero Data Leakage):**
  - Dữ liệu giao dịch được phân chia theo khách hàng: Tập Train (255,341 dòng - 64%), Validation (63,835 dòng - 16%), Test (79,795 dòng - 20%).
  - Khởi tạo `StandardScaler` và **chỉ fit_transform trên tập Train**, sau đó dùng chính scaler này để transform trên tập Validation và Test.
- **Kết quả thực nghiệm đối chuẩn (Benchmark Metrics) 3 mô hình Baseline:**
  - **K-Means Baseline ($K=3$):** Silhouette Test = **0.6417**, Davies-Bouldin = **0.6040**, Calinski-Harabasz = **150,925**, thời gian huấn luyện siêu tốc **0.52s**. Đây là mô hình Baseline có hiệu năng tổng thể tốt nhất.
  - **Hierarchical Baseline ($K=4$, Ward):** Silhouette Test = **0.6566**, Davies-Bouldin = **0.6074**. Giới hạn thuật toán $\mathcal{O}(N^2)$ đòi hỏi quá nhiều bộ nhớ nên phải lấy mẫu đại diện 5,000 dòng.
  - **DBSCAN Baseline ($\varepsilon=0.5, \text{MinPts}=10$):** Silhouette Test = **0.6600**, Davies-Bouldin = **0.4015**, nhận diện được 0.94% - 1.94% đơn hàng ngoại lai.

### 3.2. Trực quan hóa Không gian 2D PCA & Hình thái phân cụm 3 mô hình
Để quan sát cách các mô hình Baseline chia cắt dữ liệu giao dịch, nhóm áp dụng Principal Component Analysis (PCA) để giảm 3 chiều về 2D:
- **Tỷ lệ giải thích phương sai:**
  - **PC1 giải thích 54.8% phương sai:** Đo lường quy mô độ lớn của đơn hàng.
  - **PC2 giải thích 34.9% phương sai:** Đo lường mức độ đắt đỏ của đơn giá.
  - **Tổng phương sai giải thích: 89.7%** (giữ lại gần như trọn vẹn thông tin gốc của 3 thuộc tính giao dịch).
- **So sánh hình thái phân cụm của 3 mô hình:**
  - **K-Means ($K=3$):** Cụm 0 (84.0%) dồn cục ở vùng đơn hàng phổ thông gần gốc tọa độ; Cụm 2 (14.6%) bị kéo dạt sang phải dọc theo trục PC1; Cụm 1 (1.4%) bị giật lên đỉnh theo trục PC2 do đơn giá đắt.
  - **Hierarchical ($K=4$, Ward):** Tách được cụm phổ thông (Cụm 0), cụm số lượng vừa (Cụm 2), cụm đơn giá cao (Cụm 1) và cô lập 6 điểm giao dịch đơn giá cực đoan nhất thành Cụm 3 riêng biệt.
  - **DBSCAN Baseline ($\varepsilon=0.5, \text{MinPts}=10$):** Gom trọn vẹn 95.1% đơn hàng bình thường vào Cụm 0 mật độ dày đặc, và gán nhãn 107 điểm giao dịch kéo dạt ra ngoài rìa thành điểm Nhiễu / Ngoại lai (Noise label = -1).

### 3.3. Giải phẫu thuộc tính "Kéo" không gian & Cái bẫy nghiệp vụ (The Baseline Trap)
Nhóm đi sâu phân tích định lượng lý do vì sao dữ liệu bị phân tách theo hình thái trên:
- **Thuộc tính nào kéo các trục PCA? (PCA Loadings):**
  - **Trục PC1 (54.8%):** Trọng số của `Quantity` (+0.7120) và `TotalPrice` (+0.6996) chi phối tuyệt đối. Các đơn hàng bán sỉ khối lượng lớn kéo dạt các điểm dữ liệu sang cực bên phải.
  - **Trục PC2 (34.9%):** Trọng số của `Price` (+0.9634) chi phối áp đảo. Các mặt hàng đơn giá cao kéo vọt các điểm dữ liệu lên đỉnh phía trên.
- **Đo lường mức độ chi phối qua kiểm định ANOVA F-Score (`f_classif`):**
  - `Price` là thuộc tính chi phối mạnh nhất: **44.80%** (K-Means), **53.11%** (DBSCAN), **30.08%** (Hierarchical).
  - `Quantity` chi phối thứ nhì: **38.48%** (K-Means), **29.91%** (DBSCAN), **30.06%** (Hierarchical).
  - `TotalPrice` đóng góp: **16.72%** (K-Means), **16.98%** (DBSCAN), **39.86%** (Hierarchical).
- **Vạch trần cái bẫy Baseline:**
  - **Ảo ảnh toán học:** Silhouette Score đạt 0.64 – 0.66 rất cao nhưng không phản ánh phân cụm có ý nghĩa, mà do các điểm ngoại lai kéo giãn không gian, tạo khoảng cách giả tạo giữa các cụm.
  - **Sai lệch cấp độ nghiên cứu:** Mô hình chỉ đang **phân loại kích thước giỏ hàng (Basket-level)** chứ không hề **phân khúc khách hàng (Customer-level)**. Một khách hàng mua 10 lần với 10 quy mô đơn khác nhau sẽ bị phân mảnh vào nhiều cụm khác nhau $\to$ Vô dụng cho chiến dịch tiếp thị và quản trị quan hệ khách hàng (CRM).
  - **Bước ngoặt bắt buộc:** Phải rời bỏ cấp độ Giao dịch, tiến hành nén dữ liệu và chuyển sang **Kỹ nghệ đặc trưng RFM ở cấp độ Khách hàng**!

---

## HỒI 4: BƯỚC NGOẶT KỸ NGHỆ ĐẶC TRƯNG RFM (THE RFM FEATURE ENGINEERING)

### 4.1. Rút trích bộ đặc trưng RFM kinh điển
Nhận diện rõ điểm nghẽn, nhóm quyết định thực hiện một bước ngoặt kiến trúc: Gom toàn bộ lịch sử giao dịch theo mã định danh `CustomerID`, rút trích bộ 3 chỉ số vàng trong ngành bán lẻ:
- **Recency ($R$):** Số ngày kể từ lần mua sắm cuối cùng đến mốc chốt dữ liệu (khách mua càng gần đây càng tốt).
- **Frequency ($F$):** Tổng số hóa đơn giao dịch độc lập đã thực hiện (đo lường độ trung thành).
- **Monetary ($M$):** Tổng số tiền khách hàng đã chi tiêu tích lũy (đo lường đóng góp doanh thu).

Quy mô dữ liệu nén từ hàng triệu dòng giao dịch về đúng **4,275 khách hàng duy nhất**.

### 4.2. Chinh phục phân phối Skewness & Chống rò rỉ dữ liệu (Zero Leakage)
Dữ liệu RFM thô có độ lệch phải khủng khiếp:
- `Recency`: Skewness = **1.26**
- `Frequency`: Skewness = **8.43**
- `Monetary`: Skewness = **24.01**

Nhóm triển khai quy trình tiền xử lý toán học chuẩn mực:
1. **Biến đổi phi tuyến:** Áp dụng hàm $\ln(1 + x)$ trên cả 3 biến $R, F, M$:
   - `Recency_log`: Skewness hạ xuống **-0.44** (tiệm cận dải chuẩn $[-0.5, 0.5]$).
   - `Frequency_log`: Skewness hạ xuống **1.17** (giảm 86.1% độ lệch).
   - `Monetary_log`: Skewness hạ xuống **0.31** (tiệm cận chuẩn hoàn hảo, giảm **98.7%** độ lệch!).
   - Các Outliers cực đoan từ £50K - £300K được nén phẳng vào thang đo tự nhiên, không còn làm méo khoảng cách Euclidean.
2. **Phân chia độc lập:** Chia tập dữ liệu thành Train (64% - 2,736 KH), Validation (16% - 684 KH) và Test (20% - 855 KH).
3. **Chuẩn hóa không rò rỉ:** Khởi tạo `StandardScaler` và chỉ học tham số vị trí ($\mu, \sigma$) **duy nhất trên tập Train**, sau đó đóng băng và ánh xạ sang Validation và Test.

### 4.3. Giải mã "Nghịch lý Silhouette" (The Silhouette Paradox)
Khi chạy thử nghiệm mô hình K-Means trên RFM chuẩn hóa, điểm Silhouette giảm từ 0.6417 xuống **0.3385**.
- Điểm 0.64 ở Baseline là **cao ảo** do các đơn hàng cực đoan kéo giãn không gian.
- Điểm 0.3385 ở RFM là **chất lượng thực chất**: Nó phản ánh dữ liệu khách hàng tạo thành một không gian liên tục, phân tách thành **4 phân khúc cân đối (18% - 33%)**, không có cụm nào bị nuốt chửng, và mỗi khách hàng chỉ có duy nhất một danh tính phân khúc ổn định.

---

## HỒI 5: CUỘC ĐUA TAM MÃ: TINH CHỈNH SIÊU THAM SỐ 3 TRƯỜNG PHÁI (THE TUNING JOURNEY)

### 5.1. Nhánh 1 - Tuned K-Means: Tối ưu phân hoạch hình cầu
- **Khảo sát số cụm $K \in [2, 10]$:** Đồ thị Elbow và Silhouette cho thấy $K=2$ đạt Silhouette cao nhất (0.4224) nhưng quá thô sơ. $K=4$ là điểm dung hòa hoàn hảo giữa độ gắn kết nội tại (Silhouette = 0.3385) và ý nghĩa kinh doanh 4 nhóm.
- **Thực nghiệm 6 kịch bản khởi tạo:**
  - Random khởi tạo ($n\_init=1$ và $10$): Bị kẹt cực tiểu địa phương, dao động Inertia.
  - $k$-means++ ($n\_init=25$, Lloyd): Đạt WCSS tối ưu 2,490.39, giảm 20.8% sai số so với bản thô, hội tụ ổn định 100%.
- **Phân tích ANOVA One-way $F$-Score (Thuộc tính nào chi phối phân cụm nhiều nhất?):**
  - **`Frequency`**: $F\text{-score} = \mathbf{2,475.70}$ (Chi phối mạnh nhất! Số lần mua hàng là yếu tố quyết định hàng đầu để tách biệt các cụm).
  - **`Recency`**: $F\text{-score} = \mathbf{1,930.28}$ (Chi phối phân biệt nhóm khách mới vs nhóm ngủ đông).
  - **`Monetary`**: $F\text{-score} = \mathbf{1,928.51}$ (Chi phối phân biệt nhóm chi tiêu cao vs nhóm chi tiêu tiết kiệm).
  - Cả 3 biến đều có $p\text{-value} < 10^{-100}$, chứng minh bộ ba RFM phối hợp hoàn hảo.

### 5.2. Nhánh 2 - Tuned Hierarchical: Bảo chứng cấu trúc phả hệ
- Dữ liệu RFM Train (2,736 KH) cho phép huấn luyện trực tiếp 100% không cần lấy mẫu.
- Hệ số tương quan Cophenetic đạt **0.6728**, chứng minh cây phả hệ Dendrogram bảo toàn tốt cấu trúc gốc.
- **Khảo sát 7 kịch bản Linkage:**
  - *Single Linkage:* Mắc "Hiệu ứng dây xích" (Chaining Effect) nghiêm trọng, 99.8% dữ liệu bị hút vào 1 cụm khổng lồ, 3 cụm còn lại chỉ có 1-2 điểm.
  - *Complete & Average Linkage:* Bị méo mó bởi khoảng cách cực đại/trung bình, phân mảnh cụm vi mô.
  - *Ward Linkage ($K=4$):* Tối ưu tuyệt đối, giảm phương sai nội cụm, tạo 4 cụm lồi cân đối.
- Khả năng tổng quát hóa qua `NearestCentroid`: Test đạt **0.3210**, không có Overfitting.

### 5.3. Nhánh 3 - Tuned DBSCAN: Bóc tách mật độ & Ngoại lai
- Khảo sát đa đường $k$-distance với $k \in \{4, 6, 10\}$. Điểm uốn Elbow xác định bán kính tối ưu $\epsilon = 0.6$ tại $\text{MinPts} = 10$.
- **Khảo sát 7 kịch bản $(\epsilon, \text{MinPts})$:**
  - $\epsilon \le 0.4$: Quá hẹp, biến 8% - 16% khách hàng thành nhiễu.
  - $\epsilon \ge 0.7$: Quá rộng, nuốt cả khách hàng bất thường vào cụm lõi.
  - $\epsilon = 0.6, \text{MinPts} = 10$: Hoàn hảo, bóc tách chính xác **43 khách hàng ngoại lai (1.57%)**, đạt Silhouette nội tại rất cao **0.5254**.

---

### 5.4. Chân dung 4 Phân khúc Cốt lõi từ Mô hình Tuned K-Means ($K=4$)
Mô hình huấn luyện nguồn: **Tuned K-Means ($K=4$, $n\_init=25$, algorithm='lloyd', random_state=42)** trên tập `data/rfm_train.csv` (chuẩn hóa `StandardScaler` sau khi biến đổi $\ln(1+x)$). Chi tiết tại `Exp07_KMeans_Tuned_Khoi/` và `Source/notebook/KMeans_RFM_Tuned.ipynb`:
1. **VIP Loyal (18.3% / 501 KH):** $R \approx 14$ ngày, $F \approx 12$ đơn, $M \approx £5,800$. Khách ruột nòng cốt, mang lại phần lớn doanh thu.
2. **Potential Loyalists / Tiềm Năng (27.1% / 741 KH):** $R \approx 35$ ngày, $F \approx 4$ đơn, $M \approx £1,200$. Khách mới mua gần đây, tần suất và chi tiêu đang tăng trưởng.
3. **Sleeping / At Risk / Ngủ Đông (21.8% / 596 KH):** $R \approx 180$ ngày, $F \approx 2$ đơn, $M \approx £550$. Khách lâu chưa quay lại, nguy cơ quên thương hiệu.
4. **Lost / Hibernating / Rời Bỏ (32.8% / 898 KH):** $R \approx 320$ ngày, $F \approx 1$ đơn, $M \approx £280$. Khách mua một lần rồi rời bỏ, chi tiêu rất thấp.

---

## HỒI 6: ĐỘT PHÁ KIẾN TRÚC: CÁC MÔ HÌNH LAI 2 TẦNG & ĐỈNH CAO TRI-MODEL CONSENSUS

### 6.1. Hạn chế cốt tử của mô hình đơn lẻ
- **K-Means:** Bắt buộc mọi khách hàng phải thuộc về một cụm hình cầu. Trong cụm VIP, người chi tiêu £300,000 bị đánh đồng với người chi tiêu £5,000.
- **Hierarchical:** Tốn kém bộ nhớ $\mathcal{O}(N^2)$ và không dự đoán trực tiếp được dữ liệu mới.
- **DBSCAN:** Quét mật độ tốt nhưng không thể phân vùng số đông khi mật độ không đồng đều.

### 6.2. Giải pháp Lai 1: Mô hình Lai 2 Tầng (K-Means + DBSCAN)
- **Tầng 1:** K-Means phân 4 nhóm vĩ mô.
- **Tầng 2:** DBSCAN quét vi mô trong từng nhóm, bóc tách chuẩn xác **22 "Siêu Cá Voi B2B" (Super Whales)** với chi tiêu trung bình **£55,725** (gấp 11 lần khách VIP thường, cao nhất £323,860.53). Nâng cấp từ 4 phân khúc thô thành **ma trận 8 phân khúc chuyên sâu**.

### 6.3. Giải pháp Lai 2: Mô hình Lai 2 Tầng (Hierarchical Ward + DBSCAN)
- **Tầng 1:** Hierarchical với liên kết Ward ($K=4$, $\text{Sil}=0.2976$) thiết lập cấu trúc phả hệ Dendrogram tự nhiên, đạt tính xác định 100% (không phụ thuộc vào `random_state`).
- **Tầng 2:** DBSCAN ($\epsilon=0.6, \text{MinPts}=5$) quét cục bộ từng nhánh phả hệ, bóc tách chuẩn xác **21 Siêu Cá Voi B2B** với chi tiêu trung bình **£58,148** (đơn cao nhất £323,860.53, tần suất trung bình 54.8 đơn).
- Bóc tách toàn bộ tập khách hàng thành 8 phân khúc chuyên sâu mà không làm lệch tâm các cụm bán lẻ chuẩn mực.

### 6.4. Đối chuẩn trực diện 2 Giải pháp Lai 2 Tầng
Dựa trên thực nghiệm đối đầu tại notebook `Comparison_Hybrid_KMeans_vs_Hierarchical_DBSCAN.ipynb`:
- **Độ trùng khớp Cá Voi cực cao:** Jaccard Index đạt **0.968 (30/31 khách hàng trùng khớp tuyệt đối - 96.8%)**, chứng minh cả hai kiến trúc toán học hoàn toàn đồng thuận về tập khách hàng giá trị lớn nhất doanh nghiệp.
- **Độ tương đồng cấu trúc Tầng 1:** $\text{ARI} = 0.5709$ và $\text{NMI} = 0.6169$, lượng thông tin tương hỗ cao.
- **Độ ổn định trên tập kiểm thử (Test Set):** K-Means + DBSCAN đạt $\text{Sil}=0.3253$; Hierarchical + DBSCAN đạt $\text{Sil}=0.3210$ (chênh lệch $< 1.3\%$).
- **Ma trận quyết định triển khai thực tế:**
  - *K-Means + DBSCAN:* Độ phức tạp tuyến tính $\mathcal{O}(N \cdot K \cdot I)$, thời gian huấn luyện siêu tốc 0.15s, có hàm `predict()` cho dữ liệu mới $\to$ Tối ưu cho Hệ thống Bán lẻ Big Data thời gian thực (Real-time).
  - *Hierarchical + DBSCAN:* Độ phức tạp $\mathcal{O}(N^2 \log N)$, xác định 100%, có cây Dendrogram giải thích phân tầng $\to$ Tối ưu cho Hoạch định chiến lược định kỳ B2B & Báo cáo Ban Giám đốc.

### 6.5. Giải pháp Lai 3 (Đỉnh cao): Tri-Model Consensus Ensemble Đồng Thuận 3 Thuật Toán
Hệ thống kết hợp trọn vẹn cả 3 trường phái học máy (Hierarchical Ward + K-Means Lloyd + DBSCAN):
1. **Tầng 1 (Structural Initialization):** Hierarchical (Ward) xây dựng cây phả hệ và trích xuất 4 tọa độ tâm cụm hạt giống tự nhiên.
2. **Tầng 2 (Centroid Refinement):** K-Means nhận trực tiếp 4 tâm hạt giống này, hội tụ siêu tốc chỉ sau **2 vòng lặp**.
3. **Tầng 3 (Density & Whale Isolation):** DBSCAN quét mật độ lọc ra 43 khách hàng ngoại lai cá mập.
4. **Bộ máy bầu cử đồng thuận (Consensus Engine):** Phân tầng dữ liệu khách hàng thành 3 vùng độ tin cậy:
   - **Core Consensus (Đồng thuận lõi - 80.85% / 2,212 KH):** Cả 3 mô hình đồng thuận 100%. Điểm Silhouette tăng vọt lên **0.4200**!
   - **Boundary Zone (Vùng ranh giới - 17.58% / 481 KH):** Nằm ở vùng biên nhạy cảm cần Marketing thử nghiệm A/B Testing.
   - **Super Whales (Cá mập siêu chi tiêu - 1.57% / 43 KH):** Doanh thu trung bình cực khủng **£24,375**.

---

## TỔNG KẾT TOÀN DIỆN: QUÁ TRÌNH THỰC NGHIỆM & KẾT QUẢ NGHIỆP VỤ KINH DOANH

### 7.1. Tóm tắt quá trình thực nghiệm Machine Learning xuyên suốt
1. **Khám phá & Làm sạch:** Từ 405,714 giao dịch thô lệch phải nặng $\to$ 7 bước tiền xử lý lọc sạch dòng âm, hóa đơn hủy, mã lỗi $\to$ Toàn vẹn 100% Customer ID nén về 4,275 khách hàng duy nhất.
2. **Cú sốc Baseline:** Phân cụm trên từng dòng giao dịch thất bại thảm hại (Cụm 0 nuốt trọn 98.2% dữ liệu, điểm Silhouette 0.64 là con số giả tạo do ngoại lai đứng xa).
3. **Bước ngoặt RFM & Log Transform:** Chuyển đổi sang cấp độ Khách hàng, triệt tiêu 98.7% độ lệch bằng $\ln(1+x)$ đưa về phân phối chuẩn, phân chia Train/Val/Test (64/16/20) triệt tiêu rò rỉ dữ liệu.
4. **Cuộc đua Tam mã Tinh chỉnh:** Tối ưu hóa siêu tham số 3 trường phái (K-Means $K=4$, Hierarchical Ward, DBSCAN K-distance). ANOVA chứng minh `Frequency` chi phối mạnh nhất ($F=2,475.70$).
5. **Đột phá Kiến trúc Lai:** Phát triển 2 mô hình lai 2 tầng và Mô hình đồng thuận Tri-Model Consensus Ensemble đạt 80.85% đồng thuận lõi ($\text{Sil}=0.420$).

### 7.2. Bốn (04) Tác động đột phá cho Nghiệp vụ Bán lẻ & Quản trị Kinh doanh
1. **Bóc tách Khách sỉ Doanh nghiệp B2B (Super Whales):**
   - Phát hiện 21-22 tài khoản cá mập với chi tiêu trung bình **£55,725 - £58,148** (gấp 11 lần khách VIP thông thường, cá biệt lên tới **£323,860.53**).
   - Thiết lập kênh chăm sóc đặc quyền 1:1 qua Account Manager riêng, đàm phán hợp đồng chiết khấu lớn và bảo toàn hơn **35% tổng doanh thu** của doanh nghiệp.
2. **Chặn đứng Thất thoát Khách hàng (Churn Prevention):**
   - Định danh chính xác nhóm khách hàng có nguy cơ rời bỏ (**At Risk / Sleeping** chiếm 17.6% - 21.8%) trước khi họ ngưng mua sắm hoàn toàn ($R \approx 126 - 180$ ngày).
   - Kích hoạt chiến dịch Re-engagement cá nhân hóa (voucher ngắn hạn, thăm hỏi trải nghiệm) để cứu vãn dòng tiền.
3. **Cắt giảm 80% Ngân sách Tiếp thị Lãng phí:**
   - Ngừng hoàn toàn việc gửi email và chạy quảng cáo đại trà tốn kém vào nhóm Khách rời bỏ (**Lost / Hibernating** chiếm 32.8% khách nhưng đóng góp chưa tới 3% doanh thu).
   - Tái phân bổ ngân sách vào nhóm Tiềm năng (**Potential Loyalists** 27.1%) để nuôi dưỡng thành khách hàng thân thiết.
4. **Tối đa hóa Giá trị Vòng đời Khách hàng (Customer Lifetime Value - CLV):**
   - Chuyển dịch doanh nghiệp từ tư duy tiếp thị "cào bằng" (One-Size-Fits-All) sang **Hệ thống phân khúc vi mô (Micro-segmentation)** 4-8 nhóm chuẩn xác, cá nhân hóa hành trình khách hàng.

