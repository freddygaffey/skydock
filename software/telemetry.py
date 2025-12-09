import pymavlink
from pymavlink import mavutil
import math 
import numpy as np
from scipy.spatial.transform import Rotation as R # this is needed for the q

import threading
import time
from drone_state_homing import drone_state
import serial

 
# I found the videos from Intelligent Quads helpfull 
# https://www.youtube.com/watch?v=kecnaxlUiTY
# https://www.youtube.com/watch?v=6M7e7DDLTQc
# https://www.youtube.com/watch?v=NTjEcHmqmu4

# multi threading 
# https://www.youtube.com/watch?v=STEOavXqXkQ

class Telemetry():
    
    """for  quaternions I will use the [x, y, z, w] this is the convetoin for sicpy"""
    
    def __init__(self):
        self.battery_capacity = 4800 # in mah
        path_to_uav = "/dev/ttyACM0"
        self.connection = mavutil.mavlink_connection(path_to_uav, baud=115200)
        self.connection.wait_heartbeat()

        
        # defing what command to stream
        # self.set_a_message_interval("BATTERY_STATUS",interval=1)
        # self.set_a_message_interval("GLOBAL_POSITION_INT",interval=self.update_rate)
        # self.set_a_message_interval("SYS_STATUS",interval=self.update_rate)
        # self.set_a_message_interval("GIMBAL_DEVICE_ATTITUDE_STATUS",interval=self.update_rate)
        # self.set_a_message_interval("ATTITUDE_QUATERNION",interval=self.update_rate)
        # self.set_a_message_interval("SERVO_OUTPUT_RAW",interval=self.update_rate)

        self.update_rate = 1/10 # slightly hight then the ai frame rate 

        self.set_a_message_interval("SERVO_OUTPUT_RAW",interval=self.update_rate)
        self.set_a_message_interval("GLOBAL_POSITION_INT",interval=self.update_rate)
        
        # this will stream the rc chanels thay are speshal
        # self.connection.mav.request_data_stream_send(
        #     self.connection.target_system,
        #     self.connection.target_component,
        #     mavutil.mavlink.MAV_DATA_STREAM_RC_CHANNELS,  # stream for RC messages
        #     2,  # Hz
        #     1)    # start streaming

        self.start_automatic_updates()



    def update(self):
        pass
        # self.batt_v = self.get_batt_v()
        # self.gimbal_attitude = self.get_gimbal_attitude()
        # self.batt_mah_left = self.get_batt_mah_left()
        # self.num_of_sats = self.get_num_of_sats()
        # self.poss = self.get_poss()
        
    def start_automatic_updates(self):
        def update():
            while True:
                try:
                    drone_state.pass_msg(self.connection.recv_msg())
                except serial.SerialException:
                    pass
                
                time.sleep(self.update_rate/1.99)
        threading.Thread(target=update).start()
        # threading.Thread(target=update,daemon=True).start()

    def print_all_msg(self,duration=100):
        start_time = time.time()
        # while time.time() < (start_time + time.time()):
        while 1:
            # msg = self.connection.recv_match(type="RC_CHANNELS", blocking=True)
            msg = self.connection.recv_msg()
            if msg:
                # print(msg)
                print(msg)
                # if msg._type == "GLOBAL_POSITION_INT":
                #     print("true")


    def get_gimbal_attitude(self):
        """this uses QUETONIONS so BEWHERE"""
        # TODO: check if this is the correct global q
        
        q_cam = None 
        q_drone = None
        while True:
            # set cam atatrud real to dreon 
            msg = self.connection.recv_match(type="GIMBAL_DEVICE_ATTITUDE_STATUS", blocking=True).to_dict()
            q_cam = (msg["q"])
            q_cam = (q_cam[1],q_cam[2],q_cam[3],q_cam[0]) # [x, y, z, w]
                        
            # set drone atatude rel to the global
            msg = self.connection.recv_match(type="ATTITUDE_QUATERNION", blocking=True).to_dict()
            q_drone = (msg['q2'], msg['q3'], msg['q4'], msg['q1'])  # [x, y, z, w]
            
            
            # ----- fancy math stuff to get cam rel to ground ----
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
        msg = self.connection.recv_match(type="BATTERY_STATUS", blocking=True)
        msg = msg.to_dict()
        if msg["mavpackettype"] == "BATTERY_STATUS":
            return msg["voltages"][0]/1000

    def get_batt_mah_left(self):        
        msg = self.connection.recv_match(type="BATTERY_STATUS", blocking=True)
        msg = msg.to_dict()
        return self.battery_capacity - msg["current_consumed"]
    
    def get_poss(self):
        msg = self.connection.recv_match(type="GLOBAL_POSITION_INT", blocking=True)
        msg = msg.to_dict()
        return {"lat":msg["lat"],"lon":msg["lon"]}
    
    def get_num_of_sats(self):
        msg = self.connection.recv_match(type="GLOBAL_POSITION_INT", blocking=True)
        msg = msg.to_dict()
        return msg["get_num_of_sats"]
            
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


telm_singleton = Telemetry()


if __name__ == '__main__':
    from telemetry import telm_singleton
    from drone_state_homing import drone_state

    # telm_singleton.start_automatic_updates()
    # telm_singleton.print_all_msg()
    while True:
        print(drone_state)
        time.sleep(0.2)

    # telm_singleton.print_all_msg()














# class Move():

#     def see(self):
        
#         """this fuction will return all relevent date for a conputor vison data"""
#             # gps_poss, num_of_sats, gimbel_angle, ai_dict
#             # this setup allow easer passing of files 
            
#         """see_input_dict = {
#             "gps_poss":(x,y,z),
#             "num_of_sats": int(NUM),
#             "q_cam_rel_global": [x, y, z, w],
#             "ai_dict": SEE BELOW
            
#             }"""
        
#         """ai_dict {
#             "0": {
#                 bbox: (top_left, bottom_right),
#                 object: "name_of_thing_found",
#                 confidence: float
#             }
            
#             "1": {
#                 bbox: (top_left, bottom_right),
#                 object: "name_of_thing_found",
#                 confidence: float
#             }
#         }"""

#     pass