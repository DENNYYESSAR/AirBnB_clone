#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return user_dict
