# ============================================================
# DAY 7 — WEEK 1 REVISION
# Programs 31–35
# ============================================================


# ------------------------------------------------------------
# 31. Maximum Subarray Sum — Brute Force
# ------------------------------------------------------------

def maximum_subarray_brute_force():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    maximum_sum = arr[0]

    for i in range(n):

        current_sum = 0

        for j in range(i, n):

            current_sum += arr[j]

            if current_sum > maximum_sum:
                maximum_sum = current_sum

    print("Maximum subarray sum:", maximum_sum)

    print("Time Complexity: O(N²)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 32. Find Minimum Element Without min()
# ------------------------------------------------------------

def find_minimum():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    minimum = arr[0]

    for i in range(1, n):

        if arr[i] < minimum:
            minimum = arr[i]

    print("Minimum element:", minimum)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 33. Find Second Smallest Element
# ------------------------------------------------------------

def second_smallest():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    if n < 2:
        print("Second smallest element does not exist.")
        return

    smallest = float("inf")
    second = float("inf")

    for num in arr:

        if num < smallest:
            second = smallest
            smallest = num

        elif smallest < num < second:
            second = num

    if second == float("inf"):
        print("Second smallest element does not exist.")
    else:
        print("Second smallest element:", second)

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 34. Find Equilibrium Index
# ------------------------------------------------------------

def equilibrium_index():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    total_sum = 0

    for num in arr:
        total_sum += num

    left_sum = 0
    found = False

    for i in range(n):

        # Right sum = total - left - current
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            print("Equilibrium index:", i)
            found = True
            break

        left_sum += arr[i]

    if not found:
        print("No equilibrium index found.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ------------------------------------------------------------
# 35. Find Majority Element
# ------------------------------------------------------------

def majority_element():

    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter array elements: ").split()))

    # Boyer-Moore Voting Algorithm
    candidate = None
    count = 0

    for num in arr:

        if count == 0:
            candidate = num
            count = 1

        elif num == candidate:
            count += 1

        else:
            count -= 1

    # Verify candidate
    frequency = 0

    for num in arr:

        if num == candidate:
            frequency += 1

    if frequency > n // 2:
        print("Majority element:", candidate)
    else:
        print("No majority element.")

    print("Time Complexity: O(N)")
    print("Space Complexity: O(1)")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n" + "=" * 65)
        print("             DAY 7 — WEEK 1 REVISION")
        print("=" * 65)

        print("31. Maximum Subarray Sum — Brute Force")
        print("32. Find Minimum Element")
        print("33. Find Second Smallest Element")
        print("34. Find Equilibrium Index")
        print("35. Find Majority Element")
        print("36. Run All Programs")
        print("37. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "31":
            maximum_subarray_brute_force()

        elif choice == "32":
            find_minimum()

        elif choice == "33":
            second_smallest()

        elif choice == "34":
            equilibrium_index()

        elif choice == "35":
            majority_element()

        elif choice == "36":

            print("\n========== PROGRAM 31 ==========")
            maximum_subarray_brute_force()

            print("\n========== PROGRAM 32 ==========")
            find_minimum()

            print("\n========== PROGRAM 33 ==========")
            second_smallest()

            print("\n========== PROGRAM 34 ==========")
            equilibrium_index()

            print("\n========== PROGRAM 35 ==========")
            majority_element()

        elif choice == "37":
            print("\n🎉 WEEK 1 COMPLETED!")
            print("35 DSA programs completed!")
            break

        else:
            print("Invalid choice. Please try again.")


main()