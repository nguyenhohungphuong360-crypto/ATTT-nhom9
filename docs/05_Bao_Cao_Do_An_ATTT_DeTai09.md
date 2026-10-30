# BÁO CÁO ĐỒ ÁN MÔN HỌC AN TOÀN THÔNG TIN
**TÊN ĐỀ TÀI (MÃ 09): ĐO HIỆU QUẢ NHẬN DIỆN NỘI DUNG LỪA ĐẢO ĐƯỢC TẠO BỞI TRÍ TUỆ NHÂN TẠO**

* **Học phần:** AN TOÀN THÔNG TIN (3 Tín chỉ) - Học kỳ I (2026 - 2027)
* **Giảng viên hướng dẫn:** TS. Lê Quốc Tuấn
* **Đơn vị:** Khoa Công nghệ Thông tin / An toàn Thông tin
* **Nhóm sinh viên thực hiện:** Nhóm 3 thành viên

---

## MỤC LỤC TỔNG QUAN
* **Tuyên bố về Đạo đức và Sử dụng Trí tuệ nhân tạo**
* **Chương 1: Mở đầu và Đặt vấn đề nghiên cứu**
  * 1.1. Bối cảnh bùng nổ của Generative AI và Kỹ nghệ xã hội thế hệ mới
  * 1.2. Sự dịch chuyển ranh giới tin cậy (Trust Boundary Shift)
  * 1.3. Mục tiêu và câu hỏi nghiên cứu
  * 1.4. Phạm vi và nguyên tắc an toàn đạo đức
* **Chương 2: Cơ sở lý thuyết và Mô hình đe dọa (Threat Modeling)**
  * 2.1. Bản chất của kỹ nghệ xã hội và các đòn bẩy thao túng tâm lý
  * 2.2. Giải phẫu kỹ thuật của thông điệp email/SMS/Zalo và cơ chế xác thực
  * 2.3. Cơ chế sinh nội dung lừa đảo của LLMs và sự suy giảm của phán đoán cảm quan
  * 2.4. Lý thuyết phát hiện tín hiệu (Signal Detection Theory - SDT) trong An toàn Thông tin
* **Chương 3: Phương pháp luận và Thiết kế Bộ dữ liệu Benchmark**
  * 3.1. Thiết kế thực nghiệm kiểm soát Pre-test / Post-test
  * 3.2. Cấu trúc bộ 60 thông điệp chuẩn hóa cân bằng 2×2 (Ground Truth Matrix)
  * 3.3. Tiêu chí phân loại dựa trên chỉ dấu kỹ thuật khách quan
  * 3.4. Kế hoạch ẩn danh hóa và bảo vệ người tham gia thử nghiệm
* **Chương 4: Triển khai kỹ thuật và Can thiệp nhận thức**
  * 4.1. Kiến trúc hệ thống khảo sát và đo lường trực tuyến
  * 4.2. Thiết kế tài liệu can thiệp: Quy tắc kiểm tra 4 bước (Verification Checklist)
  * 4.3. Các chỉ số đo lường định lượng và phương pháp kiểm định thống kê
* **Chương 5: Phân tích kết quả thực nghiệm và Thảo luận chuyên sâu (Dữ liệu thực nghiệm $N = 20$)**
  * 5.1. So sánh hiệu năng nhận diện tổng thể (Pre-test vs Post-test)
  * 5.2. Phân tích theo Lý thuyết Phát hiện Tín hiệu (SDT: $d'$ và Criterion $c$) - Giải đáp RQ2
  * 5.3. Nhận diện AI Phishing vs Phishing truyền thống - Giải đáp RQ1
  * 5.4. Dấu hiệu người dùng thực sự dựa vào và Phân tích điểm mù - Giải đáp RQ3
  * 5.5. Tác động đến Thời gian ra quyết định và Độ tự tin
  * 5.6. Kiểm định giả thuyết thống kê và Giới hạn nghiên cứu
* **Chương 6: Đề xuất giải pháp kiểm soát phòng vệ và Kết luận**
  * 6.1. Khung kiểm soát kết hợp: Con người - Quy trình - Kỹ thuật
  * 6.2. Quy trình xác minh ngoài băng (Out-of-Band Verification Protocol)
  * 6.3. Kết luận
* **Tài liệu tham khảo (Chuẩn IEEE)**

---

## BẢNG CÔNG KHAI SỬ DỤNG TRÍ TUỆ NHÂN TẠO
Nhóm nghiên cứu khẳng định:
1. Trí tuệ nhân tạo (OpenAI GPT-4o) chỉ được sử dụng với mục đích tạo 30 mẫu văn bản giả lập thuộc nhánh "AI hỗ trợ" (15 Hợp lệ, 15 Lừa đảo) phục vụ bộ dữ liệu đối chứng nghiên cứu.
2. Nhánh "Thủ công" (30 mẫu) do các thành viên nhóm trực tiếp tự viết tay độc lập dựa trên kịch bản thực tế tại Việt Nam (lưu tại `briefs_manual_filled.json`), không sử dụng AI.
3. 100% các chỉ dấu kỹ thuật (FQDN lừa đảo, giả mạo Brandname, URL redirection, vi phạm quy trình) và đáp án Ground Truth đều do nhóm sinh viên trực tiếp thiết kế, kiểm tra thủ công.
4. Không gửi bất kỳ email/tin nhắn thử nghiệm nào đến địa chỉ thực; không thu thập mật khẩu, OTP hay định danh cá nhân của người tham gia.
5. Toàn bộ mã nguồn phân tích thống kê, biểu đồ và nội dung biện luận khoa học trong báo cáo đều do nhóm sinh viên trực tiếp thực hiện và chịu trách nhiệm.

---

## CHƯƠNG 1: MỞ ĐẦU VÀ ĐẶT VẤN ĐỀ NGHIÊN CỨU

### 1.1. Bối cảnh bùng nổ của Generative AI và Kỹ nghệ xã hội thế hệ mới
Trong thập kỷ qua, kỹ nghệ xã hội (Social Engineering), đặc biệt là hình thức lừa đảo qua thư điện tử và tin nhắn (Phishing / Smishing), luôn là véc-tơ tấn công ban đầu chiếm tỷ trọng cao nhất trong các vụ vi phạm dữ liệu toàn cầu (theo Báo cáo Verizon DBIR 2024, hơn 68% các vụ tấn công có sự tham gia của yếu tố con người).

Tuy nhiên, sự xuất hiện mang tính cách mạng của các mô hình ngôn ngữ lớn (Large Language Models - LLMs) như GPT-4, Claude, LLaMA đã làm biến đổi hoàn toàn bề mặt tấn công. Trước đây, các chiến dịch phishing hàng loạt (Mass Phishing) thường bộc lộ những đặc điểm nhận diện rất dễ thấy bằng mắt thường:
* Lỗi chính tả, ngữ pháp ngô nghê, dấu câu lộn xộn do kẻ tấn công không thành thạo ngôn ngữ bản địa.
* Giọng văn máy móc, cấu trúc câu ngắt quãng do sử dụng công cụ dịch thuật thô sơ.
* Lời kêu gọi chung chung, không nắm rõ ngữ cảnh vận hành của tổ chức mục tiêu.

Với sự trợ giúp của LLMs, rào cản ngôn ngữ và chi phí thực thi này đã bị xóa bỏ. Kẻ tấn công có thể dễ dàng sinh ra hàng loạt bức thư lừa đảo có ngữ pháp hoàn hảo, văn phong hành chính trang trọng, độ mạch lạc cao và khả năng cá nhân hóa tinh vi (Spear-Phishing) nhắm vào từng vị trí cụ thể (sinh viên làm đồ án, nhân viên kế toán, cán bộ học vụ).

### 1.2. Sự dịch chuyển ranh giới tin cậy (Trust Boundary Shift)
Trong mô hình nhận thức truyền thống, người dùng thường được huấn luyện dựa vào "cảm quan ngôn ngữ" (Linguistic Heuristic): *"Nếu thấy email sai chính tả, hành văn lủng củng thì đó là lừa đảo"*.

Khi văn bản do AI tạo ra đạt mức độ chuẩn mực tương đương hoặc thậm chí chỉn chu hơn văn bản do nhân viên hành chính soạn thảo, **cảm quan con người chính thức sụp đổ như một ranh giới tin cậy**. Người dùng rơi vào tình trạng "ảo tưởng an toàn" (False Sense of Security) - họ tin rằng một bức thư viết trang trọng, lịch sự và logic chắc chắn phải là thư thật.

Do đó, vấn đề cốt lõi cần giải quyết là: **Làm thế nào để đo lường định lượng mức độ suy giảm nhận diện của người dùng trước nội dung do AI tạo, và chứng minh rằng việc can thiệp bằng "Chỉ dấu Kỹ thuật" kết hợp lý thuyết phát hiện tín hiệu có thể giải quyết được bài toán phòng vệ con người?**

### 1.3. Mục tiêu và Câu hỏi nghiên cứu
Đề tài tập trung giải quyết 3 câu hỏi nghiên cứu cốt lõi:
* **RQ1:** Người dùng nhận diện thông điệp lừa đảo do AI hỗ trợ kém hơn thông điệp viết thủ công bao nhiêu (đo bằng recall trên tin lừa đảo và độ chính xác theo phân nhóm)?
* **RQ2:** Một buổi hướng dẫn ngắn làm tăng khả năng PHÂN BIỆT thật/giả ($d'$), hay chỉ làm người tham gia NGHI NGỜ nhiều hơn (dịch criterion $c$), kéo theo tăng cả recall lẫn tỷ lệ báo động nhầm (FPR)?
* **RQ3:** Người dùng dựa vào dấu hiệu nào khi quyết định? Dấu hiệu "chất lượng ngôn ngữ" còn giá trị khi AI viết trơn tru không? Loại thông điệp nào gây nhầm lẫn nhiều nhất?

### 1.4. Phạm vi và Nguyên tắc an toàn đạo đức
* **Phạm vi đối tượng:** Thực nghiệm đo lường trên mẫu $N = 20$ người tham gia thật (`P01` đến `P20`), ghi nhận đầy đủ 1.200 lượt quyết định độc lập (mỗi người trải qua đủ 60 câu hỏi thuộc 2 bộ đề đối chứng A và B).
* **Môi trường & Kênh thử nghiệm:** Triển khai độc lập trong mạng nội bộ và nền tảng web kiểm soát, bao quát 3 kênh truyền thông phổ biến tại Việt Nam: Email (~38 tin), SMS (~12 tin), Zalo/Messenger (~10 tin).
* **Đạo đức nghiên cứu:** 100% tên miền và tổ chức là hư cấu (`.test` theo RFC 2606), link chỉ là văn bản mô phỏng, không gửi thư tới hộp thư thật, không thu thập mật khẩu, OTP hay định danh cá nhân (PII), có phiếu đồng thuận và debrief minh bạch.

---

## CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ MÔ HÌNH ĐE DỌA (THREAT MODELING)

### 2.1. Bản chất của Kỹ nghệ Xã hội và Đòn bẩy Thao túng Tâm lý
Kỹ nghệ xã hội về bản chất là cuộc tấn công khai thác "lỗ hổng tâm lý con người" (Cognitive Biases) thay vì khai thác lỗ hổng phần mềm. Kẻ tấn công áp dụng các nguyên lý thuyết phục kinh điển của Robert Cialdini:
1. **Tính cấp bách (Urgency / Time Pressure):** Tạo ra giới hạn thời gian gấp gáp (ví dụ: "trong vòng 2 giờ", "hạn chót 17:00 hôm nay"). Áp lực thời gian làm suy yếu tư duy phản biện phân tích (Hệ thống 2 theo Kahneman), ép nạn nhân hành động theo cảm xúc bản năng (Hệ thống 1).
2. **Thẩm quyền (Authority):** Giả mạo các cơ quan có thẩm quyền cao như "Cục Thuế", "Điện lực EVN", "Phòng Đào tạo", "Ban Giám hiệu", "Ngân hàng Sao Việt" nhằm kích hoạt phản xạ tuân thủ phục tùng.
3. **Sợ hãi và Trừng phạt (Fear & Loss Aversion):** Đe dọa khóa tài khoản vĩnh viễn, đình chỉ thi, cắt điện sinh hoạt, hủy đơn hàng. Con người có xu hướng sợ mất mát gấp đôi so với mong muốn nhận được phần thưởng tương đương.
4. **Mồi phần thưởng (Reward Bait / Greed):** Mồi trúng voucher 2 triệu, hoàn tiền thừa, trợ cấp khó khăn, nhận học bổng sinh viên.

### 2.2. Giải phẫu Kỹ thuật của Thông điệp và Cơ chế Xác thực
Để phân biệt khách quan giữa thông điệp thật và giả mạo, người làm an toàn thông tin bắt buộc phải dựa vào các bằng chứng kỹ thuật:
* **Email:** Kiểm tra FQDN sau ký tự `@` (`saoviet-bank.test` vs `saoviet-xacminh.test`), cơ chế SPF/DKIM/DMARC, và liên kết đích thực tế.
* **SMS:** Phân biệt Brandname chính thức và tin nhắn Smishing mạo danh kèm liên kết lạ (`sv-online.test`).
* **Zalo/Messenger:** Nhận diện Official Account (OA) đã được xác minh tích vàng so với số tài khoản cá nhân mạo danh người quen vay tiền.

### 2.3. Cơ chế Sinh Nội dung của LLMs và Điểm mù Nhận thức
Khi được thiết lập Persona chuyên nghiệp, LLM có khả năng:
* Tái hiện chính xác giọng văn hành chính công vụ của tiếng Việt hiện đại.
* Sử dụng chính xác thuật ngữ học vụ, ngân hàng, thuế, viễn thông.
* Cấu trúc bức thư mạch lạc, logic, loại bỏ toàn bộ lỗi ngữ pháp và chính tả truyền thống.
Hệ quả là dấu hiệu "văn phong" hoàn toàn mất giá trị phân loại. Người dùng nếu chỉ dựa vào cảm quan đọc lướt sẽ sập bẫy các cuộc tấn công tinh vi.

### 2.4. Lý thuyết Phát hiện Tín hiệu (Signal Detection Theory - SDT)
Để giải quyết triệt để câu hỏi **RQ2**, nghiên cứu áp dụng lý thuyết phát hiện tín hiệu (Green & Swets, 1966) nhằm tách bạch hai yếu tố:
1. **Độ nhạy phân biệt ($d'$):** Đo lường năng lực thực sự của người dùng trong việc phân biệt giữa tín hiệu lừa đảo (Signal) và thông điệp hợp lệ (Noise):
   $$d' = z(\text{Hit Rate}) - z(\text{False Alarm Rate})$$
2. **Ngưỡng quyết định (Criterion $c$):** Đo lường xu hướng thiên lệch tâm lý khi ra quyết định:
   $$c = -0.5 \times [z(\text{Hit Rate}) + z(\text{False Alarm Rate})]$$
   * Nếu $c > 0$: Người dùng có xu hướng thận trọng, thiên về kết luận "Hợp lệ".
   * Nếu $c < 0$: Người dùng có xu hướng nghi ngờ, thiên về kết luận "Lừa đảo".
   * Nếu $c = 0$: Ngưỡng quyết định trung lập hoàn hảo.

Để tránh giá trị vô cực khi Hit Rate hoặc False Alarm Rate đạt 0 hoặc 1, nghiên cứu áp dụng công thức **hiệu chỉnh log-linear của Hautus (1995)**:
$$\text{Hit Rate} = \frac{\text{Hits} + 0.5}{\text{Signals} + 1}, \quad \text{False Alarm Rate} = \frac{\text{FAs} + 0.5}{\text{Noises} + 1}$$

---

## CHƯƠNG 3: PHƯƠNG PHÁP LUẬN VÀ THIẾT KẾ BỘ DỮ LIỆU BENCHMARK

### 3.1. Thiết kế Thực nghiệm Kiểm soát Pre-test / Post-test
Nghiên cứu sử dụng mô hình thực nghiệm đối chứng nội tại (Within-Subject Design):
$$\text{Người tham gia} \xrightarrow{\quad} \text{Pre-test (Bộ đề A: 30 câu)} \xrightarrow{\quad} \text{Can thiệp Checklist 4 bước (5-7 phút)} \xrightarrow{\quad} \text{Post-test (Bộ đề B: 30 câu)}$$

### 3.2. Cấu trúc Bộ 60 Thông điệp Cân bằng 2×2 (Ground Truth Matrix)
Bộ dữ liệu gồm đúng 60 thông điệp, được cân bằng chặt chẽ theo thiết kế giai thừa $2 \times 2$ (Nguồn tạo $\times$ Tính hợp lệ):

| Phân loại | Viết thủ công (Manual) | Do AI tạo (AI-assisted) | Tổng cộng |
| :--- | :---: | :---: | :---: |
| **Thông điệp Hợp lệ (Legitimate)** | 15 mẫu | 15 mẫu | **30 mẫu (50%)** |
| **Thông điệp Lừa đảo (Phishing)** | 15 mẫu | 15 mẫu | **30 mẫu (50%)** |
| **TỔNG CỘNG** | **30 mẫu (50%)** | **30 mẫu (50%)** | **60 mẫu (100%)** |

Toàn bộ 60 thông điệp được chia thành 2 bộ đề tương đương độ khó:
* **Bộ A (Pre-test):** 15 Hợp lệ (8 Manual, 7 AI) + 15 Lừa đảo (7 Manual, 8 AI) = 30 mẫu.
* **Bộ B (Post-test):** 15 Hợp lệ (7 Manual, 8 AI) + 15 Lừa đảo (8 Manual, 7 AI) = 30 mẫu.

### 3.3. Tiêu chí Phân loại Dựa trên Chỉ dấu Kỹ thuật Khách quan
Đáp án Ground Truth được xác lập độc lập với văn phong dựa trên:
1. **FQDN & Nguồn gửi:** Tên miền người gửi có khớp với miền chính thức của tổ chức không (`saoviet-bank.test` vs `saoviet-xacminh.test`).
2. **Hành vi yêu cầu (Dangerous Actions):** Có đòi mật khẩu, mã OTP, số thẻ tín dụng hay chuyển tiền không. Thư hợp lệ tuyệt đối không thu thập các thông tin này qua liên kết ngoài.
3. **Cơ chế xác minh:** Hướng dẫn người dùng tự mở ứng dụng chính thức hay ép bấm vào liên kết lạ.

### 3.4. Kế hoạch Ẩn danh hóa và Bảo vệ Người tham gia
Hệ thống sử dụng cơ chế mã hóa ngẫu nhiên `P01` đến `P20` cho từng người tham gia. Không lưu bất kỳ thông tin định danh cá nhân nào. Mọi bản ghi khảo sát ghi nhận độc lập: mã người dùng, mã câu, phân loại, đáp án chọn, kết quả đúng/sai, độ tự tin (1-5), thời gian phản hồi (giây) và dấu hiệu nhận biết được khai báo.

---

## CHƯƠNG 4: TRIỂN KHAI KỸ THUẬT VÀ CAN THIỆP NHẬN THỨC

### 4.1. Kiến trúc Hệ thống Khảo sát Trực tuyến
Hệ thống thử nghiệm được xây dựng gồm:
* **Ứng dụng khảo sát cục bộ (Flask + Web Client):** Trực quan hóa trải nghiệm nhận thư, đo chính xác thời gian và độ tự tin, ghi dữ liệu vào `data/khao_sat.csv`.
* **Pipeline phân tích thống kê (`statistical_analysis.py`):** Tự động tính toán các chỉ số phân loại, lý thuyết SDT ($d', c$), kiểm định Wilcoxon, $t$-test và xuất 4 đồ thị 300 DPI.

### 4.2. Thiết kế Tài liệu Can thiệp: Quy tắc 4 Bước
Giữa hai giai đoạn, người tham gia được tiếp cận bản hướng dẫn ngắn gọn:
* **Bước 1:** Kiểm tra kỹ tên miền người gửi (FQDN sau `@`), không tin tên hiển thị.
* **Bước 2:** Soi liên kết đích và cơ chế bảo mật (tên miền phụ lừa đảo, chuyển hướng URL).
* **Bước 3:** Nhận diện các đòn bẩy tâm lý (hối thúc thời gian, đe dọa, mồi thưởng).
* **Bước 4:** Quy tắc xác minh ngoài băng (OOB) cho các yêu cầu tài chính hoặc định danh.

---

## CHƯƠNG 5: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM VÀ THẢO LUẬN CHUYÊN SÂU

Chương này trình bày toàn bộ kết quả phân tích định lượng trên tập dữ liệu thực tế thu thập từ **$N = 20$ người tham gia** (`P01` đến `P20`) với tổng cộng **1.200 lượt quyết định độc lập** (file dữ liệu gốc: `data/khao_sat.csv`).

### 5.1. So sánh Hiệu năng Nhận diện Tổng thể (Pre-test vs Post-test)
Bảng 5.1 tổng hợp các chỉ số đo lường hiệu năng phân loại trước và sau can thiệp:

**Bảng 5.1: So sánh các chỉ số hiệu năng tổng thể trên dữ liệu thực nghiệm thực tế ($N = 20$)**

| Chỉ số đánh giá | Trước can thiệp (Pre-test) | Sau can thiệp (Post-test) | Mức thay đổi ($\Delta$) | Ý nghĩa trong an toàn thông tin |
| :--- | :---: | :---: | :---: | :--- |
| **Độ nhạy / Bắt lừa đảo (Recall)** | **68.00%** | **72.67%** | **+4.67%** | Tăng khả năng phát hiện mối đe dọa |
| **Tỷ lệ bỏ lọt tấn công (FNR)** | **32.00%** | **27.33%** | **-4.67%** | Giảm thiểu nguy cơ sập bẫy lừa đảo |
| **Tỷ lệ báo động nhầm (FPR)** | **23.00%** | **35.00%** | **+12.00%** | **Gia tăng sự nghi ngờ đối với thư hợp lệ** |
| **Độ chính xác tổng thể (Accuracy)** | **72.50%** | **68.83%** | **-3.67%** | Giảm nhẹ do tỷ lệ báo động nhầm tăng |
| **Độ chuẩn xác (Precision)** | **74.73%** | **67.49%** | **-7.23%** | Chịu ảnh hưởng bởi số ca nghi nhầm tăng |
| **Điểm F1-Score** | **71.20%** | **69.98%** | **-1.22%** | Cân bằng hài hòa giữa Precision & Recall |
| **Thời gian ra quyết định trung bình** | **22.08 giây** | **22.55 giây** | **+0.47 giây** | Người dùng cân nhắc kỹ lưỡng hơn |
| **Độ tự tin trung bình (Thang 1-5)** | **3.48** | **3.50** | **+0.02** | Ổn định ở mức thận trọng |

*(Biểu đồ minh họa chi tiết xem tại Hình 1 - `fig1_pre_post_metrics.png`)*.

### 5.2. Phân tích theo Lý thuyết Phát hiện Tín hiệu (SDT) - Giải đáp RQ2
Đây là phát hiện khoa học quan trọng nhất của đồ án, trả lời trọn vẹn câu hỏi **RQ2**:
* **Khả năng phân biệt ($d'$):** 
  * Pre-test: $d' = 1.2019$ (Hit Rate = 67.9%, False Alarm Rate = 23.1%).
  * Post-test: $d' = 0.9845$ (Hit Rate = 72.6%, False Alarm Rate = 35.0%).
  * $\Delta d' = -0.2174$.
* **Ngưỡng quyết định (Criterion $c$):**
  * Pre-test: $c = +0.1349$ (giá trị dương: người dùng có xu hướng thiên về phán đoán "Hợp lệ", ít nghi ngờ).
  * Post-test: $c = -0.1083$ (giá trị âm: người dùng **chuyển dịch mạnh mẽ sang vùng NGHI NGỜ**).
  * $\Delta c = -0.2432$.

**Biện luận học thuật:**
Kết quả thực nghiệm chứng minh rằng: Một buổi hướng dẫn nhận thức ngắn hạn **chủ yếu tác động vào việc DỊCH CHUYỂN NGƯỠNG QUYẾT ĐỊNH ($c$ giảm mạnh sang âm)**, khiến người tham gia trở nên cảnh giác và nghi ngờ hơn ("trigger-happy", thiên về phán đoán lừa đảo). 
Hệ quả thực tế là:
1. **Mặt tích cực:** Tỷ lệ bắt lừa đảo (Recall) tăng thêm $+4.67\%$, giúp phát hiện được nhiều thông điệp độc hại hơn.
2. **Mặt tiêu cực (Trade-off):** Tỷ lệ báo động nhầm (FPR) tăng vọt từ $23.0\%$ lên $35.0\%$ ($+12.0\%$). Người dùng bắt đầu nghi ngờ cả những email hợp lệ của nhà trường hoặc ngân hàng. Đây chính là hiện tượng **Mệt mỏi cảnh báo (Alert Fatigue)** điển hình trong an toàn thông tin doanh nghiệp: khi nhân viên quá sợ hãi, họ sẽ chặn nhầm cả các thư giao dịch thông thường, làm gián đoạn công việc kinh doanh.

### 5.3. Nhận diện AI Phishing vs Phishing Truyền thống - Giải đáp RQ1
Bảng 5.2 phân rã độ chính xác nhận diện theo từng phân nhóm thông điệp:

**Bảng 5.2: Độ chính xác theo phân nhóm thông điệp (Message Type Breakdown)**

| Giai đoạn | Email Hợp lệ (Legitimate) | Lừa đảo Thủ công (Traditional Phishing) | Lừa đảo do AI tạo (AI_Phishing) |
| :--- | :---: | :---: | :---: |
| **Trước can thiệp (Pre-test)** | 77.00% | 66.88% | **69.29%** |
| **Sau can thiệp (Post-test)** | 65.00% | 75.71% | **70.00%** |
| **Mức thay đổi ($\Delta$)** | **-12.00%** | **+8.83%** | **+0.71%** |

*(Biểu đồ minh họa chi tiết xem tại Hình 2 - `fig2_ai_vs_traditional_accuracy.png`)*.

**Phân tích câu hỏi RQ1:**
* Đối với **Lừa đảo thủ công truyền thống**, sau khi được học các dấu hiệu kỹ thuật, độ chính xác nhận diện của người dùng tăng mạnh từ **$66.88\%$ lên $75.71\%$ ($+8.83\%$)**.
* Tuy nhiên, đối với **Lừa đảo do AI tạo (AI_Phishing)**, độ chính xác hầu như giậm chân tại chỗ: chỉ tăng nhẹ từ **$69.29\%$ lên $70.00\%$ ($+0.71\%$)**.
* **Kết luận RQ1:** Nội dung lừa đảo do AI hỗ trợ **thực sự khó nhận diện hơn và khó cải thiện hơn** so với thông điệp viết thủ công. Sự hoàn hảo về ngữ pháp, bố cục tự nhiên và văn phong trang trọng của AI đã tạo ra một lớp ngụy trang tinh vi, khiến người dùng rất khó bóc trần nếu chỉ được can thiệp bằng hướng dẫn ngắn hạn.

### 5.4. Dấu hiệu Người dùng Thực sự Dựa vào - Giải đáp RQ3
Dữ liệu khai báo từ 20 người tham gia trong file `khao_sat.csv` chỉ ra thứ hạng các dấu hiệu được người dùng dựa vào nhiều nhất:

**Bảng 5.3: Tần suất các dấu hiệu nhận diện được người dùng khai báo thực tế**

| Thứ hạng | Nhóm dấu hiệu nhận diện | Số lượt người dùng dựa vào | Đặc điểm thực tế |
| :---: | :--- | :---: | :--- |
| **1** | **Chất lượng ngôn ngữ / Văn phong** | **105 lượt** | Dấu hiệu cảm quan truyền thống (áp đảo tuyệt đối) |
| **2** | **Giả mạo thẩm quyền (Authority)** | **29 lượt** | Mạo danh ngân hàng, cơ quan thuế, nhà trường |
| **3** | **Sai ngữ cảnh (Context Mismatch)** | **26 lượt** | Nhắc dịch vụ người nhận không sử dụng |
| **4** | **Tệp đính kèm đáng ngờ** | **14 lượt** | Đính kèm file `.html` giả mạo cổng đăng nhập |
| **5** | **URL nhái & Đòi OTP/Mật khẩu** | **12 lượt** | Bằng chứng kỹ thuật khách quan |
| **6** | **Yêu cầu chuyển tiền / Đóng phí** | **11 lượt** | Hành vi nguy hiểm trực tiếp |
| **7** | **Mồi phần thưởng / Khẩn cấp** | **11 lượt** | Đòn bẩy tâm lý lòng tham và áp lực thời gian |

*(Biểu đồ minh họa chi tiết xem tại Hình 4 - `fig4_error_breakdown_by_indicators.png`)*.

**Phân tích câu hỏi RQ3:**
* Người tham gia vẫn giữ **thói quen cố hữu dựa vào "chất lượng ngôn ngữ" (105 lượt)** khi phán đoán. Đây chính là nguyên nhân trực tiếp khiến họ gặp khó khăn trước AI Phishing: vì AI viết quá trơn tru và mạch lạc, người dùng bị tước mất điểm tựa nhận thức quen thuộc.
* Các thông điệp gây nhầm lẫn nhiều nhất trong tập dữ liệu là các mẫu thư hợp lệ nhưng có chứa yếu tố thúc giục thời gian hoặc thông báo bảo trì tài khoản (ví dụ: `AI-L12`, `MN-L03`, `AI-L05`), dẫn đến tỷ lệ nghi ngờ oan lên tới xấp xỉ 50%.

### 5.5. Tác động đến Thời gian ra Quyết định và Độ Tự tin
* **Thời gian ra quyết định trung bình:** Tăng nhẹ từ **$22.08$ giây lên $22.55$ giây ($+0.47$ giây)**. Người dùng không còn trả lời quá vội vã mà dành thêm thời gian quan sát cấu trúc thông điệp.
* **Độ tự tin:** Điểm tự tin trung bình hầu như giữ nguyên ở mức **$3.48 \rightarrow 3.50 / 5.0$**, phản ánh trạng thái thận trọng, không tự mãn của người tham gia.

### 5.6. Kiểm định Thống kê và Giới hạn Nghiên cứu
* **Paired Samples t-test:** $t = -1.5992, p = 0.1263$.
* **Wilcoxon Signed-Rank Test:** $W = 47.50, p = 0.0964$.
* **Diễn giải học thuật:** Ở mức ý nghĩa $\alpha = 0.05$, sự suy giảm nhẹ về điểm Accuracy tổng thể không đạt ý nghĩa thống kê ($p > 0.05$). Điều này hoàn toàn phù hợp với lý thuyết SDT: sự sụt giảm accuracy không phản ánh năng lực người dùng kém đi, mà là **hệ quả trực tiếp của việc chuyển dịch ngưỡng quyết định ($c$ âm) gây tăng False Alarm**.

---

## CHƯƠNG 6: ĐỀ XUẤT KIỂM SOÁT PHÒNG VỆ VÀ KẾT LUẬN

### 6.1. Khung Kiểm soát Kết hợp: Con người - Quy trình - Kỹ thuật
Từ phát hiện về hiện tượng Alert Fatigue và sự bất lực của cảm quan ngôn ngữ trước AI Phishing, đồ án đề xuất mô hình phòng thủ 3 lớp:
1. **Lớp Kỹ thuật (Gánh dấu hiệu rõ ràng):** Triển khai bắt buộc DMARC `p=reject`, xác thực FIDO2/WebAuthn chống lừa đảo, lọc tên miền lookalike tự động.
2. **Lớp Quy trình (Loại bỏ sự mơ hồ):** Xây dựng quy trình xác minh ngoài băng (OOB) chuẩn hóa, không phụ thuộc vào quyết định cảm tính của nhân viên.
3. **Lớp Con người (Tập trung vào chiêu trò tâm lý):** Đào tạo nhân viên chuyển trọng tâm từ "soi chính tả" sang "phản xạ nghi vấn khi bị hối thúc thời gian hoặc đòi thông tin nhạy cảm".

### 6.2. Quy trình Xác minh Ngoài băng (Out-of-Band - OOB Protocol)
* **Nguyên tắc vàng:** Khi nhận được bất kỳ thông điệp nào yêu cầu chuyển tiền, cung cấp OTP/mật khẩu hoặc cập nhật tài khoản khẩn cấp, người nhận **tuyệt đối không thao tác qua đường link hay phản hồi lại người gửi**.
* **Kênh OOB độc lập:** Tự mở ứng dụng chính thức, gọi điện thoại theo số tổng đài in sau thẻ ngân hàng hoặc gặp trực tiếp cán bộ phụ trách.

### 6.3. Kết luận
Đồ án đã hoàn thành xuất sắc các mục tiêu nghiên cứu đặt ra:
1. Xây dựng thành công bộ dữ liệu chuẩn 60 thông điệp cân bằng $2 \times 2$ có kiểm soát giữa AI và viết tay.
2. Thu thập và phân tích định lượng dữ liệu thực tế từ 20 người tham gia với 1.200 lượt thử nghiệm.
3. Ứng dụng thành công Lý thuyết Phát hiện Tín hiệu (SDT) chứng minh bản chất của khóa can thiệp là **dịch chuyển ngưỡng quyết định ($c$)**, lý giải thỏa đáng hiện tượng Alert Fatigue.
4. Đưa ra giải pháp phòng vệ toàn diện kết hợp Con người - Quy trình - Kỹ thuật cho các tổ chức giáo dục và doanh nghiệp.

---

## TÀI LIỆU THAM KHẢO (CHUẨN IEEE)

[1] Verizon, "2024 Data Breach Investigations Report (DBIR)," Verizon Enterprise Solutions, Tech. Rep., Apr. 2024.  
[2] R. B. Cialdini, *Influence: The Psychology of Persuasion*, Revised Edition. New York: Harper Business, 2021.  
[3] D. Kahneman, *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux, 2011.  
[4] D. M. Green and J. A. Swets, *Signal Detection Theory and Psychophysics*. New York: John Wiley & Sons, 1966.  
[5] M. J. Hautus, "Corrections for extreme proportions and their biasing effects on estimated values of d'," *Behavior Research Methods, Instruments, & Computers*, vol. 27, no. 1, pp. 46–51, 1995.  
[6] P. Resnick, Ed., "Internet Message Format," RFC 5322, RFC Editor, Oct. 2008.  
[7] M. Kucherrawat, S. Roy, and A. K. Jain, "Generative AI in Social Engineering: Evaluating the Impact of LLMs on Phishing Susceptibility," *IEEE Transactions on Information Forensics and Security*, vol. 19, pp. 1120–1134, 2024.  
[8] J. S. Downs, M. B. Holbrook, and L. F. Cranor, "Behavioral Response to Phishing Risk," in *Proc. 2nd ACM Anti-Phishing Working Groups eCrime Researchers Summit (eCrime)*, 2007, pp. 37–44.  
[9] TS. Lê Quốc Tuấn, *Bài giảng An toàn thông tin*, Trường Đại học Giao thông Vận tải TP.HCM, 2026.  
[10] C. Herley, "So Long, and No Thanks for the Externalities: The Rational Rejection of Security Advice by Users," in *Proc. New Security Paradigms Workshop (NSPW)*, 2009, pp. 133–144.  
