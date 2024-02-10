#!/usr/bin/python3
"""
Place module
"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity


class Place(BaseModel):
    """
    that class inherit from baseModel
    class that allows to access the
    BaseModel class attributes
    """
    city_id = City_id
    user_id = User_id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]
