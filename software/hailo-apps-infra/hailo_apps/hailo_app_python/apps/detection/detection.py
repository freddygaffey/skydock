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
import threading

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
    TAKE_PHOTO = ai_storage_singleton.take_photo
    TAKE_PHOTO = True
    PHOTO_PALTH = ai_storage_singleton.palth_to_save_photo
    if not TAKE_PHOTO:
        PHOTO_PALTH = "NO_PHOTO_TAKEN"

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


    # Get detections
    roi = hailo.get_roi_from_buffer(buffer)
    detections = roi.get_objects_typed(hailo.HAILO_DETECTION)

    ai_storage_singleton.add_frame()
    frame_arr_objects = []
    for d in detections:
        box = d.get_bbox()

        x1 = box.xmin() * width
        y1 = box.ymin() * height
        x2 = box.xmax() * width
        y2 = box.ymax() * height

        detct = ai_storage_singleton.add_detection(
            label=d.get_label(),
            confidence=d.get_confidence(),
            bbox=[(x1, y1), (x2, y2)],
            photo_path=PHOTO_PALTH,
        )
        frame_arr_objects.append(detct)

    if TAKE_PHOTO:
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        save_image(PHOTO_PALTH,frame_bgr,frame_arr_objects)

    return Gst.PadProbeReturn.OK

# def save_image(palth,image_bgr, frame_array, box_color = (0, 165, 255),box_thickness = 1):
#     def save_image_to_be_threaded(palth,image_bgr):
#         pass

def save_image(folder, image_bgr, frame_array,
               box_color=(255,0,0), box_thickness=2):
    print(frame_array)
    # --- Build filename (cheap) ---
    detection_labels = [det.label for det in frame_array]
    name_prefix = "_".join(detection_labels[:3]) if detection_labels else "none"

    now = datetime.datetime.now()
    timestamp = now.strftime("%H_%M_%S.%f")[:-3] + " " + now.strftime("%d-%m-%Y")

    filename = f"{name_prefix} {timestamp}.jpg"
    photo_path = f"{folder}/{filename}"

    # --- THREAD WORK ---
    def worker(path, img_bgr, frame_array):
        img = img_bgr.copy()  # minimal required copy (thread-safe)

        for det in frame_array:
            (x1, y1), (x2, y2) = det.bbox
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Draw rectangle
            cv2.rectangle(img, (x1, y1), (x2, y2),
                        box_color, box_thickness, lineType=cv2.LINE_8)

            # Build label
            label_text = f"{det.label} {det.confidence:.2f}"

            # Move text slightly inside the box
            text_y = y1 + 15  # 15 pixels below top of box
            text_x = max(x1, 4)  # prevent left overflow

            cv2.putText(img, label_text, (text_x, text_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        box_color, 1, lineType=cv2.LINE_8)

        # Ensure folder exists (cheap)
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
        except:
            pass

        cv2.imwrite(path, img)

    # --- Launch thread ---
    threading.Thread(
        target=worker,
        args=(photo_path, image_bgr, frame_array),
        daemon=True
    ).start()

    return photo_path

if __name__ == "__main__":
    user_data = user_app_callback_class()

    user_data.use_frame = True

    app = GStreamerDetectionApp(app_callback, user_data)
    app.run()
