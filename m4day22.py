# 🔹 DAY 22 - SEARCHING & ANALYSIS


# 🔹 1. Optimized Linear Search (Early Stop if Sorted)
def optimized_linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        if arr[i] > target:   # optimization (sorted array)
            break
    return -1


# 🔹 2. Binary Search (Edge Cases Handled)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2   # avoids overflow

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1   # not found


# 🔹 3. Sorting Comparison (Using Built-in)
def sort_and_compare(arr):
    print("Original:", arr)
    print("Sorted:", sorted(arr))


# 🔹 4. Best / Worst Case Demo (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    swapped = False

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break   # best case optimization

    return arr


# 🔹 5. Find Missing Number (1 to n)
def find_missing(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)


# 🔹 MAIN PROGRAM

arr = [1, 3, 5, 7, 9]

print("\n--- Optimized Linear Search ---")
print("Index of 5:", optimized_linear_search(arr, 5))


print("\n--- Binary Search Edge Cases ---")
print("Index of 7:", binary_search(arr, 7))
print("Index of 10:", binary_search(arr, 10))  # not found


print("\n--- Sorting Comparison ---")
sort_and_compare([4, 2, 8, 1])


print("\n--- Bubble Sort (Best Case Optimization) ---")
print(bubble_sort([1, 2, 3, 4]))  # already sorted


print("\n--- Find Missing Number ---")
arr2 = [1, 2, 4, 5]
print("Missing number:", find_missing(arr2, 5))