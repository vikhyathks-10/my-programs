
from __future__ import annotations

import random


# Shared Trie Node
class TrieNode:
    """A node in a trie."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word = False


class Trie:
    """Trie supporting insertion, exact search, and prefix search."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]

        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]

        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root

        for character in prefix:
            if character not in node.children:
                return False
            node = node.children[character]

        return True


# Program 136: Trie with Insert and Exact Search
def program_136() -> None:
    print("\n--- Program 136: Trie Insert and Search ---")
    trie = Trie()

    while True:
        print("\n1. Insert word")
        print("2. Search exact word")
        print("3. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            word = input("Enter word to insert: ").strip()

            if not word:
                print("Please enter a non-empty word.")
            else:
                trie.insert(word)
                print(f"Inserted '{word}'.")

        elif choice == "2":
            word = input("Enter word to search: ").strip()

            if trie.search(word):
                print(f"'{word}' exists in the trie.")
            else:
                print(f"'{word}' was not found.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")


# Program 137: Trie with Prefix Search
def program_137() -> None:
    print("\n--- Program 137: Trie Prefix Search ---")
    trie = Trie()

    print("Insert some words first.")
    words = input("Enter words separated by spaces: ").split()

    for word in words:
        trie.insert(word)

    while True:
        print("\n1. Insert another word")
        print("2. Search for a prefix")
        print("3. Search for an exact word")
        print("4. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            word = input("Enter word: ").strip()

            if not word:
                print("Please enter a non-empty word.")
            else:
                trie.insert(word)
                print(f"Inserted '{word}'.")

        elif choice == "2":
            prefix = input("Enter prefix: ").strip()

            if trie.starts_with(prefix):
                print(f"A word with prefix '{prefix}' exists.")
            else:
                print(f"No word starts with '{prefix}'.")

        elif choice == "3":
            word = input("Enter complete word: ").strip()

            if trie.search(word):
                print(f"'{word}' exists in the trie.")
            else:
                print(f"'{word}' was not found.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


# Program 138: Word Dictionary with Wildcard Search
class WordDictionary:
    """
    Store words in a trie.
    The '.' character matches any one character.
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root

        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()
            node = node.children[character]

        node.is_end_of_word = True

    def search(self, pattern: str) -> bool:
        def search_from(node: TrieNode, index: int) -> bool:
            if index == len(pattern):
                return node.is_end_of_word

            character = pattern[index]

            if character == ".":
                for child in node.children.values():
                    if search_from(child, index + 1):
                        return True
                return False

            child = node.children.get(character)

            if child is None:
                return False

            return search_from(child, index + 1)

        return search_from(self.root, 0)


def program_138() -> None:
    print("\n--- Program 138: Wildcard Word Dictionary ---")
    dictionary = WordDictionary()

    while True:
        print("\n1. Add word")
        print("2. Search word or pattern")
        print("3. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            word = input("Enter word to add: ").strip()

            if not word or "." in word:
                print("Enter a non-empty word without '.' wildcards.")
            else:
                dictionary.add_word(word)
                print(f"Added '{word}'.")

        elif choice == "2":
            pattern = input(
                "Enter search pattern (use '.' for any one character): "
            ).strip()

            if dictionary.search(pattern):
                print(f"Pattern '{pattern}' matches a word.")
            else:
                print(f"No word matches '{pattern}'.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")


# Program 139: Queue Using a Circular Linked List
class CircularNode:
    """A node in a circular linked list."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.next: CircularNode = self


class CircularLinkedQueue:
    """FIFO queue implemented using a circular singly linked list."""

    def __init__(self) -> None:
        self.rear: CircularNode | None = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.rear is None

    def enqueue(self, value: int) -> None:
        new_node = CircularNode(value)

        if self.rear is None:
            self.rear = new_node
        else:
            new_node.next = self.rear.next
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self) -> int | None:
        if self.rear is None:
            return None

        front = self.rear.next
        value = front.value

        if front is self.rear:
            self.rear = None
        else:
            self.rear.next = front.next

        self.size -= 1
        return value

    def peek(self) -> int | None:
        if self.rear is None:
            return None
        return self.rear.next.value

    def to_list(self) -> list[int]:
        values: list[int] = []

        if self.rear is None:
            return values

        current = self.rear.next

        while True:
            values.append(current.value)

            if current is self.rear:
                break

            current = current.next

        return values

    def display(self) -> None:
        print("Queue (front to rear):", self.to_list())


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def program_139() -> None:
    print("\n--- Program 139: Queue Using Circular Linked List ---")
    queue = CircularLinkedQueue()

    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Peek at front")
        print("4. Display queue")
        print("5. Check if empty")
        print("0. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = read_integer("Enter value to enqueue: ")
            queue.enqueue(value)
            print("Value added.")
            queue.display()

        elif choice == "2":
            value = queue.dequeue()

            if value is None:
                print("Queue is empty. Nothing to dequeue.")
            else:
                print("Dequeued value:", value)
                queue.display()

        elif choice == "3":
            value = queue.peek()

            if value is None:
                print("Queue is empty.")
            else:
                print("Front value:", value)

        elif choice == "4":
            queue.display()

        elif choice == "5":
            print("Queue empty:", queue.is_empty())

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")


# Program 140: Insert, Delete, and Get Random in Average O(1)
class RandomizedSet:
    """
    Maintain unique integers.
    A list supports random indexing, and a dictionary maps values to indices.
    """

    def __init__(self) -> None:
        self.values: list[int] = []
        self.indices: dict[int, int] = {}

    def insert(self, value: int) -> bool:
        """Insert a value; return False if it already exists."""
        if value in self.indices:
            return False

        self.indices[value] = len(self.values)
        self.values.append(value)
        return True

    def remove(self, value: int) -> bool:
        """Remove a value using swap-with-last deletion."""
        if value not in self.indices:
            return False

        index = self.indices[value]
        last_value = self.values[-1]

        self.values[index] = last_value
        self.indices[last_value] = index

        self.values.pop()
        del self.indices[value]

        return True

    def get_random(self) -> int | None:
        """Return a uniformly random stored value, or None if empty."""
        if not self.values:
            return None

        return random.choice(self.values)

    def display(self) -> None:
        print("Stored values:", self.values)


def program_140() -> None:
    print("\n--- Program 140: Randomized Set ---")
    data = RandomizedSet()

    while True:
        print("\n1. Insert value")
        print("2. Delete value")
        print("3. Get random value")
        print("4. Display values")
        print("0. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = read_integer("Enter value to insert: ")

            if data.insert(value):
                print("Value inserted.")
            else:
                print("Value already exists.")

        elif choice == "2":
            value = read_integer("Enter value to delete: ")

            if data.remove(value):
                print("Value deleted.")
            else:
                print("Value does not exist.")

        elif choice == "3":
            value = data.get_random()

            if value is None:
                print("The data structure is empty.")
            else:
                print("Random value:", value)

        elif choice == "4":
            data.display()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")


def run_all() -> None:
    program_136()
    program_137()
    program_138()
    program_139()
    program_140()


def main() -> None:
    while True:
        print("\n====== DAY 28: MIXED DATA STRUCTURES ======")
        print("136. Trie: Insert and Exact Search")
        print("137. Trie: Prefix Search")
        print("138. Word Dictionary: Wildcard Search")
        print("139. Queue Using Circular Linked List")
        print("140. Randomized Set")
        print("141. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "136":
            program_136()
        elif choice == "137":
            program_137()
        elif choice == "138":
            program_138()
        elif choice == "139":
            program_139()
        elif choice == "140":
            program_140()
        elif choice == "141":
            run_all()
        elif choice == "0":
            print("Exiting Day 28 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 136–141 or 0.")


if __name__ == "__main__":
    main()
