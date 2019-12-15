import unittest
from  folder1.test import csv_reader
from  folder1.test import type_file
import sys
import os

class TestMain(unittest.TestCase):

    def setUp(self):
        # note: this would be better done with tempfile
        self.temporary_file = "/tmp/temporary_file.csv"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        self.assertFalse(os.path.exists("folder1/lorem_ipsum.csv"))

    '''This function is necessary to check
    the presence of data inside the csv file.
    '''
    def test_empty_datafile(self):
        datafile = csv_reader(path=self.temporary_file)
        self.assertFalse(datafile)

    '''This function is necessary to check
    the extension of the file.
    '''
    def test_valid_extension(self):
        extension = type_file(path=self.temporary_file)
        self.assertEqual(extension, ".csv")

    def tearDown(self):
        os.remove(self.temporary_file)

if __name__ == '__main__':
    unittest.main()
