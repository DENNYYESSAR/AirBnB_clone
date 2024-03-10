#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """A class to handle serialization and deserialization of
    objects to/from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all objects currently stored.

        Returns:
            dict: A dictionary containing all objects stored in the file.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to be stored.

        Args:
            obj: The object to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = globals()[class_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj

    def classes(self):
        """
        Returns a dictionary of valid classes in the storage.
        """
        return {
            "BaseModel": BaseModel,
            # Add other classes here if necessary
        }
