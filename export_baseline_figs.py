# -*- coding: utf-8 -*-
"""
Export real baseline figures from note_baseline.ipynb to figures/
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid")
out_dir = "Do_an_CuoiKy/figures"
os.makedirs(out_dir, exist_ok=True)

# ── 1. Figure: Benchmark Metrics ──────────────────────────────────
benchmark_data = [
    {'Mô hình': 'K-Means (K=3)', 'Tập dữ liệu': 'Train (64%)', 'Silhouette': 0.6244, 'Davies-Bouldin': 0.6626},
    {'Mô hình': 'K-Means (K=3)', 'Tập dữ liệu': 'Validation (16%)', 'Silhouette': 0.6175, 'Davies-Bouldin': 0.6215},
    {'Mô hình': 'K-Means (K=3)', 'Tập dữ liệu': 'Test (20%)', 'Silhouette': 0.6417, 'Davies-Bouldin': 0.6040},
    {'Mô hình': 'Hierarchical (K=4)', 'Tập dữ liệu': 'Train (64%)', 'Silhouette': 0.6258, 'Davies-Bouldin': 0.6843},
    {'Mô hình': 'Hierarchical (K=4)', 'Tập dữ liệu': 'Validation (16%)', 'Silhouette': 0.6346, 'Davies-Bouldin': 0.5358},
    {'Mô hình': 'Hierarchical (K=4)', 'Tập dữ liệu': 'Test (20%)', 'Silhouette': 0.6566, 'Davies-Bouldin': 0.6074},
    {'Mô hình': 'DBSCAN (eps=0.5)', 'Tập dữ liệu': 'Train (64%)', 'Silhouette': 0.6440, 'Davies-Bouldin': 0.3666},
    {'Mô hình': 'DBSCAN (eps=0.5)', 'Tập dữ liệu': 'Validation (16%)', 'Silhouette': 0.6413, 'Davies-Bouldin': 0.3407},
    {'Mô hình': 'DBSCAN (eps=0.5)', 'Tập dữ liệu': 'Test (20%)', 'Silhouette': 0.6600, 'Davies-Bouldin': 0.4015}
]
df_benchmark = pd.DataFrame(benchmark_data)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
sns.barplot(data=df_benchmark, x='Tập dữ liệu', y='Silhouette', hue='Mô hình', palette='viridis', ax=ax1)
ax1.set_title("So sánh Silhouette Score Baseline qua 3 tập (Cao hơn là tốt hơn ↑)", fontsize=11, fontweight='bold')
ax1.set_ylim(0.5, 0.72)
ax1.set_ylabel("Silhouette Score")

sns.barplot(data=df_benchmark, x='Tập dữ liệu', y='Davies-Bouldin', hue='Mô hình', palette='mako', ax=ax2)
ax2.set_title("So sánh Davies-Bouldin Index Baseline qua 3 tập (Thấp hơn là tốt hơn ↓)", fontsize=11, fontweight='bold')
ax2.set_ylim(0.2, 0.8)
ax2.set_ylabel("Davies-Bouldin Index")
plt.tight_layout()
p1 = os.path.join(out_dir, "fig_baseline_metrics_comparison.png")
fig.savefig(p1, dpi=300, bbox_inches='tight')
plt.close(fig)
print(f"[OK] Saved: {p1}")

# ── 2. Figure: Feature Importance ANOVA ───────────────────────────
importance_data = {
    'Thuộc tính': ['Price', 'Quantity', 'TotalPrice'],
    'K-Means (%)': [44.80, 38.48, 16.72],
    'Hierarchical (%)': [30.08, 30.06, 39.86],
    'DBSCAN (%)': [53.11, 29.91, 16.98]
}
df_imp = pd.DataFrame(importance_data)
df_imp_melted = df_imp.melt(id_vars='Thuộc tính', var_name='Mô hình', value_name='Tỷ lệ (%)')

fig2, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df_imp_melted, x='Thuộc tính', y='Tỷ lệ (%)', hue='Mô hình', palette='Set2', ax=ax)
ax.set_title("Mức độ chi phối của các thuộc tính vào từng mô hình Baseline (%)", fontsize=12, fontweight='bold')
ax.set_ylabel("Tỷ lệ đóng góp (%)")
ax.set_xlabel("Thuộc tính giao dịch cơ bản")
for p in ax.patches:
    h = p.get_height()
    if h > 0:
        ax.annotate(f"{h:.1f}%", (p.get_x() + p.get_width() / 2., h),
                    ha='center', va='baseline', fontsize=10, color='black', xytext=(0, 3),
                    textcoords='offset points')
plt.tight_layout()
p2 = os.path.join(out_dir, "fig_baseline_feature_importance.png")
fig2.savefig(p2, dpi=300, bbox_inches='tight')
plt.close(fig2)
print(f"[OK] Saved: {p2}")
