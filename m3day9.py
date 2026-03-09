import csv

filename = "students.csv"

while True:
    print("\n----- CSV FILE MENU -----")
    print("1. Write data into CSV")
    print("2. Read CSV file")
    print("3. Count rows in CSV")
    print("4. Search record in CSV")
    print("5. Update record in CSV")
    print("6. Exit")

    choice = input("Enter choice: ")

    # 1. Write data
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        marks = input("Enter marks: ")

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, marks])

        print("Record added successfully.")

    # 2. Read CSV
    elif choice == "2":
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print("File not found.")

    # 3. Count rows
    elif choice == "3":
        count = 0
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    count += 1
            print("Total rows:", count)
        except FileNotFoundError:
            print("File not found.")

    # 4. Search record
    elif choice == "4":
        search_name = input("Enter name to search: ")
        found = False

        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == search_name:
                    print("Record found:", row)
                    found = True

        if not found:
            print("Record not found.")

    # 5. Update record
    elif choice == "5":
        search_name = input("Enter name to update: ")
        updated_rows = []

        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == search_name:
                    print("Old Record:", row)
                    new_age = input("Enter new age: ")
                    new_marks = input("Enter new marks: ")
                    row = [search_name, new_age, new_marks]
                updated_rows.append(row)

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        print("Record updated successfully.")

    # Exit
    elif choice == "6":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")