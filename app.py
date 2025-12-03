import streamlit as st
from src.chatwithfile.file_loader import read_file, chunk_text
from src.chatwithfile.vector_store import get_vector_store
from src.chatwithfile.rag_pipeline import rag_chain

st.set_page_config(page_title="Chat with File", page_icon="📄")

st.title("📄 Chat with your File")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])


if "vector_store_ready" not in st.session_state :
    st.session_state.vector_store_ready= False
if "processing_error" not in st.session_state :
    st.session_state.processing_error= None
    

if uploaded_file:
    if st.button("Start chatting"):
        with st.spinner("Reading file"):
            try:
                text = read_file(uploaded_file)
                chunks = chunk_text(text)
                get_vector_store(chunks)
                
                st.session_state.vector_store_ready= True
                st.session_state.processing_error= None
            
            except Exception as e:
                st.session_state.processing_error = str(e)
                st.error(f"An error occurred while processing the file: {e}")

if st.session_state.processing_error:
    st.error(f"error: {st.session_state.processing_error}")

if st.session_state.vector_store_ready:
    
    st.header("💬 Ask a question")
    question = st.text_input("Type your question here:")

    if question:
        button=None
        with st.spinner("Analyzing..."):
            result = rag_chain.invoke(question)
            answer =result.content

            st.subheader("📝 Answer")
            st.write(answer)
