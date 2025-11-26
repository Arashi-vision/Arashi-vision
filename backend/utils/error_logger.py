import logging
import os

# Ensure logs directory exists
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# File path for error log
ERROR_LOG_FILE = os.path.join(LOG_DIR, "error.log")

# Configure logging
logging.basicConfig(
    filename=ERROR_LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_error(message):
    """Write error message to logs/error.log"""
    logging.error(message)
