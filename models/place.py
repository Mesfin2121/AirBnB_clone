#!/usr/bin/python3
"""
Model of Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Model of Place

    Attributes:
        city_id (srt): string - empty string: it will be the City.id
        user_id (str): string - empty string: it will be the User.id
        name (str): string - empty string
        description (str): string - empty string
        number_rooms (int): integer - 0
        number_bathrooms (int): integer - 0
        max_guest (int): integer - 0
        price_by_night (int): integer - 0
        latitude (float): float - 0.0
        longitude (float): float - 0.0
        amenity_ids (list): list of string it will be the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
