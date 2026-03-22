# Sturdy Potato 

A moving average crossover trading strategy for Apple (AAPL) stocks.

## Overview
This project analyzes AAPL daily stock price data for 2024 using the `yfinance` library.
It generates buy/sell signals based on Simple Moving Averages (SMA).

## Strategy Logic
- **SMA20** → 20-day Simple Moving Average (short-term)
- **SMA50** → 50-day Simple Moving Average (long-term)

| Signal | Condition      | Meaning                              |
|--------|----------------|--------------------------------------|
| BUY    | SMA20 > SMA50  | Short-term trend is above long-term  |
| SELL   | SMA20 < SMA50  | Short-term trend is below long-term  |

This follows the classic **Golden Cross / Death Cross** strategy.

## Requirements
- Python 3.x
- yfinance
- pandas
- matplotlib

## How to Run
```bash
pip install yfinance pandas matplotlib
python sturdy_potato.py
```
