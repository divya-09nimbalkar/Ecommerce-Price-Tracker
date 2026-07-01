import pandas as pd
from src.scraper import scrape_mock_data

def test_scrape_mock_data():
    df = scrape_mock_data()
    # Basic checks
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "price" in df.columns
    assert "name" in df.columns
