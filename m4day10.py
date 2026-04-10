# 🔹 DAY 10 - SEARCHING USING RECURSION


# 🔹 1. Binary Search (Recursive)
def binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)


# 🔹 2. Linear Search (Recursive)
def linear_search(arr, index, target):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search(arr, index + 1, target)


# 🔹 3. First Occurrence
def first_occurrence(arr, index, target):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return first_occurrence(arr, index + 1, target)


# 🔹 4. Last Occurrence
def last_occurrence(arr, index, target):
    if index == len(arr):
        return -1

    res = last_occurrence(arr, index + 1, target)

    if res != -1:
        return res
    if arr[index] == target:
        return index
    return -1


# 🔹 5. Count Occurrences
def count_occurrences(arr, index, target):
    if index == len(arr):
        return 0

    count = 1 if arr[index] == target else 0
    return count + count_occurrences(arr, index + 1, target)


# 🔹 MAIN PROGRAM

arr = [1, 2, 3, 2, 4, 2, 5]

print("\n--- Binary Search ---")
sorted_arr = sorted(arr)
print("Sorted Array:", sorted_arr)
print("Index of 4:", binary_search(sorted_arr, 0, len(sorted_arr)-1, 4))


print("\n--- Linear Search ---")
print("Index of 3:", linear_search(arr, 0, 3))


print("\n--- First Occurrence ---")
print("First index of 2:", first_occurrence(arr, 0, 2))


print("\n--- Last Occurrence ---")
print("Last index of 2:", last_occurrence(arr, 0, 2))


print("\n--- Count Occurrences ---")
print("Count of 2:", count_occurrences(arr, 0, 2))