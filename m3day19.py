# m3day19.py
# DAY 19 — Advanced Exception Handling

# -------------------------------
# 1. File Open with Retry System
# -------------------------------
def file_retry():
    attempts = 3

    while attempts > 0:
        filename = input("Enter file name: ")

        try:
            with open(filename, "r") as file:
                print("\nFile opened successfully!")
                print(file.read())
            break

        except FileNotFoundError:
            attempts -= 1
            print(f"File not found! Attempts left: {attempts}")

            if attempts == 0:
                print("Failed after multiple attempts.")


# -------------------------------
# 2. Login System (3 Attempts)
# -------------------------------
def login_system():
    correct_username = "admin"
    correct_password = "1234"
    attempts = 0

    while attempts < 3:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if username == correct_username and password == correct_password:
                print("Login successful!")
                return
            else:
                raise ValueError("Invalid credentials")

        except ValueError as e:
            attempts += 1
            print(e)

    print("Account locked after 3 failed attempts!")


# -------------------------------
# 3. Nested Try-Except
# -------------------------------
def nested_try():
    try:
        num = int(input("Enter a number: "))

        try:
            result = 100 / num
            print("Result:", result)

        except ZeroDivisionError:
            print("Cannot divide by zero!")

    except ValueError:
        print("Invalid input! Please enter a number.")


# -------------------------------
# 4. Custom Exception (Marks)
# -------------------------------
class InvalidMarksError(Exception):
    pass

def validate_marks():
    try:
        marks = int(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            raise InvalidMarksError("Marks must be between 0 and 100")

        print("Valid marks entered:", marks)

    except InvalidMarksError as e:
        print("Error:", e)

    except ValueError:
        print("Please enter a valid number!")


# -------------------------------
# 5. Multiple Input Validation
# -------------------------------
def validate_inputs():
    try:
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))

        if age <= 0:
            raise ValueError("Age must be positive")

        if salary < 0:
            raise ValueError("Salary cannot be negative")

        print("Valid data entered!")

    except ValueError as e:
        print("Error:", e)


# -------------------------------
# MENU SYSTEM
# -------------------------------
def main():
    while True:
        print("\n===== DAY 19 MENU =====")
        print("1. File Open with Retry")
        print("2. Login System")
        print("3. Nested Try-Except")
        print("4. Validate Marks (Custom Exception)")
        print("5. Validate Multiple Inputs")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_retry()
        elif choice == "2":
            login_system()
        elif choice == "3":
            nested_try()
        elif choice == "4":
            validate_marks()
        elif choice == "5":
            validate_inputs()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


# Run program
if __name__ == "__main__":
    main()