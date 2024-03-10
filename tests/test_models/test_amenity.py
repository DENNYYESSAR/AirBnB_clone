#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class
    """
    def test_instance_creation(self):
        """
        Test creation of Amenity instance
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """
        Test attributes of Amenity instance
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
