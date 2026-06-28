# 🔹 DAY 28 - INTERVIEW CODING CHALLENGE


# ==========================================
# 🔹 Utility Class
# ==========================================

class Utility:

    @staticmethod
    def header(title):

        print("\n" + "=" * 50)

        print(title)

        print("=" * 50)


# ==========================================
# 🔹 Interview Question 1
# Palindrome Number
# ==========================================

def palindrome_number(number):

    original = str(number)

    return original == original[::-1]


# ==========================================
# 🔹 Interview Question 2
# Valid Anagram
# ==========================================

def valid_anagram(first, second):

    return sorted(first) == sorted(second)


# ==========================================
# 🔹 Interview Question 3
# Merge Two Sorted Arrays
# ==========================================

def merge_sorted_arrays(first, second):

    merged = []

    i = 0
    j = 0

    while i < len(first) and j < len(second):

        if first[i] < second[j]:

            merged.append(first[i])
            i += 1

        else:

            merged.append(second[j])
            j += 1

    while i < len(first):

        merged.append(first[i])
        i += 1

    while j < len(second):

        merged.append(second[j])
        j += 1

    return merged


# ==========================================
# 🔹 Interview Question 4
# First Non-Repeating Character
# ==========================================

def first_non_repeating(text):

    frequency = {}

    for character in text:

        frequency[character] = frequency.get(character, 0) + 1

    for character in text:

        if frequency[character] == 1:

            return character

    return None


# ==========================================
# 🔹 Interview Question 5
# Fibonacci Series
# ==========================================

def fibonacci(number):

    series = []

    first = 0
    second = 1

    for _ in range(number):

        series.append(first)

        first, second = second, first + second

    return series


# ==========================================
# 🔹 Main Program
# ==========================================

while True:

    Utility.header("DAY 28 - INTERVIEW QUESTIONS")

    print("1. Palindrome Number")

    print("2. Valid Anagram")

    print("3. Merge Two Sorted Arrays")

    print("4. First Non-Repeating Character")

    print("5. Fibonacci Series")

    print("6. Exit")

    choice = input("\nEnter Choice : ")

    # ------------------------------------

    if choice == "1":

        number = int(

            input("Enter Number : ")

        )

        if palindrome_number(number):

            print("Palindrome")

        else:

            print("Not Palindrome")

    # ------------------------------------

    elif choice == "2":

        first = input(

            "First String : "

        )

        second = input(

            "Second String : "

        )

        if valid_anagram(first, second):

            print("Valid Anagram")

        else:

            print("Not Anagram")

    # ------------------------------------

    elif choice == "3":

        first = list(

            map(

                int,

                input(

                    "First Sorted Array : "

                ).split()

            )

        )

        second = list(

            map(

                int,

                input(

                    "Second Sorted Array : "

                ).split()

            )

        )

        print(

            "Merged Array :",

            merge_sorted_arrays(

                first,

                second

            )

        )

    # ------------------------------------

    elif choice == "4":

        text = input(

            "Enter String : "

        )

        answer = first_non_repeating(text)

        if answer:

            print(

                "First Non-Repeating Character :",

                answer

            )

        else:

            print(

                "No Unique Character"

            )

    # ------------------------------------

    elif choice == "5":

        number = int(

            input(

                "How Many Terms : "

            )

        )

        print(

            fibonacci(number)

        )

    # ------------------------------------

    elif choice == "6":

        print("\nGoodbye 👋")

        break

    # ------------------------------------

    else:

        print("\nInvalid Choice")