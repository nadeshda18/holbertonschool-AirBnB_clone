#!/usr/bin/python3
"""entry point of the command interpreter
def do_quit = exit the program
def do_EOF = exit the program
def emptyline = do nothing when emptyline + ENTER
def do_create = create a new instance of BaseModel
def do_show = print the string representation of an instance
def do_destroy = delete an instance based on the class name and id
def do_all = print all string representation of all instances
def do_update = update an instance based on the class name and id
def help = display this message
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """defines the class HBNBCommand"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program with quit"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """modify the empty line + ENTER"""
        pass

    def do_create(self, arg):
        """create a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """print the string representation of an instance"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """delete an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """print all string representation of all instances"""
        if len(arg) == 0:
            print([str(value) for value in storage.all().values()])
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            print([str(value) for value in storage.all().values()])

    def do_update(self, arg):
        """update an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        elif len(arg.split()) == 2:
            print("** attribute name missing **")
        elif len(arg.split()) == 3:
            print("** value missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                setattr(storage.all()[key], arg.split()[2], arg.split()[3])
                storage.all()[key].save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
