#!/usr/bin/python3
"""Defines unittests for console.py."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import models


class TestConsole(unittest.TestCase):
    """Test suite for the console.py file"""

    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()
        self.test_storage = models.storage
        self.test_models = {
            "BaseModel": models.base_model.BaseModel,
            "User": models.user.User,
            "State": models.state.State,
            "City": models.city.City,
            "Place": models.place.Place,
            "Amenity": models.amenity.Amenity,
            "Review": models.review.Review
        }

    def test_help_command(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_create_command(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        for class_name, class_obj in self.test_models.items():
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("create {}".format(class_name))
                self.assertIn(class_obj().id + "\n", f.getvalue())

    def test_show_command(self):
        """Test the show command"""
        # Testing when class name is missing
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

        # Testing when class doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Testing when instance id is missing
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Testing when instance doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        # Testing when instance exists
        obj_id = list(self.test_storage.all().values())[0].id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertIn(str(self.test_storage.all()["BaseModel." + obj_id]) + "\n", f.getvalue())

    def test_destroy_command(self):
        """Test the destroy command"""
        # Testing when class name is missing
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())

        # Testing when class doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Testing when instance id is missing
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Testing when instance doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 123456")
            self.assertEqual("** no instance found **\n", f.getvalue())

        # Testing when instance exists
        obj_id = list(self.test_storage.all().values())[0].id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.assertNotIn(obj_id, self.test_storage.all().keys())

    def test_all_command(self):
        """Test the all command"""
        # Testing without specifying a class
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertIn("{}".format(", ".join(str(obj) for obj in self.test_storage.all().values())) + "\n", f.getvalue())

        # Testing with a specified class that doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Testing with a specified class that exists
        for class_name in self.test_models.keys():
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("all {}".format(class_name))
                self.assertIn("{}".format(", ".join(str(obj) for obj in self.test_storage.all().values() if obj.__class__.__name__ == class_name)) + "\n", f.getvalue())

    def test_count_command(self):
        """Test the count command"""
        # Testing without specifying a class
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count")
            self.assertEqual("** class name missing **\n", f.getvalue())

        # Testing with a specified class that doesn't exist
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Testing with a specified class that exists
        for class_name in self.test_models.keys():
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("count {}".format(class_name))
                self.assertIn("{}".format(sum(1 for obj in self.test_storage.all().values() if obj.__class__.__name__ == class_name)) + "\n", f.getvalue())


if __name__ == '__main__':
    unittest.main()
