#!/usr/bin/python3
"""
creating the review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    defining Review class that inherits from BaseModels
    """
    place_id = ""
    user_id = ""
    text = ""