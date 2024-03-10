#!/usr/bin/python3
"""Defines the BaseModel classes"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel or update an existing one
        from a dictionary representation.

        Args:
            *args (tuple): Unused positional arguments.
            **kwargs (dict): Keyword arguments that represent instance
                            attributes.
        """
        formt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, formt)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance, including the class
        name, id, and dictionary of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's
        __dict__, plus the __class__ key with the class name of the object.
        'created_at' and 'updated_at' are converted to strings in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
