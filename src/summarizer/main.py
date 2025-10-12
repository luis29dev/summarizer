import os
from validation import validate_api_key

from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# Validate the API key before proceeding
validate_api_key()