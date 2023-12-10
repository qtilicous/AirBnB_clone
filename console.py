#!/usr/bin/python3
"""
Console module for AirBnB clone.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel."""
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
        """Show command to print the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls_name, obj_id = arg.split()
            key = "{}.{}".format(cls_name, obj_id)
            print(storage.all().get(key, "** no instance found **"))
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy command to delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls_name, obj_id = arg.split()
            key = "{}.{}".format(cls_name, obj_id)
            storage.all().pop(key, None)
            storage.save()
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """All command to print all string representation of all instances."""
        obj_list = [str(obj) for obj in storage.all().values() if arg in str(obj)]
        print(obj_list)

    def do_update(self, arg):
        """Update command to update an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = arg.split()
            cls_name, obj_id, attr_name = args[0], args[1], args[2]
            key = "{}.{}".format(cls_name, obj_id)
            obj = storage.all().get(key)
            if obj:
                if len(args) == 3:
                    print("** value missing **")
                    return
                value = args[3]
                setattr(obj, attr_name, value)
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
