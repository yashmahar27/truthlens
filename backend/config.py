import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

print("DEBUG KEY:", NEWS_API_KEY)  # temporary debug