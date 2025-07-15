import math
import  numpy as np
# x,y,z = 100,0,0
# xo,yo,zo = 0,0
# cam_angle = [xo,yo]
# cam_gps_pos = [x,y,z]

def find_gps_from_angle_and_gps(cam_gps,cam_angle):
    rtn = []
    for i in cam_angle:
        rtn.append(math.tan(math.radians(i))*cam_gps[-1])
        
    return (rtn[0],rtn[1],cam_gps[-1])

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
# import opencv
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
      
   
    round_amount = 1
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
    max_and_min = [[TL, TR],
                [BL, BR]]
    # print(max_and_min)
    
    # TODO: get the array_of_weeds_from_ai 
    # and work out there pos and populata a array at incments 
    # of the prestion and weeds with eht acruesy
    # print(max_and_min)

    # Fix the heat_map line: convert floats to ints, and fix range usage
    heat_map = np.zeros((abs(int(TL[0]-TR[0]*multiply_amount)),abs(int(TL[1]-BR[1])*multiply_amount)),dtype=int)
    
    row_length = abs(int(round(TL[0]-TR[0])*multiply_amount))
    column_length = abs(int(round(TL[1]-BR[1])*multiply_amount))
    # print(heat_map)
    # amount_to_change_row = get_the_arr_index_range_betwen_nums(0.71119871735572815,0.996639609336853,10)
    # amount_to_change_column = get_the_arr_index_range_betwen_nums(0.1119871735572815,0.996639609336853,10)
    # TODO: for testing change later
    # heat_map = np.zeros((10,10),dtype=float)
    

    for  box in data:
        amount_to_change_row = get_the_arr_index_range_betwen_nums(box[0][0][0],box[0][1][0],row_length)
        print("amout to change row", amount_to_change_row)
        amount_to_change_column = get_the_arr_index_range_betwen_nums(box[0][0][1],box[0][1][1],row_length)
        print("amout to change comlmb", amount_to_change_column)

        confidence = box[1]
        
        for j in range(amount_to_change_row[0],amount_to_change_row[1]):
            
            heat_map_row = heat_map[j]
            change_arr = np.zeros(abs(amount_to_change_row[0]-amount_to_change_row[1]))
            inc = 0
            for i in heat_map_row[amount_to_change_row[0]:amount_to_change_row[1]]: change_arr[inc] = max(i,confidence);inc += 1
            print(heat_map_row)
            heat_map_row[amount_to_change_row[0]:amount_to_change_row[1]] = change_arr
            heat_map[j] = heat_map_row
        print("_"*20)
        for i in heat_map:
            jr = []
            for j in i:
                jr.append(int(round(j,3)))
            print(jr)
    return heat_map
    
    
    
    # get the real gps cords for all the the corners


    

    
    
    










# print(find_weed_position(cam_angle=cam_angle,cam_gps=cam_gps_pos))




# tl,br = (x1,y1),(x2,y2)


data =[[((0.04162254184484482, 0.21119871735572815), (0.8885539770126343, 0.996639609336853)), 0.7875788807868958], [((0.7283291816711426, 0.290351927280426), (0.8815857768058777, 0.4850154519081116)), 0.517029881477356], [((0.5658160448074341, 0.26361513137817383), (0.6699718236923218, 0.39314574003219604)), 0.47284382581710815], [((0.006414508912712336, 0.0), (0.9964765310287476, 0.9930207133293152)), 0.8281115889549255], [((0.1459130346775055, 0.19878216087818146), (0.19077768921852112, 0.4261070787906647)), 0.3097056746482849], [((0.2360641211271286, 0.17753943800926208), (0.2861242890357971, 0.4116947054862976)), 0.2977413535118103], [((0.7989784479141235, 0.14989562332630157), (0.998578667640686, 0.2129984349012375)), 0.26732638478279114], [((0.0017961502308025956, 0.02941570244729519), (0.9973451495170593, 0.9976823925971985)), 0.8736827373504639], [((0.04335775226354599, 0.25808602571487427), (0.8714057803153992, 0.9981401562690735)), 0.8167221546173096], [((0.06162078306078911, 0.782511830329895), (0.2045682966709137, 0.9092723727226257)), 0.37147852778434753], [((0.007508277893066406, 0.051354121416807175), (0.9984729886054993, 0.999559223651886)), 0.8505475521087646]] 
# 
# [[(
#     (43.715476989746094, 281.22076416015625), (76.88262939453125, 361.60272216796875)),0.282327800989151],
# [((3.39315185546875, 249.7642364501953), (44.88355255126953,365.84600830078125)), 0.27081629633903503],
# [((0.50506591796875, 35.005615234375), (635.240234375, 69.31201171875)), 0.8880456686019897],
# [((0.615478515625, 69.07470703125), (557.4205322265625, 640.0)), 0.8425973653793335], 
# [((8.7088623046875, 11.181884765625), (638.83740234375, 636.0928955078125)), 0.7892356514930725], 
# [((64.19122314453125, 4.4300537109375), (638.8636474609375, 638.8258056640625)), 0.8417742848396301], 
# [((4.7208251953125, 24.21331787109375), (632.30859375, 638.7199096679688)), 0.8058953285217285], 
# [((0.352935791015625, 529.0706787109375), (172.39254760742188, 639.6697998046875)), 0.6555260419845581], 
# [((3.89556884765625, 0.21559906005859375), (537.0784301757812, 106.75636291503906)), 0.6303648352622986], 
# [((0.2654609680175781, 394.982666015625), (45.79912567138672, 448.7752685546875)), 0.3240744471549988], 
# [((379.10589599609375, 584.20947265625), (603.4104614257812, 639.6546630859375)), 0.29115545749664307], 
# [((378.3924560546875, 540.166015625), (603.31201171875, 639.621826171875)), 0.2662797272205353], 
# [((3.4693603515625, 48.55462646484375), (638.8574829101562, 639.8831176757812)), 0.8731228113174438], 
# [((0.93804931640625, 13.692138671875), (638.9559936523438, 638.79736328125)), 0.8713268041610718], 
# [((104.033447265625, 67.34539794921875), (639.2037353515625, 638.6841430664062)), 0.8252782821655273], 
# [((30.00616455078125, 1.41162109375), (638.0719604492188, 637.4871826171875)), 0.8094877004623413], 
# [((153.20831298828125, 112.922607421875), (188.40707397460938, 267.23919677734375)), 0.3956886827945709]]

# chat gpt 
converted = []

for box, confidence in data:
    # Convert the bounding box to a numpy array of floats
    # Flatten the two coordinate tuples into one array [x1, y1, x2, y2]
    arr = np.array([*box[0], *box[1]], dtype=float)
    # confidence is already a float
    converted.append([arr, float(confidence)])
    

scan_for_weeds([0,0,100],[45,45],array_of_weeds_from_ai=data)
