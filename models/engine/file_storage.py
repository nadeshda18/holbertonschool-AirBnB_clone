#!/usr/bin/python3
"""module for class FileStorage"""

import json
from models.base_model import BaseModel
from os import path
from models.user import User



class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}
    CLASS_DICT = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the Json file"""
        with open(FileStorage.__file_path, 'w') as f:
            objects_dict = {key: value.to_dict()
                            for key, value in FileStorage.__objects.items()}
            json.dump(objects_dict, f)

    def reload(self):
        """deserializes the Json file to __objects"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for key, value in objs.items():
                cls_name = value["__class__"]
                cls = FileStorage.CLASS_DICT.get(cls_name)
                if cls:
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
