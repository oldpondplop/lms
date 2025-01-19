import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

app = FastAPI(title="LMS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
def read_root():
    return {"message": "LMS Backend is running!"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("__main__:app", reload=True, port=8000, host="0.0.0.0")