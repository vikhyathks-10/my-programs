"""Binary Search Variations

1. Find First Occurrence of an Element

def first_occurrence(arr, x):
    left, right = 0, len(arr)-1
    result = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == x:
            result = mid
            right = mid-1
        elif arr[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return result

print(first_occurrence([1,2,2,2,3,4], 2))  # Output: 1


2. Find Last Occurrence of an Element

def last_occurrence(arr, x):
    left, right = 0, len(arr)-1
    result = -1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == x:
            result = mid
            left = mid+1
        elif arr[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return result

print(last_occurrence([1,2,2,2,3,4], 2))  # Output: 3


3. Count Occurrences of an Element

def count_occurrences(arr, x):
    return last_occurrence(arr, x) - first_occurrence(arr, x) + 1

print(count_occurrences([1,2,2,2,3,4], 2))  # Output: 3


4. Search in Rotated Sorted Array

def search_rotated(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid+1
            else:
                right = mid-1
    return -1

print(search_rotated([4,5,6,7,0,1,2], 0))  # Output: 4

Sorting Variations

5. Bubble Sort Descending

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort_desc([3,1,4,2]))  # Output: [4,3,2,1]


6. Selection Sort – k Smallest Elements

def k_smallest(arr, k):
    for i in range(k):
        min_idx = i + arr[i:].index(min(arr[i:]))
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[:k]

print(k_smallest([7, 10, 4, 3, 20, 15], 3))  # Output: [3,4,7]


7. Insertion Sort Strings Alphabetically

def insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(insertion_sort_strings(["banana","apple","cherry"]))  
# Output: ['apple','banana','cherry']


8. Quicksort with Last Element as Pivot

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))  # Output: [1,1,2,3,6,8,10]


9. Merge Sort – Count Inversions

def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr)//2
    left, inv_left = merge_count(arr[:mid])
    right, inv_right = merge_count(arr[mid:])
    merged, inv_split = [], 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_split += len(left)-i
            j += 1
    merged += left[i:] + right[j:]
    return merged, inv_left+inv_right+inv_split

arr = [2,4,1,3,5]
print(merge_count(arr)[1])  # Output: 3 inversions
"""

"""GCD / LCM Variations

10. GCD of More Than 2 Numbers

from math import gcd
from functools import reduce
def gcd_list(lst):
    return reduce(gcd, lst)
print(gcd_list([12, 24, 36]))  # Output: 12
"""