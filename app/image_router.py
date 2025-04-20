from fastapi import APIRouter
from pydantic import BaseModel
from image_processor import ImageProcessor

router = APIRouter()
processor = ImageProcessor()

class ImageRequest(BaseModel):
    image_urls: list[str]
    confidence: float

class ImageResponse(BaseModel):
    results: list[str]

@router.post("/detect", response_model=ImageResponse)
async def process_images(request: ImageRequest):
    results: list[str] = []
    
    for url in request.image_urls:
        result_image = processor.ImageProcess(url, request.confidence)
        results.append(result_image)
        
    return {"results": results}