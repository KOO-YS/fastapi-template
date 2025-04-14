from fastapi import FastAPI
from app.api.v1.user_routes import router as user_router
from app.api.v1.rabbitmq_routes import router as rabbit_router
from app.db.database import get_engine, Base
from app.db import models
from app.utils.rabbitmq import rabbitmq_client

app = FastAPI()

app.include_router(user_router, prefix="/v1/users", tags=["Users APIs"])
app.include_router(rabbit_router, prefix='/v1/mq', tags=['RabbitMQ APIs'])

# FastAPI가 시작될 때 DB 테이블 DDL 전략
Base.metadata.create_all(bind=get_engine())

@app.on_event("startup")
async def startup():
    await rabbitmq_client.connect()

@app.get("/")
async def root():
    return {"message": "Hello World"}