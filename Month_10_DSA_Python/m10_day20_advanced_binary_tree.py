
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
# HELPER: BUILD A BINARY TREE FROM LEVEL-ORDER INPUT
# ==========================================================

def build_tree(values: list[str]) -> Node | None:
    """
    Build a binary tree from level-order values.
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

        # Create the left child.
        token = values[index]
        index += 1

        if token.upper() != "N":
            current.left = Node(int(token))
            queue.append(current.left)

        # Create the right child, if input remains.
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
    return build_tree(input("Tree: ").split())


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
# PROGRAM 96: Zigzag level-order traversal
# ==========================================================

def zigzag_traversal(root: Node | None) -> list[int]:
    if root is None:
        return []

    result: list[int] = []
    queue: Deque[Node] = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level: list[int] = []

        for _ in range(level_size):
            current = queue.popleft()
            level.append(current.data)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        if not left_to_right:
            level.reverse()

        result.extend(level)
        left_to_right = not left_to_right

    return result


def program_96(root: Node | None) -> None:
    print("Zigzag traversal:", zigzag_traversal(root))


# ==========================================================
# PROGRAM 97: Top view of a binary tree
# ==========================================================

def top_view(root: Node | None) -> list[int]:
    if root is None:
        return []

    # Store the first node encountered at each horizontal distance.
    first_at_distance: dict[int, int] = {}
    queue: Deque[tuple[Node, int]] = deque([(root, 0)])

    while queue:
        current, distance = queue.popleft()

        if distance not in first_at_distance:
            first_at_distance[distance] = current.data

        if current.left is not None:
            queue.append((current.left, distance - 1))

        if current.right is not None:
            queue.append((current.right, distance + 1))

    return [
        first_at_distance[distance]
        for distance in sorted(first_at_distance)
    ]


def program_97(root: Node | None) -> None:
    print("Top view:", top_view(root))


# ==========================================================
# PROGRAM 98: Bottom view of a binary tree
# ==========================================================

def bottom_view(root: Node | None) -> list[int]:
    if root is None:
        return []

    # BFS processes nodes level by level. Later nodes at the
    # same horizontal distance replace earlier nodes.
    last_at_distance: dict[int, int] = {}
    queue: Deque[tuple[Node, int]] = deque([(root, 0)])

    while queue:
        current, distance = queue.popleft()
        last_at_distance[distance] = current.data

        if current.left is not None:
            queue.append((current.left, distance - 1))

        if current.right is not None:
            queue.append((current.right, distance + 1))

    return [
        last_at_distance[distance]
        for distance in sorted(last_at_distance)
    ]


def program_98(root: Node | None) -> None:
    print("Bottom view:", bottom_view(root))


# ==========================================================
# PROGRAM 99: Vertical order traversal
# ==========================================================

def vertical_order(root: Node | None) -> list[list[int]]:
    if root is None:
        return []

    columns: dict[int, list[int]] = {}
    queue: Deque[tuple[Node, int]] = deque([(root, 0)])

    while queue:
        current, distance = queue.popleft()
        columns.setdefault(distance, []).append(current.data)

        if current.left is not None:
            queue.append((current.left, distance - 1))

        if current.right is not None:
            queue.append((current.right, distance + 1))

    return [
        columns[distance]
        for distance in sorted(columns)
    ]


def program_99(root: Node | None) -> None:
    result = vertical_order(root)

    if not result:
        print("Vertical order: []")
        return

    print("Vertical order (left to right):")

    for index, column in enumerate(result, start=1):
        print(f"Column {index}: {column}")


# ==========================================================
# PROGRAM 100: Maximum path sum in a binary tree
# ==========================================================

def maximum_path_sum(root: Node | None) -> int | None:
    """
    A path can start and end at any nodes, but cannot
    visit the same node more than once.

    Return None for an empty tree.
    """
    if root is None:
        return None

    best_sum: int | None = None

    def max_gain(node: Node | None) -> int:
        nonlocal best_sum

        if node is None:
            return 0

        # Ignore negative gains because they reduce the path sum.
        left_gain = max(0, max_gain(node.left))
        right_gain = max(0, max_gain(node.right))

        # Best path passing through the current node.
        path_sum = node.data + left_gain + right_gain

        if best_sum is None or path_sum > best_sum:
            best_sum = path_sum

        # Return the best one-sided path to the parent.
        return node.data + max(left_gain, right_gain)

    max_gain(root)
    return best_sum


def program_100(root: Node | None) -> None:
    result = maximum_path_sum(root)

    if result is None:
        print("Maximum path sum is undefined for an empty tree.")
    else:
        print("Maximum path sum:", result)


# ==========================================================
# MAIN MENU: PROGRAMS 96-100
# ==========================================================

def main() -> None:
    root: Node | None = None
    tree_created = False

    programs = {
        "96": ("Zigzag level-order traversal", program_96),
        "97": ("Top view of a binary tree", program_97),
        "98": ("Bottom view of a binary tree", program_98),
        "99": ("Vertical order traversal", program_99),
        "100": ("Maximum path sum", program_100),
    }

    while True:
        print("\n========== MONTH 10 - DAY 20 ==========")

        for number, (description, _) in programs.items():
            print(f"{number}. {description}")

        print("101. Run all programs (96-100)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Day 20 practice completed!")
            break

        elif choice == "101":
            try:
                new_root = read_tree()
                root = new_root
                tree_created = True

                print("\nCreated tree:")
                display_tree(root)

                for number, (description, function) in programs.items():
                    print(f"\n--- Program {number}: {description} ---")
                    function(root)

            except ValueError as error:
                print("Invalid input:", error)

        elif choice in programs:
            if not tree_created:
                try:
                    root = read_tree()
                    tree_created = True
                    display_tree(root)
                except ValueError as error:
                    print("Invalid input:", error)
                    continue

            description, function = programs[choice]
            print(f"\n--- Program {choice}: {description} ---")
            function(root)

        else:
            print("Invalid choice. Enter 96-101 or 0.")


if __name__ == "__main__":
    main()
