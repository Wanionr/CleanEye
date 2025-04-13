from app.image_detector import ImageDetector
from app.image_censor import ImageCensor
from app.detect_result import DetectResult

class ImageProcessor:
    def __init__(self):
        self.__detector = ImageDetector()
        self.__censor = ImageCensor()
    
    def ImageProcess(self, images: list[str]):
        resultlist = []

        for image in images:
            result = self.__detector.DetectImages(image)
            resultlist.append(result)

        for r in resultlist:
            self.__censor.apply(r)