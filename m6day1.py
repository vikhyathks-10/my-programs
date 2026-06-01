# 🔹 DAY 1 - ARRAYS BASICS


# 🔹 1. Find Largest Element

def find_largest(arr):

    largest = arr[0]

    for num in arr:

        if num > largest:
            largest = num

    return largest


# 🔹 2. Find Smallest Element

def find_smallest(arr):

    smallest = arr[0]

    for num in arr:

        if num < smallest:
            smallest = num

    return smallest


# 🔹 3. Find Second Largest Element

def find_second_largest(arr):

    largest = second = float('-inf')

    for num in arr:

        if num > largest:

            second = largest
            largest = num

        elif num > second and num != largest:

            second = num

    return second


# 🔹 4. Reverse an Array

def reverse_array(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


# 🔹 5. Find Sum of Array Elements

def array_sum(arr):

    total = 0

    for num in arr:
        total += num

    return total


# 🔹 MAIN PROGRAM

arr = [10, 25, 5, 40, 15]

print("Array:", arr)

print("\nLargest Element:")
print(find_largest(arr))

print("\nSmallest Element:")
print(find_smallest(arr))

print("\nSecond Largest Element:")
print(find_second_largest(arr))

print("\nReversed Array:")
print(reverse_array(arr.copy()))

print("\nSum of Array Elements:")
print(array_sum(arr))