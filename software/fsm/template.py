from typing import Protocol
import time

from telemetry import telm_singleton, GroundStaionMessages
from move import move_singleton 
from ai import ai_storage_singleton, Camera
from drone_snapshots import drone_telm_stapshot, ScanningPlanner,WeedStorage,Weed

class DroneState(Protocol):
    def enter(self): ...
    def update(self): ...
    def exit(self): ...

class FSM:
    def __init__(self):
        self.state = OnGroundState()

class OnGroundState(DroneState):
    def enter(self) -> None:
        print("Drone is on the ground.")
    
    def update(self):
        # if telm_singleton.run_pre_flight_checks() == True and "takeoff" in ground_station_commands.commands[0]:
        if telm_singleton.run_pre_flight_checks() == True and GroundStaionMessages.ask_gc_question("Permission to move to takeoff state?"):
            move_singleton.arm_and_take_off_to_hight(GroundStaionMessages.float_messages["takeoff_hight"])
            return TakeOff()
        else:
            time.sleep(3)
            return None

    def exit(self) -> None:
        print("Drone is leaving Ground state.")

class TakeOff(DroneState):
    def enter(self):
        if GroundStaionMessages.ask_gc_question(f"Permission to arm and takeoff to {GroundStaionMessages.float_messages["takeoff_hight"]} m ?"):
            move_singleton.arm_and_take_off_to_hight(GroundStaionMessages.float_messages["takeoff_hight"])
        
    def update(self):
        check_alt = round(drone_telm_stapshot.altitude_rel_home,1) == GroundStaionMessages.float_messages["takeoff_hight"]
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

    def update(self):
        """
        while true
            fly to next scan point 
            while scanning add detections 
        """
        # update poss
        loc = drone_telm_stapshot.longitude , drone_telm_stapshot.latitude
        next_point = ScanningPlanner.next_point(loc)
        if next_point is None:
            Context.scaning_complete = True
            return Spraying()
        move_singleton.fly_to_point(lat=loc[1],lon=loc[0],alt_above_home=ScanningPlanner.scan_alt)

        # add weed detections
        frame = ai_storage_singleton.get_frames_in_time_period(less_past=time.time_ns(),more_past=Weed.time_last_mass_updated)
        new_weeds = Weed.retun_all_new_valid_weeds(drone_state=drone_telm_stapshot,frame=frame,camera=Camera)

        WeedStorage.add_weed(new_weeds)


    def exit(self):
        pass

class RetunToHome(DroneState):
    @classmethod
    def need_to_RTH(cls):
        # TODO: actally do this
        pass

    def enter(self):
        move_singleton.set_mode("RTH")
    def update(self):
        if move_singleton.get_mode() != "RTH":
            move_singleton.set_mode("RTH")
        

class Spraying:
# class SprayFSM:
# class SprayFlyToPoint(DroneState):
# class SprayHomeOverWeed(DroneState):
# class SpraySpray(DroneState):




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
