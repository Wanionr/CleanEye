from ultralytics import YOLO
from numpy import ndarray
from detect_result import DetectResultBox

#이미지를 감지할 YOLO 모델이 정의된 클래스
class ImageDetector:
    __nsfw_model = YOLO("./model/model_250531.pt")

    #이미지 url을 받아 감지후 결과를 DetectResult 리스트로 반환
    def DetectingImage(self, img: ndarray, rate: int) -> list[DetectResultBox]:
        detectresults = []

        detect_grade = self.__MakeDetectGrade(rate)

        results = ImageDetector.__nsfw_model(img)

        if results and len(results) > 0:
            for box in results[0].boxes:
                print(f"result added {box.cls}:\n"
                              f"{box.xyxy}")
                if int(box.cls) in detect_grade:
                    bounding_box: list[float] = box.xyxy.tolist()[0]
                    if len(bounding_box) == 4:
                        int_bounding_box: tuple[int, int, int, int] = tuple(int(num) for num in bounding_box)
                        detectresult = DetectResultBox(int(box.cls), int_bounding_box)
                        detectresults.append(detectresult)
                        print("resutl added")
                    else:
                        print(f"Warning: Bounding box has incorrect size ({len(bounding_box)}). Skipping.")
                        print(f"Bounding box value: {bounding_box}")


        return detectresults
    
    def __MakeDetectGrade(self, rate: int):

        if rate == 100:
            grade = [n for n in range (0, 14)]
        elif(rate > 50):
            grade = [n for n in range(6, 14)]
        elif(rate > 1):
            grade = [n for n in range(10, 14)]
        else:
            grade = []

        return grade