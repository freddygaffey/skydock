# from ai import ai_storage_singleton, camera_prams
# from telemetry import telm_singleton
# from drone_state_homing import drone_state
# from move import move_singleton

# import time

# if "__main__" == __name__:
#     telm_singleton.start_automatic_updates()
#     ai_storage_singleton.start_ai()

#     while True:
#         detection = None
#         last_frame = ai_storage_singleton.get_last_frames(1)

#         # Ensure last_frame is valid
#         if not last_frame or not isinstance(last_frame, list):
#             continue
#         try:
#             last_frame = last_frame[0]
#         except IndexError:
#             continue

#         # Filter out unwanted labels
#         new_frame = []
#         for i in last_frame:
#             if i.label not in ["traffic light", "sports ball", "frisbee"]:
#                 new_frame.append(i)
#         last_frame = new_frame

#         if not last_frame:
#             continue

#         # Find the detection with the highest confidence
#         detection = max(last_frame, key=lambda x: x.confidence, default=None)
#         if detection is None or not hasattr(detection, "confidence") or not hasattr(detection, "get_vector_to_center"):
#             continue

#         # Skip low-confidence detections
#         if detection.confidence < 0.4:
#             continue

#         # Calculate distances
#         try:
#             vector_to_center = detection.get_vector_to_center
#             dist_x = camera_prams.x_dist_per_pix_per_meter * vector_to_center[0]
#             dist_y = camera_prams.y_dist_per_pix_per_meter * vector_to_center[1]
#             print(f"{dist_x = }")
#             print(f"{dist_y = }")
#         except (TypeError, IndexError, AttributeError):
#             print("Invalid vector_to_center data, skipping detection.")
#             continue

#         # Send move command
#         move_singleton.send_displacement_command_yaw_stay_same(dist_x, dist_y, 0)

#         # Handle user input
#         try:
#             input_value = input("Are you okay to send the above move command? If not, press ^C.")
#         except KeyboardInterrupt:
#             print("Move command canceled by user.")
#             continue


#         # NEED TO CALL RPICAM-HELLOW TO RESET THE CAMERA THREDS BECAUSE OF THE MESSY SHUTDOWN:w



from ai import ai_storage_singleton, camera_prams
from telemetry import telm_singleton
from drone_state_homing import drone_state 
from move import move_singleton



import time


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
    ai_storage_singleton.start_ai()
    telm_singleton.start_automatic_updates()

    while True:
        time.sleep(0.3)
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
                print(f"discarding {i.label}")

        last_frame = new_frame

        if not last_frame:
            continue

        array_of_confidences = []
        for i in last_frame:
            array_of_confidences.append(i.confidence)

        for i in last_frame:
            if i.confidence == max(array_of_confidences):
                detection = i
                break
        # print(detection)

        if detection.confidence < 0.4:
            continue 

        print(detection.label)
        dist_x = camera_prams.x_dist_per_pix_per_meter * detection.get_the_vector_center()[0]
        dist_y = camera_prams.y_dist_per_pix_per_meter * detection.get_the_vector_center()[1]
        print(f"{dist_x = }")
        print(f"{dist_y = }")
        vx = find_v_for_a_given_distance(dist_x)
        vy = find_v_for_a_given_distance(dist_y)

        print(f"{vx = }")
        print(f"{vy = }")
        # move_singleton.send_volocity_command_yaw_stay_same(vx,vy,0)
        v_tuple = (vx,vy,0)
        if drone_state.enabel_homing_and_autonomy:
            move_singleton.move_volocity_until_stop_or_max_time(v_tuple,1,change_yaw=False)


        # move_singleton.send_displacement_command_yaw_stay_same(dist_x,dist_y,0)
        


        # NEED TO CALL RPICAM-HELLOW TO RESET THE CAMERA THREDS BECAUSE OF THE MESSY SHUTDOWN
