#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
"""
Base Module
"""


class BaseModel:
    """
    initialization of instance attributes
    """
    def __init__(self, *args, **kwargs):
        formated_time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__build_class__":
                    continue
                elif key == "created_at" or key == "updated_at":

                    setattr(self, key, datetime.strptime(value, formated_time))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """

        self.updateed_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """

        obj_dict = self.__dict__.copy()

        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """

        class_name = self.__class__.__name__

        return "[{}] {} {}".format(class_name, self.id, self.__dict__)
