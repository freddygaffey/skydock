import math
# x,y,z = 100,0,0
# xo,yo,zo = 0,0
# cam_angle = [xo,yo]
# cam_gps_pos = [x,y,z]

def find_gps_from_angle_and_gps(cam_gps,cam_angle):
    rtn = []
    for i in cam_angle:
        rtn.append(math.tan(math.radians(i))*cam_gps[-1])
        
    return (rtn[0],rtn[1],cam_gps[-1])

# print(find_gps_from_angle_and_gps([0,0,1],[45,45])) test

    
# def find_weed_position_close_range(cam_gps,cam_angle):
#     """
#     Takes the gps and the cam angle (ashuming cam is pointing at the weed rel to a flat pane) 
#     returns the weeds gps cords
#     """
#     # TODO: this is a logic error
#     weed_poss = (0,0,0)


#     # the specs  for the pi cam i am using
#     """
#     notes to self 
#     Horizontal	~22.3°
#     Vertical	~16.8°
#     Diagonal	~27.7°
#     """
# import opencv
def scan_for_weeds(cam_gps,cam_angle,array_of_weeds_from_ai,horizontal_fov=22.3,vertical_fov=16.8,diagonal_fov=27.7):
    """_summary_
    Takes the gps and the cam angle (ashuming cam is pointing at the weed rel to a flat pane) 
    returns the weeds gps cords and poss of each weed as a heat map
    weed_pos (tuple): (x,y,z) of the weed

    Args:
        cam_gps (tuple): z,y,z loc of the sensor in the cam
        cam_angle (tupel):xo,yo of the cam rel to the flat plane
        array_of_weeds_from_ai (array of array of tupels): [[(center_x,center_y0),(x_hight,y_hight),confodince]*n]     
    """
      
    precision = 100 
    # find the gps pos of the corners of the camera
    cam_angle_TL = (cam_angle - horizontal_fov /2,cam_angle + vertical_fov /2)
    TL = find_gps_from_angle_and_gps(cam_gps,cam_angle_TL)
    TL = round(TL,2)\
    
    cam_angle_TR = (cam_angle + horizontal_fov /2,cam_angle + vertical_fov /2)
    TR = find_gps_from_angle_and_gps(cam_gps,cam_angle_TL)
    TR = round(TR,2)
    
    cam_angle_BL = (cam_angle + horizontal_fov /2,cam_angle - vertical_fov /2)
    BL = find_gps_from_angle_and_gps(cam_gps,cam_angle_TL)
    BL = round(BL,2)
    
    cam_angle_BR = (cam_angle - horizontal_fov /2,cam_angle - vertical_fov /2)
    BR = find_gps_from_angle_and_gps(cam_gps,cam_angle_TL)
    BR = round(BR,2)
        
    # the heat map will be done to a precision to 100mm 
    max_and_min = [[TL,TR],
                   [BL,BR]]
    # TODO: get the array_of_weeds_from_ai 
    # and work out there pos and populata a array at incments 
    # of the prestion and weeds with eht acruesy
    heat_map = []
    
    
    










# print(find_weed_position(cam_angle=cam_angle,cam_gps=cam_gps_pos))
