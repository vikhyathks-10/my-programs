
# ============================================================
# MONTH 11 - DAY 15
# ADVANCED TREE ALGORITHMS
# Programs 71-75
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

    Example:
        Input: [1, 2, 3, 4, 5, None, 6]

                1
              /   \\
             2     3
            / \\     \\
           4   5     6
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
# PROGRAM 71: MAXIMUM WIDTH OF BINARY TREE
# ============================================================

def maximum_width(root: Optional[TreeNode]) -> int:
    """
    Find maximum width including gaps between nodes.

    Uses positional indexing like a complete binary tree.
    """

    if root is None:
        return 0

    queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])

    max_width = 0

    while queue:
        level_size = len(queue)

        first_position = queue[0][1]

        first_index = 0
        last_index = 0

        for index in range(level_size):
            node, position = queue.popleft()

            normalized_position = position - first_position

            if index == 0:
                first_index = normalized_position

            if index == level_size - 1:
                last_index = normalized_position

            if node.left is not None:
                queue.append(
                    (node.left, 2 * normalized_position + 1)
                )

            if node.right is not None:
                queue.append(
                    (node.right, 2 * normalized_position + 2)
                )

        current_width = last_index - first_index + 1

        max_width = max(max_width, current_width)

    return max_width


def run_program_71() -> None:
    print("\n--- PROGRAM 71: MAXIMUM WIDTH OF BINARY TREE ---")

    root = read_tree()

    result = maximum_width(root)

    print("Maximum width of binary tree:", result)


# ============================================================
# PROGRAM 72: BURNING TREE
# ============================================================

def burning_tree_time(
    root: Optional[TreeNode],
    target: int
) -> int:
    """
    Find minimum time required to burn the entire tree.

    Fire spreads to left child, right child and parent.
    Every spread takes one second.

    Assumption: Node values are unique.
    """

    if root is None:
        raise ValueError("Tree cannot be empty.")

    # Store parent information.
    parent: dict[TreeNode, Optional[TreeNode]] = {
        root: None
    }

    queue: deque[TreeNode] = deque([root])

    target_node: Optional[TreeNode] = None

    # Build parent mapping and locate target.
    while queue:
        current = queue.popleft()

        if current.data == target:
            target_node = current

        if current.left is not None:
            parent[current.left] = current
            queue.append(current.left)

        if current.right is not None:
            parent[current.right] = current
            queue.append(current.right)

    if target_node is None:
        raise ValueError("Target node not found in the tree.")

    # Start fire from target node.
    burning_queue: deque[TreeNode] = deque([target_node])

    visited: set[TreeNode] = {target_node}

    time_taken = 0

    while burning_queue:
        level_size = len(burning_queue)

        spread_occurred = False

        for _ in range(level_size):
            current = burning_queue.popleft()

            neighbours: list[Optional[TreeNode]] = [
                current.left,
                current.right,
                parent[current]
            ]

            for neighbour in neighbours:

                if neighbour is not None and neighbour not in visited:
                    visited.add(neighbour)
                    burning_queue.append(neighbour)
                    spread_occurred = True

        if spread_occurred:
            time_taken += 1

    return time_taken


def run_program_72() -> None:
    print("\n--- PROGRAM 72: BURNING TREE ---")

    root = read_tree()

    target = int(input("Enter target node value: "))

    result = burning_tree_time(root, target)

    print("Minimum time to burn the entire tree:", result)


# ============================================================
# PROGRAM 73: MAXIMUM SUM OF NON-ADJACENT TREE NODES
# ============================================================

def maximum_non_adjacent_sum(root: Optional[TreeNode]) -> int:
    """
    Find maximum sum of nodes such that no two directly
    connected nodes are selected.

    include = Current node + sums excluding its children.
    exclude = Best sums from its children.

    Empty selection is allowed.
    """

    def solve(node: Optional[TreeNode]) -> tuple[int, int]:

        if node is None:
            return 0, 0

        left_include, left_exclude = solve(node.left)

        right_include, right_exclude = solve(node.right)

        # Select current node.
        include_node = (
            node.data
            + left_exclude
            + right_exclude
        )

        # Do not select current node.
        exclude_node = (
            max(left_include, left_exclude)
            + max(right_include, right_exclude)
        )

        return include_node, exclude_node

    include_root, exclude_root = solve(root)

    return max(include_root, exclude_root)


def run_program_73() -> None:
    print(
        "\n--- PROGRAM 73: MAXIMUM SUM OF NON-ADJACENT TREE NODES ---"
    )

    root = read_tree()

    result = maximum_non_adjacent_sum(root)

    print("Maximum sum of non-adjacent nodes:", result)


# ============================================================
# PROGRAM 74: CONVERT BINARY TREE TO DOUBLY LINKED LIST
# INORDER TRAVERSAL
# ============================================================

def binary_tree_to_dll(
    root: Optional[TreeNode]
) -> tuple[Optional[TreeNode], Optional[TreeNode]]:
    """
    Convert binary tree into a doubly linked list
    using inorder traversal.

    Left pointer becomes previous.
    Right pointer becomes next.

    Returns (head, tail).

    The original tree is modified.
    """

    head: Optional[TreeNode] = None

    previous: Optional[TreeNode] = None

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal head, previous

        if node is None:
            return

        # Process left subtree.
        inorder(node.left)

        # Connect current node with previous node.
        if previous is None:
            head = node
        else:
            previous.right = node
            node.left = previous

        previous = node

        # Process right subtree.
        inorder(node.right)

    inorder(root)

    tail = previous

    # Terminate both ends.
    if head is not None:
        head.left = None

    if tail is not None:
        tail.right = None

    return head, tail


def display_dll_forward(head: Optional[TreeNode]) -> None:
    """Display DLL from head to tail."""

    current = head

    values: list[str] = []

    while current is not None:
        values.append(str(current.data))
        current = current.right

    print("Forward DLL:", " <-> ".join(values))


def display_dll_backward(tail: Optional[TreeNode]) -> None:
    """Display DLL from tail to head."""

    current = tail

    values: list[str] = []

    while current is not None:
        values.append(str(current.data))
        current = current.left

    print("Backward DLL:", " <-> ".join(values))


def run_program_74() -> None:
    print(
        "\n--- PROGRAM 74: BINARY TREE TO DOUBLY LINKED LIST ---"
    )

    root = read_tree()

    head, tail = binary_tree_to_dll(root)

    if head is None:
        print("The tree is empty.")
        return

    display_dll_forward(head)

    display_dll_backward(tail)


# ============================================================
# PROGRAM 75: FLATTEN BINARY TREE TO LINKED LIST
# PREORDER TRAVERSAL
# ============================================================

def flatten_binary_tree(root: Optional[TreeNode]) -> None:
    """
    Flatten binary tree into linked list in preorder.

    Preorder:
        Root -> Left -> Right

    After flattening:
        Left pointers are None.
        Right pointers connect the nodes.

    Original tree is modified in place.
    """

    if root is None:
        return

    stack: list[TreeNode] = [root]

    previous: Optional[TreeNode] = None

    while stack:
        current = stack.pop()

        # Save children before modifying pointers.
        left_child = current.left
        right_child = current.right

        # Connect previous node to current node.
        if previous is not None:
            previous.left = None
            previous.right = current

        # Push right first so left is processed first.
        if right_child is not None:
            stack.append(right_child)

        if left_child is not None:
            stack.append(left_child)

        previous = current

    # Final node must have no children.
    if previous is not None:
        previous.left = None
        previous.right = None


def display_flattened_tree(root: Optional[TreeNode]) -> None:
    """Display flattened tree using right pointers."""

    current = root

    values: list[str] = []

    while current is not None:

        values.append(str(current.data))

        if current.left is not None:
            raise RuntimeError(
                "Flattening failed: left pointer is not None."
            )

        current = current.right

    print("Flattened linked list:", " -> ".join(values))


def run_program_75() -> None:
    print("\n--- PROGRAM 75: FLATTEN BINARY TREE ---")

    root = read_tree()

    flatten_binary_tree(root)

    display_flattened_tree(root)


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all_programs() -> None:
    print("\n========== RUNNING ALL DAY 15 PROGRAMS ==========")

    run_program_71()
    run_program_72()
    run_program_73()
    run_program_74()
    run_program_75()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    while True:

        print("\n==============================================")
        print("       MONTH 11 - DAY 15 DSA MENU")
        print("          ADVANCED TREE ALGORITHMS")
        print("==============================================")

        print("71. Maximum Width of Binary Tree")
        print("72. Burning Tree")
        print("73. Maximum Sum of Non-Adjacent Tree Nodes")
        print("74. Convert Binary Tree to Doubly Linked List")
        print("75. Flatten Binary Tree to Linked List")
        print("76. Run All Programs")
        print("0. Exit")

        print("==============================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 71:
                run_program_71()

            elif choice == 72:
                run_program_72()

            elif choice == 73:
                run_program_73()

            elif choice == 74:
                run_program_74()

            elif choice == 75:
                run_program_75()

            elif choice == 76:
                run_all_programs()

            elif choice == 0:
                print(
                    "Exiting Day 15 DSA Programs. Keep practicing!"
                )
                break

            else:
                print("Invalid choice. Please select 0-76.")

        except ValueError as error:
            print("Input error:", error)

        except Exception as error:
            print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()
