import yfinance as yf

# Pulls Stock Data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    # Closing Price
    closing_price = stock.history(period="1d").Close
    # Opening Price
    opening_price = stock.history(period="1d").Open
    # High Price
    high_price = stock.history(period="1d").High
    # Low Price
    low_price = stock.history(period="1d").Low
    # Volume
    volume = stock.history(period="1d").Volume

    return closing_price, opening_price, high_price, low_price, volume

stock = yf.Ticker("RELIANCE.NS")
methods = dir(stock)
for i in methods:
    print(i)