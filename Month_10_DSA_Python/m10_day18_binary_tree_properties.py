
from __future__ import annotations


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

    Example: 10 5 20 3 7 N 30
    """
    if not values:
        return None

    if values[0].upper() == "N":
        if len(values) > 1:
            raise ValueError("An empty tree cannot have additional nodes.")
        return None

    root = Node(int(values[0]))
    queue: list[Node] = [root]
    front = 0
    index = 1

    while front < len(queue) and index < len(values):
        current = queue[front]
        front += 1

        # Left child
        token = values[index]
        index += 1

        if token.upper() != "N":
            current.left = Node(int(token))
            queue.append(current.left)

        # Right child
        if index < len(values):
            token = values[index]
            index += 1

            if token.upper() != "N":
                current.right = Node(int(token))
                queue.append(current.right)

    if index < len(values):
        raise ValueError("Some values have no valid parent in the tree.")

    return root


def read_tree(prompt: str) -> Node | None:
    print(prompt)
    print("Enter level-order values separated by spaces.")
    print("Use N for a missing child. Example: 10 5 20 3 7 N 30")

    values = input("Tree: ").split()
    return build_tree(values)


def display_tree(root: Node | None) -> None:
    """Display the existing nodes in level order."""
    if root is None:
        print("Tree is empty.")
        return

    queue: list[Node] = [root]
    front = 0
    result: list[int] = []

    while front < len(queue):
        current = queue[front]
        front += 1
        result.append(current.data)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    print("Tree level order:", result)


# ==========================================================
# PROGRAM 86: Count total nodes in a binary tree
# ==========================================================

def count_nodes(root: Node | None) -> int:
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


def program_86(root: Node | None) -> None:
    print("Total number of nodes:", count_nodes(root))


# ==========================================================
# PROGRAM 87: Find the height of a binary tree
# Height is measured in number of nodes on the longest path.
# Empty tree height = 0; a single-node tree height = 1.
# ==========================================================

def tree_height(root: Node | None) -> int:
    if root is None:
        return 0

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return 1 + max(left_height, right_height)


def program_87(root: Node | None) -> None:
    print("Height of the binary tree:", tree_height(root))


# ==========================================================
# PROGRAM 88: Find maximum value in a binary tree
# ==========================================================

def maximum_value(root: Node | None) -> int | None:
    if root is None:
        return None

    left_max = maximum_value(root.left)
    right_max = maximum_value(root.right)

    result = root.data

    if left_max is not None:
        result = max(result, left_max)

    if right_max is not None:
        result = max(result, right_max)

    return result


def program_88(root: Node | None) -> None:
    result = maximum_value(root)

    if result is None:
        print("Cannot find a maximum: the tree is empty.")
    else:
        print("Maximum value:", result)


# ==========================================================
# PROGRAM 89: Count leaf nodes in a binary tree
# A leaf has no left or right child.
# ==========================================================

def count_leaf_nodes(root: Node | None) -> int:
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return (
        count_leaf_nodes(root.left)
        + count_leaf_nodes(root.right)
    )


def program_89(root: Node | None) -> None:
    print("Number of leaf nodes:", count_leaf_nodes(root))


# ==========================================================
# PROGRAM 90: Check whether two trees are identical
# They must have the same structure and node values.
# ==========================================================

def are_identical(
    first: Node | None,
    second: Node | None,
) -> bool:
    # Both empty at this position.
    if first is None and second is None:
        return True

    # Only one tree has a node at this position.
    if first is None or second is None:
        return False

    # Compare current values and both subtrees.
    return (
        first.data == second.data
        and are_identical(first.left, second.left)
        and are_identical(first.right, second.right)
    )


def program_90(first: Node | None, second: Node | None) -> None:
    if are_identical(first, second):
        print("The two binary trees are identical.")
    else:
        print("The two binary trees are NOT identical.")


# ==========================================================
# MAIN MENU: PROGRAMS 86-90
# ==========================================================

def main() -> None:
    root: Node | None = None
    tree_created = False

    while True:
        print("\n========== MONTH 10 - DAY 18 ==========")
        print("86. Count total nodes")
        print("87. Find tree height")
        print("88. Find maximum value")
        print("89. Count leaf nodes")
        print("90. Check whether two trees are identical")
        print("91. Run all programs (86-90)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Day 18 practice completed!")
            break

        elif choice == "86":
            try:
                root = read_tree("Create the binary tree:")
                tree_created = True
                display_tree(root)
                program_86(root)
            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "87":
            if not tree_created:
                print("Create a tree first using option 86.")
                continue

            program_87(root)

        elif choice == "88":
            if not tree_created:
                print("Create a tree first using option 86.")
                continue

            program_88(root)

        elif choice == "89":
            if not tree_created:
                print("Create a tree first using option 86.")
                continue

            program_89(root)

        elif choice == "90":
            try:
                first = read_tree("Enter the first tree:")
                second = read_tree("Enter the second tree:")

                print("\nFirst tree:")
                display_tree(first)
                print("Second tree:")
                display_tree(second)

                program_90(first, second)
            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "91":
            try:
                root = read_tree("Create the first tree for Programs 86-89:")
                tree_created = True

                print("\nCreated tree:")
                display_tree(root)

                print("\n--- Program 86 ---")
                program_86(root)

                print("\n--- Program 87 ---")
                program_87(root)

                print("\n--- Program 88 ---")
                program_88(root)

                print("\n--- Program 89 ---")
                program_89(root)

                print("\n--- Program 90 ---")
                first = root
                second = read_tree("Enter another tree to compare:")
                display_tree(second)
                program_90(first, second)

            except ValueError as error:
                print("Invalid input:", error)

        else:
            print("Invalid choice. Enter 86-91 or 0.")


if __name__ == "__main__":
    main()
