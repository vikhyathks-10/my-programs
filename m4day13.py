# 🔹 DAY 13 - OPTIMIZATION + TREES + BACKTRACKING


# 🔹 1. Nth Fibonacci (Optimized using Memoization)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


# 🔹 2. Recursive Sorting (Merge Sort Idea)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 🔹 3. Binary Tree Traversal (Basic Inorder)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# 🔹 4. Power Set (All Subsets)
def power_set(arr, index=0, current=[]):
    if index == len(arr):
        print(current)
        return

    # include
    power_set(arr, index+1, current + [arr[index]])

    # exclude
    power_set(arr, index+1, current)


# 🔹 5. Backtracking Intro (Simple Path)
def backtrack(n, path=[]):
    if len(path) == n:
        print(path)
        return

    for i in range(1, 3):  # choices (1 or 2)
        path.append(i)
        backtrack(n, path)
        path.pop()   # undo (backtracking)


# 🔹 MAIN PROGRAM

print("\n--- Optimized Fibonacci ---")
print("Fib(10):", fib(10))


print("\n--- Merge Sort ---")
arr = [5, 2, 9, 1, 3]
print("Sorted:", merge_sort(arr))


print("\n--- Binary Tree Traversal ---")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal:")
inorder(root)


print("\n\n--- Power Set ---")
power_set([1, 2, 3])


print("\n--- Backtracking Intro ---")
backtrack(2)