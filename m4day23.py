# 🔹 DAY 23 - IMPORTANT ARRAY PROBLEMS


# 🔹 1. Two Sum (Using HashMap)
def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i
    return None


# 🔹 2. Max Subarray (Basic - Brute Force)
def max_subarray_bruteforce(arr):
    max_sum = float('-inf')
    n = len(arr)

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum


# 🔹 3. Kadane’s Algorithm (Optimized)
def kadane(arr):
    max_sum = curr_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum


# 🔹 4. Pair Sum (All pairs)
def pair_sum(arr, target):
    pairs = []
    seen = set()

    for num in arr:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)

    return pairs


# 🔹 5. Duplicate Detection
def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


# 🔹 MAIN PROGRAM

arr = [2, 7, 11, 15]

print("\n--- Two Sum ---")
print(two_sum(arr, 9))


print("\n--- Max Subarray (Brute Force) ---")
arr2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_bruteforce(arr2))


print("\n--- Kadane’s Algorithm ---")
print(kadane(arr2))


print("\n--- Pair Sum ---")
print(pair_sum([1, 2, 3, 4, 5], 5))


print("\n--- Duplicate Detection ---")
print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))