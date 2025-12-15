class MoveSingleton:
    def arm_and_take_off_to_hight(self, height: float) -> None:
        """
        Arms the drone and initiates the takeoff to the specified height.

        Parameters:
        height (float): The height in meters to which the drone should ascend.
        """
        print(f"Arming the drone and taking off to {height} meters.")

    def fly_to_point(self, lat: float, lon: float, alt_above_home: float) -> None:
        """
        Commands the drone to fly to a specified geographical point.

        Parameters:
        lat (float): The latitude of the target point.
        lon (float): The longitude of the target point.
        alt_above_home (float): The altitude above the home position in meters.
        """
        print(f"Flying to point (Lat: {lat}, Lon: {lon}, Alt: {alt_above_home})")

    def set_mode(self, mode: str) -> None:
        """
        Sets the flight mode of the drone.

        Parameters:
        mode (str): The mode to set for the drone (e.g., 'RTH' for Return to Home).
        """
        print(f"Setting drone mode to {mode}.")

    def get_mode(self) -> str:
        """
        Retrieves the current flight mode of the drone.

        Returns:
        str: The current flight mode of the drone.
        """
        return "Current mode"  # Placeholder for actual mode retrieval logic

# Singleton instance for global access
move_singleton = MoveSingleton()