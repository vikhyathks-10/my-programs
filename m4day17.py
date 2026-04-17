# 🔹 DAY 17 - STACK IMPLEMENTATION


# 🔹 STACK USING LIST
class Stack:
    def __init__(self):
        self.stack = []

    # 🔹 Push
    def push(self, value):
        self.stack.append(value)
        print(value, "pushed")

    # 🔹 Pop
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    # 🔹 Peek
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    # 🔹 Check Empty
    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


# 🔹 BALANCED PARENTHESES
def is_balanced(expr):
    stack = []
    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (ch == ')' and top != '(') or \
               (ch == '}' and top != '{') or \
               (ch == ']' and top != '['):
                return False
    return len(stack) == 0


# 🔹 REVERSE STRING USING STACK
def reverse_string(s):
    stack = list(s)
    rev = ""
    while stack:
        rev += stack.pop()
    return rev


# 🔹 MAIN PROGRAM

s = Stack()

print("\n--- Stack Operations ---")
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Pop:", s.pop())
print("Peek:", s.peek())
s.display()


print("\n--- Balanced Parentheses ---")
expr = "{[()]}"
print(expr, "->", is_balanced(expr))


print("\n--- Reverse String ---")
print(reverse_string("vikhyath"))