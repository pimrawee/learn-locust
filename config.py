from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL")
API_KEY = os.getenv("API_KEY")

URL_CAT = os.getenv("URL_CAT")