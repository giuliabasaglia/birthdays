#! /usr/bin/env python3

from folder1 import return_birthday, birthdays
import sys
import argparse

parser = argparse.ArgumentParser(prog='This program returns the birthdays of a list of famous people')
parser.add_argument('n', 'name', help='You have to insert a name in the format: "Name Surname"')  
parser.add_argument('-v', '--verbosity',choices= [0,1,2], help='Decide the level of verbosity', type=int)
args = parser.parse_arg()
complete_name = args.name
  
  
birth = birthdays.return_birthday(complete_name)
if birthdays.return_birthday(complete_name):
    if args.verbosity == 2:
        print('{} was born the {}'.format(complete_name, birth))
    elif args.verbosity == 1:
    	print('{}:{}'.format(complete_name, birth)
    else:
        print(birth)
else:
    print('Sorry {} is not in the list'.format(complete_name))

if __name__ == '__main__':
    args = parse_arg()
    birthdays.return_birthday(args)

'''
def verbosity_level():
    date = birthdays.return_birthday(args.name)
    if args.verbosity == 2:
        print("{} was born the {}".format(args.name, date)
    elif args.verbosity == 1:
        print("{}:{}".format(args.name, date)
    else:
        print(date)
'''
