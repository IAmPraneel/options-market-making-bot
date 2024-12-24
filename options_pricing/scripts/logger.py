# Keeps track of log 

import logging

def setup_logger():
    logging.basicConfig(filename="logs/data.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger()

logger = setup_logger()
logger.info("Logger initialized.")