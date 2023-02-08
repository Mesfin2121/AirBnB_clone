#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    CLASSES = ['BaseModel']

    def do_EOF(self, arg):
        """Exit signal to exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Simple healp message for "quit" command"""
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ """
        if arg == "":
            print("** class name missing **")
        elif str(arg) in HBNBCommand.CLASSES:
            pass

        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ """
        args = arg.split(" ")
        all_object = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in all_object:
            print("** no instance found **")
        else:
            print(all_object["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
