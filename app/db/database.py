from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

DATABASE_URL = f"postgresql+psycopg2://postgres:1234@0.0.0.0:5432/{settings.DATABASE_NAME}"
# DATABASE_URL = f"postgresql+psycopg2://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

# SQLAlchemy 엔진 생성
engine = create_engine(
    DATABASE_URL,
    pool_size=10,   # 연결 유지 개수
    max_overflow=20, # 추가 요청이 올 경우 최대 확장할 갯수
    connect_args={"options": "-c search_path=public"}
)

# 세션 로컬 생성
SessionLocal = sessionmaker(
    autocommit=False,   # 자동 커밋 방지
    autoflush=False,    # 자동 플러시 방지 -> 명시적으로 commit 호출해야함
    bind=engine         # 생성한 엔진과 연동
)

# Base 모델 정의
Base = declarative_base()

# 모든 테이블을 데이터베이스에 생성
Base.metadata.create_all(bind=engine)

# 데이터베이스 세션 생성 함수
# -> (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
