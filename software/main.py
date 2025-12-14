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

if "__main__" == __name__:
    print_v_and_det = False
    ai_storage_singleton.start_ai()
    enabe_homing_last_state = False
    # telm_singleton.start_automatic_updates()
    time.sleep(0.5)
    def print_v():
        while True:
            if print_v_and_det:
                print("drone current v x",drone_telm_stapshot.velocity_x)
                print("drone current v y",drone_telm_stapshot.velocity_y)
                time.sleep(0.02)
    print_v_thread = threading.Thread(target=print_v)
    print_v_thread.start()
    while True:
        time.sleep(0.07)
        detection = None
        last_frame = ai_storage_singleton.get_last_frames(1)
        try:
            last_frame = last_frame[0]
        except IndexError:
            continue
        new_frame = [] 
        for i in last_frame:
            if i.label in ["traffic light", "sports ball", "frisbee"]:
                new_frame.append(i)
            else:
                pass
                # print(f"discarding {i.label}")

        last_frame = new_frame

        if not last_frame:
            print_v_and_det = False
            continue

        array_of_confidences = []
        for i in last_frame:
            array_of_confidences.append(i.confidence)

        for i in last_frame:
            if i.confidence == max(array_of_confidences):
                detection = i
                print_v_and_det = False
                break
        # print(detection)
        print_v_and_det = True
        if detection.confidence < 0.4:
            continue 
        print(ai_storage_singleton.get_last_frames(2),"the detection")
        print(detection.label)
        # Transform camera coordinates to match the drone's NED coordinate system
        dist_x_ned = camera_prams.y_dist_per_pix_per_meter * detection.get_the_vector_center()[1]  # Camera Y → Drone X
        dist_y_ned = -camera_prams.x_dist_per_pix_per_meter * detection.get_the_vector_center()[0]  # -Camera X → Drone Y
        print(f"{dist_x_ned = }")
        print(f"{dist_y_ned = }")
        vx = find_v_for_a_given_distance(dist_x_ned)
        vy = find_v_for_a_given_distance(dist_y_ned)

        print(f"{vx = }")
        print(f"{vy = }")
        # move_singleton.send_volocity_command_yaw_stay_same(vx,vy,0)
        v_tuple = (vx,vy,0)

        if drone_telm_stapshot.enabel_homing_and_autonomy:
            if move_singleton.get_mode() == "GUIDED":
                pass
            else:
                move_singleton.set_mode("GUIDED")

            ai_storage_singleton.take_photo_function()
            move_singleton.move_volocity_until_stop_or_max_time(v_tuple,0.3,change_yaw=False)
            print("sending the move command","-"*20)
        elif enabe_homing_last_state:
            move_singleton.stop_volocity_command()
            move_singleton.set_mode("POSHOLD")

        enabe_homing_last_state = drone_telm_stapshot.enabel_homing_and_autonomy     
            
        

        # move_singleton.send_displacement_command_yaw_stay_same(dist_x,dist_y,0)
        


        # NEED TO CALL RPICAM-HELLOW TO RESET THE CAMERA THREDS BECAUSE OF THE MESSY SHUTDOWN
