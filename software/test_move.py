import pymavlink
from pymavlink import mavutil
import math 
import numpy as np
import serial
# from get_weed_positon import find_gps_from_angle_and_gps

"""
This fill is to test the movement functions
"""


# uav_connection = mavutil.mavlink_connection("COM5")
uav_connection = mavutil.mavlink_connection('COM5')
uav_connection.wait_heartbeat()
print(f"Drone is connected at {uav_connection} ")


msg = uav_connection.recv_match
uav_connection.set_mode_auto()

