#!/usr/bin/python3

from birthdays import return_birthday
from birthdays import print_birthdays
from scripts import dbmanager
from scripts import dbmanager
from scripts import dbmanager

import argparse


args = parse_args()
dbmanager.check_or_create()
if args.a and args.p:
    dbmanager.save_new_username(args.a, args.p)
elif args.c and args.p:
    dbmanager.check_for_username(args.c, args.p)
conn.close()


'''
usiamo argvparse

'''
parser = argparse.ArgumentParser(
         prog= 'This program return the birthday of famous people')
parser.add_argument('n', nargs='+', 
         help='You can insert one or names in the format: "Name Surname"')  
parser.add_argument('-v', '--verbosity', action='count', default=0,
         help='Decide the level of verbosity')

args = parser.parse_args()


name = args.n
#bith_date = return_birthday(i)


# verbosity option

for i in name:
    #if args.verbosity:
    if return_birthday(i):
        if args.verbosity >= 2:
            print('{} was born the {}'.format(i, return_birthday(i)))
        elif args.verbosity >= 1:
            print ('{} : {}'.format(i, return_birthday(i)))
        else:
            print (return_birthday(i))
    else:
        print ('Sorry, {} is not in the list, '.format(i))
        print_birthdays()
    #else:
     #   if return_birthday(i):
      #      print('{} was bormnmmmnjnjnj the {}'.format(i, return_birthday(i)))
       # else:
        #    print('Sorry, {} is not in the list, '.format(i))
         #   print_birthdays()



	    

