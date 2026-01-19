import pandas as pd

def clean_ai_training_data(file_path):
    """
    Quy trình làm sạch dữ liệu tự động cho dự án AI Labs.
    """
    df = pd.read_csv(file_path)
    # Loại bỏ dữ liệu rỗng và trùng lặp
    df = df.dropna().drop_duplicates()
    # Chuẩn hóa văn bản cho AI Training
    df['content'] = df['content'].str.lower().str.strip()
    return df

print("Data Cleaner Module is ready for Mercor project.")
