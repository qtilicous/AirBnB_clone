#!/usr/bin/python3
"""
Module for HBNBCommand class.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = '(hbnb) '
    __classes = {"BaseModel", "User"}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel or User."""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)()
            cls.save()
            print(cls.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show command to display the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy command to delete an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """All command to display all instances."""
        args = shlex.split(arg)
        objs = storage.all()
        if not args:
            print([str(objs[obj]) for obj in objs])
        else:
            try:
                cls = eval(args[0])
                print([str(objs[obj]) for obj in objs if args[0] in obj])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update command to update an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(storage.all()[key], args[2], args[3])
            storage.save()
        except NameError:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Count command to count instances of a class."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
            print(len([obj for obj in storage.all() if args[0] in obj]))
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
