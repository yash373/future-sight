import yfinance as yf
import numpy as np
from web_search.stock_sentiment_assesment import get_sentiment


# Pulls Public Sentiment
def get_public_sentiment(ticker):
    stock_name = ticker[:-3]

    company_performance = get_sentiment(
        stock_name=stock_name,
        search_question=f"How does the {stock_name}'s latest earnings report impact its stock sentiment?",
    )

    return np.float64(company_performance)


# Pulls Stock Data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    stock_history = stock.history(period="1d")

    # This will be the row that we will eventually end up adding to the main csv file
    row = np.ndarray(111)

    # Appending stock history related values to row
    # row.append(stock_history["Close"][0]) # Adding Closing Price
    row[0] = stock_history["Close"].iloc[0]  # Adding Closing Price
    row[1] = stock_history["Open"].iloc[0]  # Adding Openeing Price
    row[2] = stock_history["High"].iloc[0]  # Adding High
    row[3] = stock_history["Low"].iloc[0]  # Adding Low
    row[4] = stock_history["Volume"].iloc[0]  # Adding Volume

    # Keys for the info dictionary object in Ticker that will be sued for extracting numerical data
    info_keys = [
        "forwardPE",
        "fullTimeEmployees",
        "auditRisk",
        "boardRisk",
        "compensationRisk",
        "shareHolderRightsRisk",
        "overallRisk",
        "governanceEpochDate",
        "compensationAsOfEpochDate",
        "maxAge",
        "priceHint",
        "previousClose",
        "dayLow",
        "dayHigh",
        "regularMarketPreviousClose",
        "regularMarketOpen",
        "regularMarketDayLow",
        "regularMarketDayHigh",
        "dividendRate",
        "dividendYield",
        "exDividendDate",
        "payoutRatio",
        "fiveYearAvgDividendYield",
        "beta",
        "trailingPE",
        "volume",
        "regularMarketVolume",
        "averageVolume",
        "averageVolume10days",
        "averageDailyVolume10Day",
        "marketCap",
        "fiftyTwoWeekLow",
        "fiftyTwoWeekHigh",
        "priceToSalesTrailing12Months",
        "fiftyDayAverage",
        "twoHundredDayAverage",
        "trailingAnnualDividendRate",
        "trailingAnnualDividendYield",
        "enterpriseValue",
        "profitMargins",
        "floatShares",
        "sharesOutstanding",
        "heldPercentInsiders",
        "heldPercentInstitutions",
        "impliedSharesOutstanding",
        "bookValue",
        "priceToBook",
        "lastFiscalYearEnd",
        "nextFiscalYearEnd",
        "mostRecentQuarter",
        "earningsQuarterlyGrowth",
        "netIncomeToCommon",
        "trailingEps",
        "forwardEps",
        "lastSplitDate",
        "enterpriseToRevenue",
        "enterpriseToEbitda",
        "SandP52WeekChange",
        "lastDividendValue",
        "lastDividendDate",
        "currentPrice",
        "targetHighPrice",
        "targetLowPrice",
        "targetMeanPrice",
        "targetMedianPrice",
        "recommendationMean",
        "numberOfAnalystOpinions",
        "totalCash",
        "totalCashPerShare",
        "ebitda",
        "totalDebt",
        "totalRevenue",
        "debtToEquity",
        "revenuePerShare",
        "grossProfits",
        "earningsGrowth",
        "revenueGrowth",
        "grossMargins",
        "ebitdaMargins",
        "operatingMargins",
        "firstTradeDateMilliseconds",
        "regularMarketChange",
        "averageDailyVolume3Month",
        "fiftyTwoWeekLowChange",
        "fiftyTwoWeekLowChangePercent",
        "fiftyTwoWeekHighChange",
        "fiftyTwoWeekHighChangePercent",
        "fiftyTwoWeekChangePercent",
        "earningsTimestamp",
        "earningsTimestampStart",
        "earningsTimestampEnd",
        "epsTrailingTwelveMonths",
        "epsForward",
        "epsCurrentYear",
        "priceEpsCurrentYear",
        "fiftyDayAverageChange",
        "fiftyDayAverageChangePercent",
        "twoHundredDayAverageChange",
        "twoHundredDayAverageChangePercent",
        "sourceInterval",
        "exchangeDataDelayedBy",
        "regularMarketTime",
        "gmtOffSetMilliseconds",
        "regularMarketChangePercent",
        "regularMarketPrice",
    ]

    # Adding data thorugh keys into the row
    for index, key in enumerate(info_keys):
        # row.append(np.float64(stock.info.get(key)))
        row[5 + index] = np.float64(stock.info.get(key))

    row[110] = get_public_sentiment(ticker)

    return row


print(get_stock_data("RELIANCE.NS"))
