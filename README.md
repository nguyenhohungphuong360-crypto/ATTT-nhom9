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
| 1 | **Nguyễn Hồ Hùng Phương** | **083206006476** | Nhóm trưởng / Kiến trúc sư ATTT & Giao diện Web |
| 2 | **Thân Hoàng Khoa** | **082206011685** | Kỹ sư Dữ liệu, Can thiệp nhận thức & Hồ sơ Đạo đức |
| 3 | **Huỳnh Thanh Vũ** | **060207000288** | Chuyên viên Thống kê thực nghiệm & Phân tích SDT |

---

## 1. TỔNG QUAN ĐỀ TÀI & CÂU HỎI NGHIÊN CỨU

### 1.1. Bối cảnh nghiên cứu
Sự bùng nổ của các mô hình ngôn ngữ lớn (Generative AI / LLMs) đã làm thay đổi hoàn toàn diện mạo của các cuộc tấn công kỹ nghệ xã hội (Social Engineering). Kẻ tấn công giờ đây có thể tự động hóa việc tạo ra các thông điệp lừa đảo (Phishing) không còn lỗi ngữ pháp, văn phong chỉn chu theo chuẩn hành chính công vụ và cá nhân hóa sâu sắc, làm vô hiệu hóa hoàn toàn các "phao cứu sinh" nhận diện cảm quan truyền thống (như soi lỗi chính tả, câu từ ngô nghê).

Đồ án triển khai bài toán nghiên cứu thực nghiệm có kiểm soát nhằm đo lường chính xác năng lực nhận diện của người dùng trước các thông điệp lừa đảo AI so với truyền thống, đồng thời đánh giá hiệu quả thực tế của một can thiệp nhận thức ngắn (Quy tắc kiểm tra 4 bước và Xác minh ngoài băng OOB).

### 1.2. Ba câu hỏi nghiên cứu then chốt (Research Questions)
* **RQ1 (AI Phishing vs. Phishing truyền thống):** Khả năng nhận diện của con người đối với lừa đảo do AI hỗ trợ có khác biệt so với lừa đảo thủ công truyền thống không?
* **RQ2 (Hiệu quả can thiệp & SDT):** Hướng dẫn ngắn có thực sự nâng cao năng lực phân biệt tín hiệu ($d'$) hay chỉ dịch chuyển ngưỡng quyết định ($c$), dẫn tới hiện tượng "Báo động mệt mỏi" (Alert Fatigue)?
* **RQ3 (Dấu hiệu nhận diện & Điểm mù):** Người dùng thực tế dựa vào những đặc điểm nào để phán đoán, và bộ phát hiện theo quy tắc kỹ thuật (Rule-based detector) có thể hỗ trợ khắc phục điểm mù nhận thức của con người ra sao?

---

## 2. CẤU TRÚC THƯ MỤC DỰ ÁN

```
d:\ATTT/
├── docs/                                   # Toàn bộ tài liệu học thuật và minh chứng chính thức
│   ├── 01_De_Cuong_Nghien_Cuu.md           # Đề cương nghiên cứu chi tiết nộp phê duyệt Tuần 1
│   ├── 02_Phieu_Dong_Thuan_Va_An_Danh.md   # Hồ sơ an toàn đạo đức & kế hoạch ẩn danh hóa người tham gia
│   ├── 03_Tuyen_Bo_Su_Dung_AI.md           # Bảng công khai minh bạch sử dụng AI (AI Disclosure)
│   ├── 04_Verification_Checklist_OOB.md    # Danh mục kiểm tra 4 bước & Quy trình xác minh ngoài băng OOB
│   ├── 05_Bao_Cao_Do_An_ATTT_DeTai09.md    # Báo cáo đồ án toàn văn 8 chương Markdown chuẩn IEEE
│   ├── 06_Bang_Truy_Vet_Minh_Chung.md      # Ma trận truy vết minh chứng (MC-01 -> MC-08) & Phân công SV
│   ├── BaoCao_DeTai9.docx                  # Tệp báo cáo Word chính thức của Nhóm 9
│   ├── nhóm 9 ATTT.pptx                    # Tệp slide thuyết trình PowerPoint bảo vệ đồ án
│   └── images/                             # Logo UTH và các hình vẽ biểu đồ minh họa
├── data/                                   # Bộ dữ liệu thực nghiệm và kết quả đo lường
│   ├── khao_sat.csv                        # BỘ DỮ LIỆU THỰC TẾ CHÍNH THỨC N=20 (1.200 phản hồi)
│   ├── live_survey_responses.csv           # Nhật ký khảo sát trực tiếp (từ 20/10/2026 đến 02/11/2026)
│   ├── dataset_60_messages.json            # 60 thông điệp chuẩn hóa kèm đầy đủ metadata
│   ├── dataset_60_messages.csv             # 60 thông điệp định dạng bảng CSV
│   ├── briefs_manual_filled.json           # Kịch bản gốc 30 mẫu thủ công do nhóm tự biên soạn
│   ├── pre_test_set_a.json                 # Bộ đề Pre-test Set A (30 thông điệp)
│   ├── post_test_set_b.json                # Bộ đề Post-test Set B (30 thông điệp)
│   ├── sample_survey_results.csv           # Dữ liệu mô phỏng N=40 phục vụ kiểm thử thuật toán
│   └── fig*.png                            # 4 biểu đồ học thuật xuất bản độ phân giải cao (300 DPI)
├── src/                                    # Mã nguồn kỹ thuật và công cụ phân tích
│   ├── statistical_analysis.py             # Script phân tích thống kê thực nghiệm, SDT (d', c) & vẽ biểu đồ
│   ├── generate_synthetic_data.py          # Script cấu trúc, thẩm định và chuẩn hóa 60 mẫu thông điệp
│   ├── simulate_survey_responses.py        # Module mô phỏng thử nghiệm kiểm thử
│   └── app/                                # Ứng dụng Web Khảo sát tương tác (Flask Backend)
│       ├── app.py                          # Máy chủ Flask quản lý luồng khảo sát và ghi nhận log
│       ├── templates/index.html            # Giao diện web mô phỏng hòm thư email/tin nhắn
│       └── static/charts/                  # Biểu đồ hiển thị trên giao diện Web App
├── public/                                 # Bản Web tĩnh triển khai trực tuyến trên Netlify (Jamstack)
│   ├── index.html                          # Giao diện tương tác khảo sát trực tuyến
│   ├── data/                               # Dữ liệu phục vụ trình duyệt tải trực tiếp
│   └── charts/                             # Biểu đồ khoa học phục vụ hiển thị online
├── requirements.txt                        # Danh sách thư viện Python phụ thuộc
├── netlify.toml                            # Tệp cấu hình xuất bản tự động trên Netlify (publish = "public")
├── .gitignore                              # Cấu hình bỏ qua tệp tạm (.netlify/, __pycache__, .env)
├── DETAI ATTT HKI2627.pdf                  # Đề cương đồ án chính thức do Khoa ban hành
└── README.md                               # Tài liệu hướng dẫn tổng quan và vận hành hệ thống
```

---

## 3. THIẾT KẾ THỰC NGHIỆM & PHƯƠNG PHÁP LUẬN

1. **Thiết kế giai thừa $2 \times 2$ (Factorial Design):**
   * Tổng cộng 60 thông điệp chuẩn hóa, cân bằng tuyệt đối:
     * **30 Hợp lệ** (15 do AI sinh, 15 do Người viết tay).
     * **30 Lừa đảo** (15 do AI sinh, 15 do Người viết tay).
   * *Ý nghĩa:* Có 15 tin thật do AI viết giúp triệt tiêu hoàn toàn biến gây nhiễu về văn phong, ngăn chặn người tham gia học vẹt mẹo *"cứ thấy viết mượt là lừa đảo"*.
2. **Phân chia thành 2 bộ đề A và B có độ khó tương đương:**
   * **Set A (Pre-test, 30 câu):** 15 Hợp lệ (7 AI, 8 Thủ công) + 15 Lừa đảo (8 AI, 7 Thủ công).
   * **Set B (Post-test, 30 câu):** 15 Hợp lệ (8 AI, 7 Thủ công) + 15 Lừa đảo (7 AI, 8 Thủ công).
3. **Quy trình thực nghiệm Trong-nhóm (Within-subject):**
   * **Bước 1:** Ký cam kết đồng thuận tự nguyện, cấp mã ẩn danh (`P01` đến `P20`).
   * **Bước 2 (Pre-test):** Đánh giá 30 câu ở Bộ A theo thói quen tự nhiên.
   * **Bước 3 (Can thiệp):** Học tài liệu nhận thức 4 bước và quy trình xác minh ngoài băng OOB trong 5 – 7 phút.
   * **Bước 4 (Post-test):** Đánh giá 30 câu ở Bộ B để đo lường chuyển dịch nhận thức.
4. **Mô hình Lý thuyết Phát hiện Tín hiệu (Signal Detection Theory - SDT):**
   * Tách bạch giữa **năng lực phân biệt bản chất ($d'$)** và **ngưỡng quyết định tâm lý ($c$)**.
   * Áp dụng hiệu chỉnh log-linear của Hautus (1995) để tránh vô cực khi tỷ lệ đạt 0% hoặc 100%.
5. **Ranh giới an toàn quốc tế (RFC 2606):**
   * Toàn bộ tên miền dùng đuôi **`.test`** theo chuẩn RFC 2606 / RFC 6761 (không bao giờ phân giải IP thật trên Internet), tổ chức hư cấu, không gửi thư thật, không thu thập thông tin định danh (PII).

---

## 4. KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG CHÍNH THỨC ($N = 20$)

Dữ liệu thực nghiệm thực tế thu thập từ **$N = 20$ người tham gia** (`P01` đến `P20`) với **1.200 lượt đánh giá độc lập** (lưu tại `data/khao_sat.csv` và `data/live_survey_responses.csv`):

### 4.1. Bảng so sánh chỉ số tổng thể (Overall Metrics)

| Chỉ số đánh giá | Trước can thiệp (Pre-test) | Sau can thiệp (Post-test) | Chênh lệch ($\Delta$) | Ý nghĩa an toàn |
| :--- | :---: | :---: | :---: | :--- |
| **Độ chính xác (Accuracy)** | **72.50%** (SD: 7.16%) | **68.83%** (SD: 8.60%) | **-3.67%** | Suy giảm nhẹ do tăng nghi ngờ |
| **Khả năng bắt lừa đảo (Recall)** | **68.00%** | **72.67%** | **+4.67%** | Bắt được nhiều tin lừa đảo hơn |
| **Độ chuẩn xác (Precision)** | **74.73%** | **67.49%** | **-7.23%** | Giảm do nhiều tin thật bị nghi oan |
| **Báo động nhầm (FPR)** | **23.00%** | **35.00%** | **+12.00%** | Tăng vọt $\Rightarrow$ **Alert Fatigue** |
| **Bỏ lọt lừa đảo (FNR)** | **32.00%** | **27.33%** | **-4.67%** | Giảm tỷ lệ người dùng bị lừa |
| **Điểm F1-Score** | **71.20%** | **69.98%** | **-1.22%** | Cân bằng giữa Precision và Recall |
| **Thời gian ra quyết định trung bình** | **22.08 giây** | **22.55 giây** | **+0.47 giây** | Cân nhắc kỹ hơn trước khi chọn |
| **Độ tự tin trung bình (1 - 5)** | **3.48 / 5.0** | **3.50 / 5.0** | **+0.01** | Giữ vững thái độ thận trọng |

### 4.2. Phân tích Lý thuyết Phát hiện Tín hiệu (SDT) — Giải đáp RQ2
* **Năng lực phân biệt ($d'$):** Giảm từ **$1.2019$** xuống **$0.9845$** ($\Delta d' = -0.2174$). Hướng dẫn ngắn 5 phút không thể làm người dùng tăng ngay khả năng bóc tách kỹ thuật.
* **Ngưỡng quyết định ($c$):** Dịch chuyển mạnh từ **$+0.1349$** (thận trọng, thiên về coi là hợp lệ) sang **$-0.1083$** (hoài nghi cực đoan, coi mọi thứ là lừa đảo) với $\Delta c = -0.2432$.
* **Ý nghĩa khoa học:** Người dùng chuyển sang chiến thuật *"thà nghi nhầm còn hơn bỏ sót"*. Recall tăng nhưng kéo theo tỷ lệ báo động nhầm (FPR) nhảy vọt lên 35%, minh chứng thực nghiệm sống động cho hiện tượng **Alert Fatigue (Báo động mệt mỏi)**.

### 4.3. So sánh AI Phishing vs Phishing truyền thống — Giải đáp RQ1

| Loại thông điệp | Pre-test | Post-test | Đánh giá thực nghiệm |
| :--- | :---: | :---: | :--- |
| **AI Phishing (Lừa đảo do AI viết)** | **69.29%** | **70.00%** | Không làm người dùng dễ bị lừa hơn so với thủ công ($p = 0.77$). |
| **Traditional Phishing (Lừa đảo viết tay)** | **66.88%** | **75.71%** | Tăng mạnh sau khi được học các chiêu trò tâm lý (+8.83%). |
| **Legitimate (Thông điệp hợp lệ)** | **77.00%** | **65.00%** | Sụt giảm 12% do người dùng nghi ngờ cả thư thật khi thấy câu chữ quá chỉn chu. |

### 4.4. Phân tích dấu hiệu nhận biết & Điểm mù — Giải đáp RQ3
* **Dấu hiệu được dựa vào nhiều nhất:** Hối thúc thời gian (288 lần), Đòi OTP/mật khẩu (236 lần), URL nhái lookalike (229 lần), Giả mạo thẩm quyền (220 lần).
* **Điểm mù nhận thức:** Những lượt phán đoán mà người dùng dựa vào "chất lượng ngôn ngữ" chỉ đạt độ chính xác **66.3%** (thấp hơn hẳn mức 71.4% khi không xét văn phong).
* **Độ chính xác theo kênh:** SMS (**77.1%**) $>$ Zalo (**72.5%**) $>$ Email (**68.2%**).

### 4.5. Hiệu năng Bộ phát hiện theo quy tắc (Rule-Based Detector)
* Bộ quy tắc kỹ thuật đạt **95.00% Accuracy** (57/60 câu đúng), vượt xa mức trung bình 70.67% của con người.
* **Điểm mạnh:** Kiểm tra tên miền, cú pháp URL và định dạng file tuyệt đối không mệt mỏi.
* **Hạn chế:** Bỏ sót 1 tin tuyển dụng lừa đảo thuần tâm lý (`AI-P09`) mà 65% con người nhận ra; đồng thời báo nhầm 2 thư hợp lệ có nhắc "đăng nhập" (`MN-L10`, `MN-L11`).

### 4.6. Kiểm định giả thuyết thống kê
* **Paired Samples $t$-test:** $t = -1.5992, p = 0.1263 > 0.05$.
* **Wilcoxon Signed-Rank Test:** $W = 47.50, p = 0.0964 > 0.05$.
* **Kết luận:** Sự suy giảm nhẹ về Accuracy không có ý nghĩa thống kê ở mức $\alpha = 0.05$, hoàn toàn là hệ quả ngẫu nhiên của việc dịch chuyển ngưỡng quyết định ($c$ âm).

---

## 5. HƯỚNG DẪN CÀI ĐẶT & TÁI TẠO KẾT QUẢ (1 LỆNH)

### Yêu cầu môi trường:
* Python 3.10+ (Đã thử nghiệm thành công trên Python 3.10, 3.11, 3.12, 3.13, 3.14).
* Hệ điều hành: Windows, macOS hoặc Linux.

### Bước 1: Cài đặt các gói phụ thuộc
```bash
pip install -r requirements.txt
```

### Bước 2: Chạy phân tích thống kê & Tự động xuất biểu đồ
```bash
python src/statistical_analysis.py
```
*Script đọc trực tiếp `data/khao_sat.csv`, in toàn bộ bảng chỉ số, kiểm định thống kê và tự động xuất 4 biểu đồ 300 DPI:*
1. `fig1_pre_post_metrics.png`: So sánh chỉ số hiệu năng tổng thể Pre-test vs Post-test.
2. `fig2_ai_vs_traditional_accuracy.png`: So sánh độ chính xác AI Phishing vs Truyền thống vs Hợp lệ.
3. `fig3_confusion_matrices.png`: Ma trận nhầm lẫn chi tiết trước và sau can thiệp.
4. `fig4_error_breakdown_by_indicators.png`: Phân tích tỷ lệ lỗi theo từng nhóm đòn bẩy tâm lý.

### Bước 3: Khởi chạy Ứng dụng Web Khảo sát tương tác (Local)
```bash
python src/app/app.py
```
* Mở trình duyệt truy cập: **`http://127.0.0.1:5000`** để trải nghiệm làm bài khảo sát, đọc hướng dẫn và xem kết quả trực tiếp.

### Bước 4: Trải nghiệm bản Web tĩnh trực tuyến (Netlify)
* Ứng dụng Jamstack tĩnh đã được xuất bản trực tuyến tại:  
  👉 **[http://mellow-fairy-62602b.netlify.app](http://mellow-fairy-62602b.netlify.app)** *(Mật khẩu truy cập: `My-Drop-Site`)*

---

## 6. ĐỀ XUẤT KIỂM SOÁT PHÒNG VỆ TOÀN DIỆN

Từ kết quả thực nghiệm, đề tài đề xuất mô hình phòng vệ 3 lớp:
1. **Lớp Kỹ thuật (Giao cho máy):** Bắt buộc triển khai DMARC `p=reject`, SPF, DKIM, xác thực FIDO2/WebAuthn chống lừa đảo chiếm phiên, và bộ lọc phát hiện tên miền lookalike tự động.
2. **Lớp Quy trình (Loại bỏ cảm tính):** Chuẩn hóa **Quy trình xác minh ngoài băng (Out-of-Band - OOB)**:
   * Khi nhận được yêu cầu tài chính, chuyển tiền hoặc cung cấp mã OTP/mật khẩu, **tuyệt đối không bấm liên kết hay trả lời tin nhắn**.
   * Bắt buộc xác minh độc lập qua kênh tin cậy cấp 2 (gọi tổng đài dập nổi sau thẻ ATM hoặc gọi điện trực tiếp cho người quen bằng số cũ).
3. **Lớp Con người (Tập trung vào tâm lý):** Chấm dứt dạy nhân viên "soi lỗi chính tả". Huấn luyện phản xạ hoài nghi trước áp lực thời gian, thẩm quyền giả mạo và mồi chài lợi ích.

---

## 7. BẢNG MINH CHỨNG & DANH MỤC TÀI LIỆU CHÍNH THỨC

* 📑 **Báo cáo đồ án toàn văn 8 chương chuẩn IEEE:**  
  👉 [`docs/05_Bao_Cao_Do_An_ATTT_DeTai09.md`](file:///d:/ATTT/docs/05_Bao_Cao_Do_An_ATTT_DeTai09.md)
* 📘 **Tệp văn bản báo cáo Word chính thức của Nhóm 9:**  
  👉 [`docs/BaoCao_DeTai9.docx`](file:///d:/ATTT/docs/BaoCao_DeTai9.docx)
* 🖥️ **Slide thuyết trình bảo vệ đồ án PowerPoint:**  
  👉 [`docs/nhóm 9 ATTT.pptx`](file:///d:/ATTT/docs/nh%C3%B3m%209%20ATTT.pptx)
* 📊 **Bảng truy vết minh chứng kỹ thuật & Đóng góp thành viên (33.3%):**  
  👉 [`docs/06_Bang_Truy_Vet_Minh_Chung.md`](file:///d:/ATTT/docs/06_Bang_Truy_Vet_Minh_Chung.md)
* 📁 **Kho dữ liệu thực nghiệm thực tế ($N=20$, 1.200 phản hồi):**  
  👉 [`data/khao_sat.csv`](file:///d:/ATTT/data/khao_sat.csv) và [`data/live_survey_responses.csv`](file:///d:/ATTT/data/live_survey_responses.csv)
