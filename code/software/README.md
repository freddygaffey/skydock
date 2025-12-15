# README.md

# Drone Control Software

This project implements a control system for a drone using a finite state machine (FSM) architecture. The software is designed to manage the drone's various states, including takeoff, scanning, and returning to home, while also integrating telemetry and artificial intelligence functionalities.

## Project Structure

```
software
├── fsm
│   ├── __init__.py
│   └── template.py
├── telemetry.py
├── move.py
├── ai.py
├── drone_snapshots.py
├── tests
│   └── test_fsm.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## File Descriptions

### FSM Module (`software/fsm/template.py`)

- **Classes:**
  - `DroneState`: A protocol that defines the interface for drone states with methods `enter`, `update`, and `exit`.
  - `FSM`: Manages the current state of the drone, starting with `OnGroundState`.
  - `Context`: Holds global constants like `take_off_hight` and `scaning_complete`.
  - `OnGroundState`: Represents the drone's state when it is on the ground.
    - `enter()`: Prints a message indicating the drone is on the ground.
    - `update()`: Checks pre-flight conditions and transitions to `TakeOff` if conditions are met.
    - `exit()`: Prints a message indicating the drone is leaving the ground state.
  - `TakeOff`: Represents the drone's takeoff state.
    - `enter()`: Requests permission to take off and executes the takeoff command.
    - `update()`: Checks if the drone has reached the takeoff height and transitions to `Scaning` or `Spraying`.
    - `exit()`: Prints a message indicating takeoff is complete.
  - `Scaning`: Represents the scanning state of the drone.
    - `enter()`: Initializes the scanning process.
    - `update()`: Flies to the next scan point and adds weed detections.
    - `exit()`: Cleans up after scanning.
  - `RetunToHome`: Represents the return-to-home state.
    - `need_to_RTH()`: Placeholder for logic to determine if a return to home is needed.
    - `enter()`: Sets the drone mode to "RTH".
    - `update()`: Ensures the drone remains in "RTH" mode.
  
- **LightState Classes:**
  - `LightState`: A protocol for light states with a `switch` method.
  - `OnState`: Represents the light being on.
    - `switch()`: Switches the light to `OffState`.
  - `OffState`: Represents the light being off.
    - `switch()`: Switches the light to `OnState`.
  - `Bulb`: Represents a light bulb that can switch states.

### Other Modules

- **Telemetry (`software/telemetry.py`)**: Contains functionality related to telemetry data for the drone, including classes and methods for handling telemetry messages and data.
  
- **Movement (`software/move.py`)**: Handles movement commands for the drone, including methods for arming the drone and taking off to a specified height.
  
- **Artificial Intelligence (`software/ai.py`)**: Contains AI-related functionality for processing images from the drone's camera and detecting objects like weeds.
  
- **Drone Snapshots (`software/drone_snapshots.py`)**: Manages snapshots of the drone's telemetry data, including classes for storing and processing this data.
  
- **Tests (`software/tests/test_fsm.py`)**: Contains unit tests for the FSM implementation, ensuring that the behavior of the various drone states and state transitions occur as expected.

### Configuration Files

- **`software/pyproject.toml`**: Configuration file for Python projects, specifying project metadata, dependencies, and build system requirements.
  
- **`software/requirements.txt`**: Lists the dependencies required for the project, which can be installed using pip.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the drone control software, execute the main script or integrate it into your drone's control system. Ensure that all necessary permissions and configurations are set up for the drone's operation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.