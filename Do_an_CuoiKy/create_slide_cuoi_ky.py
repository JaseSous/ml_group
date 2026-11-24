# -*- coding: utf-8 -*-
"""
Tao slide bao cao cuoi ky - Nhom 05
Image-heavy, minimal text
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

# ─── Color palette ───────────────────────────────────────────────
NAVY    = RGBColor(0x0f, 0x17, 0x2a)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
EMERALD = RGBColor(0x00, 0xb8, 0x94)
BLUE    = RGBColor(0x09, 0x84, 0xe3)
CORAL   = RGBColor(0xd6, 0x30, 0x31)
AMBER   = RGBColor(0xfd, 0xcb, 0x6e)
GRAY    = RGBColor(0x94, 0xa3, 0xb8)
LIGHT   = RGBColor(0xe2, 0xe8, 0xf0)

# ─── Slide dimensions: 16:9 widescreen ───────────────────────────
W = Inches(13.33)
H = Inches(7.5)

FIGS = "figures"

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H

blank_layout = prs.slide_layouts[6]  # completely blank

# ─── Helpers ─────────────────────────────────────────────────────

def add_bg(slide, color=NAVY):
    """Fill slide background with solid color."""
    from pptx.oxml.ns import qn
    from lxml import etree
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def txb(slide, text, l, t, w, h, size=18, bold=False, color=WHITE,
        align=PP_ALIGN.LEFT, italic=False, wrap=True):
    """Add a text box."""
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.italic = italic
    return tb


def kpi_card(slide, number, label, l, t, w=Inches(2.2), h=Inches(1.3),
             num_color=EMERALD, bg_color=RGBColor(0x1e, 0x29, 0x3b)):
    """Draw a KPI card: big number + small label."""
    from pptx.util import Pt
    # background rect
    rect = slide.shapes.add_shape(
        1, l, t, w, h  # MSO_SHAPE_TYPE.RECTANGLE = 1
    )
    rect.fill.solid()
    rect.fill.fore_color.rgb = bg_color
    rect.line.color.rgb = num_color
    rect.line.width = Pt(1.5)

    # number
    txb(slide, number,
        l + Inches(0.08), t + Inches(0.06),
        w - Inches(0.16), Inches(0.68),
        size=26, bold=True, color=num_color, align=PP_ALIGN.CENTER)
    # label
    txb(slide, label,
        l + Inches(0.08), t + Inches(0.72),
        w - Inches(0.16), Inches(0.52),
        size=11, bold=False, color=LIGHT, align=PP_ALIGN.CENTER)


def img(slide, path, l, t, w, h=None):
    """Add image; h=None keeps aspect ratio via width only."""
    if not os.path.exists(path):
        print(f"  [WARN] missing: {path}")
        return
    if h is None:
        slide.shapes.add_picture(path, l, t, width=w)
    else:
        slide.shapes.add_picture(path, l, t, width=w, height=h)


def pill(slide, text, l, t, color=EMERALD):
    """Small colored pill label."""
    w, h = Inches(2.0), Inches(0.32)
    rect = slide.shapes.add_shape(1, l, t, w, h)
    rect.fill.solid()
    rect.fill.fore_color.rgb = color
    rect.line.fill.background()
    txb(slide, text, l, t, w, h, size=10, bold=True,
        color=WHITE, align=PP_ALIGN.CENTER)


def divider(slide, t, color=EMERALD, l=Inches(0.5), w=None):
    if w is None: w = W - Inches(1)
    ln = slide.shapes.add_shape(1, l, t, w, Inches(0.03))
    ln.fill.solid()
    ln.fill.fore_color.rgb = color
    ln.line.fill.background()


# ═══════════════════════════════════════════════════════════════════
# SLIDE 1 — Cover
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

# Left accent bar
bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.18), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

# Right image panel (architecture figure)
img(sl, f"{FIGS}/fig00_ml_pipeline_architecture.png",
    Inches(7.3), Inches(0.6), Inches(5.7), Inches(6.3))

# Semi-transparent overlay panel on left
panel = sl.shapes.add_shape(1, Inches(0.18), Inches(0), Inches(7.1), H)
panel.fill.solid(); panel.fill.fore_color.rgb = NAVY
panel.line.fill.background()

# Tag line
txb(sl, "ĐỒ ÁN CUỐI KỲ · MÁY HỌC", Inches(0.5), Inches(0.9),
    Inches(6.5), Inches(0.5), size=13, color=EMERALD, bold=True)

# Main title
txb(sl, "Phân Cụm Khách Hàng\nOnline Retail II",
    Inches(0.5), Inches(1.5), Inches(6.5), Inches(2.4),
    size=46, bold=True, color=WHITE)

divider(sl, Inches(3.9), l=Inches(0.5), w=Inches(5.5))

txb(sl, "K-Means · Hierarchical · DBSCAN · Tri-Model Consensus",
    Inches(0.5), Inches(4.0), Inches(6.5), Inches(0.6),
    size=14, color=AMBER, italic=True)

txb(sl, "Nhóm 05 — Trường Đại học Sài Gòn\nGVHD: ……………………………",
    Inches(0.5), Inches(5.0), Inches(6.5), Inches(1.0),
    size=14, color=GRAY)

txb(sl, "2024–2025", Inches(0.5), Inches(6.2),
    Inches(3), Inches(0.5), size=12, color=GRAY)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 2 — Bài toán kinh doanh
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = BLUE; bar.line.fill.background()

txb(sl, "BÀI TOÁN", Inches(0.35), Inches(0.25),
    Inches(6), Inches(0.45), size=11, color=BLUE, bold=True)
txb(sl, "Vì Sao Cần Phân Cụm Khách Hàng?",
    Inches(0.35), Inches(0.65), Inches(8), Inches(0.9),
    size=32, bold=True, color=WHITE)
divider(sl, Inches(1.52), color=BLUE, l=Inches(0.35), w=Inches(8))

bullets = [
    ("🛒", "1,067,371", "giao dịch thực tế\n(2009–2011)", EMERALD),
    ("👤", "4,275",     "khách hàng\nduy nhất",           BLUE),
    ("🌍", "43",        "quốc gia\nmua hàng",             AMBER),
    ("📦", "4,631",     "sản phẩm\nkhác nhau",            CORAL),
]
bx = Inches(0.3)
for icon, num, lbl, col in bullets:
    kpi_card(sl, num, f"{icon} {lbl}", bx, Inches(1.8),
             w=Inches(2.9), h=Inches(1.5), num_color=col,
             bg_color=RGBColor(0x1e, 0x29, 0x3b))
    bx += Inches(3.1)

# Right: pain points
panel = sl.shapes.add_shape(1, Inches(0.3), Inches(3.55), Inches(12.5), Inches(3.65))
panel.fill.solid(); panel.fill.fore_color.rgb = RGBColor(0x1e, 0x29, 0x3b)
panel.line.color.rgb = BLUE; panel.line.width = Pt(1)

pains = [
    ("❌", "Không biết ai là khách VIP, ai sắp rời bỏ"),
    ("📉", "Chiến dịch marketing \"cào bằng\" — lãng phí ngân sách"),
    ("🔍", "Dữ liệu thô: trùng lặp, thiếu, lệch nặng → phân cụm giả"),
    ("🎯", "Mục tiêu: micro-segment → cá nhân hóa → tăng CLV"),
]
ty = Inches(3.75)
for icon, txt in pains:
    txb(sl, f"  {icon}  {txt}", Inches(0.5), ty,
        Inches(12), Inches(0.6), size=15, color=LIGHT)
    ty += Inches(0.72)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 3 — EDA: Phân phối gốc + vấn đề
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = AMBER; bar.line.fill.background()

txb(sl, "KHÁM PHÁ DỮ LIỆU (EDA)",
    Inches(0.35), Inches(0.2), Inches(8), Inches(0.4),
    size=11, color=AMBER, bold=True)
txb(sl, "Dữ Liệu Thô: Phân Phối Lệch & Ngoại Lệ Nặng",
    Inches(0.35), Inches(0.58), Inches(9), Inches(0.75),
    size=28, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=AMBER, l=Inches(0.35), w=Inches(9))

# Big image — raw RFM distributions
img(sl, f"{FIGS}/fig01_rfm_raw_distribution.png",
    Inches(0.25), Inches(1.4), Inches(8.5), Inches(5.8))

# KPI cards on right
kpi_card(sl, "34,335",   "Dòng trùng lặp",
         Inches(8.9), Inches(1.5), num_color=CORAL)
kpi_card(sl, "243,007",  "Thiếu CustomerID",
         Inches(8.9), Inches(2.95), num_color=AMBER)
kpi_card(sl, "Skew 24.22", "Monetary (thô)",
         Inches(8.9), Inches(4.4), num_color=EMERALD)
kpi_card(sl, "22,950",   "Quantity < 0",
         Inches(8.9), Inches(5.85), num_color=CORAL)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 4 — Bẫy Baseline (Silhouette cao = ảo)
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = CORAL; bar.line.fill.background()

txb(sl, "BẪY BASELINE",
    Inches(0.35), Inches(0.2), Inches(8), Inches(0.4),
    size=11, color=CORAL, bold=True)
txb(sl, "Silhouette 0.64 — Nhưng 98.2% Dữ Liệu Dồn Vào 1 Cụm!",
    Inches(0.35), Inches(0.58), Inches(12.5), Inches(0.75),
    size=26, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=CORAL, l=Inches(0.35), w=Inches(12))

# Boxplot image (shows outliers driving false clusters)
img(sl, f"{FIGS}/fig02_eda_boxplot_outliers.png",
    Inches(0.2), Inches(1.4), Inches(8.3), Inches(5.7))

# Right: big warning stats
warn = sl.shapes.add_shape(1, Inches(8.7), Inches(1.5), Inches(4.3), Inches(5.6))
warn.fill.solid(); warn.fill.fore_color.rgb = RGBColor(0x2d, 0x0e, 0x0e)
warn.line.color.rgb = CORAL; warn.line.width = Pt(2)

txb(sl, "⚠️ KẾT QUẢ GIẢ",
    Inches(8.9), Inches(1.7), Inches(4.0), Inches(0.5),
    size=16, bold=True, color=CORAL, align=PP_ALIGN.CENTER)

stats = [
    ("K-Means",      "Sil = 0.6417"),
    ("Hierarchical", "Sil = 0.6258"),
    ("DBSCAN",       "Sil = 0.6440"),
    ("→ Cluster 0",  "98.2% data!"),
]
ty = Inches(2.3)
for m, v in stats:
    txb(sl, m, Inches(8.9), ty, Inches(2.1), Inches(0.55), size=14, color=GRAY)
    txb(sl, v, Inches(11.0), ty, Inches(1.9), Inches(0.55),
        size=14, bold=True,
        color=CORAL if "98" in v else AMBER,
        align=PP_ALIGN.RIGHT)
    ty += Inches(0.7)

txb(sl, "Nguyên nhân:\nOutliers cực đoan\n→ sai phân phối\n→ metric ảo",
    Inches(8.85), Inches(5.1), Inches(4.2), Inches(1.8),
    size=13, color=LIGHT, italic=True)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 5 — RFM Engineering: Xử lý độ lệch
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

txb(sl, "RFM FEATURE ENGINEERING",
    Inches(0.35), Inches(0.2), Inches(10), Inches(0.4),
    size=11, color=EMERALD, bold=True)
txb(sl, "Log Transform: Triệt Tiêu Độ Lệch",
    Inches(0.35), Inches(0.58), Inches(9), Inches(0.75),
    size=30, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=EMERALD, l=Inches(0.35), w=Inches(12))

# Before image
txb(sl, "TRƯỚC (Raw)", Inches(0.3), Inches(1.38),
    Inches(6.2), Inches(0.35), size=12, color=CORAL, bold=True, align=PP_ALIGN.CENTER)
img(sl, f"{FIGS}/fig01_rfm_raw_distribution.png",
    Inches(0.2), Inches(1.72), Inches(6.3), Inches(4.4))

# Arrow
txb(sl, "→", Inches(6.5), Inches(3.6),
    Inches(0.6), Inches(0.6), size=36, bold=True, color=AMBER, align=PP_ALIGN.CENTER)

# After image
txb(sl, "SAU (Log Transform)", Inches(7.0), Inches(1.38),
    Inches(6.0), Inches(0.35), size=12, color=EMERALD, bold=True, align=PP_ALIGN.CENTER)
img(sl, f"{FIGS}/fig02_rfm_log_distribution.png",
    Inches(7.0), Inches(1.72), Inches(6.1), Inches(4.4))

# KPI bar at bottom
kpis = [
    ("24.22 → 0.31", "Monetary Skew\n↓ 98.7%", EMERALD),
    ("9.94 → 1.17",  "Frequency Skew\n↓ 86.1%", BLUE),
    ("1.29 → −0.44", "Recency Skew\n✓ Normal",  AMBER),
    ("4,275",        "Khách hàng\nduy nhất",     CORAL),
]
bx = Inches(0.3)
for num, lbl, col in kpis:
    kpi_card(sl, num, lbl, bx, Inches(6.3),
             w=Inches(3.1), h=Inches(1.0), num_color=col,
             bg_color=RGBColor(0x1e, 0x29, 0x3b))
    bx += Inches(3.26)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 6 — K-Means Tuning & ANOVA
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = BLUE; bar.line.fill.background()

txb(sl, "K-MEANS TUNING",
    Inches(0.35), Inches(0.2), Inches(8), Inches(0.4),
    size=11, color=BLUE, bold=True)
txb(sl, "K=4 Tối Ưu — ANOVA Xác Nhận Frequency Quan Trọng Nhất",
    Inches(0.35), Inches(0.58), Inches(12.5), Inches(0.75),
    size=26, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=BLUE, l=Inches(0.35), w=Inches(12))

# Main scenarios 2D PCA
img(sl, f"{FIGS}/fig_kmeans_scenarios_2d.png",
    Inches(0.2), Inches(1.38), Inches(8.5), Inches(5.8))

# ANOVA F-scores on right
txb(sl, "ANOVA F-SCORE", Inches(8.9), Inches(1.5),
    Inches(4.1), Inches(0.4), size=12, bold=True,
    color=AMBER, align=PP_ALIGN.CENTER)

anova = [
    ("Frequency",  "2,475.70", EMERALD),
    ("Recency",    "1,930.28", BLUE),
    ("Monetary",   "1,928.51", AMBER),
]
ty = Inches(2.05)
for feat, score, col in anova:
    kpi_card(sl, score, feat, Inches(8.85), ty,
             w=Inches(4.2), h=Inches(1.15), num_color=col,
             bg_color=RGBColor(0x1e, 0x29, 0x3b))
    ty += Inches(1.3)

# Train/Val/Test results
txb(sl, "Silhouette K=4",
    Inches(8.85), Inches(5.95), Inches(4.2), Inches(0.4),
    size=12, bold=True, color=AMBER, align=PP_ALIGN.CENTER)
results = [("Train", "0.3385"), ("Val", "0.3193"), ("Test", "0.3253")]
bx2 = Inches(8.85)
for lbl, val in results:
    kpi_card(sl, val, lbl, bx2, Inches(6.38),
             w=Inches(1.33), h=Inches(0.9), num_color=EMERALD,
             bg_color=RGBColor(0x14, 0x2a, 0x14))
    bx2 += Inches(1.42)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 7 — Hierarchical & DBSCAN Tuning
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = AMBER; bar.line.fill.background()

txb(sl, "HIERARCHICAL & DBSCAN TUNING",
    Inches(0.35), Inches(0.2), Inches(10), Inches(0.4),
    size=11, color=AMBER, bold=True)
txb(sl, "Hai Mô Hình Bổ Trợ — Phát Hiện Outlier & Cây Phân Cấp",
    Inches(0.35), Inches(0.58), Inches(12.5), Inches(0.75),
    size=26, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=AMBER, l=Inches(0.35), w=Inches(12))

# Left half: Hierarchical
txb(sl, "HIERARCHICAL WARD  (K=4)",
    Inches(0.3), Inches(1.38), Inches(6.3), Inches(0.4),
    size=12, bold=True, color=BLUE, align=PP_ALIGN.CENTER)
img(sl, f"{FIGS}/fig_hierarchical_scenarios_2d.png",
    Inches(0.2), Inches(1.78), Inches(6.4), Inches(4.6))

# Hierarchical KPIs
kpi_card(sl, "0.6728", "Cophenetic Corr.",
         Inches(0.3), Inches(6.4), w=Inches(3.0), h=Inches(0.85),
         num_color=BLUE, bg_color=RGBColor(0x1e, 0x29, 0x3b))
kpi_card(sl, "0.3210", "Test Silhouette",
         Inches(3.4), Inches(6.4), w=Inches(3.0), h=Inches(0.85),
         num_color=AMBER, bg_color=RGBColor(0x1e, 0x29, 0x3b))

# Divider
vdiv = sl.shapes.add_shape(1, Inches(6.65), Inches(1.3), Inches(0.03), Inches(6.0))
vdiv.fill.solid(); vdiv.fill.fore_color.rgb = GRAY; vdiv.line.fill.background()

# Right half: DBSCAN
txb(sl, "DBSCAN  (eps=0.6, MinPts=10)",
    Inches(6.9), Inches(1.38), Inches(6.1), Inches(0.4),
    size=12, bold=True, color=CORAL, align=PP_ALIGN.CENTER)
img(sl, f"{FIGS}/fig_dbscan_scenarios_2d.png",
    Inches(6.9), Inches(1.78), Inches(6.1), Inches(4.6))

kpi_card(sl, "0.5254", "Silhouette",
         Inches(6.95), Inches(6.4), w=Inches(2.9), h=Inches(0.85),
         num_color=CORAL, bg_color=RGBColor(0x1e, 0x29, 0x3b))
kpi_card(sl, "43 KH",  "Outlier Phát Hiện\n(1.57%)",
         Inches(10.0), Inches(6.4), w=Inches(2.9), h=Inches(0.85),
         num_color=AMBER, bg_color=RGBColor(0x1e, 0x29, 0x3b))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 8 — Kết quả Train / Cluster Profiles
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

txb(sl, "KẾT QUẢ PHÂN CỤM K-MEANS K=4",
    Inches(0.35), Inches(0.2), Inches(10), Inches(0.4),
    size=11, color=EMERALD, bold=True)
txb(sl, "4 Phân Khúc Khách Hàng Rõ Ràng",
    Inches(0.35), Inches(0.58), Inches(9), Inches(0.75),
    size=30, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=EMERALD, l=Inches(0.35), w=Inches(12))

# Cluster profile image
img(sl, f"{FIGS}/fig08_rfm_cluster_profiles.png",
    Inches(0.2), Inches(1.38), Inches(8.0), Inches(5.85))

# Cluster segment cards
segments = [
    ("🏆 VIP",        "18%",  "High F & M",     EMERALD),
    ("🌱 Tiềm năng",  "27%",  "Mid F, low M",   BLUE),
    ("😴 Ngủ đông",   "22%",  "Low F, old R",   AMBER),
    ("🚪 Rời bỏ",     "33%",  "High R, low FM", CORAL),
]
ty = Inches(1.5)
for name, pct, desc, col in segments:
    card = sl.shapes.add_shape(1, Inches(8.4), ty,
                                Inches(4.7), Inches(1.3))
    card.fill.solid(); card.fill.fore_color.rgb = RGBColor(0x1e, 0x29, 0x3b)
    card.line.color.rgb = col; card.line.width = Pt(2)

    txb(sl, name, Inches(8.55), ty + Inches(0.08),
        Inches(2.8), Inches(0.5), size=15, bold=True, color=col)
    txb(sl, pct,  Inches(11.4), ty + Inches(0.08),
        Inches(1.5), Inches(0.5), size=22, bold=True,
        color=col, align=PP_ALIGN.RIGHT)
    txb(sl, desc, Inches(8.55), ty + Inches(0.6),
        Inches(4.3), Inches(0.45), size=11, color=GRAY)
    ty += Inches(1.45)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 9 — Hybrid 2-Stage: Super Whales
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = AMBER; bar.line.fill.background()

txb(sl, "HYBRID 2-STAGE: K-MEANS + DBSCAN",
    Inches(0.35), Inches(0.2), Inches(10), Inches(0.4),
    size=11, color=AMBER, bold=True)
txb(sl, "Phát Hiện 22 Super Whales B2B — Trung Bình £55,725",
    Inches(0.35), Inches(0.58), Inches(12.5), Inches(0.75),
    size=26, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=AMBER, l=Inches(0.35), w=Inches(12))

# Main hybrid comparison figure
img(sl, f"{FIGS}/fig_comparison_kmeans_vs_hierarchical_dbscan.png",
    Inches(0.2), Inches(1.38), Inches(9.0), Inches(5.85))

# Right: super whale KPIs
kpi_card(sl, "22 KH", "Super Whales B2B",
         Inches(9.4), Inches(1.6), w=Inches(3.6), h=Inches(1.3),
         num_color=AMBER, bg_color=RGBColor(0x2a, 0x20, 0x05))
kpi_card(sl, "£55,725", "Monetary TB\n(11× VIP thường)",
         Inches(9.4), Inches(3.1), w=Inches(3.6), h=Inches(1.3),
         num_color=EMERALD, bg_color=RGBColor(0x0a, 0x2a, 0x14))
kpi_card(sl, "8",      "Micro-segments\nsau hybrid",
         Inches(9.4), Inches(4.6), w=Inches(3.6), h=Inches(1.3),
         num_color=BLUE, bg_color=RGBColor(0x1e, 0x29, 0x3b))
kpi_card(sl, "1.57%",  "Outlier = Cơ hội\nB2B ẩn",
         Inches(9.4), Inches(6.1), w=Inches(3.6), h=Inches(1.1),
         num_color=CORAL, bg_color=RGBColor(0x2a, 0x0a, 0x0a))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 10 — Tri-Model Consensus
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

txb(sl, "TRI-MODEL CONSENSUS",
    Inches(0.35), Inches(0.2), Inches(10), Inches(0.4),
    size=11, color=EMERALD, bold=True)
txb(sl, "Ba Mô Hình Đồng Thuận — Độ Tin Cậy Cao Nhất",
    Inches(0.35), Inches(0.58), Inches(12.5), Inches(0.75),
    size=28, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=EMERALD, l=Inches(0.35), w=Inches(12))

# Main consensus 2D figure
img(sl, f"{FIGS}/fig_tri_model_hybrid_consensus_2d.png",
    Inches(0.2), Inches(1.38), Inches(8.8), Inches(5.85))

# 3 consensus KPI cards
cards = [
    ("80.85%",  "Core Consensus\n2,212 khách hàng\nSil = 0.420",  EMERALD),
    ("17.58%",  "Boundary Zone\n481 khách hàng\nCần theo dõi",    AMBER),
    ("1.57%",   "Super Whales\n43 khách hàng\nAVG £24,375",       CORAL),
]
ty = Inches(1.5)
for val, lbl, col in cards:
    kpi_card(sl, val, lbl, Inches(9.2), ty,
             w=Inches(3.9), h=Inches(1.6), num_color=col,
             bg_color=RGBColor(0x1e, 0x29, 0x3b))
    ty += Inches(1.9)

txb(sl, "K-Means + Hierarchical + DBSCAN\n→ Voting nhãn → Lọc ranh giới",
    Inches(9.2), Inches(6.95), Inches(3.9), Inches(0.6),
    size=10, color=GRAY, italic=True, align=PP_ALIGN.CENTER)


# ═══════════════════════════════════════════════════════════════════
# SLIDE 11 — Ứng dụng thực tế
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.12), H)
bar.fill.solid(); bar.fill.fore_color.rgb = BLUE; bar.line.fill.background()

txb(sl, "ỨNG DỤNG THỰC TẾ",
    Inches(0.35), Inches(0.2), Inches(10), Inches(0.4),
    size=11, color=BLUE, bold=True)
txb(sl, "Chiến Lược Cho Từng Phân Khúc",
    Inches(0.35), Inches(0.58), Inches(9), Inches(0.75),
    size=30, bold=True, color=WHITE)
divider(sl, Inches(1.3), color=BLUE, l=Inches(0.35), w=Inches(12))

# 5 segment strategy cards (2 rows)
strategy = [
    ("🐳", "Super Whales\nB2B",     "Account Manager\nriêng · SLA ưu tiên\n· Contract dài hạn", AMBER),
    ("🏆", "VIP\nLoyal",             "Loyalty rewards\n· Early access\n· Upsell premium",         EMERALD),
    ("🌱", "Tiềm Năng\nGrowing",    "Email nurture\n· Cross-sell\n· Promo có thời hạn",           BLUE),
    ("😴", "Ngủ Đông\nAt-Risk",     "Win-back campaign\n· Discount 20%\n· Reminder",              AMBER),
    ("🚪", "Sắp Rời\nChurn",        "Khảo sát lý do\n· Last offer\n· Re-engage",                 CORAL),
]
positions = [
    (Inches(0.3),  Inches(1.5)),
    (Inches(2.75), Inches(1.5)),
    (Inches(5.2),  Inches(1.5)),
    (Inches(1.5),  Inches(4.3)),
    (Inches(4.0),  Inches(4.3)),
]
for (l, t), (icon, seg, strat, col) in zip(positions, strategy):
    cw, ch = Inches(2.3), Inches(2.6)
    card = sl.shapes.add_shape(1, l, t, cw, ch)
    card.fill.solid(); card.fill.fore_color.rgb = RGBColor(0x1e, 0x29, 0x3b)
    card.line.color.rgb = col; card.line.width = Pt(2)
    txb(sl, icon, l + Inches(0.05), t + Inches(0.08),
        cw, Inches(0.55), size=28, align=PP_ALIGN.CENTER)
    txb(sl, seg,  l + Inches(0.05), t + Inches(0.65),
        cw - Inches(0.1), Inches(0.55), size=13, bold=True,
        color=col, align=PP_ALIGN.CENTER)
    txb(sl, strat, l + Inches(0.1), t + Inches(1.2),
        cw - Inches(0.2), Inches(1.3), size=11, color=LIGHT,
        align=PP_ALIGN.CENTER)

# Right: ANOVA figure
img(sl, f"{FIGS}/fig14_anova_fscore_comparison.png",
    Inches(6.7), Inches(1.5), Inches(6.4), Inches(5.8))


# ═══════════════════════════════════════════════════════════════════
# SLIDE 12 — Kết luận & Cảm ơn
# ═══════════════════════════════════════════════════════════════════
sl = prs.slides.add_slide(blank_layout)
add_bg(sl, NAVY)

# Left emerald bar large
bar = sl.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.3), H)
bar.fill.solid(); bar.fill.fore_color.rgb = EMERALD; bar.line.fill.background()

# Left text
txb(sl, "KẾT LUẬN", Inches(0.5), Inches(0.6),
    Inches(6.5), Inches(0.45), size=12, color=EMERALD, bold=True)

checklist = [
    ("✅", "Làm sạch 1,067,371 giao dịch — loại bỏ noise hoàn toàn"),
    ("✅", "RFM + Log transform → phân phối chuẩn, 4,275 KH"),
    ("✅", "So sánh 3 mô hình: K-Means · Hierarchical · DBSCAN"),
    ("✅", "Phát hiện 22 Super Whales B2B — Monetary £55,725 TB"),
    ("✅", "Tri-Model Consensus: 80.85% Core · Sil = 0.420"),
    ("✅", "5 chiến lược cá nhân hóa theo phân khúc"),
]
ty = Inches(1.2)
for icon, txt in checklist:
    txb(sl, f"{icon}  {txt}", Inches(0.5), ty,
        Inches(6.5), Inches(0.68), size=14, color=LIGHT)
    ty += Inches(0.73)

divider(sl, Inches(5.6), color=EMERALD, l=Inches(0.5), w=Inches(6.0))

txb(sl, "Nhóm 05 · SGU · 2024–2025",
    Inches(0.5), Inches(5.75), Inches(6.0), Inches(0.5),
    size=12, color=GRAY)

# Right: big thank you + final figure
img(sl, f"{FIGS}/fig_tri_model_hybrid_consensus_2d.png",
    Inches(7.0), Inches(0.3), Inches(6.1), Inches(4.5))

txb(sl, "CẢM ƠN\nQUÝ THẦY CÔ\nVÀ CÁC BẠN",
    Inches(7.3), Inches(4.9), Inches(5.7), Inches(2.4),
    size=38, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

txb(sl, "Q&A",
    Inches(10.5), Inches(6.95), Inches(2.5), Inches(0.4),
    size=14, color=EMERALD, bold=True, align=PP_ALIGN.CENTER)


# ─── Save ─────────────────────────────────────────────────────────
out_path = "Slide_Cuoi_Ky_Nhom05_OnlineRetailII.pptx"
prs.save(out_path)
print(f"[OK] Saved: {out_path}")
print(f"     Slides: {len(prs.slides)}")
