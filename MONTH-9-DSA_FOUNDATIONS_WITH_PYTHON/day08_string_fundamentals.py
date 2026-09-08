# ============================================================
# DAY 8 — STRING FUNDAMENTALS
# Programs 36–40
# ============================================================


# ------------------------------------------------------------
# 36. Reverse a String
# ------------------------------------------------------------

def reverse_string():

    text = input("Enter a string: ")

    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    print("Reversed string:", reversed_text)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# 37. Check Palindrome
# ------------------------------------------------------------

def check_palindrome():

    text = input("Enter a string: ")

    left = 0
    right = len(text) - 1

    palindrome = True

    while left < right:

        if text[left] != text[right]:
            palindrome = False
            break

        left += 1
        right -= 1

    if palindrome:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 38. Count Vowels and Consonants
# ------------------------------------------------------------

def count_vowels_consonants():

    text = input("Enter a string: ")

    vowels = 0
    consonants = 0

    for char in text:

        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):

            if (char == 'a' or char == 'e' or char == 'i' or
                char == 'o' or char == 'u' or
                char == 'A' or char == 'E' or char == 'I' or
                char == 'O' or char == 'U'):

                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 39. Count Uppercase and Lowercase Characters
# ------------------------------------------------------------

def count_upper_lower():

    text = input("Enter a string: ")

    uppercase = 0
    lowercase = 0

    for char in text:

        if 'A' <= char <= 'Z':
            uppercase += 1

        elif 'a' <= char <= 'z':
            lowercase += 1

    print("Uppercase characters:", uppercase)
    print("Lowercase characters:", lowercase)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 40. Remove Spaces from a String
# ------------------------------------------------------------

def remove_spaces():

    text = input("Enter a string: ")

    result = ""

    for char in text:

        if char != ' ':
            result += char

    print("String without spaces:", result)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 60)
        print("             DAY 8 — STRING FUNDAMENTALS")
        print("=" * 60)

        print("36. Reverse a String")
        print("37. Check Palindrome")
        print("38. Count Vowels and Consonants")
        print("39. Count Uppercase/Lowercase Characters")
        print("40. Remove Spaces from a String")
        print("41. Run All Programs")
        print("42. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "36":
            reverse_string()

        elif choice == "37":
            check_palindrome()

        elif choice == "38":
            count_vowels_consonants()

        elif choice == "39":
            count_upper_lower()

        elif choice == "40":
            remove_spaces()

        elif choice == "41":

            print("\n========== PROGRAM 36 ==========")
            reverse_string()

            print("\n========== PROGRAM 37 ==========")
            check_palindrome()

            print("\n========== PROGRAM 38 ==========")
            count_vowels_consonants()

            print("\n========== PROGRAM 39 ==========")
            count_upper_lower()

            print("\n========== PROGRAM 40 ==========")
            remove_spaces()

        elif choice == "42":
            print("\nDay 8 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()