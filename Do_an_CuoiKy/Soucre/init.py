import os

# Định nghĩa đường dẫn thư mục gốc OR2/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Tự động tạo thư mục data/ nếu chưa tồn tại
os.makedirs(DATA_DIR, exist_ok=True)

# Đường dẫn file dữ liệu trong data/ và log ở thư mục gốc OR2/
PATH_DATA_CLEAN = os.path.join(DATA_DIR, "data_clean.csv")
PATH_RFM_DATA = os.path.join(DATA_DIR, "rfm_data.csv")
PATH_RFM_TRAIN = os.path.join(DATA_DIR, "rfm_train.csv")
PATH_RFM_VAL = os.path.join(DATA_DIR, "rfm_val.csv")

# File nhật ký thực nghiệm CSV nằm ngay tại thư mục gốc OR2/
PATH_EXPERIMENT_LOG = os.path.join(BASE_DIR, "Experiment_Log_Comparison.csv")