import streamlit as st
from src.chatwithfile.file_loader import read_file, chunk_text
from src.chatwithfile.vector_store import get_vector_store
from src.chatwithfile.rag_pipeline import rag_chain

st.set_page_config(page_title="Chat with File", page_icon="📄")

st.title("📄 Chat with your File")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file is not None:   
    text = read_file(uploaded_file)
    chunks = chunk_text(text)

    if st.button("Start chatting"):
        with st.spinner("Reading file"):
            get_vector_store(chunks)

            # Question box
            st.header("💬 Ask a question")

            question = st.text_input("Type your question here:")

            if question:
                with st.spinner("Analyzing..."):
                    rag_chain = rag_chain()
                    result = rag_chain.invoke({"query": question})
                    answer =result.content

                    st.subheader("📝 Answer")
                    st.write(answer)