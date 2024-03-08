#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""


import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test suite for the BaseModel class."""

    def setUp(self):
        """Set up for the tests; this method is called before each
        test function.
        """
        self.initial_instance = BaseModel()
        self.instance_dict = self.initial_instance.to_dict()

    def test_instance_creation_with_kwargs(self):
        """Test creating an instance with kwargs reflects the correct
        attribute values.
        """
        new_instance = BaseModel(**self.instance_dict)
        # Ensure the new instance's attributes match those of the
        # initial instance
        self.assertEqual(new_instance.id, self.initial_instance.id)
        self.assertEqual(new_instance.created_at.isoformat(),
                         self.initial_instance.created_at.isoformat())
        self.assertEqual(new_instance.updated_at.isoformat(),
                         self.initial_instance.updated_at.isoformat())

    def test_datetime_conversion_from_kwargs(self):
        """Test conversion of 'created_at' and 'updated_at' from
        string to datetime.
        """
        new_instance = BaseModel(**self.instance_dict)
        # Ensure 'created_at' and 'updated_at' are datetime objects
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)

    def test_ignore_class_key_in_kwargs(self):
        """Test that '__class__' key in kwargs is ignored when
        creating an instance.
        """
        modified_dict = self.instance_dict.copy()
        modified_dict['__class__'] = 'SomeOtherClass'
        new_instance = BaseModel(**modified_dict)
        # Ensure '__class__' attribute is not set
        self.assertNotIn('__class__', new_instance.__dict__)

    def test_additional_attributes_in_kwargs(self):
        """Test that additional attributes in kwargs are correctly set."""
        modified_dict = self.instance_dict.copy()
        modified_dict['extra_attribute'] = 'extra_value'
        new_instance = BaseModel(**modified_dict)
        self.assertTrue(hasattr(new_instance, 'extra_attribute'))
        self.assertEqual(new_instance.extra_attribute, 'extra_value')

    def test_instance_creation(self):
        """Test that a BaseModel instance is created with the correct
        attributes.
        """
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))
        self.assertTrue(isinstance(instance.created_at, datetime))
        self.assertTrue(isinstance(instance.updated_at, datetime))

    def test_str_method(self):
        """Test the __str__ method returns the expected string."""
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(instance.__str__(), expected_str)

    def test_save_method(self):
        """Test the save method updates 'updated_at'."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)
        self.assertTrue(instance.updated_at > old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method returns the correct dictionary."""
        instance = BaseModel()
        instance_dict = instance.to_dict()

        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertTrue('created_at' in instance_dict)
        self.assertTrue('updated_at' in instance_dict)

        # Ensure that datetime attributes are converted to strings.
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

        # Ensure that the string representation follows the ISO format.
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        try:
            datetime.strptime(instance_dict['created_at'], datetime_format)
            datetime.strptime(instance_dict['updated_at'], datetime_format)
        except ValueError:
            self.fail("created_at or updated_at does not match ISO format")


if __name__ == '__main__':
    unittest.main()
