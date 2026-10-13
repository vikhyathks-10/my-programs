
from __future__ import annotations

from collections import OrderedDict, deque
from typing import Deque


# ==========================================================
# PROGRAM 61: Implement a deque using a circular array
# ==========================================================

class ArrayDeque:
    """A deque implemented from scratch using a circular array."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity = capacity
        self.data: list[int | None] = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def __len__(self) -> int:
        return self.size

    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False

        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insert_rear(self, value: int) -> bool:
        if self.is_full():
            return False

        rear = (self.front + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1
        return True

    def delete_front(self) -> int | None:
        if self.is_empty():
            return None

        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def delete_rear(self) -> int | None:
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


def program_61() -> None:
    capacity = int(input("Enter deque capacity: "))

    if capacity <= 0:
        print("Capacity must be positive.")
        return

    dq = ArrayDeque(capacity)

    while True:
        print("\n--- PROGRAM 61: CIRCULAR ARRAY DEQUE ---")
        print("1. Insert at front")
        print("2. Insert at rear")
        print("3. Delete from front")
        print("4. Delete from rear")
        print("5. Peek at front")
        print("6. Peek at rear")
        print("7. Display deque")
        print("8. Check empty/full")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = int(input("Enter value: "))
            print("Inserted." if dq.insert_front(value) else "Deque is full.")

        elif choice == "2":
            value = int(input("Enter value: "))
            print("Inserted." if dq.insert_rear(value) else "Deque is full.")

        elif choice == "3":
            value = dq.delete_front()
            print("Deleted:", value) if value is not None else print("Deque is empty.")

        elif choice == "4":
            value = dq.delete_rear()
            print("Deleted:", value) if value is not None else print("Deque is empty.")

        elif choice == "5":
            value = dq.peek_front()
            print("Front:", value) if value is not None else print("Deque is empty.")

        elif choice == "6":
            value = dq.peek_rear()
            print("Rear:", value) if value is not None else print("Deque is empty.")

        elif choice == "7":
            print("Deque:", dq.display())

        elif choice == "8":
            print("Empty:", dq.is_empty())
            print("Full:", dq.is_full())

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ==========================================================
# PROGRAM 62: Maximum of every sliding window
# ==========================================================

def sliding_window_maximum() -> None:
    values = list(
        map(int, input("Enter array elements: ").split())
    )
    k = int(input("Enter window size K: "))

    if not values:
        print("Array cannot be empty.")
        return

    if not 1 <= k <= len(values):
        print("K must be between 1 and the array length.")
        return

    # Store indices in decreasing order of their values.
    candidates: Deque[int] = deque()
    result: list[int] = []

    for i, value in enumerate(values):
        # Remove indices outside the current window.
        while candidates and candidates[0] <= i - k:
            candidates.popleft()

        # Remove smaller or equal values from the rear.
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()

        candidates.append(i)

        if i >= k - 1:
            result.append(values[candidates[0]])

    print("Window maximums:", result)


# ==========================================================
# PROGRAM 63: Minimum of every sliding window
# ==========================================================

def sliding_window_minimum() -> None:
    values = list(
        map(int, input("Enter array elements: ").split())
    )
    k = int(input("Enter window size K: "))

    if not values:
        print("Array cannot be empty.")
        return

    if not 1 <= k <= len(values):
        print("K must be between 1 and the array length.")
        return

    # Store indices in increasing order of their values.
    candidates: Deque[int] = deque()
    result: list[int] = []

    for i, value in enumerate(values):
        # Remove indices outside the current window.
        while candidates and candidates[0] <= i - k:
            candidates.popleft()

        # Remove larger or equal values from the rear.
        while candidates and values[candidates[-1]] >= value:
            candidates.pop()

        candidates.append(i)

        if i >= k - 1:
            result.append(values[candidates[0]])

    print("Window minimums:", result)


# ==========================================================
# PROGRAM 64: Design a circular deque
# ==========================================================

class MyCircularDeque:
    """Circular deque with insert/delete operations."""

    def __init__(self, k: int) -> None:
        if k <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity = k
        self.data: list[int | None] = [None] * k
        self.front = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        rear = (self.front + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        rear = (self.front + self.size - 1) % self.capacity
        self.data[rear] = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        value = self.data[self.front]
        return value if value is not None else -1

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        rear = (self.front + self.size - 1) % self.capacity
        value = self.data[rear]
        return value if value is not None else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

    def display(self) -> list[int]:
        result: list[int] = []

        for i in range(self.size):
            index = (self.front + i) % self.capacity
            value = self.data[index]

            if value is not None:
                result.append(value)

        return result


def program_64() -> None:
    capacity = int(input("Enter circular deque capacity: "))

    if capacity <= 0:
        print("Capacity must be positive.")
        return

    dq = MyCircularDeque(capacity)

    while True:
        print("\n--- PROGRAM 64: CIRCULAR DEQUE ---")
        print("1. Insert front")
        print("2. Insert rear")
        print("3. Delete front")
        print("4. Delete rear")
        print("5. Get front")
        print("6. Get rear")
        print("7. Is empty?")
        print("8. Is full?")
        print("9. Display")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = int(input("Enter value: "))
            print(dq.insertFront(value))

        elif choice == "2":
            value = int(input("Enter value: "))
            print(dq.insertLast(value))

        elif choice == "3":
            print(dq.deleteFront())

        elif choice == "4":
            print(dq.deleteLast())

        elif choice == "5":
            print("Front:", dq.getFront())

        elif choice == "6":
            print("Rear:", dq.getRear())

        elif choice == "7":
            print(dq.isEmpty())

        elif choice == "8":
            print(dq.isFull())

        elif choice == "9":
            print("Deque:", dq.display())

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ==========================================================
# PROGRAM 65: LRU cache using OrderedDict
# ==========================================================

class LRUCache:
    """
    Least Recently Used cache.

    The least recently used item is at the beginning.
    The most recently used item is at the end.
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Cache capacity must be positive.")

        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Mark this key as most recently used.
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return

        if len(self.cache) == self.capacity:
            # Evict the least recently used item.
            self.cache.popitem(last=False)

        self.cache[key] = value

    def display(self) -> None:
        print("Cache from least to most recently used:")
        print(list(self.cache.items()))


def program_65() -> None:
    capacity = int(input("Enter LRU cache capacity: "))

    if capacity <= 0:
        print("Capacity must be positive.")
        return

    cache = LRUCache(capacity)

    while True:
        print("\n--- PROGRAM 65: LRU CACHE ---")
        print("1. Get value by key")
        print("2. Put key-value pair")
        print("3. Display cache")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            key = int(input("Enter key: "))
            value = cache.get(key)

            if value == -1:
                print("Key not found.")
            else:
                print("Value:", value)

        elif choice == "2":
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            cache.put(key, value)
            print("Cache updated.")

        elif choice == "3":
            cache.display()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ==========================================================
# MAIN MENU: PROGRAMS 61-65
# ==========================================================

def main() -> None:
    programs = {
        "61": ("Deque using a circular array", program_61),
        "62": ("Sliding window maximum", sliding_window_maximum),
        "63": ("Sliding window minimum", sliding_window_minimum),
        "64": ("Circular deque with insert/delete", program_64),
        "65": ("LRU cache", program_65),
    }

    while True:
        print("\n========== MONTH 10 - DAY 13 ==========")

        for number, (description, _) in programs.items():
            print(f"{number}. {description}")

        print("66. Run all programs (61-65)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Day 13 practice completed!")
            break

        elif choice == "66":
            for number, (description, function) in programs.items():
                print(f"\n--- Program {number}: {description} ---")
                function()

        elif choice in programs:
            description, function = programs[choice]
            print(f"\n--- Program {choice}: {description} ---")
            function()

        else:
            print("Invalid choice. Enter 61-66 or 0.")


if __name__ == "__main__":
    main()

