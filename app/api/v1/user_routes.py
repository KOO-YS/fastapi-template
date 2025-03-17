from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.crud import create_user, get_user_by_id

router = APIRouter()

@router.post("/users/")
async def create_new_user(name: str, email: str, db: Session = Depends(get_db)):
    """새로운 사용자 생성"""
    user = create_user(db, name, email)
    return {"message": "User created successfully", "user": user}

@router.get("/users/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """사용자 정보 조회"""
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
