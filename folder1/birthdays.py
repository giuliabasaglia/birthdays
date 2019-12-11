'''
trasformiamo il csv in dizionario

'''
import csv

reader = csv.reader (open('folder1/birth.csv', 'r'))
d = {}
for row in reader:
    k,v = row  
    d[k]= v
#print(d)

'''
functions
'''

def print_birthdays():
    print('We know the birthdays of these people:')
    for e in d:
        print(e)

def return_birthday(name):
    if name in d:
        return d[name]
    else:
        return False 



