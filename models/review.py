#!/usr/bin/python3
"""this module contains the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherit from BaseModel
    Public Class Attributes:
    place_id: empty string will be Place.id
    user_id: empty string will be User.id
    text: empty string"""
    place_id = ""
    user_id = ""
    text = ""
