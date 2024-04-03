import sqlite3

# Function to create SQLite database and tables if they don't exist
def create_database():
    with sqlite3.connect('expenses.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                category TEXT,
                amount REAL,
                date TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
