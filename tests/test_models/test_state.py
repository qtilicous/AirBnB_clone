# tests/test_models/test_state.py

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_state_creation(self):
        state = State()
        self.assertIsInstance(state, State)

    # Add more tests as needed for State class

if __name__ == '__main__':
    unittest.main()
