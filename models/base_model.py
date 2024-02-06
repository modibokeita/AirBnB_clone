#!/usr/bin/pyhon3
"""
BaseModel module
"""
from uuid import uuid4
import json
from datetime import datetime
class BaseModel:
    """
    the Base module that the others
    modules inherit from
    """
    def __init__(self, *args, **kwargs):

        """
        the initialization of 
        instances
        """
        self.id = str(uuid())
        self.created_date = datetime.now()
        self.update_at = datatime.now()

    def as_dict(self):

        dict_obj = self.__dict__copy()
        dict_obj = ['__class__'] = __class__.__name__
