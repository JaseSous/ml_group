from sklearn.cluster import DBSCAN
from Source.logger import evaluate_and_log
from Source.init import PATH_EXPERIMENT_LOG

class DBSCANModel:
    def __init__(self, eps=0.6, min_samples=10):
        self.name = f"Mô hình 3: DBSCAN (eps={eps}, min_samples={min_samples})"
        self.model = DBSCAN(eps=eps, min_samples=min_samples)

    def run(self, data, log_file=PATH_EXPERIMENT_LOG):
        metrics, labels = evaluate_and_log(self.name, self.model, data, log_file, is_fitted=False)
        return metrics, labels, self.model