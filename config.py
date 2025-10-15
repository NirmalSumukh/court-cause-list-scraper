import os
from dotenv import load_dotenv

load_dotenv()

# Website configuration
BASE_URL = "https://gurugram.dcourts.gov.in/cause-list-%e2%81%84-daily-board/"

# Court complexes available
COURT_COMPLEXES = [
    "District Court, Gurugram",
    "Judicial Complex, Sohna",
    "Judicial Complex, Pataudi"
]

# Default scraping configuration
DEFAULT_COURT_COMPLEX = "District Court, Gurugram"

# Court numbers to scrape (these will be dynamically fetched)
# Based on your earlier screenshot showing courts 1-39
COURT_NUMBERS_TO_SCRAPE = ["1", "2", "3", "4", "5"]  # Start with first 5 courts for testing

# Case types to scrape
CASE_TYPES = ["Civil", "Criminal"]  # Matching the exact radio button values

# Output configuration
OUTPUT_DIR = "outputs"
LOG_DIR = "logs"

# Wait time for manual captcha solving (seconds)
CAPTCHA_WAIT_TIME = 60

# Date format
DATE_FORMAT = "dd/mm/yyyy"  # Format shown in the date field

# Playwright configuration
HEADLESS_MODE = False # Set to True to run browser invisibly in the background
