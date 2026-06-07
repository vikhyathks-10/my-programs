# 🔹 DAY 7 - STACK & QUEUE


# ==================================================
# 🔹 1. Stack Using List
# ==================================================

class Stack:

    def __init__(self):

        self.stack = []

    def push(self, value):

        self.stack.append(value)

    def pop(self):

        if self.stack:
            return self.stack.pop()

        return "Stack Empty"

    def peek(self):

        if self.stack:
            return self.stack[-1]

        return "Stack Empty"

    def display(self):

        return self.stack


# ==================================================
# 🔹 2. Queue Using List
# ==================================================

class Queue:

    def __init__(self):

        self.queue = []

    def enqueue(self, value):

        self.queue.append(value)

    def dequeue(self):

        if self.queue:
            return self.queue.pop(0)

        return "Queue Empty"

    def display(self):

        return self.queue


# ==================================================
# 🔹 3. Reverse String Using Stack
# ==================================================

def reverse_string(text):

    stack = []

    for ch in text:
        stack.append(ch)

    reversed_text = ""

    while stack:
        reversed_text += stack.pop()

    return reversed_text


# ==================================================
# 🔹 4. Balanced Parentheses Checker
# ==================================================

def balanced_parentheses(expression):

    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in expression:

        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":

            if not stack:
                return False

            if stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


# ==================================================
# 🔹 5. Circular Queue Simulation
# ==================================================

class CircularQueue:

    def __init__(self, size):

        self.size = size

        self.queue = [None] * size

        self.front = -1

        self.rear = -1

    def enqueue(self, value):

        if (self.rear + 1) % self.size == self.front:

            print("Queue Full")
            return

        if self.front == -1:

            self.front = 0
            self.rear = 0

        else:

            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value

    def dequeue(self):

        if self.front == -1:

            return "Queue Empty"

        value = self.queue[self.front]

        if self.front == self.rear:

            self.front = -1
            self.rear = -1

        else:
            self.front = (self.front + 1) % self.size
        return value
    def display(self):
        if self.front == -1:
            return []
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        return result


# ==================================================
# 🔹 MAIN PROGRAM
# ==================================================

print("🔹 STACK USING LIST")

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.display())

print("Popped:", stack.pop())

print("Top Element:", stack.peek())



print("\n🔹 QUEUE USING LIST")

queue = Queue()

queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)

print(queue.display())

print("Dequeued:", queue.dequeue())

print(queue.display())



print("\n🔹 REVERSE STRING USING STACK")

print(reverse_string("Python"))



print("\n🔹 BALANCED PARENTHESES CHECKER")

print(balanced_parentheses("{[()]}"))

print(balanced_parentheses("{[(])}"))



print("\n🔹 CIRCULAR QUEUE SIMULATION")

cq = CircularQueue(5)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)

print(cq.display())

print("Dequeued:", cq.dequeue())

cq.enqueue(5)

print(cq.display())