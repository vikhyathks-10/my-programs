
# MONTH 10 - DAY 11
# Queue Fundamentals
# Programs 51-55

from __future__ import annotations

from collections import deque


# =========================================================
# PROGRAM 51: QUEUE USING PYTHON LIST
# =========================================================
class ListQueue:
    def __init__(self):
        self.items: list[int] = []

    def enqueue(self, value: int) -> None:
        self.items.append(value)

    def dequeue(self) -> int | None:
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self) -> int | None:
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def display(self) -> None:
        print("Queue (front -> rear):", self.items)


# =========================================================
# NODE CLASS FOR LINKED-LIST QUEUE
# =========================================================
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


# =========================================================
# PROGRAM 52: QUEUE USING LINKED LIST
# =========================================================
class LinkedListQueue:
    def __init__(self):
        self.front: Node | None = None
        self.rear: Node | None = None

    def enqueue(self, value: int) -> None:
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self) -> int | None:
        if self.front is None:
            return None

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek(self) -> int | None:
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self) -> bool:
        return self.front is None

    def display(self) -> None:
        if self.front is None:
            print("Queue is empty.")
            return

        current: Node | None = self.front
        print("Queue (front -> rear):", end=" ")

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# =========================================================
# PROGRAM 53: CIRCULAR QUEUE USING ARRAY
# =========================================================
class CircularQueue:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity = capacity
        self.items: list[int | None] = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            print("Queue Overflow: circular queue is full.")
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = value
        self.size += 1
        return True

    def dequeue(self) -> int | None:
        if self.is_empty():
            return None

        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        if self.size == 0:
            self.front = 0
            self.rear = -1

        return value

    def peek(self) -> int | None:
        if self.is_empty():
            return None
        return self.items[self.front]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def display(self) -> None:
        if self.is_empty():
            print("Circular queue is empty.")
            return

        values = [
            self.items[(self.front + i) % self.capacity]
            for i in range(self.size)
        ]

        print("Circular queue (front -> rear):", values)
        print(f"Size: {self.size}/{self.capacity}")


# =========================================================
# PROGRAM 54: QUEUE USING TWO STACKS
# =========================================================
class QueueUsingStacks:
    def __init__(self):
        self.input_stack: list[int] = []
        self.output_stack: list[int] = []

    def enqueue(self, value: int) -> None:
        self.input_stack.append(value)

    def _transfer(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

    def dequeue(self) -> int | None:
        self._transfer()

        if not self.output_stack:
            return None

        return self.output_stack.pop()

    def peek(self) -> int | None:
        self._transfer()

        if not self.output_stack:
            return None

        return self.output_stack[-1]

    def is_empty(self) -> bool:
        return not self.input_stack and not self.output_stack

    def display(self) -> None:
        values = list(reversed(self.output_stack)) + self.input_stack
        print("Queue (front -> rear):", values)


# =========================================================
# PROGRAM 55: STACK USING TWO QUEUES
# =========================================================
class StackUsingQueues:
    def __init__(self):
        self.primary: deque[int] = deque()
        self.secondary: deque[int] = deque()

    def push(self, value: int) -> None:
        self.secondary.append(value)

        while self.primary:
            self.secondary.append(self.primary.popleft())

        self.primary, self.secondary = self.secondary, self.primary

    def pop(self) -> int | None:
        if not self.primary:
            return None
        return self.primary.popleft()

    def peek(self) -> int | None:
        if not self.primary:
            return None
        return self.primary[0]

    def is_empty(self) -> bool:
        return not self.primary

    def display(self) -> None:
        print("Stack (top -> bottom):", list(self.primary))


# =========================================================
# GENERIC INTERACTIVE MENU FOR QUEUE CLASSES
# =========================================================
def queue_menu(queue, title: str, circular: bool = False) -> None:
    while True:
        print(f"\n--- {title} ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek front")
        print("4. Check if empty")
        print("5. Display")
        if circular:
            print("6. Check if full")
            print("7. Back to main menu")
        else:
            print("6. Back to main menu")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                value = int(input("Enter value: "))
                result = queue.enqueue(value)

                if result is None:
                    print("Enqueued successfully.")

            elif choice == 2:
                value = queue.dequeue()
                if value is None:
                    print("Queue is empty. Nothing to dequeue.")
                else:
                    print("Dequeued:", value)

            elif choice == 3:
                value = queue.peek()
                if value is None:
                    print("Queue is empty.")
                else:
                    print("Front element:", value)

            elif choice == 4:
                print("Queue is empty:", queue.is_empty())

            elif choice == 5:
                queue.display()

            elif circular and choice == 6:
                print("Queue is full:", queue.is_full())

            elif (circular and choice == 7) or (
                not circular and choice == 6
            ):
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid integers.")


# =========================================================
# MENU FOR STACK USING TWO QUEUES
# =========================================================
def stack_menu(stack: StackUsingQueues) -> None:
    while True:
        print("\n--- STACK USING TWO QUEUES ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Display")
        print("6. Back to main menu")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                value = int(input("Enter value: "))
                stack.push(value)
                print("Pushed:", value)

            elif choice == 2:
                value = stack.pop()
                if value is None:
                    print("Stack is empty. Nothing to pop.")
                else:
                    print("Popped:", value)

            elif choice == 3:
                value = stack.peek()
                if value is None:
                    print("Stack is empty.")
                else:
                    print("Top element:", value)

            elif choice == 4:
                print("Stack is empty:", stack.is_empty())

            elif choice == 5:
                stack.display()

            elif choice == 6:
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid integers.")


# =========================================================
# MAIN MENU
# =========================================================
def main() -> None:
    list_queue = ListQueue()
    linked_queue = LinkedListQueue()
    two_stack_queue = QueueUsingStacks()
    two_queue_stack = StackUsingQueues()
    circular_queue: CircularQueue | None = None

    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 11: QUEUE FUNDAMENTALS")
        print("======================================")
        print("51. Queue using Python list")
        print("52. Queue using linked list")
        print("53. Circular queue using array")
        print("54. Queue using two stacks")
        print("55. Stack using two queues")
        print("56. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 51:
                queue_menu(list_queue, "QUEUE USING PYTHON LIST")

            elif choice == 52:
                queue_menu(linked_queue, "QUEUE USING LINKED LIST")

            elif choice == 53:
                if circular_queue is None:
                    try:
                        capacity = int(input("Enter circular queue capacity: "))
                        circular_queue = CircularQueue(capacity)
                    except ValueError as error:
                        print("Invalid capacity:", error)
                        continue

                queue_menu(
                    circular_queue,
                    "CIRCULAR QUEUE USING ARRAY",
                    circular=True
                )

            elif choice == 54:
                queue_menu(two_stack_queue, "QUEUE USING TWO STACKS")

            elif choice == 55:
                stack_menu(two_queue_stack)

            elif choice == 56:
                print("Exiting Month 10 - Day 11. Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Please enter a valid menu number.")


if __name__ == "__main__":
    main()
