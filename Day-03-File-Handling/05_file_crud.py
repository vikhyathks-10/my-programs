# 05_file_crud.py

filename = "records.txt"

while True:

    print("\n1.Add")
    print("2.View")
    print("3.Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        name = input("Enter Name : ")

        with open(filename, "a") as file:
            file.write(name + "\n")

    elif choice == "2":

        try:
            with open(filename, "r") as file:
                print("\nRecords")
                print(file.read())

        except FileNotFoundError:
            print("No Records Found.")

    elif choice == "3":
        break

    else:
        print("Invalid Choice")