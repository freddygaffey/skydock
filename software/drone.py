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
    This is a drone calss
    """

   


    def __init__(self,path_to_drone,max_spray,drone_dry_mass,max_battery):
        self.max_battery = max_battery
        self.max_spray = max_spray
        # TODO: uncomment for final
        # self.uav_connection = mavutil.mavlink_connection(path_to_drone)
        self.uav_connection = mavutil.mavlink_connection('udpin:127.0.0.1:14551')
        self.uav_connection.wait_heartbeat()
        # print("Drone is connected at ",path_to_drone)
        print("Drone is connected at ")
        self.home_pos = get_home()
        # TODO: change to a actual val
        self.drone_dry_mass = 2000
        self.speed = 0 # m/s
        self.derection = 0 # compass bereing
        self.velocity = (__speed,__derection)
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


    def update(self):
        self.velocity = (get_speed(),get_derection())
        self.get_battery_range_quad_mode()
        self.get_battery_range_plane_mode()
        self.spray_quanty = self.get_spray_quanty()
        self.get_gimbel_angles()
        self.home_pos = self.get_home()
        self.spray_mass = self.get_spray_mass(self.spray_quanty)
        self.battery_volts = self.get_batt_v()
        
    def get_speed(self):
        pass
    
    def get_spray_quanty(self):    
        pass
        
    def get_gimbel_angles(self):
        pass
    
    def get_home(self):
        pass
    
    def get_spray_mass(self,spray_voume):
        return 1.1 * spray_voume
    
    def get_batt_v(self):
        pass
    
    def get_mah_used(self):
        pass
        
        
            
            

    # TODO: give the polinomial a experimental value

    def quad_polys(num,poly_type):
        if True:
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
            
    def plane_polys(num,poly_type):
        if True:
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

    def get_battery_range_quad_mode(self,mah_used = 0 ,bat_max_mah = 6000 ,bat_volts = 16.3 ,drone_weight= 2000,home_pos=(0,0),wind_speed=0.0,wind_direction=0.0):
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

    def get_battery_range_plane_mode(self,mah_used,bat_max_mah,bat_volts,drone_weight,home_pos,wind_speed=0.0,wind_direction=0.0):

        """
        This function will return the max range for the drone at the best speed ignoring the energy to speed up and slow down in the drone mode

        Args:
            mah_used (float): the mah used from the amp sensor in the h743
            bat_max_mah (float): from the drone class 
            bat_volts (float): from the uav read the live batt volts
            drone_weight (float): sum the current spay quantity and the dry weight
            wind_speed (float, optional): the wind speed in m/s. Defaults to 0.
            wind_direction (float, optional): the true north compass bearing of the wind from the base station or ardupilot. Defaults to 0.
            home_pos (tuple): (lon,lat) to home
        """
            
            



