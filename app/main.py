from fastapi import FastAPI
from app.api.v1.user_routes import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/v1/users", tags=["Users APIs"])

@app.get("/")
async def root():
    return {"message": "Hello World"}