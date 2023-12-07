#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new object"""
        # Actual implementation needed
        pass

    def do_show(self, arg):
        """Show information about a specific object"""
        # Actual implementation needed
        pass

    def do_destroy(self, arg):
        """Destroy a specific object"""
        # Actual implementation needed
        pass

    def do_all(self, arg):
        """Show information about all objects"""
        # Actual implementation needed
        pass

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_EOF(self, arg):
        """Handle end-of-file (EOF)"""
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
