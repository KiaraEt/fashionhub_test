import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "http://localhost:4000/fashionhub")