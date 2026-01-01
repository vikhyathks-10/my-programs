# 1. Queue using list
queue = []

def enqueue(x):
    queue.append(x)

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        return queue.pop(0)

# 2. Queue using collections.deque
from collections import deque

dq = deque()

dq.append(10)      # enqueue
dq.append(20)
dq.popleft()       # dequeue

# 3. Circular Queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data

# 4. Queue using two stacks
class QueueTwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            print("Queue empty")
            return
        return self.s2.pop()

# 5. Reverse a queue
def reverse_queue(q):
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())


# --------- Testing ----------
q = deque([1, 2, 3])
reverse_queue(q)
print(q)