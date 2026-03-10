import math

while True:
    print("\n----- MATH MODULE PROGRAM -----")
    print("1. Scientific Calculator")
    print("2. Find Factorial")
    print("3. Area Calculator")
    print("4. Trigonometric Calculator")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1 Scientific Calculator
    if choice == "1":
        print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Power")
        print("3. Log")
        
        sc = input("Choose operation: ")

        if sc == "1":
            num = float(input("Enter number: "))
            print("Square Root =", math.sqrt(num))

        elif sc == "2":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result =", math.pow(a, b))

        elif sc == "3":
            num = float(input("Enter number: "))
            print("Log =", math.log(num))

    # 2 Factorial
    elif choice == "2":
        num = int(input("Enter number: "))
        print("Factorial =", math.factorial(num))

    # 3 Area Calculator
    elif choice == "3":
        print("\nArea Calculator")
        print("1. Circle")
        print("2. Triangle")

        ac = input("Choose shape: ")

        if ac == "1":
            r = float(input("Enter radius: "))
            area = math.pi * r * r
            print("Area of Circle =", area)

        elif ac == "2":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = 0.5 * b * h
            print("Area of Triangle =", area)

    # 4 Trigonometric Calculator
    elif choice == "4":
        angle = float(input("Enter angle in degrees: "))
        rad = math.radians(angle)

        print("sin =", math.sin(rad))
        print("cos =", math.cos(rad))
        print("tan =", math.tan(rad))

    # Exit
    elif choice == "5":
        print("Program exited")
        break

    else:
        print("Invalid choice")