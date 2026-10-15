
from __future__ import annotations

import re


# ==========================================================
# PROGRAM 71: Basic hash map using separate chaining
# ==========================================================

class ChainedHashMap:
    """Hash map that resolves collisions using separate chaining."""

    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity = capacity
        self.buckets: list[list[tuple[int, str]]] = [
            [] for _ in range(capacity)
        ]

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: str) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> str | None:
        index = self._hash(key)

        for existing_key, value in self.buckets[index]:
            if existing_key == key:
                return value

        return None

    def remove(self, key: int) -> bool:
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)
                return True

        return False

    def display(self) -> None:
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")


def program_71() -> None:
    capacity = int(input("Enter hash table capacity: "))

    if capacity <= 0:
        print("Capacity must be positive.")
        return

    hash_map = ChainedHashMap(capacity)

    while True:
        print("\n--- PROGRAM 71: SEPARATE CHAINING ---")
        print("1. Insert or update key-value pair")
        print("2. Search for a key")
        print("3. Remove a key")
        print("4. Display hash table")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            key = int(input("Enter integer key: "))
            value = input("Enter string value: ")
            hash_map.put(key, value)
            print("Key-value pair inserted/updated.")

        elif choice == "2":
            key = int(input("Enter key to search: "))
            value = hash_map.get(key)

            if value is None:
                print("Key not found.")
            else:
                print("Value:", value)

        elif choice == "3":
            key = int(input("Enter key to remove: "))
            print("Removed." if hash_map.remove(key) else "Key not found.")

        elif choice == "4":
            hash_map.display()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ==========================================================
# PROGRAM 72: Implement a hash set
# ==========================================================

class MyHashSet:
    """Hash set implemented using separate chaining."""

    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity = capacity
        self.buckets: list[list[int]] = [
            [] for _ in range(capacity)
        ]

    def _hash(self, value: int) -> int:
        return value % self.capacity

    def add(self, value: int) -> None:
        index = self._hash(value)

        if value not in self.buckets[index]:
            self.buckets[index].append(value)

    def contains(self, value: int) -> bool:
        index = self._hash(value)
        return value in self.buckets[index]

    def remove(self, value: int) -> bool:
        index = self._hash(value)
        bucket = self.buckets[index]

        if value in bucket:
            bucket.remove(value)
            return True

        return False

    def display(self) -> list[int]:
        return [
            value
            for bucket in self.buckets
            for value in bucket
        ]


def program_72() -> None:
    capacity = int(input("Enter hash set capacity: "))

    if capacity <= 0:
        print("Capacity must be positive.")
        return

    hash_set = MyHashSet(capacity)

    while True:
        print("\n--- PROGRAM 72: HASH SET ---")
        print("1. Add value")
        print("2. Check membership")
        print("3. Remove value")
        print("4. Display set")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = int(input("Enter integer value: "))
            already_exists = hash_set.contains(value)
            hash_set.add(value)

            if already_exists:
                print("Value already exists; duplicates are ignored.")
            else:
                print("Value added.")

        elif choice == "2":
            value = int(input("Enter value to search: "))
            print(hash_set.contains(value))

        elif choice == "3":
            value = int(input("Enter value to remove: "))
            print("Removed." if hash_set.remove(value) else "Value not found.")

        elif choice == "4":
            print("Hash set:", hash_set.display())

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ==========================================================
# PROGRAM 73: Hash map with put, get and remove
# ==========================================================

class MyHashMap:
    """Integer-key, integer-value hash map."""

    def __init__(self, capacity: int = 10) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        self.capacity = capacity
        self.buckets: list[list[tuple[int, int]]] = [
            [] for _ in range(capacity)
        ]

    def _hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        return -1

    def remove(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)
                return True

        return False

    def display(self) -> None:
        items = [
            pair
            for bucket in self.buckets
            for pair in bucket
        ]
        print("Key-value pairs:", items)


def program_73() -> None:
    capacity = int(input("Enter hash map capacity: "))

    if capacity <= 0:
        print("Capacity must be positive.")
        return

    hash_map = MyHashMap(capacity)

    while True:
        print("\n--- PROGRAM 73: PUT / GET / REMOVE ---")
        print("1. Put key-value pair")
        print("2. Get value")
        print("3. Remove key")
        print("4. Display map")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            hash_map.put(key, value)
            print("Value stored.")

        elif choice == "2":
            key = int(input("Enter key: "))
            value = hash_map.get(key)

            if value == -1:
                print("Key not found, or stored value is -1.")
            else:
                print("Value:", value)

        elif choice == "3":
            key = int(input("Enter key: "))
            print("Removed." if hash_map.remove(key) else "Key not found.")

        elif choice == "4":
            hash_map.display()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ==========================================================
# PROGRAM 74: Word frequency in a paragraph
# ==========================================================

def word_frequency() -> None:
    paragraph = input("Enter a paragraph: ").lower()

    # Extract words while ignoring punctuation.
    words = re.findall(r"\b\w+\b", paragraph)

    frequency: dict[str, int] = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    if not frequency:
        print("No words found.")
        return

    print("\nWord frequencies:")

    for word, count in sorted(frequency.items()):
        print(f"{word}: {count}")

    most_common = max(frequency.values())
    common_words = [
        word
        for word, count in frequency.items()
        if count == most_common
    ]

    print("\nMost frequent word(s):", ", ".join(common_words))
    print("Maximum frequency:", most_common)


# ==========================================================
# PROGRAM 75: Intersection of two arrays using a hash set
# ==========================================================

def array_intersection() -> None:
    first = list(
        map(int, input("Enter first array: ").split())
    )
    second = list(
        map(int, input("Enter second array: ").split())
    )

    second_set = set(second)

    # Keep unique common values in the order of first appearance
    # in the first array.
    result: list[int] = []
    seen: set[int] = set()

    for value in first:
        if value in second_set and value not in seen:
            result.append(value)
            seen.add(value)

    print("Intersection:", result)


# ==========================================================
# MAIN MENU: PROGRAMS 71-75
# ==========================================================

def main() -> None:
    programs = {
        "71": ("Hash map using separate chaining", program_71),
        "72": ("Implement a hash set", program_72),
        "73": ("Hash map with put, get and remove", program_73),
        "74": ("Word frequency in a paragraph", word_frequency),
        "75": ("Array intersection using a hash set", array_intersection),
    }

    while True:
        print("\n========== MONTH 10 - DAY 15 ==========")

        for number, (description, _) in programs.items():
            print(f"{number}. {description}")

        print("76. Run all programs (71-75)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Day 15 practice completed!")
            break

        elif choice == "76":
            for number, (description, function) in programs.items():
                print(f"\n--- Program {number}: {description} ---")
                function()

        elif choice in programs:
            description, function = programs[choice]
            print(f"\n--- Program {choice}: {description} ---")
            function()

        else:
            print("Invalid choice. Enter 71-76 or 0.")


if __name__ == "__main__":
    main()
