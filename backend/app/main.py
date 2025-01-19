import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, courses, quizzes
from app.config import settings
from app.database import init_db

app = FastAPI(title="LMS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


# Include API routes
# app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(courses.router, prefix="/api/courses", tags=["Courses"])
# app.include_router(quizzes.router, prefix="/api/quizzes", tags=["Quizzes"])


# Initialize Database
# @app.lifespan("startup")
# async def startup():
#     await init_db()

@app.get("/")
def read_root():
    return {"message": "LMS Backend is running!"}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("__main__:app", reload=True, port=8000, host="0.0.0.0")