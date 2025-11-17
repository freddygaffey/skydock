import threading
import time


class ai_storage():
    def __init__(self):
        self._lock = threading.Lock()
        self._app_thread = None

        self.detections = []

    def add_detection(self, label, confidence, bbox, track_id=None):
        detection_data = {
            'label': label,
            'confidence': float(confidence),
            'bbox': bbox,
            'track_id': track_id,
            'time' : time.time_ns()
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
ai_storage_instance = ai_storage()


if __name__ == "__main__":
    from ai import ai_storage_instance
    ai_storage_instance.start_ai()
    while True:
        # print(ai.__dict__)
        # print(ai.detections)
        # print(ai.get_last_frames(-1))
        # print("this is from main")
        time.sleep(0.2)

        print(ai_storage_instance.get_last_frames(5))
        