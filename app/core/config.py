from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Template"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # 서버 설정
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))

    ENV: str = os.getenv("ENVIRONMENT", "local").lower()

    # 데이터베이스 설정
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "0.0.0.0")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT", "5432")

    DATABASE_USER: str = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "1234")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "postgres")

settings = Settings()