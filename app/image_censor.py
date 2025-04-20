import numpy as np
import cv2 as cv
from detect_result import DetectResultBox

class ImageCensor:
    def CensoringImage(self, img: np.ndarray, boxes: list[DetectResultBox]):
        """주어진 이미지와 좌표 박스에 검열 처리를 합니다.

        Args:
            img(np.ndarray): 검열 작업이 필요한 이미지
            boxes(list[DetectResultBox]): 이미지에서 감지된 부적절한 부분의 좌표 박스 리스트

        Returns:
            np.ndarray: 
        
        """
        result_img = img.copy()
        strength = (5, 5)
        for box in boxes:
            x_min, y_min, x_max, y_max = map(int, box.box)
            roi = img[y_min:y_max, x_min:x_max]
            censored_roi = self.__ImageBlur(roi, strength)
            result_img[y_min:y_max, x_min:x_max] = censored_roi

        return result_img
    
    def __ImageBlur(self, roi: np.ndarray, blur_strength: tuple[int, int]):
        censored_roi = cv.GaussianBlur(roi, blur_strength, 0)

        return censored_roi