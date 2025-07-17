import pymavlink
from pymavlink import mavutil
import math 
import numpy as np

class Drone():
    """
    This is a drone calss
    """

    __speed = 0 # m/s
    __derection = 0 # compass bereing
    __velocity = (speed,derection)
    __battery = 6000 # in mah
    __max_battery = 6000 # in mah
    __spray_quanty = 2 # in L
    __max_spray = 2 # in L
    __gimbel_angles = (0,0,0) # xyz 
    __location = (0,0) # lon lat
    state = "home" # "home", "flying_out", "flying_home", "sprayin", "scaning"
    mishion_type = "scan" # spray or scan
    home_pos = (0,0) # lon lat
    uav = None # the drone that you can connect to 
    spray = False


    def __init__(self,path_to_drone,max_battery,max_spray):
        self.__max_battery = max_battery
        self.__max_spray = max_spray
        self.uav = mavutil.mavlink_connection(path_to_drone)
        self.master.wait_heartbeat() 
        print("Drone is connected at ",path_to_drone)
        self.home_pos = get_home()


    def update(self):
        get_speed()
        get_derection()
        get_velocity()
        get_battery_range_quad_mode()
        get_battery_range_plane_mode()
        get_spray_quanty()
        get_gimbel_angles()
        self.get_home() = self.home_pos
        
        

# TODO: make self leaning to update the polinomial over time 
# TODO: include any logic at all in it

def quad_polys(self,num,poly_type):
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
    
def plane_polys(self,num,poly_type):
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


def get_battery_range_quad_mode(self,mah_used,bat_max_mah,bat_volts,drone_weight,home_pos,wind_speed=0.0,wind_direction=0.0):
    """
    this function will return the max range for the drone at the best speed ignoring the energy to speed up and slow down in the drone mode

    Args:
        mah_used (float): the mah used from the amp sensor in the h743
        bat_max_mah (float): from the drone class 
        bat_volts (float): from the uav read the live batt volts
        drone_weight (float): sum the current spay quantity and the dry weight
        wind_speed (float, optional): the wind speed in m/s. Defaults to 0.
        wind_direction (float, optional): the true north compass bearing of the wind from the base station or ardupilot. Defaults to 0.
        home_pos (tuple): (lon,lat) to home
    """
    poly = 
    
    return_dict = {
        "range":0,
        "best_speed":0}

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
    
       



