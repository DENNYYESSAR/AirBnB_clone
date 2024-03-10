#!/usr/bin/python3
"""Defines unittests for file_storage.py."""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class."""

    def setUp(self):
        """Set up for the tests; this method is called before each test
        function.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test function."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_new_and_all_methods(self):
        """Test the new and all methods."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.storage.new(instance1)
        self.storage.new(instance2)
        all_objects = self.storage.all()
        self.assertIn("BaseModel." + instance1.id, all_objects)
        self.assertIn("BaseModel." + instance2.id, all_objects)
        self.assertEqual(all_objects["BaseModel." + instance1.id], instance1)
        self.assertEqual(all_objects["BaseModel." + instance2.id], instance2)

    def test_save_and_reload_methods(self):
        """Test the save and reload methods."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.storage.new(instance1)
        self.storage.new(instance2)
        self.storage.save()

        # Create a new storage instance to ensure reloading from file
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn("BaseModel." + instance1.id, all_objects)
        self.assertIn("BaseModel." + instance2.id, all_objects)
        self.assertEqual(all_objects["BaseModel." + instance1.id].id,
                         instance1.id)
        self.assertEqual(all_objects["BaseModel." + instance2.id].id,
                         instance2.id)


if __name__ == '__main__':
    unittest.main()
