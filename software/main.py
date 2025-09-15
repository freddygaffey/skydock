from drone import *
# from get_cam_stream_and_run_ai 




uav = Drone_mvp()
print(uav.get_batt_v())
print(uav.get_batt_mah_left())
while 1:
    print(uav.get_gimbal_attitude())



