from ultralytics import YOLO
from app.detect_result import DetectResult

class ImageDetector:
    def __init__(self):
        self.__model = YOLO("yolov8n.pt")
        self.__confidence: float = 0.5

    def DetectImages(self, image: str):
        results = self.__model(image)
        
        for result in results:
            result.show()
            print(result.boxes)