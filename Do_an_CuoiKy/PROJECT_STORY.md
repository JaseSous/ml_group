# TOÀN BỘ CÂU CHUYỆN DỰ ÁN (PROJECT STORYLINE)
## Đề Tài: Phân Khúc Khách Hàng Bằng RFM & Hành Vi Mua Hàng (Online Retail II)
**Học phần:** Học máy (Machine Learning) - Trường Đại học Sài Gòn (SGU)  
**Tập thể thực hiện:** Nhóm 05 - Lớp DCT124C1  

---

## MỤC LỤC CÂU CHUYỆN DỰ ÁN

1. **Hồi 1 - Bối Cảnh & Nỗi Đau Kinh Doanh (The Business Dilemma)**
2. **Hồi 2 - Cái Bẫy Ban Đầu: Mô Hình Baseline & Nghịch Lý Silhouette (The Baseline Trap)**
3. **Hồi 3 - Bước Ngoặt Kỹ Nghệ: Chuyển Dịch Lên Cấp Độ Khách Hàng RFM (The RFM Pivot)**
4. **Hồi 4 - Cuộc Đua Tam Mã: Tinh Chỉnh 3 Trường Phái Học Không Giám Sát (The Tuning Journey)**
5. **Hồi 5 - Đỉnh Cao Đột Phá: Kiến Trúc Lai 2 Tầng K-Means & DBSCAN (The Climax Innovation)**
6. **Hồi 6 - Hiện Thực Hóa Sản Phẩm: Đóng Gói CLI predict.py & Sẵn Sàng Vận Hành (Production Readiness)**
7. **Kịch Bản Thuyết Trình Slide (Slide-by-Slide Presentation Guide)**
8. **Khung Sườn Báo Cáo Chi Tiết (Word Document Outline)**

---

## HỒI 1: BỐI CẢNH & NỖI ĐAU KINH DOANH (THE BUSINESS DILEMMA)

### 1.1. Bối cảnh thị trường
Doanh nghiệp trong đề tài là một nhà bán lẻ trực tuyến tại Vương quốc Anh (*Online Retail II*), chuyên phân phối các mặt hàng quà tặng độc đáo và đồ gia dụng trên toàn cầu. Tập dữ liệu ghi nhận hơn **1 triệu dòng giao dịch** (1,067,371 records) phát sinh từ tháng 12/2009 đến tháng 12/2011.

### 1.2. Nỗi đau thực tế của doanh nghiệp (The Business Pain Point)
- Doanh nghiệp đối mặt với bài toán kinh điển: **Đối xử với mọi khách hàng như nhau (One-Size-Fits-All Marketing)**.
- Khi có chương trình khuyến mãi, doanh nghiệp gửi email hàng loạt tới toàn bộ danh sách:
  - Khách hàng VIP cảm thấy bị quấy rầy bởi các voucher giảm giá đại trà nhỏ lẻ, làm giảm giá trị thương hiệu sang trọng.
  - Khách hàng có nguy cơ rời bỏ (*At Risk*) không nhận được sự quan tâm kịp thời để níu chân.
  - Ngân sách tiếp thị bị lãng phí nghiêm trọng vào nhóm khách hàng ảo hoặc những người đã từ bỏ thương hiệu nhiều năm.

### 1.3. Mục tiêu và sứ mệnh của nhóm nghiên cứu
Xây dựng một hệ thống phân khúc khách hàng tự động dựa trên học máy không giám sát (Unsupervised Learning) thỏa mãn 3 tiêu chuẩn khắt khe:
1. **Khách quan và chặt chẽ về toán học:** Không ấn định nhãn thủ công chủ quan, triệt tiêu hoàn toàn hiện tượng rò rỉ dữ liệu (Zero Data Leakage).
2. **Tính hành động kinh doanh cao (Actionable):** Mỗi phân khúc phải có chân dung hành vi rõ ràng, đi kèm chiến lược tiếp thị khả thi.
3. **Sẵn sàng triển khai thực tế (Production-Ready):** Có khả năng dự đoán phân khúc cho khách hàng mới trong thời gian thực ($< 5$ mili-giây).

---

## HỒI 2: CÁI BẪY BAN ĐẦU: MÔ HÌNH BASELINE & NGHỊCH LÝ SILHOUETTE (THE BASELINE TRAP)

### 2.1. Trực giác ban đầu và sai lầm thường gặp
Khi bắt tay vào đề tài, trực giác đầu tiên của nhóm (cũng là sai lầm phổ biến của nhiều người mới làm quen với dữ liệu e-commerce) là: *Làm sạch các dòng giao dịch và đưa trực tiếp các thuộc tính số có sẵn (`Quantity`, `Price`, `TotalPrice`) vào các thuật toán phân cụm.*

Sau khi tiền xử lý lọc đơn hủy/hoàn và đơn giá âm, tập dữ liệu sạch còn lại 251,000 dòng giao dịch ở tập Train. Nhóm xây dựng 3 mô hình Baseline:
- **K-Means Baseline ($K=3$):** Silhouette = 0.6244 (Train), 0.6417 (Test).
- **Hierarchical Baseline ($K=4$, Ward):** Silhouette = 0.6258 (Mẫu 5,000 dòng).
- **DBSCAN Baseline ($\epsilon=0.5, \text{min}=10$):** Silhouette = 0.6440.

### 2.2. Điểm số cao ngất ngưởng... nhưng thất bại hoàn toàn về nghiệp vụ!
Thoạt nhìn, chỉ số Silhouette Score trên 0.64 là một kết quả "trong mơ" của bài toán phân cụm. Tuy nhiên, khi đào sâu phân tích bản chất hình học và kinh doanh, nhóm nhận ra đây là một **"ảo ảnh toán học" (Mathematical Illusion)**:
- **Hiện tượng dồn cục cực đoan:** Hơn **98.2% dòng giao dịch** bị dồn vào Cụm 0 (các đơn hàng nhỏ lẻ phổ thông), trong khi Cụm 1 và Cụm 2 chỉ chứa vỏn vẹn một vài đơn hàng mua số lượng lớn hoặc giá trị cao.
- **Nghẽn bộ nhớ:** Hierarchical bị tràn bộ nhớ $O(N^2)$ (đòi hỏi ~500 GB RAM trên 251K dòng), buộc phải lấy mẫu 5,000 dòng mới chạy được.
- **Sai lệch đối tượng nghiên cứu:** Mô hình chỉ đang **phân loại quy mô giỏ hàng (Basket-level)** chứ không hề **phân khúc khách hàng (Customer-level)**. Cùng một khách hàng $A$, hôm nay mua 1 món đồ nhỏ thì nằm ở Cụm 0, ngày mai mua hộ công ty đơn lớn thì bị ném sang Cụm 1. Phòng Marketing hoàn toàn không biết khách hàng $A$ thực chất thuộc nhóm đối tượng nào để chăm sóc!

---

## HỒI 3: BƯỚC NGOẶT KỸ NGHỆ: CHUYỂN DỊCH LÊN CẤP ĐỘ KHÁCH HÀNG RFM (THE RFM PIVOT)

### 3.1. Rút trích bộ đặc trưng RFM kinh điển
Nhận diện rõ điểm nghẽn, nhóm quyết định thực hiện một bước ngoặt kiến trúc: Gom toàn bộ lịch sử giao dịch theo mã định danh `CustomerID`, rút trích bộ 3 chỉ số vàng trong ngành bán lẻ:
- **Recency ($R$):** Số ngày kể từ lần mua sắm cuối cùng đến mốc chốt dữ liệu (khách mua càng gần đây càng tốt).
- **Frequency ($F$):** Tổng số hóa đơn giao dịch độc lập đã thực hiện (đo lường độ trung thành).
- **Monetary ($M$):** Tổng số tiền khách hàng đã chi tiêu tích lũy (đo lường đóng góp doanh thu).

Quy mô dữ liệu nén từ hàng triệu dòng giao dịch về đúng **4,275 khách hàng duy nhất**.

### 3.2. Chinh phục phân phối Skewness & Chống rò rỉ dữ liệu (Zero Leakage)
Dữ liệu RFM có độ lệch phải (Right-Skewness) cực kỳ lớn: số đông khách hàng chỉ mua 1 - 2 lần với số tiền vài trăm bảng, trong khi một số ít khách hàng chi tiêu tới hàng trăm nghìn bảng.

Nhóm triển khai quy trình tiền xử lý toán học chuẩn mực:
1. **Biến đổi phi tuyến:** Áp dụng hàm $\log(x + 1)$ trên cả 3 biến $R, F, M$, nén phẳng đuôi dài và đưa phân phối về dạng gần chuẩn đối xứng.
2. **Phân chia độc lập:** Chia tập dữ liệu thành Train (64% - 2,736 KH), Validation (16% - 684 KH) và Test (20% - 855 KH).
3. **Chuẩn hóa không rò rỉ:** Khởi tạo `StandardScaler` và chỉ học tham số vị trí ($\mu, \sigma$) **duy nhất trên tập Train**, sau đó đóng băng và ánh xạ sang Validation và Test.

### 3.3. Giải mã "Nghịch lý Silhouette" (The Silhouette Paradox)
Khi chạy thử nghiệm mô hình K-Means trên RFM chuẩn hóa, điểm Silhouette giảm từ 0.6417 xuống **0.3385**.

Nhiều sinh viên khi thấy điểm giảm thường nghĩ rằng mô hình bị tệ đi. Nhưng Nhóm 05 đã chứng minh trước hội đồng điều ngược lại:
- Điểm 0.64 ở Baseline là **cao ảo** do dữ liệu bị kéo giãn bởi các đơn hàng ngoại cỡ.
- Điểm 0.3385 ở RFM là **chất lượng thực chất**: Nó phản ánh dữ liệu khách hàng tạo thành một không gian liên tục, phân tách thành **4 phân khúc cân đối (18% - 33%)**, không có cụm nào bị nuốt chửng, và đặc biệt mỗi khách hàng chỉ có duy nhất một danh tính phân khúc ổn định.

---

## HỒI 4: CUỘC ĐUA TAM MÃ: TINH CHỈNH 3 TRƯỜNG PHÁI HỌC KHÔNG GIÁM SÁT (THE TUNING JOURNEY)

Nhóm triển khai 3 nhánh nghiên cứu tinh chỉnh siêu tham số chuyên sâu:

### 4.1. Nhánh 1 - Tuned K-Means: Tìm kiếm sự cân bằng hoàn hảo
- Khảo sát dải $K \in [2, 10]$ qua đồ thị Elbow (Inertia SSE) và Silhouette Analysis.
- Phát hiện: $K=2$ có Silhouette cao nhất (0.4224) nhưng bị loại vì quá thô (chỉ chia khách mua nhiều vs mua ít). $K=4$ là điểm dung hòa tối ưu giữa độ gắn kết nội tại (Silhouette = 0.3385) và ý nghĩa kinh doanh 4 nhóm.
- Tinh chỉnh `init='k-means++'` với `n_init=25` và `max_iter=300`: Triệt tiêu hoàn toàn tính ngẫu nhiên, mô hình hội tụ ổn định 100%.
- Kiểm định đa tập: Train đạt **0.3385**, Validation đạt **0.3193**, Test đạt **0.3253** (độ suy giảm chỉ 5.6%, hoàn toàn không có Overfitting).

### 4.2. Nhánh 2 - Tuned Hierarchical: Bảo chứng cấu trúc phả hệ
- Vì dữ liệu RFM chỉ có 2,736 khách hàng Train, nhóm **huấn luyện trực tiếp trên 100% dữ liệu mà không cần lấy mẫu**.
- Hệ số tương quan Cophenetic đạt **0.6728**, xác nhận cây phả hệ Dendrogram bảo toàn tốt cấu trúc khoảng cách gốc.
- **Thử nghiệm 7 kịch bản Linkage:**
  - *Single Linkage:* Mắc lỗi "Dây chuyền" (Chaining Effect) nghiêm trọng, Cụm 0 nuốt trọn 99.9% khách hàng.
  - *Complete & Average Linkage:* Bị méo mó bởi ngoại lai, sinh ra các cụm vi mô chỉ có 3 đến 9 khách hàng.
  - *Ward Linkage ($K=4$):* Tối ưu nhất, tạo các cụm hình cầu cân đối, cho kết quả tương thích cao (> 90%) với K-Means.
- Đánh giá tổng quát qua `NearestCentroid`: Silhouette tập Test đạt **0.3210**, vượt cả tập Train (0.2976).

### 4.3. Nhánh 3 - Tuned DBSCAN: Nghệ thuật phát hiện ngoại lai
- Khảo sát đa đường đồ thị $k$-distance với $k \in \{4, 6, 10\}$.
- Điểm khuỷu tay (Elbow) xác định bán kính tối ưu $\epsilon = 0.6$ tại $k = 10$.
- Cấu hình này bóc tách chuẩn xác **43 khách hàng ngoại lai (1.57%)**, đạt Silhouette nội tại rất cao **0.5254** và Davies-Bouldin cực thấp **0.4055**.
- Tỷ lệ ngoại lai duy trì bền vững trên Validation (1.46%) và Test (1.64%).

---

## HỒI 5: ĐỈNH CAO ĐỘT PHÁ: KIẾN TRÚC LAI 2 TẦNG K-MEANS & DBSCAN (THE CLIMAX INNOVATION)

### 5.1. Câu hỏi trăn trở dẫn đến sáng tạo
Trong quá trình đánh giá độc lập, nhóm nhận ra một hạn chế cốt tử của K-Means:  
*K-Means bắt buộc mọi khách hàng phải thuộc về một cụm hình cầu. Kết quả là trong Cụm VIP, những khách hàng chi tiêu 200,000 - 300,000 bảng bị đánh đồng với khách hàng chi tiêu 5,000 bảng!*

Ngược lại, DBSCAN bóc tách ngoại lai rất giỏi nhưng nếu chạy một mình thì lại không thể phân khúc số đông.

**Ý tưởng lóe sáng:** *Tại sao không kết hợp K-Means và DBSCAN thành một mô hình lai 2 tầng (Two-Stage Hybrid Architecture)?*

### 5.2. Nguyên lý vận hành của Mô hình Lai
- **Tầng 1 (K-Means vĩ mô, $K=4$):** Chia toàn bộ khách hàng thành 4 không gian ngữ cảnh lớn.
- **Tầng 2 (DBSCAN vi mô bên trong từng cụm):** Chạy DBSCAN cục bộ bên trong từng cụm K-Means để phát hiện các vị khách dị biệt theo đúng ngữ cảnh của cụm đó.

### 5.3. Khám phá chấn động: Nhận diện 22 "Siêu Cá Voi" B2B
Khi áp dụng Tầng 2 vào Cụm 1 (Khách VIP - 498 khách hàng), DBSCAN đã tách ra chuẩn xác **22 vị khách siêu đặc biệt**:
- **Khách VIP tiêu dùng thường (476 KH):** Tần suất trung bình **11.7 đơn**, tổng chi tiêu trung bình **£5,127**.
- **22 Khách hàng "Cá Voi / B2B Whales":** Tần suất trung bình lên tới **53.0 đơn**, tổng chi tiêu trung bình đạt **£55,725** (cao gấp **11 lần** khách VIP thường, khách lớn nhất đạt £323,860).

Từ 4 phân khúc thô ban đầu, mô hình lai đã kiến tạo nên **ma trận 8 phân khúc chuyên sâu**:
1. **1B. Champions Super Whales (22 KH - 0.8%):** Siêu cá voi sỉ B2B (£55.7K, 53 đơn) $\rightarrow$ Giám đốc kinh doanh phụ trách 1-1.
2. **1A. Champions Regular (476 KH - 17.4%):** VIP tiêu dùng cá nhân (£5.1K, 12 đơn) $\rightarrow$ Đặc quyền Private Sale, tri ân sinh nhật.
3. **0B. Potential Rising Stars (3 KH - 0.1%):** Khách tiềm năng bứt phá (£4.0K, 7 đơn) $\rightarrow$ Tặng voucher kích hoạt ngay thành VIP.
4. **0A. Potential Regular (743 KH - 27.2%):** Khách tiềm năng chuẩn (£1.7K, 4 đơn) $\rightarrow$ Cross-sell / Up-sell giỏ hàng.
5. **3B. At Risk High-Loss (4 KH - 0.1%):** VIP cũ ngưng mua đột ngột (£783, 4 đơn) $\rightarrow$ CSKH gọi điện khẩn cấp cứu vãn.
6. **3A. At Risk Regular (590 KH - 21.6%):** Khách giảm dần số lần mua (£551, 2 đơn) $\rightarrow$ Chiến dịch Win-back tự động.
7. **2B. Lost Anomalies (2 KH - 0.1%):** Tài khoản dị biệt (R = 328 ngày, 4.5 đơn nhưng tổng tiền chỉ £92) $\rightarrow$ IT kiểm toán tài khoản ảo.
8. **2A. Lost Regular (896 KH - 32.7%):** Khách rời bỏ phổ thông (£292, 1.3 đơn) $\rightarrow$ Tiết kiệm chi phí, chỉ remarketing giá rẻ.

---

## HỒI 6: HIỆN THỰC HÓA SẢN PHẨM: ĐÓNG GÓI CLI `predict.py` & SẴN SÀNG VẬN HÀNH

### 6.1. Không dừng lại ở lý thuyết học thuật
Một đồ án Machine Learning xuất sắc phải chứng minh được giá trị triển khai trong môi trường doanh nghiệp thực tế. Nhóm 05 đã đóng gói toàn bộ quy trình tiền xử lý và mô hình tối ưu vào script độc lập [`predict.py`](file:///c:/Users/Quân/Desktop/ml_group/predict.py):
- **Tốc độ suy luận:** Đạt dưới **2 mili-giây** cho một dự đoán khách hàng.
- **Tương thích hai chế độ:**
  1. Chế độ CLI thời gian thực cho nhân viên bán hàng:  
     `python predict.py --recency 15 --frequency 8 --monetary 2500`
  2. Chế độ xử lý hàng loạt (Batch Processing) từ file CSV cho hệ thống dữ liệu:  
     `python predict.py --file data/rfm_test.csv --output data/predictions_test.csv`

### 6.2. Nhật ký thực nghiệm khoa học 25 bản ghi
Toàn bộ hành trình 5 giai đoạn được tự động ghi nhận vào [`Experiment_Log_Detailed.xlsx`](file:///c:/Users/Quân/Desktop/ml_group/Experiment_Log_Detailed.xlsx) và [`Experiment_Log_Comparison.csv`](file:///c:/Users/Quân/Desktop/ml_group/Experiment_Log_Comparison.csv) (mã hóa chuẩn `utf-8-sig`), lưu vết tường minh từ Baseline, Untuned RFM, Tuned RFM đến mô hình lai.

---

## 7. KỊCH BẢN THUYẾT TRÌNH SLIDE (SLIDE-BY-SLIDE PRESENTATION GUIDE)

Kịch bản 10 - 12 slide giúp nhóm làm chủ bài thuyết trình trước Hội đồng chấm điểm:

### Slide 1: Tiêu đề & Giới thiệu
- **Nội dung:** Tên đề tài, Nhóm 05, Lớp DCT124C1, Trường ĐH Sài Gòn.
- **Lời nói (Speaker):** *"Kính thưa Thầy/Cô và các bạn, hôm nay Nhóm 05 xin trình bày đề tài Phân khúc khách hàng thương mại điện tử dựa trên RFM và học máy không giám sát. Chúng em tiếp cận bài toán từ góc độ một giải pháp kinh doanh hoàn chỉnh, đi từ dữ liệu thô đến mô hình lai 2 tầng sẵn sàng cho sản xuất."*

### Slide 2: Vấn đề kinh doanh & Tập dữ liệu Online Retail II
- **Nội dung:** Quy mô 1,067,371 dòng giao dịch; Nỗi đau "One-Size-Fits-All" khiến lãng phí ngân sách và mất khách VIP.
- **Lời nói:** *"Với hơn 1 triệu dòng giao dịch thực tế, nếu doanh nghiệp gửi khuyến mãi đại trà, họ sẽ vừa làm phiền khách VIP vừa bỏ rơi khách sắp rời bỏ. Mục tiêu của chúng em là tạo ra cỗ máy phân khúc tự động, chuẩn xác và có thể hành động được."*

### Slide 3: Quy trình thực nghiệm 5 giai đoạn chuẩn mực
- **Nội dung:** Sơ đồ Mermaid từ EDA $\rightarrow$ Baseline $\rightarrow$ RFM $\rightarrow$ Tuning $\rightarrow$ Hybrid.
- **Lời nói:** *"Để đảm bảo tính khách quan khoa học, nhóm tuân thủ quy trình 5 bước nghiêm ngặt: Phân chia độc lập Train 64% / Val 16% / Test 20%, fit chuẩn hóa duy nhất trên Train để triệt tiêu hoàn toàn rò rỉ dữ liệu."*

### Slide 4: Mô hình Baseline & "Bẫy điểm số cao" (The Baseline Trap)
- **Nội dung:** Bảng số liệu Baseline (Silhouette = 0.6417); Biểu đồ phân bổ 98.2% giao dịch bị dồn vào Cụm 0.
- **Lời nói:** *"Tại bước Baseline, điểm Silhouette đạt 0.64 rất cao, nhưng đây là một cái bẫy! Mô hình chỉ phân loại kích thước giỏ hàng chứ không biết khách hàng là ai. Đây chính là động lực để nhóm thực hiện bước ngoặt chuyển dịch sang bộ chỉ số RFM."*

### Slide 5: Kỹ nghệ đặc trưng RFM & Giải mã "Nghịch lý Silhouette"
- **Nội dung:** Rút trích $R, F, M$ cho 4,275 khách hàng; Biến đổi $\log(x+1)$; So sánh Silhouette 0.64 (ảo) vs 0.3385 (thực chất).
- **Lời nói:** *"Khi chuyển sang RFM và nén độ lệch phải bằng hàm log, Silhouette đạt 0.3385. Điểm số này không hề tệ đi, mà phản ánh đúng bản chất 4 phân khúc khách hàng cân đối, có ranh giới tự nhiên và giá trị kinh doanh vượt trội."*

### Slide 6: Cuộc đua Tam mã: Tinh chỉnh K-Means, Hierarchical & DBSCAN
- **Nội dung:** Đồ thị Elbow, Silhouette, $k$-distance, và Dendrogram với hệ thức Lance-Williams.
- **Lời nói:** *"Chúng em tinh chỉnh chuyên sâu 3 trường phái: K-Means K=4 cân đối nhất; Hierarchical với Ward Linkage bảo chứng cấu trúc phả hệ; còn DBSCAN với eps=0.6 chứng tỏ là chuyên gia bóc tách ngoại lai."*

### Slide 7: Đột phá sáng tạo: Mô hình Lai 2 Tầng (Hybrid Pipeline)
- **Nội dung:** Sơ đồ 2 tầng (K-Means vĩ mô + DBSCAN vi mô); Điểm nhấn phát hiện 22 "Siêu Cá Voi" chi tiêu trung bình £55,725.
- **Lời nói:** *"Đây là đóng góp tâm đắc nhất của nhóm: Kết hợp K-Means phân 4 nhóm lớn, sau đó dùng DBSCAN đào sâu bên trong từng nhóm. Kết quả là chúng em bóc tách thành công 22 khách hàng Cá voi B2B với chi tiêu trung bình lên tới 56,000 bảng, gấp 11 lần khách VIP thường!"*

### Slide 8: Ma trận 8 phân khúc & Chiến lược kinh doanh thực tế
- **Nội dung:** Bảng 8 phân khúc với hành động cụ thể (Chăm sóc 1-1, Private Sale, Win-back, Kiểm toán tài khoản ảo).
- **Lời nói:** *"Từ 4 phân khúc thô, nhóm nâng cấp thành 8 kịch bản tiếp thị sắc bén. Mỗi nhóm khách hàng đều có một giải pháp tương ứng, giúp doanh nghiệp tối ưu hóa từng đồng chi phí tiếp thị."*

### Slide 9: Kiểm định tính tổng quát hóa & Vận hành sản xuất (`predict.py`)
- **Nội dung:** Bảng so sánh chỉ số trên Train / Val / Test (độ suy giảm $< 6\%$); Demo giao diện dòng lệnh `predict.py`.
- **Lời nói:** *"Mô hình duy trì độ ổn định tuyệt đối trên cả tập Validation và Test. Chúng em đã đóng gói thành script predict.py có tốc độ suy luận dưới 2 mili-giây, sẵn sàng tích hợp ngay vào hệ thống CRM của doanh nghiệp."*

### Slide 10: Tổng kết & Danh mục sản phẩm nghiệm thu
- **Nội dung:** Checklist sản phẩm (Báo cáo Word, Slide, 14 Notebooks, Nhật ký thực nghiệm Excel/CSV mã hóa `utf-8-sig`).
- **Lời nói:** *"Đề tài của Nhóm 05 đáp ứng trọn vẹn từ cơ sở lý thuyết toán học, chuẩn mực thực nghiệm chống rò rỉ dữ liệu, đến giải pháp kiến trúc lai sáng tạo và công cụ phần mềm thực tế. Nhóm em xin trân trọng cảm ơn Thầy/Cô!"*

---

## 8. KHUNG SƯỜN BÁO CÁO CHI TIẾT (WORD DOCUMENT OUTLINE)

Khung dàn ý chuẩn khoa học cho báo cáo chi tiết (`Bao_Cao_Giua_Ky_Nhom05_OnlineRetailII.docx`):

- **CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI & KHÁM PHÁ DỮ LIỆU (EDA)**
  - 1.1. Bối cảnh bài toán phân khúc khách hàng trong thương mại điện tử.
  - 1.2. Mô tả tập dữ liệu *Online Retail II* (1,067,371 dòng).
  - 1.3. Quy trình làm sạch dữ liệu: Xử lý đơn hủy ($C$), đơn âm, khuyết thiếu `CustomerID`.
  - 1.4. Phân tích doanh thu theo thời gian, phân bố quốc gia và mặt hàng chủ lực.

- **CHƯƠNG 2: THỰC NGHIỆM MỐC ĐỐI CHUẨN (BASELINE MODELS)**
  - 2.1. Thiết lập bài toán Baseline trên dữ liệu giao dịch sạch (`Quantity`, `Price`, `TotalPrice`).
  - 2.2. Huấn luyện 3 mô hình cơ sở: K-Means ($K=3$), Hierarchical (Ward), DBSCAN.
  - 2.3. Đánh giá trên 3 tập dữ liệu độc lập (Train, Validation, Test).
  - 2.4. Phân tích nguyên nhân thất bại của Baseline: Nghịch lý Silhouette và hiện tượng phân cụm theo giỏ hàng.

- **CHƯƠNG 3: KỸ NGHỆ ĐẶC TRƯNG RFM & PHƯƠNG PHÁP LUẬN CHỐNG RÒ RỈ**
  - 3.1. Cơ sở lý thuyết bộ chỉ số RFM (Recency, Frequency, Monetary).
  - 3.2. Thuật toán trích xuất dữ liệu cấp độ khách hàng (4,275 khách hàng).
  - 3.3. Xử lý độ lệch phải Skewness bằng phép biến đổi phi tuyến $\log(x + 1)$.
  - 3.4. Chiến lược phân chia Train (64%) / Val (16%) / Test (20%) và chuẩn hóa `StandardScaler` duy nhất trên Train.

- **CHƯƠNG 4: TINH CHỈNH SIÊU THAM SỐ CHUYÊN SÂU (HYPERPARAMETER TUNING)**
  - 4.1. Phân tích ý nghĩa toán học của các siêu tham số trong từng thuật toán.
  - 4.2. Tối ưu K-Means: Phương pháp Elbow, Silhouette Analysis, kiểm thử 6 kịch bản khởi tạo $\rightarrow$ Chọn $K=4$, `k-means++`, $n\_init=25$.
  - 4.3. Tối ưu Hierarchical: Hệ thức đệ quy Lance-Williams, khảo sát 7 kịch bản Linkage $\rightarrow$ Chọn Ward Linkage ($K=4$), bác bỏ Single/Complete Linkage.
  - 4.4. Tối ưu DBSCAN: Đồ thị đa đường $k$-distance $\rightarrow$ Chọn $\epsilon = 0.6, \text{min\_samples} = 10$.
  - 4.5. Phân tích phương sai ANOVA One-Way ($F$-Score) chứng minh vai trò cân bằng của 3 biến $R, F, M$.

- **CHƯƠNG 5: ĐỘT PHÁ KIẾN TRÚC LAI 2 TẦNG (HYBRID CLUSTERING) & TRIỂN KHAI THỰC TẾ**
  - 5.1. Thiết kế đường ống lai 2 tầng: K-Means vĩ mô + DBSCAN vi mô cục bộ.
  - 5.2. Nhận diện và bóc tách chân dung 22 khách hàng "Cá Voi / B2B Whales" (£55.7K, 53 đơn).
  - 5.3. Xây dựng ma trận chiến lược Marketing & Vận hành cho 8 phân khúc chuyên sâu.
  - 5.4. Đóng gói module dự đoán độc lập `predict.py` phục vụ thực tế qua giao diện dòng lệnh CLI.
  - 5.5. Kết luận, bài học kinh nghiệm và hướng phát triển đề tài.
