
# ============================================================
# MONTH 11 - DAY 17
# TREE-BASED ADVANCED CHALLENGES
# Programs 81-85
# ============================================================

from collections import deque
from typing import Optional


# ============================================================
# BINARY TREE NODE
# ============================================================

class TreeNode:
    def __init__(self, value: int) -> None:
        self.data: int = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


# ============================================================
# COMMON FUNCTION: BUILD BINARY TREE
# ============================================================

def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from level-order input.

    None represents a missing node.
    """

    if not values:
        return None

    root_value = values[0]

    if root_value is None:
        return None

    root = TreeNode(root_value)

    queue: deque[TreeNode] = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()

        # Attach left child.
        if index < len(values):
            left_value = values[index]

            if left_value is not None:
                left_node = TreeNode(left_value)
                current.left = left_node
                queue.append(left_node)

            index += 1

        # Attach right child.
        if index < len(values):
            right_value = values[index]

            if right_value is not None:
                right_node = TreeNode(right_value)
                current.right = right_node
                queue.append(right_node)

            index += 1

    return root


def read_tree() -> Optional[TreeNode]:
    """Read a binary tree using level-order input."""

    raw_values = input(
        "Enter tree nodes in level order (use N for missing nodes): "
    ).split()

    values: list[Optional[int]] = []

    for value in raw_values:
        if value.upper() == "N":
            values.append(None)
        else:
            values.append(int(value))

    return build_tree(values)


# ============================================================
# PROGRAM 81: ALL NODES AT DISTANCE K
# ============================================================

def nodes_at_distance_k(
    root: Optional[TreeNode],
    target_value: int,
    k: int
) -> list[int]:
    """
    Return all nodes at distance K from the target node.

    Distance is measured in number of edges.

    Assumption:
        All node values are unique.
    """

    if root is None:
        return []

    if k < 0:
        raise ValueError("Distance K cannot be negative.")

    # Store parent of every node.
    parent: dict[TreeNode, Optional[TreeNode]] = {
        root: None
    }

    queue: deque[TreeNode] = deque([root])

    target_node: Optional[TreeNode] = None

    # Build parent mapping and locate target.
    while queue:
        current = queue.popleft()

        if current.data == target_value:
            target_node = current

        if current.left is not None:
            parent[current.left] = current
            queue.append(current.left)

        if current.right is not None:
            parent[current.right] = current
            queue.append(current.right)

    if target_node is None:
        raise ValueError("Target node not found in the tree.")

    # BFS starting from target.
    bfs_queue: deque[TreeNode] = deque([target_node])

    visited: set[TreeNode] = {target_node}

    current_distance = 0

    while bfs_queue and current_distance < k:

        level_size = len(bfs_queue)

        for _ in range(level_size):

            current = bfs_queue.popleft()

            neighbours: list[Optional[TreeNode]] = [
                current.left,
                current.right,
                parent[current]
            ]

            for neighbour in neighbours:

                if neighbour is not None and neighbour not in visited:
                    visited.add(neighbour)
                    bfs_queue.append(neighbour)

        current_distance += 1

    if current_distance != k:
        return []

    return [node.data for node in bfs_queue]


def run_program_81() -> None:
    print("\n--- PROGRAM 81: ALL NODES AT DISTANCE K ---")

    root = read_tree()

    target = int(input("Enter target node value: "))

    k = int(input("Enter distance K: "))

    result = nodes_at_distance_k(root, target, k)

    print(f"Nodes at distance {k} from {target}:", result)


# ============================================================
# PROGRAM 82: VERTICAL TRAVERSAL OF BINARY TREE
# ============================================================

def vertical_traversal(
    root: Optional[TreeNode]
) -> list[list[int]]:
    """
    Group nodes according to vertical columns.

    Position rules:
        Root column = 0
        Left child column = column - 1
        Right child column = column + 1

    Nodes are sorted by:
        1. Column
        2. Row
        3. Node value

    BFS stores each node's row and column.
    """

    if root is None:
        return []

    # Store (node, row, column).
    queue: deque[tuple[TreeNode, int, int]] = deque(
        [(root, 0, 0)]
    )

    # Store (row, value) for every column.
    columns: dict[int, list[tuple[int, int]]] = {}

    while queue:

        node, row, column = queue.popleft()

        if column not in columns:
            columns[column] = []

        columns[column].append((row, node.data))

        if node.left is not None:
            queue.append(
                (node.left, row + 1, column - 1)
            )

        if node.right is not None:
            queue.append(
                (node.right, row + 1, column + 1)
            )

    result: list[list[int]] = []

    # Process columns from left to right.
    for column in sorted(columns):

        # Sort by row first and then by node value.
        sorted_nodes = sorted(columns[column])

        result.append(
            [value for row, value in sorted_nodes]
        )

    return result


def run_program_82() -> None:
    print("\n--- PROGRAM 82: VERTICAL TRAVERSAL ---")

    root = read_tree()

    result = vertical_traversal(root)

    print("Vertical traversal:")

    for index, column in enumerate(result):
        print(f"Column {index + 1}: {column}")


# ============================================================
# PROGRAM 83: MAXIMUM DIFFERENCE BETWEEN NODE AND ANCESTOR
# ============================================================

def maximum_ancestor_difference(
    root: Optional[TreeNode]
) -> int:
    """
    Find the maximum absolute difference between
    an ancestor and one of its descendants.

    For each node, track the minimum and maximum values
    along the path from the root to that node.
    """

    if root is None:
        return 0

    max_difference = 0

    def solve(
        node: Optional[TreeNode],
        path_min: int,
        path_max: int
    ) -> None:

        nonlocal max_difference

        if node is None:
            return

        # Calculate difference with an ancestor on this path.
        max_difference = max(
            max_difference,
            abs(node.data - path_min),
            abs(node.data - path_max)
        )

        # Update path minimum and maximum.
        new_min = min(path_min, node.data)
        new_max = max(path_max, node.data)

        solve(node.left, new_min, new_max)

        solve(node.right, new_min, new_max)

    solve(root, root.data, root.data)

    return max_difference


def run_program_83() -> None:
    print(
        "\n--- PROGRAM 83: MAXIMUM DIFFERENCE BETWEEN NODE AND ANCESTOR ---"
    )

    root = read_tree()

    result = maximum_ancestor_difference(root)

    print("Maximum ancestor-descendant difference:", result)


# ============================================================
# PROGRAM 84: HOUSE ROBBER III
# ============================================================

def house_robber_iii(root: Optional[TreeNode]) -> int:
    """
    Find maximum sum without selecting directly connected nodes.

    For each node:
        rob = Node value + values from children not robbed.
        skip = Best values from children.

    This is a tree-based dynamic programming problem.
    """

    def solve(node: Optional[TreeNode]) -> tuple[int, int]:
        """
        Returns:
            (rob_current, skip_current)
        """

        if node is None:
            return 0, 0

        left_rob, left_skip = solve(node.left)

        right_rob, right_skip = solve(node.right)

        # Rob the current node.
        # Neither child can be robbed.
        rob_current = (
            node.data
            + left_skip
            + right_skip
        )

        # Skip the current node.
        # Each child can be robbed or skipped.
        skip_current = (
            max(left_rob, left_skip)
            + max(right_rob, right_skip)
        )

        return rob_current, skip_current

    rob_root, skip_root = solve(root)

    return max(rob_root, skip_root)


def run_program_84() -> None:
    print("\n--- PROGRAM 84: HOUSE ROBBER III ---")

    root = read_tree()

    result = house_robber_iii(root)

    print("Maximum amount that can be robbed:", result)


# ============================================================
# PROGRAM 85: BINARY TREE CAMERAS
# ============================================================

def minimum_cameras(root: Optional[TreeNode]) -> int:
    """
    Find the minimum number of cameras needed to monitor
    every node in a binary tree.

    Camera at a node monitors:
        1. Itself.
        2. Its parent.
        3. Its immediate children.

    States:
        0 = Node needs a camera.
        1 = Node has a camera.
        2 = Node is already covered.
    """

    cameras = 0

    def solve(node: Optional[TreeNode]) -> int:

        nonlocal cameras

        # Null nodes are considered covered.
        if node is None:
            return 2

        left_state = solve(node.left)

        right_state = solve(node.right)

        # If any child needs a camera,
        # place a camera at the current node.
        if left_state == 0 or right_state == 0:

            cameras += 1

            return 1

        # If any child has a camera,
        # current node is covered.
        if left_state == 1 or right_state == 1:

            return 2

        # Both children are covered but neither has a camera.
        # Current node needs a camera from its parent.
        return 0

    root_state = solve(root)

    # If root is not covered, place one final camera.
    if root_state == 0:
        cameras += 1

    return cameras


def run_program_85() -> None:
    print("\n--- PROGRAM 85: BINARY TREE CAMERAS ---")

    root = read_tree()

    result = minimum_cameras(root)

    print("Minimum cameras required:", result)


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all_programs() -> None:

    print("\n========== RUNNING ALL DAY 17 PROGRAMS ==========")

    run_program_81()

    run_program_82()

    run_program_83()

    run_program_84()

    run_program_85()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    while True:

        print("\n==============================================")
        print("       MONTH 11 - DAY 17 DSA MENU")
        print("        TREE-BASED ADVANCED CHALLENGES")
        print("==============================================")

        print("81. All Nodes at Distance K")

        print("82. Vertical Traversal of Binary Tree")

        print("83. Maximum Difference Between Node and Ancestor")

        print("84. House Robber III")

        print("85. Binary Tree Cameras")

        print("86. Run All Programs")

        print("0. Exit")

        print("==============================================")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 81:
                run_program_81()

            elif choice == 82:
                run_program_82()

            elif choice == 83:
                run_program_83()

            elif choice == 84:
                run_program_84()

            elif choice == 85:
                run_program_85()

            elif choice == 86:
                run_all_programs()

            elif choice == 0:

                print(
                    "Exiting Day 17 DSA Programs. Keep practicing!"
                )

                break

            else:

                print("Invalid choice. Please select 0-86.")

        except ValueError as error:

            print("Input error:", error)

        except Exception as error:

            print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()
