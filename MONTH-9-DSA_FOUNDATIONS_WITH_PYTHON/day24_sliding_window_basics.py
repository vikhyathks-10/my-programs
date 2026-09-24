# ============================================================
# DAY 24 — SLIDING WINDOW BASICS
# Programs 116–120
# ============================================================


# ------------------------------------------------------------
# PROGRAM 116 — Maximum Sum Subarray of Size K
# ------------------------------------------------------------

def maximum_sum_subarray():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    k = int(input("Enter K: "))

    if k <= 0 or k > n:

        print("Invalid K.")
        return

    # Calculate first window
    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    maximum_sum = window_sum

    # Slide the window
    for i in range(k, n):

        window_sum += arr[i]
        window_sum -= arr[i - k]

        if window_sum > maximum_sum:
            maximum_sum = window_sum

    print("Maximum sum of a window:", maximum_sum)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 117 — Minimum Sum Subarray of Size K
# ------------------------------------------------------------

def minimum_sum_subarray():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    k = int(input("Enter K: "))

    if k <= 0 or k > n:

        print("Invalid K.")
        return

    # First window
    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    minimum_sum = window_sum

    # Slide the window
    for i in range(k, n):

        window_sum += arr[i]
        window_sum -= arr[i - k]

        if window_sum < minimum_sum:
            minimum_sum = window_sum

    print("Minimum sum of a window:", minimum_sum)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# PROGRAM 118 — Average of Every Window of Size K
# ------------------------------------------------------------

def average_every_window():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    k = int(input("Enter K: "))

    if k <= 0 or k > n:

        print("Invalid K.")
        return

    averages = []

    # First window
    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    averages.append(window_sum / k)

    # Remaining windows
    for i in range(k, n):

        window_sum += arr[i]
        window_sum -= arr[i - k]

        averages.append(window_sum / k)

    print("Averages of all windows:")

    for average in averages:
        print(average)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 119 — Maximum Element in Every Window
# Basic Approach
# ------------------------------------------------------------

def maximum_in_every_window():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    k = int(input("Enter K: "))

    if k <= 0 or k > n:

        print("Invalid K.")
        return

    maximums = []

    # Check every window independently
    for i in range(n - k + 1):

        current_max = arr[i]

        for j in range(i, i + k):

            if arr[j] > current_max:
                current_max = arr[j]

        maximums.append(current_max)

    print("Maximum element in every window:")
    print(maximums)

    print("Time Complexity: O(N × K)")
    print("Space Complexity: O(N)")


# ------------------------------------------------------------
# PROGRAM 120 — Count Windows Whose Sum Exceeds X
# ------------------------------------------------------------

def count_windows_exceeding_x():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array: ").split()))

    k = int(input("Enter K: "))
    x = int(input("Enter X: "))

    if k <= 0 or k > n:

        print("Invalid K.")
        return

    # Calculate first window
    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    count = 0

    if window_sum > x:
        count += 1

    # Slide the window
    for i in range(k, n):

        window_sum += arr[i]
        window_sum -= arr[i - k]

        if window_sum > x:
            count += 1

    print("Number of windows with sum greater than X:", count)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        print("\n" + "=" * 65)
        print("             DAY 24 — SLIDING WINDOW BASICS")
        print("=" * 65)

        print("116. Maximum Sum Subarray of Size K")
        print("117. Minimum Sum Subarray of Size K")
        print("118. Average of Every Window of Size K")
        print("119. Maximum Element in Every Window — Basic")
        print("120. Count Windows Whose Sum Exceeds X")
        print("121. Run All Programs")
        print("122. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "116":

            print("\n========== PROGRAM 116 ==========")
            maximum_sum_subarray()

        elif choice == "117":

            print("\n========== PROGRAM 117 ==========")
            minimum_sum_subarray()

        elif choice == "118":

            print("\n========== PROGRAM 118 ==========")
            average_every_window()

        elif choice == "119":

            print("\n========== PROGRAM 119 ==========")
            maximum_in_every_window()

        elif choice == "120":

            print("\n========== PROGRAM 120 ==========")
            count_windows_exceeding_x()

        elif choice == "121":

            print("\n========== PROGRAM 116 ==========")
            maximum_sum_subarray()

            print("\n========== PROGRAM 117 ==========")
            minimum_sum_subarray()

            print("\n========== PROGRAM 118 ==========")
            average_every_window()

            print("\n========== PROGRAM 119 ==========")
            maximum_in_every_window()

            print("\n========== PROGRAM 120 ==========")
            count_windows_exceeding_x()

        elif choice == "122":

            print("\n🎉 DAY 24 COMPLETED!")
            print("Programs 116–120 completed.")
            print("Total DSA programs completed: 120")
            break

        else:

            print("❌ Invalid choice. Please try again.")


# Start program
main()