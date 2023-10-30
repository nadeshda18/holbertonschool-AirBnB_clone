#!/usr/bin/python3
"""This module contains the BaseModel class"""

import uuid
from datetime import datetime

class BaseModel:
    """This is the BaseModel class"""
    
    def __init__(self, *args, **kwargs):
        """Initialization of the class"""
    

    def __str__(self):
        """Returns the string representation of the class""" 

    def save(self):
        """Updates the public instance attribute updated_at"""


    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
