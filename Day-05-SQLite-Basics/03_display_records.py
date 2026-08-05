# 03_display_records.py

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

print("\n===== STUDENT RECORDS =====\n")

for row in records:
    print(row)

conn.close()