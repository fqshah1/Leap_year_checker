import sqlite3
import register
import login
# Create a new SQLite database
conn = sqlite3.connect('users.db')

# Create a new table called 'users'
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
