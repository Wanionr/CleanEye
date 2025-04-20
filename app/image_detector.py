from ultralytics import YOLO
from numpy import ndarray
from detect_result import DetectResultBox

#이미지를 감지할 YOLO 모델이 정의된 클래스스
class ImageDetector:
    def __init__(self):
        self.__model = YOLO("yolov8n-seg.pt")
        self.__idDict = {"hello" : 3}

    #이미지 url을 받아 감지후 결과를 DetectResult 리스트로 반환환
    def DetectingImage(self, img: ndarray, confidence: float) -> list[DetectResultBox]:
        detectresults = []
        results = self.__model(img)

        for box in results[0].boxes:
            xyxy = box.xyxy.tolist()
            int_xyxy = [int(num) for num in xyxy[0]]

            detectresult = DetectResultBox(int(box.cls), tuple(int_xyxy))
            detectresults.append(detectresult)

        return detectresults