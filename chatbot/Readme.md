
<img width="1512" height="838" alt="Screenshot 2025-07-12 at 11 44 39 PM" src="https://github.com/user-attachments/assets/b87c9c73-e716-4ed4-9514-ba24ae5eb28f" />


#LangChain-Groq Chatbot
A conversational AI assistant built with **LangChain**, **Groq LLM API**, and **Streamlit**, designed for fast and intelligent responses. This project supports both command-line and web interfaces.

##Features
- LangChain integration for prompt orchestration
- Groq API for blazing-fast LLM responses (LLaMA-3.3-70B or Mixtral)
- Interactive UI with Streamlit
- System prompt to guide assistant behavior
- Logging, structured config, and modular architecture

##Install Dependencies
pip install -r requirements.txt

##Add Environment Variables
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0.7
MAX_TOKENS=512
APP_NAME=LangChain Groq Chatbot

##Run the App
streamlit run app.py
