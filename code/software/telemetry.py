# telemetry.py

"""
This module contains functionality related to telemetry data for the drone.
It includes classes and methods for handling telemetry messages and data.
"""

class TelemetryMessage:
    """
    Represents a telemetry message from the drone.
    
    Attributes:
        timestamp (float): The time at which the telemetry data was recorded.
        altitude (float): The altitude of the drone.
        latitude (float): The latitude position of the drone.
        longitude (float): The longitude position of the drone.
    """

    def __init__(self, timestamp: float, altitude: float, latitude: float, longitude: float):
        self.timestamp = timestamp
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

class TelemetryHandler:
    """
    Handles the processing and storage of telemetry messages.
    
    Methods:
        add_message(message: TelemetryMessage): Adds a telemetry message to the storage.
        get_latest_message() -> TelemetryMessage: Retrieves the latest telemetry message.
    """

    def __init__(self):
        self.messages = []

    def add_message(self, message: TelemetryMessage):
        """Adds a telemetry message to the storage."""
        self.messages.append(message)

    def get_latest_message(self) -> TelemetryMessage:
        """Retrieves the latest telemetry message."""
        if self.messages:
            return self.messages[-1]
        return None

# Additional classes and methods can be added here to extend telemetry functionality.