while True:

    print("\n------ EXCEPTION VALIDATION PROGRAM ------")
    print("1 Raise Exception Manually")
    print("2 Validate Age Input")
    print("3 Validate Email Input")
    print("4 Exit")

    choice = input("Enter choice: ")

    # 1 Raise exception manually
    if choice == "1":
        try:
            num = int(input("Enter a positive number: "))

            if num < 0:
                raise ValueError("Negative numbers are not allowed!")

            print("You entered:", num)

        except ValueError as e:
            print("Error:", e)

    # 2 Validate age input
    elif choice == "2":
        try:
            age = int(input("Enter your age: "))

            if age < 0 or age > 120:
                raise ValueError("Age must be between 0 and 120")

            print("Valid age:", age)

        except ValueError as e:
            print("Invalid input:", e)

    # 3 Validate email input
    elif choice == "3":
        try:
            email = input("Enter email: ")

            if "@" not in email or "." not in email:
                raise ValueError("Invalid email format")

            print("Valid email:", email)

        except ValueError as e:
            print("Error:", e)

    # Exit
    elif choice == "4":
        break

    else:
        print("Invalid choice")