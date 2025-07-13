#LangChain-Groq Webpage Summarizer
An intelligent **webpage summarization app** built using **LangChain**, **Groq LLM (LLaMA 3)**, and **Streamlit**. It extracts and summarizes content from any given URL efficiently using chunking and map-reduce techniques.

##Features
- Load webpage content with `WebBaseLoader`
- Chunk text using `CharacterTextSplitter`
- Summarize using Map-Reduce strategy with Groq's LLaMA 3 LLM
- Powered by Groq API for ultra-fast responses
- Intuitive Streamlit interface for user interaction
- Modular codebase with async support

##Install Dependencies
pip install -r requirements.txt

##Add Environment Variables
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile

##Run the App
streamlit run app.py