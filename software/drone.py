import threading
from telemetry import telm_singleton
from move import move_singleton 
from ai import ai_storage_singleton, camera_prams
from drone_state_homing import drone_state


class drone():
    def __init__(self):
        pass

    def home_over_weed(self):
        def one_homing_command():
            


