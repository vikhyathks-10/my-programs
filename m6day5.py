# 🔹 DAY 5 - SEARCHING


# 🔹 1. Linear Search

def linear_search(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


# 🔹 2. Binary Search

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# 🔹 3. Find First Occurrence

def first_occurrence(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1


# 🔹 4. Find Last Occurrence

def last_occurrence(arr, target):

    for i in range(len(arr) - 1, -1, -1):

        if arr[i] == target:
            return i

    return -1


# 🔹 5. Count Occurrences

def count_occurrences(arr, target):

    count = 0

    for num in arr:

        if num == target:
            count += 1

    return count


# 🔹 MAIN PROGRAM

arr = [1, 2, 3, 4, 4, 4, 5, 6]

target = 4


print("Array:", arr)

print("\nLinear Search:")
print(linear_search(arr, target))


print("\nBinary Search:")
print(binary_search(arr, target))


print("\nFirst Occurrence:")
print(first_occurrence(arr, target))


print("\nLast Occurrence:")
print(last_occurrence(arr, target))


print("\nCount Occurrences:")
print(count_occurrences(arr, target))