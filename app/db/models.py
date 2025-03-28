from sqlalchemy import Column, Integer, String
from app.db.database import Base

# 클래스 User와 테이블 users를 매핑
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
