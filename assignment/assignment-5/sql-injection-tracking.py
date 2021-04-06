import sys
import os
import sqlite3

# Connect to database
conn = None
try:
    conn = sqlite3.connect('users.db')
except Exception:
    print("Can't connect to the database")
    sys.exit(-1)

print("Welcome to this vulnerable database reader")
print("You have to login first")

print("Insert your user-id")
user_id = Source("user-id");   # user_id -> "user-id" -> T

print("Insert your password")
password = Source("password");    # password -> "password" -> T

retrieve_user = "SELECT * FROM credentials WHERE user_id = '" + user_id + "' and password = '" + password + "';"
# retrieve_user -> "SELECT ... ;" -> T
cursor = Sink(conn.execute(retrieve_user))

# cursor -> conn.execute(retrieve_user) -> T

entries = cursor.fetchall()
# entries -> cursor -> T

# retrieve_user -> V -> entries
# cursor -> V -> entries
# entries -> V -> entries
# entry -> V -> entries
# user_id -> V -> entries
# first_name -> V -> entries
# last_name -> V -> entries
# phone -> V -> entries

if len(entries) > 0:
    print("\n===Logged-in===")
    retrieve_user = "SELECT * FROM accounts WHERE user_id = '" + user_id + "';"
    #retrieve_user -> user_id -> T
    
    cursor = Sink(conn.execute(retrieve_user))
    # cursor -> retrieve_user -> T
    
    entries = cursor.fetchall()
    # entries -> cursor -> T

    # user_id -> V -> entries
    # first_name -> V -> entries
    # last_name -> V -> entries
    # phone -> V -> entries
    for entry in entries:
        # entry -> entries -> T

        user_id, first_name, last_name, phone = entry
        
        # user_id -> entry -> T
        # first_name -> entry -> T
        # last_name -> entry -> T
        # phone -> entry -> T

        print()
        Sink("Here is {} data:".format(user_id)); # user_id -> T
        Sink("user-id=", user_id);# user_id -> T
        Sink("first_name=", first_name); # first_name -> T
        Sink("last_name=", last_name); # last_name -> T
        Sink("phone", phone); # phone -> T
else:
    print("Wrong credentials")