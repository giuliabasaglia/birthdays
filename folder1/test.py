import csv
import os.path

'''Checking the extension of the file
'''

def type_file(path):
    extension = os.path.splitext(path)[1]
    return extension

'''Reading csv file as dictionary
'''

def csv_reader(path):
    reader = csv.reader(open(path, 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = v


csv_reader('folder1/birth.csv')
