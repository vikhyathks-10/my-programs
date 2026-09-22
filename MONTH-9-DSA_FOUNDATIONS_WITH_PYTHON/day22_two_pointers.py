# ============================================================
# DAY 22 — TWO POINTERS
# Programs 106–110
# ============================================================


# ------------------------------------------------------------
# PROGRAM 106 — Two Sum in Sorted Array
# ------------------------------------------------------------

def two_sum_sorted():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))

    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    while left < right:

        current_sum = arr[left] + arr[right]

        if current_sum == target:

            print("Pair found:", arr[left], "+", arr[right], "=", target)
            print("Indices:", left, "and", right)

            print("Time Complexity: O(N)")
            print("Space Complexity: O(1)")
            return

        elif current_sum < target:

            # Need a larger sum
            left += 1

        else:

            # Need a smaller sum
            right -= 1

    print("No pair found.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 107 — Remove Duplicates Using Two Pointers
# ------------------------------------------------------------

def remove_duplicates():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))

    if n == 0:

        print("Array is empty.")
        return

    slow = 0

    for fast in range(1, n):

        if arr[fast] != arr[slow]:

            slow += 1
            arr[slow] = arr[fast]

    new_length = slow + 1

    print("Array after removing duplicates:",
          arr[:new_length])

    print("Number of unique elements:", new_length)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 108 — Move Zeroes Using Two Pointers
# ------------------------------------------------------------

def move_zeroes():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    position = 0

    # Move all non-zero elements forward
    for i in range(n):

        if arr[i] != 0:

            arr[position], arr[i] = arr[i], arr[position]

            position += 1

    print("Array after moving zeroes:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 109 — Reverse String Using Two Pointers
# ------------------------------------------------------------

def reverse_string():

    text = input("Enter string: ")

    # Convert string to list because strings are immutable
    chars = list(text)

    left = 0
    right = len(chars) - 1

    while left < right:

        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    reversed_text = "".join(chars)

    print("Reversed string:", reversed_text)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 110 — Check Palindrome Using Two Pointers
# ------------------------------------------------------------

def check_palindrome():

    text = input("Enter string: ")

    left = 0
    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:

            print("Not a palindrome.")

            print("Time Complexity: O(N)")
            print("Space Complexity: O(1)")
            return

        left += 1
        right -= 1

    print("Palindrome.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("                 DAY 22 — TWO POINTERS")
        print("=" * 65)

        print("106. Two Sum in Sorted Array")
        print("107. Remove Duplicates Using Two Pointers")
        print("108. Move Zeroes Using Two Pointers")
        print("109. Reverse String Using Two Pointers")
        print("110. Check Palindrome Using Two Pointers")
        print("111. Run All Programs")
        print("112. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "106":

            print("\n========== PROGRAM 106 ==========")
            two_sum_sorted()

        elif choice == "107":

            print("\n========== PROGRAM 107 ==========")
            remove_duplicates()

        elif choice == "108":

            print("\n========== PROGRAM 108 ==========")
            move_zeroes()

        elif choice == "109":

            print("\n========== PROGRAM 109 ==========")
            reverse_string()

        elif choice == "110":

            print("\n========== PROGRAM 110 ==========")
            check_palindrome()

        elif choice == "111":

            print("\n========== PROGRAM 106 ==========")
            two_sum_sorted()

            print("\n========== PROGRAM 107 ==========")
            remove_duplicates()

            print("\n========== PROGRAM 108 ==========")
            move_zeroes()

            print("\n========== PROGRAM 109 ==========")
            reverse_string()

            print("\n========== PROGRAM 110 ==========")
            check_palindrome()

        elif choice == "112":

            print("\n🎉 DAY 22 COMPLETED!")
            print("Programs 106–110 completed.")
            print("Total DSA programs completed: 110")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()