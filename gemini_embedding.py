import google.generativeai as genai

"""
Generates text embeddings using Google's model.
Useful for retrieval tasks.  
Other models (e.g., OpenAI, BERT) can be added as separate classes.
"""
class GoogleEmbeddingModel:
    
    @staticmethod
    def get_embedding(text):
        """
        Converts text into an embedding.

        Args:
            text : Input text.

        Returns:
            list: Embedding vector.
        """
        response = genai.embed_content(model="models/embedding-001", content=text, task_type="retrieval_document")
        return response["embedding"]
