
from __future__ import annotations

from collections import deque
from typing import Deque


# --------------------------------------------------
# PROGRAM 56: Generate binary numbers from 1 to N
# --------------------------------------------------

def generate_binary_numbers() -> None:
    """Generate binary representations of numbers from 1 to N."""
    n = int(input("Enter N: "))

    if n < 1:
        print("N must be at least 1.")
        return

    queue: Deque[str] = deque(["1"])
    result: list[str] = []

    for _ in range(n):
        current = queue.popleft()
        result.append(current)

        queue.append(current + "0")
        queue.append(current + "1")

    print(f"Binary numbers from 1 to {n}:")
    print(" ".join(result))


# --------------------------------------------------
# PROGRAM 57: Reverse the first K elements of a queue
# --------------------------------------------------

def reverse_first_k() -> None:
    """Reverse the first K elements while preserving the rest."""
    values = list(
        map(int, input("Enter queue elements separated by spaces: ").split())
    )
    k = int(input("Enter K: "))

    if not 0 <= k <= len(values):
        print(f"K must be between 0 and {len(values)}.")
        return

    queue: Deque[int] = deque(values)
    stack: list[int] = []

    # Move the first K elements to a stack.
    for _ in range(k):
        stack.append(queue.popleft())

    # Stack reverses their order.
    while stack:
        queue.appendleft(stack.pop())

    # Rotate the remaining original elements to the back.
    for _ in range(len(values) - k):
        queue.append(queue.popleft())

    print("Queue after reversing the first K elements:")
    print(list(queue))


# --------------------------------------------------
# PROGRAM 58: Interleave the two halves of a queue
# --------------------------------------------------

def interleave_queue() -> None:
    """Interleave the first and second halves of an even-sized queue."""
    values = list(
        map(int, input("Enter an even number of queue elements: ").split())
    )

    if len(values) % 2 != 0:
        print("The queue must contain an even number of elements.")
        return

    queue: Deque[int] = deque(values)
    half = len(queue) // 2

    first_half: Deque[int] = deque()

    for _ in range(half):
        first_half.append(queue.popleft())

    result: list[int] = []

    while first_half:
        result.append(first_half.popleft())
        result.append(queue.popleft())

    print("Interleaved queue:")
    print(result)


# --------------------------------------------------
# PROGRAM 59: Implement a deque from scratch
# --------------------------------------------------

class ArrayDeque:
    """Deque implemented using a circular array."""

    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("Capacity must be at least 1.")

        self.capacity: int = capacity
        self.data: list[int | None] = [None] * capacity
        self.front: int = 0
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def __len__(self) -> int:
        return self.size

    def add_front(self, value: int) -> bool:
        if self.is_full():
            return False

        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def add_rear(self, value: int) -> bool:
        if self.is_full():
            return False

        rear = (self.front + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1
        return True

    def remove_front(self) -> int | None:
        if self.is_empty():
            return None

        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return value

    def remove_rear(self) -> int | None:
        if self.is_empty():
            return None

        rear = (self.front + self.size - 1) % self.capacity
        value = self.data[rear]
        self.data[rear] = None
        self.size -= 1

        return value

    def peek_front(self) -> int | None:
        if self.is_empty():
            return None
        return self.data[self.front]

    def peek_rear(self) -> int | None:
        if self.is_empty():
            return None

        rear = (self.front + self.size - 1) % self.capacity
        return self.data[rear]

    def display(self) -> list[int]:
        result: list[int] = []

        for i in range(self.size):
            index = (self.front + i) % self.capacity
            value = self.data[index]

            if value is not None:
                result.append(value)

        return result


def deque_menu() -> None:
    """Interactive menu for the custom deque."""
    capacity = int(input("Enter deque capacity: "))

    if capacity < 1:
        print("Capacity must be at least 1.")
        return

    dq = ArrayDeque(capacity)

    while True:
        print("\n--- DEQUE MENU ---")
        print("1. Insert at front")
        print("2. Insert at rear")
        print("3. Remove from front")
        print("4. Remove from rear")
        print("5. Peek at front")
        print("6. Peek at rear")
        print("7. Display deque")
        print("8. Check if empty")
        print("9. Check if full")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = int(input("Enter value: "))
            if dq.add_front(value):
                print("Inserted at front.")
            else:
                print("Deque overflow: deque is full.")

        elif choice == "2":
            value = int(input("Enter value: "))
            if dq.add_rear(value):
                print("Inserted at rear.")
            else:
                print("Deque overflow: deque is full.")

        elif choice == "3":
            value = dq.remove_front()
            if value is None:
                print("Deque underflow: deque is empty.")
            else:
                print("Removed from front:", value)

        elif choice == "4":
            value = dq.remove_rear()
            if value is None:
                print("Deque underflow: deque is empty.")
            else:
                print("Removed from rear:", value)

        elif choice == "5":
            value = dq.peek_front()
            if value is None:
                print("Deque is empty.")
            else:
                print("Front element:", value)

        elif choice == "6":
            value = dq.peek_rear()
            if value is None:
                print("Deque is empty.")
            else:
                print("Rear element:", value)

        elif choice == "7":
            print("Deque:", dq.display())

        elif choice == "8":
            print("Deque is empty." if dq.is_empty() else "Deque is not empty.")

        elif choice == "9":
            print("Deque is full." if dq.is_full() else "Deque is not full.")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")


# --------------------------------------------------
# PROGRAM 60: First non-repeating character in a stream
# --------------------------------------------------

def first_non_repeating_character() -> None:
    """Print the first non-repeating character after each input character."""
    stream = input("Enter a character stream: ")

    frequency: dict[str, int] = {}
    queue: Deque[str] = deque()
    result: list[str] = []

    for char in stream:
        frequency[char] = frequency.get(char, 0) + 1
        queue.append(char)

        # Remove characters that have appeared more than once.
        while queue and frequency[queue[0]] > 1:
            queue.popleft()

        if queue:
            result.append(queue[0])
        else:
            result.append("#")

    print("Input stream:             ", " ".join(stream))
    print("First non-repeating chars:", " ".join(result))
    print("(# means no non-repeating character exists.)")


# --------------------------------------------------
# MAIN MENU: PROGRAMS 56-60
# --------------------------------------------------

def main() -> None:
    programs = {
        "56": ("Generate binary numbers from 1 to N",
               generate_binary_numbers),
        "57": ("Reverse the first K queue elements",
               reverse_first_k),
        "58": ("Interleave the two queue halves",
               interleave_queue),
        "59": ("Implement a deque from scratch",
               deque_menu),
        "60": ("First non-repeating character in a stream",
               first_non_repeating_character),
    }

    while True:
        print("\n========== MONTH 10 - DAY 12 ==========")

        for number, (description, _) in programs.items():
            print(f"{number}. {description}")

        print("61. Run all programs (56-60)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Day 12 practice completed. Keep going!")
            break

        elif choice == "61":
            for number, (description, function) in programs.items():
                print(f"\n--- Program {number}: {description} ---")
                function()

        elif choice in programs:
            description, function = programs[choice]
            print(f"\n--- Program {choice}: {description} ---")
            function()

        else:
            print("Invalid choice. Enter 56-61 or 0.")


if __name__ == "__main__":
    main()
