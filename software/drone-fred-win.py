import pymavlink
from pymavlink import mavutil
import math 
import numpy as np

from get_cam_stream_and_run_ai import *
from get_weed_positon import *

 
# I found the videos from Intelligent Quads helpfull 
# https://www.youtube.com/watch?v=kecnaxlUiTY
# https://www.youtube.com/watch?v=6M7e7DDLTQc
# https://www.youtube.com/watch?v=NTjEcHmqmu4

class Drone():
    """
    This is a drone calss
    """

    __speed = 0 # m/s
    __derection = 0 # compass bereing
    __velocity = (__speed,__derection)
    __battery = 6000 # in mah
    __max_battery = 6000 # in mah
    __spray_quanty = 2 # in L
    __max_spray = 2 # in L
    __gimbel_angles = (0,0,0) # xyz 
    __location = (0,0) # lon lat
    __hight_from_ground = 0
    __hight_from_sea = 0
    state = "home" # "home", "flying_out", "flying_home", "sprayin", "scaning"
    mishion_type = "scan" # spray or scan
    home = (0,0,0) # lon lat hight at sea level
    uav_connection = None # the drone that you can connect to 
    spray = False #if true do a spray run go to hot spot and spray it if False then do a scan mishion


    def __init__(self,path_to_drone,max_battery,max_spray,drone_dry_mass):
        self.__max_battery = max_battery
        self.__max_spray = max_spray
        # TODO: uncomment for final
        # self.uav_connection = mavutil.mavlink_connection(path_to_drone)
        self.uav_connection = mavutil.mavlink_connection('udpin:127.0.0.1:14551')
        self.uav_connection.wait_heartbeat()
        # print("Drone is connected at ",path_to_drone)
        print("Drone is connected at ")
        self.home_pos = get_home()
        # TODO: change to a actual val
        self.drone_dry_mass = 2000


    def update(self):
        self.__velocity = (get_speed(),get_derection())
        self.get_battery_range_quad_mode()
        self.get_battery_range_plane_mode()
        self.get_spray_quanty()
        self.get_gimbel_angles()
        self.home_pos = get_home()
        
    def get_speed(self):
        pass
    
    def get_spray_quanty(self):    
        pass
        
    def get_gimbel_angles(self):
        pass
    
    def get_home(self):
        pass
    
    
        
    
        
        

# TODO: make self leaning to update the polinomial over time 
# TODO: include any logic at all in it

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
    
def plane_polys(num,poly_type):
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

def get_battery_range_quad_mode(self,mah_used,bat_max_mah,bat_volts,drone_weight,home_pos=(0,0),wind_speed=0.0,wind_direction=0.0):
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
    bat_watts_remining = bat_volts * (bat_max_mah - mah_used)
    thottle_dict = {}
    for i in range(0,201):
        i *= 0.5
        ith_dict = {}
        ith_dict["g"] = quad_polys(i,"g")
        ith_dict["angle"] = math.acos(math.radians(quad_polys(i,"g")/drone_weight))
        ith_dict["speed"] = math.asin(math.radians(quad_polys(i,"g")/drone_weight))
        ith_dict["flight time"] = bat_watts_remining / quad_polys(i,"w")
        ith_dict["range"] = ith_dict["speed"] * ith_dict["flight time"]
        thottle_dict[str(i)] = ith_dict
        print(ith_dict)
        
    
       
    return thottle_dict
        
    
    
    return_dict = {
        "range":0,
        "angle":0}

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
    
       



