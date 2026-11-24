# -*- coding: utf-8 -*-
"""
Tao slide bao cao cuoi ky toan dien - Nhom 05
23 Slides - Visual dominant, minimal text, high impact
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
CARD_WARN = RGBColor(0x2d, 0x12, 0x15)

W = Inches(13.33)
H = Inches(7.5)
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

def header(slide, tag, title, tag_color=EMERALD):
    # Left vertical accent line
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
    bar.fill.solid(); bar.fill.fore_color.rgb = tag_color; bar.line.fill.background()
    
    # Tag
    txb(slide, tag.upper(), Inches(0.4), Inches(0.22), Inches(8), Inches(0.35),
        size=11, bold=True, color=tag_color)
    # Title
    txb(slide, title, Inches(0.4), Inches(0.55), Inches(12.5), Inches(0.7),
        size=25, bold=True, color=WHITE)
    # Divider line
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

# Left accent bar
bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.18), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

# Right image panel (architecture figure)
img(sl, "fig00_ml_pipeline_architecture.png",
    Inches(7.2), Inches(0.6), Inches(5.8), Inches(6.3))

txb(sl, "ĐỒ ÁN CUỐI KỲ · HỌC MÁY (MACHINE LEARNING)", Inches(0.5), Inches(0.9),
    Inches(6.5), Inches(0.5), size=12, color=EMERALD, bold=True)

txb(sl, "Phân Cụm Khách Hàng\nOnline Retail II",
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
# SLIDE 2 — ĐẶT VẤN ĐỀ & MỤC TIÊU KINH DOANH
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "01 · TỔNG QUAN", "Vì Sao Doanh Nghiệp Cần Phân Cụm Khách Hàng?", BLUE)

# 4 Hero KPI Cards
cards_s2 = [
    ("1,067,371", "Giao dịch thực tế\n(2009 – 2011)", EMERALD),
    ("4,275",     "Khách hàng\nđịnh danh duy nhất", BLUE),
    ("43",        "Quốc gia\ntoàn cầu",            AMBER),
    ("4,631",     "Mặt hàng\nquà tặng & gia dụng",  CORAL),
]
bx = Inches(0.4)
for num, lbl, col in cards_s2:
    kpi_card(sl, num, lbl, bx, Inches(1.5), w=Inches(2.95), h=Inches(1.4), num_color=col, num_size=26)
    bx += Inches(3.18)

# Pain points vs Solutions panel
panel = sl.shapes.add_shape(1, Inches(0.4), Inches(3.2), Inches(12.5), Inches(3.9))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = BLUE; panel.line.width = Pt(1.5)

pains = [
    ("❌", "Thực trạng:", "Doanh nghiệp không biết ai là khách VIP, ai sắp rời bỏ (Churn) để chăm sóc kịp thời."),
    ("📉", "Hệ quả:", "Chiến dịch Marketing 'cào bằng' gây lãng phí ngân sách và tỷ lệ chuyển đổi thấp."),
    ("🔍", "Thách thức ML:", "Dữ liệu thô bị lệch nặng, nhiều giao dịch ngoại lệ cực đoan khiến mô hình dễ bị bẫy."),
    ("🎯", "Mục tiêu đồ án:", "Xây dựng hệ thống phân khúc vi mô (Micro-segmentation) chính xác cao, tăng Customer Lifetime Value (CLV)."),
]
ty = Inches(3.45)
for icon, title, desc in pains:
    txb(sl, f"{icon}  {title}", Inches(0.7), ty, Inches(2.8), Inches(0.45), size=14, bold=True, color=AMBER)
    txb(sl, desc, Inches(3.5), ty, Inches(9.1), Inches(0.7), size=14, color=LIGHT)
    ty += Inches(0.85)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 3 — TẬP DỮ LIỆU GỐC & 8 THUỘC TÍNH
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "02 · KHÁM PHÁ DỮ LIỆU", "Cấu Trúc 8 Thuộc Tính & Ma Trận Tương Quan Ban Đầu", EMERALD)

# Table on left (8 attributes)
tbl_shape = sl.shapes.add_table(9, 3, Inches(0.4), Inches(1.45), Inches(6.8), Inches(5.6))
tbl = tbl_shape.table
tbl.columns[0].width = Inches(1.8)
tbl.columns[1].width = Inches(1.3)
tbl.columns[2].width = Inches(3.7)

headers_t = [("Thuộc tính", BLUE), ("Kiểu DL", AMBER), ("Ý nghĩa thực tế", EMERALD)]
for j, (h_text, h_col) in enumerate(headers_t):
    cell = tbl.cell(0, j)
    cell.fill.solid(); cell.fill.fore_color.rgb = CARD_BG
    p = cell.text_frame.paragraphs[0]
    p.text = h_text
    p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = h_col

rows_data = [
    ("Invoice",      "String",  "Mã số hóa đơn (Bắt đầu 'C' là đơn hủy)"),
    ("StockCode",    "String",  "Mã định danh sản phẩm hàng hóa"),
    ("Description",  "String",  "Tên mô tả sản phẩm (thiếu 4,382 dòng)"),
    ("Quantity",     "Integer", "Số lượng mua mỗi dòng (có số âm)"),
    ("InvoiceDate",  "Datetime","Thời điểm giao dịch phát sinh"),
    ("Price",        "Float",   "Đơn giá mỗi sản phẩm tính theo Bảng Anh (£)"),
    ("CustomerID",   "Float",   "Mã khách hàng duy nhất (thiếu 243,007 dòng)"),
    ("Country",      "String",  "Quốc gia nơi khách hàng cư trú (43 nước)"),
]
for i, row in enumerate(rows_data):
    for j, val in enumerate(row):
        cell = tbl.cell(i+1, j)
        cell.fill.solid(); cell.fill.fore_color.rgb = RGBColor(0x13, 0x1d, 0x2e)
        p = cell.text_frame.paragraphs[0]
        p.text = val
        p.font.size = Pt(10)
        p.font.color.rgb = WHITE if j==0 else (AMBER if j==1 else LIGHT)

# Right: Heatmap
img(sl, "fig_eda_correlation_heatmap.png", Inches(7.5), Inches(1.45), Inches(5.4), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 4 — EDA KINH DOANH: DOANH THU & TÍNH MÙA VỤ
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "02 · KHÁM PHÁ DỮ LIỆU", "Xu Hướng Doanh Thu Hàng Tháng & Tính Mùa Vụ Bán Lẻ", AMBER)

img(sl, "fig03_eda_monthly_revenue.png", Inches(0.4), Inches(1.4), Inches(8.8), Inches(5.7))

# Right KPI insights
kpi_card(sl, "Q4 Peak", "Tháng 10 – 12 bùng nổ\n(Dịp Noel & Năm mới)",
         Inches(9.5), Inches(1.5), w=Inches(3.4), h=Inches(1.5), num_color=AMBER)
kpi_card(sl, "2 Năm", "Dữ liệu liên tục\n12/2009 – 12/2011",
         Inches(9.5), Inches(3.2), w=Inches(3.4), h=Inches(1.5), num_color=EMERALD)
kpi_card(sl, "> £18M", "Tổng giá trị giao dịch\ntrong 2 năm khảo sát",
         Inches(9.5), Inches(4.9), w=Inches(3.4), h=Inches(1.5), num_color=BLUE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 5 — EDA KINH DOANH: THỊ TRƯỜNG & TOP SẢN PHẨM
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "02 · KHÁM PHÁ DỮ LIỆU", "Phân Bố Thị Trường Quốc Gia & Top Sản Phẩm Bán Chạy", EMERALD)

# Left: Countries
img(sl, "fig_eda_top_countries.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(5.6))
# Right: Products
img(sl, "fig_eda_top_products.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 6 — EDA THÁCH THỨC: PHÂN PHỐI LỆCH & DỮ LIỆU KHUYẾT THIẾU
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "02 · KHÁM PHÁ DỮ LIỆU", "Dữ Liệu Thô: Phân Phối Lệch Phải Cực Đoan & Dòng Khuyết Thiếu", CORAL)

img(sl, "fig01_eda_quantity_price_dist.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

# Right 4 Warning KPI Cards
kpi_card(sl, "243,007", "Thiếu CustomerID\n(~22.8% dữ liệu)",
         Inches(9.2), Inches(1.45), w=Inches(3.7), h=Inches(1.3), num_color=CORAL, bg_color=CARD_WARN)
kpi_card(sl, "34,335", "Dòng trùng lặp\n(Đơn duplicate 3.2%)",
         Inches(9.2), Inches(2.9), w=Inches(3.7), h=Inches(1.3), num_color=AMBER, bg_color=CARD_WARN)
kpi_card(sl, "22,950", "Quantity < 0\n(Đơn trả hàng / Hủy)",
         Inches(9.2), Inches(4.35), w=Inches(3.7), h=Inches(1.3), num_color=CORAL, bg_color=CARD_WARN)
kpi_card(sl, "6,207", "Price <= 0\n(Điều chỉnh kho / Quà)",
         Inches(9.2), Inches(5.8), w=Inches(3.7), h=Inches(1.3), num_color=AMBER, bg_color=CARD_WARN)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 7 — EDA THÁCH THỨC: NGOẠI LỆ CỰC ĐOAN (OUTLIERS)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "02 · KHÁM PHÁ DỮ LIỆU", "Phát Hiện Ngoại Lệ Cực Đoan Qua Biểu Đồ Boxplot", CORAL)

img(sl, "fig02_eda_boxplot_outliers.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

# Right: Explanation
panel = sl.shapes.add_shape(1, Inches(9.2), Inches(1.45), Inches(3.7), Inches(5.65))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = CORAL; panel.line.width = Pt(1.5)

txb(sl, "⚠️ ĐẶC ĐIỂM NGOẠI LỆ", Inches(9.4), Inches(1.65), Inches(3.3), Inches(0.4),
    size=14, bold=True, color=CORAL, align=PP_ALIGN.CENTER)

notes = [
    ("Quantity đột biến:", "Có đơn hàng mua tới 80,000 sản phẩm (giao dịch bán buôn B2B cực lớn)."),
    ("Price bất thường:", "Một số sản phẩm có giá hàng nghìn £ (phí bưu điện, chỉnh mã hệ thống)."),
    ("Rủi ro mô hình:", "K-Means dùng khoảng cách Euclidean sẽ bị các điểm này kéo dạt trọng tâm."),
    ("Giải pháp:", "Không xóa thô bạo mà bóc tách bằng mô hình mật độ DBSCAN."),
]
ty = Inches(2.2)
for t, d in notes:
    txb(sl, t, Inches(9.4), ty, Inches(3.3), Inches(0.35), size=12, bold=True, color=AMBER)
    txb(sl, d, Inches(9.4), ty + Inches(0.32), Inches(3.3), Inches(0.55), size=11, color=LIGHT)
    ty += Inches(0.9)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 8 — BẪY BASELINE BAN ĐẦU (The Baseline Trap)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "03 · BẪY BASELINE", "Silhouette Đạt 0.64 — Nhưng 98.2% Dữ Liệu Dồn Vào 1 Cụm!", CORAL)

img(sl, "fig02_clean_boxplot_outliers.png", Inches(0.4), Inches(1.4), Inches(8.0), Inches(5.7))

# Right trap details
panel = sl.shapes.add_shape(1, Inches(8.7), Inches(1.45), Inches(4.2), Inches(5.65))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_WARN
panel.line.color.rgb = CORAL; panel.line.width = Pt(2)

txb(sl, "🚨 KẾT QUẢ GIẢ MẠO", Inches(8.9), Inches(1.65), Inches(3.8), Inches(0.4),
    size=16, bold=True, color=CORAL, align=PP_ALIGN.CENTER)

scores = [
    ("K-Means Baseline",      "Sil = 0.6417"),
    ("Hierarchical Baseline", "Sil = 0.6258"),
    ("DBSCAN Baseline",       "Sil = 0.6440"),
]
ty = Inches(2.2)
for m, s in scores:
    txb(sl, m, Inches(8.9), ty, Inches(2.2), Inches(0.35), size=13, color=LIGHT)
    txb(sl, s, Inches(11.1), ty, Inches(1.6), Inches(0.35), size=13, bold=True, color=AMBER, align=PP_ALIGN.RIGHT)
    ty += Inches(0.45)

ln = sl.shapes.add_shape(1, Inches(8.9), Inches(3.6), Inches(3.8), Inches(0.02))
ln.fill.solid(); ln.fill.fore_color.rgb = CORAL; ln.line.fill.background()

txb(sl, "Bản chất thất bại:", Inches(8.9), Inches(3.75), Inches(3.8), Inches(0.35), size=13, bold=True, color=CORAL)
txb(sl, "• Baseline gom trên từng dòng GIAO DỊCH (Transaction-level) thay vì KHÁCH HÀNG.\n• Cụm 0 nuốt trọn 98.2% dữ liệu.\n• Cụm 1, 2 chỉ chứa 1-2 điểm outlier cực đoan.\n• Điểm Silhouette cao giả vì các outlier đứng cách quá xa cụm lớn!",
    Inches(8.9), Inches(4.15), Inches(3.8), Inches(2.7), size=12, color=LIGHT)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 9 — PHỄU TIỀN XỬ LÝ DỮ LIỆU 5 BƯỚC
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "04 · TIỀN XỬ LÝ", "Quy Trình Làm Sạch Dữ Liệu 5 Bước (Data Cleaning Funnel)", EMERALD)

img(sl, "fig04_preprocessing_funnel.png", Inches(0.4), Inches(1.4), Inches(8.8), Inches(5.7))

# Right Funnel steps KPI
kpi_card(sl, "1,067,371", "Dữ liệu ban đầu\n(2 năm giao dịch)",
         Inches(9.5), Inches(1.5), w=Inches(3.4), h=Inches(1.2), num_color=WHITE)
kpi_card(sl, "805,549", "Giao dịch hợp lệ\n(Loại trùng, rác, thiếu ID)",
         Inches(9.5), Inches(2.95), w=Inches(3.4), h=Inches(1.2), num_color=BLUE)
kpi_card(sl, "4,275", "Khách hàng duy nhất\n(Tập phân tích RFM)",
         Inches(9.5), Inches(4.4), w=Inches(3.4), h=Inches(1.2), num_color=EMERALD)
kpi_card(sl, "100%", "Dữ liệu sẵn sàng\n(Không còn NaN, Null)",
         Inches(9.5), Inches(5.85), w=Inches(3.4), h=Inches(1.2), num_color=AMBER)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 10 — RÚT TRÍCH ĐẶC TRƯNG RFM
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "05 · KỸ NGHỆ ĐẶC TRƯNG", "Rút Trích Bộ 3 Chỉ Số Vàng RFM (Recency - Frequency - Monetary)", BLUE)

# Left: Explanation cards
rfm_defs = [
    ("R", "Recency (Độ mới)", "Số ngày kể từ lần mua hàng gần nhất của khách đến mốc chốt sổ dữ liệu. R càng nhỏ khách càng gắn kết.", BLUE),
    ("F", "Frequency (Tần suất)", "Tổng số hóa đơn mua hàng duy nhất của khách. F càng cao mức độ trung thành càng lớn.", EMERALD),
    ("M", "Monetary (Doanh thu)", "Tổng số tiền khách hàng đã đóng góp (Quantity × Price). Phản ánh giá trị tài chính thực tế.", AMBER),
]
ty = Inches(1.5)
for code, name, desc, col in rfm_defs:
    rect = sl.shapes.add_shape(1, Inches(0.4), ty, Inches(4.5), Inches(1.65))
    rect.fill.solid(); rect.fill.fore_color.rgb = CARD_BG
    rect.line.color.rgb = col; rect.line.width = Pt(1.5)
    
    txb(sl, f"{code} · {name}", Inches(0.6), ty + Inches(0.12), Inches(4.1), Inches(0.4), size=14, bold=True, color=col)
    txb(sl, desc, Inches(0.6), ty + Inches(0.55), Inches(4.1), Inches(0.95), size=11, color=LIGHT)
    ty += Inches(1.85)

# Right: Raw RFM distributions
img(sl, "fig01_rfm_raw_distribution.png", Inches(5.2), Inches(1.4), Inches(7.7), Inches(5.7))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 11 — BIẾN ĐỔI LOG TRANSFORM & CHUẨN HÓA
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "05 · KỸ NGHỆ ĐẶC TRƯNG", "Biến Đổi Log Transform: Triệt Tiêu Độ Lệch & Đưa Về Phân Phối Chuẩn", EMERALD)

img(sl, "fig02_rfm_log_distribution.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

# 4 KPI cards on right
kpi_card(sl, "24.22 → 0.31", "Monetary Skew\n(Giảm 98.7% độ lệch!)",
         Inches(9.2), Inches(1.45), w=Inches(3.7), h=Inches(1.3), num_color=EMERALD)
kpi_card(sl, "9.94 → 1.17", "Frequency Skew\n(Giảm 86.1% độ lệch)",
         Inches(9.2), Inches(2.9), w=Inches(3.7), h=Inches(1.3), num_color=BLUE)
kpi_card(sl, "1.29 → -0.44", "Recency Skew\n(Phân phối đối xứng)",
         Inches(9.2), Inches(4.35), w=Inches(3.7), h=Inches(1.3), num_color=AMBER)
kpi_card(sl, "StandardScaler", "Chuẩn hóa z-score\n(mean=0, std=1)",
         Inches(9.2), Inches(5.8), w=Inches(3.7), h=Inches(1.3), num_color=WHITE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 12 — TƯƠNG QUAN & KHÔNG GIAN 3D RFM
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "05 · KỸ NGHỆ ĐẶC TRƯNG", "Ma Trận Tương Quan & Không Gian Đặc Trưng 3D RFM", BLUE)

img(sl, "fig03_rfm_correlation_and_scatter.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(5.6))
img(sl, "fig04_rfm_3d_feature_space.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 13 — CHIẾN LƯỢC CHIA TẬP DỮ LIỆU
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "06 · PHÂN CHIA DỮ LIỆU", "Chiến Lược Chia Train / Validation / Test Chống Rò Rỉ Dữ Liệu", AMBER)

img(sl, "fig03_train_val_test_split.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

# 3 Split Cards on right
kpi_card(sl, "2,736 KH", "TẬP TRAIN (64%)\nHuấn luyện mô hình",
         Inches(9.2), Inches(1.5), w=Inches(3.7), h=Inches(1.5), num_color=EMERALD)
kpi_card(sl, "684 KH", "TẬP VALIDATION (16%)\nDò tìm siêu tham số tối ưu",
         Inches(9.2), Inches(3.2), w=Inches(3.7), h=Inches(1.5), num_color=BLUE)
kpi_card(sl, "855 KH", "TẬP TEST (20%)\nKiểm thử khách quan cuối cùng",
         Inches(9.2), Inches(4.9), w=Inches(3.7), h=Inches(1.5), num_color=AMBER)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 14 — K-MEANS TUNING: XÁC ĐỊNH K TỐI ƯU
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "07 · MÔ HÌNH K-MEANS", "Phương Pháp Elbow SSE & Hệ Số Silhouette Tìm K Tối Ưu", BLUE)

img(sl, "fig04_elbow_method_sse.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(4.6))
img(sl, "fig05_silhouette_scores_k.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(4.6))

# Bottom summary card
panel = sl.shapes.add_shape(1, Inches(0.4), Inches(6.15), Inches(12.5), Inches(1.05))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = BLUE; panel.line.width = Pt(1.5)

txb(sl, "KẾT LUẬN CHỌN K=4:", Inches(0.7), Inches(6.3), Inches(2.5), Inches(0.4), size=13, bold=True, color=AMBER)
txb(sl, "• Điểm uốn Elbow xuất hiện rõ rệt tại K=4 (độ dốc giảm SSE bắt đầu chững lại).\n• Hệ số Silhouette đạt đỉnh ổn định (0.3385 trên Train), phân cụm đồng đều, dễ giải thích kinh doanh.",
    Inches(3.2), Inches(6.25), Inches(9.5), Inches(0.85), size=12, color=LIGHT)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 15 — K-MEANS SCENARIOS & PHÂN TÍCH ANOVA
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "07 · MÔ HÌNH K-MEANS", "Không Gian 2D PCA & Phân Tích ANOVA: Frequency Quan Trọng Nhất", BLUE)

img(sl, "fig_kmeans_scenarios_2d.png", Inches(0.4), Inches(1.4), Inches(7.5), Inches(5.7))

# Right: ANOVA F-scores
kpi_card(sl, "2,475.70", "F-Score: FREQUENCY\n(Đóng góp phân cụm lớn nhất)",
         Inches(8.2), Inches(1.5), w=Inches(4.7), h=Inches(1.2), num_color=EMERALD)
kpi_card(sl, "1,930.28", "F-Score: RECENCY\n(Đóng góp quan trọng thứ nhì)",
         Inches(8.2), Inches(2.9), w=Inches(4.7), h=Inches(1.2), num_color=BLUE)
kpi_card(sl, "1,928.51", "F-Score: MONETARY\n(Đóng góp giá trị tài chính)",
         Inches(8.2), Inches(4.3), w=Inches(4.7), h=Inches(1.2), num_color=AMBER)

# Silhouette Train/Val/Test
box_s = sl.shapes.add_shape(1, Inches(8.2), Inches(5.7), Inches(4.7), Inches(1.35))
box_s.fill.solid(); box_s.fill.fore_color.rgb = CARD_BG
box_s.line.color.rgb = BLUE; box_s.line.width = Pt(1)

txb(sl, "SILHOUETTE SCORE K=4", Inches(8.4), Inches(5.8), Inches(4.3), Inches(0.3), size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
txb(sl, "Train: 0.3385  |  Val: 0.3193  |  Test: 0.3253", Inches(8.4), Inches(6.15), Inches(4.3), Inches(0.4), size=14, bold=True, color=EMERALD, align=PP_ALIGN.CENTER)
txb(sl, "✓ Độ khái quát hóa cực tốt, không bị Overfitting", Inches(8.4), Inches(6.55), Inches(4.3), Inches(0.35), size=11, italic=True, color=LIGHT, align=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 16 — HIERARCHICAL CLUSTERING TUNING
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "08 · MÔ HÌNH HIERARCHICAL", "Cây Phân Cấp Dendrogram & So Sánh 7 Kịch Bản Linkage", AMBER)

img(sl, "fig10_dendrogram_ward.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(4.6))
img(sl, "fig_hierarchical_scenarios_2d.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(4.6))

# Bottom KPIs
kpi_card(sl, "0.6728", "Cophenetic Correlation\n(Bảo toàn khoảng cách dữ liệu)",
         Inches(0.4), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=AMBER)
kpi_card(sl, "0.3210", "Test Silhouette\n(Ward Linkage K=4)",
         Inches(4.7), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=EMERALD)
kpi_card(sl, "Ward Linkage", "Tối ưu hóa tổng phương sai\n(Vượt trội Complete & Average)",
         Inches(9.0), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=BLUE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 17 — DBSCAN TUNING: MẬT ĐỘ & OUTLIERS
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "09 · MÔ HÌNH DBSCAN", "Biểu Đồ K-Distance & Khả Năng Tách Ngoại Lệ Cực Đoan", CORAL)

img(sl, "fig11_kdistance_multiline.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(4.6))
img(sl, "fig_dbscan_scenarios_2d.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(4.6))

# Bottom KPIs
kpi_card(sl, "eps = 0.6", "Bán kính lân cận tối ưu\n(Điểm uốn K-distance)",
         Inches(0.4), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=CORAL)
kpi_card(sl, "MinPts = 10", "Mật độ điểm tối thiểu\n(Chống nhiễu ngoại vi)",
         Inches(4.7), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=AMBER)
kpi_card(sl, "43 KH (1.57%)", "Ngoại lệ phát hiện\n(Super Whales giá trị cao)",
         Inches(9.0), Inches(6.15), w=Inches(3.9), h=Inches(1.05), num_color=EMERALD)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 18 — BENCHMARK TỔNG HỢP 3 MÔ HÌNH
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "10 · ĐÁNH GIÁ ĐỐI SÁNH", "So Sánh Định Lượng K-Means · Hierarchical · DBSCAN", EMERALD)

img(sl, "fig06_model_comparison_metrics.png", Inches(0.4), Inches(1.4), Inches(6.2), Inches(5.6))
img(sl, "fig_comparison_kmeans_vs_hierarchical_dbscan.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 19 — CHÂN DUNG 4 PHÂN KHÚC K-MEANS
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "11 · HỒ SƠ PHÂN KHÚC", "Chân Dung 4 Nhóm Khách Hàng Từ Mô Hình K-Means K=4", EMERALD)

img(sl, "fig08_rfm_cluster_profiles.png", Inches(0.4), Inches(1.4), Inches(7.5), Inches(5.7))

# 4 Segment Cards on right
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
# SLIDE 20 — HYBRID 2-STAGE: K-MEANS + DBSCAN
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "12 · MÔ HÌNH LAI HYBRID", "Kết Hợp K-Means + DBSCAN: Tách Rời 22 Super Whales B2B", AMBER)

img(sl, "fig12_hybrid_pca_and_whales_snake.png", Inches(0.4), Inches(1.4), Inches(8.8), Inches(5.7))

# Right: Super whale cards
kpi_card(sl, "22 KH", "SUPER WHALES B2B\n(Khách sỉ siêu cá mập)",
         Inches(9.5), Inches(1.5), w=Inches(3.4), h=Inches(1.2), num_color=AMBER)
kpi_card(sl, "£55,725", "DOANH THU TRUNG BÌNH\n(Gấp 11 lần VIP thường!)",
         Inches(9.5), Inches(2.95), w=Inches(3.4), h=Inches(1.2), num_color=EMERALD)
kpi_card(sl, "8 Nhóm", "MICRO-SEGMENTS\n(Phân tầng siêu chi tiết)",
         Inches(9.5), Inches(4.4), w=Inches(3.4), h=Inches(1.2), num_color=BLUE)
kpi_card(sl, "Bảo Toàn", "KHÔNG LỆCH TÂM\n(Cụm bán lẻ chuẩn xác)",
         Inches(9.5), Inches(5.85), w=Inches(3.4), h=Inches(1.2), num_color=WHITE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 21 — TRI-MODEL CONSENSUS
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "13 · ĐỒNG THUẬN TRI-MODEL", "Mô Hình Ensemble Đồng Thuận Cả 3 Thuật Toán", EMERALD)

img(sl, "fig_tri_model_hybrid_consensus_2d.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

# 3 Zone Cards on right
kpi_card(sl, "80.85%", "CORE CONSENSUS (2,212 KH)\n3 mô hình tuyệt đối đồng thuận\nSilhouette = 0.420",
         Inches(9.2), Inches(1.5), w=Inches(3.7), h=Inches(1.6), num_color=EMERALD)
kpi_card(sl, "17.58%", "BOUNDARY ZONE (481 KH)\nVùng ranh giới nhạy cảm\nCần Marketing thử nghiệm",
         Inches(9.2), Inches(3.4), w=Inches(3.7), h=Inches(1.6), num_color=AMBER)
kpi_card(sl, "1.57%", "SUPER WHALES (43 KH)\nNgoại lệ giá trị cao\nDoanh thu TB £24,375",
         Inches(9.2), Inches(5.3), w=Inches(3.7), h=Inches(1.6), num_color=CORAL)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 22 — CHIẾN LƯỢC KINH DOANH THỰC TẾ
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "14 · ỨNG DỤNG THỰC TẾ", "Kế Hoạch Hành Động Cá Nhân Hóa Cho Từng Phân Khúc", BLUE)

# 5 Action boxes on left
actions = [
    ("🐳 Super Whales B2B", "Chăm sóc 1:1 qua Account Manager riêng, chiết khấu sỉ, SLA giao hàng ưu tiên.", AMBER),
    ("🏆 VIP Loyal",         "Chương trình khách hàng thân thiết, Early Access sản phẩm mới, tặng quà sinh nhật.", EMERALD),
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

# Right: Benchmark bars
img(sl, "fig13_note_final_benchmark_bars.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 23 — TỔNG KẾT & CẢM ƠN (Q&A)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

# Left accent bar
bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.2), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

txb(sl, "15 · TỔNG KẾT ĐỒ ÁN", Inches(0.5), Inches(0.5), Inches(6.5), Inches(0.4), size=12, bold=True, color=EMERALD)
txb(sl, "Đóng Góp Cốt Lõi Của Đề Tài", Inches(0.5), Inches(0.9), Inches(6.5), Inches(0.7), size=28, bold=True, color=WHITE)

checks = [
    ("✅", "Làm sạch chuẩn xác 1,067,371 giao dịch, loại bỏ hoàn toàn nhiễu."),
    ("✅", "Vượt qua Bẫy Baseline (Transaction-level) bằng kỹ nghệ RFM + Log transform."),
    ("✅", "Chứng minh Frequency (F=2475.7) là thuộc tính định hình cụm mạnh nhất."),
    ("✅", "Tối ưu hóa thành công 3 thuật toán: K-Means (K=4), Hierarchical, DBSCAN."),
    ("✅", "Đột phá với Hybrid 2-Stage & Tri-Model: Bóc tách cá mập B2B (£55.7K) & vùng lõi 80.85%."),
    ("✅", "Xây dựng Playbook chiến lược cá nhân hóa gia tăng giá trị trọn đời (CLV)."),
]
ty = Inches(1.8)
for icon, txt in checks:
    txb(sl, f"{icon}  {txt}", Inches(0.5), ty, Inches(6.3), Inches(0.65), size=13, color=LIGHT)
    ty += Inches(0.75)

txb(sl, "Nhóm 05 · Đại học Sài Gòn (SGU) · 2024–2025", Inches(0.5), Inches(6.5), Inches(6.0), Inches(0.4), size=12, color=GRAY)

# Right: Thank you + figure
img(sl, "fig_tri_model_hybrid_consensus_2d.png", Inches(7.2), Inches(0.5), Inches(5.7), Inches(4.2))

txb(sl, "CẢM ƠN QUÝ THẦY CÔ\nVÀ CÁC BẠN ĐÃ LẮNG NGHE!", Inches(7.2), Inches(4.9), Inches(5.7), Inches(1.5),
    size=26, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

txb(sl, "Q & A", Inches(7.2), Inches(6.4), Inches(5.7), Inches(0.6),
    size=22, bold=True, color=AMBER, align=PP_ALIGN.CENTER)


# ─── Save ─────────────────────────────────────────────────────────
out_path = "Slide_Cuoi_Ky_Nhom05_OnlineRetailII.pptx"
prs.save(out_path)
print(f"[OK] Saved: {out_path}")
print(f"     Total slides: {len(prs.slides)}")
