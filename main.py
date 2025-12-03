from fastapi import FastAPI
from src.chatwithfile.routers import upload, chat

app = FastAPI(title="ChatWithFile API")

# Register routers
app.include_router(upload.router, prefix="/file", tags=["File"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
