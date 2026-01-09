"""
Read CSV file and perform basic inspection
Use case: Raw data ingestion
"""

import pandas as pd

def read_csv_file(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    print("Data Preview:")
    print(df.head())
    return df

if __name__ == "__main__":
    # Example usage
    df = read_csv_file("sample_data.csv")
