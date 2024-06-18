from fastapi import FastAPI
from api.routers import items

app = FastAPI()

app.include_router(items.router)
