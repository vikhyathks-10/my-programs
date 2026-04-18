# 🔹 DAY 18 - QUEUE IMPLEMENTATIONS


# 🔹 1. Queue using List
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(value, "enqueued")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)


# 🔹 2. Circular Queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            print("Removed:", self.queue[self.front])
            self.front = self.rear = -1
        else:
            print("Removed:", self.queue[self.front])
            self.front = (self.front + 1) % self.size

    def display(self):
        print("Circular Queue:", self.queue)


# 🔹 3. Deque (Double Ended Queue)
class Deque:
    def __init__(self):
        self.dq = []

    def add_front(self, value):
        self.dq.insert(0, value)

    def add_rear(self, value):
        self.dq.append(value)

    def remove_front(self):
        if self.dq:
            return self.dq.pop(0)

    def remove_rear(self):
        if self.dq:
            return self.dq.pop()

    def display(self):
        print("Deque:", self.dq)


# 🔹 4. Priority Queue (Basic)
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        self.queue.sort()   # smallest = highest priority

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)

    def display(self):
        print("Priority Queue:", self.queue)


# 🔹 5. Queue using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, value):
        self.s1.append(value)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2.pop()
        return "Queue is empty"


# 🔹 MAIN PROGRAM

print("\n--- Queue using List ---")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeued:", q.dequeue())
q.display()


print("\n--- Circular Queue ---")
cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()
cq.dequeue()
cq.enqueue(4)
cq.display()


print("\n--- Deque ---")
dq = Deque()
dq.add_front(10)
dq.add_rear(20)
dq.add_front(5)
dq.display()
print("Remove rear:", dq.remove_rear())


print("\n--- Priority Queue ---")
pq = PriorityQueue()
pq.enqueue(30)
pq.enqueue(10)
pq.enqueue(20)
pq.display()
print("Dequeued:", pq.dequeue())


print("\n--- Queue using Two Stacks ---")
qs = QueueUsingStacks()
qs.enqueue(1)
qs.enqueue(2)
qs.enqueue(3)
print("Dequeued:", qs.dequeue())
print("Dequeued:", qs.dequeue())