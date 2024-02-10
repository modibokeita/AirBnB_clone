#!/usr/bin/python3
"""
amenity Module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    that class inherit from BaseModel
    class that allow to access the
    BaseModel class attributes
    """
    name = ""
