"""
Logging example for data pipelines
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_data():
    logging.info("Data processing started")
    logging.info("Data processing completed successfully")

if __name__ == "__main__":
    process_data()
