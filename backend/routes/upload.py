from fastapi import APIRouter, UploadFile, File
from services.document_loader import load_document
from services.chunker import chunk_text

router = APIRouter()

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    content = file.file.read()
    text = load_document(content, file.filename)
    chunks = chunk_text(text)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content),
        "text": text,
        "chunks": chunks,
        "status": "success"
    }