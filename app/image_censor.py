#from app.detect_result import DetectResult

class ImageCensor:
    def apply(self, image):
        for l in image:
            print(l.url)
            print(l.label)
            print(l.box)