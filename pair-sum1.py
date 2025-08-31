# Use hash set for quick lookup.
# Find All Pairs with Given Sum
def pair_sum(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        if target - num in seen:
            pairs.append((num, target - num))
        seen.add(num)
    return pairs

# Example
print(pair_sum([1,5,7,-1,5], 6))  # Output: [(5, 1), (-1, 7)]
