import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAITextGeneration:
    def __init__(self):
        pass

    def send_chat_complete(self, messages):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4", messages=messages, stream=True
            )
            return response
        except ConnectionError as e:
            print(f"There was an error connecting to OpenAI: {e}")
            raise
