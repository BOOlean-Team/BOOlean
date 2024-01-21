from openai import OpenAI
import constants
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

client = OpenAI(
    api_key= os.getenv("API_KEY_OPENAI")
)

def get_response(input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input,
            }
        ],
        model=constants.GPT_MODEL,
    )

    return chat_completion.choices[0].message.content
