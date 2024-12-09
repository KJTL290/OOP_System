import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.db')

try:
    cursor = conn.cursor()
    
    # Ensure the 'users' table exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    
    # Inserting a single row
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    
    # Inserting multiple rows at once
    users_data = [('Bob', 25), ('Charlie', 40)]
    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_data)
    
    # Commit the changes
    conn.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the connection is closed
    conn.close()