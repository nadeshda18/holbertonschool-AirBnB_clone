#!/usr/bin/python3
"""This module contains the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is the class for User"""

    def __init__(self, *args, **kwargs):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        super().__init__(*args, **kwargs)
