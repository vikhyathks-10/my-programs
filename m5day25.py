# 🔹 DAY 25 - MIXED DSA


# 🔹 1. Stack Problem (Balanced Parentheses)

def balanced_parentheses(s):

    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:

        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":

            if not stack or stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return len(stack) == 0


# 🔹 2. Queue Problem (Simple Queue)

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):

        if self.items:
            return self.items.pop(0)

        return "Queue Empty"

    def display(self):
        return self.items


# 🔹 3. Linked List Logic

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def insert_end(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):

        temp = self.head

        while temp:

            print(temp.data, end=" -> ")

            temp = temp.next

        print("None")


# 🔹 4. Binary Search Practice

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# 🔹 5. Sorting Challenge (Bubble Sort)

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:
            break

    return arr


# 🔹 MAIN PROGRAM

print("\n--- Stack Problem ---")

print(balanced_parentheses("{[()]}"))
print(balanced_parentheses("{[(])}"))


print("\n--- Queue Problem ---")

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.display())

print("Dequeued:", q.dequeue())

print(q.display())


print("\n--- Linked List Logic ---")

ll = LinkedList()

ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)

ll.display()


print("\n--- Binary Search ---")

arr = [1, 3, 5, 7, 9]

print(binary_search(arr, 7))


print("\n--- Sorting Challenge ---")

nums = [5, 1, 4, 2, 8]

print(bubble_sort(nums))