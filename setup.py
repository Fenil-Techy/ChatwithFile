from setuptools import setup, find_packages

setup(
    name='TalkingFile',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'streamlit',
        'langchain-pinecone',
        'python-dotenv',
        'langchain_ollama',
        'langchain_community',
        'PyPDF2',
        'pinecone',# or langchain_ollama in your case
    ]
)