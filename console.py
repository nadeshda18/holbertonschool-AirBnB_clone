#!/usr/bin/python3
"""entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """defines the class HBNBCommand"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """modify the empty line + ENTER"""
        pass

    def help_quit(self):
        """print custom message"""
        print("Quit command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
