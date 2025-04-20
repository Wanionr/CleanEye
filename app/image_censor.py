import numpy as np
import cv2 as cv
from detect_result import DetectResultBox

class ImageCensor:
    def CensoringImage(self, img: np.ndarray, boxes: list[DetectResultBox]):
        """
        주어진 이미지와 좌표 박스에 검열 처리를 합니다.

        Args:
            img(np.ndarray): 검열 작업이 필요한 이미지
            boxes(list[DetectResultBox]): 이미지에서 감지된 부적절한 부분의 좌표 박스 리스트

        Returns:
            np.ndarray: 검열 처리된 이미지지
        """
        result_img = img.copy()
        strength = (5, 5)

        for box in boxes:
            x_min, y_min, x_max, y_max = map(int, box.box)

            roi = img[y_min:y_max, x_min:x_max]

            # censored_roi = self.__ImageBlur(roi, strength)
            censored_roi = self.__ImageMosaic(roi, 5)

            result_img[y_min:y_max, x_min:x_max] = censored_roi

        return result_img
    
    def __ImageBlur(self, roi: np.ndarray, blur_strength: tuple[int, int]):
        """
        주어진 원본 이미지의 일부분에 지정한 강도 만큼 블러 처리를 합니다.

        Args:
            roi: 블러 처리를 할 원본 이미지의 일부
            blur_strength: 블러 처리 강도

        Returns:
            np.ndarray: censored_roi: 블러 처리된 roi
        """
        censored_roi = cv.GaussianBlur(roi, blur_strength, 0)

        return censored_roi
    
    def __ImageMosaic(self, roi: np.ndarray, block_size: int):
        censored_roi = roi.copy()

        height, width, _ = censored_roi.shape

        row_array = np.arange(0, height - width % block_size, block_size)
        col_array = np.arange(0, width - width % block_size, block_size)

        for y in row_array:
            for x in col_array:
                block = censored_roi[y:y + block_size, x:x + block_size]

                avg_color = np.mean(block, axis=(0,1)).astype(censored_roi.dtype)

                censored_roi[y:y + block_size, x:x + block_size] = avg_color

        return censored_roi