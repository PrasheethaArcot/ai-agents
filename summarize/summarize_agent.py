from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import CharacterTextSplitter
import asyncio


load_dotenv()

llm = ChatGroq(model="llama3-70b-8192", temperature=0)

map_prompt = ChatPromptTemplate.from_messages([
    ("system", "Write a concise summary of the following:\n\n{context}")
])

reduce_prompt = ChatPromptTemplate.from_messages([
    ("system", "The following is a set of summaries:\n{context}\nDistill it into a final consolidated summary.")
])


def chunk_texts(texts, max_tokens):
    chunks = []
    current = ""
    for t in texts:
        if llm.get_num_tokens(current + t) > max_tokens:
            chunks.append(current.strip())
            current = t
        else:
            current += "\n" + t
    if current:
        chunks.append(current.strip())
    return chunks



async def summarize_url(url: str) -> str:
    loader = WebBaseLoader(url)
    docs = loader.load()

    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=1000, chunk_overlap=0)
    split_docs = text_splitter.split_documents(docs)

    map_prompt = ChatPromptTemplate.from_messages([
        ("system", "Write a concise summary of the following:\n\n{context}")
    ])

    reduce_prompt = ChatPromptTemplate.from_messages([
        ("system", "The following is a set of summaries:\n{context}\nDistill it into a final consolidated summary.")
    ])

    summaries = []
    for doc in split_docs:
        prompt = map_prompt.invoke({"context": doc.page_content})
        response = await llm.ainvoke(prompt)
        summaries.append(response.content)

    combined = "\n".join(summaries)
    chunks = chunk_texts(summaries, max_tokens=5000)

    reduced = []
    for chunk in chunks:
        reduce_input = reduce_prompt.invoke({"context": chunk})
        response = await llm.ainvoke(reduce_input)
        reduced.append(response.content)

    final_input = reduce_prompt.invoke({"context": "\n".join(reduced)})
    final_response = await llm.ainvoke(final_input)

    return final_response.content