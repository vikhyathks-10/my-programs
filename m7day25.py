# ==========================================================
# Month 7 - Day 25
# Database Programming with SQLite
#
# Topics Covered:
# 1. Create Database
# 2. Create Table
# 3. Insert Records
# 4. Read Records
# 5. Update Records
# 6. Delete Records
# ==========================================================

import sqlite3

# ==========================================================
# CONNECT DATABASE
# ==========================================================

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

print("=" * 60)
print("1. DATABASE CREATED / CONNECTED")
print("=" * 60)

print("Connected Successfully")


# ==========================================================
# CREATE TABLE
# ==========================================================

print("\n" + "=" * 60)
print("2. CREATE TABLE")
print("=" * 60)

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    branch TEXT,
    cgpa REAL
)
""")

connection.commit()

print("Table Created Successfully")


# ==========================================================
# INSERT RECORDS
# ==========================================================

print("\n" + "=" * 60)
print("3. INSERT RECORDS")
print("=" * 60)

students = [
    (1, "Vikhyath", 20, "CSE", 9.10),
    (2, "Rahul", 21, "ISE", 8.75),
    (3, "Priya", 20, "ECE", 9.30),
    (4, "Anjali", 22, "AIML", 8.90)
]

cursor.executemany("""
INSERT OR IGNORE INTO students
VALUES(?,?,?,?,?)
""", students)

connection.commit()

print("Records Inserted Successfully")


# ==========================================================
# READ RECORDS
# ==========================================================

print("\n" + "=" * 60)
print("4. READ RECORDS")
print("=" * 60)

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

print("Student Details:\n")

for record in records:
    print(record)


# ==========================================================
# UPDATE RECORD
# ==========================================================

print("\n" + "=" * 60)
print("5. UPDATE RECORD")
print("=" * 60)

cursor.execute("""
UPDATE students
SET cgpa=9.50
WHERE id=2
""")

connection.commit()

print("Record Updated Successfully")

cursor.execute("SELECT * FROM students WHERE id=2")

print(cursor.fetchone())


# ==========================================================
# DELETE RECORD
# ==========================================================

print("\n" + "=" * 60)
print("6. DELETE RECORD")
print("=" * 60)

cursor.execute("""
DELETE FROM students
WHERE id=4
""")

connection.commit()

print("Record Deleted Successfully")


# ==========================================================
# DISPLAY FINAL TABLE
# ==========================================================

print("\nFinal Table:\n")

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)


# ==========================================================
# PARAMETERIZED QUERY
# ==========================================================

print("\n" + "=" * 60)
print("7. PARAMETERIZED QUERY")
print("=" * 60)

student_id = 3

cursor.execute(
    "SELECT * FROM students WHERE id=?",
    (student_id,)
)

print(cursor.fetchone())


# ==========================================================
# COUNT RECORDS
# ==========================================================

print("\n" + "=" * 60)
print("8. COUNT RECORDS")
print("=" * 60)

cursor.execute("SELECT COUNT(*) FROM students")

print("Total Students :", cursor.fetchone()[0])


# ==========================================================
# CLOSE CONNECTION
# ==========================================================

connection.close()

print("\nDatabase Connection Closed.")


# ==========================================================
# INTERVIEW SUMMARY
# ==========================================================

print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
SQLite

✔ Lightweight Database

✔ No Server Required

✔ Stored in a Single File

--------------------------------------------------

sqlite3 Module

import sqlite3

--------------------------------------------------

Connect Database

sqlite3.connect("students.db")

--------------------------------------------------

Cursor

cursor = connection.cursor()

--------------------------------------------------

Execute Query

cursor.execute(SQL)

--------------------------------------------------

Insert Multiple Records

executemany()

--------------------------------------------------

Fetch Methods

fetchone()

fetchall()

--------------------------------------------------

Commit Changes

connection.commit()

--------------------------------------------------

Close Database

connection.close()

--------------------------------------------------

Parameterized Query

cursor.execute(
    "SELECT * FROM students WHERE id=?",
    (id,)
)

Protects against SQL Injection.

--------------------------------------------------

CRUD Operations

Create

INSERT

Read

SELECT

Update

UPDATE

Delete

DELETE

--------------------------------------------------

Most Asked Interview Questions

✔ SQLite vs MySQL

✔ execute() vs executemany()

✔ fetchone() vs fetchall()

✔ commit()

✔ cursor()

✔ SQL Injection

✔ Parameterized Queries

✔ CRUD Operations
""")