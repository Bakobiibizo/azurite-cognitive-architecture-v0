from sentence_transformers import SentenceTransformer


class SentenceTransformerEmbedding:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embedding = SentenceTransformer(model_name)

    def get_embedding(self, sentences):
        return self.embedding.encode(sentences)
