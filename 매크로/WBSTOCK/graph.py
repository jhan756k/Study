def get_stock(code):
    import FinanceDataReader as fdr
    from insider import StockInsider
    import os

    df = fdr.DataReader("code")

    df["day"] = df.index

    df.columns = ['open', 'close', 'high', 'low', 'volumn', "price_change", 'day']

    df["ma10"] = df["close"].rolling(10).mean()

    df["ma20"] = df["close"].rolling(20).mean()

    df["v_ma5"] = df["volumn"].rolling(5).mean()

    df["v_ma10"] = df["volumn"].rolling(10).mean()

    df["v_ma20"] = df["volumn"].rolling(20).mean()

    df["percent_change"] = df["close"].pct_change()

    si = StockInsider.from_external_csv_data(fpath="316140.csv", code=code)

    return si


si = get_stock("316140")

si.plot()
