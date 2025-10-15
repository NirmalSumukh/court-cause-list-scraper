import os
from dotenv import load_dotenv

load_dotenv()

# Website configuration
BASE_URL = "https://gurugram.dcourts.gov.in/cause-list-%e2%81%84-daily-board/"

# Court complex options
COURT_COMPLEXES = {
    "District Court, Gurugram": "HRGR01,HRGR02,HRGR03",
    "Judicial Complex, Sohna": "HRGRA0,HRGRA1",
    "Judicial Complex, Pataudi": "HRGRB0,HRGRB1"
}

# Default court complex
DEFAULT_COURT_COMPLEX = "District Court, Gurugram"

# Common court numbers (will be dynamically loaded from website)
DEFAULT_COURT_NUMBERS = ["1 Ms. Vani Gopal Sharma - District and Sessions Judge",
                         "2 Dr. Gagan Geet Kaur - Additional District and Sessions Judge",
                         "3 Ms. Jasmine Sharma - Additional District and Sessions Judge"]

# Case types
CASE_TYPES = ["Civil", "Criminal"]

# Output configuration
OUTPUT_DIR = "outputs"
LOG_DIR = "logs"
