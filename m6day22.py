# 🔹 DAY 22 - OPTIMIZATION PRACTICE

from collections import Counter


# ==========================================
# 🔹 1. Optimized Palindrome Checker
# ==========================================

def is_palindrome(text):

    left = 0
    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


# ==========================================
# 🔹 2. Optimized Frequency Counter
# ==========================================

def frequency_counter(text):

    return Counter(text)


# ==========================================
# 🔹 3. Optimized Search Program
# ==========================================

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# ==========================================
# 🔹 4. Optimized Sorting Logic
# ==========================================

def optimized_sort(arr):

    return sorted(arr)


# ==========================================
# 🔹 5. Optimized File Reading
# ==========================================

def read_file_line_by_line(filename):

    try:

        with open(filename, "r") as file:

            print("\nFile Contents:\n")

            for line in file:

                print(line.strip())

    except FileNotFoundError:

        print("❌ File Not Found")


# ==========================================
# 🔹 MAIN PROGRAM
# ==========================================

while True:

    print("\n===== DAY 22 OPTIMIZATION PRACTICE =====")

    print("1. Optimized Palindrome Checker")
    print("2. Optimized Frequency Counter")
    print("3. Optimized Search Program")
    print("4. Optimized Sorting Logic")
    print("5. Optimized File Reading")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    # --------------------------------------

    if choice == "1":

        text = input(
            "\nEnter String: "
        )

        if is_palindrome(text):

            print("✅ Palindrome")

        else:

            print("❌ Not Palindrome")

    # --------------------------------------

    elif choice == "2":

        text = input(
            "\nEnter String: "
        )

        freq = frequency_counter(text)

        print("\nCharacter Frequency:")

        for key, value in freq.items():

            print(
                f"{key} : {value}"
            )

    # --------------------------------------

    elif choice == "3":

        arr = list(
            map(
                int,
                input(
                    "\nEnter Sorted Numbers: "
                ).split()
            )
        )

        target = int(
            input(
                "Enter Target: "
            )
        )

        result = binary_search(
            arr,
            target
        )

        if result != -1:

            print(
                f"✅ Found at Index {result}"
            )

        else:

            print(
                "❌ Element Not Found"
            )

    # --------------------------------------

    elif choice == "4":

        arr = list(
            map(
                int,
                input(
                    "\nEnter Numbers: "
                ).split()
            )
        )

        print(
            "\nSorted Array:"
        )

        print(
            optimized_sort(arr)
        )

    # --------------------------------------

    elif choice == "5":

        filename = input(
            "\nEnter File Name: "
        )

        read_file_line_by_line(
            filename
        )

    # --------------------------------------

    elif choice == "6":

        print("\nGoodbye 👋")

        break

    # --------------------------------------

    else:

        print(
            "\n❌ Invalid Choice"
        )