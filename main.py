#! /usr/bin/env python3


import sys
import argparse


from folder1 import birthdays
from folder1 import birthdays
from scripts import dbmanager
#from scripts import save_new_username, dbmanager
#from scripts import check_for_username, dbmanager




'''
usiamo argvparse


parser = argparse.ArgumentParser(
         prog= 'This program return the birthday of famous people')
parser.add_argument('n', nargs='+', 
         help='You can insert one or names in the format: "Name Surname"')  
parser.add_argument('-v', '--verbosity', action='count', default=0,
         help='Decide the level of verbosity')

args = parser.parse_args()


name = args.n



# verbosity option

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
    #else:
     #   if return_birthday(i):
      #      print('{} was bormnmmmnjnjnj the {}'.format(i, return_birthday(i)))
       # else:
        #    print('Sorry, {} is not in the list, '.format(i))
         #   print_birthdays()
'''

''' check username e password'''
def user_parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=True)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                       "(requires -p)", required=False)
    
    return parser.parse_args()


def check_for_username(username, password):
    global conn
    global cursor
    salt = cursor.execute("SELECT salt FROM user WHERE username=?",(username))
    digest = salt + password
    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                          (username, digest))
    conn.commit()
    results = rows.fetchall()
    if results:
        print("User is present, password is valid" )
    else:
        print("User is not present, or password is invalid")


arg = user_parse_args()
dbmanager.check_or_create()
if arg.a and arg.p:
    dbmanager.save_new_username(arg.a, arg.p)
elif arg.c and arg.p:
    check_for_username(arg.c, arg.p)



















