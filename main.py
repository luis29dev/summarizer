import os
from src.summarizer.openai_client import validate_api_key
from src.summarizer.openai_client import validation_gpt_chat
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


def main():
    """Main entry point for the web page summarizer."""
    try:

        # Validate the API key before proceeding
        validate_api_key()

        # validate gpt chat
        validation_gpt_chat()

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())