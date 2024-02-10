#!/usr/bin/python3
"""
review Module
"""
from models.user import User
from models.place import Place
from models.base_model import BaseModel


class Review(BaseModel):
    """
    that class inherit from BaseModel
    class that allow to access the
    BaseModel class attributes
    """
    place_id = ""
    user_id = ""
    text = ""
