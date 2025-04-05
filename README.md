# DXFactor Chat Agent 🤖🔍  
**RAG-based Solution using Google Gemini API**

A Retrieval-Augmented Generation (RAG) chatbot built using **Google Gemini API**, designed to answer user queries based on publicly available information from [DXFactor](https://dxfactor.com/).

---

## 🚀 Features
- 🔎 Web Scraping with Selenium  
- 🧠 Gemini Embeddings + LLM (via gemini-2.0-flash-001)  
- 📦 Vector storage with ChromaDB  
- 🔁 RAG pipeline using LangChain  
- 🌐 Fallback to Tavily Search API for out-of-scope queries  
- 💬 Streamlit UI for live interaction  

---

## ⚙️ How It Works
1. **Scrape** DXFactor's content using Selenium.  
2. **Embed** and store text in **ChromaDB** using Gemini embeddings.  
3. **Retrieve** relevant content for user queries via vector similarity.  
4. **Generate** response using **Gemini 1.5 Turbo**.  
5. **Fallback** to **Tavily Search API** when no relevant data is found locally.  

---

## 🧪 Example Queries
- *What services does DXFactor provide?*  
- *Where is DXFactor headquartered?*  
- *Who are some key clients or partners mentioned on the website?*  
- *Provide a brief overview of DXFactor's main industry or niche.*  

---

## 🧠 Technical Decisions
- Unified embedding and generation using **Gemini API** for better consistency.  
- Lightweight & persistent vector DB via **ChromaDB**.  
- Used **Tavily Search** to improve responses for unknown topics.  
- Built UI with **Streamlit** for ease of deployment and demo.  

---

## 🧩 Challenges Faced
| Challenge                            | Solution                                       |
|-------------------------------------|------------------------------------------------|
| Relevant response generation        | Gemini embeddings + relevance filtering + Google LLM model |
| Handling out-of-domain queries      | Fallback to Tavily Search API                 |
| User-friendly UI                    | Built clean, simple interface with Streamlit  |

---

## 📦 Setup Instructions

### Prerequisites
- Python 3.8+  
- Google API key (for Gemini)  
- Tavily API key  
- ChromeDriver installed (for Selenium)  

---

### 1) Clone the repository:
```bash
git clone https://github.com/anilnishad19799/DxFactor
cd DxFactor
```

### 2) Create a virtual environment:
```bash
# Create environment
python -m venv rag_venv

# Activate on Windows
rag_venv\Scripts\activate

# OR activate on Linux/macOS
source rag_venv/bin/activate
```

### 3) Install dependencies:
```bash
pip install -r requirements.txt
```

### 4) Set up environment variables:
Create a `.env` file in the root folder and add:
```
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5) Scrape website & store data in ChromaDB (Optional if already done in my case it is already done and data is on GitHub):
```bash
# Run scraper to get website data
python dxfactor_scraper.py

# This generates dxfactor_data.txt
# Then convert it to vector store
python text_to_chromadb.py
```

### 6) Run the application:
```bash
streamlit run streamlit_run.py
```

---

## 📂 Output Folder

All responses generated for test queries are stored in the `output/` directory.  
You can check this folder to review how different queries are processed and answered by the chatbot.

---

## 🔮 Future Enhancements
- ⏳ Automate periodic re-scraping and DB update  
- 🧠 Improve result ranking and filtering  
- 🗨️ Add multi-turn conversational memory  

---

## 👤 Author
**Nishad Anil**  
📄 Licensed under [MIT License](LICENSE)
