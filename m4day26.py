# 🔹 DAY 26 - MIXED PROBLEM SOLVING


# 🔹 1. Sorting Optimization (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# 🔹 2. Recursive + DS Combo (Sum of Linked List)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sum_linked_list(node):
    if not node:
        return 0
    return node.data + sum_linked_list(node.next)


# 🔹 3. Stack + Problem (Next Greater Element)
def next_greater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result


# 🔹 4. Queue + Problem (First Non-Repeating Character)
from collections import deque

def first_non_repeating(stream):
    q = deque()
    freq = {}
    result = []

    for ch in stream:
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)

        while q and freq[q[0]] > 1:
            q.popleft()

        result.append(q[0] if q else '#')

    return result


# 🔹 5. Mixed Logic (Majority Element)
def majority_element(arr):
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


# 🔹 MAIN PROGRAM

print("\n--- Quick Sort ---")
print(quick_sort([5, 2, 9, 1, 3]))


print("\n--- Sum of Linked List ---")
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print("Sum:", sum_linked_list(head))


print("\n--- Next Greater Element ---")
print(next_greater([4, 5, 2, 10]))


print("\n--- First Non-Repeating Character ---")
print(first_non_repeating("aabc"))


print("\n--- Majority Element ---")
print(majority_element([2, 2, 1, 2, 3, 2, 2]))