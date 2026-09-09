# ============================================================
# DAY 9 — STRING FREQUENCY & CHARACTERS
# Programs 41–45
# ============================================================


# ------------------------------------------------------------
# 41. Character Frequency Counter
# ------------------------------------------------------------

def character_frequency():

    text = input("Enter a string: ")

    frequency = {}

    for char in text:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print("Character frequencies:")

    for char in frequency:
        print(char, ":", frequency[char])

    print("Time Complexity: O(N)")
    print("Space Complexity: O(K)")
    print("K = number of distinct characters")


# ------------------------------------------------------------
# 42. Find First Non-Repeating Character
# ------------------------------------------------------------

def first_non_repeating():

    text = input("Enter a string: ")

    frequency = {}

    # Count frequency of every character
    for char in text:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find first character whose frequency is 1
    found = False

    for char in text:

        if frequency[char] == 1:
            print("First non-repeating character:", char)
            found = True
            break

    if not found:
        print("No non-repeating character found.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# 43. Find First Repeating Character
# ------------------------------------------------------------

def first_repeating():

    text = input("Enter a string: ")

    seen = set()

    found = False

    for char in text:

        if char in seen:
            print("First repeating character:", char)
            found = True
            break

        seen.add(char)

    if not found:
        print("No repeating character found.")

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# 44. Find Most Frequent Character
# ------------------------------------------------------------

def most_frequent():

    text = input("Enter a string: ")

    frequency = {}

    # Count frequency
    for char in text:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    most_char = None
    maximum_frequency = 0

    # Find maximum frequency
    for char in frequency:

        if frequency[char] > maximum_frequency:
            maximum_frequency = frequency[char]
            most_char = char

    if most_char is not None:
        print("Most frequent character:", most_char)
        print("Frequency:", maximum_frequency)
    else:
        print("String is empty.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# 45. Remove Duplicate Characters
# ------------------------------------------------------------

def remove_duplicate_characters():

    text = input("Enter a string: ")

    seen = set()
    result = ""

    for char in text:

        if char not in seen:
            result += char
            seen.add(char)

    print("String after removing duplicates:", result)

    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("        DAY 9 — STRING FREQUENCY & CHARACTERS")
        print("=" * 65)

        print("41. Character Frequency Counter")
        print("42. First Non-Repeating Character")
        print("43. First Repeating Character")
        print("44. Most Frequent Character")
        print("45. Remove Duplicate Characters")
        print("46. Run All Programs")
        print("47. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "41":
            character_frequency()

        elif choice == "42":
            first_non_repeating()

        elif choice == "43":
            first_repeating()

        elif choice == "44":
            most_frequent()

        elif choice == "45":
            remove_duplicate_characters()

        elif choice == "46":

            print("\n========== PROGRAM 41 ==========")
            character_frequency()

            print("\n========== PROGRAM 42 ==========")
            first_non_repeating()

            print("\n========== PROGRAM 43 ==========")
            first_repeating()

            print("\n========== PROGRAM 44 ==========")
            most_frequent()

            print("\n========== PROGRAM 45 ==========")
            remove_duplicate_characters()

        elif choice == "47":
            print("\nDay 9 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()