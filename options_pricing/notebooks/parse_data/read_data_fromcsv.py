
import yfinance as yf
import pandas as pd

ticker = "MSFT"
def read_options_data(symbol, date):
    calls_df = pd.read_csv(f"data/{symbol}_calls_{date}.csv")
    puts_df = pd.read_csv(f"data/{symbol}_puts_{date}.csv")
    
    return calls_df, puts_df


def avai_options(symbol):
    stock = yf.Ticker(symbol)
    options_dates = stock.options  # Get available expiration dates
    return options_dates

list_expiration = avai_options(ticker)

# Example usage
calls_df, puts_df = read_options_data(ticker, list_expiration[0])

# Print the first few rows of the data
print("Calls DataFrame:")
print(calls_df.head())

print("\nPuts DataFrame:")
print(puts_df.head())
