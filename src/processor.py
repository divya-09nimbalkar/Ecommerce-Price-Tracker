import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean scraped data."""
    df = df.dropna()
    df["price"] = df["price"].astype(float)
    df["volume"] = df["volume"].astype(int)
    df["date"] = pd.to_datetime(df["date"])
    return df
