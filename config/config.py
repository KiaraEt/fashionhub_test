import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch BASE_URL from the system environment variable and then set a default value
BASE_URL = os.getenv("BASE_URL") or "https://pocketaces2.github.io/fashionhub"
# BASE_URL = os.getenv("BASE_URL")
