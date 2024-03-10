#!/usr/bin/python3
"""
Module for console command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Class for the command interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with EOF
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def help_quit(self):
        """
        Help message for quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help message for EOF command.
        """
        print("Exit the program with EOF")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file,
        and prints the id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del(storage.all()[key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on
        the class name.
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in storage.all().items()
                  if key.split(".")[0] == arg])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                value = args[3].strip("\"'")

                try:
                    attr_value = getattr(obj, args[2], str(args[3]))
                    if not isinstance(attr_value, str):
                        value = type(attr_value)(value)
                    setattr(obj, args[2], value)
                except ValueError as e:

                    obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
