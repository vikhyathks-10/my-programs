# 04_update_delete.py

import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE students SET age=? WHERE id=?",
    (22, 102)
)

cursor.execute(
    "DELETE FROM students WHERE id=?",
    (103,)
)

conn.commit()

print("Record Updated and Deleted Successfully!")

conn.close()