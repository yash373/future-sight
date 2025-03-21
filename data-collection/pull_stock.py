import yfinance as yf


# Pulls Stock Data
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    stock_history = stock.history(period="1d")

    # This will be the row that we will eventually end up adding to the main csv file
    row = []
    
    # Appending stock history related values to row
    row.append(stock_history["Close"][0]) # Adding Closing Price
    row.append(stock_history["Open"][0]) # Adding Openeing Price
    row.append(stock_history["High"][0]) # Adding High
    row.append(stock_history["Low"][0]) # Adding Low
    row.append(stock_history["Volume"][0]) # Adding Volume

    # Keys for the info dictionary object in Ticker that will be sued for extracting numerical data
    info_keys = ["forwardPE", "fullTimeEmployees", "auditRisk", "boardRisk", "compensationRisk","shareHolderRightsRisk", "overallRisk", "governanceEpochDate", "compensationAsOfEpochDate","maxAge", "priceHint", "previousClose", "dayLow", "dayHigh", "regularMarketPreviousClose","regularMarketOpen", "regularMarketDayLow", "regularMarketDayHigh", "dividendRate","dividendYield", "exDividendDate", "payoutRatio", "fiveYearAvgDividendYield", "beta","trailingPE", "volume", "regularMarketVolume", "averageVolume", "averageVolume10days","averageDailyVolume10Day", "marketCap", "fiftyTwoWeekLow", "fiftyTwoWeekHigh","priceToSalesTrailing12Months", "fiftyDayAverage", "twoHundredDayAverage","trailingAnnualDividendRate", "trailingAnnualDividendYield", "enterpriseValue","profitMargins", "floatShares", "sharesOutstanding", "heldPercentInsiders","heldPercentInstitutions", "impliedSharesOutstanding", "bookValue", "priceToBook","lastFiscalYearEnd", "nextFiscalYearEnd", "mostRecentQuarter", "earningsQuarterlyGrowth","netIncomeToCommon", "trailingEps", "forwardEps", "lastSplitDate","enterpriseToRevenue", "enterpriseToEbitda", "fiftyTwoWeekChange", "SandP52WeekChange","lastDividendValue", "lastDividendDate", "currentPrice", "targetHighPrice", "targetLowPrice","targetMeanPrice", "targetMedianPrice", "recommendationMean", "numberOfAnalystOpinions","totalCash", "totalCashPerShare", "ebitda", "totalDebt", "totalRevenue", "debtToEquity","revenuePerShare", "grossProfits", "earningsGrowth", "revenueGrowth", "grossMargins","ebitdaMargins", "operatingMargins", "firstTradeDateMilliseconds", "regularMarketChange","averageDailyVolume3Month", "fiftyTwoWeekLowChange", "fiftyTwoWeekLowChangePercent","fiftyTwoWeekHighChange", "fiftyTwoWeekHighChangePercent", "fiftyTwoWeekChangePercent","earningsTimestamp", "earningsTimestampStart", "earningsTimestampEnd", "epsTrailingTwelveMonths","epsForward", "epsCurrentYear", "priceEpsCurrentYear", "fiftyDayAverageChange","fiftyDayAverageChangePercent", "twoHundredDayAverageChange", "twoHundredDayAverageChangePercent","sourceInterval", "exchangeDataDelayedBy", "regularMarketTime", "gmtOffSetMilliseconds","regularMarketChangePercent", "regularMarketPrice"]

    # Adding data thorugh keys into the row
    for key in info_keys:
        row.append(stock.info.get(key))

    return row

print(get_stock_data("RELIANCE.NS"))
