import csv
import os

while True:

    print("\n------ SAFE FILE HANDLING PROGRAM ------")
    print("1 Handle File Not Found Error")
    print("2 Handle Permission Error")
    print("3 Safe File Reader")
    print("4 Safe File Writer")
    print("5 Validate File Extension")
    print("6 Handle CSV Format Errors")
    print("7 Exit")

    choice = input("Enter choice: ")

    # 1 File Not Found
    if choice == "1":
        filename = input("Enter file name: ")

        try:
            with open(filename, "r") as f:
                print(f.read())

        except FileNotFoundError:
            print("Error: File not found!")

    # 2 Permission Error
    elif choice == "2":
        filename = input("Enter file name: ")

        try:
            with open(filename, "w") as f:
                f.write("Testing permission")

        except PermissionError:
            print("Error: No permission to write file!")

    # 3 Safe File Reader
    elif choice == "3":
        filename = input("Enter file name: ")

        try:
            with open(filename, "r") as f:
                for line in f:
                    print(line.strip())

        except FileNotFoundError:
            print("File does not exist.")
        except Exception as e:
            print("Unexpected error:", e)

    # 4 Safe File Writer
    elif choice == "4":
        filename = input("Enter file name: ")
        data = input("Enter text: ")

        try:
            with open(filename, "a") as f:
                f.write(data + "\n")
            print("Data written successfully.")

        except PermissionError:
            print("Write permission denied.")
        except Exception as e:
            print("Error:", e)

    # 5 Validate File Extension
    elif choice == "5":
        filename = input("Enter file name: ")

        if filename.endswith(".txt"):
            print("Valid text file.")
        else:
            print("Invalid file type! Only .txt allowed.")

    # 6 Handle CSV Format Errors
    elif choice == "6":
        filename = input("Enter CSV file name: ")

        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)

                for row in reader:
                    if len(row) != 3:
                        raise ValueError("Invalid CSV format! Each row must have 3 values")

                    print("Row:", row)

        except FileNotFoundError:
            print("CSV file not found.")
        except ValueError as e:
            print("Format Error:", e)
        except Exception as e:
            print("Other Error:", e)

    # Exit
    elif choice == "7":
        break

    else:
        print("Invalid choice")