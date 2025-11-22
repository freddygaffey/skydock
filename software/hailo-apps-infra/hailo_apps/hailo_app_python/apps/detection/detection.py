# import sys
# from pathlib import Path
# import gi
# gi.require_version('Gst', '1.0')
# from gi.repository import Gst
# import hailo
# from hailo_apps.hailo_app_python.core.gstreamer.gstreamer_app import app_callback_class
# from hailo_apps.hailo_app_python.apps.detection.detection_pipeline import GStreamerDetectionApp


# from hailo_apps.hailo_app_python.core.common.buffer_utils import (
#     get_numpy_from_buffer,
# )

# # Import ai storage
# project_root = Path(__file__).parent.parent.parent.parent.parent
# if str(project_root) not in sys.path:
#     sys.path.insert(0, str(project_root))

# from ai import ai_storage_singleton

# ai_storage = ai_storage_singleton


# class user_app_callback_class(app_callback_class):
#     def __init__(self):
#         super().__init__()


# def app_callback(pad, info, user_data):
#     buffer = info.get_buffer()
#     if buffer is None:
#         return Gst.PadProbeReturn.OK

#     user_data.increment()
#     frame_number = user_data.get_count()

#     frame = get_numpy_from_buffer(buffer, format, width, height)
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert from BGR to RGB
#     print(frame)
#     # Get detections
#     roi = hailo.get_roi_from_buffer(buffer)
#     detections = roi.get_objects_typed(hailo.HAILO_DETECTION)

#     # Save each detection to ai_storage
#     for detection in detections:
#         label = detection.get_label()
#         bbox = detection.get_bbox()
#         confidence = detection.get_confidence()
        
#         track_id = None
#         track = detection.get_objects_typed(hailo.HAILO_UNIQUE_ID)
#         if len(track) == 1:
#             track_id = track[0].get_id()
        
#         ai_storage.add_detection(
#             label=label,
#             confidence=confidence,
#             bbox=bbox,
#             track_id=track_id,
#         )

#     return Gst.PadProbeReturn.OK


# if __name__ == "__main__":
#     user_data = user_app_callback_class()
#     app = GStreamerDetectionApp(app_callback, user_data)
#     app.run()


# -----------------------------------------------
# region imports
# Standard library imports

# Third-party imports
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
import cv2

# Local application-specific imports
import hailo
from hailo_apps.hailo_app_python.core.common.buffer_utils import get_caps_from_pad, get_numpy_from_buffer
from hailo_apps.hailo_app_python.core.gstreamer.gstreamer_app import app_callback_class
from hailo_apps.hailo_app_python.apps.detection.detection_pipeline import GStreamerDetectionApp
# endregion imports

from ai import ai_storage_singleton

ai_storage = ai_storage_singleton
# -----------------------------------------------------------------------------------------------
# User-defined class to be used in the callback function
# -----------------------------------------------------------------------------------------------
# Inheritance from the app_callback_class
class user_app_callback_class(app_callback_class):
    def __init__(self):
        super().__init__()
        
# -----------------------------------------------------------------------------------------------
# User-defined callback function
# -----------------------------------------------------------------------------------------------

# This is the callback function that will be called when data is available from the pipeline
def app_callback(pad, info, user_data):
    # Get the GstBuffer from the probe info
    buffer = info.get_buffer()
    # Check if the buffer is valid
    if buffer is None:
        return Gst.PadProbeReturn.OK

    # Using the user_data to count the number of frames
    user_data.increment()
    string_to_print = f"Frame count: {user_data.get_count()}\n"

    # Get the caps from the pad
    format, width, height = get_caps_from_pad(pad)

    # If the user_data.use_frame is set to True, we can get the video frame from the buffer
    frame = None
    if user_data.use_frame and format is not None and width is not None and height is not None:
        # Get video frame
        frame = get_numpy_from_buffer(buffer, format, width, height)

    # Get the detections from the buffer
    roi = hailo.get_roi_from_buffer(buffer)
    detections = roi.get_objects_typed(hailo.HAILO_DETECTION)

    # Parse the detections
    detection_count = 0
    for detection in detections:
        label = detection.get_label()
        bbox = detection.get_bbox()
        confidence = detection.get_confidence()
        
        ai_storage.add_detection(
            label=label,
            confidence=confidence,
            bbox=bbox,
        )

    if user_data.use_frame:
        # Note: using imshow will not work here, as the callback function is not running in the main thread
        # Let's print the detection count to the frame
        # cv2.putText(frame, f"Detections: {detection_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Example of how to use the new_variable and new_function from the user_data
        # Let's print the new_variable and the result of the new_function to the frame
            # cv2.putText(frame, f"{user_data.new_function()} {user_data.new_variable}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Convert the frame to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        user_data.set_frame(frame)
        cv2.imwrite("frame.jpg", frame)
        with file = open("name.file","w"):
            file.write(frame)

    print(string_to_print)
    return Gst.PadProbeReturn.OK

if __name__ == "__main__":
    # Create an instance of the user app callback class
    user_data = user_app_callback_class()
    app = GStreamerDetectionApp(app_callback, user_data)
    app.run()
