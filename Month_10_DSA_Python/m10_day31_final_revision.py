from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


# ============================================================
# TREE NODE
# ============================================================

@dataclass
class TreeNode:
    data: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order input. None represents a missing node."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue: list[TreeNode] = [root]
    index = 1

    while queue and index < len(values):
        current = queue.pop(0)

        if index < len(values) and values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1

        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1

    return root


def preorder(root: Optional[TreeNode]) -> list[int]:
    result: list[int] = []

    def traverse(node: Optional[TreeNode]) -> None:
        if node is None:
            return

        result.append(node.data)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return result


def display_tree_as_list(root: Optional[TreeNode]) -> None:
    print("Preorder:", preorder(root))


# ============================================================
# PROGRAM 151 — FLATTEN BINARY TREE INTO LINKED LIST
# ============================================================

def flatten_binary_tree(root: Optional[TreeNode]) -> None:
    """
    Flatten the tree in preorder using the original nodes.
    Every left pointer becomes None.
    Every right pointer points to the next preorder node.
    """

    current = root

    while current is not None:

        if current.left is not None:
            predecessor = current.left

            while predecessor.right is not None:
                predecessor = predecessor.right

            predecessor.right = current.right
            current.right = current.left
            current.left = None

        current = current.right


def program_151() -> None:
    print("\nPROGRAM 151 — FLATTEN BINARY TREE")

    values = list(
        map(
            lambda x: None if x.lower() == "null" else int(x),
            input("Enter level-order values (use null for missing nodes): ").split()
        )
    )

    root = build_tree(values)

    print("Original preorder:", preorder(root))

    flatten_binary_tree(root)

    result: list[int] = []
    current = root

    while current is not None:
        result.append(current.data)

        if current.left is not None:
            print("Error: A left pointer is not None.")
            return

        current = current.right

    print("Flattened linked list:", result)


# ============================================================
# PROGRAM 152 — DESIGN A MIN STACK
# ============================================================

class MinStack:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> Optional[int]:
        if not self.stack:
            print("Stack is empty.")
            return None

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self) -> Optional[int]:
        if not self.stack:
            print("Stack is empty.")
            return None

        return self.stack[-1]

    def get_min(self) -> Optional[int]:
        if not self.min_stack:
            print("Stack is empty.")
            return None

        return self.min_stack[-1]


def program_152() -> None:
    print("\nPROGRAM 152 — DESIGN A MIN STACK")

    stack = MinStack()

    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Top")
        print("4. Get Minimum")
        print("0. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            value = int(input("Enter value: "))
            stack.push(value)
            print(value, "pushed.")

        elif choice == "2":
            removed = stack.pop()
            if removed is not None:
                print("Popped:", removed)

        elif choice == "3":
            print("Top:", stack.top())

        elif choice == "4":
            print("Minimum:", stack.get_min())

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ============================================================
# PROGRAM 153 — LOWEST COMMON ANCESTOR IN A BST
# ============================================================

def lowest_common_ancestor(
    root: Optional[TreeNode],
    p: int,
    q: int
) -> Optional[TreeNode]:

    current = root

    while current is not None:

        if p < current.data and q < current.data:
            current = current.left

        elif p > current.data and q > current.data:
            current = current.right

        else:
            return current

    return None


def bst_contains(root: Optional[TreeNode], target: int) -> bool:
    current = root

    while current is not None:
        if target == current.data:
            return True
        elif target < current.data:
            current = current.left
        else:
            current = current.right

    return False


def program_153() -> None:
    print("\nPROGRAM 153 — LCA IN A BINARY SEARCH TREE")

    values = list(map(int, input("Enter BST values: ").split()))

    root: Optional[TreeNode] = None

    def insert(node: Optional[TreeNode], value: int) -> TreeNode:
        if node is None:
            return TreeNode(value)

        if value < node.data:
            node.left = insert(node.left, value)
        elif value > node.data:
            node.right = insert(node.right, value)

        return node

    for value in values:
        root = insert(root, value)

    p = int(input("Enter first node: "))
    q = int(input("Enter second node: "))

    if not bst_contains(root, p) or not bst_contains(root, q):
        print("One or both nodes are not present in the BST.")
        return

    ancestor = lowest_common_ancestor(root, p, q)

    if ancestor is not None:
        print("Lowest Common Ancestor:", ancestor.data)
    else:
        print("LCA not found.")


# ============================================================
# PROGRAM 154 — MERGE TWO BINARY MAX HEAPS
# ============================================================

def heapify_down(heap: list[int], size: int, index: int) -> None:
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and heap[left] > heap[largest]:
        largest = left

    if right < size and heap[right] > heap[largest]:
        largest = right

    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        heapify_down(heap, size, largest)


def build_max_heap(heap: list[int]) -> None:
    size = len(heap)

    for index in range(size // 2 - 1, -1, -1):
        heapify_down(heap, size, index)


def merge_max_heaps(heap1: list[int], heap2: list[int]) -> list[int]:
    merged = heap1 + heap2
    build_max_heap(merged)
    return merged


def program_154() -> None:
    print("\nPROGRAM 154 — MERGE TWO BINARY MAX HEAPS")

    heap1 = list(map(int, input("Enter first max heap: ").split()))
    heap2 = list(map(int, input("Enter second max heap: ").split()))

    merged = merge_max_heaps(heap1, heap2)

    print("Merged max heap:", merged)


# ============================================================
# PROGRAM 155 — DESIGN AN LFU CACHE
# ============================================================

class LFUCache:
    """
    O(1) average-time LFU cache.

    - key_to_value: stores key -> value
    - key_to_freq: stores key -> frequency
    - freq_to_keys: stores keys grouped by frequency
    - Each frequency group uses an ordered dictionary.
      The oldest key in a group is the least recently used.
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.key_to_value: dict[int, int] = {}
        self.key_to_freq: dict[int, int] = {}
        self.freq_to_keys: dict[int, dict[int, None]] = defaultdict(dict)
        self.min_freq = 0

    def _update_frequency(self, key: int) -> None:
        frequency = self.key_to_freq[key]

        # Remove key from its old frequency group.
        del self.freq_to_keys[frequency][key]

        # If this was the last key at the minimum frequency,
        # increase the minimum frequency.
        if not self.freq_to_keys[frequency]:
            del self.freq_to_keys[frequency]

            if self.min_freq == frequency:
                self.min_freq += 1

        # Move key to the next frequency group.
        new_frequency = frequency + 1
        self.key_to_freq[key] = new_frequency
        self.freq_to_keys[new_frequency][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1

        self._update_frequency(key)
        return self.key_to_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        # Update an existing key.
        if key in self.key_to_value:
            self.key_to_value[key] = value
            self._update_frequency(key)
            return

        # Evict the LFU key when the cache is full.
        if len(self.key_to_value) >= self.capacity:
            least_recent_key = next(
                iter(self.freq_to_keys[self.min_freq])
            )

            del self.freq_to_keys[self.min_freq][least_recent_key]
            del self.key_to_value[least_recent_key]
            del self.key_to_freq[least_recent_key]

            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # Insert the new key with frequency 1.
        self.key_to_value[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


def program_155() -> None:
    print("\nPROGRAM 155 — DESIGN AN LFU CACHE")

    capacity = int(input("Enter cache capacity: "))
    cache = LFUCache(capacity)

    while True:
        print("\n1. Put")
        print("2. Get")
        print("0. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            cache.put(key, value)
            print(f"Inserted/updated ({key}, {value}).")

        elif choice == "2":
            key = int(input("Enter key: "))
            print("Result:", cache.get(key))

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all() -> None:
    print("\n========== RUNNING PROGRAM 151 ==========")
    program_151()

    print("\n========== RUNNING PROGRAM 152 ==========")
    program_152()

    print("\n========== RUNNING PROGRAM 153 ==========")
    program_153()

    print("\n========== RUNNING PROGRAM 154 ==========")
    program_154()

    print("\n========== RUNNING PROGRAM 155 ==========")
    program_155()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:
    while True:
        print("\n" + "=" * 55)
        print("       MONTH 10 — DAY 31 FINAL REVISION CHALLENGE")
        print("=" * 55)

        print("151. Flatten Binary Tree into Linked List")
        print("152. Design a Min Stack")
        print("153. Lowest Common Ancestor in BST")
        print("154. Merge Two Binary Max Heaps")
        print("155. Design an LFU Cache")
        print("156. Run All Programs")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "151":
            program_151()

        elif choice == "152":
            program_152()

        elif choice == "153":
            program_153()

        elif choice == "154":
            program_154()

        elif choice == "155":
            program_155()

        elif choice == "156":
            run_all()

        elif choice == "0":
            print("\nMonth 10 Final Revision Completed!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()