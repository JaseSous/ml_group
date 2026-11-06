from sklearn.cluster import AgglomerativeClustering
from Source.logger import evaluate_and_log
from Source.init import PATH_EXPERIMENT_LOG

class HierarchicalModel:
    def __init__(self, n_clusters=4, linkage='ward'):
        self.name = f"Mô hình 2: Hierarchical (K={n_clusters}, linkage='{linkage}')"
        self.model = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)

    def run(self, data, log_file=PATH_EXPERIMENT_LOG):
        metrics, labels = evaluate_and_log(self.name, self.model, data, log_file, is_fitted=False)
        return metrics, labels, self.model