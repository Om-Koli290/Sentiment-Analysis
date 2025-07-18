import requests
import pandas as pd
import yfinance as yf
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

API_KEY = '4a79956fedaa4dc49bee301633487986'
QUERY = 'Apple'
FROM_DATE = '2025-06-20'
TO_DATE = '2025-07-16'
PAGE_SIZE = 100
MAX_PAGES = 5

def fetch_news(query, from_date, to_date, api_key, pages=MAX_PAGES):
    all_articles = []

    for page in range(1, pages + 1):
        url = (
            f'https://newsapi.org/v2/everything?'
            f'q={query}&'
            f'from={from_date}&to={to_date}&'
            f'sortBy=popularity&'
            f'language=en&'
            f'pageSize={PAGE_SIZE}&page={page}&'
            f'apiKey={api_key}'
        )

        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error fetching page {page}: {response.status_code}")
            break

        data = response.json()
        articles = data.get('articles', [])

        for article in articles:
            all_articles.append({
                'date': article['publishedAt'][:10],
                'headline': article['title'],
                'source': article['source']['name'],
                'url': article['url']
            })

        if len(articles) < PAGE_SIZE:
            break

    return pd.DataFrame(all_articles)

def fetch_price_data(ticker, start_date, end_date):
    df_price = yf.download(ticker, start=start_date, end=end_date, interval="1d", progress=False)
    df_price.reset_index(inplace=True)
    df_price['date'] = df_price['Date'].dt.strftime('%Y-%m-%d')
    # Keep only useful columns
    df_price = df_price[['date', 'Close']]
    df_price.rename(columns={'Close': 'close'}, inplace=True)
    return df_price

def save_to_csv(df, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"✅ Saved to '{filename}'")

if __name__ == "__main__":
    # Fetch news and save
    news_df = fetch_news(QUERY, FROM_DATE, TO_DATE, API_KEY)
    save_to_csv(news_df, "Output/apple_headlines.csv")

    # Fetch price data and save
    price_df = fetch_price_data("AAPL", FROM_DATE, TO_DATE)
    save_to_csv(price_df, "Output/aapl_price.csv")
