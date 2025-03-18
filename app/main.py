from fastapi import FastAPI
from app.api.v1.user_routes import router as user_router
from app.db.database import get_engine, Base
from app.db import models

app = FastAPI()

app.include_router(user_router, prefix="/v1/users", tags=["Users APIs"])

# FastAPI가 시작될 때 DB 테이블 DDL 전략
Base.metadata.create_all(bind=get_engine())

@app.get("/")
async def root():
    return {"message": "Hello World"}