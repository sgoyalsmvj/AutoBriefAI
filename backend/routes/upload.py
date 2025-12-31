from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    content = file.file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content),
        "status": "success"
    }