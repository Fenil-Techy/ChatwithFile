from setuptools import setup, find_packages

setup(
    name='chatwithfile',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'streamlit',
        'langchain-pinecone',
        'python-dotenv',
        'langchain_openai',
        'langchain_community',
        'PyPDF2',
        'pinecone',# or langchain_ollama in your case
    ]
)