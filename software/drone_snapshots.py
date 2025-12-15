from dataclasses import dataclass, field
import time
import math
from ai import ai_storage_singleton

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

    gimble_orintaion = 0 # 0 is pointing down 
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



class Weed:
    min_confidence = 0.2
    allowed_labels = ["sports_ball"] 
    time_last_mass_updated = time.time_ns()

    @classmethod
    def retun_all_new_valid_weeds(cls,drone_state,frame,camera):
        cls.time_last_mass_updated = time.time_ns()
        class_instanses_to_add = []
        for detection in frame:
            if detection.confidence >= cls.min_confidence and detection.lable in cls.allowed_labels:
                class_instance = cls(drone_state,detection,camera)
                class_instanses_to_add.append(class_instance)
        
        return class_instanses_to_add           


    def __init__(self,drone_state,detection,camera):
        # self.location = [drone_state.longitude, drone_state.latitude]
        self.drone_state = drone_state 
        self.detection = detection
        self.camera = camera
        self.confidence = detection.confidence
        sprayed: bool = False
        self.path_to_photo = detection.path_to_photo
        self.weed_loc = self.find_loc()

    def find_loc(self):
        drone_lon, drone_lat = drone_loc = [self.drone_state.longitude, self.drone_state.latitude]
        drone_yaw = self.drone_state.heading
        droen_alt = self.drone_state.altitude_rel_home
        px,py = self.detection.get_vector_to_center()
        x_dist  = self.camera.x_dist_per_pix_per_meter * droen_alt * px 
        y_dist = self.camera.y_dist_per_pix_per_meter * droen_alt * py

        heading_rad = math.radians(drone_yaw)

        # some fancy vecrot rotate equation
        north_offset = y_dist * math.cos(heading_rad) - x_dist * math.sin(heading_rad)
        east_offset  = y_dist * math.sin(heading_rad) + x_dist * math.cos(heading_rad)

        # Convert meters → latitude/longitude
        weed_lat = drone_lat  + north_offset / 111_320
        weed_lon = drone_lon + east_offset / (111_320 * math.cos(math.radians(drone_lat)))

        return weed_lon, weed_lat

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

        distance_between_the_2_points = R * (2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))
        return distance_between_the_2_points


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
        if type(weed) == list: cls.all_weeds.extend(weed)
        else: cls.all_weeds.append(weed)

class ScanningPlanner:
    # self.scan_palth = scan_path # [(long,lat,alt_from_home),] this is on order of the scanning palth
    scan_precision = 2 # in meter
    points_visited = []
    scan_alt = 10
        

    @classmethod
    def next_point(cls,current_location):
        # TODO: make the not use recuton as it can be bad but it will be fine for now
        pen_next_point = None
        for i in cls.scan_path:
            if i not in cls.points_visited:
                pen_next_point = i
                break
        if pen_next_point is None:
            return None
        if cls._haversine_distance(pen_next_point,current_location) < cls.scan_precision:
            cls.point_compleate(pen_next_point)
            return cls.next_point(current_location)
        else:
            return pen_next_point 

    @classmethod
    def point_compleate(cls,point):
        cls.points_visited.append(point)
        


    def _haversine_distance(cls, p1, p2):
        lon1, lat1 = p1
        lon2, lat2 = p2
        
        R = 6371000  # Earth radius in meters

        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        a = (math.sin(dphi/2)**2 +
            math.cos(phi1) * math.cos(phi2) * math.sin(dlon/2)**2)

        distance_between_the_2_points = R * (2 * math.atan2(math.sqrt(a), math.sqrt(1-a)))
        return distance_between_the_2_points

        