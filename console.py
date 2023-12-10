#!/usr/bin/python3
"""
Console module for the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        return True

    def emptyline(self):
        """
        Empty line does nothing.
        """
        pass

    def do_create(self, arg):
        """
        Create command to create a new instance of BaseModel.
        Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show command to print the string representation of an instance.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance.
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        All command to print string representation of all instances.
        Usage: all [<class_name>]
        """
        args = arg.split()
        obj_list = []
        if not args:
            for key in storage.all():
                obj_list.append(str(storage.all()[key]))
            print(obj_list)
        elif args[0] in storage.classes:
            for key in storage.all():
                if args[0] in key:
                    obj_list.append(str(storage.all()[key]))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update command to update an instance attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_key = args[0] + "." + args[1]
            obj = storage.all()[obj_key]
            setattr(obj, args[2], args[3][1:-1])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
