# ============================================================
# DAY 16 — INSERTION SORT
# Programs 76–80
# ============================================================


# ------------------------------------------------------------
# PROGRAM 76 — Insertion Sort
# ------------------------------------------------------------

def insertion_sort():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    for i in range(1, n):

        key = arr[i]
        j = i - 1

        # Shift elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    print("Sorted array:", arr)

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 77 — Descending Insertion Sort
# ------------------------------------------------------------

def descending_insertion_sort():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    for i in range(1, n):

        key = arr[i]
        j = i - 1

        # Shift smaller elements to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    print("Array in descending order:", arr)

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 78 — Sort Nearly Sorted Array
# ------------------------------------------------------------

def sort_nearly_sorted():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    k = int(input("Enter K (maximum displacement): "))

    # Insertion-sort logic
    for i in range(1, n):

        key = arr[i]

        # Since the array is nearly sorted,
        # search only up to K positions backward.
        j = i - 1
        limit = max(0, i - k)

        while j >= limit and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    print("Sorted array:", arr)

    print("Time Complexity: O(N × K)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 79 — Insert an Element into a Sorted Array
# ------------------------------------------------------------

def insert_into_sorted_array():
    n = int(input("Enter N: "))

    arr = list(map(int, input("Enter sorted array: ").split()))

    element = int(input("Enter element to insert: "))

    # Add extra space for the new element
    arr.append(0)

    j = n - 1

    # Shift elements greater than the new element
    while j >= 0 and arr[j] > element:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = element

    print("Array after insertion:", arr)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 80 — Sort Array Using Insertion-Sort Logic
# ------------------------------------------------------------

def insertion_logic_sort():
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    # Build sorted portion one element at a time
    for current in range(1, n):

        value = arr[current]
        position = current

        while position > 0:

            if arr[position - 1] > value:
                arr[position] = arr[position - 1]
                position -= 1
            else:
                break

        arr[position] = value

    print("Sorted array:", arr)

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("                DAY 16 — INSERTION SORT")
        print("=" * 65)

        print("76. Insertion Sort")
        print("77. Descending Insertion Sort")
        print("78. Sort Nearly Sorted Array")
        print("79. Insert an Element into a Sorted Array")
        print("80. Sort an Array Using Insertion-Sort Logic")
        print("81. Run All Programs")
        print("82. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "76":

            print("\n========== PROGRAM 76 ==========")
            insertion_sort()

        elif choice == "77":

            print("\n========== PROGRAM 77 ==========")
            descending_insertion_sort()

        elif choice == "78":

            print("\n========== PROGRAM 78 ==========")
            sort_nearly_sorted()

        elif choice == "79":

            print("\n========== PROGRAM 79 ==========")
            insert_into_sorted_array()

        elif choice == "80":

            print("\n========== PROGRAM 80 ==========")
            insertion_logic_sort()

        elif choice == "81":

            print("\n========== PROGRAM 76 ==========")
            insertion_sort()

            print("\n========== PROGRAM 77 ==========")
            descending_insertion_sort()

            print("\n========== PROGRAM 78 ==========")
            sort_nearly_sorted()

            print("\n========== PROGRAM 79 ==========")
            insert_into_sorted_array()

            print("\n========== PROGRAM 80 ==========")
            insertion_logic_sort()

        elif choice == "82":

            print("\n🎉 DAY 16 COMPLETED!")
            print("Programs 76–80 completed.")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()