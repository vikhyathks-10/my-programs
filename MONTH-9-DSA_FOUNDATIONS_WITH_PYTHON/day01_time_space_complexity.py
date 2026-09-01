# DAY 1 — Time & Space Complexity
# Programs 1–5

def sum_of_n_numbers():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter numbers: ").split()))

    total = 0

    for num in arr:
        total += num

    print("Sum:", total)
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


def find_maximum():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter numbers: ").split()))

    maximum = arr[0]

    for i in range(1, n):
        if arr[i] > maximum:
            maximum = arr[i]

    print("Maximum element:", maximum)
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


def count_frequency():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter numbers: ").split()))
    x = int(input("Enter element to count: "))

    count = 0

    for num in arr:
        if num == x:
            count += 1

    print("Frequency of", x, ":", count)
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


def compare_nested_loops():
    n = int(input("Enter N: "))

    print("\nLoop 1:")
    for i in range(n):
        print(i, end=" ")

    print("\nTime Complexity: O(N)")
    print("Space Complexity: O(1)")

    print("\n\nLoop 2:")
    for i in range(n):
        for j in range(n):
            pass

    print("Nested loop executed.")
    print("Time Complexity: O(N²)")
    print("Space Complexity: O(1)")

    print("\nLoop 3:")
    for i in range(n):
        for j in range(5):
            pass

    print("Nested loop with constant inner loop executed.")
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")

    print("\nLoop 4:")
    i = 1

    while i < n:
        i *= 2

    print("Repeatedly doubled until N.")
    print("Time Complexity: O(log N)")
    print("Space Complexity: O(1)")


def find_duplicates():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter numbers: ").split()))

    # Approach 1: Brute Force
    brute_duplicates = set()

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                brute_duplicates.add(arr[i])

    print("\nBrute Force Approach:")
    print("Duplicates:", brute_duplicates)
    print("Time Complexity: O(N²)")
    print("Space Complexity: O(N)")

    # Approach 2: Using Set
    seen = set()
    efficient_duplicates = set()

    for num in arr:
        if num in seen:
            efficient_duplicates.add(num)
        else:
            seen.add(num)

    print("\nSet Approach:")
    print("Duplicates:", efficient_duplicates)
    print("Average Time Complexity: O(N)")
    print("Space Complexity: O(N)")


def main():
    while True:
        print("\n" + "=" * 50)
        print("       DAY 1 — TIME & SPACE COMPLEXITY")
        print("=" * 50)

        print("1. Find Sum of N Numbers")
        print("2. Find Maximum Element")
        print("3. Count Frequency of an Element")
        print("4. Compare Loop Complexities")
        print("5. Find Duplicate Elements")
        print("6. Run All Programs")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            sum_of_n_numbers()

        elif choice == "2":
            find_maximum()

        elif choice == "3":
            count_frequency()

        elif choice == "4":
            compare_nested_loops()

        elif choice == "5":
            find_duplicates()

        elif choice == "6":
            print("\n--- PROGRAM 1 ---")
            sum_of_n_numbers()

            print("\n--- PROGRAM 2 ---")
            find_maximum()

            print("\n--- PROGRAM 3 ---")
            count_frequency()

            print("\n--- PROGRAM 4 ---")
            compare_nested_loops()

            print("\n--- PROGRAM 5 ---")
            find_duplicates()

        elif choice == "7":
            print("Day 1 completed! 🚀")
            break

        else:
            print("Invalid choice. Try again.")


main()