import threading
import time

        # ai_storage_singleton.photo_taken(photo_path)

class ai_storage():
    def __init__(self):
        self._lock = threading.Lock()
        self._app_thread = None
        self.detections = []
        self.take_photo = True
        self.__photo_not_taken = 0
        self.time_last_photo_taken = round(time.time())
        self.rate_take_photo = 1 # sec

    def photo_taken(self,photo_path):
            self.take_photo = False

    def photo_not_taken(self):
        if round(time.time()) % self.rate_take_photo == 0 and self.time_last_photo_taken != round(time.time()):
            self.take_photo = True
        self.time_last_photo_taken = round(time.time())
        
        pass
    #     self.__photo_not_taken +=1
    #     if self.__photo_not_taken > 10:
    #         self.take_photo = True 
        
        # logic around when to take photos


    def add_detection(self, label, confidence, bbox, track_id=None,photo_path=None):
        if photo_path is not None:
            self.photo_taken(photo_path)
        else:
            self.photo_not_taken()

        detection_data = {
            'label': label,
            'confidence': float(confidence),
            'bbox': bbox,
            'track_id': track_id,
            'time' : time.time_ns(),
            'photo_path': photo_path
            }

        with self._lock:
            self.detections.append(detection_data)
            # print(detection_data, flush=True)
            # print("this is from the add detections")
            # print(f"Saved: {label} (conf: {confidence:.2f})", flush=True)
    
    def get_last_frames(self,num_of_frames=1):
        with self._lock:
            if num_of_frames == -1:
                return self.detections.copy()
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


# ---- SINGLETON INSTANCE CREATED ONCE ----
ai_storage_singleton = ai_storage()


if __name__ == "__main__":
    from ai import ai_storage_singleton
    ai_storage_singleton.start_ai()
    while True:
        time.sleep(0.1)

        print(ai_storage_singleton.get_last_frames(1))

