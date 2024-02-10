#!/usr/bin/pytho3

"""
file storage model
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User

class FileStorage:

    """
    the class to handle the file storage
    that convert the to json file and
    then deserialized the file to be able to read
    """

    __file_path = "file.json"

    __objects = {}

    def all(self):
        """
        the method all return
        the method in fileStorage class
        """
        return FileStorage.__objects

    def new(self, obj):

        """
        the method new sets new object
        and return that object with
        and id on it
        """
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        """
        the save method saves the file to
        json file and that should be able hold
        the data
        """
        all_bjs = FileStorage.__objects
        serialized_obj = {}

        for key in all_bjs.keys():
            serialized_obj[key] = all_bjs[key].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:

            json.dump(serialized_obj, file)

    def reload(self):
        """
        the reload method loads file has been
        deserialized that can be able
        to be readed
        """
        if exists(FileStorage.__file_path):

            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:

                try:
                    load_file = json.load(file)

                    for key, value in load_file.items():

                        class_name, obj_id = key.split(".")

                        class_ = eval(class_name)

                        instance = class_(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
