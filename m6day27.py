# 🔹 DAY 27 - MIXED DSA CHALLENGES


# ==========================================
# 🔹 Utility
# ==========================================

class Utility:

    @staticmethod
    def header(title):

        print("\n" + "=" * 50)

        print(title)

        print("=" * 50)


# ==========================================
# 🔹 Challenge 1 - Two Sum
# ==========================================

def two_sum(numbers, target):

    visited = {}

    for index, number in enumerate(numbers):

        difference = target - number

        if difference in visited:

            return [visited[difference], index]

        visited[number] = index

    return []


# ==========================================
# 🔹 Challenge 2 - Reverse String
# ==========================================

def reverse_string(text):

    return text[::-1]


# ==========================================
# 🔹 Challenge 3 - Valid Parentheses
# ==========================================

def valid_parentheses(expression):

    stack = []

    pairs = {

        ')': '(',
        ']': '[',
        '}': '{'

    }

    for character in expression:

        if character in "([{":

            stack.append(character)

        elif character in ")]}":

            if not stack:

                return False

            if stack.pop() != pairs[character]:

                return False

    return len(stack) == 0


# ==========================================
# 🔹 Challenge 4 - Binary Search
# ==========================================

def binary_search(numbers, target):

    left = 0

    right = len(numbers) - 1

    while left <= right:

        middle = (left + right) // 2

        if numbers[middle] == target:

            return middle

        elif numbers[middle] < target:

            left = middle + 1

        else:

            right = middle - 1

    return -1


# ==========================================
# 🔹 Challenge 5 - Kadane Algorithm
# ==========================================

def maximum_subarray(numbers):

    current = numbers[0]

    maximum = numbers[0]

    for number in numbers[1:]:

        current = max(number, current + number)

        maximum = max(maximum, current)

    return maximum


# ==========================================
# 🔹 Main Program
# ==========================================

while True:

    Utility.header("DAY 27 - MIXED DSA CHALLENGE")

    print("1. Two Sum")

    print("2. Reverse String")

    print("3. Valid Parentheses")

    print("4. Binary Search")

    print("5. Maximum Subarray Sum")

    print("6. Exit")

    choice = input("\nEnter Choice : ")

    # --------------------------------------

    if choice == "1":

        numbers = list(

            map(

                int,

                input(

                    "Enter Numbers : "

                ).split()

            )

        )

        target = int(

            input("Enter Target : ")

        )

        print(

            "Answer :",

            two_sum(numbers, target)

        )

    # --------------------------------------

    elif choice == "2":

        text = input(

            "Enter String : "

        )

        print(

            "Reversed :",

            reverse_string(text)

        )

    # --------------------------------------

    elif choice == "3":

        expression = input(

            "Enter Expression : "

        )

        if valid_parentheses(expression):

            print("Valid")

        else:

            print("Invalid")

    # --------------------------------------

    elif choice == "4":

        numbers = list(

            map(

                int,

                input(

                    "Enter Sorted Numbers : "

                ).split()

            )

        )

        target = int(

            input(

                "Enter Target : "

            )

        )

        result = binary_search(

            numbers,

            target

        )

        if result == -1:

            print("Element Not Found")

        else:

            print(

                "Found At Index",

                result

            )

    # --------------------------------------

    elif choice == "5":

        numbers = list(

            map(

                int,

                input(

                    "Enter Numbers : "

                ).split()

            )

        )

        print(

            "Maximum Sum :",

            maximum_subarray(numbers)

        )

    # --------------------------------------

    elif choice == "6":

        print("\nGoodbye 👋")

        break

    # --------------------------------------

    else:

        print("\nInvalid Choice")