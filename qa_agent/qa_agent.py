import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_groq import ChatGroq

load_dotenv()
os.environ["TOKENIZERS_PARALLELISM"] = os.getenv("TOKENIZERS_PARALLELISM", "false")

class GroqChatbot:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.0,
            max_retries=2,
            api_key=self.api_key,
        )
        self.vectorstore = self._load_vectorstore()

    def _load_vectorstore(self):
        docs = PyPDFDirectoryLoader("pdfs").load()
        chunks = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(docs)
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        return Chroma.from_documents(chunks, embeddings, persist_directory="vector_store")

    def truncate_text(self, context: str, max_tokens: int = 6500) -> str:
        tokens = context.split()
        return " ".join(tokens[:max_tokens]) if len(tokens) > max_tokens else context

    def get_response(self, query: str) -> str:
        retriever = self.vectorstore.as_retriever()
        relevant_docs = retriever.invoke(query)
        context = " ".join(doc.page_content for doc in relevant_docs)
        context = self.truncate_text(context)
        prompt = f"Question: {query}\n\nContext: {context}\n\nAnswer:"
        response = self.llm.invoke(prompt)
        return response.content
