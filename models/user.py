#!/usr/bin/python3

"""
User Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user model inheriting the
    BaseModel that to be able
    to access the BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
