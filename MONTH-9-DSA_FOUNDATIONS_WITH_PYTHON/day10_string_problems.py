# ============================================================
# DAY 10 — STRING PROBLEMS
# Programs 46–50
# ============================================================


# ------------------------------------------------------------
# 46. Check Whether Two Strings Are Anagrams
# ------------------------------------------------------------

def check_anagram():

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    if len(str1) != len(str2):
        print("The strings are not anagrams.")
        print("Time Complexity: O(N)")
        print("Space Complexity: O(K)")
        return

    frequency = {}

    # Count characters in first string
    for char in str1:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Remove characters using second string
    for char in str2:

        if char not in frequency:
            print("The strings are not anagrams.")
            print("Time Complexity: O(N)")
            print("Space Complexity: O(K)")
            return

        frequency[char] -= 1

        if frequency[char] < 0:
            print("The strings are not anagrams.")
            print("Time Complexity: O(N)")
            print("Space Complexity: O(K)")
            return

    print("The strings are anagrams.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# 47. Check Whether One String Is a Rotation of Another
# ------------------------------------------------------------

def check_rotation():

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    if len(str1) != len(str2):
        print("The strings are not rotations.")
        print("Time Complexity: O(N)")
        print("Space Complexity: O(N)")
        return

    combined = str1 + str1

    if str2 in combined:
        print("The second string is a rotation of the first.")
    else:
        print("The second string is NOT a rotation of the first.")

    print("Time Complexity: O(N) average/practical")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# 48. Find Common Characters Between Two Strings
# ------------------------------------------------------------

def common_characters():

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    seen = set()
    result = ""

    # Store characters from first string
    for char in str1:
        seen.add(char)

    # Find common characters
    for char in str2:

        if char in seen:
            if char not in result:
                result += char

    if result:
        print("Common characters:", result)
    else:
        print("No common characters.")

    print("Average Time Complexity: O(N + M)")
    print("Space Complexity: O(K)")


# ------------------------------------------------------------
# 49. Find Longest Word in a Sentence
# ------------------------------------------------------------

def longest_word():

    sentence = input("Enter a sentence: ")

    longest = ""
    current = ""

    for char in sentence:

        if char != ' ':
            current += char

        else:
            if len(current) > len(longest):
                longest = current

            current = ""

    # Check the last word
    if len(current) > len(longest):
        longest = current

    print("Longest word:", longest)
    print("Length:", len(longest))

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# 50. Reverse Words in a Sentence
# ------------------------------------------------------------

def reverse_words():

    sentence = input("Enter a sentence: ")

    words = []
    current = ""

    # Extract words manually
    for char in sentence:

        if char != ' ':
            current += char

        else:
            if current != "":
                words.append(current)
                current = ""

    # Add final word
    if current != "":
        words.append(current)

    # Print words in reverse order
    print("Reversed sentence:", end=" ")

    for i in range(len(words) - 1, -1, -1):
        print(words[i], end=" ")

    print()

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("             DAY 10 — STRING PROBLEMS")
        print("=" * 65)

        print("46. Check Whether Two Strings Are Anagrams")
        print("47. Check Whether One String Is a Rotation of Another")
        print("48. Find Common Characters Between Two Strings")
        print("49. Find Longest Word in a Sentence")
        print("50. Reverse Words in a Sentence")
        print("51. Run All Programs")
        print("52. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "46":
            check_anagram()

        elif choice == "47":
            check_rotation()

        elif choice == "48":
            common_characters()

        elif choice == "49":
            longest_word()

        elif choice == "50":
            reverse_words()

        elif choice == "51":

            print("\n========== PROGRAM 46 ==========")
            check_anagram()

            print("\n========== PROGRAM 47 ==========")
            check_rotation()

            print("\n========== PROGRAM 48 ==========")
            common_characters()

            print("\n========== PROGRAM 49 ==========")
            longest_word()

            print("\n========== PROGRAM 50 ==========")
            reverse_words()

        elif choice == "52":
            print("\nDay 10 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()