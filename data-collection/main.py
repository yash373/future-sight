# Importing Dependencies
import yfinance as yf
import pandas as pd
import numpy as np

# Pulls Stock Data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return data