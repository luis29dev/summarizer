import os
from dotenv import load_dotenv
from openai import OpenAI
from src.summarizer.scrapers import Website

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

# Summarization logic

# Define system and user prompts
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

# Construct messages for the chat completion
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]
# Summarize function ß
def summarize(url):
    website = Website(url)
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages_for(website)
    )
    return response.choices[0].message.content