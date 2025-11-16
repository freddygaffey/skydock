import threading
import time

ai_storage_instance = None

class ai_storage():

    def __init__(self):
        self._lock = threading.Lock()
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
            print(f"Saved: {label} (conf: {confidence:.2f})", flush=True)
    
    def get_last_frames(self,num_of_frames=1):
        with self._lock:
            if num_of_frames == -1:
                return self.detections.copy()
            return self.detections[-num_of_frames:].copy()
    
    def start_ai(self):
        from hailo_apps.hailo_app_python.apps.detection.detection import (
            app_callback,
            user_app_callback_class,
            ai_storage
        )
        from hailo_apps.hailo_app_python.apps.detection.detection_pipeline import (
            GStreamerDetectionApp
        )
        
        
        user_data = user_app_callback_class()
        app = GStreamerDetectionApp(app_callback, user_data)
        
        app.run()
    

def get_ai_storage():
    global ai_storage_instance
    if ai_storage_instance is None:
        ai_storage_instance = ai_storage()
    return ai_storage_instance   

if __name__ == "__main__":
    ai = ai_storage()
    ai.start_ai()