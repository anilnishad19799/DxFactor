from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class GoogleEmbeddingModel:
    def __init__(self, model_name="models/text-embedding-004"):
        self.embedding_model = GoogleGenerativeAIEmbeddings(model=model_name)

    def get_embedding(self, text):
        """
        Converts text into an embedding.
        Args:
            text : input text.
        Returns:
            list: Embedding vector.
        """
        return self.embedding_model.embed_query(text)
