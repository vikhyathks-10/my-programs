import csv
import os

filename = "students.csv"

# Create file with header if not exists
if not os.path.exists(filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Marks1", "Marks2", "Marks3", "Average", "Grade"])


# -------- Grade Function --------
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"


while True:

    print("\n------ CSV STUDENT SYSTEM (ADVANCED) ------")
    print("1 Add Student")
    print("2 Search Student")
    print("3 Update Student")
    print("4 Show All Students")
    print("5 Exit")

    choice = input("Enter choice: ")

    # 1 Add Student
    if choice == "1":
        name = input("Enter name: ")
        m1 = int(input("Enter marks1: "))
        m2 = int(input("Enter marks2: "))
        m3 = int(input("Enter marks3: "))

        avg = (m1 + m2 + m3) / 3
        grade = get_grade(avg)

        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, m1, m2, m3, avg, grade])

        print("Student added successfully.")

    # 2 Search Student
    elif choice == "2":
        search_name = input("Enter name to search: ")
        found = False

        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                if row[0].lower() == search_name.lower():
                    print("Record:", row)
                    found = True

        if not found:
            print("Student not found.")

    # 3 Update Student
    elif choice == "3":
        search_name = input("Enter name to update: ")
        rows = []
        updated = False

        with open(filename, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows.append(header)

            for row in reader:
                if row[0].lower() == search_name.lower():
                    print("Old Record:", row)

                    m1 = int(input("Enter new marks1: "))
                    m2 = int(input("Enter new marks2: "))
                    m3 = int(input("Enter new marks3: "))

                    avg = (m1 + m2 + m3) / 3
                    grade = get_grade(avg)

                    row = [search_name, m1, m2, m3, avg, grade]
                    updated = True

                rows.append(row)

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        if updated:
            print("Record updated successfully.")
        else:
            print("Student not found.")

    # 4 Show All Students
    elif choice == "4":
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print("File not found.")

    # Exit
    elif choice == "5":
        break

    else:
        print("Invalid choice")