import google.generativeai as genai
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import gemini_api_key
import os

class DXFactorSearchEngine:
    def __init__(self, data_path: str, chroma_path: str = "./chromadb_store", collection_name: str = "dxfactor_db"):

        # Initialize ChromaDB (Persistent Client)
        self.chroma_client = chromadb.PersistentClient(path=chroma_path)
        self.collection = self.chroma_client.get_or_create_collection(name=collection_name)

        # Load data from file
        self.data_path = data_path
        self.full_text = self._load_data()

        # Initialize embedding model
        self.embedding_model = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    def _load_data(self) -> str:
        with open(self.data_path, "r", encoding="utf-8") as file:
            return file.read()

    def _get_embedding(self, text: str) -> list:
        return self.embedding_model.embed_query(text)

    def preprocess_and_store(self, chunk_size: int = 500, chunk_overlap: int = 50):
        # Split Text into Chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            add_start_index=True
        )
        chunks = splitter.split_text(self.full_text)
        print(f"Split data into {len(chunks)} chunks.")

        # Convert Chunks to Embeddings and Store in ChromaDB
        for idx, chunk in enumerate(chunks):
            embedding = self._get_embedding(chunk)
            self.collection.add(
                ids=[str(idx)],
                embeddings=[embedding],
                metadatas=[{"text": chunk}]
            )
        print("Data stored successfully in ChromaDB!")

    def search(self, query: str, n_results: int = 5):
        # Query ChromaDB
        query_embedding = self._get_embedding(query)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results["metadatas"][0]

    def display_results(self, response):
        # 8️⃣ Display Results
        for item in response:
            print(f"🔹 Relevant Text: {item['text']}")


# Example usage:
if __name__ == "__main__":
    engine = DXFactorSearchEngine(
        data_path="dxfactor_data.txt"
    )

    engine.preprocess_and_store()
    response = engine.search("What services does DXFactor provide?")
    engine.display_results(response)
