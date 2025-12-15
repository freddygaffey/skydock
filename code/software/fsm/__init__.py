# Contents of /software/fsm/__init__.py

"""
This package provides a finite state machine (FSM) implementation for controlling a drone.
It includes various states that the drone can be in, such as OnGroundState, TakeOff, 
Scanning, and ReturnToHome. Each state implements the DroneState protocol, which defines 
the methods required for state transitions.

Modules:
- template: Contains the FSM implementation and state definitions.
"""