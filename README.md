
---

#  Ecommerce Price Tracker

A robust Python-based data pipeline designed to scrape product prices from e-commerce websites, process and clean the raw data, perform analysis, and visualize pricing trends over time.

---

##  Features

* **Web Scraping:** Extract live product pricing data efficiently using `BeautifulSoup`.
* **Data Pipeline:** Separate stages for raw data collection and cleaned, structured data processing.
* **Data Analytics:** Analyze price fluctuations, historical trends, and key statistical insights.
* **Data Visualization:** Generate charts and plots to track pricing changes easily.
* **Automated Testing:** Unit tests implemented with `pytest` to ensure pipeline stability.

---

##  Project Structure

```text
ECOMMERCE_PRICE_TRACKER/
├── data/
│   ├── processed/          # Cleaned, ready-to-analyze datasets
│   └── raw/                # Unmodified data scraped directly from sites
│       └── sample.csv
├── docs/                   # Project documentation and output visualizations
│   ├── output1.png
│   └── output2.png
├── models/                 # Saved models or statistical configurations
├── notebooks/              # Jupyter Notebooks for exploratory data analysis
│   └── exploration.ipynb
├── src/                    # Main source code of the application
│   ├── __init__.py
│   ├── analytics.py        # Trend analysis and pricing metrics
│   ├── main.py             # Pipeline orchestrator (execution entry point)
│   ├── processor.py        # Data cleaning and transformation logic
│   ├── scraper.py          # Web scraping modules
│   ├── utils.py            # Shared utility helper functions
│   └── visualization.py    # Chart and graph generation script
├── tests/                  # Unit tests matching the source modules
│   ├── test_analytics.py
│   ├── test_processor.py
│   └── test_scraper.py
├── .gitignore              # Files and folders ignored by Git
└── README.md               # Project documentation

```

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-price-tracker.git
cd ecommerce-price-tracker

```

### 2. Set Up a Virtual Environment

```bash
# Create the environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (macOS/Linux)
source .venv/bin/activate

```

### 3. Install Dependencies

*(Make sure to create a `requirements.txt` file if you haven't already. It typically includes: `beautifulsoup4`, `requests`, `pandas`, `matplotlib`, `seaborn`, and `pytest`.)*

```bash
pip install -r requirements.txt

```

---

##  Usage

### Run the Pipeline

To execute the complete web scraping, processing, and analysis pipeline, run the main orchestration script:

```bash
python src/main.py

```

### Exploratory Analysis

You can explore the dataset interactively using the Jupyter Notebook located in the `notebooks/` directory:

```bash
jupyter notebook notebooks/exploration-checkpoint.ipynb

```

---

##  Running Tests

This project uses `pytest` for unit testing. To run the test suite and ensure all components are functioning as expected, execute:

```bash
pytest

```
