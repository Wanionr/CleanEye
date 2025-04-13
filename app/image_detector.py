from ultralytics import YOLO
from app.detect_result import DetectResult

#이미지를 감지할 YOLO 모델이 정의된 클래스스
class ImageDetector:
    def __init__(self):
        self.__model = YOLO("yolov8n.pt")
       #self.__confidence: float = 0.5
       # self.__idDict <- id를 label string으로 바꿀 dict가 들어감

    #이미지 url을 받아 감지후 결과를 DetectResult 리스트로 반환환
    def DetectImages(self, image: str) -> list[DetectResult]:
        detectresults = []
        results = self.__model(image)

        print(results[0].boxes.cls)
        print(results[0].boxes.xyxy)

        for box in results[0].boxes:
            detectresult = DetectResult(image,int(box.cls), box.xyxy.tolist() , 0.5)

            detectresults.append(detectresult)

        return detectresults