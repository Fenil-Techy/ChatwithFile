import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnablePassthrough, RunnableMap

load_dotenv()

# Load Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_index = os.getenv("PINECONE_INDEX")

pc = Pinecone(api_key=pinecone_api_key) 
index = pinecone_index 
embeddings = OpenAIEmbeddings( model="text-embedding-3-small" ) 
vector_store = PineconeVectorStore(index_name=index, embedding=embeddings)

# Retriever (limit to 3 docs for speed)
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# LLM (faster + cheaper)
llm = ChatOpenAI(model="gpt-4o-mini")

# Prompt
prompt = ChatPromptTemplate.from_template(
    """Answer the following question: {question}
    Context: {context}
    Give a concise, meaningful answer without unnecessary details."""
)

# Chain
rag_chain = (
    RunnableMap({
        "context": retriever,
        "question": RunnablePassthrough()
    })
    | prompt
    | llm
)
