
from __future__ import annotations

from collections import deque
from typing import Deque


# ==========================================================
# PROGRAM 81: Create a binary tree using a node class
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


def build_tree(level_values: list[str]) -> Node | None:
    """
    Build a binary tree from level-order values.
    Use N to represent a missing child.
    Example: 1 2 3 4 5 N 6
    """
    if not level_values or level_values[0].upper() == "N":
        return None

    root = Node(int(level_values[0]))
    queue: Deque[Node] = deque([root])
    index = 1

    while queue and index < len(level_values):
        current = queue.popleft()

        # Create the left child if it exists.
        if index < len(level_values):
            token = level_values[index]
            index += 1

            if token.upper() != "N":
                current.left = Node(int(token))
                queue.append(current.left)

        # Create the right child if it exists.
        if index < len(level_values):
            token = level_values[index]
            index += 1

            if token.upper() != "N":
                current.right = Node(int(token))
                queue.append(current.right)

    if index < len(level_values):
        raise ValueError("Some values have no valid parent in the tree.")

    return root


def display_tree_level_order(root: Node | None) -> None:
    """Display existing nodes level by level."""
    if root is None:
        print("The tree is empty.")
        return

    queue: Deque[Node] = deque([root])
    values: list[int] = []

    while queue:
        current = queue.popleft()
        values.append(current.data)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    print("Tree level order:", values)


def program_81() -> Node | None:
    print("Enter tree values in level-order.")
    print("Use N for a missing child.")
    print("Example: 1 2 3 4 5 N 6")

    values = input("Enter values separated by spaces: ").split()

    try:
        root = build_tree(values)
        print("Binary tree created successfully.")
        display_tree_level_order(root)
        return root
    except ValueError as error:
        print("Invalid tree input:", error)
        return None


# ==========================================================
# PROGRAM 82: Recursive preorder traversal
# Root -> Left -> Right
# ==========================================================

def preorder(root: Node | None, result: list[int]) -> None:
    if root is None:
        return

    result.append(root.data)
    preorder(root.left, result)
    preorder(root.right, result)


def program_82(root: Node | None) -> None:
    result: list[int] = []
    preorder(root, result)
    print("Preorder traversal:", result)


# ==========================================================
# PROGRAM 83: Recursive inorder traversal
# Left -> Root -> Right
# ==========================================================

def inorder(root: Node | None, result: list[int]) -> None:
    if root is None:
        return

    inorder(root.left, result)
    result.append(root.data)
    inorder(root.right, result)


def program_83(root: Node | None) -> None:
    result: list[int] = []
    inorder(root, result)
    print("Inorder traversal:", result)


# ==========================================================
# PROGRAM 84: Recursive postorder traversal
# Left -> Right -> Root
# ==========================================================

def postorder(root: Node | None, result: list[int]) -> None:
    if root is None:
        return

    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.data)


def program_84(root: Node | None) -> None:
    result: list[int] = []
    postorder(root, result)
    print("Postorder traversal:", result)


# ==========================================================
# PROGRAM 85: Level-order traversal using a queue
# ==========================================================

def level_order(root: Node | None) -> list[int]:
    if root is None:
        return []

    result: list[int] = []
    queue: Deque[Node] = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.data)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return result


def program_85(root: Node | None) -> None:
    print("Level-order traversal:", level_order(root))


# ==========================================================
# MAIN MENU: PROGRAMS 81-85
# ==========================================================

def main() -> None:
    root: Node | None = None
    tree_created = False

    programs = {
        "82": ("Recursive preorder traversal", program_82),
        "83": ("Recursive inorder traversal", program_83),
        "84": ("Recursive postorder traversal", program_84),
        "85": ("Level-order traversal using a queue", program_85),
    }

    while True:
        print("\n========== MONTH 10 - DAY 17 ==========")
        print("81. Create a binary tree")
        print("82. Recursive preorder traversal")
        print("83. Recursive inorder traversal")
        print("84. Recursive postorder traversal")
        print("85. Level-order traversal using a queue")
        print("86. Run all programs (81-85)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Day 17 practice completed!")
            break

        elif choice == "81":
            new_root = program_81()

            if new_root is not None:
                root = new_root
                tree_created = True
            else:
                print("No new tree was stored.")

        elif choice in programs:
            if not tree_created:
                print("Create a tree first using option 81.")
                continue

            description, function = programs[choice]
            print(f"\n--- Program {choice}: {description} ---")
            function(root)

        elif choice == "86":
            new_root = program_81()

            if new_root is None:
                print("Could not create a non-empty tree. Returning to menu.")
                continue

            root = new_root
            tree_created = True

            for number, (description, function) in programs.items():
                print(f"\n--- Program {number}: {description} ---")
                function(root)

        else:
            print("Invalid choice. Enter 81-86 or 0.")


if __name__ == "__main__":
    main()
