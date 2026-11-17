import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Bảng màu chuẩn từ nhom_9_ATTT_UTH.pptx
COLOR_PRIMARY_TEAL = RGBColor(0x15, 0x84, 0x8B)   # #15848B
COLOR_KICKER_RED    = RGBColor(0xC0, 0x00, 0x00)   # #C00000
COLOR_TEXT_DARK     = RGBColor(0x1F, 0x2D, 0x33)   # #1F2D33
COLOR_TEXT_MUTED    = RGBColor(0x55, 0x65, 0x6C)   # #55656C
COLOR_BORDER_LIGHT  = RGBColor(0xC9, 0xE3, 0xE4)   # #C9E3E4
COLOR_WHITE         = RGBColor(0xFF, 0xFF, 0xFF)   # #FFFFFF
COLOR_ACCENT_YELLOW = RGBColor(0xF2, 0xC2, 0x30)   # #F2C230
COLOR_BG_CARD_LIGHT = RGBColor(0xF9, 0xFC, 0xFC)   # #F9FCFC
COLOR_BG_BOTTOM     = RGBColor(0xEE, 0xF6, 0xF7)   # #EEF6F7

def setup_header(slide, kicker_text, title_text):
    # Kicker
    kicker_box = slide.shapes.add_textbox(640080, 1005840, 10911535, 274320)
    tf_k = kicker_box.text_frame
    tf_k.word_wrap = True
    tf_k.margin_left = tf_k.margin_top = tf_k.margin_right = tf_k.margin_bottom = 0
    p_k = tf_k.paragraphs[0]
    p_k.text = kicker_text
    p_k.font.name = "Segoe UI"
    p_k.font.size = Pt(12)
    p_k.font.bold = True
    p_k.font.color.rgb = COLOR_KICKER_RED

    # Title
    title_box = slide.shapes.add_textbox(640080, 1280160, 10911535, 777240)
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.name = "Segoe UI"
    p_t.font.size = Pt(23)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_TEXT_DARK

def add_card(slide, left, top, width, height, bg_color, border_color=None):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
    else:
        card.line.fill.background()
    return card

def build_slides():
    prs = Presentation('docs/nhom_9_ATTT_UTH.pptx')
    blank_layout = prs.slide_layouts[6] # Blank
    
    new_prs = Presentation('docs/nhom_9_ATTT_UTH.pptx')
    # Xoá các slide cũ
    while len(new_prs.slides) > 0:
        rId = new_prs.slides._sldIdLst[0].rId
        new_prs.part.drop_rel(rId)
        del new_prs.slides._sldIdLst[0]

    # =========================================================================
    # SLIDE 1: RQ1 - CÔNG THỨC SO SÁNH TIN LỪA ĐẢO AI VS THỦ CÔNG
    # =========================================================================
    s1 = new_prs.slides.add_slide(blank_layout)
    setup_header(s1, "RQ1 · CÔNG THỨC & PHƯƠNG PHÁP TÍNH TOÁN", "Đo lường mức độ khó nhận diện giữa tin do AI tạo và viết tay thủ công")

    # Card Left: Bắt tin lừa đảo (Recall)
    c1_left = add_card(s1, 640080, 2180000, 5318607, 2750000, COLOR_BG_CARD_LIGHT, COLOR_BORDER_LIGHT)
    tb1_l = s1.shapes.add_textbox(850000, 2300000, 4900000, 2500000)
    tf1_l = tb1_l.text_frame
    tf1_l.word_wrap = True
    tf1_l.margin_left = tf1_l.margin_right = tf1_l.margin_top = tf1_l.margin_bottom = 0
    
    p = tf1_l.paragraphs[0]
    p.text = "1. TỶ LỆ BẮT TRÚNG TIN LỪA ĐẢO (RECALL)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_TEAL

    p = tf1_l.add_paragraph()
    p.text = "Recall = TP / (TP + FN) = Bắt đúng / Tổng tin lừa đảo"
    p.font.name = "Segoe UI Black"
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_TEXT_DARK
    p.space_before = Pt(8)
    p.space_after = Pt(8)

    items_l1 = [
        "• TP (True Positive): Tin lừa đảo được người dùng gắn đúng là 'Lừa đảo'.",
        "• FN (False Negative): Tin lừa đảo nhưng bị bỏ sót, gán nhầm là 'Hợp lệ'.",
        "• Đo lường theo 2 nhánh: Recall(AI) so với Recall(Thủ công).",
        "• Hiệu số nhánh: ΔRecall = Recall(AI) − Recall(Thủ công).",
        "→ Kết quả thực tế: 69,3% vs 66,9% (chênh lệch +2,4 đ%, p = 0,77)."
    ]
    for item in items_l1:
        p = tf1_l.add_paragraph()
        p.text = item
        p.font.name = "Segoe UI"
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_DARK
        p.space_after = Pt(3)

    # Card Right: Giữ đúng tin hợp lệ (TNR) & Báo nhầm (FPR)
    c1_right = add_card(s1, 6233007, 2180000, 5318607, 2750000, COLOR_PRIMARY_TEAL)
    tb1_r = s1.shapes.add_textbox(6450000, 2300000, 4900000, 2500000)
    tf1_r = tb1_r.text_frame
    tf1_r.word_wrap = True
    tf1_r.margin_left = tf1_r.margin_right = tf1_r.margin_top = tf1_r.margin_bottom = 0

    p = tf1_r.paragraphs[0]
    p.text = "2. GIỮ ĐÚNG TIN HỢP LỆ (TNR) & BÁO ĐỘNG NHẦM (FPR)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_YELLOW

    p = tf1_r.add_paragraph()
    p.text = "TNR = TN / (TN + FP)  |  FPR = FP / (TN + FP)"
    p.font.name = "Segoe UI Black"
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_WHITE
    p.space_before = Pt(8)
    p.space_after = Pt(8)

    items_r1 = [
        "• TN (True Negative): Tin hợp lệ được giữ đúng là 'Hợp lệ'.",
        "• FP (False Positive): Tin hợp lệ nhưng bị nghi nhầm, báo cờ 'Lừa đảo'.",
        "• TNR (Độ đặc hiệu): Khả năng nhận diện chính xác thư an toàn.",
        "• FPR (Tỷ lệ báo nhầm): Thước đo sự nghi ngờ quá mức của người dùng.",
        "→ Kết quả thực tế: Giữ đúng tin thật do AI giảm 8,3 đ% (73,1% vs 81,4%). Người dùng nghi ngờ oan thư thật do AI viết nhiều hơn!"
    ]
    for item in items_r1:
        p = tf1_r.add_paragraph()
        p.text = item
        p.font.name = "Segoe UI"
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_WHITE
        p.space_after = Pt(3)

    # Bottom summary box: Kiểm định thống kê
    c1_bot = add_card(s1, 640080, 5080000, 10911535, 1050000, COLOR_BG_BOTTOM, COLOR_BORDER_LIGHT)
    tb1_b = s1.shapes.add_textbox(850000, 5160000, 10500000, 900000)
    tf1_b = tb1_b.text_frame
    tf1_b.word_wrap = True
    tf1_b.margin_left = tf1_b.margin_right = tf1_b.margin_top = tf1_b.margin_bottom = 0

    p = tf1_b.paragraphs[0]
    p.text = "PHƯƠNG PHÁP KIỂM ĐỊNH THỐNG KÊ GHÉP CẶP (WITHIN-SUBJECT PAIRED ANALYSIS):"
    p.font.name = "Segoe UI"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_TEAL

    p = tf1_b.add_paragraph()
    p.text = "• Hiệu số từng người: di = Điểm(AI) − Điểm(Thủ công) được tính riêng cho từng cá nhân để triệt tiêu biến thiên nền tảng giữa người giỏi và người yếu.\n• Ước lượng khoảng tin cậy 95% bằng Bootstrap (1.000 lần lặp) và kiểm định phi tham số Wilcoxon signed-rank test để không phụ thuộc phân phối chuẩn."
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_TEXT_DARK
    p.space_before = Pt(3)


    # =========================================================================
    # SLIDE 2: RQ2 - CÔNG THỨC LÝ THUYẾT PHÁT HIỆN TÍN HIỆU (SDT: d' & c)
    # =========================================================================
    s2 = new_prs.slides.add_slide(blank_layout)
    setup_header(s2, "RQ2 · CÔNG THỨC LÝ THUYẾT PHÁT HIỆN TÍN HIỆU (SDT)", "Tách biệt năng lực phân biệt thật/giả (d′) khỏi xu hướng nghi ngờ (c)")

    # Card Left: Độ nhạy phân biệt d'
    c2_left = add_card(s2, 640080, 2180000, 5318607, 2750000, COLOR_BG_CARD_LIGHT, COLOR_BORDER_LIGHT)
    tb2_l = s2.shapes.add_textbox(850000, 2300000, 4900000, 2500000)
    tf2_l = tb2_l.text_frame
    tf2_l.word_wrap = True
    tf2_l.margin_left = tf2_l.margin_right = tf2_l.margin_top = tf2_l.margin_bottom = 0

    p = tf2_l.paragraphs[0]
    p.text = "1. ĐỘ NHẠY PHÂN BIỆT THẬT / GIẢ (d′ - SENSITIVITY)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_TEAL

    p = tf2_l.add_paragraph()
    p.text = "d′ = z(Hit Rate) − z(False-Alarm Rate)"
    p.font.name = "Segoe UI Black"
    p.font.size = Pt(16)
    p.font.color.rgb = COLOR_TEXT_DARK
    p.space_before = Pt(8)
    p.space_after = Pt(8)

    items_l2 = [
        "• Hit Rate (Tỷ lệ bắt trúng) = (TP + 0,5) / (TP + FN + 1)",
        "• FA Rate (Tỷ lệ báo nhầm) = (FP + 0,5) / (FP + TN + 1)",
        "  (Áp dụng hiệu chỉnh log-linear Hautus 1995 để tránh lỗi vô cùng khi rate = 0 hoặc 1).",
        "• z(·): Nghịch đảo hàm phân phối tích lũy chuẩn tắc (Inverse Normal CDF).",
        "• Ý nghĩa: Đo năng lực thực sự tách tín hiệu lừa đảo khỏi nhiễu (tin hợp lệ). d′ càng cao, phân biệt càng chuẩn xác."
    ]
    for item in items_l2:
        p = tf2_l.add_paragraph()
        p.text = item
        p.font.name = "Segoe UI"
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_DARK
        p.space_after = Pt(3)

    # Card Right: Ngưỡng quyết định c
    c2_right = add_card(s2, 6233007, 2180000, 5318607, 2750000, COLOR_PRIMARY_TEAL)
    tb2_r = s2.shapes.add_textbox(6450000, 2300000, 4900000, 2500000)
    tf2_r = tb2_r.text_frame
    tf2_r.word_wrap = True
    tf2_r.margin_left = tf2_r.margin_right = tf2_r.margin_top = tf2_r.margin_bottom = 0

    p = tf2_r.paragraphs[0]
    p.text = "2. NGƯỠNG QUYẾT ĐỊNH / THIÊN KIẾN (c - CRITERION)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_YELLOW

    p = tf2_r.add_paragraph()
    p.text = "c = −0,5 × [ z(Hit Rate) + z(False-Alarm Rate) ]"
    p.font.name = "Segoe UI Black"
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_WHITE
    p.space_before = Pt(8)
    p.space_after = Pt(8)

    items_r2 = [
        "• c = 0: Điểm cân bằng trung lập (không thiên vị bên nào).",
        "• c < 0 (Âm): Xu hướng NGHI NGỜ / DÈ CHỪNG (dễ bấm 'Lừa đảo').",
        "• c > 0 (Dương): Xu hướng DỄ DÃI / TIN TƯỞNG (dễ bấm 'Hợp lệ').",
        "• Đánh giá hiệu quả hướng dẫn trước - sau (Pre vs Post):",
        "  - Δd′ = d′(Post) − d′(Pre) : Đo mức tăng năng lực phân biệt.",
        "  - Δc = c(Post) − c(Pre) : Đo mức dịch chuyển tâm lý nghi ngờ."
    ]
    for item in items_r2:
        p = tf2_r.add_paragraph()
        p.text = item
        p.font.name = "Segoe UI"
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_WHITE
        p.space_after = Pt(3)

    # Bottom summary box
    c2_bot = add_card(s2, 640080, 5080000, 10911535, 1050000, COLOR_BG_BOTTOM, COLOR_BORDER_LIGHT)
    tb2_b = s2.shapes.add_textbox(850000, 5160000, 10500000, 900000)
    tf2_b = tb2_b.text_frame
    tf2_b.word_wrap = True
    tf2_b.margin_left = tf2_b.margin_right = tf2_b.margin_top = tf2_b.margin_bottom = 0

    p = tf2_b.paragraphs[0]
    p.text = "KẾT LUẬN CỐT LÕI TỪ MÔ HÌNH SDT TRÊN DỮ LIỆU THỰC TẾ:"
    p.font.name = "Segoe UI"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_TEAL

    p = tf2_b.add_paragraph()
    p.text = "• Sau hướng dẫn: Recall tăng (+4,7 đ%), nhưng d′ lại giảm nhẹ (−0,22) và c giảm sâu từ +0,13 xuống −0,19 (dịch chuyển sang vùng nghi ngờ).\n• Phát hiện mấu chốt: Nếu chỉ nhìn Recall sẽ kết luận sai là hướng dẫn có hiệu quả. Thực chất hướng dẫn chỉ làm người dùng 'đa nghi hơn' chứ không 'thông thái hơn'!"
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_TEXT_DARK
    p.space_before = Pt(3)


    # =========================================================================
    # SLIDE 3: RQ3 - CÔNG THỨC PHÂN TÍCH DẤU HIỆU & TỶ LỆ LỖI
    # =========================================================================
    s3 = new_prs.slides.add_slide(blank_layout)
    setup_header(s3, "RQ3 · CÔNG THỨC PHÂN TÍCH DẤU HIỆU & TỶ LỆ LỖI", "Đo lường tần suất dựa vào dấu hiệu và tỷ lệ gán nhầm theo nhóm chỉ báo")

    # Card Left: Tần suất & Tỷ lệ lỗi theo dấu hiệu
    c3_left = add_card(s3, 640080, 2180000, 5318607, 2750000, COLOR_BG_CARD_LIGHT, COLOR_BORDER_LIGHT)
    tb3_l = s3.shapes.add_textbox(850000, 2300000, 4900000, 2500000)
    tf3_l = tb3_l.text_frame
    tf3_l.word_wrap = True
    tf3_l.margin_left = tf3_l.margin_right = tf3_l.margin_top = tf3_l.margin_bottom = 0

    p = tf3_l.paragraphs[0]
    p.text = "1. TẦN SUẤT CHỌN & TỶ LỆ ĐOÁN SAI THEO DẤU HIỆU"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_TEAL

    p = tf3_l.add_paragraph()
    p.text = "Error Rate(k) = [ Sai khi chọn k ] / [ Tổng lượt chọn k ]"
    p.font.name = "Segoe UI Black"
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_TEXT_DARK
    p.space_before = Pt(8)
    p.space_after = Pt(8)

    items_l3 = [
        "• Tần suất f(k): Số lần người tham gia dựa vào dấu hiệu k khi ra quyết định.",
        "• Error Rate(k): Tỷ lệ phán đoán sai lệch khi người dùng vin vào dấu hiệu k.",
        "• Top dấu hiệu bị khai thác nhiều nhất: Hối thúc thời gian (288 lần), Đòi OTP/mật khẩu (236 lần), URL nhái (229 lần).",
        "• Dấu hiệu đánh lừa: Dựa vào 'Chất lượng ngôn ngữ' chỉ đạt độ đúng 66,3% (thấp hơn mức trung bình 71,4%) → AI đã triệt tiêu hoàn toàn giá trị của dấu hiệu này!"
    ]
    for item in items_l3:
        p = tf3_l.add_paragraph()
        p.text = item
        p.font.name = "Segoe UI"
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_DARK
        p.space_after = Pt(3)

    # Card Right: Tỷ lệ báo nhầm trên tin hợp lệ có bẫy
    c3_right = add_card(s3, 6233007, 2180000, 5318607, 2750000, COLOR_PRIMARY_TEAL)
    tb3_r = s3.shapes.add_textbox(6450000, 2300000, 4900000, 2500000)
    tf3_r = tb3_r.text_frame
    tf3_r.word_wrap = True
    tf3_r.margin_left = tf3_r.margin_right = tf3_r.margin_top = tf3_r.margin_bottom = 0

    p = tf3_r.paragraphs[0]
    p.text = "2. TỶ LỆ BÁO NHẦM TIN HỢP LỆ CÓ BẪY NGỮ CẢNH (FPR)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_YELLOW

    p = tf3_r.add_paragraph()
    p.text = "FPR(bẫy) = FP(tin hợp lệ có bẫy) / Tổng tin hợp lệ có bẫy"
    p.font.name = "Segoe UI Black"
    p.font.size = Pt(14.5)
    p.font.color.rgb = COLOR_WHITE
    p.space_before = Pt(8)
    p.space_after = Pt(8)

    items_r3 = [
        "• Bẫy yêu cầu đăng nhập: Tin hợp lệ có nhắc 'đăng nhập portal' bị gán nhầm thành lừa đảo lên tới 45% (AI-L15) và 30% (MN-L07).",
        "• Bẫy thời hạn/hạn chót: Tin hợp lệ có mốc thời hạn bị nghi ngờ tới 40% (AI-L03) và 30% (MN-L03).",
        "• Nguyên nhân: Người dùng áp dụng quy tắc máy móc ('cứ có link/đăng nhập/hạn chót là lừa') mà bỏ qua việc soi tên miền chính thức (FQDN)."
    ]
    for item in items_r3:
        p = tf3_r.add_paragraph()
        p.text = item
        p.font.name = "Segoe UI"
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_WHITE
        p.space_after = Pt(3)

    # Bottom summary box: Độ tự tin
    c3_bot = add_card(s3, 640080, 5080000, 10911535, 1050000, COLOR_BG_BOTTOM, COLOR_BORDER_LIGHT)
    tb3_b = s3.shapes.add_textbox(850000, 5160000, 10500000, 900000)
    tf3_b = tb3_b.text_frame
    tf3_b.word_wrap = True
    tf3_b.margin_left = tf3_b.margin_right = tf3_b.margin_top = tf3_b.margin_bottom = 0

    p = tf3_b.paragraphs[0]
    p.text = "HIỆU CHỈNH ĐỘ TỰ TIN (CONFIDENCE CALIBRATION ANALYSIS):"
    p.font.name = "Segoe UI"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_TEAL

    p = tf3_b.add_paragraph()
    p.text = "• Đo lường sự tương thích giữa mức độ tự tin (Thang Likert 1–5) và xác suất trả lời đúng thực tế.\n• Người tham gia có mức độ tự nhận thức (metacognition) rất tốt: Khi tự tin mức 1 chỉ đúng 11,5% (biết mình đang đoán mò), nhưng khi tự tin mức 5 đạt độ chính xác lên tới 94,4%."
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_TEXT_DARK
    p.space_before = Pt(3)

    output_path = 'docs/slide_cong_thuc_RQ1_2_3.pptx'
    new_prs.save(output_path)
    print(f"Đã lưu thành công 3 slide công thức chuẩn vào: {output_path}")

build_slides()
