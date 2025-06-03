import numpy as np
import cv2 as cv
from detect_result import DetectResultBox

class ImageCensor:
    def CensoringImage(self, img: np.ndarray, boxes: list[DetectResultBox], type: int):
        """
        censoring image

        Args:
            img(np.ndarray): image to censor
            boxes(list[DetectResultBox]): detect result box list
            type: image consor type(2: mosaic, 3: blur)

        Returns:
            np.ndarray: censored image
        """
        result_img = img.copy()

        if(img.shape[2] > img.shape[1]):
            strength = int(img.shape[2])
        else:
            strength = int(img.shape[1])
        
        if(type == 2):
            strength = int(strength / 30)

            for box in boxes:
                x_min, y_min, x_max, y_max = map(int, box.box)

                roi = img[y_min:y_max, x_min:x_max]

                censored_roi = self.__ImageMosaic(roi, strength)

                result_img[y_min:y_max, x_min:x_max] = censored_roi

            return result_img
        elif(type == 3):
            strength = int(strength / 10)

            if(strength % 2 == 0):
                strength += 1

            for box in boxes:
                x_min, y_min, x_max, y_max = map(int, box.box)

                roi = img[y_min:y_max, x_min:x_max]

                censored_roi = self.__ImageBlur(roi, (strength, strength))

                result_img[y_min:y_max, x_min:x_max] = censored_roi

            return result_img

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
    
    def __ImageBlur(self, roi: np.ndarray, blur_strength: tuple[int, int]):
        """
        주어진 원본 이미지의 일부분에 지정한 강도 만큼 블러 처리를 합니다.

        Args:
            roi: 블러 처리를 할 원본 이미지의 일부
            blur_strength: 블러 처리 강도, 반드시 (홀수 int, 홀수 int) 튜플을 받습니다.

        Returns:
            np.ndarray: censored_roi: 블러 처리된 roi
        """
        censored_roi = cv.GaussianBlur(roi, blur_strength, 0)

        return censored_roi