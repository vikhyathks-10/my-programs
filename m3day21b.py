import csv
import os

filename = "students.csv"

# Ensure file exists
if not os.path.exists(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Marks"])  # header


while True:

    print("\n------ CSV STUDENT SYSTEM ------")
    print("1 Add student record")
    print("2 Search student")
    print("3 Update student record")
    print("4 Delete student record")
    print("5 Validate CSV structure")
    print("6 Exit")

    choice = input("Enter choice: ")

    # 1 Add student
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        marks = input("Enter marks: ")

        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, age, marks])

        print("Student added successfully.")

    # 2 Search student
    elif choice == "2":
        search_name = input("Enter name to search: ")
        found = False

        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header

            for row in reader:
                if row[0].lower() == search_name.lower():
                    print("Record found:", row)
                    found = True

        if not found:
            print("Student not found.")

    # 3 Update student
    elif choice == "3":
        search_name = input("Enter name to update: ")
        updated = False
        rows = []

        with open(filename, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows.append(header)

            for row in reader:
                if row[0].lower() == search_name.lower():
                    print("Old Record:", row)
                    new_age = input("Enter new age: ")
                    new_marks = input("Enter new marks: ")
                    row = [search_name, new_age, new_marks]
                    updated = True
                rows.append(row)

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        if updated:
            print("Record updated successfully.")
        else:
            print("Student not found.")

    # 4 Delete student
    elif choice == "4":
        search_name = input("Enter name to delete: ")
        deleted = False
        rows = []

        with open(filename, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows.append(header)

            for row in reader:
                if row[0].lower() != search_name.lower():
                    rows.append(row)
                else:
                    deleted = True

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        if deleted:
            print("Record deleted successfully.")
        else:
            print("Student not found.")

    # 5 Validate CSV structure
    elif choice == "5":
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                header = next(reader)

                if header != ["Name", "Age", "Marks"]:
                    raise ValueError("Invalid header format!")

                for row in reader:
                    if len(row) != 3:
                        raise ValueError("Invalid row format!")

                    if not row[1].isdigit() or not row[2].isdigit():
                        raise ValueError("Age and Marks must be numbers!")

            print("CSV structure is valid.")

        except Exception as e:
            print("CSV Validation Error:", e)

    # Exit
    elif choice == "6":
        break

    else:
        print("Invalid choice")