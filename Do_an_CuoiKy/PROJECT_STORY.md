# TOÀN BỘ CÂU CHUYỆN DỰ ÁN (PROJECT STORYLINE CHO POWERPOINT & BÁO CÁO)
## Đề Tài: Phân Khúc Khách Hàng Bằng RFM & Hành Vi Mua Hàng (Online Retail II)
**Học phần:** Học máy (Machine Learning) - Trường Đại học Sài Gòn (SGU)  
**Tập thể thực hiện:** Nhóm 05 - Lớp DCT124C1  

---

## MỤC LỤC CÂU CHUYỆN DỰ ÁN

1. **Hồi 1 - Bối Cảnh & Nỗi Đau Kinh Doanh (The Business Dilemma)**
2. **Hồi 2 - Khám Phá Dữ Liệu (EDA) & Hiện Tượng Lệch Phân Phối Cực Đoan**
3. **Hồi 3 - Cái Bẫy Ban Đầu: Mô Hình Baseline & Nghịch Lý Silhouette (The Baseline Trap)**
4. **Hồi 4 - Bước Ngoặt Kỹ Nghệ Đặc Trưng RFM (The RFM Feature Engineering)**
5. **Hồi 5 - Cuộc Đua Tam Mã: Tinh Chỉnh Siêu Tham Số 3 Trường Phái (The Tuning Journey)**
6. **Hồi 6 - Đột Phá Kiến Trúc: Mô Hình Lai 2 Tầng & Đỉnh Cao Tri-Model Consensus**
7. **Hồi 7 - Hiện Thực Hóa Ứng Dụng: Chiến Lược Kinh Doanh & Đóng Gói CLI `predict.py`**
8. **Kịch Bản Thuyết Trình Chi Tiết 12 Slide PowerPoint (Slide-by-Slide Deck)**

---

## HỒI 1: BỐI CẢNH & NỖI ĐAU KINH DOANH (THE BUSINESS DILEMMA)

### 1.1. Bối cảnh thị trường
Doanh nghiệp trong đề tài là một nhà bán lẻ trực tuyến tại Vương quốc Anh (*Online Retail II*), chuyên phân phối sỉ và lẻ các mặt hàng quà tặng độc đáo trên toàn cầu. Tập dữ liệu ghi nhận hơn **1 triệu dòng giao dịch** (1,067,371 records) phát sinh từ tháng 12/2009 đến tháng 12/2011.

### 1.2. Nỗi đau thực tế của doanh nghiệp (The Business Pain Point)
- Doanh nghiệp đối mặt với bài toán kinh điển: **Đối xử với mọi khách hàng như nhau (One-Size-Fits-All Marketing)**.
- Khi có chương trình khuyến mãi, doanh nghiệp gửi email hàng loạt tới toàn bộ danh sách:
  - Khách hàng VIP cảm thấy bị quấy rầy bởi các voucher giảm giá đại trà nhỏ lẻ, làm giảm giá trị thương hiệu.
  - Khách hàng có nguy cơ rời bỏ (*At Risk*) không nhận được sự quan tâm kịp thời để níu chân.
  - Ngân sách tiếp thị bị lãng phí nghiêm trọng vào nhóm tài khoản ảo hoặc những người đã từ bỏ thương hiệu nhiều năm.

### 1.3. Mục tiêu của đề tài
Xây dựng một hệ thống phân khúc khách hàng tự động dựa trên học máy không giám sát (Unsupervised Learning) thỏa mãn 3 tiêu chuẩn khắt khe:
1. **Khách quan và chặt chẽ về toán học:** Không gán nhãn thủ công chủ quan, triệt tiêu hoàn toàn hiện tượng rò rỉ dữ liệu (Zero Data Leakage).
2. **Tính hành động kinh doanh cao (Actionable):** Mỗi phân khúc phải có chân dung hành vi rõ ràng, đi kèm chiến lược tiếp thị khả thi.
3. **Sẵn sàng triển khai thực tế (Production-Ready):** Có khả năng dự đoán phân khúc cho khách hàng mới trong thời gian thực ($< 5$ mili-giây).

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

### 2.2. Bốn "bệnh lý" lớn được phát hiện qua EDA
1. **Dữ liệu trùng lặp hoàn toàn:** Phát hiện **34,335 dòng trùng lặp** do ghi nhận đơn hàng lặp lại từ hệ thống web.
2. **Dữ liệu khuyết thiếu nghiêm trọng:** Có tới **243,007 dòng thiếu `CustomerID`** (chiếm ~22.8%). Do mục tiêu đề tài là phân khúc khách hàng, các giao dịch không định danh bắt buộc phải được bóc tách xử lý riêng.
3. **Giá trị âm và bằng 0 bất thường:**
   - 22,950 dòng có `Quantity < 0` (hàng hoàn trả, đơn bị hủy bỏ).
   - 6,207 dòng có `Price <= 0` (lỗi kế toán, quà tặng thử nghiệm, điều chỉnh công nợ).
4. **Phân phối lệch phải cực đoan (Extreme Right-Skewness):**
   - Đơn giá `Price` lệch phải với Skewness lên tới **24.22** (hầu hết hàng hóa dưới £10, nhưng cá biệt có dịch vụ manual tính tới £38,970).
   - Số lượng `Quantity` lệch phải với Skewness **9.94** (xuất hiện đơn hàng sỉ lên tới hàng chục nghìn sản phẩm).

---

## HỒI 3: CÁI BẪY BAN ĐẦU: MÔ HÌNH BASELINE & NGHỊCH LÝ SILHOUETTE (THE BASELINE TRAP)

### 3.1. Trực giác ban đầu và sai lầm thường gặp
Khi bắt tay vào đề tài, trực giác đầu tiên của nhóm (cũng là sai lầm phổ biến của nhiều người mới làm quen với dữ liệu e-commerce) là: *Làm sạch các dòng giao dịch và đưa trực tiếp các thuộc tính số có sẵn (`Quantity`, `Price`, `TotalPrice`) vào các thuật toán phân cụm.*

Sau khi tiền xử lý lọc đơn hủy/hoàn và đơn giá âm, tập dữ liệu sạch còn lại 251,000 dòng giao dịch ở tập Train. Nhóm xây dựng 3 mô hình Baseline:
- **K-Means Baseline ($K=3$):** Silhouette = 0.6244 (Train), 0.6417 (Test).
- **Hierarchical Baseline ($K=4$, Ward):** Silhouette = 0.6258 (Mẫu 5,000 dòng).
- **DBSCAN Baseline ($\epsilon=0.5, \text{min}=10$):** Silhouette = 0.6440.

### 3.2. Điểm số cao ngất ngưởng... nhưng thất bại hoàn toàn về nghiệp vụ!
Thoạt nhìn, chỉ số Silhouette Score trên 0.64 là một kết quả "trong mơ" của bài toán phân cụm. Tuy nhiên, khi đào sâu phân tích bản chất hình học và kinh doanh, nhóm nhận ra đây là một **"ảo ảnh toán học" (Mathematical Illusion)**:
- **Hiện tượng dồn cục cực đoan:** Hơn **98.2% dòng giao dịch** bị dồn vào Cụm 0 (các đơn hàng nhỏ lẻ phổ thông), trong khi Cụm 1 và Cụm 2 chỉ chứa vỏn vẹn một vài đơn hàng mua số lượng lớn hoặc giá trị cao.
- **Nghẽn bộ nhớ:** Hierarchical bị tràn bộ nhớ $\mathcal{O}(N^2)$ (đòi hỏi ~500 GB RAM trên 251K dòng), buộc phải lấy mẫu 5,000 dòng mới chạy được.
- **Sai lệch đối tượng nghiên cứu:** Mô hình chỉ đang **phân loại quy mô giỏ hàng (Basket-level)** chứ không hề **phân khúc khách hàng (Customer-level)**. Cùng một khách hàng $A$, hôm nay mua 1 món đồ nhỏ thì nằm ở Cụm 0, ngày mai mua hộ công ty đơn lớn thì bị ném sang Cụm 1. Phòng Marketing hoàn toàn không biết khách hàng $A$ thực chất thuộc nhóm đối tượng nào để chăm sóc!

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

## HỒI 6: ĐỘT PHÁ KIẾN TRÚC: MÔ HÌNH LAI 2 TẦNG & ĐỈNH CAO TRI-MODEL CONSENSUS

### 6.1. Hạn chế cốt tử của mô hình đơn lẻ
- **K-Means:** Bắt buộc mọi khách hàng phải thuộc về một cụm hình cầu. Trong cụm VIP, người chi tiêu £300,000 bị đánh đồng với người chi tiêu £5,000.
- **Hierarchical:** Tốn kém bộ nhớ $\mathcal{O}(N^2)$ và không dự đoán trực tiếp được dữ liệu mới.
- **DBSCAN:** Quét mật độ tốt nhưng không thể phân vùng số đông khi mật độ không đồng đều.

### 6.2. Giải pháp 1: Mô hình Lai 2 Tầng (K-Means + DBSCAN)
- **Tầng 1:** K-Means phân 4 nhóm vĩ mô.
- **Tầng 2:** DBSCAN quét vi mô trong từng nhóm, bóc tách chuẩn xác **22 "Siêu Cá Voi B2B" (Super Whales)** với chi tiêu trung bình **£55,725** (gấp 11 lần khách VIP thường). Nâng cấp từ 4 phân khúc thô thành **ma trận 8 phân khúc chuyên sâu**.

### 6.3. Giải pháp 2 (Đỉnh cao): Tri-Model Hybrid & Consensus Ensemble (Hierarchical + K-Means + DBSCAN)
Hệ thống kết hợp trọn vẹn cả 3 trường phái học máy:
1. **Tầng 1 (Structural Initialization):** Hierarchical (Ward) xây dựng cây phả hệ và trích xuất 4 tọa độ tâm cụm hạt giống tự nhiên.
2. **Tầng 2 (Centroid Refinement):** K-Means nhận trực tiếp 4 tâm hạt giống này (`algorithm='lloyd'`), hội tụ siêu tốc chỉ sau **2 vòng lặp** mà không cần chạy lặp ngẫu nhiên `n_init`.
3. **Tầng 3 (Density & Whale Isolation):** DBSCAN quét mật độ lọc ra 43 khách hàng ngoại lai cá mập.
4. **Bộ máy bầu cử đồng thuận (Consensus Engine):** Phân tầng dữ liệu khách hàng thành 3 vùng độ tin cậy:
   - **Core Consensus (Đồng thuận lõi - 80.85% / 2,212 KH):** Cả 3 mô hình đồng thuận 100%. Điểm Silhouette tăng vọt lên **0.4200**!
   - **Boundary Contested (Biên tranh chấp - 17.58% / 481 KH):** Nằm ở vùng ranh giới chuyển dịch giữa các nhóm.
   - **Super Whales (Cá mập siêu chi tiêu - 1.57% / 43 KH):** Doanh thu trung bình cực khủng **£24,375**.

---

## HỒI 7: HIỆN THỰC HÓA ỨNG DỤNG: CHIẾN LƯỢC KINH DOANH & ĐÓNG GÓI CLI `predict.py`

### 7.1. Chân dung phân khúc & Chiến lược hành động thực tế (Actionable Business Strategies)

| Nhóm Phân Khúc | Tỷ lệ (%) | Recency | Frequency | Monetary | Chiến Lược Tiếp Thị & Hành Động (Actionable Strategy) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Super Whales (Cá mập B2B)** | **1.57%** | 13.5 ngày | 37.1 lần | **£24,375** | Giám đốc kinh doanh phụ trách chăm sóc 1-1, hợp đồng chiết khấu sỉ, hạn mức tín dụng riêng. |
| **VIP Champions (Lõi)** | **17.4%** | 15.2 ngày | 11.7 lần | **£5,127** | Đặc quyền Private Sale, tri ân sinh nhật cao cấp, giới thiệu sản phẩm mới trước công chúng. |
| **Loyal Customers (Lõi)** | **27.2%** | 62.4 ngày | 4.2 lần | **£1,680** | Chương trình tích điểm thành viên (Loyalty Points), ưu đãi khi mua combo sản phẩm. |
| **Boundary (Tranh chấp biên)** | **17.58%** | 125.7 ngày | 2.8 lần | **£970** | Gửi email kích cầu cá nhân hóa, tặng voucher giảm giá có thời hạn ngắn để đẩy lên nhóm Loyal. |
| **Hibernating / Lost (Rời bỏ)** | **32.7%** | 215.8 ngày | 1.3 lần | **£292** | Chiến dịch Win-Back tự động chi phí thấp, tối ưu ngân sách tránh lãng phí. |

### 7.2. Đóng gói sản phẩm CLI `predict.py`
Toàn bộ đường ống (Pipeline) tiền xử lý và mô hình tối ưu được đóng gói thành công cụ CLI:
- Tốc độ suy luận: **< 2 mili-giây / khách hàng**.
- Hỗ trợ cả 2 chế độ:
  - Dự đoán thời gian thực cho nhân viên: `python predict.py --recency 15 --frequency 8 --monetary 2500`
  - Dự đoán hàng loạt cho hệ thống dữ liệu: `python predict.py --file data/rfm_test.csv --output data/predictions_test.csv`

---

