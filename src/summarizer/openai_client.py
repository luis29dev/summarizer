import os
from dotenv import load_dotenv
from openai import OpenAI

 # Load environment variables in a file called .env
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

def validate_api_key():
    """Validate the OpenAI API key from environment variables."""

    # Check the key validity
    if not api_key:
        print("No API key was found - please head over to the troubleshooting notebook in this folder to identify and fix it!")
    elif not api_key.startswith("sk-proj-"):
        print("An API key was found, but it doesn't start with sk-proj-; please check you're using the right key")
    elif api_key.strip() != api_key:
        print("An API key was found, but it looks like it might have space or tab characters at the start or end ")
    else:
        print("API key found and looks good so far!")


# create an instance of the OpenAI client
openai = OpenAI()


# create a message and get a response from the model
def validation_gpt_chat():
    message = "Hello, GPT! This is my first ever message to you! Hi!"
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
    print(response.choices[0].message.content)