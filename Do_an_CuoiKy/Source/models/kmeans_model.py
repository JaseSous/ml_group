from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from Source.logger import evaluate_and_log
from Source.init import PATH_EXPERIMENT_LOG

class TunedKMeans:
    def __init__(self, random_state=42):
        self.random_state = random_state
        self.best_k = 3
        self.model = None

    def tune(self, data, k_range=range(2, 8)):
        sse, sil_scores = {}, {}
        best_sil = -1
        for k in k_range:
            km = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
            labels = km.fit_predict(data)
            sil = silhouette_score(data, labels)
            sse[k] = km.inertia_
            sil_scores[k] = sil
            if sil > best_sil:
                best_sil = sil
                self.best_k = k
        return self.best_k, sse, sil_scores

    def run(self, data, k=None, log_file=PATH_EXPERIMENT_LOG):
        n_clusters = k if k else self.best_k
        name = f"Mô hình 1: K-Means (Tuned K={n_clusters})"
        self.model = KMeans(n_clusters=n_clusters, random_state=self.random_state, n_init=10)
        metrics, labels = evaluate_and_log(name, self.model, data, log_file, is_fitted=False)
        return metrics, labels, self.model