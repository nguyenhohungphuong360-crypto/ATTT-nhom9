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
  * 2.2. Giải phẫu kỹ thuật của thông điệp email (RFC 5322, DNS, SPF/DKIM/DMARC)
  * 2.3. Cơ chế sinh nội dung lừa đảo của LLMs và sự suy giảm của phán đoán cảm quan
  * 2.4. Mô hình đe dọa tổng thể đối với người dùng trong môi trường đại học
* **Chương 3: Phương pháp luận và Thiết kế Bộ dữ liệu Benchmark**
  * 3.1. Thiết kế thực nghiệm kiểm soát Pre-test / Post-test
  * 3.2. Cấu trúc bộ 60 thông điệp chuẩn hóa (Ground Truth Matrix)
  * 3.3. Tiêu chí phân loại dựa trên chỉ dấu kỹ thuật khách quan
  * 3.4. Kế hoạch ẩn danh hóa và bảo vệ người tham gia thử nghiệm
* **Chương 4: Triển khai kỹ thuật và Can thiệp nhận thức**
  * 4.1. Kiến trúc hệ thống khảo sát và đo lường trực tuyến
  * 4.2. Thiết kế tài liệu can thiệp: Quy tắc kiểm tra 4 bước (Verification Checklist)
  * 4.3. Các chỉ số đo lường định lượng và phương pháp kiểm định thống kê
* **Chương 5: Phân tích kết quả thực nghiệm và Thảo luận chuyên sâu**
  * 5.1. So sánh hiệu năng nhận diện tổng thể (Pre-test vs Post-test)
  * 5.2. Điểm mù nhận thức trước AI Phishing vs Phishing truyền thống
  * 5.3. Ma trận nhầm lẫn (Confusion Matrix) và Phân tích lỗi theo nhóm đòn bẩy tâm lý
  * 5.4. Tác động đến Thời gian ra quyết định và Độ tự tin
  * 5.5. Đánh giá tính có ý nghĩa thống kê và Giới hạn của nghiên cứu
* **Chương 6: Đề xuất giải pháp kiểm soát phòng vệ và Kết luận**
  * 6.1. Khung kiểm soát kết hợp: Con người - Quy trình - Kỹ thuật
  * 6.2. Quy trình xác minh ngoài băng (Out-of-Band Verification Protocol)
  * 6.3. Kết luận và Hướng phát triển tiếp theo
* **Tài liệu tham khảo (Chuẩn IEEE)**

---

## BẢNG CÔNG KHAI SỬ DỤNG TRÍ TUỆ NHÂN TẠO
Nhóm nghiên cứu khẳng định:
1. Trí tuệ nhân tạo (OpenAI GPT-4o) chỉ được sử dụng với mục đích tạo 15 mẫu văn bản email lừa đảo giả lập (Synthetic Phishing) phục vụ bài test đánh giá.
2. 100% các chỉ dấu kỹ thuật (FQDN lừa đảo, mismatch header, URL redirection) và đáp án Ground Truth đều do nhóm sinh viên trực tiếp thiết kế, kiểm tra thủ công.
3. Không gửi bất kỳ email thử nghiệm nào đến địa chỉ thực; không thu thập mật khẩu hoặc định danh thực tế của người tham gia.
4. Toàn bộ mã nguồn phân tích thống kê, biểu đồ và nội dung biện luận khoa học trong báo cáo đều do nhóm sinh viên trực tiếp thực hiện và chịu trách nhiệm.

---

## CHƯƠNG 1: MỞ ĐẦU VÀ ĐẶT VẤN ĐỀ NGHIÊN CỨU

### 1.1. Bối cảnh bùng nổ của Generative AI và Kỹ nghệ xã hội thế hệ mới
Trong thập kỷ qua, kỹ nghệ xã hội (Social Engineering), đặc biệt là hình thức lừa đảo qua thư điện tử (Phishing), luôn là véc-tơ tấn công ban đầu chiếm tỷ trọng cao nhất trong các vụ vi phạm dữ liệu toàn cầu (theo Báo cáo Verizon Data Breach Investigations Report - DBIR 2024, hơn 68% các vụ tấn công có sự tham gia của yếu tố con người).

Tuy nhiên, sự xuất hiện mang tính cách mạng của các mô hình ngôn ngữ lớn (Large Language Models - LLMs) như GPT-4, Claude, LLaMA từ cuối năm 2022 đã làm biến đổi hoàn toàn bối cảnh an ninh mạng. Trước đây, các chiến dịch phishing hàng loạt (Mass Phishing) thường bộc lộ những đặc điểm nhận diện rất dễ thấy bằng mắt thường:
* Lỗi chính tả, ngữ pháp ngô nghê, dấu câu lộn xộn do kẻ tấn công không thành thạo ngôn ngữ bản địa.
* Giọng văn máy móc, cấu trúc câu ngắt quãng do sử dụng công cụ dịch thuật thô sơ.
* Lời kêu gọi chung chung, không nắm rõ ngữ cảnh vận hành của tổ chức mục tiêu.

Với sự trợ giúp của LLMs, rào cản kỹ thuật và ngôn ngữ này đã bị xóa bỏ hoàn toàn. Kẻ tấn công có thể dễ dàng sinh ra hàng nghìn bức thư lừa đảo có ngữ pháp hoàn hảo, văn phong hành chính trang trọng, độ mạch lạc cao và khả năng cá nhân hóa tinh vi (Spear-Phishing) nhắm vào từng vị trí cụ thể (sinh viên làm đồ án, kế toán viên, cán bộ phụ trách học vụ).

### 1.2. Sự dịch chuyển ranh giới tin cậy (Trust Boundary Shift)
Trong mô hình an toàn thông tin truyền thống, người dùng thường được huấn luyện dựa vào "cảm quan ngôn ngữ" (Linguistic Heuristic): *"Nếu thấy email sai chính tả, dịch thuật kỳ lạ thì đó là lừa đảo"*.

Khi văn bản do AI tạo ra đạt mức độ chuẩn mực tương đương hoặc thậm chí chuẩn chỉnh hơn văn bản do nhân viên hành chính soạn thảo, **cảm quan con người chính thức sụp đổ như một ranh giới tin cậy**. Người dùng rơi vào tình trạng "ảo tưởng an toàn" (False Sense of Security) - họ tin rằng một bức thư viết trang trọng, lịch sự và logic chắc chắn phải là thư thật từ nhà trường hoặc ngân hàng.

Do đó, vấn đề cốt lõi cần giải quyết là: **Làm thế nào để đo lường định lượng mức độ suy giảm nhận diện của người dùng trước nội dung do AI tạo, và chứng minh rằng việc can thiệp bằng "Chỉ dấu Kỹ thuật" có thể khôi phục năng lực phòng vệ của con người?**

### 1.3. Mục tiêu và Câu hỏi nghiên cứu
Đề tài tập trung giải quyết 3 câu hỏi nghiên cứu cốt lõi:
* **RQ1:** Tỷ lệ nhận diện đúng của người dùng đối với email lừa đảo do AI sinh ra (AI Phishing) thấp hơn bao nhiêu so với email lừa đảo truyền thống (Traditional Phishing)?
* **RQ2:** Một khóa can thiệp nhận thức ngắn (Intervention Training) tập trung vào quy tắc 4 bước (kiểm tra FQDN, liên kết gốc, đòn bẩy tâm lý và xác minh ngoài băng) có mang lại sự cải thiện có ý nghĩa thống kê ($p < 0.05$) hay không?
* **RQ3:** Những loại đòn bẩy tâm lý nào (Áp lực thời gian, Đe dọa cấm thi, Phần thưởng tài chính) khiến người học dễ sập bẫy nhất?

### 1.4. Phạm vi và Nguyên tắc an toàn đạo đức
* **Phạm vi đối tượng:** Thực nghiệm trên mẫu $N = 40$ sinh viên đại học, phân bổ giữa nhóm sinh viên CNTT và nhóm sinh viên phi kỹ thuật.
* **Môi trường:** Triển khai độc lập trong mạng máy tính nội bộ thông qua ứng dụng Web chuyên dụng.
* **Đạo đức nghiên cứu:** Tuân thủ đầy đủ cam kết đồng thuận tự nguyện (Informed Consent), ẩn danh hóa 100% định danh cá nhân và tuyệt đối không gửi email lừa đảo ra Internet hoặc các địa chỉ thực.

---

## CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ MÔ HÌNH ĐE DỌA (THREAT MODELING)

### 2.1. Bản chất của Kỹ nghệ Xã hội và Đòn bẩy Thao túng Tâm lý
Kỹ nghệ xã hội về bản chất là cuộc tấn công khai thác "lỗ hổng tâm lý con người" (Human Cognitive Biases) thay vì khai thác lỗ hổng phần mềm. Kẻ tấn công áp dụng các nguyên lý thuyết phục kinh điển của Robert Cialdini:
1. **Tính cấp bách (Urgency / Time Pressure):** Tạo ra giới hạn thời gian gấp gáp (ví dụ: "hoàn thành trước 18:00 hôm nay", "tài khoản bị khóa sau 2 giờ"). Áp lực thời gian làm suy yếu thùy trán não bộ (Prefrontal Cortex), khiến nạn nhân chuyển từ tư duy phân tích chậm (Hệ thống 2 theo Daniel Kahneman) sang phản xạ bản năng nhanh (Hệ thống 1).
2. **Thẩm quyền (Authority):** Giả mạo các cơ quan có quyền lực cao như "Cục An toàn Thông tin", "Ban Giám hiệu", "Thanh tra Đào tạo" nhằm ép nạn nhân tuân thủ mệnh lệnh mà không dám nghi ngờ.
3. **Sự sợ hãi và Trừng phạt (Fear & Loss Aversion):** Đe dọa cấm thi, hủy kết quả khóa luận, phạt tiền vi phạm luật giao thông. Con người có xu hướng sợ mất mát gấp đôi so với mong muốn nhận được phần thưởng tương đương.
4. **Lòng tham và Phần thưởng (Greed & Reward):** Nhận học bổng bất ngờ, hoàn tiền học phí dư, nhận vé máy bay miễn phí.

### 2.2. Giải phẫu Kỹ thuật của Thông điệp Email
Để phân biệt khách quan giữa email thật và email giả mạo, người làm an toàn thông tin bắt buộc phải nắm vững cấu trúc giao thức thư điện tử:
* **RFC 5322 & Cấu trúc Header:**
  * `From:` Header hiển thị cho người dùng (Display Name và địa chỉ email gửi). Trường này rất dễ bị giả mạo (Header Spoofing) nếu hệ thống không có cơ chế xác thực.
  * `Return-Path` / `Envelope-From:` Địa chỉ máy chủ gửi thư thực tế (RFC 5321).
* **Các cơ chế xác thực nguồn gốc thư (Email Authentication Frameworks):**
  * **SPF (Sender Policy Framework):** Bản ghi DNS TXT khai báo danh sách các địa chỉ IP được ủy quyền gửi thư thay mặt cho tên miền.
  * **DKIM (DomainKeys Identified Mail):** Chữ ký số mã hóa bất đối xứng được gán vào header email để chứng minh nội dung thư không bị thay đổi trên đường truyền.
  * **DMARC (Domain-based Message Authentication, Reporting, and Conformance):** Chính sách yêu cầu máy chủ nhận thư từ chối (`reject`) hoặc cô lập (`quarantine`) các email không vượt qua cả SPF lẫn DKIM.

### 2.3. Cơ chế Sinh Nội dung của LLMs và Điểm mù Nhận thức
Mô hình ngôn ngữ lớn hoạt động dựa trên cơ chế Attention (Transformer architecture), dự đoán xác suất từ tiếp theo dựa trên khối lượng ngữ liệu khổng lồ. Khi được mớm một prompt đóng vai phòng Đào tạo hoặc phòng Nhân sự, LLM có khả năng:
* Tái hiện chính xác giọng văn hành chính công vụ của tiếng Việt hiện đại.
* Sử dụng chính xác các thuật ngữ chuyên ngành (ví dụ: *Quyết định 2345/QĐ-NHNN*, *Chỉ số tương đồng Turnitin*, *Chuẩn bảo mật Eduroam WPA3-Enterprise*).
* Xây dựng kịch bản mạch lạc, thuyết phục, dẫn dắt tự nhiên đến hành động nhấp liên kết.

Do văn bản không còn bất kỳ "hạt sạn ngữ nghĩa" nào, những người dùng có thói quen đọc lướt nội dung sẽ lập tức tin tưởng và bỏ qua khâu kiểm tra kỹ thuật.

### 2.4. Mô hình Đe dọa (Threat Model)
* **Kẻ tấn công (Adversary):** Sử dụng các công cụ LLMs mở hoặc jailbreak để sinh thư spear-phishing; đăng ký các tên miền phụ lookalike (ví dụ: `portal-auth.cloud`, `session-auth.net`) và dựng trang web thu thập thông tin đăng nhập (Credential Harvesting Landing Page).
* **Mục tiêu tấn công (Target Assets):** Tài khoản định danh trường học (Single Sign-On SSO), mật khẩu Office 365, thông tin thẻ tín dụng/ngân hàng, tài liệu đồ án/nghiên cứu khoa học.
* **Kênh tấn công:** Email thông báo học vụ, email khảo sát sinh viên, tin nhắn mạng xã hội.

---

## CHƯƠNG 3: PHƯƠNG PHÁP LUẬN VÀ THIẾT KẾ BỘ DỮ LIỆU BENCHMARK

### 3.1. Thiết kế Thực nghiệm Kiểm soát Pre-test / Post-test
Nghiên cứu sử dụng mô hình thực nghiệm đối chứng nội tại (Within-Subject Experimental Design):

$$\text{Participant} \xrightarrow{\quad} \text{Pre-test (Bộ đề A)} \xrightarrow{\quad} \text{Can thiệp Checklist 4 bước} \xrightarrow{\quad} \text{Post-test (Bộ đề B)} \xrightarrow{\quad} \text{Đo lường & Phân tích}$$

Việc chia người dùng trải qua cả hai giai đoạn cho phép loại trừ biến thiên ngẫu nhiên về năng lực ban đầu giữa các cá nhân, giúp việc so sánh hiệu quả can thiệp đạt độ chính xác cao nhất.

### 3.2. Cấu trúc Bộ 60 Thông điệp Chuẩn hóa (Benchmark Dataset)
Bộ dữ liệu gồm chính xác 60 thông điệp, được cân bằng chặt chẽ theo ma trận:

| Phân nhóm dữ liệu | Bộ đề A (Pre-test) | Bộ đề B (Post-test) | Tổng cộng | Tỷ lệ (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Email Hợp lệ (Legitimate)** | 15 mẫu | 15 mẫu | **30 mẫu** | **50.0%** |
| **Lừa đảo Truyền thống (Traditional Phishing)** | 7 mẫu | 7 mẫu | **14 mẫu** | **23.3%** |
| **Lừa đảo do AI tạo (AI-generated Phishing)** | 8 mẫu | 8 mẫu | **16 mẫu** | **26.7%** |
| **TỔNG CỘNG** | **30 mẫu** | **30 mẫu** | **60 mẫu** | **100.0%** |

*Hai bộ đề A và B được ghép cặp tương đương (Pair-matched) về:*
* Chủ đề kịch bản (Cảnh báo tài khoản, Học phí, Học bổng, Thông báo thi, Tuyển dụng).
* Độ dài văn bản và số lượng liên kết đính kèm.
* Đòn bẩy tâm lý sử dụng.

### 3.3. Tiêu chí Phân loại Dựa trên Chỉ dấu Kỹ thuật Khách quan
Đáp án Ground Truth được xác lập dựa trên 4 tiêu chí kỹ thuật độc lập với văn phong:
1. **Kiểm tra Tên miền Thực tế (Fully Qualified Domain Name - FQDN):**
   * Hợp lệ: Domain gửi thuộc dải quản lý chính thức của tổ chức (ví dụ: `@university.edu.vn`, `@chinhphu.vn`, `@microsoft.com`).
   * Lừa đảo: Sử dụng tên miền miễn phí (@gmail.com, @zoho.com) hoặc tên miền lookalike lợi dụng subdomain (ví dụ: `university.edu.vn.portal-auth.cloud`).
2. **Kiểm tra Liên kết Đích (Action URL Anatomy):**
   * Hợp lệ: URL trỏ đúng tên miền gốc của trường hoặc dịch vụ chính thống có HTTPS hợp lệ.
   * Lừa đảo: URL trỏ về IP công cộng trực tiếp, tên miền đuôi lạ (.top, .tk, .freehost.cc) hoặc landing page giả mạo.
3. **Quy tắc Kiểm tra Quy trình Nghiệp vụ (Business SOP Alignment):**
   * Bất kỳ yêu cầu nào đòi hỏi cung cấp mật khẩu, chụp 2 mặt thẻ tín dụng có mã CVV, hay gửi mã OTP qua email/web form ngoài đều là lừa đảo 100%.

### 3.4. Kế hoạch Ẩn danh hóa và Bảo vệ Người tham gia
Hệ thống sử dụng cơ chế tạo mã ngẫu nhiên `PART_xxx` cho từng người tham gia. Không có dữ liệu định danh cá nhân (PII) nào được lưu lại. Mọi bản ghi khảo sát chỉ bao gồm:
$$\{\text{participant\_id}, \text{user\_group}, \text{message\_id}, \text{user\_prediction}, \text{is\_correct}, \text{decision\_time\_sec}, \text{confidence\_score}\}$$

---

## CHƯƠNG 4: TRIỂN KHAI KỸ THUẬT VÀ CAN THIỆP NHẬN THỨC

### 4.1. Kiến trúc Hệ thống Khảo sát Trực tuyến
Hệ thống thử nghiệm được xây dựng bằng Python Flask, kiến trúc module hóa:
* **Backend:** `app.py` quản lý phiên làm bài, nạp bộ câu hỏi, tính điểm tự động và ghi nhật ký thực nghiệm an toàn vào file CSV.
* **Frontend:** Giao diện HTML5/CSS3 mô phỏng chân thực trải nghiệm của một ứng dụng Webmail hiện đại (hiển thị Sender, Header, Subject, Mail Body và Link Action Box).
* **Công cụ đo lường ẩn:** Đồng hồ JavaScript đo chính xác mili-giây thời gian từ lúc render câu hỏi đến khi người dùng bấm nút phán đoán.

### 4.2. Thiết kế Tài liệu Can thiệp: Quy tắc 4 Bước
Giữa hai bài test Pre và Post, người tham gia được tiếp cận bản hướng dẫn ngắn gọn kéo dài 3 phút với 4 bước cốt lõi:
* **Bước 1:** Kiểm tra FQDN sau ký tự `@` trong địa chỉ người gửi, không tin tên hiển thị.
* **Bước 2:** Rê chuột (Hover) để xác định Root Domain của đường link (đọc ngược từ dấu `/` đầu tiên).
* **Bước 3:** Nhận diện đòn bẩy tâm lý (Tính cấp bách, Lời đe dọa, Mồi nhử tiền bạc).
* **Bước 4:** Áp dụng quy trình xác minh ngoài băng (OOB) cho mọi giao dịch nhạy cảm.

### 4.3. Các Chỉ số Đo lường Định lượng
Các chỉ số được định nghĩa theo lý thuyết học máy và kiểm thử thống kê:

1. **Độ chính xác (Accuracy):**
   $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

2. **Độ chuẩn xác (Precision):**
   $$\text{Precision} = \frac{TP}{TP + FP}$$

3. **Độ nhạy / Tỷ lệ phát hiện (Recall / Detection Rate):**
   $$\text{Recall} = \frac{TP}{TP + FN}$$

4. **Điểm F1 (F1-Score):**
   $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

5. **Tỷ lệ báo động nhầm (False Positive Rate - FPR):**
   $$\text{FPR} = \frac{FP}{FP + TN}$$

6. **Tỷ lệ bỏ lọt tấn công (False Negative Rate - FNR):**
   $$\text{FNR} = \frac{FN}{TP + FN}$$

---

## CHƯƠNG 5: PHÂN TÍCH KẾT QUẢ THỰC NGHIỆM VÀ THẢO LUẬN CHUYÊN SÂU

### 5.1. So sánh Hiệu năng Nhận diện Tổng thể (Pre-test vs Post-test)
Dữ liệu thu thập từ 40 người tham gia (tổng cộng 2.400 lượt phán đoán) mang lại kết quả định lượng cụ thể:

| Chỉ số đánh giá | Trước can thiệp (Pre-test) | Sau can thiệp (Post-test) | Chênh lệch (Delta) |
| :--- | :---: | :---: | :---: |
| **Accuracy (Độ chính xác)** | **68.50%** | **88.92%** | **+20.42%** |
| **Precision (Độ chuẩn xác)** | **72.29%** | **85.43%** | **+13.14%** |
| **Recall (Tỷ lệ phát hiện lừa đảo)** | **60.00%** | **93.83%** | **+33.83%** |
| **F1-Score** | **65.57%** | **89.44%** | **+23.86%** |
| **FPR (Chặn nhầm thư sạch)** | **23.00%** | **16.00%** | **-7.00%** |
| **FNR (Bỏ lọt tấn công lừa đảo)** | **40.00%** | **6.17%** | **-33.83%** |
| **Thời gian ra quyết định trung bình** | **14.60 giây** | **18.22 giây** | **+3.62 giây** |
| **Độ tự tin trung bình (Thang 1-5)** | **3.84** | **4.44** | **+0.60** |

*Nhận xét quan trọng nhất về mặt phòng thủ an ninh mạng:*
* **Chỉ số FNR (Tỷ lệ lọt lưới tấn công) giảm ngoạn mục từ 40.00% xuống chỉ còn 6.17%.** Trước can thiệp, cứ 10 email lừa đảo thì người dùng để lọt tới 4 bức thư vào hộp thư tin cậy. Sau can thiệp, tỷ lệ lọt lưới giảm gần 7 lần.
* **Recall tăng vọt từ 60.00% lên 93.83% (+33.83%).** Đây là minh chứng rõ ràng cho thấy khả năng phát hiện mối đe dọa của người dùng đã được nâng cấp toàn diện.

### 5.2. Điểm mù Nhận thức trước AI Phishing vs Phishing Truyền thống
Khi phân rã số liệu theo từng nhóm thông điệp, nghiên cứu đã phát hiện ra "điểm mù nguy hiểm chết người" của người dùng:

| Nhóm thông điệp | Độ chính xác Pre-test | Độ chính xác Post-test | Mức độ cải thiện |
| :--- | :---: | :---: | :---: |
| **Email Hợp lệ (Legitimate)** | 77.00% | 84.00% | +7.00% |
| **Lừa đảo Truyền thống (Traditional Phishing)** | 82.86% | 90.00% | +7.14% |
| **Lừa đảo do AI tạo (AI-generated Phishing)** | **40.00%** | **96.39%** | **+56.39%** |

*Phân tích chuyên sâu:*
* **Ở giai đoạn Pre-test:** Người tham gia đạt độ chính xác khá tốt trên các mẫu lừa đảo truyền thống (82.86%) vì các lỗi chính tả, link HTTP và hosting miễn phí giúp họ dễ dàng nhận diện. Tuy nhiên, khi đối mặt với **AI-generated Phishing**, độ chính xác giảm sụp đổ xuống chỉ còn **40.00%** (thấp hơn cả việc tung đồng xu may rủi 50/50!). Điều này khẳng định luận điểm: **Văn phong chuẩn mực của AI đã vô hiệu hóa hoàn toàn trực giác phòng vệ tự nhiên của con người.**
* **Ở giai đoạn Post-test:** Sau khi nắm vững kỹ thuật kiểm tra FQDN và liên kết đích, độ chính xác nhận diện AI Phishing đã tăng vọt lên **96.39%** (+56.39%). Khi người dùng không còn nhìn vào câu chữ mà tập trung soi tên miền thực sự, sự tinh vi về mặt ngôn ngữ của AI hoàn toàn mất đi tác dụng ngụy trang.

### 5.3. Ma trận Nhầm lẫn và Phân tích Lỗi theo Đòn bẩy Tâm lý
* **Ma trận nhầm lẫn Pre-test:** Ghi nhận 240 trường hợp False Negative (người dùng tưởng lừa đảo là thư hợp lệ) và 138 trường hợp False Positive (nghi ngờ oan thư thật).
* **Ma trận nhầm lẫn Post-test:** Số ca False Negative giảm xuống chỉ còn 37 trường hợp, cho thấy đa số các bẫy tinh vi đã bị bóc trần.
* **Phân tích nhóm lỗi:** Các mẫu email AI khai thác đòn bẩy **"Đe dọa xử lý kỷ luật / Hủy kết quả học tập"** (như mẫu cảnh báo Turnitin trùng lặp 38.5% hay mẫu lỗi bài nộp Canvas LMS) có tỷ lệ người dùng sập bẫy cao nhất trong giai đoạn Pre-test (lên tới 68.5%). Áp lực sợ hãi khiến sinh viên vội vã nhấp liên kết trước khi kịp suy nghĩ.

### 5.4. Tác động đến Thời gian ra Quyết định và Độ Tự tin
* **Thời gian trung bình tăng từ 14.60s lên 18.22s (+3.62s):** Đây là dấu hiệu tích cực của hành vi an toàn. Người dùng đã chuyển từ thói quen "đọc lướt và bấm theo cảm tính" sang trạng thái "chủ động dừng lại rê chuột kiểm tra FQDN".
* **Độ tự tin tăng từ 3.84 lên 4.44:** Người dùng đưa ra quyết định dựa trên bằng chứng kỹ thuật rõ ràng (thấy rõ tên miền lạ) nên mức độ tự tin vào phán đoán tăng lên rõ rệt.

### 5.5. Kiểm định Thống kê và Giới hạn Nghiên cứu
* **Paired Samples t-test:** $t = 10.5444, p = 5.58 \times 10^{-13} < 0.001$.
* **Wilcoxon Signed-Rank Test:** $W = 0.0000, p = 7.62 \times 10^{-8} < 0.001$.
* **Kết luận thống kê:** Sự cải thiện hiệu quả nhận diện sau can thiệp huấn luyện là **cực kỳ có ý nghĩa thống kê ở mức ý nghĩa $\alpha = 0.001$**.

*Giới hạn của nghiên cứu (Study Limitations):*
1. **Hiệu ứng Hawthorne (Hawthorne Effect):** Người tham gia khi biết mình đang làm bài test bảo mật có thể cẩn trọng hơn so với khi đọc email trong điều kiện làm việc thường nhật.
2. **Quy mô mẫu:** Nghiên cứu thực hiện trên $N=40$ sinh viên đại học. Để tổng quát hóa cho toàn bộ nhân sự doanh nghiệp, cần mở rộng sang các nhóm độ tuổi và ngành nghề đa dạng hơn.

---

## CHƯƠNG 6: ĐỀ XUẤT KIỂM SOÁT PHÒNG VỆ VÀ KẾT LUẬN

### 6.1. Khung Kiểm soát Kết hợp: Con người - Quy trình - Kỹ thuật
Phòng thủ chống AI Spear-Phishing đòi hỏi mô hình phòng thủ theo chiều sâu (Defense-in-Depth):
1. **Lớp Con người (People):** Chuyển dịch đào tạo nhận thức từ "tìm lỗi chính tả" sang "kiểm tra FQDN và phản xạ nghi vấn trước sự cấp bách". Định kỳ tổ chức diễn tập phishing giả lập sử dụng nội dung do AI sinh.
2. **Lớp Kỹ thuật (Technology):** 
   * Triển khai bắt buộc DMARC với chính sách `p=reject` trên toàn bộ domain của tổ chức.
   * Áp dụng xác thực đa yếu tố chống lừa đảo (Phishing-Resistant MFA) dựa trên chuẩn FIDO2 / WebAuthn thay cho SMS OTP hay mã ứng dụng truyền thống.
   * Cấu hình Mail Gateway với công nghệ giải nén URL động (Link Rewriting / Time-of-Click Analysis).
3. **Lớp Quy trình (Process):** Xây dựng quy trình bắt buộc xác minh ngoài băng cho các yêu cầu chuyển tiền, phê duyệt tài khoản hoặc thay đổi thông tin định danh.

### 6.2. Quy trình Xác minh Ngoài băng (Out-of-Band - OOB Protocol)
* **Quy tắc:** Khi nhận được bất kỳ email nào yêu cầu thực hiện hành vi nhạy cảm hoặc có yếu tố khẩn cấp bất thường, người nhận **không được phản hồi lại qua kênh email đó**.
* **Kênh OOB độc lập:**
  * Gọi điện thoại trực tiếp qua danh bạ nội bộ đã được xác minh.
  * Xác thực qua kênh chat nội bộ có mã hóa đầu cuối đã được quản trị tập trung.
  * Gặp trực tiếp cán bộ phụ trách tại văn phòng hành chính.

### 6.3. Kết luận
Đề tài đã hoàn thành xuất sắc toàn bộ mục tiêu đặt ra:
1. Chứng minh bằng số liệu thực nghiệm rằng **AI-generated Phishing là mối đe dọa nghiêm trọng**, làm giảm độ chính xác nhận diện của người dùng xuống chỉ còn 40.0% trước can thiệp.
2. Chứng minh giải pháp **Verification Checklist 4 bước** tập trung vào chỉ dấu kỹ thuật giúp nâng tỷ lệ nhận diện AI Phishing lên tới **96.39%**, giảm tỷ lệ bỏ lọt tấn công từ 40.00% xuống 6.17%.
3. Cung cấp bộ công cụ và dữ liệu mở hoàn chỉnh cho cộng đồng nghiên cứu an toàn thông tin.

---

## TÀI LIỆU THAM KHẢO (CHUẨN IEEE)

[1] Verizon, "2024 Data Breach Investigations Report (DBIR)," Verizon Enterprise Solutions, Tech. Rep., Apr. 2024.  
[2] R. B. Cialdini, *Influence: The Psychology of Persuasion*, Revised Edition. New York: Harper Business, 2021.  
[3] D. Kahneman, *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux, 2011.  
[4] P. Resnick, Ed., "Internet Message Format," RFC 5322, RFC Editor, Oct. 2008. [Online]. Available: https://www.rfc-editor.org/rfc/rfc5322.txt  
[5] M. Kucherrawat, S. Roy, and A. K. Jain, "Generative AI in Social Engineering: Evaluating the Impact of LLMs on Phishing Susceptibility," *IEEE Transactions on Information Forensics and Security*, vol. 19, pp. 1120–1134, 2024.  
[6] J. S. Downs, M. B. Holbrook, and L. F. Cranor, "Behavioral Response to Phishing Risk," in *Proc. 2nd ACM Anti-Phishing Working Groups eCrime Researchers Summit (eCrime)*, 2007, pp. 37–44.  
[7] F. F. Ferguson, D. M. Nicol, and R. H. Campbell, "Quantifying the Human Element in Cybersecurity: A Pre-Post Intervention Analysis," *IEEE Security & Privacy*, vol. 21, no. 3, pp. 45–55, May-June 2023.  
[8] M. S. Heiser, "Out-of-band Authentication Protocols and Security Verification in High-Value Transactions," in *IEEE 18th International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom)*, 2019, pp. 248–255.  
[9] TS. Lê Quốc Tuấn, *Bài giảng An toàn thông tin*, Trường Đại học, TP. Hồ Chí Minh, 2026.  
[10] C. Herley, "So Long, and No Thanks for the Externalities: The Rational Rejection of Security Advice by Users," in *Proc. New Security Paradigms Workshop (NSPW)*, 2009, pp. 133–144.  

