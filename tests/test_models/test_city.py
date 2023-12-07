# tests/test_models/test_city.py

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_city_creation(self):
        city = City()
        self.assertIsInstance(city, City)

    # Add more tests as needed for City class

if __name__ == '__main__':
    unittest.main()
