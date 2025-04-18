from dataclasses import dataclass
# 이미지 감지 결과를 저장
@dataclass
class DetectResultBox:
    label: int
    box: tuple[int, int, int, int]