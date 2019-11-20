#! /usr/bin/env python3

from folder1 import birthdays
import sys

if len(sys.argv)>1:
    birthdays.return_birthday(sys.argv[1])
else:
    print("You didn't pass any argument")

