from scripts.logger import logger
from scripts.fetch_market_data import fetch_data
from scripts.process_data import process_data

def main():
    logger.info("Starting the options pricing project.")
    
    # Fetch market data
    data = fetch_data("AAPL", "2023-01-01", "2023-12-31")
    logger.info("Market data fetched successfully.")
    
    # Process data (e.g., calculate Greeks)
    processed_data = process_data(data)
    logger.info("Data processed successfully.")
    
    # Further tasks or analysis can go here
    logger.info("Project execution completed.")

if __name__ == "__main__":
    main()