#!/usr/bin/python3
"""
A module cmd that contains the entry point of the command interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
import re


class HBNBCommand(cmd.Cmd):
    """A class HBNH interpreter command
    Attributes:
        prompt (str):
        CLASSES (list): list of all classes name.
    """

    prompt = '(hbnb)'

    CLASSES = ['BaseModel', 'User', 'State']

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
        """Overwrite default emptyline command"""
        pass

    def do_create(self, arg):
        """Create command for creating new class instances
        Usage:
            create <ClassNmae>"""
        args = shlex.split(arg)

        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Show command string representation of an instance
        Usage:
            show <ClassNmae> <id>"""
        args = shlex.split(arg)
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
        """ Deletes an instance
        Usage:
            destroy <ClassNmae> <id>"""
        args = shlex.split(arg)
        all_object = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in all_object.keys():
            print("** no instance found **")
        else:
            del all_object["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances
        Usage:
            all <ClassName>"""
        args = arg.split(" ")
        all_object = storage.all()
        list_object = []

        if len(args) == 0:
            for k, v in all_object.items():
                list_object.append(str(v))
            print(list_object)
        elif args[0] not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        else:
            for k, v in all_object.items():
                if k.split('.')[0] == args[0]:
                    list_object.append(str(v))
            print(list_object)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        Usage:
            update <class name> <id> <attribute name> <"attribute value">"""
        args = shlex.split(arg)
        all_object = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.CLASSES:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])

            if key not in all_object:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                new_obj = all_object.get(key)
                setattr(new_obj, args[2], args[3])
                storage.save()

    # def default(self, arg):
    #     """ """
    #     pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = shlex.split(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
