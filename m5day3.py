# 🔹 DAY 3 - SYS MODULE

import sys


# 🔹 1. Get Python Version

print("\n--- Python Version ---")
print(sys.version)


# 🔹 2. Command-Line Arguments

print("\n--- Command-Line Arguments ---")

print("Arguments Passed:")

for arg in sys.argv:
    print(arg)


# 🔹 3. Read Input from Command Line

# Example:
# python sys_day3.py Vikyat

if len(sys.argv) > 1:
    print("\nHello,", sys.argv[1])
else:
    print("\nNo name provided")


# 🔹 4. Mini Calculator using sys.argv

# Example:
# python sys_day3.py 10 + 20

if len(sys.argv) == 4:

    num1 = int(sys.argv[1])
    op = sys.argv[2]
    num2 = int(sys.argv[3])

    print("\n--- Mini Calculator ---")

    if op == "+":
        print("Result:", num1 + num2)

    elif op == "-":
        print("Result:", num1 - num2)

    elif op == "*":
        print("Result:", num1 * num2)

    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid Operator")


# 🔹 5. Exit Program using sys.exit()

choice = input("\nDo you want to exit? (yes/no): ")

if choice.lower() == "yes":
    print("Program Exiting...")
    sys.exit()

print("Program Continues...")