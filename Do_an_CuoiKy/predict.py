"""
Script dự đoán phân khúc khách hàng mới (Customer Segmentation Inference)
Sử dụng mô hình tối ưu K-Means (K=4) và StandardScaler đã huấn luyện.

Cách sử dụng:
1. Dự đoán cho 1 khách hàng:
   python predict.py --recency 15 --frequency 8 --monetary 2500

2. Dự đoán hàng loạt từ file CSV:
   python predict.py --file data/rfm_test.csv --output data/predictions_test.csv
"""

import os
import sys
import json
import argparse
import joblib
import pandas as pd
import numpy as np

# Đảm bảo in tiếng Việt và emoji đúng chuẩn trên Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Đường dẫn mặc định
MODEL_PATH = os.path.join("saved_models", "kmeans_k4_model.joblib")
SCALER_PATH = os.path.join("saved_models", "scaler.joblib")
MAPPING_PATH = os.path.join("saved_models", "cluster_mapping.json")

def load_artifacts():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise FileNotFoundError("Không tìm thấy mô hình hoặc scaler trong thư mục 'saved_models/'!")
    
    scaler = joblib.load(SCALER_PATH)
    model = joblib.load(MODEL_PATH)
    
    with open(MAPPING_PATH, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
        
    return scaler, model, mapping

def predict_single(recency, frequency, monetary):
    scaler, model, mapping = load_artifacts()
    
    input_df = pd.DataFrame([[recency, frequency, monetary]], columns=['Recency', 'Frequency', 'Monetary'])
    input_scaled = scaler.transform(input_df)
    
    cluster = int(model.predict(input_scaled)[0])
    segment_info = mapping.get(str(cluster), {'name': f'Cụm {cluster}', 'description': 'Không có mô tả'})
    
    print("\n" + "="*60)
    print("🎯 KẾT QUẢ PHÂN KHÚC KHÁCH HÀNG")
    print("="*60)
    print(f"📌 Thông số RFM đầu vào:")
    print(f"   • Recency (Độ gần đây)   : {recency} ngày")
    print(f"   • Frequency (Tần suất)   : {frequency} hóa đơn")
    print(f"   • Monetary (Tổng chi tiêu): {monetary:,.2f} £")
    print("-" * 60)
    print(f"🏆 Cụm dự đoán : Cụm {cluster}")
    print(f"🏷️  Phân khúc   : {segment_info['name']}")
    print(f"💡 Đặc điểm    : {segment_info['description']}")
    print("="*60 + "\n")
    return cluster, segment_info['name']

def predict_batch(file_path, output_path=None):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Không tìm thấy file dữ liệu tại '{file_path}'!")
        
    scaler, model, mapping = load_artifacts()
    df = pd.read_csv(file_path)
    
    required_cols = ['Recency', 'Frequency', 'Monetary']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"File thiếu cột bắt buộc '{col}'!")
            
    X_scaled = scaler.transform(df[required_cols])
    clusters = model.predict(X_scaled)
    
    df['Predicted_Cluster'] = clusters
    df['Segment_Name'] = df['Predicted_Cluster'].astype(str).map(lambda c: mapping.get(c, {}).get('name', f'Cluster {c}'))
    
    if output_path is None:
        output_path = file_path.replace(".csv", "_predicted.csv")
        
    df.to_csv(output_path, index=False)
    print(f"\n✅ Đã hoàn thành dự đoán cho {len(df)} khách hàng!")
    print(f"💾 File kết quả đã lưu tại: {output_path}")
    print("\nThống kê số lượng khách hàng theo từng phân khúc:")
    print(df['Segment_Name'].value_counts())
    return df

def main():
    parser = argparse.ArgumentParser(description="Dự đoán phân khúc khách hàng dựa trên mô hình RFM K-Means")
    parser.add_argument("--recency", type=float, help="Số ngày từ lần mua gần nhất")
    parser.add_argument("--frequency", type=float, help="Tổng số đơn hàng đã mua")
    parser.add_argument("--monetary", type=float, help="Tổng số tiền đã chi tiêu (£)")
    parser.add_argument("--file", type=str, help="Đường dẫn file CSV chứa cột Recency, Frequency, Monetary")
    parser.add_argument("--output", type=str, help="Đường dẫn file CSV lưu kết quả (tùy chọn)")
    
    args = parser.parse_args()
    
    if args.file:
        predict_batch(args.file, args.output)
    elif args.recency is not None and args.frequency is not None and args.monetary is not None:
        predict_single(args.recency, args.frequency, args.monetary)
    else:
        print("Vui lòng cung cấp tham số cho 1 khách hàng (--recency, --frequency, --monetary) hoặc file CSV (--file)!")
        print("Ví dụ: python predict.py --recency 15 --frequency 8 --monetary 2500")

if __name__ == "__main__":
    main()
