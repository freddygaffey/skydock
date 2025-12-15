from typing import List, Dict, Any

class DroneTelemetrySnapshot:
    """Class to represent a snapshot of the drone's telemetry data."""
    
    def __init__(self, altitude: float, longitude: float, latitude: float, timestamp: float):
        self.altitude = altitude  # Altitude of the drone in meters
        self.longitude = longitude  # Longitude of the drone's position
        self.latitude = latitude  # Latitude of the drone's position
        self.timestamp = timestamp  # Timestamp of the snapshot

class TelemetryStorage:
    """Class to manage storage and retrieval of telemetry snapshots."""
    
    def __init__(self):
        self.snapshots: List[DroneTelemetrySnapshot] = []  # List to store telemetry snapshots

    def add_snapshot(self, snapshot: DroneTelemetrySnapshot) -> None:
        """Add a new telemetry snapshot to the storage."""
        self.snapshots.append(snapshot)

    def get_latest_snapshot(self) -> DroneTelemetrySnapshot:
        """Retrieve the latest telemetry snapshot."""
        if self.snapshots:
            return self.snapshots[-1]
        raise ValueError("No telemetry snapshots available.")

    def get_all_snapshots(self) -> List[Dict[str, Any]]:
        """Retrieve all telemetry snapshots as a list of dictionaries."""
        return [
            {
                "altitude": snapshot.altitude,
                "longitude": snapshot.longitude,
                "latitude": snapshot.latitude,
                "timestamp": snapshot.timestamp,
            }
            for snapshot in self.snapshots
        ]