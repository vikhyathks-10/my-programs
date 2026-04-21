# 🔹 DAY 21 - SEARCHING & SORTING


# 🔹 1. Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 🔹 2. Binary Search (Iterative)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# 🔹 3. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 🔹 4. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# 🔹 5. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr


# 🔹 MAIN PROGRAM

arr = [64, 25, 12, 22, 11]

print("\n--- Linear Search ---")
print("Index of 22:", linear_search(arr, 22))


print("\n--- Binary Search ---")
sorted_arr = sorted(arr)
print("Sorted Array:", sorted_arr)
print("Index of 25:", binary_search(sorted_arr, 25))


print("\n--- Bubble Sort ---")
print(bubble_sort(arr.copy()))


print("\n--- Selection Sort ---")
print(selection_sort(arr.copy()))


print("\n--- Insertion Sort ---")
print(insertion_sort(arr.copy()))