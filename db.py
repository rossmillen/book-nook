import sqlite3

# This must be usable in app.py
def init_db():
    connection = sqlite3.connect("booknook.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password_hash TEXT
        )
        """)
    connection.commit()
    connection.close()

# This must be usable in views.py
def db_connection():
    connection = sqlite3.connect("booknook.db")
    connection.row_factory = sqlite3.Row
    return connection