from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL")
API_KEY = os.getenv("API_KEY")

URL_CAT = os.getenv("URL_CAT")
URL_ONLINE_BOUTIQUE = os.getenv("URL_ONLINE_BOUTIQUE")
URL_HTTPBIN = os.getenv("URL_HTTPBIN")