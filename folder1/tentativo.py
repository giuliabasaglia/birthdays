#!/usr/bin/python3

from birthdays import return_birthday
import argparse


'''
usiamo argvparse

'''
parser = argparse.ArgumentParser(prog= 'This program return the birthday of famous people')
parser.add_argument('n', help='You have to insert a name in the format: "Name Surname"')  
parser.add_argument('-v', '--verbosity', type=int, choices =[0,1,2], help='Decide the level of verbosity')
args = parser.parse_args()


name = args.n
birth_date = return_birthday(name)

# verbosity option
if birth_date:
	if args.verbosity == 2:
	    print('{} was born the {}'.format(name, birth_date))
	elif args.verbosity == 1:
	    print('{}:{}'.format(name, birth_date))
	else:
	    print(birth_date)
else:
	print('{} is not in the list'.format(name))
