#!/usr/bin/python3
"""
City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    that class inherit from
    BaseModel class that allows
    to access the BaseModel class
    attributes
    """
    state_id = State.id
    name = ""
