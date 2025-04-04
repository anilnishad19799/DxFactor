from langchain_tavily import TavilySearch
from config import tavily_api_key

class TavilySearchEngine:

    def __init__(self):
        """
        Initializes the Tavily search engine with an API key.
        """
        self.tavily = TavilySearch(tavily_api_key=tavily_api_key)

    def search(self, query):
        """
        Searches the web using Tavily.

        Args:
            query : The search query.

        Returns:
            Search results with top 5 results.
        """
        return self.tavily.invoke({"query": query, "num_results": 5})
