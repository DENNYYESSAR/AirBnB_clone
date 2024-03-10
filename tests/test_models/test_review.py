#!/usr/bin/python3
"""Defines unittests for models/review.py."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for Review class
    """
    def test_instance_creation(self):
        """
        Test creation of Review instance
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attributes(self):
        """
        Test attributes of Review instance
        """
        review = Review(place_id="123", user_id="456", text="Great place!")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
