import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", "8000"))
HOST = os.getenv("HOST", "0.0.0.0")

DEFAULT_PATTERN_THRESHOLD = 60
TOP_N_PATTERNS = 3

ADULT_AGE = 18
ELDERLY_AGE = 65
STANDARD_WEIGHT = 60

QIAN_TO_GRAM = 3.125

PREGNANT_WARNING_LEVEL = "danger"
LACTATION_WARNING_LEVEL = "warning"
CONFLICT_WARNING_LEVEL = "danger"
