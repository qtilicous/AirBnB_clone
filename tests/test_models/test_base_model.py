#!/usr/bin/python3
"""
This module defines the HBNBCommand class.
A command-line interpreter for the AirBnB clone.
"""
import cmd
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class is a command-line interpreter for the AirBnB clone.
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Create a new instance of a specified class, save it, and print its id.

        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return
        classes = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
            'User': User
        }
        if arg not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance
        based on the class name and id.

        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    # Add similar methods for 'destroy', 'all', and 'update'


if __name__ == '__main__':
    HBNBCommand().cmdloop()
