import pymavlink
from pymavlink import mavutil
import math 
import numpy as np
from scipy.spatial.transform import Rotation as R # this is needed for the q
from dataclasses import dataclass
import base64

import threading
import time
from drone_snapshots import drone_telm_stapshot, ground_station_commands
import serial
from move import move_singleton
 
# I found the videos from Intelligent Quads helpfull 
# https://www.youtube.com/watch?v=kecnaxlUiTY
# https://www.youtube.com/watch?v=6M7e7DDLTQc
# https://www.youtube.com/watch?v=NTjEcHmqmu4

# multi threading 
# https://www.youtube.com/watch?v=STEOavXqXkQ

class GroundStaionMessages:
    messages = []
    messages_lock = threading.Lock()

    @staticmethod
    def encode_message(message):
        # message = base64.b64encode(message.encode("utf-8")).decode("ascii")
        return message  

    @staticmethod
    def decode_message(message):
        # message = base64.b64decode(message.encode("ascii")).decode("utf-8")
        return message

    @staticmethod
    def get_latest_message():
        with GroundStaionMessages.messages_lock:
            try:
                return GroundStaionMessages.messages[-1]
            except IndexError:
                return GroundStaionMessages.messages

    @staticmethod
    def passer(message):
        if message._type == "STATUSTEXT" and "gc:" in message.text:
            message_text = message.text
            message_text = GroundStaionMessages.decode_message(message_text)
            message_text = message_text[3:]
            message_array = eval(message_text)
            message_array[0] = message_array[0][1:]
            # print(message_array,"this from passer")

            with GroundStaionMessages.messages_lock:
                GroundStaionMessages.messages.append(message_array)
                
    @staticmethod
    def ask_gc_question(question):
        question_to_send = f"drone: {question}"
        if len(question) >= 43:
            raise ValueError("question is to long") 
        
        telm_singleton.send_text_message(GroundStaionMessages.encode_message(question_to_send))

        def check_for_message_retun_ans():
            while True:
                time.sleep(0.5)
                message = GroundStaionMessages.get_latest_message()

                if len(message) == 0: continue
                print(message[0],"message question")
                print(question,"function question")
                if question != message[0]: continue
                elif "accepted" == message[1]: return True
                elif "rejected" == message[1]: return False
                else: raise ValueError("idk what happed")

        return check_for_message_retun_ans()
        # thed = threading.Thread(target=check_for_message_retun_ans,daemon=True).start()
        
class Telemetry():
    """for  quaternions I will use the [x, y, z, w] this is the convetoin for sicpy"""
    
    def __init__(self):
        self.battery_capacity = 4800 # in mah
        self.most_recent_message = None

        try:
            path_to_uav = "/dev/ttyACM1"
            self.connection = mavutil.mavlink_connection(path_to_uav, baud=115200)
            self.connection.wait_heartbeat()
            move_singleton.connection = self.connection
        except serial.serialutil.SerialException as e:
            path_to_uav = "/dev/ttyACM0"
            self.connection = mavutil.mavlink_connection(path_to_uav, baud=115200)
            self.connection.wait_heartbeat()
            move_singleton.connection = self.connection
 


        self.update_rate = 1/32 # slightly hight then the ai frame rate 

        # defing what command to stream
        # self.set_a_message_interval("BATTERY_STATUS",interval=1)
        # self.set_a_message_interval("GLOBAL_POSITION_INT",interval=self.update_rate)
        # self.set_a_message_interval("SYS_STATUS",interval=self.update_rate)
        # self.set_a_message_interval("GIMBAL_DEVICE_ATTITUDE_STATUS",interval=self.update_rate)
        # self.set_a_message_interval("ATTITUDE_QUATERNION",interval=self.update_rate)
        # self.set_a_message_interval("SERVO_OUTPUT_RAW",interval=self.update_rate)

        self.start_automatic_message_passer()

    def start_automatic_message_passer(self):

        self.set_a_message_interval("SERVO_OUTPUT_RAW",interval=self.update_rate)
        self.set_a_message_interval("GLOBAL_POSITION_INT",interval=self.update_rate)

        def message_in(message):
            drone_telm_stapshot.pass_msg(message)
            ground_station_commands.pass_message(message)
            move_singleton.msg_passer(message)
            GroundStaionMessages.passer(message)
            self.most_recent_message = message
            
        def passer():
            while True:
                try:
                    msg = self.connection.recv_msg()
                    if msg:message_in(msg)
                except serial.SerialException:
                    pass

        threading.Thread(target=passer).start()

    def print_all_msg(self,duration=100):
        while 1:
            # msg = self.connection.recv_match(type="RC_CHANNELS", blocking=True)
            msg = self.most_recent_message
            if msg:
                # print(msg)
                # print(msg)
                if msg._type == "STATUSTEXT":
                    print(msg)

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

    def run_pre_flight_checks(self):
        """retun true if good to go
        retun the arm fail message if not good to go"""
        for _ in range(5):
            self.connection.mav.command_long_send(
                self.connection.target_system,       # target_system
                self.connection.target_component,    # target_component
                mavutil.mavlink.MAV_CMD_RUN_PREARM_CHECKS,  # command 401
                0,                          # confirmation
                0, 0, 0, 0, 0, 0, 0         # params 1-7 (not used)
            )

            result = self.connection.recv_match(type='COMMAND_ACK', blocking=True,timeout=1)
            if result.command == 401:
                break 
        
        msg = self.connection.recv_match(type='STATUSTEXT', blocking=True, timeout=1)
        if msg: return msg.text
        if msg == None and result.command == 401:
            return True
        # example of fialing
        # COMMAND_ACK {command : 401, result : 0, progress : 0, result_param2 : 0, target_system : 255, target_component : 0}
        # PreArm: GPS 1: Bad fix 

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

    def send_text_message(self,message:str):
            if len(message) > 50-7:
                raise ValueError("the send text message must be under 50 chars")
            self.connection.mav.statustext_send(
                mavutil.mavlink.MAV_SEVERITY_INFO, 
                f"{message}".encode("utf-8"))
            

telm_singleton = Telemetry()


if __name__ == '__main__':
    # from telemetry import telm_singleton
    # from software.drone_snapshots import drone_telm_stapshot

    # telm_singleton.start_automatic_updates_homing()
    # while True: print(telm_singleton.run_pre_flight_checks())

    
    # telm_singleton.print_all_msg()
    while True:
        print(GroundStaionMessages.ask_gc_question(input("> ")))

        # telm_singleton.send_text_message("hi this is a text message form the drone")
        # print("sent message")
        # print(ground_station_commands)
        # time.sleep(0.2)

    # telm_singleton.print_all_msg()
