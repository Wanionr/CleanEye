#app/main.py
from fastapi import FastAPI
from app.image_detector import ImageDetector

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "NSFW Image Filter Server is running!"}