from sklearn.cluster import KMeans
from Source.logger import evaluate_and_log
from Source.init import PATH_EXPERIMENT_LOG

class BaselineKMeans:
    def __init__(self, n_clusters=3, random_state=42):
        self.name = f"Baseline: K-Means (K={n_clusters}, Untuned)"
        self.model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)

    def run(self, data, log_file=PATH_EXPERIMENT_LOG):
        metrics, labels = evaluate_and_log(self.name, self.model, data, log_file, is_fitted=False)
        return metrics, labels, self.model