# 🔹 DAY 11 - PAIR & SUM PROBLEMS


# ==================================================
# 🔹 1. Pair Sum Problem
# ==================================================

def pair_sum(arr, target):

    pairs = []

    n = len(arr)

    for i in range(n):

        for j in range(i + 1, n):

            if arr[i] + arr[j] == target:

                pairs.append((arr[i], arr[j]))

    return pairs


# ==================================================
# 🔹 2. Triplet Sum Problem
# ==================================================

def triplet_sum(arr, target):

    triplets = []

    n = len(arr)

    for i in range(n):

        for j in range(i + 1, n):

            for k in range(j + 1, n):

                if arr[i] + arr[j] + arr[k] == target:

                    triplets.append(
                        (arr[i], arr[j], arr[k])
                    )

    return triplets


# ==================================================
# 🔹 3. Two Sum Optimized
# ==================================================

def two_sum_optimized(arr, target):

    seen = {}

    for i, num in enumerate(arr):

        complement = target - num

        if complement in seen:

            return [seen[complement], i]

        seen[num] = i

    return []


# ==================================================
# 🔹 4. Closest Pair Problem
# ==================================================

def closest_pair(arr, target):

    arr.sort()

    left = 0
    right = len(arr) - 1

    closest = (arr[left], arr[right])

    min_diff = float('inf')

    while left < right:

        current_sum = arr[left] + arr[right]

        diff = abs(target - current_sum)

        if diff < min_diff:

            min_diff = diff

            closest = (arr[left], arr[right])

        if current_sum < target:

            left += 1

        else:

            right -= 1

    return closest


# ==================================================
# 🔹 5. Target Difference Pair
# ==================================================

def target_difference_pair(arr, diff):

    seen = set()

    for num in arr:

        if num - diff in seen:

            return (num - diff, num)

        if num + diff in seen:

            return (num, num + diff)

        seen.add(num)

    return None


# ==================================================
# 🔹 MAIN PROGRAM
# ==================================================

arr = [1, 2, 3, 4, 5, 6]

print("Array:")
print(arr)


print("\n🔹 Pair Sum Problem")
print(pair_sum(arr, 7))


print("\n🔹 Triplet Sum Problem")
print(triplet_sum(arr, 10))


print("\n🔹 Two Sum Optimized")
print(two_sum_optimized(arr, 7))


print("\n🔹 Closest Pair Problem")
print(closest_pair(arr, 8))


print("\n🔹 Target Difference Pair")
print(target_difference_pair(arr, 2))