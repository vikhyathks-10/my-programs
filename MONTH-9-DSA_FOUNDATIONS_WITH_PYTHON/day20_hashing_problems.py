# ============================================================
# DAY 20 — HASHING PROBLEMS
# Programs 96–100
# ============================================================


# ------------------------------------------------------------
# PROGRAM 96 — Group Anagrams
# ------------------------------------------------------------

def group_anagrams():

    n = int(input("Enter number of strings: "))

    words = []

    for i in range(n):
        word = input(f"Enter string {i + 1}: ")
        words.append(word)

    groups = {}

    for word in words:

        # Frequency signature for 26 lowercase letters
        frequency = [0] * 26

        for char in word.lower():

            if 'a' <= char <= 'z':
                frequency[ord(char) - ord('a')] += 1

        key = tuple(frequency)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    print("\nAnagram Groups:")

    group_number = 1

    for group in groups.values():

        print("Group", group_number, ":", group)

        group_number += 1

    print("Average Time Complexity: O(N × M)")
    print("Space Complexity: O(N × M)")


# ------------------------------------------------------------
# PROGRAM 97 — Find Common Elements in Three Arrays
# ------------------------------------------------------------

def common_three_arrays():

    n = int(input("Enter size of first array: "))
    arr1 = list(map(int, input("Enter first sorted array: ").split()))

    m = int(input("Enter size of second array: "))
    arr2 = list(map(int, input("Enter second sorted array: ").split()))

    k = int(input("Enter size of third array: "))
    arr3 = list(map(int, input("Enter third sorted array: ").split()))

    # Store elements of first array
    set1 = set(arr1)

    # Store elements of second array
    set2 = set(arr2)

    # Elements common to first and second
    common = set1 & set2

    # Elements common to all three
    result = common & set(arr3)

    result = list(result)

    result.sort()

    if len(result) == 0:
        print("No common elements found.")
    else:
        print("Common elements:", result)

    print("Average Time Complexity: O(N + M + K)")
    print("Space Complexity: O(N + M)")


# ------------------------------------------------------------
# PROGRAM 98 — Find Longest Consecutive Sequence
# ------------------------------------------------------------

def longest_consecutive_sequence():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    numbers = set(arr)

    longest = 0

    for number in numbers:

        # Start only if number is the beginning
        # of a consecutive sequence
        if number - 1 not in numbers:

            current = number
            length = 1

            while current + 1 in numbers:

                current += 1
                length += 1

            if length > longest:
                longest = length

    print("Longest consecutive sequence length:", longest)

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 99 — Find Pair With Given Difference
# ------------------------------------------------------------

def pair_with_difference():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    difference = int(input("Enter difference: "))

    numbers = set(arr)

    found = False

    for value in arr:

        # Case:
        # larger - smaller = difference
        if value + difference in numbers:

            print("Pair found:", value, "and", value + difference)

            found = True
            break

    if not found:

        print("No pair with the given difference found.")

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 100 — Find Subarray With Sum Zero
# ------------------------------------------------------------

def zero_sum_subarray():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    prefix_sum = 0

    # Store prefix sums already seen
    seen = {0}

    for value in arr:

        prefix_sum += value

        # If prefix sum appears again,
        # the elements between those positions
        # have sum zero.
        if prefix_sum in seen:

            print("A subarray with sum zero exists.")

            print("Time Complexity: O(N)")
            print("Space Complexity: O(N)")
            return

        seen.add(prefix_sum)

    print("No subarray with sum zero exists.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("               DAY 20 — HASHING PROBLEMS")
        print("=" * 65)

        print("96. Group Anagrams")
        print("97. Find Common Elements in Three Arrays")
        print("98. Find Longest Consecutive Sequence")
        print("99. Find Pair With Given Difference")
        print("100. Find Subarray With Sum Zero")
        print("101. Run All Programs")
        print("102. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "96":

            print("\n========== PROGRAM 96 ==========")
            group_anagrams()

        elif choice == "97":

            print("\n========== PROGRAM 97 ==========")
            common_three_arrays()

        elif choice == "98":

            print("\n========== PROGRAM 98 ==========")
            longest_consecutive_sequence()

        elif choice == "99":

            print("\n========== PROGRAM 99 ==========")
            pair_with_difference()

        elif choice == "100":

            print("\n========== PROGRAM 100 ==========")
            zero_sum_subarray()

        elif choice == "101":

            print("\n========== PROGRAM 96 ==========")
            group_anagrams()

            print("\n========== PROGRAM 97 ==========")
            common_three_arrays()

            print("\n========== PROGRAM 98 ==========")
            longest_consecutive_sequence()

            print("\n========== PROGRAM 99 ==========")
            pair_with_difference()

            print("\n========== PROGRAM 100 ==========")
            zero_sum_subarray()

        elif choice == "102":

            print("\n🎉 DAY 20 COMPLETED!")
            print("Programs 96–100 completed.")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()