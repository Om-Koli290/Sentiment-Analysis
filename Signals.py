import pandas as pd


def generate_signals(daily_sentiment_df, strong_threshold=0.3, weak_threshold=0.1):
    """
    Generate trading signals based on daily sentiment scores.

    Parameters:
    - daily_sentiment_df: DataFrame with ['date', 'daily_sentiment_score']
    - strong_threshold: float, threshold for strong buy/sell signal
    - weak_threshold: float, threshold for weak buy/sell signal

    Returns:
    - DataFrame with columns ['date', 'daily_sentiment_score', 'signal']
      where signal is one of:
      'Strong Buy', 'Weak Buy', 'Hold', 'Weak Sell', 'Strong Sell'
    """

    def classify(score):
        if score >= strong_threshold:
            return 'Strong Buy'
        elif weak_threshold <= score < strong_threshold:
            return 'Weak Buy'
        elif -weak_threshold < score < weak_threshold:
            return 'Hold'
        elif -strong_threshold < score <= -weak_threshold:
            return 'Weak Sell'
        elif score <= -strong_threshold:
            return 'Strong Sell'

    df = daily_sentiment_df.copy()
    df['signal'] = df['sentiment_score'].apply(classify)
    return df
