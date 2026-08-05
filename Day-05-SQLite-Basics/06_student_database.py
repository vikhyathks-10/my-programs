# 06_student_database.py

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


def add_student():
    sid = int(input("ID: "))
    name = input("Name: ")
    age = int(input("Age: "))
    branch = input("Branch: ")

    cursor.execute(
        "INSERT INTO students VALUES(?,?,?,?)",
        (sid, name, age, branch)
    )

    conn.commit()

    print("Student Added Successfully!")


def view_students():

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    print("\n===== STUDENTS =====")

    for row in data:
        print(row)


def search_student():

    sid = int(input("Enter ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (sid,)
    )

    record = cursor.fetchone()

    if record:
        print(record)
    else:
        print("Student Not Found")


def update_student():

    sid = int(input("Enter ID: "))
    age = int(input("New Age: "))

    cursor.execute(
        "UPDATE students SET age=? WHERE id=?",
        (age, sid)
    )

    conn.commit()

    print("Student Updated Successfully!")


def delete_student():

    sid = int(input("Enter ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (sid,)
    )

    conn.commit()

    print("Student Deleted Successfully!")


while True:

    print("\n===== STUDENT DATABASE =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")

conn.close()