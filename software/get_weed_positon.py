import math
import numpy as np
import random
import matplotlib.pyplot as mp
import os
import json

"""
this is a file that conteins the functons necercery to tun the output form a yolo model and the posston of the drones gimbel and in 3d space to work help define the weeds possiton both in scanning and in spraying
"""

def find_point_with_gps_and_angle(gps,angle):
    """
    Estimate the GPS coordinates of a point given the drone's position and gimbal angles.

    Args:
    gps (list): [latitude, longitude, height_above_ground] in meters
    angle (list): [x_angle, y_angle] in degrees
                    - x_angle (angle[0]): left/right relative to forward (positive = right)
                    - y_angle (angle[1]): up/down (positive = down)

    Returns:
    list: [latitude, longitude] of the target point
    """
    x_pos_in_m = math.tan(math.radians(angle[0]))*gps[-1]
    y_pos_in_m = math.tan(math.radians(angle[1]))*gps[-1]
    
    
    
    lat_rad = math.radians(gps[0])
    deg_per_m_lat = 1 / 111320
    deg_per_m_lon = 1 / (111320 * math.cos(lat_rad))
        
    new_lon = gps[1]+deg_per_m_lon*x_pos_in_m
    new_lat =  gps[0]+deg_per_m_lat*y_pos_in_m
    
    return [new_lat,new_lon]
    















# old code will do a rewrite
#  -------------------------------------------------------------------------------------------
exit()

def find_gps_from_angle_and_gps(cam_gps,cam_angle):
    rtn = []
    for i in cam_angle:
        rtn.append(math.tan(math.radians(i))*cam_gps[-1])

    return (rtn[0],rtn[1])


def get_the_arr_index_range_betwen_nums(min,max,arr_length):
    
    r = [-1,-1]
    increments = 1/arr_length
    poss = 0
    for val in [min,max]:
        for i in range(arr_length):
            if val not in r:
                if val == 0 or val == 1:
                    r[poss] = i
                elif val > increments * (i + 1) and val >= increments * i:
                    r[poss] = i

        poss += 1
    if r[0] == -1:
        r[0] = 0
    return r

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


def scan_for_weeds(cam_gps,cam_angle,array_of_weeds_from_ai,horizontal_fov=22.3,vertical_fov=16.8,diagonal_fov=27.7):
    """_summary_
    Takes the gps and the cam angle (ashuming cam is pointing at the weed rel to a flat pane)
    returns the weeds gps cords and poss of each weed as a heat map
    weed_pos (tuple): (x,y,z) of the weed

    Args:
        cam_gps (tuple): z,y,z loc of the sensor in the cam
        cam_angle (tupel):xo,yo of the cam rel to the flat plane
        array_of_weeds_from_ai (array of array of tuples): [[(top_left,bottem_right),confodince]*n]
    """


    round_amount = 2
    multiply_amount = 1
    # find the gps pos of the corners of the camera
    cam_angle_TL = (cam_angle[0] - horizontal_fov / 2, cam_angle[1] + vertical_fov / 2)
    TL = find_gps_from_angle_and_gps(cam_gps, cam_angle_TL)
    TL = (round(TL[0], round_amount), round(TL[1], round_amount))

    cam_angle_TR = (cam_angle[0] + horizontal_fov / 2, cam_angle[1] + vertical_fov / 2)
    TR = find_gps_from_angle_and_gps(cam_gps, cam_angle_TR)
    TR = (round(TR[0], round_amount), round(TR[1], round_amount))

    cam_angle_BL = (cam_angle[0] + horizontal_fov / 2, cam_angle[1] - vertical_fov / 2)
    BL = find_gps_from_angle_and_gps(cam_gps, cam_angle_BL)
    BL = (round(BL[0], round_amount), round(BL[1], round_amount))

    cam_angle_BR = (cam_angle[0] - horizontal_fov / 2, cam_angle[1] - vertical_fov / 2)
    BR = find_gps_from_angle_and_gps(cam_gps, cam_angle_BR)
    BR = (round(BR[0], round_amount), round(BR[1], round_amount))

    # the heat map will be done to a precision to 100mm
    TL_and_BR = [[TL, BR]]

    # Fix the heat_map line: convert floats to ints, and fix range usage
    heat_map = np.zeros((abs(int(TL[1]-BR[1])*multiply_amount),(abs(int(TL[0]-TR[0]*multiply_amount)))),dtype=float)
    # print("heat map size ",(abs(int(TL[0]-TR[0]*multiply_amount)),abs(int(TL[1]-BR[1])*multiply_amount)))
    row_length = abs(int(round(TL[0]-TR[0])*multiply_amount))
    column_length = abs(int(round(TL[1]-BR[1])*multiply_amount))



    for box in data:
        amount_to_change_row = get_the_arr_index_range_betwen_nums(box[0][0][1],box[0][1][1],row_length)
        # print("row length ",row_length)
        # print("amout to change row", amount_to_change_row)
        amount_to_change_column = get_the_arr_index_range_betwen_nums(box[0][0][0],box[0][1][0],column_length)
        # print("amout to change comlmb", amount_to_change_column)
        # print("colem lenght",column_length)
        confidence = box[1]
        for j in range(amount_to_change_column[0],amount_to_change_column[1]):

            heat_map_row = heat_map[j]
            # print(heat_map)
            for i in range(amount_to_change_row[0],amount_to_change_row[1]):

                # print(i)
                # heat_map_row[i] = 0.1
                heat_map_row[i] = (confidence+heat_map[j][i])/2

            heat_map[j] = heat_map_row
        # print("_"*50)
        # for i in heat_map:
        #     jr = []
        #     for j in i:
        #         jr.append(float(round(j,5)))
        #         # if jr[-1] >= 0.874:
        #         #     jr[-1] = 0
        #     print(jr)
    try:    
        file_csv = open(f"all_past_heatmaps/0.csv","x")
        print("wrote to 0.csv")
        json.dump(TL_and_BR,file_csv) 
        file_csv.write("\n")    
    except FileExistsError:
        names = os.listdir("all_past_heatmaps")
        name = 1
        for i in names:
            i = i.replace(".csv","")
            name = max(name,int(i))
        file_csv = open(f"all_past_heatmaps/{name + 1}.csv","x")
        json.dump(TL_and_BR,file_csv)        
        file_csv.write("\n")
        
    for hmr in heat_map:
        csv_row = ""
        for hmc in hmr:
            csv_row += f"{hmc},"
        file_csv.write(csv_row+"\n")
    file_csv.close()
    
    return (TL_and_BR,heat_map)


data = []


heat_map_final = (scan_for_weeds([0,0,300],[30,45],array_of_weeds_from_ai=data))

# def update_map_with_scan():
#     csv = ""
#     for i in heat_map_final[1]:
#         csv_row = ""
#         for j in i:
#             csv_row += f"{round(j,4)},"
#         csv_row = csv_row[0:-2]
#         csv_row += "\n"
#         csv = csv + csv_row
#     file_csv = open("array.csv",'w')
#     file_csv.write(csv)
#     file_csv.close()
        

# data = []
# for _ in range(1):
#     data.append([((random.random(),random.random()),(random.random(),random.random())),random.random()])

heat_map = (scan_for_weeds([0,0,300],[30,45],array_of_weeds_from_ai=data))

        
for i in range(1):
    data = []
    for _ in range(30):
        data.append([((random.random(),random.random()),(random.random(),random.random())),random.random()])
    
    gps_arr = [random.randrange(-100000,100000)/4,random.randrange(-100000,100000)/4,random.randrange(0,300)]
    cam_arr = [random.randrange(-180,180),random.randrange(-180,180)]
    output = scan_for_weeds(gps_arr,cam_arr,array_of_weeds_from_ai=data)
    output = output[0]
    for i in output:
        for j in i:
            print(j[0],"\n",j[1])


# max,min,inc

# global_heat_map = os.listdir
# def get_the_max_cords():
# # names = []
# os.chdir("all_past_heatmaps")
# for i in os.listdir():
#     file = open(i)
#     name = file.readlines(1)
#     file.close()
#     name = name[0]
#     name = eval(name)
#     name = name[0]
#     names.append(name)    
#     print(name)
    
    
    
    
# names = os.listdir()
# names = names[1:]
# names = names[:-1]
# new_names = []
# for i in range(len(names)):
#     temp = names[i][0:-4]
#     # temp = eval(temp[i])
#     temp.replace("[[","")
#     temp.replace("]]","")
#     temp = eval(temp)
#     new_names.append(temp)
    
# names = new_names

print(names)

# max_x1 = names[0][0][0][0]
# max_x2 = names[0][0][1][0]
# max_y1 = names[0][0][0][1]
# max_y2 = names[0][0][1][1]

max_x1 = names[0][0][0]
max_x2 = names[0][1][0]
max_y1 = names[0][0][1]
max_y2 = names[0][1][1]

for i in names:
    
    max_x1 = min(max_x1,i[0][0])
    max_x2 = max(max_x2,i[1][0])
    max_y1 = min(max_x1,i[0][1])
    max_y2 = max(max_x2,i[1][1])
    # print(i)
    
print("max x1",max_x1)
print("max x2",max_x2)
print("max y1",max_y1)
print("max y2",max_y2)


def conbine_arrays(og_array_file,add_array_file):
    pass

    



def conbine_arrays(og_array_file,add_array_file):
    pass

    



os.chdir("../")

try:
    global_heat_map_file = open("global_heat_map.csv","x+")
    global_heat_map_file.writelines()
    global_heat_map_file.writelines()
    print(max_x1,",",max_x2,"\n",max_x2,",",max_y1)
    global_heat_map_file.write("""max_x1,max_x2,max_x2,max_y1\n""")
    global_heat_map_file.write("""max_x1,max_x2,max_x2,max_y1\n""")
    to_write = f"{max_x1},{max_x2},{max_x2},{max_y1}"
    txt_global_heat_map_file.write(to_write)
    del(to_write)
    global_heat_map = np.zeros(row_column := (int(abs(max_x1-max_x2)),int(abs(max_y1-max_y2))),dtype=float)
    txt_global_heat_map_file.close()
    global_heat_map_file.close()
except FileExistsError:
    global_heat_map_file = open("global_heat_map.csv","r")
    txt_global_heat_map_file = open("global_heat_map.txt","r")
    global_heat_map_old = np.array(global_heat_map_file.readline())
# global_heat_map = global_heat_map_file.readline()