import pymavlink
from pymavlink import mavutil

class Drone():
    """
    This is a drone calss
    """

    __speed = 0 # m/s
    __derection = 0 # compass bereing
    __volocity = (speed,derection)
    __battery = 6000 # in mah
    __max_battery = 6000 # in mah
    __spray_quanty = 2 # in L
    __max_spray = 2 # in L
    __gimbel_xyz_loc_from_rtk_gps = (0,0,0) # (x,y,z) in mm
    __gimbel_angles = (0,0,0) # xyz 
    __location = (0,0) # lon lat
    __state = "home" # "home", "flying_out", "fluing_home", "sprayin", "scaning"
    uav = none


    def __init__(self,path_to_drone,max_battery,max_spray,gimbel_xyz_loc_from_rtk_gps):
        self.__max_battery = max_battery
        self.__max_spray = max_spray
        self.__gimbel_xyz_loc_from_rtk_gps = gimbel_xyz_loc_from_rtk_gps
        self.uav = mavutil.mavlink_connection(path_to_drone)
        self.master.wait_heartbeat() 
        print("Drone is connected at ",path_to_drone)


    def update(self):
        get_speed()
        get_derection()
        get_volocity()
        get_battery()
        get_spray()
        get_spray_quanty()
        get_gimbel_angles()

    def get_speed(self)







