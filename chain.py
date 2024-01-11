import os
from typing import Any, Dict, List

from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import Pinecone
import pinecone 
from dotenv import load_dotenv, dotenv_values
load_dotenv() 

pinecone.init(
    api_key = os.getenv("PINECONE_API_KEY"),
    environment = os.getenv("PINECONE_ENVIRONMENT_REGION"),
)

def run_llm(query: str, chat_history: List[Dict[str, Any]] = []):
    embeddings = OpenAIEmbeddings(openai_api_key = os.getenv("OPENAI_API_KEY"))
    docsearch = Pinecone.from_existing_index(
        embedding = embeddings,
        index_name = "chat-doc-index"
    )
    chat = ChatOpenAI(
        verbose = True,
        temperature = 0,
    )
    qa = ConversationalRetrievalChain.from_llm(
        llm = chat, 
        retriever = docsearch.as_retriever(), 
        return_source_documents = True
    )
    return qa({"question": query, "chat_history": chat_history})

if __name__ == "__main__":
    ans = run_llm(query = "What is GPT4?")
    print(ans) 