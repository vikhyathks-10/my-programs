# 02_insert_records.py

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

students = [
    (101, "Rahul", 20, "CSE"),
    (102, "Priya", 21, "ECE"),
    (103, "Amit", 20, "ISE")
]

cursor.executemany(
    "INSERT OR REPLACE INTO students VALUES(?,?,?,?)",
    students
)

conn.commit()

print("Records Inserted Successfully!")

conn.close()