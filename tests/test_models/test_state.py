#!/usr/bin/python3
"""Defines unittests for models/state.py."""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for State class
    """
    def test_instance_creation(self):
        """
        Test creation of State instance
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")

    def test_attributes(self):
        """
        Test attributes of State instance
        """
        state = State(name="California")
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
