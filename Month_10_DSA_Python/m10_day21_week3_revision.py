
from __future__ import annotations

from collections import deque
from typing import Deque, Iterator


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
# HELPER: BUILD A TREE FROM LEVEL-ORDER INPUT
# ==========================================================

def build_tree(values: list[str]) -> Node | None:
    """Use N to represent a missing child."""
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
    print("Enter level-order values, using N for missing children.")
    print("Example: 1 2 3 4 5 N 6")
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
# PROGRAM 101: Construct tree from preorder and inorder
# ==========================================================

def build_from_preorder_inorder(
    preorder_values: list[int],
    inorder_values: list[int],
) -> Node | None:
    """
    Construct a binary tree from preorder and inorder traversals.
    Assumes all node values are unique.
    """

    if len(preorder_values) != len(inorder_values):
        raise ValueError("Preorder and inorder lengths must match.")

    if len(set(preorder_values)) != len(preorder_values):
        raise ValueError("Node values must be unique.")

    if set(preorder_values) != set(inorder_values):
        raise ValueError("Preorder and inorder must contain the same values.")

    positions = {
        value: index
        for index, value in enumerate(inorder_values)
    }
    preorder_index = 0

    def construct(left: int, right: int) -> Node | None:
        nonlocal preorder_index

        if left > right:
            return None

        if preorder_index >= len(preorder_values):
            raise ValueError("Invalid traversal sequences.")

        value = preorder_values[preorder_index]
        preorder_index += 1

        split = positions[value]

        if split < left or split > right:
            raise ValueError("Inconsistent preorder and inorder sequences.")

        root = Node(value)
        root.left = construct(left, split - 1)
        root.right = construct(split + 1, right)

        return root

    root = construct(0, len(inorder_values) - 1)

    if preorder_index != len(preorder_values):
        raise ValueError("Invalid traversal sequences.")

    return root


def get_preorder(root: Node | None) -> list[int]:
    if root is None:
        return []

    return [root.data] + get_preorder(root.left) + get_preorder(root.right)


def get_inorder(root: Node | None) -> list[int]:
    if root is None:
        return []

    return get_inorder(root.left) + [root.data] + get_inorder(root.right)


def program_101() -> Node | None:
    preorder_values = list(
        map(int, input("Enter preorder traversal: ").split())
    )
    inorder_values = list(
        map(int, input("Enter inorder traversal: ").split())
    )

    root = build_from_preorder_inorder(preorder_values, inorder_values)

    print("Tree constructed successfully.")
    print("Preorder verification:", get_preorder(root))
    print("Inorder verification:", get_inorder(root))
    display_tree(root)

    return root


# ==========================================================
# PROGRAM 102: Serialize and deserialize a binary tree
# ==========================================================

def serialize(root: Node | None) -> str:
    """
    Serialize using preorder with N markers for missing children.
    This preserves both node values and tree structure.
    """
    values: list[str] = []

    def encode(node: Node | None) -> None:
        if node is None:
            values.append("N")
            return

        values.append(str(node.data))
        encode(node.left)
        encode(node.right)

    encode(root)
    return ",".join(values)


def deserialize(data: str) -> Node | None:
    """Reconstruct a tree from the serialized preorder sequence."""
    if not data:
        raise ValueError("Serialized data cannot be empty.")

    tokens = iter(data.split(","))

    def decode() -> Node | None:
        try:
            token = next(tokens)
        except StopIteration as error:
            raise ValueError("Serialized data is incomplete.") from error

        if token == "N":
            return None

        try:
            value = int(token)
        except ValueError as error:
            raise ValueError(f"Invalid node value: {token}") from error

        node = Node(value)
        node.left = decode()
        node.right = decode()
        return node

    root = decode()

    # Reject trailing tokens that do not belong to the tree.
    try:
        next(tokens)
    except StopIteration:
        return root

    raise ValueError("Serialized data contains extra tokens.")


def program_102(root: Node | None) -> None:
    data = serialize(root)
    print("Serialized tree:", data)

    restored_root = deserialize(data)
    print("Deserialized tree:")
    display_tree(restored_root)

    print(
        "Round-trip successful:",
        serialize(restored_root) == data,
    )


# ==========================================================
# PROGRAM 103: Boundary traversal of a binary tree
# Anti-clockwise: root, left boundary, leaves, right boundary
# ==========================================================

def boundary_traversal(root: Node | None) -> list[int]:
    if root is None:
        return []

    def is_leaf(node: Node) -> bool:
        return node.left is None and node.right is None

    if is_leaf(root):
        return [root.data]

    result: list[int] = [root.data]

    # Add the left boundary, excluding leaves.
    current = root.left

    while current is not None:
        if not is_leaf(current):
            result.append(current.data)

        if current.left is not None:
            current = current.left
        else:
            current = current.right

    # Add all leaf nodes from left to right.
    def add_leaves(node: Node | None) -> None:
        if node is None:
            return

        if is_leaf(node):
            result.append(node.data)
            return

        add_leaves(node.left)
        add_leaves(node.right)

    add_leaves(root.left)
    add_leaves(root.right)

    # Add the right boundary in reverse, excluding leaves.
    right_boundary: list[int] = []
    current = root.right

    while current is not None:
        if not is_leaf(current):
            right_boundary.append(current.data)

        if current.right is not None:
            current = current.right
        else:
            current = current.left

    result.extend(reversed(right_boundary))
    return result


def program_103(root: Node | None) -> None:
    print("Anti-clockwise boundary traversal:", boundary_traversal(root))


# ==========================================================
# PROGRAM 104: Check whether a binary tree is symmetric
# ==========================================================

def is_symmetric(root: Node | None) -> bool:
    def are_mirrors(
        first: Node | None,
        second: Node | None,
    ) -> bool:
        if first is None and second is None:
            return True

        if first is None or second is None:
            return False

        return (
            first.data == second.data
            and are_mirrors(first.left, second.right)
            and are_mirrors(first.right, second.left)
        )

    if root is None:
        return True

    return are_mirrors(root.left, root.right)


def program_104(root: Node | None) -> None:
    if is_symmetric(root):
        print("The binary tree is symmetric.")
    else:
        print("The binary tree is NOT symmetric.")


# ==========================================================
# PROGRAM 105: Distance between two nodes
# Distance is measured in edges.
# ==========================================================

def find_lca(
    root: Node | None,
    first_value: int,
    second_value: int,
) -> Node | None:
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


def find_depth(
    root: Node | None,
    target: int,
    depth: int = 0,
) -> int | None:
    if root is None:
        return None

    if root.data == target:
        return depth

    left_depth = find_depth(root.left, target, depth + 1)

    if left_depth is not None:
        return left_depth

    return find_depth(root.right, target, depth + 1)


def distance_between_nodes(
    root: Node | None,
    first_value: int,
    second_value: int,
) -> int | None:
    if root is None:
        return None

    first_depth = find_depth(root, first_value)
    second_depth = find_depth(root, second_value)

    if first_depth is None or second_depth is None:
        return None

    ancestor = find_lca(root, first_value, second_value)

    if ancestor is None:
        return None

    ancestor_depth = find_depth(root, ancestor.data)

    if ancestor_depth is None:
        return None

    return first_depth + second_depth - 2 * ancestor_depth


def program_105(root: Node | None) -> None:
    first_value = int(input("Enter the first node value: "))
    second_value = int(input("Enter the second node value: "))

    distance = distance_between_nodes(root, first_value, second_value)

    if distance is None:
        print("One or both target nodes do not exist in the tree.")
    else:
        print("Distance between nodes:", distance, "edges")


# ==========================================================
# MAIN MENU: PROGRAMS 101-105
# ==========================================================

def main() -> None:
    root: Node | None = None
    tree_created = False

    programs = {
        "102": ("Serialize and deserialize a tree", program_102),
        "103": ("Boundary traversal", program_103),
        "104": ("Check whether tree is symmetric", program_104),
        "105": ("Distance between two nodes", program_105),
    }

    while True:
        print("\n========== MONTH 10 - DAY 21 ==========")
        print("101. Construct tree from preorder and inorder")
        print("102. Serialize and deserialize a tree")
        print("103. Boundary traversal")
        print("104. Check whether tree is symmetric")
        print("105. Distance between two nodes")
        print("106. Run all programs (101-105)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Week 3 revision completed!")
            break

        elif choice == "101":
            try:
                root = program_101()
                tree_created = True
            except ValueError as error:
                print("Invalid traversal input:", error)

        elif choice == "106":
            try:
                print("\n--- Program 101 ---")
                root = program_101()
                tree_created = True

                print("\n--- Program 102 ---")
                program_102(root)

                print("\n--- Program 103 ---")
                program_103(root)

                print("\n--- Program 104 ---")
                program_104(root)

                print("\n--- Program 105 ---")
                program_105(root)

            except ValueError as error:
                print("Invalid input:", error)

        elif choice in programs:
            if not tree_created:
                try:
                    root = read_tree()
                    tree_created = True
                    display_tree(root)
                except ValueError as error:
                    print("Invalid tree input:", error)
                    continue

            description, function = programs[choice]
            print(f"\n--- Program {choice}: {description} ---")

            try:
                function(root)
            except ValueError as error:
                print("Invalid input:", error)

        else:
            print("Invalid choice. Enter 101-106 or 0.")


if __name__ == "__main__":
    main()
