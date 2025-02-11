import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OPEN_METEO_API_URL = os.getenv("OPEN_METEO_API_URL")
