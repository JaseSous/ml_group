# -*- coding: utf-8 -*-
"""
Tao slide bao cao cuoi ky toan dien - Nhom 05
24 Slides - CAU TRUC CHUAN 7 HOI THEO PROJECT_STORY.MD
Visual dominant (hinh anh 60-75%), minimal text, cuc ky ro rang va mach lac
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
    # Left accent line
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
    bar.fill.solid(); bar.fill.fore_color.rgb = tag_color; bar.line.fill.background()
    
    # Act Tag
    txb(slide, act_tag.upper(), Inches(0.4), Inches(0.22), Inches(9.5), Inches(0.35),
        size=11, bold=True, color=tag_color)
    # Title
    txb(slide, title, Inches(0.4), Inches(0.55), Inches(12.5), Inches(0.7),
        size=23, bold=True, color=WHITE)
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
# SLIDE 2 — HỒI 1: BỐI CẢNH & NỖI ĐAU KINH DOANH
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 1 · BỐI CẢNH & NỖI ĐAU KINH DOANH (THE BUSINESS DILEMMA)",
       "Vì Sao Doanh Nghiệp Bắt Buộc Phải Phân Cụm Khách Hàng?", BLUE)

cards_s2 = [
    ("405,714", "Giao dịch thực tế\n(Giai đoạn 2009–2010)", EMERALD),
    ("4,275",   "Khách hàng\nđịnh danh duy nhất",       BLUE),
    ("37",      "Quốc gia\ntoàn cầu (UK 91.2%)",        AMBER),
    ("4,420",   "Mặt hàng\nquà tặng & gia dụng",        CORAL),
]
bx = Inches(0.4)
for num, lbl, col in cards_s2:
    kpi_card(sl, num, lbl, bx, Inches(1.5), w=Inches(2.95), h=Inches(1.4), num_color=col, num_size=26)
    bx += Inches(3.18)

panel = sl.shapes.add_shape(1, Inches(0.4), Inches(3.2), Inches(12.5), Inches(3.9))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = BLUE; panel.line.width = Pt(1.5)

pains = [
    ("❌", "Thực trạng kinh doanh:", "Doanh nghiệp không biết ai là khách VIP, ai đang có nguy cơ rời bỏ (Churn) để chăm sóc."),
    ("📉", "Hệ quả tiếp thị:", "Chiến dịch Marketing 'cào bằng' gây lãng phí ngân sách và tỷ lệ chuyển đổi đơn hàng thấp."),
    ("🔍", "Thách thức Machine Learning:", "Phân phối giao dịch bị lệch phải cực nặng, tồn tại ngoại lai đơn hàng lớn kéo dạt cụm."),
    ("🎯", "Mục tiêu cốt lõi:", "Xây dựng hệ thống phân khúc vi mô (Micro-segmentation) chính xác cao, tăng Customer Lifetime Value (CLV)."),
]
ty = Inches(3.45)
for icon, title, desc in pains:
    txb(sl, f"{icon}  {title}", Inches(0.7), ty, Inches(2.9), Inches(0.45), size=14, bold=True, color=AMBER)
    txb(sl, desc, Inches(3.6), ty, Inches(9.0), Inches(0.7), size=14, color=LIGHT)
    ty += Inches(0.85)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 3 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - CẤU TRÚC THUỘC TÍNH
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
# SLIDE 4 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - XU HƯỚNG DOANH THU
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
# SLIDE 5 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - THỊ TRƯỜNG & SẢN PHẨM
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 2 · KHÁM PHÁ DỮ LIỆU (EDA)",
       "Phân Bố Thị Trường Quốc Gia & Top Sản Phẩm Bán Chạy", EMERALD)

img(sl, "fig_eda_top_countries.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(5.6))
img(sl, "fig_eda_top_products.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 6 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - BỆNH LÝ PHÂN PHỐI LỆCH
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
# SLIDE 7 — HỒI 2: KHÁM PHÁ DỮ LIỆU (EDA) - NGOẠI LẠI THEO IQR
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
# SLIDE 8 — HỒI 3: CÁI BẪY BAN ĐẦU - MÔ HÌNH BASELINE (METRICS)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 3 · CÁI BẪY BAN ĐẦU: MÔ HÌNH BASELINE (THE BASELINE TRAP)",
       "Trực Giác Ban Đầu & Thực Nghiệm 3 Mô Hình Baseline Trên Giao Dịch", BLUE)

img(sl, "fig_baseline_metrics_comparison.png", Inches(0.4), Inches(1.4), Inches(8.5), Inches(5.7))

kpi_card(sl, "K-Means (K=3)", "Mô hình tốt nhất Baseline\nSil Test: 0.6417 | DB: 0.6040\nCalinski-Harabasz: 150,925\nThời gian chạy: 0.52s",
         Inches(9.2), Inches(1.45), w=Inches(3.7), h=Inches(1.75), num_color=EMERALD, num_size=20)
kpi_card(sl, "Hierarchical (K=4)", "Ward Linkage (5K mẫu)\nSil Test: 0.6566 | DB: 0.6074\nGiới hạn bộ nhớ O(N²)",
         Inches(9.2), Inches(3.35), w=Inches(3.7), h=Inches(1.75), num_color=AMBER, num_size=20)
kpi_card(sl, "DBSCAN (eps=0.5)", "MinPts = 10\nSil Test: 0.6600 | DB: 0.4015\nTỷ lệ ngoại lai: 0.94% - 1.94%",
         Inches(9.2), Inches(5.25), w=Inches(3.7), h=Inches(1.75), num_color=CORAL, num_size=20)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 9 — HỒI 3: CÁI BẪY BAN ĐẦU - ANOVA & BƯỚC NGOẶT CHUYỂN TIẾP
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 3 · CÁI BẪY BAN ĐẦU: MÔ HÌNH BASELINE (THE BASELINE TRAP)",
       "Mức Độ Chi Phối Thuộc Tính & Bước Chuyển Sang Cấp Độ Khách Hàng", BLUE)

img(sl, "fig_baseline_feature_importance.png", Inches(0.4), Inches(1.4), Inches(7.5), Inches(5.7))

kpi_card(sl, "Price (44.8%)", "Thuộc tính chi phối lớn nhất K-Means\n(Quantity: 38.5% | TotalPrice: 16.7%)",
         Inches(8.2), Inches(1.45), w=Inches(4.7), h=Inches(1.3), num_color=AMBER)
kpi_card(sl, "Price (53.1%)", "Thuộc tính chi phối lớn nhất DBSCAN\n(Quantity: 29.9% | TotalPrice: 17.0%)",
         Inches(8.2), Inches(2.9), w=Inches(4.7), h=Inches(1.3), num_color=CORAL)

panel = sl.shapes.add_shape(1, Inches(8.2), Inches(4.35), Inches(4.7), Inches(2.75))
panel.fill.solid(); panel.fill.fore_color.rgb = CARD_BG
panel.line.color.rgb = BLUE; panel.line.width = Pt(1.5)

txb(sl, "📌 TẠI SAO PHẢI CHUYỂN SANG RFM?", Inches(8.4), Inches(4.5), Inches(4.3), Inches(0.35),
    size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
txb(sl, "• Mô hình Baseline phân cụm trên cấp độ GIAO DỊCH (Transaction-level) chứ không phải KHÁCH HÀNG (Customer-level).\n• Một khách hàng mua nhiều đơn hàng rời rạc sẽ bị phân mảnh vào các cụm khác nhau.\n• Doanh nghiệp cần hiểu chân dung và hành vi tích lũy của từng cá nhân để cá nhân hóa tiếp thị.\n→ Bước ngoặt bắt buộc: Rút trích bộ 3 chỉ số RFM theo Customer ID!",
    Inches(8.4), Inches(4.9), Inches(4.3), Inches(2.1), size=11, color=LIGHT)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 10 — HỒI 4: BƯỚC NGOẶT KỸ NGHỆ RFM - PHỄU TIỀN XỬ LÝ
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 4 · BƯỚC NGOẶT KỸ NGHỆ ĐẶC TRƯNG RFM (FEATURE ENGINEERING)",
       "Quy Trình Phễu Làm Sạch & Nén Dữ Liệu Về Cấp Độ Khách Hàng", EMERALD)

img(sl, "fig04_preprocessing_funnel.png", Inches(0.4), Inches(1.4), Inches(8.8), Inches(5.7))

kpi_card(sl, "405,714", "Dữ liệu ban đầu\n(Tập nạp gốc)",
         Inches(9.5), Inches(1.5), w=Inches(3.4), h=Inches(1.2), num_color=WHITE)
kpi_card(sl, "-6,743", "Loại bỏ trùng lặp\n(Duplicate 1.66%)",
         Inches(9.5), Inches(2.95), w=Inches(3.4), h=Inches(1.2), num_color=AMBER)
kpi_card(sl, "398,971", "Giao dịch sạch\n(Toàn vẹn 100%)",
         Inches(9.5), Inches(4.4), w=Inches(3.4), h=Inches(1.2), num_color=EMERALD)
kpi_card(sl, "4,275 KH", "Khách hàng duy nhất\n(Gom nhóm theo ID)",
         Inches(9.5), Inches(5.85), w=Inches(3.4), h=Inches(1.2), num_color=BLUE)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 11 — HỒI 4: BƯỚC NGOẶT KỸ NGHỆ RFM - RÚT TRÍCH RFM KINH ĐIỂN
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
# SLIDE 12 — HỒI 4: BƯỚC NGOẶT KỸ NGHỆ RFM - LOG TRANSFORM & CHUẨN HÓA
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
# SLIDE 13 — HỒI 4: BƯỚC NGOẶT KỸ NGHỆ RFM - TƯƠNG QUAN & KHÔNG GIAN 3D
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 4 · BƯỚC NGOẶT KỸ NGHỆ ĐẶC TRƯNG RFM (FEATURE ENGINEERING)",
       "Ma Trận Tương Quan & Không Gian Đặc Trưng 3D RFM", BLUE)

img(sl, "fig03_rfm_correlation_and_scatter.png", Inches(0.4), Inches(1.4), Inches(6.1), Inches(5.6))
img(sl, "fig04_rfm_3d_feature_space.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 14 — HỒI 4: BƯỚC NGOẶT KỸ NGHỆ RFM - CHIA TẬP & NGHỊCH LÝ SILHOUETTE
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
# SLIDE 15 — HỒI 5: CUỘC ĐUA TAM MÃ - K-MEANS TUNING (ELBOW & SILHOUETTE)
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
# SLIDE 16 — HỒI 5: CUỘC ĐUA TAM MÃ - K-MEANS 2D PCA & ANOVA
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
# SLIDE 17 — HỒI 5: CUỘC ĐUA TAM MÃ - HIERARCHICAL TUNING
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
# SLIDE 18 — HỒI 5: CUỘC ĐUA TAM MÃ - DBSCAN TUNING
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
# SLIDE 19 — HỒI 5: CUỘC ĐUA TAM MÃ - ĐỐI CHUẨN 3 THẾ HỆ
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)
header(sl, "HỒI 5 · CUỘC ĐUA TAM MÃ: TINH CHỈNH SIÊU THAM SỐ (THE TUNING JOURNEY)",
       "Đối Chuẩn Tổng Thể: Tiến Hóa Từ Baseline → Untuned RFM → Tuned RFM", EMERALD)

img(sl, "fig06_model_comparison_metrics.png", Inches(0.4), Inches(1.4), Inches(6.2), Inches(5.6))
img(sl, "fig_comparison_kmeans_vs_hierarchical_dbscan.png", Inches(6.8), Inches(1.4), Inches(6.1), Inches(5.6))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 20 — HỒI 5: CUỘC ĐUA TAM MÃ - CHÂN DUNG 4 PHÂN KHÚC K-MEANS
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
# SLIDE 21 — HỒI 6: ĐỘT PHÁ KIẾN TRÚC - MÔ HÌNH LAI 2 TẦNG
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
# SLIDE 22 — HỒI 6: ĐỘT PHÁ KIẾN TRÚC - TRI-MODEL CONSENSUS
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
# SLIDE 23 — HỒI 7: HIỆN THỰC HÓA ỨNG DỤNG - CHIẾN LƯỢC KINH DOANH
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
# SLIDE 24 — HỒI 7: HIỆN THỰC HÓA ỨNG DỤNG - CLI PREDICT & TỔNG KẾT
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.2), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

txb(sl, "HỒI 7 · HIỆN THỰC HÓA ỨNG DỤNG & ĐÓNG GÓI SẢN PHẨM", Inches(0.5), Inches(0.45), Inches(7.5), Inches(0.35), size=11, bold=True, color=EMERALD)
txb(sl, "Đóng Gói CLI predict.py & Tổng Kết Nghiệm Thu", Inches(0.5), Inches(0.85), Inches(7.5), Inches(0.65), size=24, bold=True, color=WHITE)

checks = [
    ("⚡", "Đóng gói CLI predict.py: Tốc độ suy luận < 2 mili-giây / khách hàng."),
    ("✅", "Làm sạch 405,714 giao dịch, toàn vẹn 100% Customer ID, loại 6,743 trùng."),
    ("✅", "Đánh giá Baseline 3 mô hình trên giao dịch: Price (44.8%) chi phối mạnh nhất."),
    ("✅", "Chuyển tiếp lên cấp độ khách hàng bằng kỹ nghệ RFM + Log transform cho 4,275 KH."),
    ("✅", "Chứng minh Frequency (F=2475.7) là thuộc tính định hình phân khúc mạnh nhất."),
    ("✅", "Đột phá Hybrid 2-Stage & Tri-Model: Bóc tách cá mập B2B (£55.7K) & vùng lõi 80.85%."),
    ("✅", "Xây dựng Playbook chiến lược cá nhân hóa gia tăng giá trị trọn đời (CLV)."),
]
ty = Inches(1.6)
for icon, txt in checks:
    txb(sl, f"{icon}  {txt}", Inches(0.5), ty, Inches(7.0), Inches(0.62), size=12, color=LIGHT)
    ty += Inches(0.68)

txb(sl, "Nhóm 05 · Đại học Sài Gòn (SGU) · 2024–2025", Inches(0.5), Inches(6.6), Inches(6.0), Inches(0.4), size=12, color=GRAY)

img(sl, "fig_tri_model_hybrid_consensus_2d.png", Inches(7.7), Inches(0.5), Inches(5.2), Inches(4.2))

txb(sl, "CẢM ƠN QUÝ THẦY CÔ\nVÀ CÁC BẠN ĐÃ LẮNG NGHE!", Inches(7.7), Inches(4.9), Inches(5.2), Inches(1.3),
    size=23, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

txb(sl, "Q & A", Inches(7.7), Inches(6.35), Inches(5.2), Inches(0.55),
    size=22, bold=True, color=AMBER, align=PP_ALIGN.CENTER)


# ─── Save ─────────────────────────────────────────────────────────
out_path = "Slide_Cuoi_Ky_Nhom05_OnlineRetailII.pptx"
try:
    prs.save(out_path)
    print(f"[OK] Saved: {out_path}")
except PermissionError:
    alt_path = "Slide_Cuoi_Ky_Nhom05_OnlineRetailII_7Hoi.pptx"
    prs.save(alt_path)
    print(f"[NOTE] '{out_path}' dang mo trong PowerPoint, da luu ban moi vao: {alt_path}")
print(f"     Total slides: {len(prs.slides)}")
