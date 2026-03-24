filename = "students.txt"

while True:

    print("\n------ STUDENT MANAGEMENT SYSTEM ------")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Update Student")
    print("5 Delete Student")
    print("6 Exit")

    choice = input("Enter choice: ")

    # 1 Add Student
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        marks = input("Enter marks: ")

        with open(filename, "a") as f:
            f.write(f"{name},{age},{marks}\n")

        print("Student added successfully.")

    # 2 View Students
    elif choice == "2":
        try:
            with open(filename, "r") as f:
                print("\n--- Student Records ---")
                for line in f:
                    name, age, marks = line.strip().split(",")
                    print(f"Name: {name}, Age: {age}, Marks: {marks}")
        except FileNotFoundError:
            print("No records found.")

    # 3 Search Student
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        try:
            with open(filename, "r") as f:
                for line in f:
                    name, age, marks = line.strip().split(",")
                    if name.lower() == search_name.lower():
                        print(f"Found -> Name: {name}, Age: {age}, Marks: {marks}")
                        found = True
        except FileNotFoundError:
            print("File not found.")

        if not found:
            print("Student not found.")

    # 4 Update Student
    elif choice == "4":
        search_name = input("Enter name to update: ")
        updated = False
        records = []

        try:
            with open(filename, "r") as f:
                for line in f:
                    name, age, marks = line.strip().split(",")

                    if name.lower() == search_name.lower():
                        print("Old Record:", name, age, marks)
                        age = input("Enter new age: ")
                        marks = input("Enter new marks: ")
                        updated = True

                    records.append(f"{name},{age},{marks}\n")

            with open(filename, "w") as f:
                f.writelines(records)

            if updated:
                print("Record updated successfully.")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("File not found.")

    # 5 Delete Student
    elif choice == "5":
        search_name = input("Enter name to delete: ")
        deleted = False
        records = []

        try:
            with open(filename, "r") as f:
                for line in f:
                    name, age, marks = line.strip().split(",")

                    if name.lower() != search_name.lower():
                        records.append(line)
                    else:
                        deleted = True

            with open(filename, "w") as f:
                f.writelines(records)

            if deleted:
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("File not found.")

    # Exit
    elif choice == "6":
        break

    else:
        print("Invalid choice")