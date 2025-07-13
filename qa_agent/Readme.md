
<img width="1512" height="858" alt="Screenshot 2025-07-12 at 11 46 11 PM" src="https://github.com/user-attachments/assets/1b4d20e8-36b7-4225-bda7-408712754e47" />

An interactive Q&A chatbot that reads PDF documents, indexes them with vector embeddings, and answers natural language questions using **Groq's LLM** (`llama-3.1-8b-instant`). Built with **LangChain**, **Hugging Face**, **ChromaDB**, and **Streamlit**.

##Features
- Ask questions based on your uploaded PDFs
- Uses Hugging Face sentence embeddings for semantic similarity
- Stores and retrieves context via Chroma vector store
- Powered by Groq’s blazing-fast LLM
- Friendly chat interface built with Streamlit

##Install Dependencies
pip install -r requirements.txt

##Add Environment Variables
GROQ_API_KEY=your_groq_api_key
TOKENIZERS_PARALLELISM=false

##Add PDFS
Place PDF files into the /pdfs folder. The app will automatically index and load them.

##Run the App
streamlit run app.py
