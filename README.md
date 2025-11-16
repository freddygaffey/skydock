# SkyDock
SkyDock - is an autonomous VTOL aircraft powered by ArduPilot, designed for low-altitude, long-range missions. It features a 6 km range at 2 meters above ground, a laser for simulated object tracking, autonomous recharging, and chemical refilling simulation.

git clone https://github.com/hailo-ai/hailo-apps-infra.git

replace the contence of /home/fred/skydock/software/hailo-apps-infra/hailo_apps/hailo_app_python/apps/detection/detection.py

and replace it with 
```
import sys
from pathlib import Path
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
import hailo
from hailo_apps.hailo_app_python.core.gstreamer.gstreamer_app import app_callback_class
from hailo_apps.hailo_app_python.apps.detection.detection_pipeline import GStreamerDetectionApp

# Import ai storage
project_root = Path(__file__).parent.parent.parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
from ai import get_ai_storage

ai_storage = get_ai_storage()


class user_app_callback_class(app_callback_class):
    def __init__(self):
        super().__init__()


def app_callback(pad, info, user_data):
    buffer = info.get_buffer()
    if buffer is None:
        return Gst.PadProbeReturn.OK

    user_data.increment()
    frame_number = user_data.get_count()

    # Get detections
    roi = hailo.get_roi_from_buffer(buffer)
    detections = roi.get_objects_typed(hailo.HAILO_DETECTION)

    # Save each detection to ai_storage
    for detection in detections:
        label = detection.get_label()
        bbox = detection.get_bbox()
        confidence = detection.get_confidence()
        
        track_id = None
        track = detection.get_objects_typed(hailo.HAILO_UNIQUE_ID)
        if len(track) == 1:
            track_id = track[0].get_id()
        
        ai_storage.add_detection(
            label=label,
            confidence=confidence,
            bbox=bbox,
            track_id=track_id,
        )

    return Gst.PadProbeReturn.OK


if __name__ == "__main__":
    user_data = user_app_callback_class()
    app = GStreamerDetectionApp(app_callback, user_data)
    app.run()
```

change software/hailo-apps-infra/hailo_apps/hailo_app_python/core/common/core.py line 96 to 
```
"--input", "-i", type=str, default="rpi",
```
??? comment out the usesages of setproctitle

use the ./install.sh to make the venv