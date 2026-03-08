import shutil

while True:
    print("\n----- FILE HANDLING MENU -----")
    print("1. Backup a file")
    print("2. Store student marks in file")
    print("3. Read marks and calculate average")
    print("4. Store login credentials")
    print("5. Validate login from file")
    print("6. Exit")

    choice = input("Enter choice: ")

    # 1. Backup a file
    if choice == "1":
        source = input("Enter file to backup: ")
        backup = source + ".bak"

        shutil.copy(source, backup)
        print("Backup created as", backup)

    # 2. Store student marks
    elif choice == "2":
        file = open("marks.txt", "a")

        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        file.write(name + " " + marks + "\n")
        file.close()

        print("Marks stored successfully")

    # 3. Read marks and calculate average
    elif choice == "3":
        file = open("marks.txt", "r")

        total = 0
        count = 0

        for line in file:
            data = line.split()
            mark = int(data[1])
            total += mark
            count += 1

        file.close()

        if count > 0:
            avg = total / count
            print("Average Marks:", avg)
        else:
            print("No data found")

    # 4. Store login credentials
    elif choice == "4":
        username = input("Enter username: ")
        password = input("Enter password: ")

        file = open("login.txt", "a")
        file.write(username + " " + password + "\n")
        file.close()

        print("Credentials saved")

    # 5. Validate login
    elif choice == "5":
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        file = open("login.txt", "r")

        found = False

        for line in file:
            u, p = line.split()
            if u == user and p == pwd:
                found = True
                break

        file.close()

        if found:
            print("Login successful")
        else:
            print("Invalid username or password")

    # Exit
    elif choice == "6":
        print("Program exited")
        break

    else:
        print("Invalid choice")