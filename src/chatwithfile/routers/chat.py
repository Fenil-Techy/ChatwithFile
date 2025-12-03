from fastapi import APIRouter
from pydantic import BaseModel
from src.chatwithfile.rag_pipeline import rag_chain


router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/")
async def chat_endpoint(request: ChatRequest):
    try:
        response = rag_chain.invoke(request.question)
        return {"answer": response.content}
    except Exception as e:
        return {"status": "error", "message": str(e)}
