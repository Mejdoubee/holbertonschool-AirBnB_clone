#!/usr/bin/python3
'''
entry point
'''
import cmd

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

    def help_quit(self):
        '''Quit command to exit the program'''
        print("Quit command to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
