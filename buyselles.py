import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download stock data
data = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

# Calculate moving averages
data["SMA20"] = data["Close"].rolling(window=20).mean()
data["SMA50"] = data["Close"].rolling(window=50).mean()

# Create signal column
data["Signal"] = 0
data.loc[data["SMA20"] > data["SMA50"], "Signal"] = 1
data.loc[data["SMA20"] < data["SMA50"], "Signal"] = -1

print(data.tail())

# Plot chart
plt.figure(figsize=(10,5))
plt.plot(data["Close"], label="Price")
plt.plot(data["SMA20"], label="20 SMA")
plt.plot(data["SMA50"], label="50 SMA")

plt.title("Trading Signals")
plt.legend()
plt.show()