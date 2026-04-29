# 🔹 DAY 29 - REVISION + DEBUG + OPTIMIZATION


# 🔹 1. Mixed Revision (Kadane + Two Sum)
def kadane(arr):
    max_sum = curr = arr[0]
    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])
        max_sum = max(max_sum, curr)
    return max_sum


def two_sum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        if target - num in seen:
            return (seen[target - num], i)
        seen[num] = i
    return None


# 🔹 2. Weak Area Practice (Sliding Window)
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# 🔹 3. Debugging Problem (Fix this logic)
def buggy_reverse(arr):
    # BUG: incorrect loop condition
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# 🔹 4. Optimize Old Code (Improved Bubble Sort)
def optimized_bubble(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# 🔹 5. Re-implement Key DS (Stack)
class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop() if self.data else None

    def peek(self):
        return self.data[-1] if self.data else None


# 🔹 MAIN PROGRAM

print("\n--- Mixed Revision ---")
print("Kadane:", kadane([-2,1,-3,4,-1,2,1,-5,4]))
print("Two Sum:", two_sum([2,7,11,15], 9))


print("\n--- Weak Area Practice ---")
print("Longest substring:", longest_unique_substring("abcabcbb"))


print("\n--- Debugging ---")
print("Reverse:", buggy_reverse([1,2,3,4]))


print("\n--- Optimization ---")
print("Sorted:", optimized_bubble([5,3,2,4,1]))


print("\n--- Stack Re-implementation ---")
s = Stack()
s.push(10)
s.push(20)
print("Peek:", s.peek())
print("Pop:", s.pop())