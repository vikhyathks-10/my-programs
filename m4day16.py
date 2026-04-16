# 🔹 DAY 16 - ADVANCED ARRAY PROBLEMS


# 🔹 1. Second Largest Element
def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


# 🔹 2. Remove Duplicates
def remove_duplicates(arr):
    return list(set(arr))   # simple method


# 🔹 3. Merge Two Arrays
def merge_arrays(arr1, arr2):
    return arr1 + arr2


# 🔹 4. Intersection of Arrays
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


# 🔹 5. Prefix Sum
def prefix_sum(arr):
    prefix = []
    current = 0
    for num in arr:
        current += num
        prefix.append(current)
    return prefix


# 🔹 MAIN PROGRAM

arr = [10, 20, 30, 40, 30, 20]

print("\n--- Second Largest ---")
print(second_largest(arr))


print("\n--- Remove Duplicates ---")
print(remove_duplicates(arr))


print("\n--- Merge Arrays ---")
arr2 = [50, 60]
print(merge_arrays(arr, arr2))


print("\n--- Intersection ---")
print(intersection(arr, arr2))


print("\n--- Prefix Sum ---")
print(prefix_sum(arr))