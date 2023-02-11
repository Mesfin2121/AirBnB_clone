#!/usr/bin/python3
"""
Model of Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
     Model of Review

    Attributes:
        place_id (str): string - empty string: it will be the Place.id
        user_id (str): string - empty string: it will be the User.id
        text (str): string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
