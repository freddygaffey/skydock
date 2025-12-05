import os
import sys
import time

from drone_state_homing import drone_state 
from ai import ai_storage_singleton

dir_num = 0
ai_storage_singleton.start_ai()
while True:
    root_path = "/home/fred/skydock/software/do_calibration_cam/"

    alt = drone_state.altitude_rel_home

    photo_palth = root_path + "/alt = " + str(alt)

    ai_storage_singleton.take_photo_function(photo_palth)
    print(f"made a file kina {photo_palth}")
    time.sleep(2)



# import time
# import os

# from picamera2 import Picamera2

# from ai import ai_storage_singleton
# from drone import Telemetry

# if __name__ == "__main__":
#     ai_storage_singleton.start_ai()
#     drone = Telemetry()
 

#     # while True:
#     #     time.sleep(0.01)
#     #     print(ai_storage_singleton.get_last_frames())
#     #     print(drone.get_gimbal_attitude())
