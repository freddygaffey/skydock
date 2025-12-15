# test_fsm.py

import unittest
from fsm.template import FSM, OnGroundState, TakeOff, Scaning, Context

class TestFSM(unittest.TestCase):

    def setUp(self):
        self.fsm = FSM()

    def test_initial_state(self):
        self.assertIsInstance(self.fsm.state, OnGroundState)

    def test_on_ground_state_enter(self):
        self.fsm.state.enter()
        # Check if the correct message is printed (you may want to capture stdout)

    def test_on_ground_state_update_to_takeoff(self):
        # Mock the necessary methods and conditions
        Context.take_off_hight = 2
        # Simulate pre-flight checks passing
        # Simulate permission granted
        next_state = self.fsm.state.update()
        self.assertIsInstance(next_state, TakeOff)

    def test_takeoff_state_enter(self):
        self.fsm.state = TakeOff()
        self.fsm.state.enter()
        # Check if the correct message is printed (you may want to capture stdout)

    def test_takeoff_state_update_to_scanning(self):
        self.fsm.state = TakeOff()
        # Simulate reaching the takeoff height
        Context.scaning_complete = False
        next_state = self.fsm.state.update()
        self.assertIsInstance(next_state, Scaning)

    def test_scanning_state_update_complete(self):
        self.fsm.state = Scaning()
        # Simulate scanning completion
        Context.scaning_complete = True
        next_state = self.fsm.state.update()
        self.assertIsInstance(next_state, None)  # Assuming it transitions to None or another state

    def test_return_to_home_state(self):
        # Test the return to home logic
        pass  # Implement this test based on your return to home logic

if __name__ == '__main__':
    unittest.main()