#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for City class
    """
    def test_instance_creation(self):
        """
        Test creation of City instance
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attributes(self):
        """
        Test attributes of City instance
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
