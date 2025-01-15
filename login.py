import sqlite3
import getpass
import register
import login
import database
def login():
    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Get the username and password from the user
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Check if the username and password match
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    if cursor.fetchone():
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

    conn.close()
login()