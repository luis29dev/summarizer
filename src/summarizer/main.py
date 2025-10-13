import os
from summarizer.open_ai_client import validate_api_key
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


# Validate the API key before proceeding
validate_api_key()

