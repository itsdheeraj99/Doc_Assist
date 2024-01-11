import os 

from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Pinecone
import pinecone 
from dotenv import load_dotenv, dotenv_values
load_dotenv() 

pinecone.init(
    api_key = os.getenv("PINECONE_API_KEY"),
    environment = os.getenv("PINECONE_ENVIRONMENT_REGION"),
)


def ingest_docs():
    loader = PyPDFLoader("https://arxiv.org/pdf/2303.08774.pdf")
    raw_docs = loader.load()
    print(f"loaded {len(raw_docs)} documents")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 400, chunk_overlap = 50, separators=["\n\n", "\n", " ", ""]
    )
    documents = text_splitter.split_documents(raw_docs)
    print(len(documents))

    embeddings = OpenAIEmbeddings(chunk_size = 1, disallowed_special=())
    print(f"Adding {len(documents)} to Pinecone")
    Pinecone.from_documents(documents, embeddings, index_name = "chat-doc-index")
    print("Loaded the embeddings to vectorstore") 
    


if __name__ == '__main__':
    ingest_docs() 
