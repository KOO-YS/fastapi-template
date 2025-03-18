from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

DATABASE_URL = f"postgresql+psycopg2://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

# SQLAlchemy 엔진 및 세션 생성
def get_engine():
    """SQLAlchemy 엔진을 생성하여 반환"""
    engine = create_engine(
        DATABASE_URL,
        pool_size=10,       # 연결 유지 개수
        max_overflow=20,    # 추가 요청이 올 경우 최대 확장할 갯수
        echo=True,          # SQL 실행 로그 출력 (디버깅 용도)
    )
    return engine

# 세션 로컬 생성
def get_session_local(engine):
    """세션 로컬 생성 (FastAPI에서 의존성 주입용)"""
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal

# Base 모델 정의
Base = declarative_base()

# 모든 테이블을 데이터베이스에 생성

# 데이터베이스 세션 생성 함수
# -> (Dependency Injection)
def get_db():
    engine = get_engine()  # 엔진 생성
    SessionLocal = get_session_local(engine)  # 세션 로컬 생성
    db = SessionLocal()  # DB 세션 객체 생성
    try:
        yield db
    finally:
        db.close()
