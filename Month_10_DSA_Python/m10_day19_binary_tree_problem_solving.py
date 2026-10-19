
from __future__ import annotations

from collections import deque
from typing import Deque


# ==========================================================
# BINARY TREE NODE
# ==========================================================

class Node:
    """Represents one node in a binary tree."""

    def __init__(
        self,
        data: int,
        left: Node | None = None,
        right: Node | None = None,
    ) -> None:
        self.data = data
        self.left = left
        self.right = right


# ==========================================================
# HELPER: BUILD A BINARY TREE
# ==========================================================

def build_tree(values: list[str]) -> Node | None:
    """
    Build a binary tree from level-order input.
    Use N for a missing child.

    Example: 1 2 3 4 5 N 6
    """
    if not values:
        return None

    if values[0].upper() == "N":
        if len(values) > 1:
            raise ValueError("An empty tree cannot have additional nodes.")
        return None

    root = Node(int(values[0]))
    queue: Deque[Node] = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()

        token = values[index]
        index += 1

        if token.upper() != "N":
            current.left = Node(int(token))
            queue.append(current.left)

        if index < len(values):
            token = values[index]
            index += 1

            if token.upper() != "N":
                current.right = Node(int(token))
                queue.append(current.right)

    if index < len(values):
        raise ValueError("Some values have no valid parent in the tree.")

    return root


def read_tree() -> Node | None:
    print("Enter tree nodes in level-order.")
    print("Use N for a missing child. Example: 1 2 3 4 5 N 6")
    values = input("Tree: ").split()
    return build_tree(values)


def display_tree(root: Node | None) -> None:
    if root is None:
        print("Tree is empty.")
        return

    queue: Deque[Node] = deque([root])
    result: list[int] = []

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    print("Tree level-order:", result)


# ==========================================================
# PROGRAM 91: Find the diameter of a binary tree
# Diameter is measured in EDGES.
# ==========================================================

def tree_diameter(root: Node | None) -> int:
    diameter = 0

    def height(node: Node | None) -> int:
        nonlocal diameter

        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        # Longest path through this node, measured in edges.
        diameter = max(diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return diameter


def program_91(root: Node | None) -> None:
    print("Tree diameter (number of edges):", tree_diameter(root))


# ==========================================================
# PROGRAM 92: Check whether a binary tree is height-balanced
# ==========================================================

def is_height_balanced(root: Node | None) -> bool:
    """
    A tree is balanced when every node's subtree heights
    differ by at most 1.
    Returns -1 from the helper as soon as imbalance is found.
    """

    def check_height(node: Node | None) -> int:
        if node is None:
            return 0

        left_height = check_height(node.left)

        if left_height == -1:
            return -1

        right_height = check_height(node.right)

        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return check_height(root) != -1


def program_92(root: Node | None) -> None:
    if is_height_balanced(root):
        print("The binary tree is height-balanced.")
    else:
        print("The binary tree is NOT height-balanced.")


# ==========================================================
# PROGRAM 93: Lowest common ancestor in a binary tree
# ==========================================================

def contains(root: Node | None, target: int) -> bool:
    if root is None:
        return False

    if root.data == target:
        return True

    return (
        contains(root.left, target)
        or contains(root.right, target)
    )


def find_lca(
    root: Node | None,
    first_value: int,
    second_value: int,
) -> Node | None:
    """
    Return the lowest common ancestor.
    This function assumes both target values exist in the tree.
    """

    if root is None:
        return None

    if root.data == first_value or root.data == second_value:
        return root

    left_result = find_lca(root.left, first_value, second_value)
    right_result = find_lca(root.right, first_value, second_value)

    if left_result is not None and right_result is not None:
        return root

    if left_result is not None:
        return left_result

    return right_result


def program_93(root: Node | None) -> None:
    if root is None:
        print("Cannot find an LCA in an empty tree.")
        return

    first_value = int(input("Enter the first node value: "))
    second_value = int(input("Enter the second node value: "))

    if not contains(root, first_value):
        print(f"Node {first_value} does not exist in the tree.")
        return

    if not contains(root, second_value):
        print(f"Node {second_value} does not exist in the tree.")
        return

    ancestor = find_lca(root, first_value, second_value)

    if ancestor is not None:
        print("Lowest common ancestor:", ancestor.data)
    else:
        print("Lowest common ancestor not found.")


# ==========================================================
# PROGRAM 94: Find the left view of a binary tree
# ==========================================================

def left_view(root: Node | None) -> list[int]:
    if root is None:
        return []

    result: list[int] = []
    queue: Deque[Node] = deque([root])

    while queue:
        level_size = len(queue)

        for index in range(level_size):
            current = queue.popleft()

            # The first node at each level is visible from the left.
            if index == 0:
                result.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

    return result


def program_94(root: Node | None) -> None:
    print("Left view:", left_view(root))


# ==========================================================
# PROGRAM 95: Find the right view of a binary tree
# ==========================================================

def right_view(root: Node | None) -> list[int]:
    if root is None:
        return []

    result: list[int] = []
    queue: Deque[Node] = deque([root])

    while queue:
        level_size = len(queue)

        for index in range(level_size):
            current = queue.popleft()

            # The last node at each level is visible from the right.
            if index == level_size - 1:
                result.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

    return result


def program_95(root: Node | None) -> None:
    print("Right view:", right_view(root))


# ==========================================================
# MAIN MENU: PROGRAMS 91-95
# ==========================================================

def main() -> None:
    root: Node | None = None
    tree_created = False

    programs = {
        "91": ("Find tree diameter", program_91),
        "92": ("Check whether the tree is balanced", program_92),
        "93": ("Find lowest common ancestor", program_93),
        "94": ("Find left view", program_94),
        "95": ("Find right view", program_95),
    }

    while True:
        print("\n========== MONTH 10 - DAY 19 ==========")
        print("91. Find tree diameter")
        print("92. Check whether tree is height-balanced")
        print("93. Find lowest common ancestor")
        print("94. Find left view")
        print("95. Find right view")
        print("96. Run all programs (91-95)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Day 19 practice completed!")
            break

        elif choice == "96":
            try:
                root = read_tree()
                tree_created = True

                print("\nCreated tree:")
                display_tree(root)

                for number, (description, function) in programs.items():
                    print(f"\n--- Program {number}: {description} ---")
                    function(root)

            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "91":
            if not tree_created:
                try:
                    root = read_tree()
                    tree_created = True
                    display_tree(root)
                except ValueError as error:
                    print("Invalid input:", error)
                    continue

            program_91(root)

        elif choice in ("92", "94", "95"):
            if not tree_created:
                print("Create a tree first using option 91 or 96.")
                continue

            _, function = programs[choice]
            function(root)

        elif choice == "93":
            if not tree_created:
                print("Create a tree first using option 91 or 96.")
                continue

            program_93(root)

        else:
            print("Invalid choice. Enter 91-96 or 0.")


if __name__ == "__main__":
    main()
