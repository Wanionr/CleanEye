import numpy as np
import cv2 as cv
import requests
import os
from image_detector import ImageDetector
from image_censor import ImageCensor
from utils import SERVER_URL
from urllib.parse import urljoin, urlparse

IMAGE_SAVE_DIR = "/app/static/censored_images"

class ImageProcessor:
    def __init__(self):
        self.__detector = ImageDetector()
        self.__censor = ImageCensor()
    
    def ImageProcess(self, image_url: str, rate: int, type: int):
        img = self.ImageURLtoNdarray(image_url)

        if img is None:
            return None

        detect_result = self.__detector.DetectingImage(img, rate)

        if(detect_result):
            if type == 1:
                return image_url

            print("image censoring...")

            censored_img = self.__censor.CensoringImage(img, detect_result, type)

            # 원본 URL에서 파일 이름 추출 및 변경
            parsed_url = urlparse(image_url)
            filename_base = os.path.splitext(os.path.basename(parsed_url.path))[0]
            filename = f"censored_{filename_base}.png"
            filepath = os.path.join(IMAGE_SAVE_DIR, filename)

            # 이미지 파일로 저장
            cv.imwrite(filepath, censored_img)
            # 접근 가능한 URL 생성
            censored_url = urljoin(SERVER_URL, f"/static/censored_images/{filename}")
        else:
            return None

        return censored_url

    
    def ImageURLtoNdarray(self, image_url: str) -> np.ndarray:
        img_ndarray = None

        try:
            img_response = requests.get(image_url)

            img_array = np.asarray(bytearray(img_response.content), dtype=np.uint8)
            img_ndarray = cv.imdecode(img_array, cv.IMREAD_COLOR)
        except requests.exceptions.RequestException as e:
            print("=====Failed to download image=====\n"
                  f"image url: {image_url}\n"
                  f"{e}")

        print("img translate done")

        return img_ndarray