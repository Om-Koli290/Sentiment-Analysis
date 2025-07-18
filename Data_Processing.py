import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def load_news_data(path="Output/apple_headlines.csv"):
    return pd.read_csv(path)

def load_price_data(path="Output/aapl_price.csv"):
    return pd.read_csv(path)

def apply_sentiment(news_df):
    sia = SentimentIntensityAnalyzer()
    news_df["sentiment"] = news_df["headline"].apply(lambda x: sia.polarity_scores(x)["compound"])
    return news_df

def calculate_daily_sentiment(news_df):
    daily_sentiment = news_df.groupby("date")["sentiment"].mean().reset_index()
    daily_sentiment.rename(columns={"sentiment": "sentiment_score"}, inplace=True)
    return daily_sentiment

def merge_data(price_df, sentiment_df):
    merged = pd.merge(price_df, sentiment_df, on="date", how="left")
    merged['sentiment_score'].fillna(0, inplace=True)  # Fill missing sentiment with 0 (neutral)
    return merged

if __name__ == "__main__":
    news_df = load_news_data()
    price_df = load_price_data()

    news_df = apply_sentiment(news_df)
    daily_sentiment_df = calculate_daily_sentiment(news_df)
    combined_df = merge_data(price_df, daily_sentiment_df)

    combined_df.to_csv("Output/combined_data.csv", index=False)
    print("✅ Combined price and sentiment data saved to 'Output/combined_data.csv'")
