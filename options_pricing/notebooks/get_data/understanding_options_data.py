import yfinance as yf

ticker = "MSFT"

stock = yf.Ticker(ticker)

date = stock.options[0]
options_data = stock.option_chain(date)
calls = options_data.calls
puts = options_data.puts

calls.columns()
puts.columns()
    