from dataclasses import dataclass, field
import time
import math

@dataclass
class DroneStateForHoming:
    time_updated_GLOBAL_POSITION_INT: float = 0
    # Global position in degrees/meters
    latitude: float = 0
    longitude: float = 0
    altitude_rel_home: float = 0 # rel form ground

    # Velocity in m/s in local NED frame
    velocity_x: float = 0.0
    velocity_y: float = 0.0
    velocity_z: float = 0.0

    enabel_homing_and_autonomy: bool = False

    # gimble orintaion

    heading: float = 0
    def pass_msg(self,msg):
        if msg is None:
            return 0

        if msg._type == "GLOBAL_POSITION_INT":
        # if True:
            self.time_updated_GLOBAL_POSITION_INT = msg.time_boot_ms / 1000.0  # ms → s

            # Position
            self.latitude = msg.lat / 1e7
            self.longitude = msg.lon / 1e7
            self.altitude_rel_home = msg.relative_alt / 1000.0  # mm → m

            # Velocity
            self.velocity_x = msg.vx / 100.0  # cm/s → m/s
            self.velocity_y = msg.vy / 100.0
            self.velocity_z = msg.vz / 100.0

            # Heading 65535 = unknown)
            self.heading = msg.hdg / 100.0 if msg.hdg != 65535 else None

        if msg._type == "SERVO_OUTPUT_RAW":
            if msg.servo8_raw <= 1000:
                self.enabel_homing_and_autonomy = False
            if msg.servo8_raw > 1000:
                self.enabel_homing_and_autonomy = True
                
drone_telm_stapshot = DroneStateForHoming()

@dataclass
class GroundStationCommands:
    """
    posiabel messages:
    gc: takeoff
    gc: takeoff {int < 10}
    
    """
    commands: list = field(default_factory=list)
    times: list = field(default_factory=list)
    # commands: list = []
    # times: list = []

    def pass_message(self,message):
        # STATUSTEXT {severity : 6, text : gc: this is a message from the gc, id : 0, chunk_seq : 0}
        if message._type == "STATUSTEXT" and "gc:" in message.text:
            self.times.insert(0, time.time_ns())
            self.commands.insert(0,message.text)

ground_station_commands = GroundStationCommands()

@dataclass
class Weed:
    location: tuple[float,float]
    confidence: int
    sprayed: bool = False
    path_to_photo: str = "have a look for it youself you lazzy person"

class WeedStorage:
    all_weeds = [] # array of weed obgects

    @classmethod
    def _haversine_distance(cls, p1, p2):
        lon1, lat1 = p1
        lon2, lat2 = p2
        
        R = 6371000  # Earth radius in meters

        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        a = (math.sin(dphi/2)**2 +
            math.cos(phi1) * math.cos(phi2) * math.sin(dlon/2)**2)

        return R * (2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))

    @classmethod
    def next_weed_to_spray(cls,drone_loc):
        """this will retun the closet weed can be made more effint later"""
        min_dist = float("inf")
        weed = None

        for i in cls.all_weeds:
            if i.sprayed:
                continue
            if (dist := cls.__haversine_distance(i.location,drone_loc)) < min_dist:
                min_dist = dist
                weed = i
        return weed
                
    @classmethod
    def mark_as_sprayed(cls,weed_obj):
        for i in range(len(cls.all_weeds)):
            weed_enu = cls.all_weeds[i] 
            if weed_obj is weed_enu:
                weed_enu.sprayed = True
                return weed_enu

    @classmethod
    def add_weed(cls,weed):
        cls.all_weeds.append(weed)

class Scanning:
    def __init__(self,scan_path): 
        self.scan_palth = scan_path # [(long,lat,alt_from_home),] this is on order of the scanning palth
        self.scan_precision = 2 # in meter
        self.points_visited = []

    def next_point(self):
        for i in self.scan_path:
            if i not in self.points_visited:
                return i


    def point_compleate(self,point):
        self.points_visited.append(point)


        
        