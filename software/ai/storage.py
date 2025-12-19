import time
import threading
from .camera import Camera
from .detection import Detection

class ai_storage():
    def __init__(self):
        self._lock = threading.Lock()
        self._app_thread = None
        self.all_frames = []
        self.current_frame = []
        self._ai_has_started = False

        # photo stuff
        self.take_photo = True
        self.time_last_photo_taken = round(time.time())
        self.rate_take_photo = 1000000000000 # sec
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
                self.all_frames.append(self.current_frame)
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
            if num_of_frames == False:
                return self.all_frames.copy()
            # elif num_of_frames == 1:
            #     return self.detections[0].copy() # not give [[frame]]
            return self.all_frames[-num_of_frames:].copy()

    def get_frames_in_time_period(self,more_past,less_past=None):
        # TODO: make faster 
        if not less_past:
            less_past = time.time_ns()
        with self._lock:
            all_frames = self.all_frames.copy()
        frames_to_return = []
        for i in all_frames:
            if i.time_detected >= more_past and i.time_detected <= less_past:
                frames_to_return.append(i)

    def start_ai(self):
        from .hailo_apps.hailo_app_python.apps.detection.detection import (
            app_callback,
            user_app_callback_class
        )
        from .hailo_apps.hailo_app_python.apps.detection.detection_pipeline import (
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
    # from ai import ai_storage_singleton
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

        