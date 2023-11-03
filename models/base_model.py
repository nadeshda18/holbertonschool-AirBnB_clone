#!/usr/bin/python3
"""This module contains the BaseModel class"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """This is the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialization of the class"""
        if kwargs:
            for key, value in kwargs.items():
                # Convert string to datetime object if key is "created_at" or "updated_at"
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                # Set attribute if key is not "__class__"
                if key != "__class__":
                    setattr(self, key, value)
        else:
            # Set id, created_at, and updated_at attributes if no kwargs are passed
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        # Add instance to __objects dictionary and save to JSON file
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        class_dict = dict(self.__dict__)
        # Add class name to dictionary
        class_dict["__class__"] = self.__class__.__name__
        # Convert datetime objects to ISO format strings
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
