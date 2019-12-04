'''
open the birth.csv which contains 
'''

import csv

reader = csv.reader (open('birth.csv', 'r'))
d = {}
for row in reader:
    k,v = row  
    d[k]= v
#print(d)


def check_name(name_surname):
    if name_surname in d.keys():
        return (d[name_surname])
    else:
        return ('Sorry, {} name not found'. format(name_surname))



