from fastapi import FastAPI
from routes.upload import router as upload_router
from routes.query import router as query_router 

app = FastAPI()

app.include_router(upload_router, prefix="/upload")
app.include_router(query_router, prefix="/query")

@app.get("/")
def read_root():
    return {"Hello": "World"}

