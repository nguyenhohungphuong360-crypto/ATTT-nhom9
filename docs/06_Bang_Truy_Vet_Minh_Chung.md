# BẢNG TRUY VẾT MINH CHỨNG & ĐÓNG GÓP THÀNH VIÊN
**Học phần:** AN TOÀN THÔNG TIN - Giảng viên: TS. Lê Quốc Tuấn  
**Đề tài 09:** Đo hiệu quả nhận diện nội dung lừa đảo được tạo bởi trí tuệ nhân tạo  

---

## 1. BẢNG TRUY VẾT MINH CHỨNG KỸ THUẬT (EVIDENCE TRACEABILITY MATRIX)

Căn cứ theo yêu cầu của đề cương môn học An toàn Thông tin, bảng dưới đây đối chiếu toàn bộ các phép thử, kết quả mong đợi, kết quả thực tế đạt được từ dữ liệu thực nghiệm và minh chứng kỹ thuật liên quan:

| Mã MC | Phép thử / Nhiệm vụ kỹ thuật | Kết quả mong đợi | Kết quả thực tế đạt được (Dữ liệu thực nghiệm $N = 20$) | Tệp / Ảnh / Mã nguồn liên quan | Thành viên chịu trách nhiệm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MC-01** | Xây dựng bộ dữ liệu 60 thông điệp giả lập cân bằng giai thừa $2 \times 2$ (30 Hợp lệ, 30 Lừa đảo; 30 AI, 30 Thủ công) | Đủ 60 mẫu; tỷ lệ 50:50; có cả mẫu do AI sinh và mẫu viết tay; gán nhãn Ground Truth dựa trên chỉ dấu kỹ thuật khách quan | Đạt 100%. Bộ 60 thông điệp cân bằng tuyệt đối giữa AI và Thủ công, chia thành Set A (30 mẫu) và Set B (30 mẫu) tương đương độ khó, bao quát cả 3 kênh: Email, SMS, Zalo. | `data/dataset_full.json`<br>`data/briefs_manual_filled.json`<br>`data/dataset_60_messages.json` | **Thân Hoàng Khoa & Nguyễn Hồ Hùng Phương** |
| **MC-02** | Xây dựng hồ sơ an toàn và đạo đức thực nghiệm | Có Phiếu đồng thuận tự nguyện, Kế hoạch ẩn danh hóa và Bản tuyên bố sử dụng AI theo đúng quy định | Đạt 100%. Đáp ứng chuẩn đạo đức nghiên cứu: tên miền `.test`, không gửi thư thật, không thu thập PII/OTP, mã hóa ID ẩn danh dạng `P01` đến `P20`. | `docs/02_Phieu_Dong_Thuan_Va_An_Danh.md`<br>`docs/03_Tuyen_Bo_Su_Dung_AI.md` | **Nguyễn Hồ Hùng Phương** |
| **MC-03** | Phát triển ứng dụng Web mô phỏng khảo sát và can thiệp nhận thức | Web app chạy ổn định; giao diện hòm thư trực quan; đo chính xác thời gian ($T_{\text{decision}}$) và độ tự tin ($C_{\text{confidence}}$) | Đạt 100%. Ứng dụng Flask Web app hoạt động độc lập (kèm phiên bản Jamstack tĩnh deploy Netlify), tự động đo thời gian ra quyết định (giây) và lưu vết câu trả lời. | `src/app/app.py`<br>`src/app/templates/index.html`<br>`public/index.html` | **Thân Hoàng Khoa** |
| **MC-04** | Thu thập số liệu thực nghiệm thực tế từ người tham gia | Có file nhật ký thô ghi nhận đầy đủ các lượt phán đoán trước và sau can thiệp của người dùng thật | Đạt 100%. File `khao_sat.csv` ghi nhận đầy đủ 1.200 bản ghi thực tế từ $N = 20$ người tham gia (`P01` ➔ `P20`), mỗi người hoàn thành đủ 60 câu hỏi theo 2 bộ đối chứng. | `data/khao_sat.csv`<br>`public/data/khao_sat.csv` | **Huỳnh Thanh Vũ** |
| **MC-05** | Phân tích thống kê & Lý thuyết Phát hiện Tín hiệu (SDT: $d'$ và Criterion $c$) | Tính toán đầy đủ Accuracy, Recall, Precision, FPR, $d'$, $c$; kiểm định $t$-test và Wilcoxon Signed-Rank | Đạt 100%. Recall bắt lừa đảo tăng từ 68.00% lên 72.67% ($+4.67\%$). Ngưỡng quyết định $c$ dịch chuyển mạnh từ $+0.1349$ sang $-0.1083$ ($\Delta c = -0.2432$), chứng minh người dùng cảnh giác hơn dẫn tới Alert Fatigue (FPR tăng từ 23% lên 35%). Wilcoxon $W = 47.50, p = 0.0964$. | `src/statistical_analysis.py`<br>`data/khao_sat.csv` | **Huỳnh Thanh Vũ** |
| **MC-06** | Trực quan hóa kết quả và Biểu đồ phân tích lỗi theo nhóm dấu hiệu | Có biểu đồ so sánh Pre/Post, biểu đồ AI vs Thủ công, ma trận nhầm lẫn và biểu đồ tần suất dấu hiệu | Đạt 100%. Xuất thành công 4 biểu đồ học thuật độ phân giải cao (300 DPI) được đồng bộ đầy đủ trên toàn hệ thống. | `src/app/static/charts/fig1_pre_post_metrics.png`<br>`fig2_ai_vs_traditional_accuracy.png`<br>`fig3_confusion_matrices.png`<br>`fig4_error_breakdown_by_indicators.png` | **Nguyễn Hồ Hùng Phương & Huỳnh Thanh Vũ** |
| **MC-07** | Xây dựng Danh mục kiểm tra nhận diện và Quy trình OOB | Có tài liệu Checklist 4 bước và mô hình xác minh ngoài băng cho tổ chức | Đạt 100%. Có sơ đồ Sequence Diagram chuẩn hóa quy trình OOB 3 cấp độ, hướng dẫn xác minh độc lập qua kênh tin cậy. | `docs/04_Verification_Checklist_OOB.md` | **Thân Hoàng Khoa** |
| **MC-08** | Soạn thảo Báo cáo đồ án toàn văn và Tài liệu hướng dẫn tái tạo | Báo cáo chi tiết cấu trúc 8 chương; README hướng dẫn cài đặt và tái tạo 1 lệnh | Đạt 100%. Báo cáo chuẩn mực khoa học IEEE, phản ánh trung thực kết quả thực nghiệm từ dữ liệu thật, có hướng dẫn chạy tái tạo trong 1 câu lệnh. | `docs/05_Bao_Cao_Do_An_ATTT_DeTai09.md`<br>`docs/BaoCao_DeTai9.docx`<br>`docs/nhóm 9 ATTT.pptx`<br>`README.md` | **Cả 3 SV** |

---

## 2. BẢNG PHÂN CÔNG VÀ ĐÁNH GIÁ ĐÓNG GÓP THÀNH VIÊN

| STT | Họ và tên sinh viên | Mã số sinh viên | Vai trò | Nhiệm vụ chính phụ trách | Mức độ đóng góp | Chữ ký |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: |
| 1 | **Nguyễn Hồ Hùng Phương** | **083206006476** | Nhóm trưởng / Kiến trúc sư ATTT & Giao diện Web | - Chủ trì thiết kế đề cương, mô hình đe dọa và phương pháp luận.<br>- Thẩm định các chỉ dấu kỹ thuật cho 60 mẫu thông điệp.<br>- Phát triển toàn bộ ứng dụng Web Form khảo sát Flask và bản Netlify.<br>- Soạn thảo Chương 1, Chương 3 và Chương 6 của Báo cáo. | **33.3%** | *(Ký tên)* |
| 2 | **Thân Hoàng Khoa** | **082206011685** | Kỹ sư Dữ liệu, Can thiệp nhận thức & Hồ sơ Đạo đức | - Thiết kế bộ mẫu lừa đảo do AI hỗ trợ và rà soát kịch bản thủ công.<br>- Xây dựng Phiếu chấp thuận đạo đức & Kế hoạch ẩn danh.<br>- Thiết kế tài liệu can thiệp nhận thức 4 bước và sơ đồ OOB.<br>- Soạn thảo Chương 2 và slide thuyết trình bảo vệ. | **33.3%** | *(Ký tên)* |
| 3 | **Huỳnh Thanh Vũ** | **060207000288** | Chuyên viên Thống kê & Phân tích InfoSec | - Thu thập, tổng hợp dữ liệu khảo sát thực tế $N=20$ người tham gia (`khao_sat.csv`).<br>- Lập trình script thống kê Pandas/Scipy tính toán chỉ số và SDT ($d', c$).<br>- Vẽ 4 biểu đồ trực quan hóa dữ liệu và phân tích hiện tượng Alert Fatigue.<br>- Soạn thảo Chương 4, Chương 5 và lập bảng truy vết minh chứng. | **33.3%** | *(Ký tên)* |
| **TỔNG CỘNG** | | | | | **100%** | |
