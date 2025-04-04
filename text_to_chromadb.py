import google.generativeai as genai
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import gemini_api_key

class TextToChromaDB:
    def __init__(self, api_key, db_path="./chromadb_store"):
        """Initialize the class with API key and ChromaDB storage path."""
        self.api_key = api_key
        self.db_path = db_path
        genai.configure(api_key=self.api_key)
        self.chroma_client = chromadb.PersistentClient(path=self.db_path)
        self.collection = self.chroma_client.get_or_create_collection(name="dxfactor_db")

    def get_embedding(self, text):
        """Generate embeddings using Google Gemini API."""
        response = genai.embed_content(model="models/embedding-001", content=text, task_type="retrieval_document")
        return response["embedding"]

    def load_and_split_text(self, file_path, chunk_size=300, chunk_overlap=100):
        """Load text from file and split into smaller chunks."""
        with open(file_path, "r", encoding="utf-8") as file:
            full_text = file.read()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, 
            chunk_overlap=chunk_overlap,
            length_function=len, 
            add_start_index=True
        )
        return text_splitter.split_text(full_text)

    def store_embeddings(self, file_path):
        """Convert text chunks into embeddings and store them in ChromaDB."""
        chunks = self.load_and_split_text(file_path)
        print(f"Split data into {len(chunks)} chunks.")
        
        for idx, chunk in enumerate(chunks):
            embedding = self.get_embedding(chunk)
            self.collection.add(ids=[str(idx)], embeddings=[embedding], metadatas=[{"text": chunk}])
        
        print("Data stored successfully in ChromaDB!")

# Example Usage
if __name__ == "__main__":
    processor = TextToChromaDB(api_key=gemini_api_key)
    processor.store_embeddings("dxfactor_data.txt")
