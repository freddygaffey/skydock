from ai import ai_storage_singleton, camera_prams
from telemetry import telm_singleton
from drone_snapshots import drone_telm_stapshot 
from move import move_singleton

import time
import threading

import sys

class Tee:
    def __init__(self, filename):
        self.file = open(filename, "w")
        self.stdout = sys.stdout

    def write(self, data):
        self.stdout.write(data)
        self.file.write(data)

    def flush(self):
        self.stdout.flush()
        self.file.flush()

sys.stdout = Tee("drone_log.txt")

def find_v_for_a_given_distance(dist):
    """dist in m retuns m/s"""
    if dist < 0:
        is_neg = -1
    else:
        is_neg = 1
    
    dist = abs(dist)

    if dist >= 10:
        return 3 * is_neg 
    else:
        return ((dist) ** 0.5) * is_neg 
#---------------------
# constans 
print_v_bool = False
change_mode = True
lock = threading.Lock()

#---------------------

def print_v():
    while True:
        with lock:
            temp_thread_bool = print_v_bool

        if temp_thread_bool:
            print("drone current x volocity is ",drone_telm_stapshot.velocity_x)
            print("drone current y volocity is ",drone_telm_stapshot.velocity_y)
        time.sleep(0.03)
threading.Thread(target=print_v).start()


time.sleep(1)
ai_storage_singleton.start_ai()
while True:
    time.sleep(0.06)

    frame = ai_storage_singleton.get_last_frames(1)

    if drone_telm_stapshot.enabel_homing_and_autonomy == False:
        if move_singleton.get_mode() == "GUIDED":
            move_singleton.set_mode("POSHOLD")
    with lock:
        print_v_bool = False
    new_frame = []
    for i in frame:
        if frame is None:
            continue
        elif frame.label not in ["traffic light", "sports ball", "frisbee"]:
            continue
        else:
            new_frame.append(i)
    max_conf = 0
    max_det = None
    for i in new_frame:
        if i.confidence > max_conf:
            max_conf = i.confidence
            max_det = i
        


    # frame = frame[0]

    with lock:
        print_v_bool = True

    dist_x_ned = camera_prams.y_dist_per_pix_per_meter * frame.get_the_vector_center()[1]  # Camera Y → Drone X
    dist_y_ned = -camera_prams.x_dist_per_pix_per_meter * frame.get_the_vector_center()[0]  # -Camera X → Drone Y

    print(f"dist to weed in x dir {dist_x_ned}")
    print(f"dist to weed in y dir {dist_y_ned}")

    vx = find_v_for_a_given_distance(dist_x_ned)
    vy = find_v_for_a_given_distance(dist_y_ned)

    print(f"vlolocity x {vx}")
    print(f"vlolocity y {vy}")

    # speed = dist / time 
    # dist/speed = time 
    try:
        x_time = abs(dist_x_ned / vx)
        y_time = abs(dist_y_ned / vy)
    except ZeroDivisionError:
        continue
    
    max_time = min(x_time,y_time)

    if int(time.time()) % 2 == 0:
        ai_storage_singleton.take_photo_function()

    if drone_telm_stapshot.enabel_homing_and_autonomy and move_singleton.get_mode() == "POSHOLD":
        change_mode = True
    elif drone_telm_stapshot.enabel_homing_and_autonomy and move_singleton.get_mode() == "GUIDED":
        move_singleton.move_volocity_until_stop_or_max_time((vx,vy,0),max_time,change_yaw=True)
    elif change_mode == True:
        print("change mode to gided")
        move_singleton.set_mode("GUIDED")
        change_mode = False
