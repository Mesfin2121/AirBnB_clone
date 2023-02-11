#!/usr/bin/python3
"""
Model of user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Model of user

    Attributes:
        email (str): string - empty string
        password (str): string - empty string
        first_name (str): string - empty string
        last_name (str): string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
