# -*- coding: utf-8 -*-
"""
This example uses docopt with the built in cmd module to demonstrate an 
interactive command application.
Usage:
    run_sgr book_seat <first_name> <last_name> <seat_no>...
    run_allocator (-i | --interactive)
    run_allocator (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit
"""
import sys
import cmd
from docopt import docopt, DocoptExit

from madaraka import Madaraka

madaraka = Madaraka()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.
            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)
    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn
    
class MyInteractive (cmd.Cmd):
    prompt = '(run_allocator) '
    file = None
    
    @docopt_cmd
    def do_book_seat(self, args):
        """Usage: book_seat <first_name> <last_name> <seat_no>"""
        
        fname = args['<first_name>']
        lname = args['<last_name>']
        seat_no = args['<seat_no>']
        
        madaraka.book_seat(fname, lname, seat_no)
        
    @docopt_cmd
    def do_retrieve_manifest(self, args):
        """Usage: retrieve_manifest"""
        
        madaraka.retrieve_manifest()
        
        
    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        
        print("Good Bye!")
        exit()      
opt = docopt(__doc__, sys.argv[1:])
if opt['--interactive']:
    
    MyInteractive().cmdloop()
print(opt)