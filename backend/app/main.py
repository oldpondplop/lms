import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LMS Backend is running!"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("__main__:app", reload=True, port=8000, host="0.0.0.0")