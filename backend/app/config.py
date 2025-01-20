import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
  DATABASE_URL: str = os.getenv("DATABASE_URL")
  FRONTEND_URL: str = os.getenv("FRONTEND_URL")
  DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")
  # auth
  SECRET_KEY: str = os.getenv("SECRET_KEY")
  ALGORITHM: str = os.getenv("HS256")
  ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

  class Config:
    env_file = ".env"

settings = Settings()
