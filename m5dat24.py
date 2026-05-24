# 🔹 DAY 24 - PATTERN PROBLEMS


# 🔹 1. Pyramid Pattern

def pyramid(n):

    print("\n--- Pyramid Pattern ---")

    for i in range(1, n + 1):

        spaces = " " * (n - i)

        stars = "* " * i

        print(spaces + stars)


# 🔹 2. Diamond Pattern

def diamond(n):

    print("\n--- Diamond Pattern ---")

    # Upper part
    for i in range(1, n + 1):

        spaces = " " * (n - i)

        stars = "* " * i

        print(spaces + stars)

    # Lower part
    for i in range(n - 1, 0, -1):

        spaces = " " * (n - i)

        stars = "* " * i

        print(spaces + stars)


# 🔹 3. Number Triangle

def number_triangle(n):

    print("\n--- Number Triangle ---")

    for i in range(1, n + 1):

        for j in range(1, i + 1):

            print(j, end=" ")

        print()


# 🔹 4. Pascal Triangle

def pascal_triangle(n):

    print("\n--- Pascal Triangle ---")

    for i in range(n):

        num = 1

        print(" " * (n - i), end="")

        for j in range(i + 1):

            print(num, end=" ")

            num = num * (i - j) // (j + 1)

        print()


# 🔹 5. Hollow Square

def hollow_square(n):

    print("\n--- Hollow Square ---")

    for i in range(n):

        for j in range(n):

            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()


# 🔹 MAIN PROGRAM

n = 5

pyramid(n)

diamond(n)

number_triangle(n)

pascal_triangle(n)

hollow_square(n)