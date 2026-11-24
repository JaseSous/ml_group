# -*- coding: utf-8 -*-
"""
Export 2D PCA visualization of all 3 Baseline models with feature loading vectors.
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN

out_dir = "Do_an_CuoiKy/figures"
os.makedirs(out_dir, exist_ok=True)

# 1. Load data
train_df = pd.read_csv("Do_an_CuoiKy/data/train.csv")
features = ['Quantity', 'Price', 'TotalPrice']

X_train_raw = train_df[features]
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_raw)

# 2. PCA on Train
pca = PCA(n_components=2, random_state=42)
pca.fit(X_train_scaled)

var_exp = pca.explained_variance_ratio_ * 100
print(f"Explained Variance: PC1={var_exp[0]:.1f}%, PC2={var_exp[1]:.1f}% (Total: {sum(var_exp):.1f}%)")

# 3. Sample 5,000 for clear visualization
np.random.seed(42)
sample_idx = np.random.choice(len(X_train_scaled), size=5000, replace=False)
X_sub = X_train_scaled[sample_idx]
X_sub_pca = pca.transform(X_sub)

# 4. Fit Baseline models on sample
km = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)
km_labels = km.fit_predict(X_sub)

agg = AgglomerativeClustering(n_clusters=4, linkage='ward')
agg_labels = agg.fit_predict(X_sub)

db = DBSCAN(eps=0.5, min_samples=10)
db_labels = db.fit_predict(X_sub)

# 5. Create figure: 3 subplots side by side
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, axes = plt.subplots(1, 3, figsize=(18, 5.5), sharex=True, sharey=True)

# Colors
palette_km = ['#2563eb', '#dc2626', '#10b981']
palette_agg = ['#2563eb', '#dc2626', '#10b981', '#f59e0b']
db_unique = sorted(list(set(db_labels)))
palette_db = {}
base_colors = sns.color_palette("tab10", len(db_unique))
for idx, lbl in enumerate(db_unique):
    if lbl == -1:
        palette_db[lbl] = '#94a3b8' # Gray for noise
    else:
        palette_db[lbl] = base_colors[idx]

# Subplot 1: K-Means
ax = axes[0]
for clr_idx, c in enumerate(range(3)):
    mask = (km_labels == c)
    ax.scatter(X_sub_pca[mask, 0], X_sub_pca[mask, 1], s=25, alpha=0.65,
               c=palette_km[clr_idx], label=f"Cụm {c} ({np.sum(mask):,})")
ax.set_title("1. K-Means Baseline (K=3)\nSil = 0.6417 | DB = 0.6040", fontsize=11, fontweight='bold', color='#1e293b')
ax.set_xlabel(f"PCA 1 ({var_exp[0]:.1f}%) — Kéo bởi Quantity & TotalPrice", fontsize=9, fontweight='bold')
ax.set_ylabel(f"PCA 2 ({var_exp[1]:.1f}%) — Kéo bởi Price", fontsize=9, fontweight='bold')
ax.legend(loc='upper right', frameon=True, fontsize=8)

# Subplot 2: Hierarchical
ax = axes[1]
for clr_idx, c in enumerate(range(4)):
    mask = (agg_labels == c)
    ax.scatter(X_sub_pca[mask, 0], X_sub_pca[mask, 1], s=25, alpha=0.65,
               c=palette_agg[clr_idx], label=f"Cụm {c} ({np.sum(mask):,})")
ax.set_title("2. Hierarchical Baseline (K=4, Ward)\nSil = 0.6566 | DB = 0.6074", fontsize=11, fontweight='bold', color='#1e293b')
ax.set_xlabel(f"PCA 1 ({var_exp[0]:.1f}%) — Kéo bởi Quantity & TotalPrice", fontsize=9, fontweight='bold')
ax.legend(loc='upper right', frameon=True, fontsize=8)

# Subplot 3: DBSCAN
ax = axes[2]
for lbl in db_unique:
    mask = (db_labels == lbl)
    name = f"Nhiễu / Outlier (-1) ({np.sum(mask):,})" if lbl == -1 else f"Cụm {lbl} ({np.sum(mask):,})"
    ax.scatter(X_sub_pca[mask, 0], X_sub_pca[mask, 1], s=25, alpha=0.7 if lbl != -1 else 0.4,
               c=[palette_db[lbl]], label=name)
ax.set_title("3. DBSCAN Baseline (eps=0.5, MinPts=10)\nSil = 0.6600 | DB = 0.4015", fontsize=11, fontweight='bold', color='#1e293b')
ax.set_xlabel(f"PCA 1 ({var_exp[0]:.1f}%) — Kéo bởi Quantity & TotalPrice", fontsize=9, fontweight='bold')
ax.legend(loc='upper right', frameon=True, fontsize=8)

# Feature loading vectors on Subplot 1
loadings = pca.components_
scale_factor = 4.0
for i, feat in enumerate(features):
    axes[0].arrow(0, 0, loadings[0, i]*scale_factor, loadings[1, i]*scale_factor,
                  color='#d97706', width=0.08, head_width=0.35, alpha=0.9, zorder=5)
    axes[0].text(loadings[0, i]*scale_factor*1.15, loadings[1, i]*scale_factor*1.15,
                 f"Vector: {feat}", color='#b45309', fontsize=9, fontweight='bold', zorder=6)

plt.suptitle("SO SÁNH KHÔNG GIAN 2D PCA CỦA 3 MÔ HÌNH BASELINE TRÊN DỮ LIỆU GIAO DỊCH\n(StandardScaler trên ['Quantity', 'Price', 'TotalPrice'])",
             fontsize=13, fontweight='bold', y=1.03)
plt.tight_layout()

save_path = os.path.join(out_dir, "fig_baseline_pca_2d_models.png")
fig.savefig(save_path, dpi=300, bbox_inches='tight')
plt.close(fig)
print(f"[OK] Successfully saved: {save_path}")
