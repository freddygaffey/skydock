import pymavlink
from pymavlink import mavutil
import math 
import numpy as np
from scipy.spatial.transform import Rotation as R # this is needed for the q


 
# I found the videos from Intelligent Quads helpfull 
# https://www.youtube.com/watch?v=kecnaxlUiTY
# https://www.youtube.com/watch?v=6M7e7DDLTQc
# https://www.youtube.com/watch?v=NTjEcHmqmu4

# multi threading 
# https://www.youtube.com/watch?v=STEOavXqXkQ

class Drone_mvp():
    """this is a drone mvp will be renamed later to Drone"""
    
    """for  quaternions I will use the [x, y, z, w] this is the convetoin for sicpy"""
    
    def __init__(self):
        self.battery_capacity = 4800 # in mah
        path_to_uav = "/dev/ttyACM1"
        self.connection = mavutil.mavlink_connection(path_to_uav, baud=115200)
        self.connection.wait_heartbeat()
        
        # defing what command to stream
        self.set_a_message_interval("BATTERY_STATUS",interval=1)
        # self.set_a_message_interval("GPS_RAW_INT",interval=10)
        # self.set_a_message_interval("SYS_STATUS",interval=20)
        self.set_a_message_interval("GIMBAL_DEVICE_ATTITUDE_STATUS",interval=0.25)
        self.set_a_message_interval("ATTITUDE_QUATERNION",interval=0.25)

        
        # this will stream the rc chanels thay are speshal
        self.connection.mav.request_data_stream_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_DATA_STREAM_RC_CHANNELS,  # stream for RC messages
            2,  # Hz
            1)    # start streaming
        
    def update():
        self.batt_v = self.get_batt_v()
        self.gimbal_attitude = self.get_gimbal_attitude()
        self.batt_mah_left = self.get_batt_mah_left()
        
    
    
    def get_gimbal_attitude(self):
        """this uses QUETONIONS so BEWHERE"""
        # TODO: check if this is the correct global q
        
        q_cam = None 
        q_drone = None
        while True:
            msg = self.connection.recv_msg()  
            if msg is not None:
                msg = msg.to_dict()
                if msg["mavpackettype"] == "GIMBAL_DEVICE_ATTITUDE_STATUS":
                    q_cam = (msg["q"])
                elif msg["mavpackettype"] == "ATTITUDE_QUATERNION":
                    q_drone = (msg['q1'], msg['q2'], msg['q3'],msg['q4'])  # [x, y, z,w]
                if q_cam != None and q_drone != None:
                    # convert to a rotaion matrix 
                    r_drone = R.from_quat(q_drone)
                    r_cam = R.from_quat(q_cam)

                    # work out global camera orientation
                    r_global = r_drone * r_cam

                    # Convert back to quaternion [w, x, y, z]
                    q_global = r_global.as_quat()
                    return q_global
            
    def get_batt_v(self):
        """this code works by converitng the msg to a dict then filtering"""
        while True:
            msg = self.connection.recv_msg()  
            if msg is not None:
                msg = msg.to_dict()
                if msg["mavpackettype"] == "BATTERY_STATUS":
                    return msg["voltages"][0]/1000

    def get_batt_mah_left(self):
        """this code works by converitng the msg to a dict then filtering"""
        while True:
            msg = self.connection.recv_msg()  
            if msg is not None:
                msg = msg.to_dict()
                if msg["mavpackettype"] == "BATTERY_STATUS":
                    return self.battery_capacity - msg["current_consumed"]

                
   
    def set_a_message_interval(self,message_name,interval=1):
        """interval in sec"""
        # https://mavlink.io/en/mavgen_python/howto_requestmessages.html
        interval *= 1000000
        message = self.connection.mav.command_long_encode(
            self.connection.target_system,  # Target system ID
            self.connection.target_component,  # Target component ID
            mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,  # ID of command to send
            0,  # Confirmation
            eval(f"mavutil.mavlink.MAVLINK_MSG_ID_{message_name}"),  # param1: Message ID to be streamed
            interval, # param2: Interval in microseconds
            0,0,0,0,0)

        # Send the COMMAND_LONG
        self.connection.mav.send(message)
        string_to_print = "set " + message_name + " to repeat every: " + str(interval/1000000) + " seconds"
        print(string_to_print)

class See():
    """this is a class of what the cammera sees"""

    """see_input_dict = {
        "gps_poss":(x,y,z),
        "gps_num_of_sats": int(NUM),
        "q_cam_rel_global": [x, y, z, w],
        "ai_dict": SEE BELOW
        
        }"""
    
    """ai_dict {
        "0": {
            bbox: (top_left, bottom_right),
            object: "name_of_thing_found",
            confidence: float
        }
        
        "1": {
            bbox: (top_left, bottom_right),
            object: "name_of_thing_found",
            confidence: float
        }
    }"""

    
    def __init__(self,see_input_dict):
        
        # gps_poss, gps_num_of_sats, gimbel_angle, ai_dict
        # this setup allow easer passing of files 
        
                