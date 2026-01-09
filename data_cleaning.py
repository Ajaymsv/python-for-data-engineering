"""
Basic data cleaning operations
Use case: Preparing data before transformations
"""

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df = df.drop_duplicates()
    return df

if __name__ == "__main__":
    data = {
        "name": ["Ajay", "Rahul", None, "Ajay"],
        "age": [25, 30, 28, 25]
    }
    df = pd.DataFrame(data)
    clean_df = clean_data(df)
    print(clean_df)
