import threading
from telemetry import telm_singleton
import time
from pymavlink import mavutil

class Move():
    def __init__(self):
        self.connection = telm_singleton.connection
        self.mode_mapping = {'STABILIZE': 0,'ACRO': 1,'ALT_HOLD': 2,'AUTO': 3,'GUIDED': 4,'LOITER': 5,'RTL': 6,'CIRCLE': 7,'OF_LOITER': 10,'DRIFT': 11,'SPORT': 13,'FLIP': 14,'AUTOTUNE': 15,'POSHOLD': 16,'BRAKE': 17,'THROW': 18,'AVOID_ADSB': 19,'GUIDED_NOGPS': 20,'SMART_RTL': 21,'FLOWHOLD': 22,'FOLLOW': 23,'ZIGZAG': 24,'SYSTEMIDLE': 25,'AUTOTUNE': 26,'RALLY': 27}
        self.current_mode = self.get_mode()

        self._v_thread = None
        self._v_thread_stop_event = threading.Event()

    def set_mode(self, mode):
        if mode not in self.mode_mapping.keys():
            raise Exception("INVALID MODE (ps THIS IS FORM FREDDY)")
        self.connection.mav.command_long_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_MODE,
            0,  # Confirmation
            1,  # 1: Set mode
            self.mode_mapping[mode],  # Mode ID
            0, 0, 0, 0, 0
        )

    def get_mode(self):
        """retuns the currnt mode (in eglish)"""
        msg = self.connection.recv_match(type='HEARTBEAT', blocking=True)
        if msg:
            mode_id = msg.custom_mode
            current_mode = None
            for i in self.mode_mapping:
                if self.mode_mapping[i] == mode_id:
                    current_mode = i
                    break
            if current_mode ==  None: raise Exception("mode not found (freddy)")
        return current_mode

    def send_displacement_command_yaw_stay_same(self,mx,my,mz,bitmask=4088):
            self.connection.mav.set_position_target_local_ned_send(
                0,
                self.connection.target_system,
                self.connection.target_component,
                mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,
                bitmask,  # ignore velocity, acceleration, yaw/yaw_rate (position only)
                mx, my, mz,  # position offsets in meters
                0, 0, 0,     # velocity ignored
                0, 0, 0,     # acceleration ignored
                0, 0         # yaw and yaw_rate ignored
                )

    def send_volocity_command_yaw_stay_same(self,mx,my,mz,bitmask=int(0b10111000111)):
        # this command must be sent every 3 seconds to continue moving
        if not bitmask:
            raise ValueError("bit mask not set for volocity command")

        self.connection.mav.set_position_target_local_ned_send(
            0,
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,
                bitmask,  # ignore velocity, acceleration, yaw/yaw_rate (position only)
            0, 0, 0,  
            mx, my, mz,     # velocity 
            0, 0, 0,     
            0, 0         # TODO: yaw and yaw_rate 
        )

    def send_e_stop_command(self):
        old_mode = self.get_mode()
        self.set_mode("BRAKE")
        time.sleep(3)
        self.set_mode(old_mode)
        self.stop_volocity_command()

    def send_displacement_command_yaw_stay_same(self,mx,my,mz,bitmask=4088):
            self.connection.mav.set_position_target_local_ned_send(
                0,
                self.connection.target_system,
                self.connection.target_component,
                mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,
                bitmask,  # ignore velocity, acceleration, yaw/yaw_rate (position only)
                mx, my, mz,  # position offsets in meters
                0, 0, 0,     # velocity ignored
                0, 0, 0,     # acceleration ignored
                0, 0         # yaw and yaw_rate ignored
                )

    def move_volocity_until_stop_or_max_time(self,direction,max_time,change_yaw=False):
        self.stop_volocity_command()

        def repeatedly_send_v_command(direction,max_time,change_yaw):
            dyaw = 3527
            no_dyaw = 1479 
            if change_yaw:
                bitmask = dyaw
            else:
                bitmask = no_dyaw
            start_time = time.time()
            while time.time() < start_time + max_time and not self._v_thread_stop_event.is_set():
                print("sending volocity command on thread")
                self.send_volocity_command_yaw_stay_same(direction[0],direction[1],direction[2],bitmask)
                time.sleep(0.3)
                
        if self._v_thread is None or not self._v_thread.is_alive(): # this will check if none like after init or later is not runing
            self._v_thread_stop_event.clear()
            self._v_thread = threading.Thread(target=repeatedly_send_v_command,args=(direction,max_time,change_yaw))
            self._v_thread.start()
            print("started sending move command")

    def stop_volocity_command(self):
        if self._v_thread and self._v_thread.is_alive():
            self._v_thread_stop_event.set()
            self._v_thread.join()
            self.send_volocity_command_yaw_stay_same(0,0,0)
            self._v_thread = None 

    def arm(self): # dange UNTESTED
        # TODO: test in real world
        self.connection.mav.command_long_send(
            self.connection.target_system,
            self.connection.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0, 1, 0, 0, 0, 0, 0, 0
        )
        while True:
            msg = self.connection.recv_match(type='HEARTBEAT', blocking=True)
            if msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED:
                return True
            time.sleep(1)
            
    def arm_and_take_off_to_hight(self,hight): # dange UNTESTED
        # TODO: test in real world
            self.arm()
            self.connection.mav.command_long_send(
                self.connection.target_system,
                self.connection.target_component,
                mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
                0, 0, 0, 0, 0, 0, 0, hight
            )


    

move_singleton = Move()
