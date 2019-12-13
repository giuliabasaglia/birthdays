import sqlite3
import hashlib
import argparse
import random

conn = sqlite3.connect('example-pwd.db')
cursor = conn.cursor()

conn = 0
cursor = 0
def check_or_create():
    ''' check if database exists in a specific file, if not create one. '''
    global conn
    global cursor
    conn = sqlite3.connect('../example-pwd.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
                     (username CHAR(256) NOT NULL, password CHAR(256) NOT NULL, salt CHAR(256) NOT NULL,
                      PRIMARY KEY (username))''')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                       "(requires -p)", required=False)
    return parser.parse_args()


def save_new_username(username, password):
    global conn
    global cursor
    salt = str(random.random())
    digest = salt + password
    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()

    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()
    print('Username {} successfully added.'.format(username)



def check_for_username(username, password):
    global conn
    global cursor
#problema
    try:
        cursor.execute("SELECT username FROM user WHERE username=?",(username,)).fetchall()[0] #sostituito a fetchone()
    except:
        print('Username is not valid')
        return #
    salt = cursor.execute("SELECT salt FROM user WHERE username=?",(username,))
    results = salt.fetchone()
    #print (results)
    digest = (results[0]) + password
    for i in range(100000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                      (username, digest))
    conn.commit()
    results = rows.fetchall()
    if results:
        print("User is present, password is valid" )
        return True
    else:
        print("Password is invalid")
        return False



'''

def check_for_username(username, password):
    global conn
    global cursor
#problema
    if cursor.execute("SELECT username FROM user WHERE username=?",(username,)):
        salt = cursor.execute("SELECT salt FROM user WHERE username=?",(username,))
        results = salt.fetchone()
        print (results)
        digest = (results[0]) + password
        for i in range(100000):
            digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
        rows = cursor.execute("SELECT * FROM user WHERE username=? and password=?",
                          (username, digest))
        conn.commit()
        results = rows.fetchall()
        if results:
            print("User is present, password is valid" )
            return True
        else:
            print("Password is invalid")
            return False
    else:
        print("Username not valid")
        return False
'''


if __name__=="__main__":
    check_or_create()
    parse_args()
    args = parse_args()
    if args.a and args.p:
        save_new_username(args.a, args.p)
    elif args.c and args.p:
        check_for_username(args.c, args.p)
    conn.close()   
     

    


