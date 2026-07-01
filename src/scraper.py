import pandas as pd

def scrape_mock_data() -> pd.DataFrame:
    """Return mock dataset instead of live scraping."""
    data = {
        "date": ["2024-01-01","2024-01-02","2024-01-03"],
        "name": ["Laptop","Smartphone","Headphones"],
        "price": [850, 640, 120],
        "volume": [15, 30, 50]
    }
    return pd.DataFrame(data)
