import datetime
import time

while True:
    print("\n----- DATETIME MODULE PROGRAM -----")
    print("1. Current Date & Time")
    print("2. Age Calculator")
    print("3. Days Between Two Dates")
    print("4. Countdown Timer")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1 Current Date & Time
    if choice == "1":
        now = datetime.datetime.now()
        print("Current Date & Time:", now)

    # 2 Age Calculator
    elif choice == "2":
        year = int(input("Enter birth year: "))
        month = int(input("Enter birth month: "))
        day = int(input("Enter birth day: "))

        birthdate = datetime.date(year, month, day)
        today = datetime.date.today()

        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        print("Your Age:", age, "years")

    # 3 Days Between Two Dates
    elif choice == "3":
        print("Enter First Date")
        y1 = int(input("Year: "))
        m1 = int(input("Month: "))
        d1 = int(input("Day: "))

        print("Enter Second Date")
        y2 = int(input("Year: "))
        m2 = int(input("Month: "))
        d2 = int(input("Day: "))

        date1 = datetime.date(y1, m1, d1)
        date2 = datetime.date(y2, m2, d2)

        diff = abs((date2 - date1).days)
        print("Days Between:", diff)

    # 4 Countdown Timer
    elif choice == "4":
        seconds = int(input("Enter countdown seconds: "))

        while seconds > 0:
            print("Time left:", seconds, "seconds")
            time.sleep(1)
            seconds -= 1

        print("Time's up!")

    # Exit
    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")