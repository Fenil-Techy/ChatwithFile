import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_ollama import OllamaEmbeddings

load_dotenv()

pinecone_api_key =os.getenv("PINECONE_API_KEY")  
pinecone_index =os.getenv("PINECONE_INDEX")

dimesnion = 4096  # Dimension of the embeddings, adjust acc to model if necessary

def get_vector_store(chunks):
    if not pinecone_api_key or not pinecone_index:
        raise ValueError("PINECONE_API_KEY and PINECONE_INDEX must be set in the environment variables.")
    
    # Initialize Pinecone
    pc=Pinecone(api_key=pinecone_api_key)
    
    # Create or connect to the Pinecone index
    index =pinecone_index
    
    # Initialize Ollama embeddings
    embeddings = OllamaEmbeddings(model="llama3.1:8b")
    
    # Create the vector store
    vector_store = PineconeVectorStore.from_texts(texts=chunks,index_name=index, embedding=embeddings)
    
    return vector_store