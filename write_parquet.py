"""
Write processed data to Parquet format
Use case: Optimized storage for analytics
"""

import pandas as pd

def write_parquet(df: pd.DataFrame, output_path: str) -> None:
    df.to_parquet(output_path, index=False)
    print(f"Data written to {output_path}")

if __name__ == "__main__":
    data = {
        "user_id": [1, 2, 3],
        "country": ["India", "US", "UK"]
    }
    df = pd.DataFrame(data)
    write_parquet(df, "users.parquet")
