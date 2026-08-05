# 01_create_database.py

import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    branch TEXT
)
""")

conn.commit()

print("Database and Table Created Successfully!")

conn.close()