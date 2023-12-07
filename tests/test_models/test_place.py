# tests/test_models/test_place.py

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        place = Place()
        self.assertIsInstance(place, Place)

    # Add more tests as needed for Place class

if __name__ == '__main__':
    unittest.main()
