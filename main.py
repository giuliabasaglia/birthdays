#! /usr/bin/env python3


import sys
import argparse
import sqlite3
import hashlib

from folder1 import birthdays
from scripts import dbmanager


"""Requires the credentials (username and password).

If valid, it returns the birthday of the searched famous person/people.
"""

def parse_argument():
    parser = argparse.ArgumentParser(
             prog= "This program return the birthday of famous people")

    parser.add_argument('n', nargs='+',
             help='You can insert one or names in the format: "Name Surname"')
 
    parser.add_argument('-v', '--verbosity', action='count', default=0,
              help='Decide the level of verbosity')

    #Check for username and password
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                       "(requires -p)", required=True)
    args = parser.parse_args()
    return args

def verbosity_levels(name):
    
    for i in name:
    #if args.verbosity:
        if birthdays.return_birthday(i):
            if args.verbosity >= 2:
                print('{} was born the {}'.format(i, birthdays.return_birthday(i)))
            elif args.verbosity >= 1:
                print ('{} : {}'.format(i, birthdays.return_birthday(i)))
            else:
                print (birthdays.return_birthday(i))
        else:
            print ('Sorry, {} is not in the list, '.format(i))
            birthdays.print_birthdays()


if __name__ == "__main__":
     parse_argument()   
     args = parse_argument()

     if dbmanager.check_for_username(args.c, args.p):
         verbosity_levels(args.n)
     
     
      
          


#arg = user_parse_args()
#dbmanager.check_or_create()
#if arg.a and arg.p:
#    dbmanager.save_new_username(arg.a, arg.p)
#elif arg.c and arg.p:
    



















