
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

@dataclass
class Detection():
    label: str 
    confidence: float
    bbox: List[Tuple[float, float]]
    track_id: Optional[int] = None
    photo_path: Optional[str] = None

    time_detected: int = field(default_factory=lambda: time.time_ns())
    # vector_to_center: Tuple[float, float] = field(init=False)  # computed after init

    # def __post_init__(self):
    #     self.vector_to_center = self.get_the_vector_center()

    def get_the_vector_center(self):
        cx = Camera.width / 2
        cy = Camera.height / 2

        bbx = (self.bbox[0][0] + self.bbox[1][0]) / 2
        bby = (self.bbox[0][1] + self.bbox[1][1]) / 2

        return (bbx - cx, bby - cy) 