from fastapi import FastAPI
from src.endpoints.item import item_router
from src.endpoints.user import user_router

app = FastAPI()
app.include_router(item_router, prefix="/items")
app.include_router(user_router, prefix="/user")