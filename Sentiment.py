import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm
import nltk

# Download VADER lexicon if not already done
nltk.download('vader_lexicon')


def compute_daily_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily average sentiment scores from news headlines.

    Parameters:
    - df: DataFrame with columns ['date', 'headline']

    Returns:
    - DataFrame with columns ['date', 'daily_sentiment_score']
    """
    sid = SentimentIntensityAnalyzer()
    tqdm.pandas()

    # Compute compound sentiment score for each headline
    df['sentiment_score'] = df['headline'].progress_apply(lambda x: sid.polarity_scores(x)['compound'])

    # Convert date column to datetime.date (drop time part)
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Group by date and compute average compound score
    daily_sentiment = df.groupby('date')['sentiment_score'].mean().reset_index()
    daily_sentiment.rename(columns={'sentiment_score': 'daily_sentiment_score'}, inplace=True)

    return daily_sentiment
