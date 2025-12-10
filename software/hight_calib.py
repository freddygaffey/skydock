import os
import sys
import time

from software.drone_snapshots import drone_telm_stapshot 
from telemetry import telm_singleton
from ai import ai_storage_singleton

dir_num = 0
ai_storage_singleton.start_ai()
telm_singleton.start_automatic_updates_homing
while True:
    root_path = "/home/fred/skydock/software/do_calibration_cam/"

    alt = drone_telm_stapshot.altitude_rel_home
    alt = round(alt,0)

    photo_palth = root_path + "alt = " + str(alt)

    ai_storage_singleton.take_photo_function(photo_palth)
    time.sleep(2)
