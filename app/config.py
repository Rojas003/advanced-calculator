from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

APP_MODE = os.getenv("APP_MODE", "production")
HISTORY_FILE = os.getenv("HISTORY_FILE", "calc_history.csv")