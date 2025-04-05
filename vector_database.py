from chromadb import PersistentClient
from langchain_community.vectorstores import Chroma
from gemini_embedding import GoogleEmbeddingModel

class VectorDatabase:
    """
    Manages the ChromaDB vector database.
    """
    def __init__(self):
        self.client = PersistentClient(path="../chromadb_store")
        self.collection = self.client.get_collection(name="dxfactor_db")

    def retrieve_documents(self, query):
        embedding_model = GoogleEmbeddingModel()  # Create object
        query_embedding = embedding_model.get_embedding(query)
        results = self.collection.query(query_embeddings=[query_embedding], n_results=10)
        return [item["text"] for item in results["metadatas"][0]]

