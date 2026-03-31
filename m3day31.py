import csv
import os

users_file = "users.txt"
students_file = "students.csv"

# Create files if not exist
if not os.path.exists(users_file):
    open(users_file, "w").close()

if not os.path.exists(students_file):
    with open(students_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Marks"])


# -------- AUTH SYSTEM --------
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(users_file, "a") as f:
        f.write(f"{username},{password}\n")

    print("User registered successfully")


def login():
    attempts = 3

    while attempts > 0:
        user = input("Username: ")
        pwd = input("Password: ")

        with open(users_file, "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                if u == user and p == pwd:
                    print("Login successful ✅")
                    return True

        attempts -= 1
        print("Invalid credentials. Attempts left:", attempts)

    print("Account locked ❌")
    return False


# -------- STUDENT SYSTEM --------
def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    with open(students_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, age, marks])

    print("Student added")


def view_students():
    with open(students_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def search_student():
    name = input("Enter name to search: ")
    found = False

    with open(students_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].lower() == name.lower():
                print("Found:", row)
                found = True

    if not found:
        print("Student not found")


def update_student():
    name = input("Enter name to update: ")
    rows = []
    updated = False

    with open(students_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].lower() == name.lower():
                age = input("New age: ")
                marks = input("New marks: ")
                row = [name, age, marks]
                updated = True
            rows.append(row)

    with open(students_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Updated" if updated else "Student not found")


def delete_student():
    name = input("Enter name to delete: ")
    rows = []
    deleted = False

    with open(students_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].lower() != name.lower():
                rows.append(row)
            else:
                deleted = True

    with open(students_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Deleted" if deleted else "Student not found")


# -------- MAIN PROGRAM --------
while True:

    print("\n------ STUDENT PORTAL ------")
    print("1 Register")
    print("2 Login")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        if login():

            while True:
                print("\n--- STUDENT MENU ---")
                print("1 Add Student")
                print("2 View Students")
                print("3 Search Student")
                print("4 Update Student")
                print("5 Delete Student")
                print("6 Logout")

                opt = input("Enter option: ")

                try:
                    if opt == "1":
                        add_student()
                    elif opt == "2":
                        view_students()
                    elif opt == "3":
                        search_student()
                    elif opt == "4":
                        update_student()
                    elif opt == "5":
                        delete_student()
                    elif opt == "6":
                        break
                    else:
                        print("Invalid option")

                except Exception as e:
                    print("Error:", e)

    elif choice == "3":
        break

    else:
        print("Invalid choice")