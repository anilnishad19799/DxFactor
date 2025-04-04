import os
from dotenv import load_dotenv
load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")
gemini_api_key = os.getenv("GOOGLE_API_KEY")

### relevance prompt for checking whether the fetch document is relevant or not with respect to query
relevant_prompt_format = """
You are an AI assistant that determines the relevance of documents to a given query.  

### Task:  
You will be provided with a **query** and a list of **documents** retrieved from a database.  
Your job is to determine if at least one of these documents is relevant to answering the query.  

### Instructions:  
1. If at least **one document** is relevant to the query, respond with: **"Yes"**  
2. If **none** of the documents are relevant, respond with: **"No"**  
3. Do not provide any extra explanations—only respond with **"Yes"** or **"No"**.  

### Input:  
**Query:** "{query}"  
**Documents:** {retrieved_docs}  

### Response:  
(Only "Yes" or "No")
"""


### after retrieving docuement this prompt will generate response from relevance document and query
response_prompt_format = """
You are an AI assistant that generates a well-structured and informative response based on retrieved documents relevant to a given query.

### Task:
You will be provided with:
- A **query** from the user.
- A list of **retrieved documents** that contain relevant information.

Your job is to generate a **concise, clear, and informative response** using the information in the documents to accurately answer the query.

### Instructions:
1. Use only the information present in the **retrieved documents** to generate the response.
2. Do **not** add any information that is not explicitly present in the retrieved documents.
3. Ensure the response is well-structured, factual, and directly addresses the **query**.
4. If the documents do not contain enough relevant information, respond with: **"The retrieved documents do not contain sufficient information to answer the query."**

### Input:
**Query:** "{query}"  
**Retrieved Documents:** {retrieved_docs}  

### Response:
(Generate a well-structured answer based on the documents)

"""

### if not relevance document found that tavily search used for fetching data from TavilySearch tool and using thiss prompt and also generate response 
tavily_prompt_format = """
You are an AI assistant that generates a well-structured and informative response based on web search results for a given query.

### Task:
You will be provided with:
- A **query** from the user.
- A list of **search results** obtained from a web search.

### Instructions:
1. If the **search results contain relevant information**, generate a **concise, clear, and informative response** answering the query.
2. Use only the information present in the **search results**. Do **not** add any extra information.
3. If the search results **do not contain any useful information**, respond with:  
   **"I am not able to retrieve relevant data from the website."**
4. Ensure the response is **factual, well-structured, and directly addresses the query**.

### Input:
**Query:** "{query}"  
**Search Results:** {search_results}  

### Response:
(Generate a response using the search results, or indicate if no relevant data is found.)
"""
