import math 
import numpy as np
# TODO: make self leaning to update the polinomial over time 
# TODO: include any logic at all in it


def battery_range_quad_mode(mah_used,bat_max_mah,bat_volts,drone_weight,home_bearing=0.0,wind_speed=0.0,wind_direction=0.0):
    """
    this function will return the max range for the drone at the best speed ignoring the energy to speed up and slow down in the drone mode

    Args:
        mah_used (float): the mah used from the amp sensor in the h743
        bat_max_mah (float): from the drone class 
        bat_volts (float): from the uav read the live batt volts
        drone_weight (float): sum the current spay quantity and the dry weight
        wind_speed (float, optional): the wind speed in m/s. Defaults to 0.
        wind_direction (float, optional): the true north compass bearing of the wind from the base station or ardupilot. Defaults to 0.
        home_bearing (float, optional): the true north compass bearing to home
    """
    poly = 
    
    return_dict = {
        "range":0,
        "best_speed":0}
    




def battery_range_plane_mode(mah_used,bat_max_mah,bat_volts,drone_weight,home_bearing=0.0,wind_speed=0.0,wind_direction=0.0):

    """
    This function will return the max range for the drone at the best speed ignoring the energy to speed up and slow down in the drone mode

    Args:
        mah_used (float): the mah used from the amp sensor in the h743
        bat_max_mah (float): from the drone class 
        bat_volts (float): from the uav read the live batt volts
        drone_weight (float): sum the current spay quantity and the dry weight
        wind_speed (float, optional): the wind speed in m/s. Defaults to 0.
        wind_direction (float, optional): the true north compass bearing of the wind from the base station or ardupilot. Defaults to 0.
        home_bearing (float, optional): the true north compass bearing to home
    """
       