#app/main.py
from fastapi import FastAPI
from app.image_processor import ImageProcessor

app = FastAPI()

@app.get("/")
def read_root():
    processor = ImageProcessor()
    processor.ImageProcess(["https://ultralytics.com/images/bus.jpg"])
    return {"message": "NSFW Image Filter Server is running!"}