import os
from src.summarizer.open_ai_client import validate_api_key
from src.summarizer.open_ai_client import validation_gpt_chat
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


# Validate the API key before proceeding
validate_api_key()

# validate gpt chat
validation_gpt_chat()