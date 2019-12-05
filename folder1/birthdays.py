'''
trasformiamo il csv in dizionario

'''
import csv

reader = csv.reader (open('birth.csv', 'r'))
d = {}
for row in reader:
    k,v = row  
    d[k]= v
#print(d)

'''
functions
'''

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in d:
        print(name)

def return_birthday(name):
    if name in d:
        return d[name]
    else:
        return (' is not in the list')



