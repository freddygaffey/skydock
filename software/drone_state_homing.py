from dataclasses import dataclass

@dataclass
class DroneStateHoming:
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
                

drone_state = DroneStateHoming()
