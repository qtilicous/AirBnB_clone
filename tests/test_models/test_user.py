# tests/test_models/test_user.py

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User()
        self.assertIsInstance(user, User)

    # Add more tests as needed for User class

if __name__ == '__main__':
    unittest.main()
