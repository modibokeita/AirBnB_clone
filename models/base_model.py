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
        formated_time = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or "updated_at":
                    setattr(self, key, datetime.strptime(value, formated_time))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid())
            self.created_date = datetime.utcnow()
            self.update_at = datetime.utcnow()

    def save():

        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        dict_obj = self.__dict__copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["update_at"] = self.updated_at.isoformat()
        return dict_obj

    def __str__(self):

        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return "[{}] {} {}".format(class_name, self.id, self.__dict__)
