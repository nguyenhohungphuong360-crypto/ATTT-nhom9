# BẢNG CÔNG KHAI VIỆC SỬ DỤNG TRÍ TUỆ NHÂN TẠO (AI DISCLOSURE STATEMENT)
**Học phần:** AN TOÀN THÔNG TIN - Giảng viên: TS. Lê Quốc Tuấn  
**Đề tài 09:** Đo hiệu quả nhận diện nội dung lừa đảo được tạo bởi trí tuệ nhân tạo  

---

## 1. MỤC ĐÍCH CỦA BẢN CÔNG KHAI
Căn cứ theo quy định của đề cương học phần An toàn Thông tin (Trang 3 & Trang 15), nhóm nghiên cứu công khai minh bạch toàn bộ việc ứng dụng các mô hình Trí tuệ nhân tạo (AI/LLMs) trong quá trình thực hiện đồ án, nêu rõ công cụ, phạm vi, nội dung kiểm soát thủ công và trách nhiệm học thuật.

---

## 2. MA TRẬN SỬ DỤNG TRÍ TUỆ NHÂN TẠO

| Hạng mục công việc | Mô hình AI sử dụng | Mục đích cụ thể | Mức độ can thiệp của AI | Quy trình kiểm soát và trách nhiệm của Nhóm sinh viên |
| :--- | :--- | :--- | :--- | :--- |
| **1. Tạo mẫu lừa đảo giả lập (Phishing Synthetic Data)** | OpenAI GPT-4o & Claude 3.5 Sonnet | Sinh 15 mẫu email lừa đảo (AI-generated Phishing) có văn phong hành chính tự nhiên, hoàn chỉnh ngữ pháp và áp dụng các đòn bẩy tâm lý (Urgency, Authority, Greed). | **Sinh nội dung văn bản (Text Generation)** | **100% Nhóm rà soát và cấu hình thủ công:** Nhóm sinh viên trực tiếp thiết kế các chỉ dấu kỹ thuật khách quan (Root FQDN lừa đảo, giả mạo Subdomain, URL redirect, vi phạm quy trình nghiệp vụ). Tuyệt đối không để AI tự ý chèn dữ liệu cá nhân hay tổ chức có thật. |
| **2. Xây dựng mẫu đối chứng (Ground Truth)** | Không sử dụng AI | Thu thập 30 mẫu email hợp lệ và 15 mẫu lừa đảo truyền thống từ thực tế. | **0% (Thủ công 100%)** | Nhóm sinh viên tự thu thập, chuẩn hóa định dạng và gán nhãn Ground Truth dựa trên tiêu chuẩn kỹ thuật (RFC 5322, DNS DMARC/SPF). |
| **3. Thiết kế Can thiệp & Checklist OOB** | Không sử dụng AI | Xây dựng quy tắc 4 bước nhận diện kỹ thuật và sơ đồ xác minh ngoài băng. | **0% (Thủ công 100%)** | Nhóm sinh viên tự đúc kết dựa trên kiến thức phòng thủ an toàn thông tin chuyên sâu và quy chuẩn doanh nghiệp. |
| **4. Lập trình Web Khảo sát & Phân tích Dữ liệu** | GitHub Copilot / LLM Code Assistant | Hỗ trợ gợi ý cú pháp lập trình Python (Flask, Pandas, Scipy, Seaborn). | **Hỗ trợ gợi ý cú pháp mã nguồn (Code completion)** | **100% Nhóm chịu trách nhiệm:** Nhóm tự thiết kế kiến trúc hệ thống, kiểm thử đơn vị, xác thực công thức toán học thống kê ($t$-test, Wilcoxon, ma trận nhầm lẫn) và debug mã nguồn. |
| **5. Viết Báo cáo & Phân tích Đánh giá** | Không sử dụng AI để viết hộ nội dung khoa học | Soạn thảo các luận điểm, phân tích số liệu thực nghiệm, biện luận kết quả và kết luận. | **0% (Tự viết 100%)** | Toàn bộ các phân tích định lượng, nhận xét điểm mù tâm lý và đề xuất giải pháp đều do 3 thành viên trong nhóm trực tiếp nghiên cứu và bảo vệ trước hội đồng. |

---

## 3. CÁC NGUYÊN TẮC AN TOÀN ĐÃ TUÂN THỦ NGHIÊM NGẶT
1. **Kiểm soát Prompt An toàn (Responsible Prompting):** Toàn bộ prompt đưa vào LLM đều được thiết lập trong ngữ cảnh học thuật nghiên cứu an toàn phòng vệ (Defensive Cybersecurity Research). Không tạo mã khai thác (exploit payload) hay mã độc thực tế.
2. **Không rò rỉ dữ liệu nhạy cảm:** Không đưa bất kỳ thông tin cá nhân của sinh viên, giảng viên hoặc dữ liệu nội bộ chưa công bố của nhà trường vào các công cụ AI trực tuyến.
3. **Tính trung thực học thuật (Academic Integrity):** Báo cáo phản ánh trung thực số liệu đo lường thực tế, không bịa đặt số liệu hay chỉnh sửa kết quả kiểm định thống kê.

