while True:

    print("\n------ EXCEPTION HANDLING PROGRAM ------")
    print("1 Handle Division by Zero")
    print("2 Handle Invalid Input")
    print("3 Multiple Except Blocks")
    print("4 Use Finally Block")
    print("5 Custom Error Message")
    print("6 Exit")

    choice = input("Enter choice: ")

    # 1 Division by zero
    if choice == "1":
        try:
            a = int(input("Enter number: "))
            b = int(input("Enter divisor: "))
            result = a / b
            print("Result:", result)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")

    # 2 Invalid input
    elif choice == "2":
        try:
            num = int(input("Enter a number: "))
            print("You entered:", num)

        except ValueError:
            print("Invalid input! Please enter a number.")

    # 3 Multiple except blocks
    elif choice == "3":
        try:
            a = int(input("Enter number: "))
            b = int(input("Enter divisor: "))
            print("Result:", a / b)

        except ZeroDivisionError:
            print("Cannot divide by zero.")

        except ValueError:
            print("Please enter valid numbers.")

    # 4 Finally block
    elif choice == "4":
        try:
            num = int(input("Enter number: "))
            print("Square:", num * num)

        except ValueError:
            print("Invalid number.")

        finally:
            print("This block always executes.")

    # 5 Custom error message
    elif choice == "5":
        try:
            age = int(input("Enter age: "))

            if age < 0:
                raise ValueError("Age cannot be negative!")

            print("Age entered:", age)

        except ValueError as e:
            print("Custom Error:", e)

    # Exit
    elif choice == "6":
        break

    else:
        print("Invalid choice")