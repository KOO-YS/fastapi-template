from sqlalchemy.orm import Session
from app.db.models import User

def create_user(db: Session, name: str, email: str):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()             # 명시적 선언
    db.refresh(new_user)    # 최신 상태 반환
    return new_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
