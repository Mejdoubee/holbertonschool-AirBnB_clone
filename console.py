#!/usr/bin/python3
import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, args):
        '''EOF command to exit the program'''
        return True

    def emptyline(self):
        '''An empty line + ENTER shouldn’t execute anything'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
