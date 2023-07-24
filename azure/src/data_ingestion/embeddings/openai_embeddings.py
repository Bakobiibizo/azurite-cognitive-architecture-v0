import os
from dotenv import load_dotenv
from openai import Embedding

load_dotenv()


class OpenAIEmbeddings:
    def __init__(self):
        self.embedding = Embedding(
            api_key=os.environ.get("OPENAI_API_KEY"),
            model_name="text-embedding-ada-002",
        )

    def get_embedding(self, sentences):
        return self.embedding.encode(sentences)