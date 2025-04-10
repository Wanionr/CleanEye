from app.image_detector import ImageDetector
from app.image_censor import ImageCensor
from app.detect_result import DetectResult

class ImageProcessor:
    def __init__(self):
        self.__detector = ImageDetector()
        self.__censor = ImageCensor()
    
    def ImageProcess(self, images: list[str]):

        for image in images:
            resultlist = list[DetectResult]

            resultlist = self.__detector(image)
            