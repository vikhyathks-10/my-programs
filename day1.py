# 1️⃣ Longest Conseutive Sequence
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)

    return longest


# 2️⃣ Trapping Rain Water
def trapRainWater(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1

    return water


# 3️⃣ Maximum Product Subarray
def maxProductSubarray(nums):
    max_prod = min_prod = result = nums[0]

    for i in range(1, len(nums)):
        temp = max_prod
        max_prod = max(nums[i], nums[i] * max_prod, nums[i] * min_prod)
        min_prod = min(nums[i], nums[i] * temp, nums[i] * min_prod)
        result = max(result, max_prod)

    return result


# 4️⃣ Chocolate Distribution
def chocolateDistribution(arr, m):
    if m == 0 or len(arr) == 0:
        return 0

    arr.sort()
    min_diff = float('inf')

    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff


# 5️⃣ Kth Smallest Element
def kthSmallest(arr, k):
    arr.sort()
    return arr[k - 1]


# 6️⃣ Count Inversions in Array
def countInversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])

        merged = []
        i = j = inv = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inv + inv_left + inv_right

    _, total_inv = merge_sort(arr)
    return total_inv


# 🔽 Example Usage
arr = [1, 9, 3, 10, 4, 20, 2]
print("Longest Consecutive:", longestConsecutive(arr))

height = [4, 2, 0, 3, 2, 5]
print("Trapped Water:", trapRainWater(height))

nums = [2, 3, -2, 4]
print("Max Product Subarray:", maxProductSubarray(nums))

choco = [7, 3, 2, 4, 9, 12, 56]
m = 3
print("Chocolate Distribution:", chocolateDistribution(choco, m))

karr = [7, 10, 4, 3, 20, 15]
k = 3
print("Kth Smallest:", kthSmallest(karr, k))

inv_arr = [8, 4, 2, 1]
print("Inversion Count:", countInversions(inv_arr))
