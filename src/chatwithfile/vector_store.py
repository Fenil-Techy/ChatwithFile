import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")  
pinecone_index = os.getenv("PINECONE_INDEX")

def get_vector_store(chunks):
    if not pinecone_api_key or not pinecone_index:
        raise ValueError("PINECONE_API_KEY and PINECONE_INDEX must be set in the environment variables.")
    
    # Initialize Pinecone client
    pc = Pinecone(api_key=pinecone_api_key)
    
    # Get index object
    index = pinecone_index

    # Embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # ✅ Build vector store directly on index
    vector_store = PineconeVectorStore.from_texts(
        texts=chunks,
        embedding=embeddings,
        index_name=index
    )
    
    return vector_store
