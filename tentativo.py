#!/usr/bin/python3

import argparse
'''
parser= argparse.ArgumentParser()
parser.add_argument('-a','--add', help = 'create a local account')
args= parser.parse_args()
print('creating user' +args.add)
'''

import csv

'''
trasformiamo il csv in dizionario

'''
reader = csv.reader (open('birth.csv', 'r'))
d = {}
for row in reader:
    k,v = row  
    d[k]= v
#print(d)

'''
usiamo argvparse

'''
parser = argparse.ArgumentParser(prog= 'typetypetype')
parser.add_argument('n', help='You have to insert a name in the format: "Name Surname"')  
parser.add_argument('-v', '--verbosity', type=int, choices =[0,1,2], help='Decide the level of verbosity')
args = parser.parse_args()


name = args.n
birthday_data= return_birthday(name)
if name in d:
    # verbosity option
    if args.verbosity == 2:
        print('ciao 2:, data:{}'.format(name)
    elif args.verbosity == 1:
        print('Ciao 1:{}'.format(name))
    else:
        print('ciao 0:{}'.format(name))
else:
    print('Sadly, we don\'t have {}\'s birthday.'.format(name))



  
