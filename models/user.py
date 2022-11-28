#!/usr/bin/python3
"""
user class that inherits from the Basemodel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    defining the user class with it's attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
