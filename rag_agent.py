from tavily_search import TavilySearchEngine
from vector_database import VectorDatabase
from gemini_model import GeminiWrapper
from langchain.prompts import PromptTemplate
from config import relevant_prompt_format, response_prompt_format, tavily_prompt_format

"""
Implements the agentic corrective workflow.
Handles document retrieval, relevance check, and response generation.
"""
class AgenticRAGWorkflow:
    def __init__(self):
        """
        Initializes vector DB, Tavily search, and Gemini model.
        """
        self.vector_db = VectorDatabase()
        self.tavily = TavilySearchEngine()
        self.gemini = GeminiWrapper()

        # Prompts for checking relevance 
        self.relevant_prompt = PromptTemplate(
            input_variables=["query", "retrieved_docs"],
            template=relevant_prompt_format
        )
        
        # prompts for generating response 
        self.response_prompt = PromptTemplate(
            input_variables=["query", "retrieved_docs"],
            template=response_prompt_format
        )

    def process_query(self, query):
        """
        Processes a query by retrieving documents and generating a response.

        Args:
            query : User query.

        Returns:
            Response text and data.
        """
        retrieved_docs = self.vector_db.retrieve_documents(query)
        source = "Vector Database"

        # Check if retrieved documents are relevant
        if retrieved_docs:
            relevance_prompt_text = self.relevant_prompt.format(query=query, retrieved_docs=retrieved_docs)
            relevance_response = self.gemini.generate(relevance_prompt_text)

            if "yes" in relevance_response.lower():
                response_prompt_text = self.response_prompt.format(query=query, retrieved_docs=retrieved_docs)
                final_response = self.gemini.generate(response_prompt_text)
                return final_response, source

        # If no relevant documents, perform a web search
        search_results = self.tavily.search(query)
        if search_results:
            source = "Tavily Search"
            tavily_prompt_text = self.response_prompt.format(query=query, retrieved_docs=search_results)
            final_response = self.gemini.generate(tavily_prompt_text)
            return final_response, source

        return "Result Not Found", "None"
