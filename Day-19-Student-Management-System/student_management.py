import json
import os

FILE_NAME = "students.json"

# ==================================================

# FILE HANDLING

# ==================================================

def load_students():
    """Load student records from JSON file."""

    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(
            FILE_NAME,
            "r",
            encoding="utf-8"
        ) as file:

            students = json.load(file)

            if isinstance(students, dict):
                return students

            return {}

    except json.JSONDecodeError:
        print("\nError: Invalid students.json file.")
        return {}

    except Exception as e:
        print(f"\nError loading students: {e}")
        return {}

def save_students(students):
    """Save student records to JSON file."""

    try:
        with open(
            FILE_NAME,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                students,
                file,
                indent=4
            )

        return True

    except Exception as e:
        print(f"\nError saving students: {e}")
        return False

# ==================================================

# PROGRAM 96

# ADD STUDENT

# ==================================================

def add_student(students):

    print("\n" + "-" * 45)
    print("             ADD STUDENT")
    print("-" * 45)

    student_id = input(
        "Enter Student ID: "
    ).strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print(
            "\nStudent with this ID already exists."
        )
        return

    name = input(
        "Enter Student Name: "
    ).strip()

    if not name:
        print("Student name cannot be empty.")
        return

    age_input = input(
        "Enter Age: "
    ).strip()

    try:
        age = int(age_input)

        if age <= 0:
            print("Age must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    course = input(
        "Enter Course: "
    ).strip()

    if not course:
        print("Course cannot be empty.")
        return

    email = input(
        "Enter Email: "
    ).strip()

    if not email:
        print("Email cannot be empty.")
        return

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "email": email
    }

    if save_students(students):

        print(
            f"\nStudent '{name}' added successfully."
        )

# ==================================================

# PROGRAM 97

# SEARCH STUDENT

# ==================================================

def search_student(students):

    print("\n" + "-" * 45)
    print("           SEARCH STUDENT")
    print("-" * 45)

    student_id = input(
        "Enter Student ID: "
    ).strip()

    if student_id in students:

        student = students[student_id]

        print("\nStudent Found!")
        print("-" * 30)
        print(f"ID     : {student_id}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print(f"Email  : {student['email']}")

    else:

        print(
            "\nStudent with this ID was not found."
        )

# ==================================================

# PROGRAM 98

# UPDATE STUDENT

# ==================================================

def update_student(students):

    print("\n" + "-" * 45)
    print("           UPDATE STUDENT")
    print("-" * 45)

    student_id = input(
        "Enter Student ID: "
    ).strip()

    if student_id not in students:

        print(
            "\nStudent with this ID was not found."
        )

        return

    student = students[student_id]

    print("\nCurrent Student Details:")
    print(f"Name   : {student['name']}")
    print(f"Age    : {student['age']}")
    print(f"Course : {student['course']}")
    print(f"Email  : {student['email']}")

    print(
        "\nPress Enter to keep the existing value."
    )

    name = input(
        f"Name [{student['name']}]: "
    ).strip()

    age_input = input(
        f"Age [{student['age']}]: "
    ).strip()

    course = input(
        f"Course [{student['course']}]: "
    ).strip()

    email = input(
        f"Email [{student['email']}]: "
    ).strip()

    if name:
        student["name"] = name

    if age_input:

        try:
            age = int(age_input)

            if age <= 0:
                print(
                    "Invalid age. Keeping old age."
                )
            else:
                student["age"] = age

        except ValueError:

            print(
                "Invalid age. Keeping old age."
            )

    if course:
        student["course"] = course

    if email:
        student["email"] = email

    if save_students(students):

        print(
            "\nStudent details updated successfully."
        )

# ==================================================

# PROGRAM 99

# DELETE STUDENT

# ==================================================

def delete_student(students):

    print("\n" + "-" * 45)
    print("           DELETE STUDENT")
    print("-" * 45)

    student_id = input(
        "Enter Student ID: "
    ).strip()

    if student_id not in students:

        print(
            "\nStudent with this ID was not found."
        )

        return

    student = students[student_id]

    print(
        f"\nStudent: {student['name']}"
    )

    confirmation = input(
        "Are you sure you want to delete "
        "this student? (y/n): "
    ).strip().lower()

    if confirmation == "y":

        del students[student_id]

        if save_students(students):

            print(
                "\nStudent deleted successfully."
            )

    else:

        print("\nDelete operation cancelled.")

# ==================================================

# DISPLAY ALL STUDENTS

# ==================================================

def display_all_students(students):

    print("\n" + "-" * 55)
    print("              ALL STUDENTS")
    print("-" * 55)

    if not students:

        print("No student records available.")
        return

    for student_id, student in students.items():

        print(
            f"\nID     : {student_id}"
        )

        print(
            f"Name   : {student['name']}"
        )

        print(
            f"Age    : {student['age']}"
        )

        print(
            f"Course : {student['course']}"
        )

        print(
            f"Email  : {student['email']}"
        )

        print("-" * 30)

# ==================================================

# MENU

# ==================================================

def display_menu():

    print("\n" + "=" * 55)
    print("          STUDENT MANAGEMENT SYSTEM")
    print("=" * 55)

    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    print("=" * 55)

# ==================================================

# PROGRAM 100

# COMPLETE MENU-DRIVEN SYSTEM

# ==================================================

def main():

    students = load_students()

    print(
        "\nWelcome to Student Management System!"
    )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_student(students)

        elif choice == "2":

            search_student(students)

        elif choice == "3":

            update_student(students)

        elif choice == "4":

            delete_student(students)

        elif choice == "5":

            display_all_students(students)

        elif choice == "6":

            print(
                "\nThank you for using "
                "Student Management System!"
            )

            break

        else:

            print(
                "\nInvalid choice."
                " Please enter a number from 1 to 6."
            )

# ==================================================

# PROGRAM ENTRY POINT

# ==================================================

if __name__ == "__main__":
    main()
