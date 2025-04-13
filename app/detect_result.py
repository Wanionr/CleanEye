from dataclasses import dataclass
# 이미지 감지 결과를 저장
@dataclass
class DetectResult:
    url: str
    label: int
    box: list[float, float, float, float]
    confidence: float