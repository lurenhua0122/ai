# filename: ytd_gain.py
import yfinance as yf
import pandas as pd

# Define the ticker symbols for the 10 largest technology companies
ticker_symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'FB', 'TSM', 'NVDA', 'PYPL', 'INTC']

# Fetch the historical data for the ticker symbols
data = yf.download(ticker_symbols, start='2021-01-01', end='2021-12-31')

# Calculate the YTD gain for each ticker symbol
ytd_gains = {}
for symbol in ticker_symbols:
    ticker_data = data[symbol]
    ytd_gain = (ticker_data['Close'][-1] - ticker_data['Close'][0]) / ticker_data['Close'][0] * 100
    ytd_gains[symbol] = ytd_gain

# Sort the YTD gains in descending order
sorted_ytd_gains = sorted(ytd_gains.items(), key=lambda x: x[1], reverse=True)

# Print the YTD gains for the 10 largest technology companies
for symbol, ytd_gain in sorted_ytd_gains:
    print(f"{symbol}: {ytd_gain:.2f}%")