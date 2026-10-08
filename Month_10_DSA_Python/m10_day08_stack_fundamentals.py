# MONTH 10 - DAY 8
# Stack Fundamentals
# Programs 36-40

from __future__ import annotations


# =========================================================
# STACK USING PYTHON LIST
# =========================================================
class ArrayStack:
    def __init__(self):
        self.stack: list[int] = []

    # Push
    def push(self, value: int) -> None:
        self.stack.append(value)

    # Pop
    def pop(self) -> int | None:
        if self.is_empty():
            return None

        return self.stack.pop()

    # Peek
    def peek(self) -> int | None:
        if self.is_empty():
            return None

        return self.stack[-1]

    # isEmpty
    def is_empty(self) -> bool:
        return len(self.stack) == 0

    # Display
    def display(self) -> None:
        if self.is_empty():
            print("Stack is empty.")
            return

        print("Stack:", self.stack)
        print("Top:", self.stack[-1])


# =========================================================
# NODE CLASS FOR LINKED-LIST STACK
# =========================================================
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


# =========================================================
# STACK USING LINKED LIST
# =========================================================
class LinkedStack:
    def __init__(self):
        self.top: Node | None = None

    # Push
    def push(self, value: int) -> None:
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

    # Pop
    def pop(self) -> int | None:
        if self.is_empty():
            return None

        if self.top is None:
            return None

        value = self.top.data
        self.top = self.top.next

        return value

    # Peek
    def peek(self) -> int | None:
        if self.is_empty():
            return None

        if self.top is None:
            return None

        return self.top.data

    # isEmpty
    def is_empty(self) -> bool:
        return self.top is None

    # Display
    def display(self) -> None:
        if self.is_empty():
            print("Stack is empty.")
            return

        current: Node | None = self.top

        print("Stack (Top -> Bottom):", end=" ")

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# =========================================================
# PROGRAM 36
# IMPLEMENT STACK USING PYTHON LIST
# =========================================================
def program_36() -> None:
    stack = ArrayStack()

    values = list(map(
        int,
        input("Enter stack elements separated by spaces: ").split()
    ))

    for value in values:
        stack.push(value)

    print("\nStack created using Python list:")
    stack.display()


# =========================================================
# PROGRAM 37
# IMPLEMENT STACK USING LINKED LIST
# =========================================================
def program_37() -> None:
    stack = LinkedStack()

    values = list(map(
        int,
        input("Enter stack elements separated by spaces: ").split()
    ))

    for value in values:
        stack.push(value)

    print("\nStack created using linked list:")
    stack.display()


# =========================================================
# PROGRAM 38
# PUSH, POP, PEEK AND ISEMPTY
# =========================================================
def program_38() -> None:
    stack = ArrayStack()

    while True:
        print("\n--------------------------------------")
        print("STACK OPERATIONS")
        print("--------------------------------------")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. isEmpty")
        print("5. Display")
        print("6. Back to main menu")
        print("--------------------------------------")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            value = int(input("Enter value to push: "))
            stack.push(value)
            print("Value pushed successfully.")

        elif choice == 2:
            value = stack.pop()

            if value is None:
                print("Stack Underflow. Stack is empty.")
            else:
                print("Popped value:", value)

        elif choice == 3:
            value = stack.peek()

            if value is None:
                print("Stack is empty.")
            else:
                print("Top element:", value)

        elif choice == 4:
            if stack.is_empty():
                print("Stack is empty: True")
            else:
                print("Stack is empty: False")

        elif choice == 5:
            stack.display()

        elif choice == 6:
            break

        else:
            print("Invalid choice.")


# =========================================================
# PROGRAM 39
# REVERSE STRING USING STACK
# =========================================================
def reverse_string_using_stack(text: str) -> str:
    stack: list[str] = []

    # Push every character
    for character in text:
        stack.append(character)

    reversed_text = ""

    # Pop every character
    while stack:
        reversed_text += stack.pop()

    return reversed_text


def program_39() -> None:
    text = input("Enter a string: ")

    reversed_text = reverse_string_using_stack(text)

    print("Original string:", text)
    print("Reversed string:", reversed_text)


# =========================================================
# PROGRAM 40
# CHECK BALANCED PARENTHESES
# =========================================================
def is_balanced(expression: str) -> bool:
    stack: list[str] = []

    opening = "([{"
    closing = ")]}"

    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in expression:

        # Opening bracket
        if character in opening:
            stack.append(character)

        # Closing bracket
        elif character in closing:

            if not stack:
                return False

            if stack[-1] != matching[character]:
                return False

            stack.pop()

    return len(stack) == 0


def program_40() -> None:
    expression = input("Enter an expression: ")

    if is_balanced(expression):
        print("Parentheses are balanced.")
    else:
        print("Parentheses are NOT balanced.")


# =========================================================
# MAIN MENU
# =========================================================
def main() -> None:

    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 8")
        print(" STACK FUNDAMENTALS")
        print("======================================")
        print("36. Implement stack using Python list")
        print("37. Implement stack using linked list")
        print("38. Push, Pop, Peek and isEmpty")
        print("39. Reverse string using stack")
        print("40. Check balanced parentheses")
        print("41. Run all programs")
        print("42. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        try:

            if choice == 36:
                program_36()

            elif choice == 37:
                program_37()

            elif choice == 38:
                program_38()

            elif choice == 39:
                program_39()

            elif choice == 40:
                program_40()

            elif choice == 41:

                print("\n========== PROGRAM 36 ==========")
                program_36()

                print("\n========== PROGRAM 37 ==========")
                program_37()

                print("\n========== PROGRAM 38 ==========")
                program_38()

                print("\n========== PROGRAM 39 ==========")
                program_39()

                print("\n========== PROGRAM 40 ==========")
                program_40()

            elif choice == 42:
                print("Exiting Month 10 - Day 8.")
                print("Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter integers only.")


# =========================================================
# PROGRAM START
# =========================================================
if __name__ == "__main__":
    main()