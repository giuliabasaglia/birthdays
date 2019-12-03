'''
open the birth.txt which contains 
'''
import csv

with open("birth.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(dict(row))
csvfile.close()
