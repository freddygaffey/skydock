from pymavlink import mavutil
from telemetry import Telemetry
from telemetry import telm_singleton

# path_to_uav = "/dev/rcfomm0"
# connection = mavutil.mavlink_connection(path_to_uav, baud=115200)
while True:
    telm_singleton.print_all_msg()
    # imput_str = input("question to send to GC from drone ")
    # telm_singleton.send_text_message(imput_str)
