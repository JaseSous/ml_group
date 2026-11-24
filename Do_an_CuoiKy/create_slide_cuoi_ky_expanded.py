# -*- coding: utf-8 -*-
"""
Tao slide bao cao cuoi ky toan dien - Nhom 05
27 Slides - CAU TRUC CHUAN 7 HOI DUA THEO PROJECT_STORY.MD
Chi tiet tung hoi, so do truc quan trich xuat tu notebook, minimal text
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ─── Color palette ───────────────────────────────────────────────
NAVY    = RGBColor(0x0f, 0x17, 0x2a)  # #0f172a
WHITE   = RGBColor(0xff, 0xff, 0xff)
EMERALD = RGBColor(0x00, 0xb8, 0x94)  # #00b894
BLUE    = RGBColor(0x09, 0x84, 0xe3)  # #0984e3
CORAL   = RGBColor(0xd6, 0x30, 0x31)  # #d63031
AMBER   = RGBColor(0xfd, 0xcb, 0x6e)  # #fdcb6e
GRAY    = RGBColor(0x94, 0xa3, 0xb8)  # #94a3b8
LIGHT   = RGBColor(0xe2, 0xe8, 0xf0)  # #e2e8f0
CARD_BG = RGBColor(0x1e, 0x29, 0x3b)  # #1e293b

W = Inches(13.33)
H = Inches(7.5)
script_dir = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(script_dir, "figures")
if not os.path.exists(FIGS):
    FIGS = "figures"

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H
blank_layout = prs.slide_layouts[6]

# ─── Helpers ─────────────────────────────────────────────────────

def add_bg(slide, color=NAVY):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def txb(slide, text, l, t, w, h, size=18, bold=False, color=WHITE,
        align=PP_ALIGN.LEFT, italic=False, wrap=True):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.italic = italic
    return tb

def header(slide, act_tag, title, tag_color=EMERALD):
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
    bar.fill.solid(); bar.fill.fore_color.rgb = tag_color; bar.line.fill.background()
    
    txb(slide, act_tag.upper(), Inches(0.4), Inches(0.22), Inches(10.5), Inches(0.35),
        size=11, bold=True, color=tag_color)
    txb(slide, title, Inches(0.4), Inches(0.55), Inches(12.5), Inches(0.7),
        size=23, bold=True, color=WHITE)
    ln = slide.shapes.add_shape(1, Inches(0.4), Inches(1.25), Inches(12.5), Inches(0.02))
    ln.fill.solid(); ln.fill.fore_color.rgb = tag_color; ln.line.fill.background()

def kpi_card(slide, number, label, l, t, w=Inches(2.5), h=Inches(1.2),
             num_color=EMERALD, bg_color=CARD_BG, num_size=24, lbl_size=11):
    rect = slide.shapes.add_shape(1, l, t, w, h)
    rect.fill.solid(); rect.fill.fore_color.rgb = bg_color
    rect.line.color.rgb = num_color; rect.line.width = Pt(1.5)
    
    txb(slide, number, l + Inches(0.05), t + Inches(0.08), w - Inches(0.1), Inches(0.6),
        size=num_size, bold=True, color=num_color, align=PP_ALIGN.CENTER)
    txb(slide, label, l + Inches(0.05), t + Inches(0.68), w - Inches(0.1), h - Inches(0.72),
        size=lbl_size, bold=False, color=LIGHT, align=PP_ALIGN.CENTER)

def img(slide, rel_path, l, t, w, h=None):
    full_path = os.path.join(FIGS, rel_path)
    if not os.path.exists(full_path):
        print(f"  [WARN] missing: {full_path}")
        return
    if h is None:
        slide.shapes.add_picture(full_path, l, t, width=w)
    else:
        slide.shapes.add_picture(full_path, l, t, width=w, height=h)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 1 — TRANG BÌA (Cover)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.18), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

img(sl, "fig00_ml_pipeline_architecture.png",
    Inches(7.2), Inches(0.6), Inches(5.8), Inches(6.3))

txb(sl, "ĐỒ ÁN CUỐI KỲ · HỌC MÁY (MACHINE LEARNING)", Inches(0.5), Inches(0.9),
    Inches(6.5), Inches(0.5), size=12, color=EMERALD, bold=True)

txb(sl, "Phân Khúc Khách Hàng\nOnline Retail II",
    Inches(0.5), Inches(1.5), Inches(6.5), Inches(2.2),
    size=44, bold=True, color=WHITE)

ln = sl.shapes.add_shape(1, Inches(0.5), Inches(3.8), Inches(5.8), Inches(0.03))
ln.fill.solid(); ln.fill.fore_color.rgb = EMERALD; ln.line.fill.background()

txb(sl, "K-Means · Hierarchical · DBSCAN · Tri-Model Consensus",
    Inches(0.5), Inches(4.0), Inches(6.5), Inches(0.5),
    size=15, color=AMBER, italic=True)

txb(sl, "Nhóm 05 — Trường Đại học Sài Gòn (SGU)\nGVHD: ThS. Trịnh Phước Thọ",
    Inches(0.5), Inches(4.9), Inches(6.5), Inches(0.9),
    size=14, color=LIGHT)

txb(sl, "Năm học 2024 – 2025", Inches(0.5), Inches(6.2),
    Inches(4), Inches(0.4), size=12, color=GRAY)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 2 — MỤC LỤC CÂU CHUYỆN (7 HỒI KHOA HỌC)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "TỔNG QUAN HÀNH TRÌNH ĐỒ ÁN", "Cấu Trúc 7 Hồi Khoa Học Của Đề Tài (Project Storyline)", AMBER)

acts = [
    ("HỒI 1", "Bối Cảnh & Nỗi Đau Kinh Doanh", "Nỗi đau tiếp thị đại trà 'One-Size-Fits-All' và mục tiêu phân khúc vi mô tối ưu CLV.", BLUE),
    ("HỒI 2", "Khám Phá Dữ Liệu & Tiền Xử Lý", "Cấu trúc 8 thuộc tính, quy trình 7 bước làm sạch và đặc tả 2 Database được huấn luyện.", EMERALD),
    ("HỒI 3", "Thực Nghiệm Mô Hình Baseline", "Thuộc tính giao dịch, không gian 2D PCA & giải phẫu nguyên nhân thất bại nghiệp vụ.", CORAL),
    ("HỒI 4", "Bước Ngoặt Kỹ Nghệ RFM", "Nén dữ liệu về 4,275 KH, triệt tiêu 98.7% độ lệch bằng Log Transform & Zero Leakage.", BLUE),
    ("HỒI 5", "Cuộc Đua Tam Mã (Tuning)", "Tối ưu hóa 3 trường phái K-Means (K=4), Hierarchical Ward, DBSCAN bóc tách ngoại lai.", EMERALD),
    ("HỒI 6", "Đột Phá Kiến Trúc Lai", "Mô hình Lai 2 tầng bóc tách 22 Super Whales (£55.7K) & Đỉnh cao Tri-Model Consensus 80.85%.", AMBER),
    ("HỒI 7", "Hiện Thực Hóa Ứng Dụng", "Playbook chiến lược kinh doanh cho 5 phân khúc khách hàng & tổng kết nghiệm thu đồ án.", CORAL),
]

ty = Inches(1.45)
for code, title, desc, col in acts:
    card = sl.shapes.add_shape(1, Inches(0.4), ty, Inches(12.5), Inches(0.75))
    card.fill.solid(); card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = col; card.line.width = Pt(1.5)
    
    pill_b = sl.shapes.add_shape(1, Inches(0.55), ty + Inches(0.12), Inches(1.3), Inches(0.5))
    pill_b.fill.solid(); pill_b.fill.fore_color.rgb = col; pill_b.line.fill.background()
    txb(sl, code, Inches(0.55), ty + Inches(0.2), Inches(1.3), Inches(0.35), size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    
    txb(sl, title, Inches(2.0), ty + Inches(0.12), Inches(3.8), Inches(0.5), size=13, bold=True, color=WHITE)
    txb(sl, desc, Inches(5.8), ty + Inches(0.12), Inches(7.0), Inches(0.5), size=11, color=LIGHT)
    ty += Inches(0.82)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 3 — HỒI 1: BỐI CẢNH & NỖI ĐAU KINH DOANH
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 1 · BỐI CẢNH & NỖI ĐAU KINH DOANH (THE BUSINESS DILEMMA)",
       "Bối Cảnh Thị Trường Bán Lẻ & 3 Mục Tiêu Chiến Lược Của Đồ Án", BLUE)

cards_s2 = [
    ("405,714", "Giao dịch thực tế\n(Giai đoạn 2009–2010)", EMERALD),
    ("4,275",   "Khách hàng\nđịnh danh duy nhất",       BLUE),
    ("37",      "Quốc gia\ntoàn cầu (UK 91.2%)",        AMBER),
    ("4,420",   "Mặt hàng\nquà tặng & gia dụng",        CORAL),
]
bx = Inches(0.4)
for num, lbl, col in cards_s2:
    kpi_card(sl, num, lbl, bx, Inches(1.4), w=Inches(2.95), h=Inches(1.25), num_color=col, num_size=24)
    bx += Inches(3.18)

# Panel Trái: Bối cảnh thị trường & 3 Nỗi đau kinh doanh
panel_l = sl.shapes.add_shape(1, Inches(0.4), Inches(2.85), Inches(6.1), Inches(4.35))
panel_l.fill.solid(); panel_l.fill.fore_color.rgb = CARD_BG
panel_l.line.color.rgb = CORAL; panel_l.line.width = Pt(1.5)

txb(sl, "🏢 BỐI CẢNH THỊ TRƯỜNG & 3 NỖI ĐAU CỐT TỬ", Inches(0.6), Inches(3.0), Inches(5.7), Inches(0.35),
    size=12, bold=True, color=CORAL)

pains_text = [
    ("📌 Bối cảnh thực tế:", "Nhà bán lẻ trực tuyến quà tặng UK (Online Retail II) kết hợp bán lẻ B2C cho cá nhân và bán sỉ B2B quy mô lớn trên 37 quốc gia, khiến hành vi khách hàng cực kỳ đa dạng và phức tạp."),
    ("❌ Tiếp thị 'cào bằng' (One-Size-Fits-All):", "Gửi email đại trà và voucher nhỏ lẻ cào bằng cho toàn bộ danh sách, làm phiền khách VIP và làm suy giảm nghiêm trọng uy tín thương hiệu."),
    ("📉 Nguy cơ mất khách hàng âm thầm (Churn):", "Không có cơ chế nhận diện khách hàng có nguy cơ rời bỏ để can thiệp kịp thời, dẫn đến chảy máu khách hàng trung thành vào tay đối thủ."),
    ("💸 Lãng phí ngân sách tiếp thị:", "Đốt tiền quảng cáo vào tài khoản ảo/ngưng hoạt động; tỷ lệ chuyển đổi đơn hàng và ROI thấp do thiếu định vị và cá nhân hóa thông điệp.")
]
ty_l = Inches(3.42)
for title_p, desc_p in pains_text:
    txb(sl, title_p, Inches(0.6), ty_l, Inches(5.7), Inches(0.24), size=10, bold=True, color=AMBER)
    txb(sl, desc_p, Inches(0.6), ty_l + Inches(0.24), Inches(5.7), Inches(0.55), size=9, color=LIGHT)
    ty_l += Inches(0.85)

# Panel Phải: 3 Mục tiêu chiến lược của đề tài
panel_r = sl.shapes.add_shape(1, Inches(6.8), Inches(2.85), Inches(6.1), Inches(4.35))
panel_r.fill.solid(); panel_r.fill.fore_color.rgb = CARD_BG
panel_r.line.color.rgb = EMERALD; panel_r.line.width = Pt(1.5)

txb(sl, "🎯 3 MỤC TIÊU CHIẾN LƯỢC CỦA ĐỒ ÁN", Inches(7.0), Inches(3.0), Inches(5.7), Inches(0.35),
    size=12, bold=True, color=EMERALD)

goals_text = [
    ("🤖 1. Mục tiêu Khoa học (Machine Learning Pipeline):", "Xây dựng quy trình phân cụm không giám sát khách quan, chống rò rỉ dữ liệu (Zero Data Leakage), giải quyết phân phối lệch phải (Extreme Skewness) và bóc tách chuẩn xác ngoại lai Super Whales B2B."),
    ("📊 2. Mục tiêu Nghiệp vụ (Marketing & CRM Actionable):", "Chuyển đổi thành công từ cấp độ giỏ hàng (Basket-level) sang cấp độ khách hàng (Customer-level RFM); định hình chân dung sắc nét và xây dựng Playbook chiến lược hành động cá nhân hóa từng nhóm tăng CLV."),
    ("⚡ 3. Mục tiêu Ứng dụng & Triển khai thực tế:", "Xây dựng ma trận phân khúc và Playbook chiến lược tiếp thị khả thi, sẵn sàng chuyển giao cho phòng Marketing và CRM áp dụng trực tiếp.")
]
ty_r = Inches(3.42)
for title_g, desc_g in goals_text:
    txb(sl, title_g, Inches(7.0), ty_r, Inches(5.7), Inches(0.24), size=10, bold=True, color=EMERALD)
    txb(sl, desc_g, Inches(7.0), ty_r + Inches(0.24), Inches(5.7), Inches(0.75), size=9, color=LIGHT)
    ty_r += Inches(1.1)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 4 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - CẤU TRÚC 8 THUỘC TÍNH
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 2 · KHÁM PHÁ DỮ LIỆU (EDA)",
       "Cấu Trúc 8 Thuộc Tính Gốc & Ma Trận Tương Quan Ban Đầu", EMERALD)

tbl_shape = sl.shapes.add_table(9, 3, Inches(0.4), Inches(1.45), Inches(6.8), Inches(5.6))
tbl = tbl_shape.table
tbl.columns[0].width = Inches(1.7)
tbl.columns[1].width = Inches(1.2)
tbl.columns[2].width = Inches(3.9)

headers_t = [("Thuộc tính", BLUE), ("Kiểu DL", AMBER), ("Ý nghĩa & Trạng thái dữ liệu", EMERALD)]
for j, (h_text, h_col) in enumerate(headers_t):
    cell = tbl.cell(0, j)
    cell.fill.solid(); cell.fill.fore_color.rgb = CARD_BG
    p = cell.text_frame.paragraphs[0]
    p.text = h_text
    p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = h_col

rows_data = [
    ("Invoice",      "String",   "Mã hóa đơn duy nhất từng đơn hàng"),
    ("StockCode",    "String",   "Mã số phân loại sản phẩm trong kho (3,997 mã)"),
    ("Description",  "String",   "Tên mô tả sản phẩm (4,420 mặt hàng khác nhau)"),
    ("Quantity",     "Integer",  "Số lượng mặt hàng mỗi dòng (Mean: 11.8)"),
    ("InvoiceDate",  "Datetime", "Thời điểm giao dịch (12/2009 – 12/2010)"),
    ("UnitPrice",    "Float",    "Đơn giá sản phẩm tính theo Bảng Anh (£)"),
    ("Customer ID",  "Float",    "Mã định danh khách hàng (ĐỦ 100% - 0 DÒNG THIẾU)"),
    ("Country",      "String",   "Quốc gia khách hàng (37 nước, UK chiếm 91.2%)"),
]
for i, row in enumerate(rows_data):
    for j, val in enumerate(row):
        cell = tbl.cell(i+1, j)
        cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor(0x13, 0x1d, 0x2e)
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE if j==0 else (AMBER if j==1 else (EMERALD if "ĐỦ 100%" in val else LIGHT))

img(sl, "fig_eda_correlation_heatmap.png", Inches(7.5), Inches(1.45), Inches(5.4), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 5 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - XU HƯỚNG DOANH THU
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 2 · KHÁM PHÁ DỮ LIỆU (EDA)",
       "Xu Hướng Doanh Thu Hàng Tháng & Tính Mùa Vụ Bán Lẻ", AMBER)

img(sl, "fig03_eda_monthly_revenue.png", Inches(0.4), Inches(1.4), Inches(8.8), Inches(5.7))

kpi_card(sl, "11/2010", "Tháng đỉnh doanh thu\n(£1,110,899.67)",
         Inches(9.5), Inches(1.5), w=Inches(3.4), h=Inches(1.5), num_color=AMBER)
kpi_card(sl, "Q4 Peak", "Mùa vụ bùng nổ cuối năm\n(Giáng sinh & Năm mới)",
         Inches(9.5), Inches(3.2), w=Inches(3.4), h=Inches(1.5), num_color=EMERALD)
kpi_card(sl, "£8.34M", "Tổng doanh thu ghi nhận\n(Trung bình £20.55/giao dịch)",
         Inches(9.5), Inches(4.9), w=Inches(3.4), h=Inches(1.5), num_color=BLUE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 6 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - THỊ TRƯỜNG & SẢN PHẨM
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 2 · KHÁM PHÁ DỮ LIỆU (EDA)",
       "Phân Bố Thị Trường Quốc Gia & Top Sản Phẩm Bán Chạy", EMERALD)

img(sl, "fig_eda_top_countries.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(5.6))
img(sl, "fig_eda_top_products.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 7 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - BỆNH LÝ PHÂN PHỐI LỆCH
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 2 · KHÁM PHÁ DỮ LIỆU (EDA)",
       "Dữ Liệu Thô: Toàn Vẹn 100% Thuộc Tính Nhưng Phân Phối Lệch Nặng", AMBER)

img(sl, "fig01_eda_quantity_price_dist.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

kpi_card(sl, "0 Dòng Thiếu", "Toàn vẹn Customer ID\n(Đầy đủ 100% mã khách)",
         Inches(9.2), Inches(1.45), w=Inches(3.7), h=Inches(1.3), num_color=EMERALD, bg_color=CARD_BG)
kpi_card(sl, "6,743 Dòng", "Dòng trùng lặp hoàn toàn\n(Chiếm 1.66% dữ liệu)",
         Inches(9.2), Inches(2.9), w=Inches(3.7), h=Inches(1.3), num_color=AMBER, bg_color=CARD_BG)
kpi_card(sl, "0 Dòng Âm", "Quantity & Price <= 0: 0\n(Không có đơn hủy)",
         Inches(9.2), Inches(4.35), w=Inches(3.7), h=Inches(1.3), num_color=BLUE, bg_color=CARD_BG)
kpi_card(sl, "Lệch Phải", "Quantity & Price lệch nặng\n(Cần xử lý ngoại lai)",
         Inches(9.2), Inches(5.8), w=Inches(3.7), h=Inches(1.3), num_color=CORAL, bg_color=CARD_BG)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 8 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - NGOẠI LAI THEO IQR
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 2 · KHÁM PHÁ DỮ LIỆU (EDA)",
       "Phát Hiện Ngoại Lai Cực Đoan Theo Phương Pháp IQR (Boxplot)", CORAL)

img(sl, "fig02_eda_boxplot_outliers.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

kpi_card(sl, "25,944 Dòng", "Ngoại lai Quantity (6.39%)\nNgưỡng trên IQR: > 27 sp",
         Inches(9.2), Inches(1.45), w=Inches(3.7), h=Inches(1.3), num_color=CORAL, bg_color=CARD_BG)
kpi_card(sl, "31,722 Dòng", "Ngoại lai UnitPrice (7.82%)\nNgưỡng trên IQR: > 7.50 £",
         Inches(9.2), Inches(2.9), w=Inches(3.7), h=Inches(1.3), num_color=AMBER, bg_color=CARD_BG)

panel = sl.shapes.add_shape(1, Inches(9.2), Inches(4.35), Inches(3.7), Inches(2.75))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = AMBER; panel.line.width = Pt(1.5)

txb(sl, "💡 Ý NGHĨA KINH DOANH", Inches(9.4), Inches(4.5), Inches(3.3), Inches(0.35),
    size=13, bold=True, color=AMBER, align=PP_ALIGN.CENTER)
txb(sl, "• Quantity đạt max tới 600 sản phẩm: Đây là các đơn hàng bán sỉ B2B quy mô lớn.\n• Không nên xóa bỏ cơ học vì đây chính là các khách hàng giá trị cao (Whales) của doanh nghiệp.\n• Giải pháp: Bóc tách bằng mô hình phân cụm mật độ DBSCAN.",
    Inches(9.4), Inches(4.9), Inches(3.3), Inches(2.1), size=11, color=LIGHT)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 9 — GIAI ĐOẠN 2: TIỀN XỬ LÝ & LÀM SẠCH DỮ LIỆU (PREPROCESSING)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "GIAI ĐOẠN 2 · TIỀN XỬ LÝ & LÀM SẠCH DỮ LIỆU (DATA PREPROCESSING)",
       "Quy Trình 7 Bước Làm Sạch Dữ Liệu & Phân Chia Chống Rò Rỉ (Zero Data Leakage)", EMERALD)

img(sl, "fig04_preprocessing_funnel.png", Inches(0.4), Inches(1.4), Inches(7.2), Inches(5.7))

kpi_card(sl, "405,714", "Dữ liệu ban đầu\n(Tập nạp gốc)",
         Inches(7.9), Inches(1.45), w=Inches(2.45), h=Inches(1.2), num_color=WHITE, num_size=19)
kpi_card(sl, "-6,743", "Khử trùng lặp\n(Duplicate 1.66%)",
         Inches(10.5), Inches(1.45), w=Inches(2.45), h=Inches(1.2), num_color=AMBER, num_size=19)
kpi_card(sl, "398,971", "Giao dịch sạch\n(Toàn vẹn 100% ID)",
         Inches(7.9), Inches(2.75), w=Inches(2.45), h=Inches(1.2), num_color=EMERALD, num_size=19)
kpi_card(sl, "4,275 KH", "Khách hàng duy nhất\n(Zero Leakage Split)",
         Inches(10.5), Inches(2.75), w=Inches(2.45), h=Inches(1.2), num_color=BLUE, num_size=19)

panel_prep = sl.shapes.add_shape(1, Inches(7.9), Inches(4.1), Inches(5.05), Inches(3.0))
panel_prep.fill.solid(); panel_prep.fill.fore_color.rgb = CARD_BG
panel_prep.line.color.rgb = EMERALD; panel_prep.line.width = Pt(1.5)

txb(sl, "📋 QUY TRÌNH TIỀN XỬ LÝ CHUẨN MỰC (NOTEBOOK 02)", Inches(8.1), Inches(4.2), Inches(4.7), Inches(0.3),
    size=11, bold=True, color=EMERALD)

steps_txt = [
    "1. Khử trùng lặp: Loại bỏ 6,743 dòng lặp lại hoàn toàn (1.66%).",
    "2. Kiểm tra dữ liệu thiếu: 100% CustomerID toàn vẹn (0 dòng thiếu).",
    "3. Ép kiểu chuẩn hóa: CustomerID (int/string), InvoiceDate (datetime).",
    "4. Lọc dữ liệu không hợp lệ: Không có đơn hủy ('C'), Quantity & Price > 0.",
    "5. Tính trường thành tiền: TotalPrice = Quantity × Price.",
    "6. Bảo toàn ngoại lai IQR: Giữ nguyên đơn hàng sỉ lớn làm đầu vào DBSCAN.",
    "7. Phân chia Train/Val/Test (64%/16%/20%) theo CustomerID độc lập."
]
ty_step = Inches(4.55)
for s in steps_txt:
    txb(sl, s, Inches(8.1), ty_step, Inches(4.7), Inches(0.28), size=9, color=LIGHT)
    ty_step += Inches(0.34)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 10 — KIẾN TRÚC DỮ LIỆU: ĐẶC TẢ DATABASE & BỘ THUỘC TÍNH HUẤN LUYỆN
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "KIẾN TRÚC DỮ LIỆU · ĐẶC TẢ DATABASE & BỘ THUỘC TÍNH HUẤN LUYỆN",
       "Phân Định 2 Cơ Sở Dữ Liệu Được Huấn Luyện: Database Giao Dịch vs Database Khách Hàng", BLUE)

panel_d1 = sl.shapes.add_shape(1, Inches(0.4), Inches(1.4), Inches(6.1), Inches(5.7))
panel_d1.fill.solid(); panel_d1.fill.fore_color.rgb = CARD_BG
panel_d1.line.color.rgb = BLUE; panel_d1.line.width = Pt(1.5)

txb(sl, "📦 DATABASE 1: GIAO DỊCH SẠCH (TRANSACTION-LEVEL)", Inches(0.6), Inches(1.55), Inches(5.7), Inches(0.35),
    size=12, bold=True, color=BLUE)

d1_items = [
    ("Tệp dữ liệu lưu trữ:", "data/train.csv (251,501 dòng - 64%)\ndata/valid.csv (72,685 dòng - 16%)\ndata/test.csv (74,785 dòng - 20%)"),
    ("Đơn vị quan sát (Sample Unit):", "Từng dòng mặt hàng trong hóa đơn giỏ hàng (Basket-level)."),
    ("THUỘC TÍNH DÙNG ĐỂ TRAIN (X):", "['Quantity', 'Price', 'TotalPrice']\n• Quantity: Số lượng sản phẩm mua trong từng dòng đơn hàng\n• Price: Đơn giá bán lẻ từng mặt hàng (£)\n• TotalPrice: Thành tiền của mặt hàng (Quantity × Price)"),
    ("Phương pháp chuẩn hóa:", "StandardScaler (chỉ fit_transform trên tập Train 255K dòng, transform cho Validation và Test)."),
    ("Mô hình áp dụng huấn luyện:", "K-Means Baseline (K=3), Hierarchical Baseline (K=4), DBSCAN Baseline (eps=0.5)."),
    ("Mục đích nghiên cứu:", "Thiết lập mốc đối chuẩn ban đầu (Baseline Benchmark) và vạch trần bẫy phân cụm trên cấp độ giỏ hàng.")
]
ty_d1 = Inches(1.95)
for title_d, desc_d in d1_items:
    txb(sl, title_d, Inches(0.6), ty_d1, Inches(5.7), Inches(0.24), size=10, bold=True, color=AMBER if "TRAIN" in title_d else WHITE)
    txb(sl, desc_d, Inches(0.6), ty_d1 + Inches(0.22), Inches(5.7), Inches(0.55), size=9, color=LIGHT)
    ty_d1 += Inches(0.84)

panel_d2 = sl.shapes.add_shape(1, Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.7))
panel_d2.fill.solid(); panel_d2.fill.fore_color.rgb = CARD_BG
panel_d2.line.color.rgb = EMERALD; panel_d2.line.width = Pt(1.5)

txb(sl, "👥 DATABASE 2: KHÁCH HÀNG RFM (CUSTOMER-LEVEL)", Inches(7.0), Inches(1.55), Inches(5.7), Inches(0.35),
    size=12, bold=True, color=EMERALD)

d2_items = [
    ("Tệp dữ liệu lưu trữ:", "data/rfm_train.csv (2,736 khách hàng - 64%)\ndata/rfm_val.csv (684 khách hàng - 16%)\ndata/rfm_test.csv (855 khách hàng - 20%)"),
    ("Đơn vị quan sát (Sample Unit):", "Từng tài khoản khách hàng định danh duy nhất (CustomerID)."),
    ("THUỘC TÍNH DÙNG ĐỂ TRAIN (X):", "['Recency_log', 'Frequency_log', 'Monetary_log']\n• Recency_log: ln(1 + Số ngày từ lần mua cuối đến 2010-12-10)\n• Frequency_log: ln(1 + Tổng số hóa đơn độc lập InvoiceNo)\n• Monetary_log: ln(1 + Tổng chi tiêu tích lũy TotalPrice)"),
    ("Phương pháp chuẩn hóa:", "Biến đổi phi tuyến ln(1+x) triệt tiêu 98.7% skewness + StandardScaler (fit trên RFM Train)."),
    ("Mô hình áp dụng huấn luyện:", "Tuned K-Means (K=4), Tuned Hierarchical Ward, Tuned DBSCAN, Mô hình Lai 2 tầng, Tri-Model Consensus."),
    ("Mục đích nghiên cứu:", "Định hình chân dung hành vi khách hàng toàn diện phục vụ tiếp thị cá nhân hóa và quản trị quan hệ khách hàng (CRM).")
]
ty_d2 = Inches(1.95)
for title_d, desc_d in d2_items:
    txb(sl, title_d, Inches(7.0), ty_d2, Inches(5.7), Inches(0.24), size=10, bold=True, color=EMERALD if "TRAIN" in title_d else WHITE)
    txb(sl, desc_d, Inches(7.0), ty_d2 + Inches(0.22), Inches(5.7), Inches(0.55), size=9, color=LIGHT)
    ty_d2 += Inches(0.84)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 11 — HỒI 3: PHẦN 1 - THIẾT LẬP THUỘC TÍNH & HIỆU NĂNG 3 MÔ HÌNH BASELINE
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 3 · THỰC NGHIỆM MÔ HÌNH CƠ SỞ (BASELINE MODEL)",
       "Phần 1: Thiết Lập Ban Đầu - 3 Thuộc Tính Huấn Luyện Giao Dịch & Hiệu Năng Đối Chuẩn", BLUE)

img(sl, "fig_baseline_metrics_comparison.png", Inches(0.4), Inches(1.4), Inches(8.3), Inches(5.7))

kpi_card(sl, "['Quantity', 'Price', 'TotalPrice']",
         "3 thuộc tính giao dịch cơ bản\nChuẩn hóa StandardScaler\nTrain 255K | Val 63K | Test 79K\nChống rò rỉ dữ liệu (Zero Leakage)",
         Inches(8.9), Inches(1.45), w=Inches(4.0), h=Inches(1.75), num_color=BLUE, num_size=15)

kpi_card(sl, "K-Means (K=3) — Tốt Nhất",
         "Mô hình Baseline tốt nhất\nSil Test: 0.6417 | DB: 0.6040\nCalinski-Harabasz: 150,925\nThời gian chạy siêu tốc: 0.52s",
         Inches(8.9), Inches(3.35), w=Inches(4.0), h=Inches(1.75), num_color=EMERALD, num_size=18)

kpi_card(sl, "Hierarchical & DBSCAN",
         "• Hierarchical (K=4): Sil Test = 0.6566\n  Nghẽn bộ nhớ O(N²), sample 5,000 dòng\n• DBSCAN (eps=0.5): Sil Test = 0.6600\n  DB: 0.4015 | Lọc 0.94% - 1.94% ngoại lai",
         Inches(8.9), Inches(5.25), w=Inches(4.0), h=Inches(1.75), num_color=AMBER, num_size=18)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 12 — HỒI 3: PHẦN 2 - TRỰC QUAN HÓA KHÔNG GIAN 2D PCA 3 MÔ HÌNH BASELINE
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 3 · THỰC NGHIỆM MÔ HÌNH CƠ SỞ (BASELINE MODEL)",
       "Phần 2: Trực Quan Hóa Không Gian 2D PCA - So Sánh Hình Thái Phân Cụm 3 Mô Hình", EMERALD)

img(sl, "fig_baseline_pca_2d_models.png", Inches(0.4), Inches(1.4), Inches(8.8), Inches(5.7))

kpi_card(sl, "89.7% Thông Tin",
         "Phương sai giải thích tích lũy 2D PCA:\n• PC1 (54.8%): Quy mô số lượng & doanh thu\n• PC2 (34.9%): Mức giá bán lẻ sản phẩm",
         Inches(9.4), Inches(1.45), w=Inches(3.5), h=Inches(1.75), num_color=AMBER, num_size=20)

kpi_card(sl, "K-Means: Cụm Bị Kéo Lệch",
         "• Cụm 0 (84.0%): Dồn cục ở gốc tọa độ\n• Cụm 2 (14.6%): Kéo dạt sang phải dọc PC1\n• Cụm 1 (1.4%): Giật lên đỉnh cao theo PC2",
         Inches(9.4), Inches(3.35), w=Inches(3.5), h=Inches(1.75), num_color=BLUE, num_size=17)

kpi_card(sl, "DBSCAN: Lọc Nhiễu -1",
         "• Cụm 0 (95.1%): Giao dịch bình thường\n• Noise -1 (107 mẫu): Lọc chính xác các\nđơn hàng ngoại lai bị kéo dạt ra ngoài rìa",
         Inches(9.4), Inches(5.25), w=Inches(3.5), h=Inches(1.75), num_color=CORAL, num_size=17)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 13 — HỒI 3: PHẦN 3 - GIẢI PHẪU THUỘC TÍNH KÉO KHÔNG GIAN & CÁI BẪY NGHIỆP VỤ
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 3 · THỰC NGHIỆM MÔ HÌNH CƠ SỞ (BASELINE MODEL)",
       "Phần 3: Giải Phẫu Thuộc Tính Kéo Không Gian & Bản Chất Thất Bại Nghiệp Vụ", CORAL)

img(sl, "fig_baseline_feature_importance.png", Inches(0.4), Inches(1.4), Inches(7.5), Inches(5.7))

kpi_card(sl, "Price (44.8% - 53.1%)",
         "Kéo tuyệt đối trục PC2 (Loading: +0.9634)\nChi phối lớn nhất K-Means (44.8%) & DBSCAN (53.1%)\nĐơn giá cao giật ngược dữ liệu lên đỉnh",
         Inches(8.2), Inches(1.45), w=Inches(4.7), h=Inches(1.3), num_color=AMBER, num_size=19)
kpi_card(sl, "Quantity (29.9% - 38.5%)",
         "Kéo trục PC1 (Loading: +0.7120) cùng TotalPrice (+0.6996)\nĐơn hàng bán sỉ kéo dạt dữ liệu sang cực bên phải\nTotalPrice đóng góp phần còn lại (16.7% - 17.0%)",
         Inches(8.2), Inches(2.9), w=Inches(4.7), h=Inches(1.3), num_color=BLUE, num_size=19)

panel = sl.shapes.add_shape(1, Inches(8.2), Inches(4.35), Inches(4.7), Inches(2.75))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = CORAL; panel.line.width = Pt(1.5)

txb(sl, "🚨 VÌ SAO BASELINE THẤT BẠI VỀ NGHIỆP VỤ?", Inches(8.4), Inches(4.5), Inches(4.3), Inches(0.35),
    size=12, bold=True, color=CORAL, align=PP_ALIGN.CENTER)
txb(sl, "• Silhouette đạt 0.64 rất cao là ẢO ẢNH TOÁN HỌC do các đơn hàng cực đoan kéo giãn không gian, tạo khoảng trống giả tạo.\n• Mô hình chỉ phân loại KÍCH THƯỚC GIỎ HÀNG (Basket-level) chứ không phân khúc KHÁCH HÀNG (Customer-level).\n• Cùng một khách hàng hôm nay mua đơn nhỏ nằm Cụm 0, ngày mai mua đơn lớn bị ném sang Cụm 2.\n→ Bắt buộc phải chuyển đổi sang cấp độ Khách hàng (RFM)!",
    Inches(8.4), Inches(4.88), Inches(4.3), Inches(2.15), size=11, color=LIGHT)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 12 — HỒI 4: BƯỚC NGOẶT RFM - RÚT TRÍCH BỘ 3 CHỈ SỐ VÀNG
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 4 · BƯỚC NGOẶT KỸ NGHỆ ĐẶC TRƯNG RFM (FEATURE ENGINEERING)",
       "Rút Trích Bộ 3 Chỉ Số Vàng RFM Cho 4,275 Khách Hàng", BLUE)

rfm_defs = [
    ("R", "Recency (Độ mới)", "Số ngày kể từ lần mua gần nhất đến mốc chốt sổ (2010-12-10). R nhỏ = khách gắn kết.\nMean: 90.6 ngày | Min: 1 | Max: 373", BLUE),
    ("F", "Frequency (Tần suất)", "Tổng số hóa đơn mua hàng duy nhất của khách hàng. F cao = khách ruột.\nMean: 4.4 đơn | Min: 1 | Max: 205", EMERALD),
    ("M", "Monetary (Doanh thu)", "Tổng số tiền khách đã chi trả (Quantity × UnitPrice). Giá trị tài chính.\nMean: £1,942.87 | Min: £2.95 | Max: £349,164", AMBER),
]
ty = Inches(1.5)
for code, name, desc, col in rfm_defs:
    rect = sl.shapes.add_shape(1, Inches(0.4), ty, Inches(4.5), Inches(1.65))
    rect.fill.solid(); rect.fill.fore_color.rgb = CARD_BG
    rect.line.color.rgb = col; rect.line.width = Pt(1.5)
    
    txb(sl, f"{code} · {name}", Inches(0.6), ty + Inches(0.12), Inches(4.1), Inches(0.4), size=14, bold=True, color=col)
    txb(sl, desc, Inches(0.6), ty + Inches(0.55), Inches(4.1), Inches(0.95), size=11, color=LIGHT)
    ty += Inches(1.85)

img(sl, "fig01_rfm_raw_distribution.png", Inches(5.2), Inches(1.4), Inches(7.7), Inches(5.7))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 13 — HỒI 4: BƯỚC NGOẶT RFM - CHINH PHỤC ĐỘ LỆCH (LOG1P)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 4 · BƯỚC NGOẶT KỸ NGHỆ ĐẶC TRƯNG RFM (FEATURE ENGINEERING)",
       "Biến Đổi Log Transform: Triệt Tiêu Độ Lệch & Chuẩn Hóa StandardScaler", EMERALD)

img(sl, "fig02_rfm_log_distribution.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

kpi_card(sl, "24.22 → 0.31", "Monetary Skewness\n(Giảm 98.72% độ lệch!)",
         Inches(9.2), Inches(1.45), w=Inches(3.7), h=Inches(1.3), num_color=EMERALD)
kpi_card(sl, "9.94 → 1.17", "Frequency Skewness\n(Giảm 88.21% độ lệch)",
         Inches(9.2), Inches(2.9), w=Inches(3.7), h=Inches(1.3), num_color=BLUE)
kpi_card(sl, "1.29 → -0.44", "Recency Skewness\n(Phân phối đối xứng)",
         Inches(9.2), Inches(4.35), w=Inches(3.7), h=Inches(1.3), num_color=AMBER)
kpi_card(sl, "StandardScaler", "Chuẩn hóa z-score\n(mean=0, std=1 trên Train)",
         Inches(9.2), Inches(5.8), w=Inches(3.7), h=Inches(1.3), num_color=WHITE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 14 — HỒI 4: BƯỚC NGOẶT RFM - TƯƠNG QUAN & KHÔNG GIAN 3D
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 4 · BƯỚC NGOẶT KỸ NGHỆ ĐẶC TRƯNG RFM (FEATURE ENGINEERING)",
       "Ma Trận Tương Quan & Không Gian Đặc Trưng 3D RFM", BLUE)

img(sl, "fig03_rfm_correlation_and_scatter.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(5.6))
img(sl, "fig04_rfm_3d_feature_space.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 15 — HỒI 4: BƯỚC NGOẶT RFM - CHIA TẬP & NGHỊCH LÝ SILHOUETTE
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 4 · BƯỚC NGOẶT KỸ NGHỆ ĐẶC TRƯNG RFM (FEATURE ENGINEERING)",
       "Chiến Lược Chia Dữ Liệu (Zero Leakage) & Giải Mã Nghịch Lý Silhouette", AMBER)

img(sl, "fig03_train_val_test_split.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

kpi_card(sl, "2,736 KH", "TẬP TRAIN (64.0%)\n251,501 giao dịch (Fit mô hình)",
         Inches(9.2), Inches(1.45), w=Inches(3.7), h=Inches(1.3), num_color=EMERALD)
kpi_card(sl, "684 KH", "TẬP VALIDATION (16.0%)\n72,685 giao dịch (Dò siêu tham số)",
         Inches(9.2), Inches(2.85), w=Inches(3.7), h=Inches(1.3), num_color=BLUE)
kpi_card(sl, "855 KH", "TẬP TEST (20.0%)\n74,785 giao dịch (Kiểm thử cuối)",
         Inches(9.2), Inches(4.25), w=Inches(3.7), h=Inches(1.3), num_color=AMBER)

panel = sl.shapes.add_shape(1, Inches(9.2), Inches(5.65), Inches(3.7), Inches(1.45))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = AMBER; panel.line.width = Pt(1)

txb(sl, "GIẢI MÃ NGHỊCH LÝ SILHOUETTE", Inches(9.3), Inches(5.75), Inches(3.5), Inches(0.3), size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
txb(sl, "Điểm Sil 0.3385 ở RFM là CHẤT LƯỢNG THỰC CHẤT:\nPhân tách 4 cụm cân đối (18%-33%), không cụm nào bị nuốt chửng, mỗi khách hàng có 1 danh tính ổn định.",
    Inches(9.3), Inches(6.05), Inches(3.5), Inches(0.95), size=10, color=LIGHT, align=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 16 — HỒI 5: CUỘC ĐUA TAM MÃ - K-MEANS TUNING (ELBOW & SILHOUETTE)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 5 · CUỘC ĐUA TAM MÃ: TINH CHỈNH SIÊU THAM SỐ (THE TUNING JOURNEY)",
       "Nhánh 1 - Tuned K-Means: Phương Pháp Elbow SSE & Hệ Số Silhouette Tìm K Tối Ưu", BLUE)

img(sl, "fig04_elbow_method_sse.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(4.6))
img(sl, "fig05_silhouette_scores_k.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(4.6))

panel = sl.shapes.add_shape(1, Inches(0.4), Inches(6.15), Inches(12.5), Inches(1.05))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = BLUE; panel.line.width = Pt(1.5)

txb(sl, "KẾT LUẬN CHỌN K=4:", Inches(0.7), Inches(6.3), Inches(2.5), Inches(0.4), size=13, bold=True, color=AMBER)
txb(sl, "• Điểm uốn Elbow xuất hiện rõ nét tại K=4 (độ dốc giảm SSE bắt đầu chững lại).\n• Hệ số Silhouette đạt đỉnh ổn định (0.3385 trên Train), phân cụm đồng đều và dễ gán nhãn nghiệp vụ.",
    Inches(3.2), Inches(6.25), Inches(9.5), Inches(0.85), size=12, color=LIGHT)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 17 — HỒI 5: CUỘC ĐUA TAM MÃ - K-MEANS 2D PCA & ANOVA
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 5 · CUỘC ĐUA TAM MÃ: TINH CHỈNH SIÊU THAM SỐ (THE TUNING JOURNEY)",
       "Nhánh 1 - Tuned K-Means: Không Gian 2D PCA & Phân Tích ANOVA: Frequency Số 1", BLUE)

img(sl, "fig_kmeans_scenarios_2d.png", Inches(0.4), Inches(1.4), Inches(7.5), Inches(5.7))

kpi_card(sl, "2,475.70", "F-Score: FREQUENCY\n(Đóng góp phân cụm lớn nhất)",
         Inches(8.2), Inches(1.5), w=Inches(4.7), h=Inches(1.2), num_color=EMERALD)
kpi_card(sl, "1,930.28", "F-Score: RECENCY\n(Đóng góp quan trọng thứ nhì)",
         Inches(8.2), Inches(2.9), w=Inches(4.7), h=Inches(1.2), num_color=BLUE)
kpi_card(sl, "1,928.51", "F-Score: MONETARY\n(Đóng góp giá trị tài chính)",
         Inches(8.2), Inches(4.3), w=Inches(4.7), h=Inches(1.2), num_color=AMBER)

box_s = sl.shapes.add_shape(1, Inches(8.2), Inches(5.7), Inches(4.7), Inches(1.35))
box_s.fill.solid(); box_s.fill.fore_color.rgb = CARD_BG
box_s.line.color.rgb = BLUE; box_s.line.width = Pt(1)

txb(sl, "SILHOUETTE SCORE K=4", Inches(8.4), Inches(5.8), Inches(4.3), Inches(0.3), size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
txb(sl, "Train: 0.3385  |  Val: 0.3193  |  Test: 0.3253", Inches(8.4), Inches(6.15), Inches(4.3), Inches(0.4), size=14, bold=True, color=EMERALD, align=PP_ALIGN.CENTER)
txb(sl, "✓ Độ khái quát hóa cao, không bị Overfitting", Inches(8.4), Inches(6.55), Inches(4.3), Inches(0.35), size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 18 — HỒI 5: CUỘC ĐUA TAM MÃ - HIERARCHICAL TUNING
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 5 · CUỘC ĐUA TAM MÃ: TINH CHỈNH SIÊU THAM SỐ (THE TUNING JOURNEY)",
       "Nhánh 2 - Tuned Hierarchical: Cây Phân Cấp Dendrogram & 7 Kịch Bản Linkage", AMBER)

img(sl, "fig10_dendrogram_ward.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(4.6))
img(sl, "fig_hierarchical_scenarios_2d.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(4.6))

kpi_card(sl, "0.6728", "Cophenetic Correlation\n(Bảo toàn khoảng cách dữ liệu)",
         Inches(0.4), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=AMBER)
kpi_card(sl, "0.3210", "Test Silhouette\n(Ward Linkage K=4)",
         Inches(4.7), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=EMERALD)
kpi_card(sl, "Ward Linkage", "Tối ưu hóa tổng phương sai\n(Vượt trội Complete & Average)",
         Inches(9.0), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=BLUE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 19 — HỒI 5: CUỘC ĐUA TAM MÃ - DBSCAN TUNING
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 5 · CUỘC ĐUA TAM MÃ: TINH CHỈNH SIÊU THAM SỐ (THE TUNING JOURNEY)",
       "Nhánh 3 - Tuned DBSCAN: Biểu Đồ K-Distance & Khả Năng Tách Ngoại Lệ Cực Đoan", CORAL)

img(sl, "fig11_kdistance_multiline.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(4.6))
img(sl, "fig_dbscan_scenarios_2d.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(4.6))

kpi_card(sl, "eps = 0.6", "Bán kính lân cận tối ưu\n(Điểm uốn K-distance)",
         Inches(0.4), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=CORAL)
kpi_card(sl, "MinPts = 10", "Mật độ điểm tối thiểu\n(Chống nhiễu ngoại vi)",
         Inches(4.7), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=AMBER)
kpi_card(sl, "43 KH (1.57%)", "Ngoại lệ phát hiện\n(Super Whales giá trị cao)",
         Inches(9.0), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=EMERALD)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 20 — HỒI 5: CUỘC ĐUA TAM MÃ - ĐỐI CHUẨN 3 THẾ HỆ
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 5 · CUỘC ĐUA TAM MÃ: TINH CHỈNH SIÊU THAM SỐ (THE TUNING JOURNEY)",
       "Đối Chuẩn Tổng Thể: Tiến Hóa Từ Baseline → Untuned RFM → Tuned RFM", EMERALD)

img(sl, "fig06_model_comparison_metrics.png", Inches(0.4), Inches(1.4), Inches(6.2), Inches(5.6))
img(sl, "fig_comparison_kmeans_vs_hierarchical_dbscan.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 21 — HỒI 5: CUỘC ĐUA TAM MÃ - CHÂN DUNG 4 PHÂN KHÚC K-MEANS
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 5 · CUỘC ĐUA TAM MÃ: TINH CHỈNH SIÊU THAM SỐ (THE TUNING JOURNEY)",
       "Chân Dung 4 Phân Khúc Khách Hàng Cốt Lõi Từ Mô Hình K-Means (K=4)", EMERALD)

img(sl, "fig08_rfm_cluster_profiles.png", Inches(0.4), Inches(1.4), Inches(7.5), Inches(5.7))

segs = [
    ("🏆 VIP LOYAL", "18.3%", "R: 14 ngày | F: 12 đơn | M: £5,800\nKhách ruột, mang lại phần lớn doanh thu", EMERALD),
    ("🌱 TIỀM NĂNG", "27.1%", "R: 35 ngày | F: 4 đơn | M: £1,200\nKhách mới mua gần đây, đang tăng trưởng", BLUE),
    ("😴 NGỦ ĐÔNG",  "21.8%", "R: 180 ngày | F: 2 đơn | M: £550\nKhách lâu chưa quay lại, nguy cơ quên brand", AMBER),
    ("🚪 RỜI BỎ",    "32.8%", "R: 320 ngày | F: 1 đơn | M: £280\nKhách đã bỏ đi, chi tiêu thấp", CORAL),
]
ty = Inches(1.45)
for title, pct, desc, col in segs:
    card = sl.shapes.add_shape(1, Inches(8.2), ty, Inches(4.7), Inches(1.3))
    card.fill.solid(); card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = col; card.line.width = Pt(1.5)
    
    txb(sl, title, Inches(8.35), ty + Inches(0.08), Inches(2.7), Inches(0.4), size=13, bold=True, color=col)
    txb(sl, pct, Inches(11.3), ty + Inches(0.08), Inches(1.4), Inches(0.4), size=18, bold=True, color=col, align=PP_ALIGN.RIGHT)
    txb(sl, desc, Inches(8.35), ty + Inches(0.52), Inches(4.4), Inches(0.68), size=10, color=LIGHT)
    ty += Inches(1.45)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 22 — HỒI 6: ĐỘT PHÁ KIẾN TRÚC - MÔ HÌNH LAI 2 TẦNG
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 6 · ĐỘT PHÁ KIẾN TRÚC: MÔ HÌNH LAI & TRI-MODEL CONSENSUS",
       "Giải Pháp 1: Mô Hình Lai 2 Tầng (K-Means + DBSCAN) Bóc Tách 22 Super Whales", AMBER)

img(sl, "fig12_hybrid_pca_and_whales_snake.png", Inches(0.4), Inches(1.4), Inches(8.8), Inches(5.7))

kpi_card(sl, "22 KH", "SUPER WHALES B2B\n(Khách sỉ siêu cá mập)",
         Inches(9.5), Inches(1.5), w=Inches(3.4), h=Inches(1.2), num_color=AMBER)
kpi_card(sl, "£55,725", "DOANH THU TRUNG BÌNH\n(Gấp 11 lần VIP thường!)",
         Inches(9.5), Inches(2.95), w=Inches(3.4), h=Inches(1.2), num_color=EMERALD)
kpi_card(sl, "8 Nhóm", "MICRO-SEGMENTS\n(Phân tầng siêu chi tiết)",
         Inches(9.5), Inches(4.4), w=Inches(3.4), h=Inches(1.2), num_color=BLUE)
kpi_card(sl, "Bảo Toàn", "KHÔNG LỆCH TÂM\n(Cụm bán lẻ chuẩn xác)",
         Inches(9.5), Inches(5.85), w=Inches(3.4), h=Inches(1.2), num_color=WHITE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 23 — HỒI 6: ĐỘT PHÁ KIẾN TRÚC - TRI-MODEL CONSENSUS
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 6 · ĐỘT PHÁ KIẾN TRÚC: MÔ HÌNH LAI & TRI-MODEL CONSENSUS",
       "Giải Pháp 2 (Đỉnh Cao): Tri-Model Consensus Ensemble Đồng Thuận 3 Thuật Toán", EMERALD)

img(sl, "fig_tri_model_hybrid_consensus_2d.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

kpi_card(sl, "80.85%", "CORE CONSENSUS (2,212 KH)\n3 mô hình tuyệt đối đồng thuận\nSilhouette = 0.420",
         Inches(9.2), Inches(1.5), w=Inches(3.7), h=Inches(1.6), num_color=EMERALD)
kpi_card(sl, "17.58%", "BOUNDARY ZONE (481 KH)\nVùng ranh giới nhạy cảm\nCần Marketing thử nghiệm",
         Inches(9.2), Inches(3.4), w=Inches(3.7), h=Inches(1.6), num_color=AMBER)
kpi_card(sl, "1.57%", "SUPER WHALES (43 KH)\nNgoại lệ giá trị cao\nDoanh thu TB £24,375",
         Inches(9.2), Inches(5.3), w=Inches(3.7), h=Inches(1.6), num_color=CORAL)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 24 — HỒI 7: HIỆN THỰC HÓA ỨNG DỤNG - CHIẾN LƯỢC KINH DOANH
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 7 · HIỆN THỰC HÓA ỨNG DỤNG & ĐÓNG GÓI SẢN PHẨM",
       "Kế Hoạch Hành Động Cá Nhân Hóa Cho 5 Phân Khúc Khách Hàng", BLUE)

actions = [
    ("🐳 Super Whales B2B", "Chăm sóc 1:1 qua Account Manager riêng, chiết khấu sỉ, SLA giao hàng ưu tiên.", AMBER),
    ("🏆 VIP Loyal",         "Chương trình khách hàng thân thiết, Early Access sản phẩm mới, tri ân sinh nhật.", EMERALD),
    ("🌱 Tiềm Năng",         "Gợi ý sản phẩm liên quan (Cross-sell), voucher kích thích mua đơn tiếp theo.", BLUE),
    ("😴 Ngủ Đông",          "Chiến dịch 'We Miss You', tặng coupon 15-20% có thời hạn để kéo lại tương tác.", AMBER),
    ("🚪 Nguy Cơ Rời Bỏ",    "Gửi khảo sát tìm hiểu lý do, Flash sale thanh lý, tối ưu chi phí quảng cáo.", CORAL),
]
ty = Inches(1.45)
for title, text, col in actions:
    card = sl.shapes.add_shape(1, Inches(0.4), ty, Inches(6.0), Inches(1.05))
    card.fill.solid(); card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = col; card.line.width = Pt(1.5)
    
    txb(sl, title, Inches(0.55), ty + Inches(0.08), Inches(5.7), Inches(0.35), size=13, bold=True, color=col)
    txb(sl, text, Inches(0.55), ty + Inches(0.45), Inches(5.7), Inches(0.55), size=10, color=LIGHT)
    ty += Inches(1.15)

img(sl, "fig13_note_final_benchmark_bars.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))





# ═══════════════════════════════════════════════════════════════════
# SLIDE 26 — TỔNG KẾT NGHIỆM THU ĐỒ ÁN (DELIVERABLES)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "TỔNG KẾT & NGHIỆM THU ĐỒ ÁN",
       "Danh Mục Sản Phẩm Bàn Giao & 6 Đóng Góp Cốt Lõi", EMERALD)

# Table on left (deliverables)
tbl_shape = sl.shapes.add_table(6, 3, Inches(0.4), Inches(1.45), Inches(6.8), Inches(5.6))
tbl = tbl_shape.table
tbl.columns[0].width = Inches(0.7)
tbl.columns[1].width = Inches(2.3)
tbl.columns[2].width = Inches(3.8)

headers_d = [("STT", BLUE), ("Sản phẩm", AMBER), ("Mô tả & Trạng thái", EMERALD)]
for j, (h_text, h_col) in enumerate(headers_d):
    cell = tbl.cell(0, j)
    cell.fill.solid(); cell.fill.fore_color.rgb = CARD_BG
    p = cell.text_frame.paragraphs[0]
    p.text = h_text
    p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = h_col

rows_deliv = [
    ("1", "Báo cáo chi tiết", "Báo cáo Word chuẩn học thuật đầy đủ 7 hồi nghiên cứu"),
    ("2", "Slide thuyết trình", "Slide PowerPoint 28 trang chuẩn 16:9, hình ảnh trực quan"),
    ("3", "Mã nguồn Notebook", "Hệ thống Jupyter Notebooks đã chạy đầy đủ kết quả thực nghiệm"),
    ("4", "Bộ mô hình & Logs", "Các file mô hình (.pkl), nhật ký thực nghiệm & nhãn dự đoán"),
    ("5", "Kho dữ liệu sạch", "Tập dữ liệu sạch, các file CSV nén RFM & báo cáo phân tích"),
]
for i, row in enumerate(rows_deliv):
    for j, val in enumerate(row):
        cell = tbl.cell(i+1, j)
        cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor(0x13, 0x1d, 0x2e)
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE if j==0 else (AMBER if j==1 else LIGHT)

# Right: 6 core achievements
panel_r = sl.shapes.add_shape(1, Inches(7.5), Inches(1.45), Inches(5.4), Inches(5.6))
panel_r.fill.solid(); panel_r.fill.fore_color.rgb = CARD_BG
panel_r.line.color.rgb = EMERALD; panel_r.line.width = Pt(1.5)

txb(sl, "⭐ 6 ĐÓNG GÓP KHOA HỌC & THỰC TIỄN", Inches(7.7), Inches(1.65), Inches(5.0), Inches(0.35), size=13, bold=True, color=EMERALD)

achievements = [
    ("✔", "Làm sạch chuẩn xác 405,714 giao dịch, toàn vẹn 100% ID."),
    ("✔", "Vạch trần cái bẫy Baseline và chuyển sang cấp độ khách hàng."),
    ("✔", "Rút trích RFM và triệt tiêu 98.7% độ lệch bằng Log Transform."),
    ("✔", "ANOVA chứng minh Frequency là thuộc tính định hình mạnh nhất."),
    ("✔", "Đột phá mô hình Lai 2 tầng bóc tách 22 Super Whales (£55.7K)."),
    ("✔", "Mô hình Tri-Model Consensus đạt vùng lõi tin cậy 80.85% (Sil 0.42)."),
]
ty = Inches(2.2)
for icon, txt in achievements:
    txb(sl, f"{icon}  {txt}", Inches(7.7), ty, Inches(5.0), Inches(0.48), size=11, color=LIGHT)
    ty += Inches(0.55)

txb(sl, "Nhóm 05 · Đại học Sài Gòn (SGU) · 2024–2025", Inches(7.7), Inches(6.4), Inches(5.0), Inches(0.35), size=11, italic=True, color=GRAY)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 27 — CẢM ƠN & Q&A
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.2), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

img(sl, "fig_tri_model_hybrid_consensus_2d.png", Inches(0.8), Inches(1.0), Inches(6.8), Inches(5.5))

panel_end = sl.shapes.add_shape(1, Inches(7.9), Inches(1.0), Inches(5.0), Inches(5.5))
panel_end.fill.solid(); panel_end.fill.fore_color.rgb = CARD_BG
panel_end.line.color.rgb = AMBER; panel_end.line.width = Pt(2)

txb(sl, "CẢM ƠN QUÝ THẦY CÔ\nVÀ CÁC BẠN ĐÃ LẮNG NGHE!",
    Inches(8.1), Inches(1.6), Inches(4.6), Inches(1.5),
    size=26, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

divider = sl.shapes.add_shape(1, Inches(8.5), Inches(3.3), Inches(3.8), Inches(0.02))
divider.fill.solid(); divider.fill.fore_color.rgb = AMBER; divider.line.fill.background()

txb(sl, "ĐỀ TÀI: PHÂN KHÚC KHÁCH HÀNG ONLINE RETAIL II\nNHÓM 05 — ĐẠI HỌC SÀI GÒN (SGU)",
    Inches(8.1), Inches(3.6), Inches(4.6), Inches(0.8),
    size=12, bold=True, color=EMERALD, align=PP_ALIGN.CENTER)

txb(sl, "Q & A",
    Inches(8.1), Inches(4.7), Inches(4.6), Inches(0.8),
    size=36, bold=True, color=AMBER, align=PP_ALIGN.CENTER)

txb(sl, "Rất mong nhận được đóng góp quý báu từ Thầy/Cô!",
    Inches(8.1), Inches(5.7), Inches(4.6), Inches(0.5),
    size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)


# ─── Save ─────────────────────────────────────────────────────────
target_dir = os.path.dirname(os.path.abspath(__file__))
paths_to_save = [
    os.path.join(target_dir, "Slide_Cuoi_Ky_Nhom05_OnlineRetailII.pptx"),
    os.path.join(target_dir, "Slide_Cuoi_Ky_Nhom05_OnlineRetailII_7Hoi.pptx")
]
for p in paths_to_save:
    try:
        prs.save(p)
        print(f"[OK] Saved: {p}")
    except PermissionError:
        print(f"[WARNING] File dang mo trong PowerPoint, vui long dong de ghi de: {p}")
print(f"     Total slides: {len(prs.slides)}")
