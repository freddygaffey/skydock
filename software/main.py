
import time
import os

from picamera2 import Picamera2

from ai import ai_storage_singleton
from drone import Telemetry

if __name__ == "__main__":
    ai_storage_singleton.start_ai()
    drone = Telemetry()
 

    while True:
        time.sleep(0.01)
        print(ai_storage_singleton.get_last_frames())
        print(drone.get_gimbal_attitude())


        
        