"""coding interview problems in Python

Find Duplicate Elements
arr = [1, 2, 3, 4, 2, 5, 3]
duplicates = set([x for x in arr if arr.count(x) > 1])
print("Duplicates:", duplicates)

 Rotate Array by k Steps
def rotate(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

print(rotate([1,2,3,4,5,6], 2))  # [5,6,1,2,3,4]

 Check Anagrams
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True

 Word Frequency in String
def word_frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("this is a test this is"))

 15. Stack using List
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())  # 30

Queue using List
queue = []
queue.append(10)
queue.append(20)
queue.append(30)
print(queue.pop(0))  # 10

Circular Queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear+1) % self.size == self.front:
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front+1) % self.size
            return temp

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
print(cq.dequeue())  # 10

 Priority Queue
import heapq

pq = []
heapq.heappush(pq, (1, "task1"))
heapq.heappush(pq, (3, "task3"))
heapq.heappush(pq, (2, "task2"))

while pq:
    print(heapq.heappop(pq))

Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  # 30 -> 20 -> 10 -> None

reverse the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev


# ---- Driver Code ----
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Original List:")
ll.display()

ll.reverse()
print("Reversed List:")
ll.display()
Output:
Original List: 40 -> 30 -> 20 -> 10 -> None
Reversed List: 10 -> 20 -> 30 -> 40 -> None
"""