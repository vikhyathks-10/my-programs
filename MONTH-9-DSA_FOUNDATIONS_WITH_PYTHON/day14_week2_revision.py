# ============================================================
# DAY 14 — WEEK 2 REVISION
# Programs 66–70
# ============================================================


# ------------------------------------------------------------
# 66. Find Longest Palindromic Substring
# ------------------------------------------------------------

def longest_palindrome():

    text = input("Enter a string: ")

    if text == "":
        print("String is empty.")
        return

    longest = ""

    # Expand around every possible center
    for i in range(len(text)):

        # Odd-length palindrome
        left = i
        right = i

        while left >= 0 and right < len(text):
            if text[left] != text[right]:
                break

            if right - left + 1 > len(longest):
                longest = text[left:right + 1]

            left -= 1
            right += 1

        # Even-length palindrome
        left = i
        right = i + 1

        while left >= 0 and right < len(text):
            if text[left] != text[right]:
                break

            if right - left + 1 > len(longest):
                longest = text[left:right + 1]

            left -= 1
            right += 1

    print("Longest palindromic substring:", longest)
    print("Length:", len(longest))

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# 67. Anagram Grouping — Basic Version
# ------------------------------------------------------------

def anagram_grouping():

    n = int(input("Enter number of strings: "))

    strings = []

    for i in range(n):
        strings.append(input(f"Enter string {i + 1}: "))

    groups = {}

    for word in strings:

        # Create frequency signature
        frequency = [0] * 26

        for char in word:

            if 'a' <= char <= 'z':
                frequency[ord(char) - ord('a')] += 1

            elif 'A' <= char <= 'Z':
                frequency[ord(char) - ord('A')] += 1

        key = tuple(frequency)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    print("\nAnagram groups:")

    group_number = 1

    for group in groups.values():

        print("Group", group_number, ":", group)
        group_number += 1

    print("Time Complexity: O(N × M)")
    print("Space Complexity: O(N × M)")
    print("N = number of strings")
    print("M = average string length")


# ------------------------------------------------------------
# 68. Search Element in Sorted Array
# ------------------------------------------------------------

def search_sorted_array():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:

            print("Element found at index:", mid)

            print("Time Complexity: O(log N)")
            print("Space Complexity: O(1)")
            return

        elif arr[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    print("Element not found.")

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 69. Find Missing Element Using Binary Search
# ------------------------------------------------------------

def missing_using_binary_search():

    n = int(input("Enter N: "))

    print("Enter sorted array containing numbers from 1 to N")
    print("with exactly one number missing.")

    arr = list(map(int, input("Enter array: ").split()))

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) // 2

        # If no number was missing before mid,
        # expected value at index mid is mid + 1.
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1

    # left represents the missing number
    missing = left + 1

    print("Missing element:", missing)

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 70. Search in a Nearly Sorted Array
# ------------------------------------------------------------

def search_nearly_sorted():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter nearly sorted array: ").split()))
    target = int(input("Enter target: "))

    left = 0
    right = n - 1

    while left <= right:

        mid = left + (right - left) // 2

        # Check middle
        if arr[mid] == target:
            print("Element found at index:", mid)

            print("Time Complexity: O(log N)")
            print("Space Complexity: O(1)")
            return

        # Check left neighbor
        if mid - 1 >= left and arr[mid - 1] == target:
            print("Element found at index:", mid - 1)

            print("Time Complexity: O(log N)")
            print("Space Complexity: O(1)")
            return

        # Check right neighbor
        if mid + 1 <= right and arr[mid + 1] == target:
            print("Element found at index:", mid + 1)

            print("Time Complexity: O(log N)")
            print("Space Complexity: O(1)")
            return

        # Decide which half to search
        if arr[mid] > target:
            right = mid - 2

        else:
            left = mid + 2

    print("Element not found.")

    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("             DAY 14 — WEEK 2 REVISION")
        print("=" * 65)

        print("66. Find Longest Palindromic Substring")
        print("67. Anagram Grouping — Basic Version")
        print("68. Search Element in Sorted Array")
        print("69. Find Missing Element Using Binary Search")
        print("70. Search in a Nearly Sorted Array")
        print("71. Run All Programs")
        print("72. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "66":
            longest_palindrome()

        elif choice == "67":
            anagram_grouping()

        elif choice == "68":
            search_sorted_array()

        elif choice == "69":
            missing_using_binary_search()

        elif choice == "70":
            search_nearly_sorted()

        elif choice == "71":

            print("\n========== PROGRAM 66 ==========")
            longest_palindrome()

            print("\n========== PROGRAM 67 ==========")
            anagram_grouping()

            print("\n========== PROGRAM 68 ==========")
            search_sorted_array()

            print("\n========== PROGRAM 69 ==========")
            missing_using_binary_search()

            print("\n========== PROGRAM 70 ==========")
            search_nearly_sorted()

        elif choice == "72":

            print("\n🎉 WEEK 2 COMPLETED!")
            print("70 DSA programs completed!")
            break

        else:
            print("Invalid choice. Please try again.")


main()