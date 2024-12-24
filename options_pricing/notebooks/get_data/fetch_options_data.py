# To fetch options data , put / call ticker wise 
'''
- options data from yfinance : https://algotrading101.com/learn/yfinance-guide/

'''

import yfinance as yf

ticker = "MSFT"
def fetch_options_data(symbol,date):
    stock = yf.Ticker(symbol)

    options_data = stock.option_chain(date)
    # Fetch options data for the first expiration date as an example
    calls = options_data.calls
    puts = options_data.puts
    
    # Print the first few rows of calls and puts to verify
    print("Calls:")
    print(calls.head())
    
    print("\nPuts:")
    print(puts.head())

def avai_options(symbol):
    stock = yf.Ticker(symbol)
    options_dates = stock.options  # Get available expiration dates
    return(options_dates)

list_expiration = avai_options(ticker)

#print(list_expiration)

fetch_options_data(ticker,list_expiration[0])