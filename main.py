from src.summarizer.openai_client import validate_api_key
from src.summarizer.openai_client import validation_gpt_chat
from src.summarizer.scrapers import Website



def main():
    """Main entry point for the web page summarizer."""
    try:

        # Validate the API key before proceeding
        validate_api_key()

        # validate gpt chat
        validation_gpt_chat()

        # Test the Website scraper
        url = "https://cnn.com"
        website = Website(url)
        print(f"Title: {website.title}")


    except Exception as e:
        print(f"An error occurred: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())