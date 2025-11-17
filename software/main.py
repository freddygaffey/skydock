
import time
from ai import ai_storage_instance
from drone import Telemetry

if __name__ == "__main__":
    ai_storage_instance.start_ai()
    drone = Telemetry()

    while True:
        time.sleep(0.001)
        print(ai_storage_instance.get_last_frames())
        print(drone.get_gimbal_attitude())
        
        