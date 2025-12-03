from fastapi import APIRouter, UploadFile, File
from src.chatwithfile.file_loader import read_file, chunk_text
from src.chatwithfile.vector_store import get_vector_store


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # 1. Read file content
        text = read_file(file.file)
        
        # 2. Chunk text
        chunks = chunk_text(text)
        
        # 3. Push to Pinecone
        vector_store = get_vector_store(chunks)
        
        return {"status": "success", "chunks_added": len(chunks)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
