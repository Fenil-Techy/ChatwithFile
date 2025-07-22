import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnablePassthrough, RunnableMap

load_dotenv()

pinecone_api_key =os.getenv("PINECONE_API_KEY")  
pinecone_index =os.getenv("PINECONE_INDEX")

pc = Pinecone(api_key=pinecone_api_key)
index = pinecone_index
embeddings = OllamaEmbeddings(model="llama3.1:8b")
vector_store = PineconeVectorStore(index_name=index, embedding=embeddings)


llm=ChatOllama(model="llama3.1:8b")

prompt=ChatPromptTemplate.from_template(
    """Answer the question based only on the following context: {context}
    Question: {question}    
    Answer:"""
)

retriever = vector_store.as_retriever()

rag_chain = (
    RunnableMap({
        "context": retriever,
        "question": RunnablePassthrough()
    })
    | prompt
    | llm
)
