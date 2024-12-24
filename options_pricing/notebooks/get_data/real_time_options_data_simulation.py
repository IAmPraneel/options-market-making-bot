import yfinance as yf
import time

def simulate_real_time_data(symbol, interval=10, iterations=1):
    stock = yf.Ticker(symbol)
    
    while iterations > 0:
        # Fetch the current options data
        print(" Iteration : ",iterations)
        options_data = stock.option_chain(stock.options[0])
        
        # Get calls and puts data
        calls = options_data.calls
        puts = options_data.puts
        
        # Print or process data
        print(f"Calls at {time.strftime('%Y-%m-%d %H:%M:%S')}:")
        print(calls.head())
        
        #print(f"\nPuts at {time.strftime('%Y-%m-%d %H:%M:%S')}:")
        #print(puts.head())
        
        # Sleep for the specified interval before fetching new data
        time.sleep(interval)
        iterations -= 1
# Start the simulation with MSFT, updating every 60 seconds
simulate_real_time_data('MSFT', 60 , 2)

print("Done")