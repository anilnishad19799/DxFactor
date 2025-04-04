from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class GeminiWrapper:
    def __init__(self, model_name="gemini-2.0-flash-001"):
        self.model_name = model_name
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2
        )

    def generate(self, prompt):
        response = self.llm.invoke(prompt)
        return response.content if response else "No response from Gemini."