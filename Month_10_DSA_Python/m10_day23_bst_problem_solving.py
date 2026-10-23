
from __future__ import annotations

from collections import deque
from typing import Deque


class Node:
    """A node in a binary tree."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


def insert_bst(root: Node | None, value: int) -> Node:
    """Insert a unique value into a BST."""
    if root is None:
        return Node(value)

    current = root

    while True:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                break
            current = current.left
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                break
            current = current.right
        else:
            print(f"Duplicate value {value} ignored.")
            break

    return root


def build_bst(values: list[int]) -> Node | None:
    """Build a BST by inserting values in the given order."""
    root: Node | None = None

    for value in values:
        root = insert_bst(root, value)

    return root


def read_bst() -> Node | None:
    """Read values and construct a BST."""
    values = read_integer_list(
        "Enter BST values separated by spaces: "
    )

    if not values:
        print("The BST is empty.")
        return None

    return build_bst(values)


def read_integer_list(prompt: str) -> list[int]:
    """Read a list of integers safely."""
    while True:
        try:
            text = input(prompt).strip()
            if not text:
                return []
            return [int(item) for item in text.split()]
        except ValueError:
            print("Invalid input. Please enter integers only.")


def inorder_values(root: Node | None) -> list[int]:
    """Return the inorder traversal of a tree."""
    result: list[int] = []
    stack: list[Node] = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result


def display_bst(root: Node | None) -> None:
    if root is None:
        print("Tree is empty.")
    else:
        print("Inorder traversal:", inorder_values(root))


# Program 111: Find the Inorder Predecessor
def inorder_predecessor(
    root: Node | None, target: int
) -> int | None:
    """Find the greatest value in the BST that is smaller than target."""
    predecessor: int | None = None
    current = root

    while current is not None:
        if target > current.value:
            predecessor = current.value
            current = current.right
        else:
            current = current.left

    return predecessor


def program_111() -> None:
    print("\n--- Program 111: Inorder Predecessor ---")
    root = read_bst()

    if root is None:
        return

    display_bst(root)
    target = int(input("Enter the node value: "))
    result = inorder_predecessor(root, target)

    if result is None:
        print("No inorder predecessor exists.")
    else:
        print("Inorder predecessor:", result)


# Program 112: Find the Inorder Successor
def inorder_successor(
    root: Node | None, target: int
) -> int | None:
    """Find the smallest value in the BST that is greater than target."""
    successor: int | None = None
    current = root

    while current is not None:
        if target < current.value:
            successor = current.value
            current = current.left
        else:
            current = current.right

    return successor


def program_112() -> None:
    print("\n--- Program 112: Inorder Successor ---")
    root = read_bst()

    if root is None:
        return

    display_bst(root)
    target = int(input("Enter the node value: "))
    result = inorder_successor(root, target)

    if result is None:
        print("No inorder successor exists.")
    else:
        print("Inorder successor:", result)


# Program 113: Validate Whether a Binary Tree Is a BST
def build_binary_tree_level_order(
    tokens: list[str],
) -> Node | None:
    """
    Build a binary tree from level-order tokens.
    Use N for a missing child.
    Example: 10 5 15 N N 12 20
    """
    if not tokens or tokens[0].upper() == "N":
        return None

    root = Node(int(tokens[0]))
    queue: Deque[Node] = deque([root])
    index = 1

    while queue and index < len(tokens):
        current = queue.popleft()

        if index < len(tokens):
            token = tokens[index]
            index += 1

            if token.upper() != "N":
                current.left = Node(int(token))
                queue.append(current.left)

        if index < len(tokens):
            token = tokens[index]
            index += 1

            if token.upper() != "N":
                current.right = Node(int(token))
                queue.append(current.right)

    return root


def is_valid_bst(
    root: Node | None,
    lower: int | None = None,
    upper: int | None = None,
) -> bool:
    """Validate a BST using allowed value ranges."""
    if root is None:
        return True

    if lower is not None and root.value <= lower:
        return False

    if upper is not None and root.value >= upper:
        return False

    return (
        is_valid_bst(root.left, lower, root.value)
        and is_valid_bst(root.right, root.value, upper)
    )


def program_113() -> None:
    print("\n--- Program 113: Validate a BST ---")
    print("Enter level-order values; use N for missing children.")
    print("Example: 10 5 15 N N 12 20")

    while True:
        tokens = input("Enter tree values: ").split()

        try:
            for token in tokens:
                if token.upper() != "N":
                    int(token)
            break
        except ValueError:
            print("Invalid input. Use integers or N.")

    root = build_binary_tree_level_order(tokens)

    if root is None:
        print("The tree is empty; an empty tree is a valid BST.")
        return

    if is_valid_bst(root):
        print("The binary tree is a valid BST.")
    else:
        print("The binary tree is NOT a valid BST.")


# Program 114: Find the Kth Smallest Element
def kth_smallest(root: Node | None, k: int) -> int | None:
    """Return the kth smallest value using inorder traversal."""
    if k <= 0:
        return None

    stack: list[Node] = []
    current = root
    count = 0

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        count += 1

        if count == k:
            return current.value

        current = current.right

    return None


def program_114() -> None:
    print("\n--- Program 114: Kth Smallest Element ---")
    root = read_bst()

    if root is None:
        return

    display_bst(root)
    k = int(input("Enter k: "))
    result = kth_smallest(root, k)

    if result is None:
        print("Invalid k: the tree has fewer than k nodes or k is not positive.")
    else:
        print(f"The {k}th smallest element is:", result)


# Program 115: Find the Kth Largest Element
def kth_largest(root: Node | None, k: int) -> int | None:
    """Return the kth largest value using reverse inorder traversal."""
    if k <= 0:
        return None

    stack: list[Node] = []
    current = root
    count = 0

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.right

        current = stack.pop()
        count += 1

        if count == k:
            return current.value

        current = current.left

    return None


def program_115() -> None:
    print("\n--- Program 115: Kth Largest Element ---")
    root = read_bst()

    if root is None:
        return

    display_bst(root)
    k = int(input("Enter k: "))
    result = kth_largest(root, k)

    if result is None:
        print("Invalid k: the tree has fewer than k nodes or k is not positive.")
    else:
        print(f"The {k}th largest element is:", result)


def run_all() -> None:
    program_111()
    program_112()
    program_113()
    program_114()
    program_115()


def main() -> None:
    while True:
        print("\n========== DAY 23: BST PROBLEM SOLVING ==========")
        print("111. Find Inorder Predecessor")
        print("112. Find Inorder Successor")
        print("113. Validate a Binary Search Tree")
        print("114. Find Kth Smallest Element")
        print("115. Find Kth Largest Element")
        print("116. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "111":
            program_111()
        elif choice == "112":
            program_112()
        elif choice == "113":
            program_113()
        elif choice == "114":
            program_114()
        elif choice == "115":
            program_115()
        elif choice == "116":
            run_all()
        elif choice == "0":
            print("Exiting Day 23 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 111–116 or 0.")


if __name__ == "__main__":
    main()
