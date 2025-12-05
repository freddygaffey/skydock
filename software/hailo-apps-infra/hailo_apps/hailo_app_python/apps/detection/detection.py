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
import os
import random
import time

# Local application-specific imports
import hailo
from hailo_apps.hailo_app_python.core.common.buffer_utils import get_caps_from_pad, get_numpy_from_buffer
from hailo_apps.hailo_app_python.core.gstreamer.gstreamer_app import app_callback_class
from hailo_apps.hailo_app_python.apps.detection.detection_pipeline import GStreamerDetectionApp
# endregion imports

from ai import ai_storage_singleton

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
import datetime

def app_callback(pad, info, user_data):
    TAKE_PHOTO = ai_storage_singleton.take_photo  # use the singleton flag

    buffer = info.get_buffer()
    if buffer is None:
        return Gst.PadProbeReturn.OK

    user_data.increment()

    # Get video caps
    format, width, height = get_caps_from_pad(pad)
    if not format or not width or not height:
        return Gst.PadProbeReturn.OK

    # Extract the frame
    frame = get_numpy_from_buffer(buffer, format, width, height)
    if frame is None:
        return Gst.PadProbeReturn.OK

    # Convert RGB → BGR for OpenCV
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Get detections
    roi = hailo.get_roi_from_buffer(buffer)
    detections = roi.get_objects_typed(hailo.HAILO_DETECTION)

    detection_labels = []

    # Draw all detections on the frame (human-readable style)
    for d in detections:
        label = d.get_label()
        confidence = d.get_confidence()
        bbox = d.get_bbox()
        detection_labels.append(label)

        # Convert bbox to pixel coordinates
        x1 = int(bbox.xmin() * width) if bbox.xmin() <= 1 else int(bbox.xmin())
        y1 = int(bbox.ymin() * height) if bbox.ymin() <= 1 else int(bbox.ymin())
        x2 = int(bbox.xmax() * width) if bbox.xmax() <= 1 else int(bbox.xmax())
        y2 = int(bbox.ymax() * height) if bbox.ymax() <= 1 else int(bbox.ymax())

        # Clamp to frame
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(width - 1, x2), min(height - 1, y2)

        # Human-readable colors and thickness
        box_color = (0, 165, 255)  # Orange (BGR)
        box_thickness = 1

        # Draw bounding box
        cv2.rectangle(frame_bgr, (x1, y1), (x2, y2), box_color, box_thickness)

        # Label + confidence
        text = f"{label} {confidence:.2f}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        font_thickness = 2
        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
        
        # Draw semi-transparent background for text
        overlay = frame_bgr.copy()
        cv2.rectangle(overlay, (x1, y1 - text_height - 10), (x1 + text_width + 6, y1), box_color, -1)
        alpha = 0.6  # transparency
        frame_bgr = cv2.addWeighted(overlay, alpha, frame_bgr, 1 - alpha, 0)

        # Draw text on top
        cv2.putText(frame_bgr, text, (x1 + 3, y1 - 5), font, font_scale, (255, 255, 255), font_thickness)

    # Ensure photos folder exists
    # photos_folder = "/home/fred/skydock/software/photos"
    photos_folder = ai_storage_singleton.palth_to_save_photo
    os.makedirs(photos_folder, exist_ok=True)

    # Build filename
    name_prefix = "_".join(detection_labels[:3]) if detection_labels else "none"  # first 3 detections
    now = datetime.datetime.now()
    timestamp = now.strftime("%H_%M_%S.%f")[:-3] + " " + now.strftime("%d-%m-%Y")
    filename = f"{name_prefix} {timestamp}.jpg"
    photo_path = f"{photos_folder}/{filename}"

    # Save the image with all detections
    if TAKE_PHOTO and detections:
        cv2.imwrite(photo_path, frame_bgr)
        # print("Photo taken:", photo_path)
    else:
        photo_path = None

    # Add all detections to ai_storage

    ai_storage_singleton.add_frame()
    time.sleep(0.001)
    for d in detections:
        box = d.get_bbox()

        x1 = box.xmin() if box.xmin() <= 1 else box.xmin() / width
        y1 = box.ymin() if box.ymin() <= 1 else box.ymin() / height
        x2 = box.xmax() if box.xmax() <= 1 else box.xmax() / width
        y2 = box.ymax() if box.ymax() <= 1 else box.ymax() / height

        # Clamp between 0 and 1
        x1 = min(max(x1, 0), 1)
        y1 = min(max(y1, 0), 1)
        x2 = min(max(x2, 0), 1)
        y2 = min(max(y2, 0), 1)

        ai_storage_singleton.add_detection(
            label=d.get_label(),
            confidence=d.get_confidence(),
            bbox=[(x1, y1), (x2, y2)],
            photo_path=photo_path,
        )


    return Gst.PadProbeReturn.OK

if __name__ == "__main__":
    user_data = user_app_callback_class()

    user_data.use_frame = True

    app = GStreamerDetectionApp(app_callback, user_data)
    app.run()
