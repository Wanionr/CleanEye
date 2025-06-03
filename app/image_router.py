from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from image_processor import ImageProcessor

router = APIRouter()
processor = ImageProcessor()

class ImageRequest(BaseModel):
    requestUrl: str
    urls: list[str]
    rate: int
    type: int

class ImageResponse(BaseModel):
    requestUrl: str
    type: int
    filteredUrls: list[str]
    urls: list[str]

@router.post("/detect", response_model=ImageResponse)
async def process_images(request: ImageRequest):  
    response = ImageResponse(
        requestUrl = request.requestUrl,
        type = request.type,
        filteredUrls = [],
        urls = []
    )

    for url in request.urls:
        print(f"processing {url}")
        
        resultUrl = await run_in_threadpool(processor.ImageProcess, url, request.rate, request.type)
        if resultUrl is not None:
            response.urls.append(url)
            response.filteredUrls.append(resultUrl)
        
    return response