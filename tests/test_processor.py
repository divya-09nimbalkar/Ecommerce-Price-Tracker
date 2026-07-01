import pandas as pd
from src.processor import clean_data

def test_clean_data():
    raw = pd.DataFrame({
        "date": ["2024-01-01", None],
        "name": ["Laptop", "Phone"],
        "price": [850, None],
        "volume": [15, 30]
    })
    cleaned = clean_data(raw)
    # Ensure no NaN values remain
    assert cleaned.isnull().sum().sum() == 0
    # Ensure date is converted to datetime
    assert pd.api.types.is_datetime64_any_dtype(cleaned["date"])
