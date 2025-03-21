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
    # P/E Ratio
    pe_ratio = stock.info["forwardPE"]
    
    # fullTimeEmployees
    fullTimeEmployees = ticker.info.get("fullTimeEmployees")

    # auditRisk
    auditRisk = ticker.info.get("auditRisk")

    # boardRisk
    boardRisk = ticker.info.get("boardRisk")

    # compensationRisk
    compensationRisk = ticker.info.get("compensationRisk")

    # shareHolderRightsRisk
    shareHolderRightsRisk = ticker.info.get("shareHolderRightsRisk")

    # overallRisk
    overallRisk = ticker.info.get("overallRisk")

    # governanceEpochDate
    governanceEpochDate = ticker.info.get("governanceEpochDate")

    # compensationAsOfEpochDate
    compensationAsOfEpochDate = ticker.info.get("compensationAsOfEpochDate")

    # maxAge
    maxAge = ticker.info.get("maxAge")

    # priceHint
    priceHint = ticker.info.get("priceHint")

    # previousClose
    previousClose = ticker.info.get("previousClose")

    # open
    open = ticker.info.get("open")

    # dayLow
    dayLow = ticker.info.get("dayLow")

    # dayHigh
    dayHigh = ticker.info.get("dayHigh")

    # regularMarketPreviousClose
    regularMarketPreviousClose = ticker.info.get("regularMarketPreviousClose")

    # regularMarketOpen
    regularMarketOpen = ticker.info.get("regularMarketOpen")

    # regularMarketDayLow
    regularMarketDayLow = ticker.info.get("regularMarketDayLow")

    # regularMarketDayHigh
    regularMarketDayHigh = ticker.info.get("regularMarketDayHigh")

    # dividendRate
    dividendRate = ticker.info.get("dividendRate")

    # dividendYield
    dividendYield = ticker.info.get("dividendYield")

    # exDividendDate
    exDividendDate = ticker.info.get("exDividendDate")

    # payoutRatio
    payoutRatio = ticker.info.get("payoutRatio")

    # fiveYearAvgDividendYield
    fiveYearAvgDividendYield = ticker.info.get("fiveYearAvgDividendYield")

    # beta
    beta = ticker.info.get("beta")

    # trailingPE
    trailingPE = ticker.info.get("trailingPE")

    # forwardPE
    forwardPE = ticker.info.get("forwardPE")

    # volume
    volume = ticker.info.get("volume")

    # regularMarketVolume
    regularMarketVolume = ticker.info.get("regularMarketVolume")

    # averageVolume
    averageVolume = ticker.info.get("averageVolume")

    # averageVolume10days
    averageVolume10days = ticker.info.get("averageVolume10days")

    # averageDailyVolume10Day
    averageDailyVolume10Day = ticker.info.get("averageDailyVolume10Day")

    # marketCap
    marketCap = ticker.info.get("marketCap")

    # fiftyTwoWeekLow
    fiftyTwoWeekLow = ticker.info.get("fiftyTwoWeekLow")

    # fiftyTwoWeekHigh
    fiftyTwoWeekHigh = ticker.info.get("fiftyTwoWeekHigh")

    # priceToSalesTrailing12Months
    priceToSalesTrailing12Months = ticker.info.get("priceToSalesTrailing12Months")

    # fiftyDayAverage
    fiftyDayAverage = ticker.info.get("fiftyDayAverage")

    # twoHundredDayAverage
    twoHundredDayAverage = ticker.info.get("twoHundredDayAverage")

    # trailingAnnualDividendRate
    trailingAnnualDividendRate = ticker.info.get("trailingAnnualDividendRate")

    # trailingAnnualDividendYield
    trailingAnnualDividendYield = ticker.info.get("trailingAnnualDividendYield")

    # enterpriseValue
    enterpriseValue = ticker.info.get("enterpriseValue")

    # profitMargins
    profitMargins = ticker.info.get("profitMargins")

    # floatShares
    floatShares = ticker.info.get("floatShares")

    # sharesOutstanding
    sharesOutstanding = ticker.info.get("sharesOutstanding")

    # heldPercentInsiders
    heldPercentInsiders = ticker.info.get("heldPercentInsiders")

    # heldPercentInstitutions
    heldPercentInstitutions = ticker.info.get("heldPercentInstitutions")

    # impliedSharesOutstanding
    impliedSharesOutstanding = ticker.info.get("impliedSharesOutstanding")

    # bookValue
    bookValue = ticker.info.get("bookValue")

    # priceToBook
    priceToBook = ticker.info.get("priceToBook")

    # lastFiscalYearEnd
    lastFiscalYearEnd = ticker.info.get("lastFiscalYearEnd")

    # nextFiscalYearEnd
    nextFiscalYearEnd = ticker.info.get("nextFiscalYearEnd")

    # mostRecentQuarter
    mostRecentQuarter = ticker.info.get("mostRecentQuarter")

    # earningsQuarterlyGrowth
    earningsQuarterlyGrowth = ticker.info.get("earningsQuarterlyGrowth")

    # netIncomeToCommon
    netIncomeToCommon = ticker.info.get("netIncomeToCommon")

    # trailingEps
    trailingEps = ticker.info.get("trailingEps")

    # forwardEps
    forwardEps = ticker.info.get("forwardEps")

    # lastSplitDate
    lastSplitDate = ticker.info.get("lastSplitDate")

    # enterpriseToRevenue
    enterpriseToRevenue = ticker.info.get("enterpriseToRevenue")

    # enterpriseToEbitda
    enterpriseToEbitda = ticker.info.get("enterpriseToEbitda")

    # fiftyTwoWeekChange
    fiftyTwoWeekChange = ticker.info.get("fiftyTwoWeekChange")

    # SandP52WeekChange
    SandP52WeekChange = ticker.info.get("SandP52WeekChange")

    # lastDividendValue
    lastDividendValue = ticker.info.get("lastDividendValue")

    # lastDividendDate
    lastDividendDate = ticker.info.get("lastDividendDate")

    # currentPrice
    currentPrice = ticker.info.get("currentPrice")

    # targetHighPrice
    targetHighPrice = ticker.info.get("targetHighPrice")

    # targetLowPrice
    targetLowPrice = ticker.info.get("targetLowPrice")

    # targetMeanPrice
    targetMeanPrice = ticker.info.get("targetMeanPrice")

    # targetMedianPrice
    targetMedianPrice = ticker.info.get("targetMedianPrice")

    # recommendationMean
    recommendationMean = ticker.info.get("recommendationMean")

    # numberOfAnalystOpinions
    numberOfAnalystOpinions = ticker.info.get("numberOfAnalystOpinions")

    # totalCash
    totalCash = ticker.info.get("totalCash")

    # totalCashPerShare
    totalCashPerShare = ticker.info.get("totalCashPerShare")

    # ebitda
    ebitda = ticker.info.get("ebitda")

    # totalDebt
    totalDebt = ticker.info.get("totalDebt")

    # totalRevenue
    totalRevenue = ticker.info.get("totalRevenue")

    # debtToEquity
    debtToEquity = ticker.info.get("debtToEquity")

    # revenuePerShare
    revenuePerShare = ticker.info.get("revenuePerShare")

    # grossProfits
    grossProfits = ticker.info.get("grossProfits")

    # earningsGrowth
    earningsGrowth = ticker.info.get("earningsGrowth")

    # revenueGrowth
    revenueGrowth = ticker.info.get("revenueGrowth")

    # grossMargins
    grossMargins = ticker.info.get("grossMargins")

    # ebitdaMargins
    ebitdaMargins = ticker.info.get("ebitdaMargins")

    # operatingMargins
    operatingMargins = ticker.info.get("operatingMargins")

    # firstTradeDateMilliseconds
    firstTradeDateMilliseconds = ticker.info.get("firstTradeDateMilliseconds")

    # regularMarketChange
    regularMarketChange = ticker.info.get("regularMarketChange")

    # averageDailyVolume3Month
    averageDailyVolume3Month = ticker.info.get("averageDailyVolume3Month")

    # fiftyTwoWeekLowChange
    fiftyTwoWeekLowChange = ticker.info.get("fiftyTwoWeekLowChange")

    # fiftyTwoWeekLowChangePercent
    fiftyTwoWeekLowChangePercent = ticker.info.get("fiftyTwoWeekLowChangePercent")

    # fiftyTwoWeekHighChange
    fiftyTwoWeekHighChange = ticker.info.get("fiftyTwoWeekHighChange")

    # fiftyTwoWeekHighChangePercent
    fiftyTwoWeekHighChangePercent = ticker.info.get("fiftyTwoWeekHighChangePercent")

    # fiftyTwoWeekChangePercent
    fiftyTwoWeekChangePercent = ticker.info.get("fiftyTwoWeekChangePercent")

    # earningsTimestamp
    earningsTimestamp = ticker.info.get("earningsTimestamp")

    # earningsTimestampStart
    earningsTimestampStart = ticker.info.get("earningsTimestampStart")

    # earningsTimestampEnd
    earningsTimestampEnd = ticker.info.get("earningsTimestampEnd")

    # epsTrailingTwelveMonths
    epsTrailingTwelveMonths = ticker.info.get("epsTrailingTwelveMonths")

    # epsForward
    epsForward = ticker.info.get("epsForward")

    # epsCurrentYear
    epsCurrentYear = ticker.info.get("epsCurrentYear")

    # priceEpsCurrentYear
    priceEpsCurrentYear = ticker.info.get("priceEpsCurrentYear")

    # fiftyDayAverageChange
    fiftyDayAverageChange = ticker.info.get("fiftyDayAverageChange")

    # fiftyDayAverageChangePercent
    fiftyDayAverageChangePercent = ticker.info.get("fiftyDayAverageChangePercent")

    # twoHundredDayAverageChange
    twoHundredDayAverageChange = ticker.info.get("twoHundredDayAverageChange")

    # twoHundredDayAverageChangePercent
    twoHundredDayAverageChangePercent = ticker.info.get(
        "twoHundredDayAverageChangePercent"
    )

    # sourceInterval
    sourceInterval = ticker.info.get("sourceInterval")

    # exchangeDataDelayedBy
    exchangeDataDelayedBy = ticker.info.get("exchangeDataDelayedBy")

    # regularMarketTime
    regularMarketTime = ticker.info.get("regularMarketTime")

    # gmtOffSetMilliseconds
    gmtOffSetMilliseconds = ticker.info.get("gmtOffSetMilliseconds")

    # regularMarketChangePercent
    regularMarketChangePercent = ticker.info.get("regularMarketChangePercent")

    # regularMarketPrice
    regularMarketPrice = ticker.info.get("regularMarketPrice")


print(get_stock_data("RELIANCE.NS"))