#! /usr/bin/env python3

from folder1 import birthdays
import sys
import argparse

#def parse_arg:
parser = argparse.ArgumentParser(prog="This program returns the birthdays of a list of famous people")
parser.add_argument("name", help='You have to insert a name in the format: "Name Surname"')  # c'è un modo per impostare il formato?
#  c'è un modo per far sì che all'utente esca la lista di nomi contenuti nel dizionario?
# vorremmo fare in modo che inserendo la data di nascita ritorni il nome?
parser.add_argument("-v", "--verbosity",choices= [0,1,2], help='Decide the level of verbosity')
args = parse.parse_args()
date = birthdays.return_birthday(args.name)
if args.verbosity == 2:
    print("{} was born the {}".format(args.name, date)
elif args.verbosity == 1:
    print("{}:{}".format(args.name, date)
else:
    print(date)


#if len(sys.argv)>1:
#    birthdays.return_birthday(sys.argv[1])
#else:
#    print("You didn't pass any argument")

