from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import AsyncSessionLocal
from app.models import Course

router = APIRouter()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@router.get("/")
async def get_courses(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM courses")
    return result.fetchall()
