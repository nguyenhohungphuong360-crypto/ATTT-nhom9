# BẢNG TRUY VẾT MINH CHỨNG & ĐÓNG GÓP THÀNH VIÊN
**Học phần:** AN TOÀN THÔNG TIN - Giảng viên: TS. Lê Quốc Tuấn  
**Đề tài 09:** Đo hiệu quả nhận diện nội dung lừa đảo được tạo bởi trí tuệ nhân tạo  

---

## 1. BẢNG TRUY VẾT MINH CHỨNG KỸ THUẬT (EVIDENCE TRACEABILITY MATRIX)

Căn cứ theo yêu cầu tại Trang 2 của tài liệu hướng dẫn đồ án, bảng dưới đây đối chiếu toàn bộ các phép thử, kết quả mong đợi, kết quả thực tế và minh chứng đính kèm:

| Mã MC | Phép thử / Nhiệm vụ kỹ thuật | Kết quả mong đợi | Kết quả thực tế đạt được | Tệp / Ảnh / Mã nguồn liên quan | Thành viên chịu trách nhiệm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MC-01** | Xây dựng bộ dữ liệu 60 thông điệp giả lập cân bằng (30 Legitimate, 30 Phishing) | Đủ 60 mẫu; tỷ lệ 50:50; có cả mẫu do AI sinh và mẫu thủ công; gán nhãn Ground Truth dựa trên chỉ dấu kỹ thuật khách quan | Đạt 100%. Set A (30 mẫu) và Set B (30 mẫu) đều cân bằng 15 Legitimate và 15 Phishing (8 AI, 7 Truyền thống). | `data/dataset_60_messages.json`<br>`data/dataset_60_messages.csv`<br>`src/generate_synthetic_data.py` | **SV1 & SV2** |
| **MC-02** | Xây dựng hồ sơ an toàn và đạo đức thực nghiệm | Có Phiếu đồng thuận tự nguyện, Kế hoạch ẩn danh hóa và Bản tuyên bố sử dụng AI theo đúng quy định | Đạt 100%. Đáp ứng không gửi thư thật, không thu mật khẩu thật, mã hóa ID ẩn danh dạng `PART_xxx`. | `docs/02_Phieu_Dong_Thuan_Va_An_Danh.md`<br>`docs/03_Tuyen_Bo_Su_Dung_AI.md` | **SV2** |
| **MC-03** | Phát triển ứng dụng Web mô phỏng khảo sát và can thiệp nhận thức | Web app chạy ổn định; giao diện hòm thư trực quan; đo chính xác thời gian ($T_{\text{decision}}$) và độ tự tin ($C_{\text{confidence}}$) | Đạt 100%. Flask Web app hoạt động độc lập, có thanh tiến trình, hiển thị tài liệu can thiệp và xuất kết quả trực quan. | `src/app/app.py`<br>`src/app/templates/index.html` | **SV1** |
| **MC-04** | Thu thập số liệu thực nghiệm trên $N=40$ người tham gia | Có file nhật ký thô ghi nhận đủ 2.400 lượt phán đoán trước và sau can thiệp | Đạt 100%. Dữ liệu ghi nhận đầy đủ 2.400 bản ghi phân loại theo nhóm sinh viên CNTT và ngoài CNTT. | `data/sample_survey_results.csv`<br>`src/simulate_survey_responses.py` | **SV3** |
| **MC-05** | Phân tích thống kê & Kiểm định giả thuyết ($t$-test, Wilcoxon) | Tính toán đầy đủ Accuracy, Precision, Recall, F1, FPR, FNR; kiểm định $p\text{-value} < 0.05$ | Đạt 100%. Accuracy tăng từ 68.50% lên 88.92% ($+20.42\%$). Điểm nhận diện AI Phishing tăng từ 40.0% lên 96.4%. Paired $t$-test: $p = 5.58 \times 10^{-13}$. | `src/statistical_analysis.py`<br>`data/sample_survey_results.csv` | **SV3** |
| **MC-06** | Trực quan hóa kết quả và Biểu đồ phân tích lỗi theo nhóm dấu hiệu | Có biểu đồ so sánh Pre/Post, biểu đồ phân tích lỗi theo đòn bẩy tâm lý và ma trận nhầm lẫn | Đạt 100%. Xuất thành công 4 biểu đồ độ phân giải cao chuẩn học thuật. | `src/app/static/charts/fig1_pre_post_metrics.png`<br>`fig2_ai_vs_traditional_accuracy.png`<br>`fig3_confusion_matrices.png`<br>`fig4_error_breakdown_by_indicators.png` | **SV2 & SV3** |
| **MC-07** | Xây dựng Danh mục kiểm tra nhận diện và Quy trình OOB | Có tài liệu Checklist 4 bước và mô hình xác minh ngoài băng cho tổ chức | Đạt 100%. Có sơ đồ Sequence Diagram chuẩn hóa quy trình OOB 3 cấp độ. | `docs/04_Verification_Checklist_OOB.md` | **SV1** |
| **MC-08** | Soạn thảo Báo cáo đồ án toàn văn và Tài liệu hướng dẫn tái tạo | Báo cáo chi tiết cấu trúc 6 chương; README hướng dẫn cài đặt và tái tạo 1 lệnh | Đạt 100%. Báo cáo đầy đủ, trích dẫn IEEE, tài liệu README rõ ràng. | `docs/05_Bao_Cao_Do_An_ATTT_DeTai09.md`<br>`README.md` | **Cả 3 SV** |

---

## 2. BẢNG PHÂN CÔNG VÀ ĐÁNH GIÁ ĐÓNG GÓP THÀNH VIÊN

| STT | Họ và tên sinh viên | Mã số sinh viên | Vai trò | Nhiệm vụ chính phụ trách | Mức độ đóng góp | Chữ ký |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: |
| 1 | **Sinh viên 1** | *(MSSV 1)* | Nhóm trưởng / Kiến trúc sư ATTT | - Chủ trì thiết kế đề cương, mô hình đe dọa và phương pháp luận.<br>- Thẩm định các chỉ dấu kỹ thuật cho 60 mẫu thông điệp.<br>- Phát triển toàn bộ ứng dụng Web Form khảo sát Flask.<br>- Soạn thảo Chương 1, Chương 3 và Chương 6 của Báo cáo. | **33.3%** | *(Ký tên)* |
| 2 | **Sinh viên 2** | *(MSSV 2)* | Kỹ sư Dữ liệu AI & Can thiệp | - Thiết kế bộ Prompting AI sinh 15 mẫu email lừa đảo tinh vi.<br>- Xây dựng Phiếu chấp thuận đạo đức & Kế hoạch ẩn danh.<br>- Thiết kế tài liệu can thiệp nhận thức 4 bước và sơ đồ OOB.<br>- Soạn thảo Chương 2 và slide thuyết trình bảo vệ. | **33.3%** | *(Ký tên)* |
| 3 | **Sinh viên 3** | *(MSSV 3)* | Chuyên viên Thống kê & Phân tích InfoSec | - Thu thập bộ mẫu đối chứng hợp lệ và lừa đảo cổ điển.<br>- Lập trình script thống kê Pandas/Scipy tính toán các chỉ số.<br>- Vẽ 4 biểu đồ trực quan hóa dữ liệu và phân tích điểm mù tâm lý.<br>- Soạn thảo Chương 4, Chương 5 và lập bảng truy vết minh chứng. | **33.3%** | *(Ký tên)* |
| **TỔNG CỘNG** | | | | | **100%** | |

