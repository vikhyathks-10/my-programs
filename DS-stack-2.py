# 6. Next Greater Element
def next_greater(arr):
    st = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while st and arr[i] > arr[st[-1]]:
            result[st.pop()] = arr[i]
        st.append(i)
    return result

# 7. Evaluate postfix expression
def evaluate_postfix(expr):
    st = []

    for ch in expr.split():
        if ch.isdigit():
            st.append(int(ch))
        else:
            b = st.pop()
            a = st.pop()
            if ch == '+': st.append(a + b)
            elif ch == '-': st.append(a - b)
            elif ch == '*': st.append(a * b)
            elif ch == '/': st.append(a // b)
    return st[0]

# 8. Infix to Postfix conversion
def infix_to_postfix(expr):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    st = []
    postfix = ""

    for ch in expr:
        if ch.isalnum():
            postfix += ch
        elif ch == '(':
            st.append(ch)
        elif ch == ')':
            while st and st[-1] != '(':
                postfix += st.pop()
            st.pop()
        else:
            while st and st[-1] != '(' and precedence[ch] <= precedence[st[-1]]:
                postfix += st.pop()
            st.append(ch)

    while st:
        postfix += st.pop()

    return postfix

# 9. Minimum element in stack in O(1)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        return self.min_stack[-1]

# 10. Sort a stack using recursion
def sorted_insert(stack, x):
    if not stack or x > stack[-1]:
        stack.append(x)
        return
    temp = stack.pop()
    sorted_insert(stack, x)
    stack.append(temp)

def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)


# --------- Testing ----------
arr = [4, 5, 2, 25]
print(next_greater(arr))
print(evaluate_postfix("2 3 1 * + 9 -"))
print(infix_to_postfix("A*(B+C)"))
