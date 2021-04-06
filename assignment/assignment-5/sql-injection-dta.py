import sys
import os
import sqlite3

Connect to database
conn = None
try:
    conn = sqlite3.connect('users.db')
except Exception:
    print("Can't connect to the database")
    sys.exit(-1)

print("Welcome to this vulnerable database reader")
print("You have to login first")

print("Insert your user-id")
user_id = input()
make_tainted("user_id")

print("Insert your password")
password = input()
make_tainted("password")

retrieve_user = "SELECT * FROM credentials WHERE user_id = '" + user_id + "' and password = '" + password + "';"
make_cond_tainted("retrieve_user", array("user_id", "password"))

if isTainted("retrieve_user") and isSqlInjectionAttack("retrieve_user"):
    exit("SQL injection attack detected!")
cursor = conn.execute(retrieve_user)

entries = cursor.fetchall()
make_cond_tainted("entries", array("cursor"))

if len(entries) > 0:
    print("\n===Logged-in===")
    retrieve_user = "SELECT * FROM accounts WHERE user_id = '" + user_id + "';"
    make_cond_tainted("retrieve_user", array("user_id"))

    if isTainted("retrieve_user") and isSqlInjectionAttack("retrieve_user"):
        exit("SQL injection attack detected!")
    cursor = conn.execute(retrieve_user)

    entries = cursor.fetchall()
    make_cond_tainted("entries", array("cursor"))

    for entry in entries:
        make_cond_tainted("entry", array("entries"))

        user_id, first_name, last_name, phone = entry
        make_cond_tainted("user_id", array("entry"))
        make_cond_tainted("first_name", array("entry"))
        make_cond_tainted("last_name", array("entry"))
        make_cond_tainted("phone", array("entry"))

        print()
        if isTainted("user_id") and isXssAttack(user_id):
            exit("XSS attack detected!")
        print("Here is {} data:".format(user_id))

        if isTainted("user_id") and isXssAttack(user_id):
            exit("XSS attack detected!")
        print("user-id=", user_id)

        if isTainted("first_name") and isXssAttack(first_name):
            exit("XSS attack detected!")
        print("first_name=", first_name)

        if isTainted("last_name") and isXssAttack(last_name):
            exit("XSS attack detected!")
        print("last_name=", last_name)

        if isTainted("phone") and isXssAttack(phone):
            exit("XSS attack detected!")
        print("phone", phone)

else:
    print("Wrong credentials")