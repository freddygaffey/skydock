import pymavlink
from pymavlink import mavutil
import math 
import numpy as np
# from get_cam_stream_and_run_ai import *
# from get_weed_positon import *

 
# I found the videos from Intelligent Quads helpfull 
# https://www.youtube.com/watch?v=kecnaxlUiTY
# https://www.youtube.com/watch?v=6M7e7DDLTQc
# https://www.youtube.com/watch?v=NTjEcHmqmu4

class Drone():
    """
    This is a drone class
    """
    def __init__(self,path_to_drone,max_spray,drone_dry_mass,max_battery):
        self.max_battery = max_battery
        self.max_spray = max_spray
        # TODO: uncomment for final
        self.uav_connection = mavutil.mavlink_connection(path_to_drone)
        # self.uav_connection = mavutil.mavlink_connection('/dev/ttyUSB0', baud=115200)
        self.uav_connection.wait_heartbeat()
        # print("Drone is connected at ",path_to_drone)
        print(f"Drone is connected at {self.uav_connection} ")
        self.home_pos = get_home()
        # TODO: change to a actual val
        self.drone_dry_mass = 2000
        self.speed = 0 # m/s
        self.direction = 0 # compass bearing
        self.velocity = (self.speed,self.direction)
        self.max_battery = 6000 # in mah
        self.spray_quanty = 2 # in L
        self.spray_mass = get_spray_mass(self.spray_quanty)
        self.max_spray = 2 # in L
        self.gimbel_angles = (0,0,0) # xyz 
        self.location = (0,0) # lon lat
        self.hight_from_ground = 0
        self.hight_from_sea = 0
        self.state = "home" # "home", "flying_out", "flying_home", "sprayin", "scaning"
        self.mishion_type = "scan" # spray or scan
        self.home = (0,0,0) # lon lat hight at sea level
        uav_connection = None # the drone that you can connect to 
        self.spray = False #if true do a spray run go to hot spot and spray it if False then do a scan mishion
        self.mah_used = 0
        self.battery_volts = 16.4
        self.sprayed_so_far = 0 # in Litres
        self.wind_speed = 0.0 # in m/s
        self.wind_direction = 0.0 # in compass bearing

    def update(self):
        self.velocity = (self.get_speed(),self.get_direction())
        self.get_battery_range_quad_mode()
        self.get_battery_range_plane_mode()
        self.spray_quanty = self.get_spray_quanty()
        self.get_gimbel_angles()
        self.home_pos = self.get_home()
        self.spray_mass = self.get_spray_mass(self.spray_quanty)
        self.battery_volts = self.get_batt_v()
        self.wind_speed = self.get_wind_speed()
        self.wind_direction = self.get_wind_direction()
        
    def get_speed(self):
        msg = self.uav_connection.recv_match(type='VFR_HUD', blocking=True) 
        speed = msg.groundspeed  # in m/s
        if msg:
            return speed
        else:
            print("no speed data received")
            return 0

    def get_spray_quanty(self):
        sprayed_so_far = self.read_sensor_volume()  # in Litres
        remaining = max(0, self.max_spray - sprayed_so_far) #which flow sensor are we using?
        return remaining

# TODO: need to change to use the gryo pitch and comosss with gible angel 
    def get_gimbel_angles_abs(self):
        msg = self.uav_connection.recv_match(type='MOUNT_STATUS', blocking=True)
        


    
    def get_home(self):
        msg = self.uav_connection.recv_match(type='HOME_POSITION', blocking=True, timeout=5)
        
        if msg is None:
            print("warning: HOME_POSITION message not received.")
            return None
        lat = msg.latitude / 1e7
        lon = msg.longitude / 1e7
        alt = msg.altitude / 1000.0  # mm to meters

        return (lon, lat, alt)

    def get_spray_mass(self,spray_volume):
        return 1.1 * spray_volume

    def get_batt_v(self):
        msg = self.uav_connection.recv_match(type='BATTERY_STATUS', blocking=True, timeout=5)
        if msg is None:
            print("battery status not received.")
            return None

        voltage_mv = msg.voltages[0]
        
        if voltage_mv == 65535:
            print("battery voltage not available.")
            return None

        return voltage_mv / 1000.0  # Convert mV to V

    def get_mah_used(self):
        msg = self.uav_connection.recv_match(type='BATTERY_STATUS', blocking=True)
        mah = msg.current_consumed
        return mah
    
    def get_wind_speed(self):
        msg = self.uav_connection.recv_match(type='WIND', blocking=True, timeout=5)
        if msg is None:
            print("wind speed not received.")
            return 0.0
        return msg.speed
    
    def get_wind_direction(self):
        msg = self.uav_connection.recv_match(type='WIND', blocking=True, timeout=5)
        if msg is None:
            print("wind direction not received.")
            return 0.0
        return msg.direction

    # TODO: give the polinomial a experimental value

    def quad_polys(num,poly_type):
        if poly_type == "a":
            a = 1
            b = 0
            c = 1
            num = a*(num**2) + b*num + c
            return num
        if poly_type == "w":
            a = 1
            b = 0
            c = 1
            num = a*(num**2) + b*num + c
            return num
        
        if poly_type == "g":
            a = 1
            b = 0
            c = 1
            num = a*(num**2) + b*num + c
            return num
        
        if poly_type == "rpm":
            a = 1
            b = 0
            c = 1
            num = a*(num**2) + b*num + c
            return num

    def get_battery_range_quad_mode(self,mah_used = 0 ,bat_max_mah = 6000 ,bat_volts = 16.3 ,drone_weight= 2000,home_pos=self.home_pos,wind_speed=self.wind_speed,wind_direction=self.wind_direction):
        if True:
            """
            this function will return the max range for the drone at the best speed ignoring the energy to speed up and slow down in the drone mode

            Args:
                mah_used (float): the mah used from the amp sensor in the h743
                bat_max_mah (float): from the drone class 
                bat_volts (float): from the uav read the live batt volts
                drone_weight (float): IN GRAMS sum the current spay quantity and the dry weight
                wind_speed (float, optional): the wind speed in m/s. Defaults to 0.
                wind_direction (float, optional): the true north compass bearing of the wind from the base station or ardupilot. Defaults to 0.
                home_pos (tuple): (lon,lat) to home
            """
            
            # TODO: could insert some logic to use wind so that it is better 
            bat_watts_remining = bat_volts * (bat_max_mah - mah_used)
            thottle_dict = {}
            for i in range(0,201):
                i *= 0.5
                ith_dict = {}
                ith_dict["g"] = quad_polys(i,"g")
                ith_dict["angle"] = math.acos(math.radians(quad_polys(i,"g")/drone_weight))
                ith_dict["speed"] = math.asin(math.radians(quad_polys(i,"g")/drone_weight))
                ith_dict["flight time"] = bat_watts_remining / quad_polys(i,"w") # TODO: work out units 
                ith_dict["range"] = ith_dict["speed"] * ith_dict["flight time"] # TODO: work out units
                thottle_dict[str(i)] = ith_dict
                # print(ith_dict)
            bests ={
                "time":{"throttle":0,
                        "time":0},
                "range":{"throttle":0,
                        "range":0}}
            
            for i in thottle_dict:
                # print(thottle_dict[i])
                if bests["time"]["time"] < thottle_dict[i]["flight time"]:
                    bests["time"]["time"] = thottle_dict[i]["flight time"] # TODO: work out units
                    bests["time"]["throttle"] = float(i)
                if bests["range"]["range"] < thottle_dict[i]["range"]: # TODO: work out units
                    bests["range"]["range"] = thottle_dict[i]["range"] # TODO: work out units
                    bests["range"]["throttle"] = float(i)
            print(bests)
            return bests


            



