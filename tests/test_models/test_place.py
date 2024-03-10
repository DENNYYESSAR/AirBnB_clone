#!/usr/bin/python3
"""Defines unittests for models/place.py."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class
    """
    def test_instance_creation(self):
        """
        Test creation of Place instance
        """
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_attributes(self):
        """
        Test attributes of Place instance
        """
        place = Place(city_id="LA", user_id="123", name="Cozy House",
                      description="A cozy place to stay", number_rooms=2,
                      number_bathrooms=1, max_guest=4, price_by_night=100,
                      latitude=34.0522, longitude=-118.2437,
                      amenity_ids=["wifi", "pool"])
        self.assertEqual(place.city_id, "LA")
        self.assertEqual(place.user_id, "123")
        self.assertEqual(place.name, "Cozy House")
        self.assertEqual(place.description, "A cozy place to stay")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 34.0522)
        self.assertEqual(place.longitude, -118.2437)
        self.assertEqual(place.amenity_ids, ["wifi", "pool"])


if __name__ == '__main__':
    unittest.main()
