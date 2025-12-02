from dataclasses import dataclass, field
from typing import List, Tuple, Optional
import time
import threading


@dataclass
class Detection():
    label: str 
    confidence: float
    bbox: List[Tuple[float, float]]
    track_id: Optional[int] = None
    photo_path: Optional[str] = None

    time: int = field(default_factory=lambda: time.time_ns())
    vector_to_center: Tuple[float, float] = field(init=False)  # computed after init

    def __post_init__(self):
        self.vector_to_center = self.get_the_vector_center()

    def get_the_vector_center(self):
        center_tuple = (0.5,0.5)
        (cx,cy)  = center_tuple

        center_of_bb = ((self.bbox[0][0] + self.bbox[1][0])/2 , (self.bbox[0][1] + self.bbox[1][1])/2) # this takes ave x and ave y 
        (bbx, bby) = center_of_bb

        dx = cx - bbx
        dy = cy - bby

        mag = (dx**2 + dy**2)**0.5 # this is finding the mag with pythag 
        if mag == 0:
            return (0, 0)
        
        vector = (dx /mag, dy /mag)
        return vector

@dataclass(frozen=True)
class Camera:
    fov_x = 27.4
    fov_y = 21.0
    
class ai_storage():
    def __init__(self):
        self._lock = threading.Lock()
        self._app_thread = None
        self.detections = []

        # photo stuff
        self.take_photo = True
        self.__photo_not_taken = 0
        self.time_last_photo_taken = round(time.time())
        self.rate_take_photo = 8 # sec

    def photo_taken(self,photo_path):
            self.take_photo = False

    def photo_not_taken(self):
        if round(time.time()) % self.rate_take_photo == 0 and self.time_last_photo_taken != round(time.time()):
            self.take_photo = True
        self.time_last_photo_taken = round(time.time())

    def add_detection(self, label, confidence, bbox, track_id=None,photo_path=None):
        if photo_path is not None:
            self.photo_taken(photo_path)
        else:
            self.photo_not_taken()
        
        detection_data = Detection(
            label=label,
            confidence=confidence,
            bbox=bbox,
            track_id=track_id,
            photo_path=photo_path
        )

        with self._lock:
            self.detections.append(detection_data)
    
    def get_last_frames(self,num_of_frames=1):
        with self._lock:
            if num_of_frames == -1:
                return self.detections.copy()
            elif num_of_frames == 1:
                return self.detections[-num_of_frames:].copy()[0] # not give [[frame]]
            return self.detections[-num_of_frames:].copy()
    
    def start_ai(self):
        from hailo_apps.hailo_app_python.apps.detection.detection import (
            app_callback,
            user_app_callback_class
        )
        from hailo_apps.hailo_app_python.apps.detection.detection_pipeline import (
            GStreamerDetectionApp
        )
        user_data = user_app_callback_class()
        app = GStreamerDetectionApp(app_callback, user_data)

        self._app_thread = threading.Thread(
            target=app.run,
            daemon=True           # allow program to exit even if thread is running
        )
        self._app_thread.start()


# ---- SINGLETON INSTANCES CREATED ONCE ----
ai_storage_singleton = ai_storage()
camera_prams = Camera()


if __name__ == "__main__":
    from ai import ai_storage_singleton
    ai_storage_singleton.start_ai()
    while True:
        time.sleep(0.3)

        last_frames = ai_storage_singleton.get_last_frames(1)
        # print(last_frames)
        if last_frames:
            print(last_frames[0].vector_to_center)
            print(last_frames[0].label,"^^^")
            print("\n")
        else:
            print("No detections yet")

        # print(ai_storage_singleton.get_last_frames(1)[0].vector_to_center)

