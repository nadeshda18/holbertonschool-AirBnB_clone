#!/usr/bin/python3
"""this module contains the Class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel
    Public Class Attributes:
    state_id: empty string will be State.id
    name: empty string"""
    state_id = ""
    name = ""
