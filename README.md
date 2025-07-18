# 📰📈 Sentiment-Based Trading Signal Generator

This project uses **financial news sentiment** and **stock price data** to generate simple trading signals and visualize them on a price chart. It combines real-time news scraping, NLP sentiment scoring, and data merging techniques.

---

## 🧠 What It Does

- Pulls news articles related to a given stock (via [NewsAPI](https://newsapi.org))
- Calculates daily sentiment scores using **NLTK's VADER**
- Downloads historical price data using `yfinance`
- Merges both into a single dataset
- Generates trading signals based on sentiment
- Visualizes price chart + buy/sell markers

---

## ⚙️ Setup Instructions

### 🔧 Dependencies

Install required packages using:

pip install pandas matplotlib yfinance nltk requests

Make sure to download VADER's lexicon:

import nltk
nltk.download('vader_lexicon')

🔑 API Key
Get a free API key from newsapi.org, and set the API_KEY variable in fetch_data.py:
API_KEY = 'your_api_key_here'

▶️ How to Run

1. Fetch News + Price Data

python fetch_data.py

This will save:

Output/apple_headlines.csv

Output/aapl_price.csv

2. Process Sentiment + Merge

python process_data.py
This will save:

Output/combined_data.csv

3. Generate + Plot Signals

python plot_signals.py
A price chart with trading signals (Buy, Sell, Hold) will be displayed.

🧪 Signal Logic
Signals are generated based on the daily sentiment score:

Sentiment Score	Signal
> +0.5	Strong Buy
0 to +0.5	Buy
~0	Hold
0 to -0.5	Sell
< -0.5	Strong Sell

You can edit this logic in Signals.py.

📌 Notes
This project uses daily granularity. Intraday sentiment would require more advanced NLP and data feeds.


📈 Example Output
A plot with Apple’s stock price and overlaid signals like “Strong Buy” and “Sell” based on daily news sentiment.

