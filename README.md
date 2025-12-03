# 🧠 AI Chat With File

An intelligent chat application that allows users to upload documents (PDF/TXT/DOCX) and chat with an AI assistant that understands the file using Python, LangChain, Streamlit, and OpenAI.

## 📌 Features

📁 Upload PDF, TXT, or DOCX files

🤖 Ask questions based on the file content

⚙️ Uses LangChain for text chunking, embeddings & retrieval

🧠 OpenAI models for smart responses

🌐 Streamlit UI (simple and fast)

## Screenshot
<img width="1300" height="885" alt="Screenshot 2025-12-03 165340" src="https://github.com/user-attachments/assets/a511ec31-0dd0-41f5-a5a4-08bca5a70a8b" />


## 🚀 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/ai-chat-with-file.git
cd ai-chat-with-file

2️⃣ Create virtual environment
python -m venv venv

3️⃣ Activate environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Add your OpenAI API key
- Create a file named .env:
- OPENAI_API_KEY=your_api_key_here
- Or export it in terminal:
- export OPENAI_API_KEY=your_api_key_here

▶️ Run the App
streamlit run app.py
