#!/usr/bin/python3
"""Console module"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNCB command class"""

    prompt = ' (hbnb) '

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def empty(self, arg):
        """empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
