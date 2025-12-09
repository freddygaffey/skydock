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

    time_detected: int = field(default_factory=lambda: time.time_ns())
    # vector_to_center: Tuple[float, float] = field(init=False)  # computed after init

    # def __post_init__(self):
    #     self.vector_to_center = self.get_the_vector_center()

    def get_the_vector_center(self):
        cx = camera_prams.width / 2
        cy = camera_prams.height / 2

        bbx = (self.bbox[0][0] + self.bbox[1][0]) / 2
        bby = (self.bbox[0][1] + self.bbox[1][1]) / 2

        return (bbx - cx, bby - cy) 

@dataclass(frozen=True)
class Camera:
    x_dist_per_pix_per_meter: float = 0.0003792011843564136
    y_dist_per_pix_per_meter: float = 0.0005137066016141622
    fov_x: float = 27.4   # degrees
    fov_y: float = 21.0   # degrees
    width: int = 1280
    height: int = 720
    
class ai_storage():
    def __init__(self):
        self._lock = threading.Lock()
        self._app_thread = None
        self.detections = []
        self.current_frame = []
        self._ai_has_started = False

        # photo stuff
        self.take_photo = True
        self.time_last_photo_taken = round(time.time())
        self.rate_take_photo = 2 # sec
        self.palth_to_save_photo = "/home/fred/skydock/software/photos"

    def take_photo_function(self,palth):
        self.palth_to_save_photo = palth
        self.take_photo = True

    def photo_taken(self,photo_path):
        self.take_photo = False
        self.time_last_photo_taken = round(time.time())


    def photo_not_taken(self):
        if round(time.time()) % self.rate_take_photo == 0 and self.time_last_photo_taken != round(time.time()):
            self.take_photo = True
        self.time_last_photo_taken = round(time.time())
        
    def add_frame(self):
        with self._lock:
            if self.current_frame != []:
                self.detections.append(self.current_frame)
                self.current_frame = []

    def add_detection(self, label, confidence, bbox, track_id=None,photo_path=None):
        if photo_path is not "NO_PHOTO_TAKEN":
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
            self.current_frame.append(detection_data)

        return detection_data
    
    def get_last_frames(self,num_of_frames=1):
        with self._lock:
            if num_of_frames == -1:
                return self.detections.copy()
            # elif num_of_frames == 1:
            #     return self.detections[0].copy() # not give [[frame]]
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
        if not self._ai_has_started:
            self._app_thread.start()
            self._ai_has_started = True
        else:
            print("ai has allready started")


# ---- SINGLETON INSTANCES CREATED ONCE ----
ai_storage_singleton = ai_storage()
# ai_storage_singleton._ai_storage__start_ai()

camera_prams = Camera()



if __name__ == "__main__":
    from ai import ai_storage_singleton
    ai_storage_singleton.start_ai()
    while True:
        time.sleep(0.3)

        last_frames = ai_storage_singleton.get_last_frames(1)
        if not last_frames:
            print("is none")
            continue
        else:
            print(type(last_frames))
            for i in last_frames[0]:
                print(i)
                print("\n")
            print("-"*10)

        