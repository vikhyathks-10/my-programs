# ==========================================================
# Month 7 - Day 14
# Python deque (Double Ended Queue)
#
# Topics Covered:
# 1. Queue using deque
# 2. Stack using deque
# 3. Sliding Window using deque
# 4. Rotate deque
# 5. Palindrome Check using deque
# 6. BFS Simulation
# ==========================================================

from collections import deque

print("=" * 60)
print("1. QUEUE USING DEQUE")
print("=" * 60)

queue = deque()

queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")

print("Queue:", queue)

print("Serving:", queue.popleft())
print("Serving:", queue.popleft())

print("Remaining Queue:", queue)


print("\n" + "=" * 60)
print("2. STACK USING DEQUE")
print("=" * 60)

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

print("Pop:", stack.pop())
print("Pop:", stack.pop())

print("Remaining Stack:", stack)


print("\n" + "=" * 60)
print("3. SLIDING WINDOW USING DEQUE")
print("=" * 60)

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

dq = deque()
result = []

for i in range(len(arr)):

    while dq and dq[0] <= i - k:
        dq.popleft()

    while dq and arr[dq[-1]] < arr[i]:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        result.append(arr[dq[0]])

print("Array :", arr)
print("Maximum in Each Window :", result)


print("\n" + "=" * 60)
print("4. ROTATE DEQUE")
print("=" * 60)

dq = deque([1, 2, 3, 4, 5])

print("Original:", dq)

dq.rotate(2)

print("Rotate Right by 2:", dq)

dq.rotate(-3)

print("Rotate Left by 3 :", dq)


print("\n" + "=" * 60)
print("5. PALINDROME CHECK USING DEQUE")
print("=" * 60)

word = "madam"

dq = deque(word)

is_palindrome = True

while len(dq) > 1:

    if dq.popleft() != dq.pop():
        is_palindrome = False
        break

if is_palindrome:
    print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")


print("\n" + "=" * 60)
print("6. BFS SIMULATION")
print("=" * 60)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
queue = deque(['A'])

print("BFS Traversal:")

while queue:

    node = queue.popleft()

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

print()


print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ deque

Double Ended Queue

Import:

from collections import deque

--------------------------------------------------

✔ Advantages

• Fast insertion at both ends
• Fast deletion at both ends

Time Complexity

append()      O(1)
appendleft()  O(1)
pop()         O(1)
popleft()     O(1)

--------------------------------------------------

✔ Queue

FIFO

append()

popleft()

--------------------------------------------------

✔ Stack

LIFO

append()

pop()

--------------------------------------------------

✔ rotate()

rotate(k)

Positive → Right

Negative → Left

--------------------------------------------------

✔ Sliding Window

deque stores useful indices.

Time:
O(n)

--------------------------------------------------

✔ BFS

Queue is used in BFS.

deque is much faster than list
for queue operations.

--------------------------------------------------

Interview Tip

Whenever you hear:

✔ Queue
✔ Sliding Window
✔ BFS
✔ Recent Elements

Think:

👉 deque

It's much faster than using
a normal Python list.
""")