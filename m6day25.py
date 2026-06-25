# 🔹 DAY 25 - CODE OPTIMIZATION PRACTICE

# ==========================================
# 🔹 1. Improve Time Complexity
# ==========================================

def improve_time_complexity():

    numbers = [10, 20, 30, 40, 50, 60]

    target = 40

    number_set = set(numbers)

    if target in number_set:
        print("\n✅ Element Found")
    else:
        print("\n❌ Element Not Found")


# ==========================================
# 🔹 2. Improve Space Complexity
# ==========================================

def improve_space_complexity():

    print("\nSquares (Generated One By One):")

    for number in range(1, 11):

        square = number * number

        print(square, end=" ")

    print()


# ==========================================
# 🔹 3. Replace Brute Force Solution
# ==========================================

def replace_brute_force():

    numbers = [2, 7, 11, 15]

    target = 9

    visited = {}

    for index, value in enumerate(numbers):

        difference = target - value

        if difference in visited:

            print("\nPair Found:")

            print(
                difference,
                value
            )

            return

        visited[value] = index

    print("\nNo Pair Found")


# ==========================================
# 🔹 4. Optimize String Operations
# ==========================================

def optimize_string_operations():

    words = [
        "Python",
        "is",
        "awesome"
    ]

    sentence = " ".join(words)

    print("\nOptimized String:")

    print(sentence)


# ==========================================
# 🔹 5. Optimize Array Operations
# ==========================================

def optimize_array_operations():

    numbers = [
        5, 2, 8, 1, 3
    ]

    sorted_numbers = sorted(numbers)

    print("\nSorted Array:")

    print(sorted_numbers)


# ==========================================
# 🔹 MAIN PROGRAM
# ==========================================

while True:

    print("\n========== DAY 25 ==========")

    print("1. Improve Time Complexity")

    print("2. Improve Space Complexity")

    print("3. Replace Brute Force Solution")

    print("4. Optimize String Operations")

    print("5. Optimize Array Operations")

    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        improve_time_complexity()

    elif choice == "2":

        improve_space_complexity()

    elif choice == "3":

        replace_brute_force()

    elif choice == "4":

        optimize_string_operations()

    elif choice == "5":

        optimize_array_operations()

    elif choice == "6":

        print("\nGoodbye 👋")

        break

    else:

        print("\n❌ Invalid Choice")