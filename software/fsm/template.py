from typing import Protocol
import time


from telemetry import telm_singleton
from move import move_singleton 
from ai import ai_storage_singleton, camera_prams
from drone_snapshots import drone_telm_stapshot, ground_station_commands

class DroneState(Protocol):
    def enter(self): ...

    def update(self): ...

    def exit(self): ...

class FSM:
    def __init__(self):
        self.state = OnGroundState()

class Context:
    take_off_hight = 2
    scaning_complete = False

class OnGroundState(DroneState):
    def enter(self) -> None:
        print("Drone is on the ground.")
    
    def update(self):
        if telm_singleton.run_pre_flight_checks() == True and "takeoff" in ground_station_commands.commands[0]:
            try: 
                hight = int(ground_station_commands.commands[0][-1])
            except ValueError:
                hight = 2 # defaut take off hight 
            Context.take_off_hight = hight
            move_singleton.arm_and_take_off_to_hight(hight)
            return TakeOff()
        else:
            time.sleep(3)
            return None

    def exit(self) -> None:
        print("Drone is leaving Ground state.")

class TakeOff(DroneState):
    def enter(self):
        move_singleton.arm_and_take_off_to_hight(Context.take_off_hight)

    def update(self):
        check_alt = round(drone_telm_stapshot.altitude_rel_home,1) == Context.take_off_hight
        if check_alt != True:
            return None
        elif Context.scaning_complete:
            return Scaning()
        else:
            return SprayFSM()
        
    def exit(self):
        print("takeoff conpleate")

class Scaning(DroneState):
    def enter(self):
        pass

class RetunToHome(DroneState):
    def enter(self):
        move_singleton.set_mode("RTH")

class SprayFSM:
class SprayFlyToPoint(DroneState):
class SprayHomeOverWeed(DroneState):
class SpraySpray(DroneState):




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
    