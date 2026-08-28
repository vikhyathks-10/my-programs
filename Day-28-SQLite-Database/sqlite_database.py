# ============================================================
# MONTH 8 - DAY 28
# PYTHON + SQLITE DATABASE
#
# Programs 141-145
#
# 141. Create a Database
# 142. Insert Records
# 143. Search Records
# 144. Update/Delete Records
# 145. Complete Python + SQLite Application
#
# Library:
# sqlite3
#
# How to run:
# python sqlite_database.py
# ============================================================

import sqlite3


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

DATABASE_NAME = "students.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def connect_database():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    return connection


# ============================================================
# PROGRAM 141
# CREATE DATABASE AND TABLE
# ============================================================

def create_database():

    print("\n" + "=" * 60)
    print("        PROGRAM 141 - CREATE DATABASE")
    print("=" * 60)

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            marks REAL NOT NULL
        )
    """)

    connection.commit()

    connection.close()

    print("\nDatabase created successfully!")

    print(
        f"Database file: {DATABASE_NAME}"
    )

    print(
        "Students table is ready."
    )


# ============================================================
# PROGRAM 142
# INSERT RECORD
# ============================================================

def insert_record():

    print("\n" + "=" * 60)
    print("           PROGRAM 142 - INSERT RECORD")
    print("=" * 60)

    name = input(
        "\nEnter student name: "
    ).strip()

    if not name:

        print(
            "Name cannot be empty."
        )

        return

    try:

        age = int(
            input("Enter age: ")
        )

        marks = float(
            input("Enter marks: ")
        )

    except ValueError:

        print(
            "\nPlease enter valid numeric values."
        )

        return

    course = input(
        "Enter course: "
    ).strip()

    if not course:

        print(
            "Course cannot be empty."
        )

        return

    if age <= 0:

        print(
            "Age must be greater than 0."
        )

        return

    if marks < 0 or marks > 100:

        print(
            "Marks must be between 0 and 100."
        )

        return

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (name, age, course, marks)
        VALUES (?, ?, ?, ?)
        """,
        (
            name,
            age,
            course,
            marks
        )
    )

    connection.commit()

    connection.close()

    print(
        "\nStudent record inserted successfully!"
    )


# ============================================================
# DISPLAY ALL RECORDS
# ============================================================

def display_records():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    records = cursor.fetchall()

    connection.close()

    if not records:

        print(
            "\nNo student records found."
        )

        return

    print("\n" + "-" * 75)

    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Course':<20}"
        f"{'Marks':<10}"
    )

    print("-" * 75)

    for record in records:

        student_id = record[0]
        name = record[1]
        age = record[2]
        course = record[3]
        marks = record[4]

        print(
            f"{student_id:<5}"
            f"{name:<20}"
            f"{age:<8}"
            f"{course:<20}"
            f"{marks:<10.2f}"
        )

    print("-" * 75)


# ============================================================
# PROGRAM 143
# SEARCH RECORDS
# ============================================================

def search_records():

    print("\n" + "=" * 60)
    print("           PROGRAM 143 - SEARCH RECORD")
    print("=" * 60)

    print(
        "\n1. Search by ID"
    )

    print(
        "2. Search by Name"
    )

    print(
        "3. Search by Course"
    )

    choice = input(
        "\nEnter choice: "
    ).strip()

    connection = connect_database()

    cursor = connection.cursor()

    if choice == "1":

        try:

            student_id = int(
                input(
                    "Enter student ID: "
                )
            )

        except ValueError:

            print(
                "Invalid ID."
            )

            connection.close()

            return

        cursor.execute(
            """
            SELECT * FROM students
            WHERE id = ?
            """,
            (student_id,)
        )

    elif choice == "2":

        name = input(
            "Enter student name: "
        ).strip()

        cursor.execute(
            """
            SELECT * FROM students
            WHERE name LIKE ?
            """,
            (
                "%" + name + "%",
            )
        )

    elif choice == "3":

        course = input(
            "Enter course: "
        ).strip()

        cursor.execute(
            """
            SELECT * FROM students
            WHERE course LIKE ?
            """,
            (
                "%" + course + "%",
            )
        )

    else:

        print(
            "\nInvalid choice."
        )

        connection.close()

        return

    records = cursor.fetchall()

    connection.close()

    if not records:

        print(
            "\nNo matching records found."
        )

        return

    print("\n" + "-" * 75)

    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Course':<20}"
        f"{'Marks':<10}"
    )

    print("-" * 75)

    for record in records:

        print(
            f"{record[0]:<5}"
            f"{record[1]:<20}"
            f"{record[2]:<8}"
            f"{record[3]:<20}"
            f"{record[4]:<10.2f}"
        )

    print("-" * 75)


# ============================================================
# PROGRAM 144
# UPDATE RECORD
# ============================================================

def update_record():

    print("\n" + "=" * 60)
    print("           PROGRAM 144 - UPDATE RECORD")
    print("=" * 60)

    try:

        student_id = int(
            input(
                "\nEnter student ID to update: "
            )
        )

    except ValueError:

        print(
            "Invalid ID."
        )

        return

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    record = cursor.fetchone()

    if not record:

        print(
            "\nStudent not found."
        )

        connection.close()

        return

    print(
        "\nCurrent record:"
    )

    print(
        f"Name   : {record[1]}"
    )

    print(
        f"Age    : {record[2]}"
    )

    print(
        f"Course : {record[3]}"
    )

    print(
        f"Marks  : {record[4]}"
    )

    print(
        "\nPress Enter to keep the existing value."
    )

    name = input(
        f"Name [{record[1]}]: "
    ).strip()

    age_input = input(
        f"Age [{record[2]}]: "
    ).strip()

    course = input(
        f"Course [{record[3]}]: "
    ).strip()

    marks_input = input(
        f"Marks [{record[4]}]: "
    ).strip()

    if not name:

        name = record[1]

    if not course:

        course = record[3]

    if age_input:

        try:

            age = int(
                age_input
            )

        except ValueError:

            print(
                "Invalid age."
            )

            connection.close()

            return

    else:

        age = record[2]

    if marks_input:

        try:

            marks = float(
                marks_input
            )

        except ValueError:

            print(
                "Invalid marks."
            )

            connection.close()

            return

    else:

        marks = record[4]

    if age <= 0:

        print(
            "Age must be greater than 0."
        )

        connection.close()

        return

    if marks < 0 or marks > 100:

        print(
            "Marks must be between 0 and 100."
        )

        connection.close()

        return

    cursor.execute(
        """
        UPDATE students
        SET name = ?,
            age = ?,
            course = ?,
            marks = ?
        WHERE id = ?
        """,
        (
            name,
            age,
            course,
            marks,
            student_id
        )
    )

    connection.commit()

    connection.close()

    print(
        "\nRecord updated successfully!"
    )


# ============================================================
# PROGRAM 144
# DELETE RECORD
# ============================================================

def delete_record():

    print("\n" + "=" * 60)
    print("           PROGRAM 144 - DELETE RECORD")
    print("=" * 60)

    try:

        student_id = int(
            input(
                "\nEnter student ID to delete: "
            )
        )

    except ValueError:

        print(
            "Invalid ID."
        )

        return

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    record = cursor.fetchone()

    if not record:

        print(
            "\nStudent not found."
        )

        connection.close()

        return

    print(
        f"\nStudent: {record[1]}"
    )

    confirm = input(
        "Are you sure you want to delete? (y/n): "
    ).strip().lower()

    if confirm == "y":

        cursor.execute(
            """
            DELETE FROM students
            WHERE id = ?
            """,
            (student_id,)
        )

        connection.commit()

        print(
            "\nRecord deleted successfully!"
        )

    else:

        print(
            "\nDelete operation cancelled."
        )

    connection.close()


# ============================================================
# PROGRAM 145
# COMPLETE DATABASE APPLICATION
# ============================================================

def database_application():

    while True:

        print("\n" + "=" * 65)
        print("             STUDENT DATABASE APPLICATION")
        print("=" * 65)

        print(
            "1. Create Database/Table"
        )

        print(
            "2. Insert Student"
        )

        print(
            "3. Display All Students"
        )

        print(
            "4. Search Student"
        )

        print(
            "5. Update Student"
        )

        print(
            "6. Delete Student"
        )

        print(
            "7. Exit"
        )

        print("=" * 65)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            create_database()

        elif choice == "2":

            insert_record()

        elif choice == "3":

            display_records()

        elif choice == "4":

            search_records()

        elif choice == "5":

            update_record()

        elif choice == "6":

            delete_record()

        elif choice == "7":

            print(
                "\nExiting Student Database Application..."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    # Create database automatically when program starts

    create_database()

    print("\n" + "=" * 65)
    print("          PYTHON + SQLITE DATABASE")
    print("=" * 65)

    print(
        "\nPrograms 141-145"
    )

    print(
        "Database: students.db"
    )

    while True:

        print("\n" + "=" * 65)

        print(
            "1. Create Database"
        )

        print(
            "2. Insert Record"
        )

        print(
            "3. Search Records"
        )

        print(
            "4. Update Record"
        )

        print(
            "5. Delete Record"
        )

        print(
            "6. Display All Records"
        )

        print(
            "7. Complete Student Database Application"
        )

        print(
            "8. Exit"
        )

        print("=" * 65)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            create_database()

        elif choice == "2":

            insert_record()

        elif choice == "3":

            search_records()

        elif choice == "4":

            update_record()

        elif choice == "5":

            delete_record()

        elif choice == "6":

            display_records()

        elif choice == "7":

            database_application()

        elif choice == "8":

            print(
                "\nThank you for using "
                "Python + SQLite!"
            )

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()