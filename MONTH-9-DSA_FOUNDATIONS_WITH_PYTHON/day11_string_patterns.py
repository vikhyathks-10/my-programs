# ============================================================
# DAY 11 — STRING PATTERNS
# Programs 51–55
# ============================================================


# ------------------------------------------------------------
# 51. Longest Common Prefix
# ------------------------------------------------------------

def longest_common_prefix():

    n = int(input("Enter number of strings: "))

    if n <= 0:
        print("No strings provided.")
        return

    strings = []

    for i in range(n):
        strings.append(input(f"Enter string {i + 1}: "))

    prefix = strings[0]

    for i in range(1, n):

        current = strings[i]
        j = 0

        while j < len(prefix) and j < len(current):
            if prefix[j] != current[j]:
                break
            j += 1

        prefix = prefix[:j]

        if prefix == "":
            break

    print("Longest common prefix:", prefix)

    print("Time Complexity: O(N × M)")
    print("Space Complexity: O(M)")
    print("N = number of strings")
    print("M = length of the shortest string")


# ------------------------------------------------------------
# 52. Check Balanced Parentheses
# ------------------------------------------------------------

def balanced_parentheses():

    expression = input("Enter expression: ")

    stack = []
    balanced = True

    for char in expression:

        if char == '(' or char == '[' or char == '{':
            stack.append(char)

        elif char == ')' or char == ']' or char == '}':

            if len(stack) == 0:
                balanced = False
                break

            top = stack.pop()

            if char == ')' and top != '(':
                balanced = False
                break

            if char == ']' and top != '[':
                balanced = False
                break

            if char == '}' and top != '{':
                balanced = False
                break

    if len(stack) != 0:
        balanced = False

    if balanced:
        print("Parentheses are balanced.")
    else:
        print("Parentheses are NOT balanced.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# 53. Count Substrings of a String
# ------------------------------------------------------------

def count_substrings():

    text = input("Enter a string: ")

    n = len(text)

    # Number of non-empty substrings
    count = n * (n + 1) // 2

    print("Number of non-empty substrings:", count)

    print("Time Complexity: O(1)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 54. Find All Occurrences of a Pattern
# ------------------------------------------------------------

def find_all_occurrences():

    text = input("Enter the main string: ")
    pattern = input("Enter the pattern: ")

    positions = []

    if pattern == "":
        print("Pattern cannot be empty.")
        return

    n = len(text)
    m = len(pattern)

    # Check every possible starting position
    for i in range(n - m + 1):

        match = True

        for j in range(m):

            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            positions.append(i)

    if len(positions) == 0:
        print("Pattern not found.")
    else:
        print("Pattern found at indices:", positions)

    print("Time Complexity: O(N × M)")
    print("Space Complexity: O(K)")
    print("N = length of text")
    print("M = length of pattern")
    print("K = number of occurrences")


# ------------------------------------------------------------
# 55. Basic String Compression
# ------------------------------------------------------------

def string_compression():

    text = input("Enter a string: ")

    if text == "":
        print("String is empty.")
        return

    compressed = ""

    count = 1

    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            count += 1

        else:
            compressed += text[i - 1] + str(count)
            count = 1

    # Add the final group
    compressed += text[-1] + str(count)

    print("Compressed string:", compressed)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("              DAY 11 — STRING PATTERNS")
        print("=" * 65)

        print("51. Longest Common Prefix")
        print("52. Check Balanced Parentheses")
        print("53. Count Substrings of a String")
        print("54. Find All Occurrences of a Pattern")
        print("55. Basic String Compression")
        print("56. Run All Programs")
        print("57. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "51":
            longest_common_prefix()

        elif choice == "52":
            balanced_parentheses()

        elif choice == "53":
            count_substrings()

        elif choice == "54":
            find_all_occurrences()

        elif choice == "55":
            string_compression()

        elif choice == "56":

            print("\n========== PROGRAM 51 ==========")
            longest_common_prefix()

            print("\n========== PROGRAM 52 ==========")
            balanced_parentheses()

            print("\n========== PROGRAM 53 ==========")
            count_substrings()

            print("\n========== PROGRAM 54 ==========")
            find_all_occurrences()

            print("\n========== PROGRAM 55 ==========")
            string_compression()

        elif choice == "57":
            print("\nDay 11 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()