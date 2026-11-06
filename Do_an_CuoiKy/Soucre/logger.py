import os
import datetime as dt
import pandas as pd
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from Source.init import PATH_EXPERIMENT_LOG

def evaluate_and_log(name, model, data, log_file=PATH_EXPERIMENT_LOG, is_fitted=False):
    """
    Đánh giá mô hình và GHI THÊM (Append) vào file CSV nhật ký ở thư mục gốc.
    """
    if not is_fitted:
        labels = model.fit_predict(data)
    else:
        labels = model.predict(data)

    valid_mask = labels != -1
    
    if len(set(labels[valid_mask])) > 1:
        sil = silhouette_score(data[valid_mask], labels[valid_mask])
        db = davies_bouldin_score(data[valid_mask], labels[valid_mask])
        ch = calinski_harabasz_score(data[valid_mask], labels[valid_mask])
    else:
        sil, db, ch = None, None, None

    metrics = {
        'Timestamp': dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Model': name,
        'Silhouette': round(sil, 4) if sil is not None else "N/A",
        'Davies-Bouldin': round(db, 4) if db is not None else "N/A",
        'Calinski-Harabasz': round(ch, 4) if ch is not None else "N/A"
    }

    df_metrics = pd.DataFrame([metrics])

    # Chế độ Append: Nếu chưa có file thì tạo mới, nếu có rồi thì ghi nối vào cuối
    if not os.path.exists(log_file):
        df_metrics.to_csv(log_file, index=False, mode='w')
    else:
        df_metrics.to_csv(log_file, index=False, mode='a', header=False)

    return metrics, labels