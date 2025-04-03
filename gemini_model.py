import google.generativeai as genai
from config import gemini_api_key

"""
Wrapper for Google's Gemini model.
Handles text generation using the specified model.
"""
class GeminiWrapper:
    def __init__(self, model_name="gemini-1.5-flash"):
        """
        Initializes the Gemini model.

        Args:
            model_name : Name of the Gemini model to use.
        """
        self.model_name = model_name
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt):
        """
        Generates text based on the input prompt.

        Args:
            prompt : Input text.

        Returns:
            Generated response or error message.
        """
        response = self.model.generate_content(prompt)
        return response.text if response else "No response from Gemini."
