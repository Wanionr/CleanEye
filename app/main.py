from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.image_router import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="/app/app/static"), name="static")

app.include_router(router)