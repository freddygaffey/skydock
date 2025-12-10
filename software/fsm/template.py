from typing import Protocol


from telemetry import telm_singleton
from move import move_singleton 
from ai import ai_storage_singleton, camera_prams
from drone_snapshots import drone_telm_stapshot, ground_station_commands

class DroneState(Protocol):
    def enter(self, drone): ...

    def update(self, drone): ...

    def exit(self, drone): ...

class OnGroundState(DroneState):
    def enter(self, drone) -> None:
        print("Drone is on the ground.")
    
    def update(self, drone) -> None:
        if telm_singleton.run_pre_flight_checks() == True and "takeoff" in ground_station_commands.commands[0]:
            try: 
                hight = int(ground_station_commands.commands[0][-1])
            except ValueError:
                hight = 2 # defaut take off hight 
            move_singleton.arm_and_take_off_to_hight(hight)



    def exit(self, drone) -> None:
        print("Drone is leaving Ground state.")


class 




class LightState(Protocol):
    def switch(self, bulb) -> None:
        ...

class OnState(LightState):
    def switch(self,bulb) -> None:
        bulb.state = OffState()
        print("The light is on.")
    
class OffState(LightState):
    def switch(self,bulb) -> None:
        bulb.state = OnState()
        print("The light is off.")

class Bulb:
    def __init__(self):
        self.state = OnState()
    
    def switch(self):
        self.state.switch(self)

if __name__ == "__main__":
    bulb = Bulb()
    bulb.switch()  # The light is off.
    bulb.switch()  # The light is on.
    