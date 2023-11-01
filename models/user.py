#!/usr/bin/python3
"""This module contains the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is the class for User
    Public Class Attributes:
    email: empty string
    password: empty string
    first_name: empty string
    last_name: empty string"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
