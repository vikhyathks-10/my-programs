# 1. Stack using list
stack = []

def push(x):
    stack.append(x)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        return stack.pop()

# 2. Stack using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            print("Stack is empty")
            return
        popped = self.top.data
        self.top = self.top.next
        return popped

# 3. Reverse a string using stack
def reverse_string(s):
    st = []
    for ch in s:
        st.append(ch)

    rev = ""
    while st:
        rev += st.pop()
    return rev

# 4. Check balanced parentheses
def is_balanced(expr):
    st = []
    pairs = {')':'(', '}':'{', ']':'['}

    for ch in expr:
        if ch in "({[":
            st.append(ch)
        elif ch in ")}]":
            if not st or st.pop() != pairs[ch]:
                return False
    return not st

# 5. Implement stack using two queues
from collections import deque

class StackTwoQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            print("Stack empty")
            return
        return self.q1.popleft()


# --------- Testing ----------
print(reverse_string("hello"))
print(is_balanced("{[()]}"))
