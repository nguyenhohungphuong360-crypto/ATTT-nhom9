# TRƯỜNG ĐẠI HỌC GIAO THÔNG VẬN TẢI TP.HCM (UTH)
## KHOA CÔNG NGHỆ THÔNG TIN — BỘ MÔN AN TOÀN THÔNG TIN
### ĐỒ ÁN MÔN HỌC: AN TOÀN THÔNG TIN (MÃ HỌC PHẦN: 3 TÍN CHỈ)

---

# ĐỀ TÀI 09: ĐO HIỆU QUẢ NHẬN DIỆN NỘI DUNG LỪA ĐẢO ĐƯỢC TẠO BỞI TRÍ TUỆ NHÂN TẠO
*(Measuring Human Detection Efficacy Against AI-Generated Phishing)*

* **Giảng viên hướng dẫn:** TS. Lê Quốc Tuấn  
* **Học kỳ:** Học kỳ I — Năm học 2026 - 2027  
* **Nhóm sinh viên thực hiện:** Nhóm 9  

| STT | Họ và tên sinh viên | Mã số sinh viên | Vai trò phụ trách |
| :---: | :--- | :---: | :--- |
| 1 | **Thân Hoàng Khoa** | **082206011685**|  Kỹ sư Dữ liệu, Can thiệp nhận thức & Hồ sơ Đạo đức)|
| 2 | **Nguyễn Hồ Hùng Phương** | **083206006476** | Nhóm trưởng / Kiến trúc sư ATTT & Giao diện Web |
| 3 | **Huỳnh Thanh Vũ** | **060207000288** | Chuyên viên Thống kê thực nghiệm & Phân tích SDT |

---

## 1. TỔNG QUAN ĐỀ TÀI & CÂU HỎI NGHIÊN CỨU

### 1.1. Bối cảnh
Sự bùng nổ của các mô hình ngôn ngữ lớn (LLMs / Generative AI) đã làm thay đổi hoàn toàn cục diện kỹ nghệ xã hội (Social Engineering). Kẻ tấn công có thể tự động hóa việc tạo ra các thông điệp lừa đảo (Phishing) không còn lỗi ngữ pháp hay từ ngữ vụng về, có tính cá nhân hóa sâu sắc, làm vô hiệu hóa các trực giác cảm quan truyền thống của con người.

Đồ án triển khai nghiên cứu thực nghiệm có kiểm soát nhằm đánh giá chính xác năng lực nhận diện của người dùng Việt Nam trước các thông điệp lừa đảo AI so với truyền thống, đồng thời đo lường hiệu quả thực tế của một can thiệp nhận thức ngắn (Quy tắc kiểm tra 4 bước và Xác minh ngoài băng OOB).

### 1.2. Ba câu hỏi nghiên cứu then chốt (Research Questions)
* **RQ1 (AI Phishing vs. Phishing truyền thống):** Khả năng nhận diện của con người đối với lừa đảo do AI hỗ trợ có khác biệt so với lừa đảo thủ công truyền thống không?
* **RQ2 (Hiệu quả can thiệp & SDT):** Sau khi được can thiệp nhận thức ngắn, người tham gia có thực sự nâng cao năng lực phân biệt tín hiệu ($d'$) hay chỉ thay đổi ngưỡng quyết định ($c$), dẫn tới hiện tượng "Báo động mệt mỏi" (Alert Fatigue)?
* **RQ3 (Dấu hiệu nhận diện & Bộ quy tắc):** Người dùng thực tế dựa vào những đặc điểm nào để phán đoán, và bộ phát hiện theo quy tắc kỹ thuật (Rule-based detector) có thể hỗ trợ khắc phục điểm mù nhận thức của con người như thế nào?

---

## 2. CẤU TRÚC THƯ MỤC DỰ ÁN

```
d:\ATTT/
├── docs/                                   # Toàn bộ tài liệu học thuật và minh chứng chính thức
│   ├── 01_De_Cuong_Nghien_Cuu.md           # Đề cương nghiên cứu chi tiết nộp phê duyệt
│   ├── 02_Phieu_Dong_Thuan_Va_An_Danh.md   # Hồ sơ an toàn đạo đức, ẩn danh hóa người tham gia
│   ├── 03_Tuyen_Bo_Su_Dung_AI.md           # Bảng công khai minh bạch sử dụng AI (AI Disclosure)
│   ├── 04_Verification_Checklist_OOB.md    # Danh mục kiểm tra 4 bước & Quy trình xác minh ngoài băng OOB
│   ├── 05_Bao_Cao_Do_An_ATTT_DeTai09.md    # Báo cáo đồ án toàn văn 8 chương chuẩn IEEE
│   ├── 06_Bang_Truy_Vet_Minh_Chung.md      # Ma trận truy vết minh chứng & Bảng phân công 3 SV
│   ├── BaoCao_DeTai9.docx                  # Tệp báo cáo Word chính thức của Nhóm 9
│   └── images/                             # Logo trường UTH và các biểu đồ thực nghiệm
├── data/                                   # Bộ dữ liệu thực nghiệm và kết quả đo lường
│   ├── khao_sat.csv                        # Bộ dữ liệu thực tế N=20 người tham gia (1.200 phản hồi)
│   ├── dataset_full.json                   # 60 mẫu thông điệp chuẩn hóa kèm đầy đủ metadata
│   ├── dataset_60_messages.json            # Bản phân phối 60 thông điệp giả lập
│   ├── dataset_60_messages.csv             # Bản phân phối 60 thông điệp dạng bảng CSV
│   ├── briefs_manual_filled.json           # Kịch bản gốc 30 mẫu thủ công do nhóm tự biên soạn
│   ├── pre_test_set_a.json                 # Bộ đề Pre-test Set A (30 thông điệp)
│   ├── post_test_set_b.json                # Bộ đề Post-test Set B (30 thông điệp)
│   └── *.png                               # Các biểu đồ khoa học đã xuất bản (300 DPI)
├── src/                                    # Mã nguồn kỹ thuật và công cụ phân tích
│   ├── statistical_analysis.py             # Script phân tích thống kê thực nghiệm & SDT (d', c)
│   ├── generate_synthetic_data.py          # Script cấu trúc và thẩm định 60 mẫu thông điệp
│   ├── simulate_survey_responses.py        # Module mô phỏng thử nghiệm kiểm thử
│   └── app/                                # Ứng dụng Web Khảo sát tương tác (Flask)
│       ├── app.py                          # Backend máy chủ Flask
│       ├── templates/index.html            # Giao diện web mô phỏng hòm thư email/tin nhắn
│       └── static/charts/                  # Biểu đồ trực quan hóa kết quả khảo sát
├── public/                                 # Bản Web tĩnh triển khai Jamstack (Netlify)
├── requirements.txt                        # Danh sách thư viện Python phụ thuộc
└── README.md                               # Tài liệu hướng dẫn cài đặt và vận hành hệ thống
```

---

## 3. THIẾT KẾ THỰC NGHIỆM & PHƯƠNG PHÁP LUẬN

1. **Thiết kế giai thừa $2 \times 2$ (Factorial Design):**
   * Tổng cộng 60 thông điệp chuẩn hóa, cân bằng tuyệt đối:
     * **30 Hợp lệ** (15 AI sinh, 15 Thủ công)
     * **30 Lừa đảo** (15 AI sinh, 15 Thủ công)
   * Chia thành 2 bộ tương đương độ khó: **Set A (Pre-test, 30 câu)** và **Set B (Post-test, 30 câu)**.
2. **Quy trình thử nghiệm Pre-test / Post-test:**
   * **Giai đoạn 1 (Pre-test):** Người tham gia đánh giá Set A theo trực giác sẵn có, ghi nhận phán đoán, thời gian ra quyết định ($T_{\text{decision}}$) và độ tự tin (thang 1 - 5).
   * **Can thiệp nhận thức:** Tiếp cận tài liệu hướng dẫn ngắn (Quy tắc kiểm tra 4 bước và Xác minh OOB).
   * **Giai đoạn 2 (Post-test):** Người tham gia tiếp tục đánh giá Set B để đo lường chuyển dịch nhận thức.
3. **Mô hình Lý thuyết Phát hiện Tín hiệu (Signal Detection Theory - SDT):**
   * Tách biệt năng lực phân biệt bản chất ($d'$) khỏi xu hướng tâm lý / thiên lệch quyết định (Criterion $c$).
   * Áp dụng hiệu chỉnh log-linear của Hautus (1995) để xử lý các tỷ lệ cực đoan (0% hoặc 100%).

---

## 4. KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG CHÍNH THỨC ($N = 20$)

Dữ liệu thực tế được thu thập đầy đủ từ **$N = 20$ người tham gia** (`P01` đến `P20`), tương ứng với **1.200 lượt đánh giá độc lập** (lưu tại `data/khao_sat.csv`):

### 4.1. Bảng so sánh chỉ số tổng thể (Overall Metrics)

| Chỉ số đánh giá | Trước can thiệp (Pre-test) | Sau can thiệp (Post-test) | Chênh lệch ($\Delta$) | Ý nghĩa an toàn |
| :--- | :---: | :---: | :---: | :--- |
| **Độ chính xác (Accuracy)** | **72.50%** | **68.83%** | **-3.67%** | Suy giảm nhẹ do tăng cảnh giác |
| **Tỷ lệ bắt lừa đảo (Recall / Hit Rate)** | **68.00%** | **72.67%** | **+4.67%** | Bắt được nhiều tin lừa đảo hơn |
| **Độ chuẩn xác (Precision)** | **74.73%** | **67.49%** | **-7.23%** | Giảm do nhiều tin hợp lệ bị nghi |
| **Báo động nhầm (False Positive Rate - FPR)** | **23.00%** | **35.00%** | **+12.00%** | Tăng vọt $\Rightarrow$ **Alert Fatigue** |
| **Bỏ lọt lừa đảo (False Negative Rate - FNR)** | **32.00%** | **27.33%** | **-4.67%** | Giảm tỷ lệ bị lừa |
| **Thời gian ra quyết định trung bình** | **22.08 giây** | **22.55 giây** | **+0.47 giây** | Cân nhắc kỹ hơn trước khi chọn |
| **Độ tự tin trung bình (thang 1 - 5)** | **3.48 / 5.0** | **3.50 / 5.0** | **+0.01** | Giữ vững tâm lý thận trọng |

### 4.2. Phân tích Lý thuyết Phát hiện Tín hiệu (SDT) — Giải đáp RQ2
* **Khả năng phân biệt ($d'$):** Giảm từ **$1.2019$** xuống **$0.9845$** ($\Delta d' = -0.2174$). Can thiệp ngắn chưa làm tăng ngay năng lực bóc tách tín hiệu tinh vi.
* **Ngưỡng quyết định (Criterion $c$):** Dịch chuyển mạnh từ **$+0.1349$** (thận trọng, thiên về coi là hợp lệ) sang **$-0.1083$** (nghi ngờ, thiên về coi là lừa đảo) với $\Delta c = -0.2432$.
* **Kết luận khoa học:** Can thiệp đào tạo ngắn không làm người dùng "thông minh hơn" về mặt kỹ thuật, mà chủ yếu **thay đổi hành vi và ngưỡng chấp nhận rủi ro**. Người dùng trở nên hoài nghi mọi thông điệp, dẫn đến tăng Recall bắt lừa đảo nhưng kéo theo hiện tượng **Báo động mệt mỏi (Alert Fatigue)** khi 35% email hợp lệ bị gắn cờ nhầm.

### 4.3. So sánh AI Phishing vs Phishing truyền thống — Giải đáp RQ1

| Loại thông điệp | Độ chính xác Pre-test | Độ chính xác Post-test | Đánh giá hành vi |
| :--- | :---: | :---: | :--- |
| **AI Phishing (Lừa đảo AI)** | **69.29%** | **70.00%** | Ngữ pháp chuẩn xác khiến người dùng khó phát hiện hơn ở pha đầu |
| **Traditional Phishing (Lừa đảo thủ công)** | **66.88%** | **75.71%** | Tăng mạnh sau khi được học các dấu hiệu hối thúc tâm lý (+8.83%) |
| **Legitimate (Thông điệp hợp lệ)** | **77.00%** | **65.00%** | Giảm 12% do người dùng nghi ngờ thái quá sau bài học |

### 4.4. Kiểm định giả thuyết thống kê
* **Paired Samples $t$-test:** $t = -1.5992, p = 0.1263 > 0.05$.
* **Wilcoxon Signed-Rank Test:** $W = 47.50, p = 0.0964 > 0.05$.
* **Ý nghĩa:** Sự suy giảm Accuracy không có ý nghĩa thống kê ở mức $\alpha = 0.05$, chứng minh đây là biến thiên tự nhiên do sự dịch chuyển ngưỡng quyết định ($c$), hoàn toàn phù hợp với mô hình SDT trong an toàn thông tin.

### 4.5. Hiệu năng của Bộ phát hiện theo quy tắc (Rule-Based Detector)
* Bộ phát hiện theo quy tắc kỹ thuật khách quan đạt **95.00% Accuracy** trên cùng 60 thông điệp, vượt trội so với độ chính xác trung bình của con người ($70.67\%$).
* Tuy nhiên, hệ thống kỹ thuật vẫn bỏ sót các kịch bản lừa đảo thuần tâm lý (quà tặng, kết bạn không chứa liên kết độc hại) mà con người lại nhận biết rất tốt.

---

## 5. HƯỚNG DẪN CÀI ĐẶT & TÁI TẠO KẾT QUẢ (1 LỆNH)

### Yêu cầu môi trường:
* Python 3.10 trở lên (Hỗ trợ tốt trên Python 3.10, 3.11, 3.12, 3.13, 3.14).
* Hệ điều hành: Windows, macOS hoặc Linux.

### Bước 1: Cài đặt các gói phụ thuộc
```bash
pip install -r requirements.txt
```

### Bước 2: Chạy phân tích thống kê & tự động xuất biểu đồ
```bash
python src/statistical_analysis.py
```
*Script sẽ tự động đọc `data/khao_sat.csv`, tính toán các chỉ số phân loại, tham số SDT ($d', c$), kiểm định thống kê và xuất 4 biểu đồ 300 DPI:*
1. `fig1_pre_post_metrics.png`: So sánh các chỉ số hiệu năng trước và sau can thiệp.
2. `fig2_ai_vs_traditional_accuracy.png`: So sánh độ chính xác giữa AI Phishing, Phishing thủ công và tin Hợp lệ.
3. `fig3_confusion_matrices.png`: Ma trận nhầm lẫn Pre-test vs Post-test.
4. `fig4_error_breakdown_by_indicators.png`: Tỷ lệ lỗi theo từng nhóm đòn bẩy thao túng tâm lý.

### Bước 3: Khởi chạy Ứng dụng Web Khảo sát mô phỏng (Local App)
```bash
python src/app/app.py
```
Truy cập trình duyệt tại: **`http://127.0.0.1:5000`** để trải nghiệm giao diện làm bài khảo sát, đọc tài liệu can thiệp và xem kết quả phân tích trực quan.

---

## 6. ĐỀ XUẤT KIỂM SOÁT PHÒNG VỆ TOÀN DIỆN

Từ kết quả thực nghiệm, đồ án kiến nghị mô hình bảo vệ 3 lớp:
1. **Lớp Kỹ thuật:** Triển khai bắt buộc SPF, DKIM, DMARC (`p=reject`), FIDO2/WebAuthn chống lừa đảo đánh cắp phiên, và bộ lọc phát hiện tên miền giả mạo (Lookalike domain).
2. **Lớp Quy trình:** Ban hành chuẩn **Quy trình xác minh ngoài băng (Out-of-Band - OOB)**:
   * Khi nhận được yêu cầu tài chính, chuyển tiền, hay cung cấp OTP/mật khẩu, **tuyệt đối không thao tác qua liên kết hoặc trả lời tin nhắn**.
   * Bắt buộc xác minh độc lập qua kênh tin cậy cấp 2 (gọi tổng đài chính thức in trên thẻ ngân hàng, gặp trực tiếp cán bộ phụ trách).
3. **Lớp Con người:** Đổi mới chương trình đào tạo nhận thức: chuyển từ việc "soi lỗi chính tả" sang "phản xạ hoài nghi trước áp lực thời gian, thẩm quyền giả mạo và yêu cầu thông tin nhạy cảm".

---

## 7. BẢNG MINH CHỨNG & ĐÓNG GÓP THÀNH VIÊN

Chi tiết bảng truy vết toàn bộ minh chứng kỹ thuật và đánh giá đóng góp công bằng (33.3% mỗi thành viên) được lưu trữ tại:
👉 **[`docs/06_Bang_Truy_Vet_Minh_Chung.md`](file:///d:/ATTT/docs/06_Bang_Truy_Vet_Minh_Chung.md)**

Tệp văn bản báo cáo đồ án Word chính thức của nhóm:
👉 **[`docs/BaoCao_DeTai9.docx`](file:///d:/ATTT/docs/BaoCao_DeTai9.docx)**

Bản báo cáo chi tiết Markdown chuẩn IEEE 8 chương:
👉 **[`docs/05_Bao_Cao_Do_An_ATTT_DeTai09.md`](file:///d:/ATTT/docs/05_Bao_Cao_Do_An_ATTT_DeTai09.md)**
