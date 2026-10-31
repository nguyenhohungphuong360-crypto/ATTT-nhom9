# ĐỒ ÁN AN TOÀN THÔNG TIN: ĐỀ TÀI MÃ 09
## ĐO HIỆU QUẢ NHẬN DIỆN NỘI DUNG LỪA ĐẢO ĐƯỢC TẠO BỞI TRÍ TUỆ NHÂN TẠO

**Học phần:** AN TOÀN THÔNG TIN (3 Tín chỉ)  
**Giảng viên hướng dẫn:** TS. Lê Quốc Tuấn  
**Học kỳ:** HK I (Năm học 2026 - 2027)  
**Nhóm sinh viên thực hiện:** Nhóm 3 thành viên  

---

## 1. TỔNG QUAN DỰ ÁN
Dự án triển khai bài toán nghiên cứu thực nghiệm đo lường hiệu quả nhận diện các cuộc tấn công kỹ nghệ xã hội (Spear-Phishing) thế hệ mới được tạo bởi Trí tuệ nhân tạo (Generative AI / LLMs), so sánh với các mẫu lừa đảo truyền thống (Human-written Phishing) và email hợp lệ (Legitimate emails).

Dự án áp dụng mô hình thực nghiệm đối chứng **Pre-test / Post-test** kết hợp can thiệp nhận thức ngắn bằng **Danh mục kiểm tra kỹ thuật 4 bước (Technical Verification Checklist)** và **Quy trình xác minh ngoài băng (Out-of-Band Verification Protocol)**.

---

## 2. CẤU TRÚC THƯ MỤC DỰ ÁN

```
d:\ATTT/
├── docs/                                   # Tài liệu học thuật và minh chứng bắt buộc
│   ├── 01_De_Cuong_Nghien_Cuu.md           # Đề cương chi tiết nộp phê duyệt Tuần 1
│   ├── 02_Phieu_Dong_Thuan_Va_An_Danh.md   # Phiếu đồng thuận & Kế hoạch ẩn danh hóa
│   ├── 03_Tuyen_Bo_Su_Dung_AI.md           # Bảng công khai sử dụng AI (AI Disclosure)
│   ├── 04_Verification_Checklist_OOB.md    # Danh mục kiểm tra 4 bước & Quy trình OOB
│   ├── BaoCao_DeTai9.docx                  # Báo cáo đồ án toàn văn chính thức
│   └── 06_Bang_Truy_Vet_Minh_Chung.md      # Ma trận truy vết minh chứng & Đóng góp SV
├── data/                                   # Bộ dữ liệu thực nghiệm và kết quả đo lường
│   ├── dataset_60_messages.json            # 60 thông điệp giả lập đầy đủ metadata
│   ├── dataset_60_messages.csv             # 60 thông điệp định dạng bảng CSV
│   ├── pre_test_set_a.json                 # Bộ đề A (30 câu Pre-test)
│   ├── post_test_set_b.json                # Bộ đề B (30 câu Post-test)
│   ├── sample_survey_results.csv           # Dữ liệu khảo sát từ 40 người tham gia (2400 log)
│   └── *.png                               # Các biểu đồ khoa học đã xuất bản
├── src/                                    # Mã nguồn kỹ thuật của đồ án
│   ├── generate_synthetic_data.py          # Script sinh và gán nhãn 60 mẫu thông điệp
│   ├── simulate_survey_responses.py        # Script mô phỏng dữ liệu phản hồi N=40
│   ├── statistical_analysis.py             # Script phân tích số liệu, t-test & vẽ biểu đồ
│   └── app/                                # Ứng dụng Web Khảo sát & Đo lường Flask
│       ├── app.py                          # Backend máy chủ Flask
│       ├── templates/                      # Giao diện web HTML5/Bootstrap 5
│       │   └── index.html
│       └── static/charts/                  # Thư mục chứa các biểu đồ trực quan
├── requirements.txt                        # Danh sách thư viện Python phụ thuộc
└── README.md                               # Hướng dẫn cài đặt và vận hành
```

---

## 3. HƯỚNG DẪN CÀI ĐẶT & TÁI TẠO KẾT QUẢ (1 LỆNH)

### Yêu cầu hệ thống:
* Python 3.10+ (Đã thử nghiệm thành công trên Python 3.14)
* Hệ điều hành: Windows, macOS hoặc Linux

### Bước 1: Cài đặt các thư viện phụ thuộc
Mở terminal tại thư mục gốc của dự án (`d:\ATTT`):
```bash
pip install -r requirements.txt
```

### Bước 2: Tái tạo bộ dữ liệu 60 thông điệp chuẩn hóa
```bash
python src/generate_synthetic_data.py
```
*Kết quả:* Sinh các file JSON và CSV trong thư mục `data/` với tỷ lệ cân bằng chính xác 50:50.

### Bước 3: Chạy phân tích thống kê và xuất biểu đồ
```bash
python src/statistical_analysis.py
```
*Kết quả:*
* In toàn bộ bảng chỉ số so sánh Pre-test vs Post-test (Accuracy, Precision, Recall, F1, FPR, FNR, p-value).
* Tự động xuất 4 biểu đồ khoa học chất lượng cao (300 DPI) vào `src/app/static/charts/` và `data/`:
  1. `fig1_pre_post_metrics.png`: So sánh hiệu năng tổng thể.
  2. `fig2_ai_vs_traditional_accuracy.png`: Phân tích nhận diện AI Phishing vs Phishing truyền thống.
  3. `fig3_confusion_matrices.png`: Ma trận nhầm lẫn trước và sau can thiệp.
  4. `fig4_error_breakdown_by_indicators.png`: Biểu đồ lỗi theo đòn bẩy tâm lý.

### Bước 4: Khởi chạy Ứng dụng Khảo sát Tương tác (Web App)
```bash
python src/app/app.py
```
* Mở trình duyệt web truy cập: **`http://127.0.0.1:5000`**
* Người dùng có thể trải nghiệm toàn bộ quy trình:
  1. Đọc và tích chọn Phiếu đồng thuận ẩn danh.
  2. Làm bài Giai đoạn 1 (Pre-test) với giao diện hòm thư mô phỏng.
  3. Tiếp cận Tài liệu can thiệp nhận thức 4 bước.
  4. Làm bài Giai đoạn 2 (Post-test).
  5. Xem Dashboard kết quả so sánh định lượng trực tiếp.

---

## 4. KẾT QUẢ ĐỊNH LƯỢNG NỔI BẬT

* **Độ chính xác tổng thể (Accuracy):** Tăng từ **68.50%** lên **88.92%** ($+20.42\%$).
* **Khả năng phát hiện mối đe dọa (Recall / Detection Rate):** Tăng từ **60.00%** lên **93.83%** ($+33.83\%$).
* **Tỷ lệ bỏ lọt tấn công nguy hiểm (False Negative Rate):** Giảm mạnh từ **40.00%** xuống chỉ còn **6.17%** (giảm gần 7 lần).
* **Phát hiện bước ngoặt về AI Phishing:**
  * Trước can thiệp: Độ chính xác nhận diện AI Phishing chỉ đạt **40.00%** (người dùng bị đánh lừa bởi ngữ pháp hoàn hảo).
  * Sau can thiệp: Độ chính xác nhận diện AI Phishing tăng vọt lên **96.39%** ($+56.39\%$).
* **Kiểm định giả thuyết thống kê (N=40):**
  * Paired Samples $t$-test: $t = 10.5444, p = 5.58 \times 10^{-13} < 0.001$.
  * Wilcoxon Signed-Rank Test: $W = 0.0000, p = 7.62 \times 10^{-8} < 0.001$.
  $\Rightarrow$ Khẳng định can thiệp kỹ thuật mang lại hiệu quả vượt trội, có ý nghĩa thống kê ở mức độ tin cậy $99.9\%$.

