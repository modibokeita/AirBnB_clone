#!/usr/bin/python3
"""
the entry point
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    that can have some method to
    be able to interact with the
    console
    """
    prompt = "(hbnb)"

    val_classes = [
            "BaseModel", "User",
            "City", "State",
            "Amenity", "Place",
            "Review"
            ]

    def do_quit(self, line):
        """
        The method that allows
        you to quit the program when
        you enter qui from console
        """
        return True

    def do_EOF(self, line):

        """
        The EOF method that show the
        end of file and qui the
        program
        """
        print()
        return True

    def emptyline(self):
        """
        that method handle an empty
        line when the user did not enter
        anything on console and print
        the specific message from the
        console
        """
        print("Please enter a command")

    def do_create(self, line):
        """
        that create method actually can create
        new instance from class BaseModel and
        new user when user enter on console create User
        """
        commands = shlex.split(line)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.val_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_all(self, line):
        """
        that method prints all instaces or a
        specific useing all class name
        """
        commands = shlex.split(line)
        obj = storage.all()

        if len(commands) == 0:
            for key, value in obj.items():
                print(str(value))
        elif commands[0] not in self.val_classes:
            print("** class doesn't exist **")
        else:
            for key, value in obj.items():
                if key.split(".")[0] == commands[0]:
                    print(str(value))

    def do_show(self, line):
        """
        that method show the tring representation
        of a class and id. usage: class id
        """
        commands = shlex.split(line)

        if len(commands) == 0:
            print("** class name missing *")
        elif commands[0] not in self.val_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()

            key = "{}.{}".format(commands[0], commands[1])

            if key in obj:
                print(obj[key])
            else:
                print("** no instance **")

    def do_destroy(self, line):
        """
        that method deletes an instance based on
        class name and id. usage: destroy class id
        """
        commands = shlex.spli(line)

        if len(commands) == 0:
            print("** class name missing **")
        elif command[0] not in self.val_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()

            key = "{}.{}".format(commands[0], commands[1])

            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        """
        update an instance by adding or updating
        an attribute. Usages: update class name, id
        attribute name, attribute value
        """

        commands = shlex.split(line)

        if len(commands) == 0:
            print("** class name missing **")

        elif commands[0] not in self.val_classes:
            print("** class doesn't exist")
        elif len(commands) < 2:
            print("** instance id missing *")
        else:
            obj = storage.all()

            key = "{}.{}".format(commands[0], commands[1])

            if key not in obj:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                objects = obj[key]

                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass

                setattr(objects, attr_name, attr_value)
                objects.save()


if __name__ == "__main__":

    HBNBCommand().cmdloop()
