# DAY 29 - RECURSION PROBLEMS
# Programs 141 - 145


# ---------------------------------------------------------
# 141. Reverse a String Recursively
# ---------------------------------------------------------
def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]


def program_141():
    s = input("Enter a string: ")

    result = reverse_string(s)

    print("Reversed string:", result)
    print("Complexity: O(N^2) time in Python due to string slicing/concatenation")
    print("Recursion stack: O(N)")


# ---------------------------------------------------------
# 142. Check Palindrome Recursively
# ---------------------------------------------------------
def is_palindrome(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return is_palindrome(s, left + 1, right - 1)


def program_142():
    s = input("Enter a string: ")

    if is_palindrome(s, 0, len(s) - 1):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    print("Complexity: O(N) time, O(N) recursion stack")


# ---------------------------------------------------------
# 143. Find Fibonacci Number
# ---------------------------------------------------------
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def program_143():
    n = int(input("Enter N: "))

    if n < 0:
        print("Enter a non-negative integer.")
        return

    result = fibonacci(n)

    print(f"Fibonacci({n}) =", result)
    print("Complexity: O(2^N) time, O(N) recursion stack")


# ---------------------------------------------------------
# 144. Find GCD Recursively
# ---------------------------------------------------------
def gcd(a, b):
    a = abs(a)
    b = abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)


def program_144():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = gcd(a, b)

    print("GCD:", result)
    print("Complexity: O(log(min(A, B))) time, O(log(min(A, B))) stack")


# ---------------------------------------------------------
# 145. Count Digits Recursively
# ---------------------------------------------------------
def count_digits(n):
    n = abs(n)

    if n < 10:
        return 1

    return 1 + count_digits(n // 10)


def program_145():
    n = int(input("Enter an integer: "))

    result = count_digits(n)

    print("Number of digits:", result)
    print("Complexity: O(D) time, O(D) recursion stack")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():

    while True:

        print("\n==========================================")
        print("       DAY 29 - RECURSION PROBLEMS")
        print("==========================================")
        print("141. Reverse a string recursively")
        print("142. Check palindrome recursively")
        print("143. Find Fibonacci number")
        print("144. Find GCD recursively")
        print("145. Count digits recursively")
        print("146. Run All Programs")
        print("147. Exit")
        print("==========================================")

        choice = int(input("Enter your choice: "))

        if choice == 141:
            program_141()

        elif choice == 142:
            program_142()

        elif choice == 143:
            program_143()

        elif choice == 144:
            program_144()

        elif choice == 145:
            program_145()

        elif choice == 146:
            print("\nRunning all Day 29 programs...\n")

            program_141()
            program_142()
            program_143()
            program_144()
            program_145()

        elif choice == 147:
            print("Exiting Day 29. Keep grinding! 🔥")
            break

        else:
            print("Invalid choice. Please try again.")


# Program starts here
if __name__ == "__main__":
    main()