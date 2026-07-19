# ==========================================================
# Month 7 - Day 19
# File Handling & Exception Handling
#
# Topics Covered:
# 1. Reading a File
# 2. Writing to a File
# 3. Appending to a File
# 4. try-except-finally
# 5. Custom Exception
# 6. Multiple Exceptions
# ==========================================================

print("=" * 60)
print("1. WRITING TO A FILE")
print("=" * 60)

with open("sample.txt", "w") as file:
    file.write("Welcome to Python File Handling.\n")
    file.write("This is Day 19 Practice.\n")

print("Data Written Successfully!")


print("\n" + "=" * 60)
print("2. READING A FILE")
print("=" * 60)

with open("sample.txt", "r") as file:
    content = file.read()

print("File Content:")
print(content)


print("\n" + "=" * 60)
print("3. APPENDING TO A FILE")
print("=" * 60)

with open("sample.txt", "a") as file:
    file.write("Appending a new line.\n")

print("Data Appended Successfully!")

with open("sample.txt", "r") as file:
    print(file.read())


print("\n" + "=" * 60)
print("4. TRY - EXCEPT - FINALLY")
print("=" * 60)

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Please enter a valid integer!")

finally:
    print("Execution Completed.")


print("\n" + "=" * 60)
print("5. CUSTOM EXCEPTION")
print("=" * 60)

class AgeError(Exception):
    pass

try:
    age = int(input("Enter Age: "))

    if age < 18:
        raise AgeError("Age must be at least 18.")

    print("Eligible!")

except AgeError as e:
    print("Custom Exception:", e)


print("\n" + "=" * 60)
print("6. MULTIPLE EXCEPTIONS")
print("=" * 60)

try:
    a = int(input("Enter Numerator: "))
    b = int(input("Enter Denominator: "))

    print("Division =", a / b)

except ValueError:
    print("Invalid Input!")

except ZeroDivisionError:
    print("Division by Zero!")

except Exception as e:
    print("Unexpected Error:", e)


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ File Handling

Modes

r  -> Read

w  -> Write

a  -> Append

x  -> Create New File

--------------------------------------------------

✔ with open()

Automatically closes file.

Preferred over

open()

--------------------------------------------------

✔ Read Methods

read()

readline()

readlines()

--------------------------------------------------

✔ Write Methods

write()

writelines()

--------------------------------------------------

✔ Exception Handling

try

except

else

finally

--------------------------------------------------

✔ Common Exceptions

ValueError

TypeError

IndexError

KeyError

FileNotFoundError

ZeroDivisionError

--------------------------------------------------

✔ Custom Exception

class MyError(Exception):
    pass

Raise using

raise MyError()

--------------------------------------------------

Interview Tip

Whenever you hear

✔ File Processing

Think:

with open()

Whenever you hear

✔ Error Handling

Think:

try-except

Always use specific exceptions
instead of generic Exception.
""")