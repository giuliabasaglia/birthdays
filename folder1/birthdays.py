'''
functions
'''

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in csvfile:
        print(name)

def return_birthday(name):
    if name in csvfile:
        print('{}\'s birthday is {}.'.format(name, csvfile[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

def get_name(val): 
    for name, date in birthdays.items(): 
         if val == date: 
                return date 

