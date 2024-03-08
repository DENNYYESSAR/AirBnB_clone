#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from os.path import exists


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
        return self.__objects

    def new(self, obj):
        """
        Add a new object to be stored.

        Args:
            obj: The object to be stored.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump({key: obj.to_dict() for key,
                      obj in self.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj_cls = eval(class_name)  # Convert class name to class
                    self.__objects[key] = obj_cls(**obj_dict)
