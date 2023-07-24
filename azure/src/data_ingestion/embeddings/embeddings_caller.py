from openai_embeddings import Embedding
from sentence_transformer_embeddings import SentenceTransformerEmbedding


class EmbeddingsCaller:
    def __init__(self, select_embeddings="sentence_transformers"):
        embeddings_map = {
            "sentence_transformers": SentenceTransformerEmbedding,
            "openai": Embedding,
        }
        self.embedding = embeddings_map.get(select_embeddings)
        if not self.embedding:
            raise ValueError("Invalid embeddings selected")

    def get_embedding(self, sentences):
        return self.embedding.get_embedding(sentences)
