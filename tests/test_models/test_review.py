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
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
