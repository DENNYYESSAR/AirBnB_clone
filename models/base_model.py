#!/usr/bin/python3
"""Defines the BaseModel classes"""

import models
import uuid
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
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        # Convert string to datetime
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            
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
        self.updated_at = datetime.now()

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
