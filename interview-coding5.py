"""Common Python Coding Interview Questions and Solutions
1. Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # Output: 3

 2. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 25, 12, 22, 11]))

 3. Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))

 4. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort([64, 25, 12, 22, 11]))

 5. Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([64, 25, 12, 22, 11]))

 6. Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1; k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1; k += 1
    return arr

print(merge_sort([64, 25, 12, 22, 11]))

 7. GCD of Two Numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # Output: 6

 8. LCM of Two Numbers
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

print(lcm(12, 15))  # Output: 60

 9. Pascal’s Triangle
def pascal(n):
    for i in range(n):
        num = 1
        for j in range(i+1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

pascal(5)

 10. Find Missing Number (1 to n)
def find_missing(arr, n):
    total = n*(n+1)//2
    return total - sum(arr)

print(find_missing([1,2,3,5], 5))  # Output: 4
"""