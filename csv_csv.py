import csv

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

with open('birth.txt', 'w') as f:
    fieldname = ['name', 'date of birth']
    w = csv.DictWriter(f, birthdays.keys())

    w.writeheader()
    w.writerow(birthdays)
