from PyPDF2 import PdfReader
from io import BytesIO

def load_document(file_bytes: bytes, filename: str) -> str:
    if filename.lower().endswith(".pdf"):
        pdf_stream = BytesIO(file_bytes)  
        reader = PdfReader(pdf_stream)

        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        return text

    # fallback: treat as plain text
    return file_bytes.decode("utf-8", errors="ignore")
