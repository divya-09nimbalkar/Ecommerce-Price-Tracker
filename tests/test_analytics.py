import pandas as pd
from src.analytics import run_analysis

def test_run_analysis():
    df = pd.DataFrame({
        "date": ["2024-01-01","2024-01-02"],
        "name": ["Laptop","Phone"],
        "price": [850, 640],
        "volume": [15, 30]
    })
    results = run_analysis(df)
    assert "rows" in results
    assert results["rows"] == 2
    assert results["avg_price"] == (850+640)/2
