# to fetch basic stock data from yfinance ohcl

import yfinance as yf

def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

if __name__ == "__main__":
    ticker = "AAPL"
    data = fetch_data(ticker, "2023-01-01", "2023-12-31")
    print(data.columns)