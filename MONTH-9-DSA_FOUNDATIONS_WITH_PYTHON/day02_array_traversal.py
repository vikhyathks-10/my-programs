# DAY 2 — Array Traversal and In-Place Operations
# Programs 6–10


# --------------------------------------------------
# 6. Find Largest Element
# --------------------------------------------------

def find_largest():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    largest = arr[0]

    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]

    print("Largest element:", largest)
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# --------------------------------------------------
# 7. Find Smallest Element
# --------------------------------------------------

def find_smallest():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    smallest = arr[0]

    for i in range(1, n):
        if arr[i] < smallest:
            smallest = arr[i]

    print("Smallest element:", smallest)
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# --------------------------------------------------
# 8. Find Second Largest Element
# --------------------------------------------------

def second_largest():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    if n < 2:
        print("Second largest element does not exist.")
        return

    largest = float("-inf")
    second = float("-inf")

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    if second == float("-inf"):
        print("Second largest element does not exist.")
    else:
        print("Second largest element:", second)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# --------------------------------------------------
# 9. Reverse an Array — In-Place
# --------------------------------------------------

def reverse_array():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    left = 0
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    print("Reversed array:", arr)
    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# --------------------------------------------------
# 10. Check Whether Array Is Sorted
# --------------------------------------------------

def check_sorted():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    sorted_array = True

    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            sorted_array = False
            break

    if sorted_array:
        print("Array is sorted in ascending order.")
    else:
        print("Array is NOT sorted.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 55)
        print("       DAY 2 — ARRAY TRAVERSAL & IN-PLACE")
        print("=" * 55)

        print("6. Find Largest Element")
        print("7. Find Smallest Element")
        print("8. Find Second Largest Element")
        print("9. Reverse an Array")
        print("10. Check Whether Array Is Sorted")
        print("11. Run All Programs")
        print("12. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "6":
            find_largest()

        elif choice == "7":
            find_smallest()

        elif choice == "8":
            second_largest()

        elif choice == "9":
            reverse_array()

        elif choice == "10":
            check_sorted()

        elif choice == "11":

            print("\n========== PROGRAM 6 ==========")
            find_largest()

            print("\n========== PROGRAM 7 ==========")
            find_smallest()

            print("\n========== PROGRAM 8 ==========")
            second_largest()

            print("\n========== PROGRAM 9 ==========")
            reverse_array()

            print("\n========== PROGRAM 10 ==========")
            check_sorted()

        elif choice == "12":
            print("\nDay 2 completed! 🚀")
            break

        else:
            print("Invalid choice. Please try again.")


main()