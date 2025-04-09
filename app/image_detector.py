from ultralytics import YOLO
#import cv2

class ImageDetector:
    def __init__(self):
        self.__model = YOLO("yolov8n.pt")
        self.__confidence: float = 0.5

    def DetectImages(self):
        results = self.__model("https://ultralytics.com/images/bus.jpg")

        for result in results:
            result.show()
            print(result.boxes)