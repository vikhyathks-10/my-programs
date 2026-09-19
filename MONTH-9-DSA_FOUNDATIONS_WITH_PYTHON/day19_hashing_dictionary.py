# ============================================================
# DAY 19 — HASHING WITH DICTIONARY
# Programs 91–95
# ============================================================


# ------------------------------------------------------------
# PROGRAM 91 — Frequency Counter Using Dictionary
# ------------------------------------------------------------

def frequency_counter():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    frequency = {}

    for value in arr:

        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    print("\nFrequency of elements:")

    for value, count in frequency.items():
        print(value, "->", count)

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# PROGRAM 92 — Find Duplicate Elements
# ------------------------------------------------------------

def find_duplicates():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    frequency = {}

    for value in arr:

        frequency[value] = frequency.get(value, 0) + 1

    duplicates = []

    for value, count in frequency.items():

        if count > 1:
            duplicates.append(value)

    if len(duplicates) == 0:
        print("No duplicate elements found.")
    else:
        print("Duplicate elements:", duplicates)

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# PROGRAM 93 — Find First Unique Element
# ------------------------------------------------------------

def first_unique():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    frequency = {}

    # Count frequency
    for value in arr:
        frequency[value] = frequency.get(value, 0) + 1

    # Find first element with frequency 1
    for value in arr:

        if frequency[value] == 1:

            print("First unique element:", value)

            print("Average Time Complexity: O(N)")
            print("Space Complexity: O(K)")
            return

    print("No unique element found.")

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# PROGRAM 94 — Two Sum Using Dictionary
# ------------------------------------------------------------

def two_sum_dictionary():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    target = int(input("Enter target: "))

    seen = {}

    for i in range(n):

        current = arr[i]

        required = target - current

        if required in seen:

            print("Pair found:")
            print("Indices:", seen[required], "and", i)
            print("Values:", required, "and", current)

            print("Average Time Complexity: O(N)")
            print("Space Complexity: O(N)")
            return

        seen[current] = i

    print("No pair found.")

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 95 — Elements Occurring More Than Once
# ------------------------------------------------------------

def occurring_more_than_once():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    frequency = {}

    for value in arr:

        frequency[value] = frequency.get(value, 0) + 1

    print("\nElements occurring more than once:")

    found = False

    for value, count in frequency.items():

        if count > 1:

            print(value, "->", count, "times")
            found = True

    if not found:
        print("No element occurs more than once.")

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("             DAY 19 — HASHING WITH DICTIONARY")
        print("=" * 65)

        print("91. Frequency Counter Using Dictionary")
        print("92. Find Duplicate Elements")
        print("93. Find First Unique Element")
        print("94. Two Sum Using Dictionary")
        print("95. Find Elements Occurring More Than Once")
        print("96. Run All Programs")
        print("97. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "91":

            print("\n========== PROGRAM 91 ==========")
            frequency_counter()

        elif choice == "92":

            print("\n========== PROGRAM 92 ==========")
            find_duplicates()

        elif choice == "93":

            print("\n========== PROGRAM 93 ==========")
            first_unique()

        elif choice == "94":

            print("\n========== PROGRAM 94 ==========")
            two_sum_dictionary()

        elif choice == "95":

            print("\n========== PROGRAM 95 ==========")
            occurring_more_than_once()

        elif choice == "96":

            print("\n========== PROGRAM 91 ==========")
            frequency_counter()

            print("\n========== PROGRAM 92 ==========")
            find_duplicates()

            print("\n========== PROGRAM 93 ==========")
            first_unique()

            print("\n========== PROGRAM 94 ==========")
            two_sum_dictionary()

            print("\n========== PROGRAM 95 ==========")
            occurring_more_than_once()

        elif choice == "97":

            print("\n🎉 DAY 19 COMPLETED!")
            print("Programs 91–95 completed.")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()