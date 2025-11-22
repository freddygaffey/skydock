from telemetry import Telemetry, telm_singleton
import time

class Move(Telemetry):

    def __init__(self,telm_singleton.connection):
        self.connection = drone_connection
        self.move_mode = "STOP"
        self.mode_mapping = {'STABILIZE': 0,'ACRO': 1,'ALT_HOLD': 2,'AUTO': 3,'GUIDED': 4,'LOITER': 5,'RTL': 6,'CIRCLE': 7,'OF_LOITER': 10,'DRIFT': 11,'SPORT': 13,'FLIP': 14,'AUTOTUNE': 15,'POSHOLD': 16,'BRAKE': 17,'THROW': 18,'AVOID_ADSB': 19,'GUIDED_NOGPS': 20,'SMART_RTL': 21,'FLOWHOLD': 22,'FOLLOW': 23,'ZIGZAG': 24,'SYSTEMIDLE': 25,'AUTOTUNE': 26,'RALLY': 27}
        self.current_mode = self.get_mode()

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

    def send_displacement_command_yaw_stay_same(self,mx,my,mz,bitmask=248):
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

    def send_volocity_command_yaw_stay_same(self,mx,my,mz,bitmask=4088):
        # TODO: set the right bitmask

        # this command must be sent every 3 seconds to contiu moving
        if not bitmask:
            raise ValueError("bit mask not set for volocity command")
            bitmask = "???" 

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

        # 3527 # this woks but will turn to face the directon of travel
        # 3520 # same as obove  
        # 3523 #
        # 3591 #
        # 3576 #
        # 0b110111000111 3527

        # 1	✅ Velocity only, yaw stays the same	952	Safest and most common for “move in direction but don’t turn.”
        # 2	Velocity + yaw control (set yaw absolute or rate)	944	Same as above but lets you use myaw_poss or myaw_rate.
        # 3	Velocity only, yaw rate active (ignore yaw position)	936	Lets you spin while moving.
        # 4	Velocity + yaw position only (ignore yaw rate)	940	Keeps facing a heading you send.
        # 5	Velocity only, ignore yaw completely (very permissive)	4095	Ignores everything, often used when testing or debugging.
        # 4095
        # 940
        # 936
        # 944  # move weridly
        # 952 # not work 

        # bit1:PosX, bit2:PosY, bit3:PosZ, bit4:VelX, bit5:VelY, bit6:VelZ, bit7:AccX, bit8:AccY, bit9:AccZ, bit11:yaw, bit12:yaw rate

    def send_fly_to_point_yaw_change(self,mx,my,mz):
        bitmask=248
        
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

    def send_stop_command(self,new=True,old=False):
        self.move_mode = "STOP"
        if new:
            old_mode = self.get_mode()
            self.set_mode("BRAKE")
            time.sleep(3)
            self.set_mode(old_mode)
        elif old:
            self.send_volocity_command_yaw_stay_same(0,0,0,0,0)
        else:
            raise ValueError("not inputed the choice")

move_singleton = Move()
