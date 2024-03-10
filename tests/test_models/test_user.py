#!/usr/bin/python3
"""Defines unittests for models/user.py."""

import unittest
from models.user import User
import os
import models


class TestUser(unittest.TestCase):
    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_update_attributes(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict(self):
        user = User()
        user_dict = user.to_dict()

        self.assertTrue(isinstance(user_dict, dict))
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")

    def test_from_dict(self):
        user_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**user_data)

        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')


if __name__ == '__main__':
    unittest.main()
