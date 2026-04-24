# 🔹 DAY 24 - ARRAY + SLIDING WINDOW


# 🔹 1. Move Zeros to End (In-place)
def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr


# 🔹 2. Rotate Array (Optimized - Reversal Method)
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)

    return arr


# 🔹 3. Intersection of Sorted Arrays (Two Pointers)
def intersection_sorted(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result


# 🔹 4. Sliding Window (Max Sum of Subarray of Size k)
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# 🔹 5. Subarray Sum Equals Target
def subarray_sum(arr, target):
    curr_sum = 0
    prefix = {0: 1}
    count = 0

    for num in arr:
        curr_sum += num
        if (curr_sum - target) in prefix:
            count += prefix[curr_sum - target]

        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

    return count


# 🔹 MAIN PROGRAM

print("\n--- Move Zeros ---")
print(move_zeros([0, 1, 0, 3, 12]))


print("\n--- Rotate Array ---")
print(rotate_array([1, 2, 3, 4, 5], 2))


print("\n--- Intersection Sorted Arrays ---")
print(intersection_sorted([1, 2, 3, 4], [2, 3, 5]))


print("\n--- Sliding Window (Max Sum) ---")
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))


print("\n--- Subarray Sum Equals Target ---")
print(subarray_sum([1, 2, 3, 2, 1], 3))