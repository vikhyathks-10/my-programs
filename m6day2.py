# 🔹 DAY 2 - ARRAYS INTERMEDIATE


# 🔹 1. Remove Duplicates

def remove_duplicates(arr):

    result = []

    for num in arr:

        if num not in result:
            result.append(num)

    return result


# 🔹 2. Rotate Array by K Positions

def rotate_array(arr, k):

    k = k % len(arr)

    return arr[-k:] + arr[:-k]


# 🔹 3. Merge Two Arrays

def merge_arrays(arr1, arr2):

    merged = arr1 + arr2

    return merged


# 🔹 4. Find Missing Number

def find_missing_number(arr):

    n = len(arr) + 1

    expected_sum = n * (n + 1) // 2

    actual_sum = sum(arr)

    return expected_sum - actual_sum


# 🔹 5. Find Duplicate Element

def find_duplicate(arr):

    seen = set()

    for num in arr:

        if num in seen:
            return num

        seen.add(num)

    return None


# 🔹 MAIN PROGRAM

arr1 = [1, 2, 2, 3, 4, 4, 5]

arr2 = [6, 7, 8]


print("Original Array:")
print(arr1)


print("\nRemove Duplicates:")
print(remove_duplicates(arr1))


print("\nRotate Array by K = 2:")
print(rotate_array(arr1, 2))


print("\nMerge Two Arrays:")
print(merge_arrays(arr1, arr2))


print("\nFind Missing Number:")
missing_arr = [1, 2, 3, 5]
print(find_missing_number(missing_arr))


print("\nFind Duplicate Element:")
duplicate_arr = [1, 2, 3, 4, 3, 5]
print(find_duplicate(duplicate_arr))