#  DAY 8 - SUBARRAY PROBLEMS


# ==================================================
#  1. Maximum Subarray Sum (Kadane's Algorithm)
# ==================================================

def maximum_subarray_sum(arr):

    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):

        current_sum = max(arr[i],
                          current_sum + arr[i])

        max_sum = max(max_sum,
                      current_sum)

    return max_sum


# ==================================================
# 2. Minimum Subarray Sum
# ==================================================

def minimum_subarray_sum(arr):

    min_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):

        current_sum = min(arr[i],
                          current_sum + arr[i])

        min_sum = min(min_sum,
                      current_sum)

    return min_sum


# ==================================================
# 3. Find All Subarrays
# ==================================================

def find_all_subarrays(arr):

    subarrays = []

    for i in range(len(arr)):

        for j in range(i, len(arr)):

            subarrays.append(arr[i:j + 1])

    return subarrays


# ==================================================
# 4. Subarray With Given Sum
# ==================================================

def subarray_with_given_sum(arr, target):

    for i in range(len(arr)):

        current_sum = 0

        for j in range(i, len(arr)):

            current_sum += arr[j]

            if current_sum == target:

                return arr[i:j + 1]

    return []


# ==================================================
#  5. Longest Increasing Subarray
# ==================================================

def longest_increasing_subarray(arr):

    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):

        if arr[i] > arr[i - 1]:

            current_length += 1

            max_length = max(max_length,
                             current_length)

        else:

            current_length = 1

    return max_length


# ==================================================
# MAIN PROGRAM
# ==================================================

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]

print("Array:")
print(arr)


print("\n Maximum Subarray Sum")
print(maximum_subarray_sum(arr))


print("\n Minimum Subarray Sum")
print(minimum_subarray_sum(arr))


print("\n Find All Subarrays")

all_subarrays = find_all_subarrays([1, 2, 3])

for subarray in all_subarrays:
    print(subarray)


print("\n Subarray With Given Sum")

print(subarray_with_given_sum(
    [1, 2, 3, 7, 5],
    12
))


print("\n Longest Increasing Subarray")

print(
    longest_increasing_subarray(
        [1, 2, 3, 1, 2, 3, 4, 5]
    )
)