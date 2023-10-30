#!/usr/bin/python3
"""module for class FileStorage"""

import json
from models.base_model import BaseModel
from os import path


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the Json file"""
        objects_dict = {key: obj.to.dict()
                        for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, mode="w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """deserializes the Json file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                FileStorage.__objects = {k: v.from_dict() for k, v in
                                         json.load(f).items()}
        except FileNotFoundError:
            pass
