# 05_search_records.py

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

student_id = int(input("Enter Student ID: "))

cursor.execute(
    "SELECT * FROM students WHERE id=?",
    (student_id,)
)

record = cursor.fetchone()

if record:
    print("\nStudent Found")
    print(record)
else:
    print("\nStudent Not Found")

conn.close()