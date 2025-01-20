from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  DATABASE_URL: str
  FRONTEND_URL: str
  DEBUG: bool = False
  # Auth
  SECRET_KEY: str
  ALGORITHM: str = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

  class Config:
    env_file = ".env"


settings = Settings()