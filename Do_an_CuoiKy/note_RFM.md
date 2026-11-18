# Báo Cáo Tổng Kết & Đối Chuẩn Thực Nghiệm Mô Hình RFM
## So Sánh 3 Thuật Toán Phân Cụm (K-Means, Hierarchical, DBSCAN) & Đối Chiếu Với Baseline

---

## 1. Tổng Quan Kiến Trúc Thực Nghiệm

Dữ liệu RFM được xây dựng từ tập giao dịch đã làm sạch, trích xuất theo từng `CustomerID` và chia độc lập thành 3 tập dữ liệu chống rò rỉ (Data Leakage):
- **Tập Train (64%):** 2,736 khách hàng
- **Tập Validation (16%):** 684 khách hàng
- **Tập Test (20%):** 855 khách hàng
- **Tiền xử lý:** Biến đổi log $\log(x + 1)$ nhằm khử độ lệch phải (Right-Skewness), chuẩn hóa `StandardScaler` (fit duy nhất trên tập Train).

Ba thuật toán phân cụm đại diện cho 3 trường phái học không giám sát kinh điển được thực nghiệm trên cùng một không gian đặc trưng RFM:
1. **K-Means Clustering:** Phân cụm dựa trên tâm hình học (Centroid-based), cấu hình tối ưu $K = 4$.
2. **Hierarchical Clustering (Agglomerative):** Phân cụm thứ bậc dựa trên khoảng cách liên kết tối thiểu hóa phương sai (Ward Linkage), cấu hình tối ưu $K = 4$.
3. **DBSCAN:** Phân cụm dựa trên mật độ không gian (Density-based), cấu hình tối ưu qua đồ thị $k$-distance ($k = 10, \epsilon = 0.6$).

---

## 2. Bảng Tổng Hợp Số Liệu Đối Chuẩn 3 Mô Hình trên Train / Validation / Test

| Thuật toán | Cấu hình | Tập dữ liệu | Silhouette (↑) | Davies-Bouldin (↓) | Calinski-Harabasz (↑) | Số cụm | Tỷ lệ Nhiễu | Thời gian |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **K-Means** | $K = 4$, `init='k-means++'` | **Train (64%)** | **0.3385** | **0.9960** | **2,090.80** | 4 | 0.00% | ~0.04s |
| | `random_state=42` | **Validation (16%)** | **0.3193** | **1.0210** | **503.80** | 4 | 0.00% | ~0.01s |
| | | **Test (20%)** | **0.3253** | **1.0248** | **629.08** | 4 | 0.00% | ~0.01s |
| **Hierarchical** | $K = 4$, `linkage='ward'` | **Train (64%)** | 0.2976 | 1.0827 | 1,808.38 | 4 | 0.00% | ~0.11s |
| *(Agglomerative)* | (Dự đoán qua NearestCentroid) | **Validation (16%)** | 0.3093 | 1.0281 | 485.68 | 4 | 0.00% | ~0.02s |
| | | **Test (20%)** | 0.3210 | 1.0485 | 621.10 | 4 | 0.00% | ~0.02s |
| **DBSCAN** | $k = 10$, $\epsilon = 0.6$ | **Train (64%)** | 0.5254\* | 0.4055 | 117.32 | 2 | **1.57% (43 KH)** | ~0.08s |
| *(Density-Based)* | (Dự đoán qua Nearest Core) | **Validation (16%)** | 0.5274\* | 0.3382 | 17.46 | 2 | **1.46% (10 KH)** | ~0.03s |
| | | **Test (20%)** | 0.5298\* | 0.4017 | 25.43 | 2 | **1.64% (14 KH)** | ~0.03s |

*\*Lưu ý: Chỉ số Silhouette và Davies-Bouldin của DBSCAN chỉ tính trên các cụm mật độ hợp lệ (loại trừ điểm nhiễu mang nhãn -1).*

---

## 3. So Sánh Mức Độ Chi Phối của Các Thuộc Tính RFM (ANOVA F-Score)

| Thuộc tính RFM | K-Means RFM ($K=4$) | Hierarchical RFM ($K=4$) | DBSCAN RFM ($k=10, \epsilon=0.6$) |
| :--- | :---: | :---: | :---: |
| **Recency ($R$)** | **30.50%** ($F = 1,487.8$) | **39.05%** ($F = 2,165.7$) | **56.40%** ($F = 148.2$) |
| **Frequency ($F$)** | **39.10%** ($F = 1,906.7$) | **35.60%** ($F = 1,974.3$) | **12.40%** ($F = 32.6$) |
| **Monetary ($M$)** | **30.40%** ($F = 1,482.9$) | **25.35%** ($F = 1,406.1$) | **31.20%** ($F = 81.9$) |

**Nhận xét:**
- **K-Means:** Phân bổ đồng đều nhất trên cả 3 chiều ($F \approx 39.1\%$, $R \approx 30.5\%$, $M \approx 30.4\%$). Điều này chứng minh thuật toán khai thác trọn vẹn sức mạnh của cả bộ 3 chỉ số hành vi khách hàng.
- **Hierarchical:** Ưu tiên tách cụm mạnh dựa trên Recency ($39.05\%$) và Frequency ($35.60\%$).
- **DBSCAN:** Bị chi phối quá lớn bởi Recency ($56.40\%$) trong khi Frequency chỉ đóng góp $12.40\%$.

---

## 4. Đánh Giá Giá Trị Ứng Dụng Kinh Doanh

| Tiêu chí nghiệp vụ | K-Means RFM ($K=4$) | Hierarchical RFM ($K=4$) | DBSCAN RFM ($k=10, \epsilon=0.6$) |
| :--- | :--- | :--- | :--- |
| **Số lượng phân khúc** | **4 cụm độc lập** | **4 cụm độc lập** | **2 cụm + 1 nhóm Ngoại lai (-1)** |
| **Tỷ lệ phân bổ mẫu** | **Rất cân đối (18% - 33%)** | **Rất cân đối (18% - 33%)** | Mất cân đối (Cụm 0 chiếm >98.4%) |
| **Phân khúc đại chúng** | **Xuất sắc:** VIP, Tiềm năng, Nguy cơ, Rời bỏ | **Xuất sắc:** Rất tương đồng với K-Means | **Kém:** Gom gần như toàn bộ khách vào cụm 0 |
| **Phát hiện dị biệt / Ngoại lai** | Kém hơn (bị kéo vào cụm gần nhất) | Kém hơn (bị gộp vào cây phân cấp) | **Xuất sắc:** Tách 1.57% nhóm "Cá voi" & gian lận |
| **Tốc độ dự đoán điểm mới** | **Micro-seconds:** $O(K \times d)$ | Nhanh qua `NearestCentroid` | Phức tạp qua tập Core Samples |

---

## 5. Quyết Định Lựa Chọn Mô Hình RFM Tối Ưu Nhất

> ### Mô hình chiến thắng trên không gian RFM: **TUNED K-MEANS CLUSTERING ($K = 4$)**

**4 Căn cứ khoa học và thực tiễn:**
1. **Điểm kiểm định Test dẫn đầu:** Silhouette trên tập Test đạt **$0.3253$** (cao hơn $0.3210$ của Hierarchical), Davies-Bouldin đạt mức tối ưu nhất **$1.0248$**, Calinski-Harabasz đạt **$629.08$** (vượt trội hoàn toàn so với DBSCAN $25.43$).
2. **Khai thác thuộc tính cân bằng:** Phân bổ đồng đều cả 3 chiều $F$ ($39.1\%$), $R$ ($30.5\%$), $M$ ($30.4\%$).
3. **Phân khúc có tính ứng dụng cao:** Xác lập 4 chân dung khách hàng sắc nét:
   - **Champions (VIP - 20.3%):** $R=14$ ngày, $F=13$ đơn, $M=7,362$ GBP $\rightarrow$ Chăm sóc đặc quyền 1-on-1.
   - **Potential Loyalists (Tiềm năng - 32.8%):** $R=22$ ngày, $F=2$ đơn, $M=552$ GBP $\rightarrow$ Kích thích tần suất (cross-sell/up-sell).
   - **At Risk (Nguy cơ - 26.0%):** $R=86$ ngày, $F=4$ đơn, $M=1,688$ GBP $\rightarrow$ Chiến dịch cứu vãn (Win-back).
   - **Lost (Rời bỏ - 20.9%):** $R=189$ ngày, $F=1.2$ đơn, $M=291$ GBP $\rightarrow$ Giảm chi phí tiếp thị trực tiếp.
4. **Sẵn sàng triển khai thực tế (Production Readiness):** Tọa độ tâm cụm cố định cho phép dự đoán khách hàng mới trong thời gian thực cực kỳ nhẹ tải qua `predict.py`.

---

## 6. So Sánh Đối Đầu: K-Means RFM ($K=4$) VS. K-Means Baseline ($K=3$)

| Tiêu chí so sánh | K-Means Baseline ($K=3$) | Tuned K-Means RFM ($K=4$) | Đánh giá bước nhảy vọt |
| :--- | :--- | :--- | :--- |
| **Đơn vị phân tích (Entity)** | Từng dòng hóa đơn giao dịch riêng lẻ | Từng khách hàng tổng thể (`CustomerID`) | Chuyển từ "phân loại đơn hàng" sang "phân khúc con người". |
| **Thuộc tính đầu vào** | `Quantity`, `UnitPrice`, `TotalPrice` | `Recency`, `Frequency`, `Monetary` | Nắm bắt toàn diện chu kỳ sống khách hàng (LTV). |
| **Xử lý độ lệch (Skewness)** | Không xử lý log (dữ liệu lệch phải cực nặng) | Biến đổi log $\log(x+1)$ về tiệm cận chuẩn | Ổn định khoảng cách Euclid, phân cụm chuẩn xác. |
| **Quy mô tập huấn luyện** | 251,501 dòng giao dịch | 2,736 khách hàng (từ 398,000 dòng) | Tối ưu hóa bộ nhớ và tốc độ xử lý. |
| **Silhouette Score trên Test** | 0.6417 | 0.3253 | Giải mã nghịch lý: 0.64 là giá trị ảo do phân cách cơ học đơn hàng nhỏ/lớn; 0.32 là giá trị thực chất trong không gian hành vi 3D. |
| **Davies-Bouldin trên Test** | 0.6040 | 1.0248 | Cụm RFM đan xen tự nhiên giữa các giai đoạn chuyển tiếp hành vi. |
| **Giá trị ứng dụng kinh doanh** | Rất thấp (chỉ biết đơn to/nhỏ, không biết ai mua) | **Rất cao (xác lập 4 Persona rõ ràng, cá nhân hóa tiếp thị)** | Đem lại ROI thực tế trực tiếp cho doanh nghiệp. |

---

## 7. Kiến Trúc Đề Xuất: Mô Hình Phối Hợp Hybrid Clustering

Nhóm nghiên cứu đề xuất giải pháp kiến trúc phân cụm hai tầng (Two-Stage Hybrid Architecture) kết hợp sức mạnh của cả DBSCAN và K-Means:

```text
[Dữ liệu RFM của Khách hàng Mới]
               │
               ▼
   [Tầng 1: DBSCAN Anomaly Filter] ─── (Khoảng cách tới Core > 0.6) ───► [Nhóm Siêu VIP / Gian lận]
               │                                                          (Chăm sóc đặc biệt 1-on-1)
               ▼ (Điểm mật độ bình thường)
   [Tầng 2: Tuned K-Means (K=4)] ───► 4 Phân khúc: Champions / Potential / At Risk / Lost
                                      (Chiến dịch Marketing tự động hóa cá nhân hóa)
```

Mô hình kết hợp này vừa bảo đảm không bỏ sót các khách hàng "cá voi" dị biệt, vừa phân loại chuẩn xác 4 phân khúc khách hàng đại chúng cho các chiến dịch tiếp thị quy mô lớn.
