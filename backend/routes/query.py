from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/")
async def query_document(payload: QueryRequest):
    return {"question": payload.question,
        "answer": "Document processing pipeline not connected yet."}