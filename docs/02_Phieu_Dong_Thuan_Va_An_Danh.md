# PHIẾU ĐỒNG THUẬN THAM GIA THỰC NGHIỆM & KẾ HOẠCH ẨN DANH HÓA
**Đề tài 09:** Đo hiệu quả nhận diện nội dung lừa đảo được tạo bởi trí tuệ nhân tạo  
**Học phần:** An toàn Thông tin - Giảng viên: TS. Lê Quốc Tuấn  

---

## PHẦN A: BẢN THÔNG TIN DÀNH CHO NGƯỜI THAM GIA (PARTICIPANT INFORMATION SHEET)

### 1. Mục đích của nghiên cứu
Nghiên cứu này được thực hiện trong khuôn khổ đồ án môn học An toàn Thông tin nhằm:
* Đánh giá khả năng phân biệt giữa thông điệp email hợp lệ và thông điệp lừa đảo do Trí tuệ nhân tạo (Generative AI) tạo ra.
* Đo lường hiệu quả của một bài hướng dẫn nhận thức ngắn (Security Awareness Checklist) trong việc nâng cao kỹ năng tự bảo vệ của người dùng số.

### 2. Quy trình tham gia thử nghiệm
Nếu đồng ý tham gia, bạn sẽ hoàn thành 3 giai đoạn diễn ra trong khoảng 15 – 20 phút:
1. **Giai đoạn 1 (Pre-test):** Đọc 30 thông điệp mẫu và phán đoán xem đó là "Hợp lệ (Legitimate)" hay "Lừa đảo (Phishing)", đồng thời chọn mức độ tự tin.
2. **Giai đoạn 2 (Can thiệp ngắn):** Đọc bản hướng dẫn ngắn gọn (khoảng 3 phút) về Quy tắc kiểm tra kỹ thuật (Checklist 4 bước: kiểm tra tên miền thực tế FQDN, cấu trúc liên kết và quy trình ngoài băng).
3. **Giai đoạn 3 (Post-test):** Đọc 30 thông điệp mẫu thứ hai (có độ khó tương đương) và thực hiện đánh giá để đo lường sự tiến bộ.

### 3. Nguyên tắc An toàn & Đạo đức tuyệt đối
* **Không có rủi ro bảo mật:** Các mẫu thông điệp hoàn toàn là dữ liệu mô phỏng trong môi trường lab an toàn. Không có email nào được gửi đến hộp thư thật của bạn.
* **Không yêu cầu thông tin nhạy cảm:** Bạn KHÔNG bao giờ được yêu cầu cung cấp mật khẩu thật, mã OTP ngân hàng, số thẻ tín dụng hay số căn cước công dân.
* **Quyền rút lui:** Bạn hoàn toàn có quyền từ chối tham gia hoặc dừng bài làm bất kỳ lúc nào mà không phải chịu bất kỳ ảnh hưởng hay đánh giá tiêu cực nào.

---

## PHẦN B: KẾ HOẠCH BẢO MẬT VÀ ẨN DANH HÓA DỮ LIỆU (ANONYMIZATION PLAN)

Để bảo vệ quyền riêng tư theo tiêu chuẩn an toàn thông tin:
1. **Cơ chế Mã hóa Định danh (Pseudonymization):**
   * Người tham gia không cần đăng ký bằng Họ tên thật hay Mã số sinh viên.
   * Hệ thống tự động cấp phát một mã định danh ngẫu nhiên (UUID) duy nhất, ví dụ: `PART_014`.
   * Mọi số liệu ghi nhận trong cơ sở dữ liệu (`raw_responses.csv`, bảng phân tích) chỉ liên kết với mã `participant_id`.
2. **Phạm vi dữ liệu thu thập:**
   * Dữ liệu ghi nhận chỉ bao gồm: Lựa chọn phán đoán (Phishing/Legitimate), Thời gian đưa ra quyết định (giây), Độ tự tin (1-5 Likert) và Nhóm ngành học chung (CNTT hoặc Ngoài CNTT).
   * Địa chỉ IP mạng và dấu vân tay trình duyệt (Fingerprinting) bị loại bỏ hoàn toàn, không lưu trữ trong log phân tích.
3. **Bảo quản và Hủy dữ liệu:**
   * Dữ liệu được lưu trữ trên thư mục cục bộ của nhóm nghiên cứu có phân quyền truy cập.
   * Sau khi học phần kết thúc và báo cáo được nghiệm thu, toàn bộ tệp nhật ký thô sẽ được xóa hủy an toàn.

---

## PHẦN C: PHIẾU ĐỒNG THUẬN TỰ NGUYỆN (INFORMED CONSENT FORM)

*(Phiếu này được tích hợp tại màn hình chào mừng của ứng dụng khảo sát trước khi bắt đầu)*

Vui lòng đọc kỹ các điều khoản sau trước khi nhấn xác nhận:

- [x] Tôi xác nhận đã đọc và hiểu rõ mục đích, quy trình và các quyền lợi khi tham gia nghiên cứu này.
- [x] Tôi hiểu rằng việc tham gia là hoàn toàn tự nguyện và tôi không phải cung cấp bất kỳ mật khẩu hay dữ liệu cá nhân nhạy cảm nào.
- [x] Tôi đồng ý để nhóm nghiên cứu sử dụng các câu trả lời ẩn danh của tôi phục vụ cho mục đích phân tích học thuật trong học phần An toàn Thông tin.

**Xác nhận của Người tham gia:**  
*Hành động tích chọn đồng ý và nhấn nút "Bắt đầu làm bài" trên ứng dụng được xem là chữ ký điện tử xác nhận sự đồng thuận tự nguyện của người tham gia.*

