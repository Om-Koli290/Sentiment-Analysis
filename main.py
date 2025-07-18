import pandas as pd
import matplotlib.pyplot as plt
from Signals import generate_signals

# Load combined price + sentiment data
df = pd.read_csv("Output/combined_data.csv", parse_dates=["date"])
df = df.sort_values("date")

# Generate signals
df = generate_signals(df)

# Plot price chart
plt.figure(figsize=(14, 6))
plt.plot(df["date"], df["close"], label="Price", color="black", linewidth=1)

# Signal colors and marker types
signal_styles = {
    "Strong Buy": ("green", "^"),
    "Buy": ("lightgreen", "^"),
    "Hold": ("gray", "o"),
    "Sell": ("lightcoral", "v"),
    "Strong Sell": ("red", "v")
}

# Overlay signal markers on the price line
for signal_type, (color, marker) in signal_styles.items():
    signal_df = df[df["signal"] == signal_type]
    plt.scatter(signal_df["date"], signal_df["close"], label=signal_type, color=color, marker=marker, s=60, alpha=0.9)

# Final plot formatting
plt.title("Price Chart with Sentiment-Based Trading Signals")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
