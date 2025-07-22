from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader

def read_file(uploaded_file):
    if uploaded_file.name.endswith('.pdf'):
        reader=PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    elif uploaded_file.name.endswith('.txt'):
        text = uploaded_file.read().decode("utf-8")
        return text
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or TXT file.")

def chunk_text(text, chunk_size=1000,chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks