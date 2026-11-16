
# ============================================================
# MONTH 11 - DAY 16
# ADVANCED TREE CONSTRUCTION AND QUERIES
# Programs 76-80
# ============================================================

from typing import Optional
from collections import deque


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


def display_inorder(root: Optional[TreeNode]) -> list[int]:
    """Return inorder traversal of a binary tree."""

    result: list[int] = []

    def inorder(node: Optional[TreeNode]) -> None:
        if node is None:
            return

        inorder(node.left)
        result.append(node.data)
        inorder(node.right)

    inorder(root)

    return result


def display_preorder(root: Optional[TreeNode]) -> list[int]:
    """Return preorder traversal of a binary tree."""

    result: list[int] = []

    def preorder(node: Optional[TreeNode]) -> None:
        if node is None:
            return

        result.append(node.data)
        preorder(node.left)
        preorder(node.right)

    preorder(root)

    return result


# ============================================================
# PROGRAM 76: CONSTRUCT TREE FROM INORDER AND POSTORDER
# ============================================================

def construct_tree_from_inorder_postorder(
    inorder: list[int],
    postorder: list[int]
) -> Optional[TreeNode]:
    """
    Construct a binary tree using inorder and postorder traversals.

    Assumption:
        All node values are unique.

    Inorder:
        Left -> Root -> Right

    Postorder:
        Left -> Right -> Root
    """

    if len(inorder) != len(postorder):
        raise ValueError(
            "Inorder and postorder must have equal lengths."
        )

    if len(set(inorder)) != len(inorder):
        raise ValueError("Node values must be unique.")

    if set(inorder) != set(postorder):
        raise ValueError(
            "Inorder and postorder must contain the same values."
        )

    if not inorder:
        return None

    # Store the index of every value in inorder.
    inorder_index = {
        value: index
        for index, value in enumerate(inorder)
    }

    # Start from the last element of postorder.
    post_index = [len(postorder) - 1]

    def build(left: int, right: int) -> Optional[TreeNode]:

        if left > right:
            return None

        if post_index[0] < 0:
            raise ValueError("Invalid traversal sequences.")

        # Current root is the last unprocessed postorder value.
        root_value = postorder[post_index[0]]
        post_index[0] -= 1

        root = TreeNode(root_value)

        middle = inorder_index[root_value]

        # Build right subtree first.
        root.right = build(middle + 1, right)

        # Then build left subtree.
        root.left = build(left, middle - 1)

        return root

    root = build(0, len(inorder) - 1)

    if post_index[0] != -1:
        raise ValueError("Invalid traversal sequences.")

    return root


def run_program_76() -> None:
    print(
        "\n--- PROGRAM 76: CONSTRUCT TREE FROM INORDER AND POSTORDER ---"
    )

    inorder = list(
        map(int, input("Enter inorder traversal: ").split())
    )

    postorder = list(
        map(int, input("Enter postorder traversal: ").split())
    )

    root = construct_tree_from_inorder_postorder(
        inorder,
        postorder
    )

    print("Constructed tree successfully.")

    print("Inorder traversal:", display_inorder(root))

    print("Preorder traversal:", display_preorder(root))


# ============================================================
# PROGRAM 77: MAXIMUM SUM BST IN BINARY TREE
# ============================================================

def maximum_sum_bst(root: Optional[TreeNode]) -> int:
    """
    Find the maximum sum of all nodes belonging to a valid BST
    subtree inside a binary tree.

    A valid BST requires:
        All left subtree values < current node.
        All right subtree values > current node.

    An empty subtree is allowed, so the answer is at least zero.
    """

    max_sum = 0

    def solve(
        node: Optional[TreeNode]
    ) -> tuple[bool, int, Optional[int], Optional[int]]:
        """
        Returns:
            is_bst
            subtree_sum
            minimum_value
            maximum_value
        """

        nonlocal max_sum

        if node is None:
            return True, 0, None, None

        left_valid, left_sum, left_min, left_max = solve(node.left)

        right_valid, right_sum, right_min, right_max = solve(node.right)

        # Check whether current subtree is a valid BST.
        left_is_smaller = (
            left_max is None or left_max < node.data
        )

        right_is_larger = (
            right_min is None or right_min > node.data
        )

        if left_valid and right_valid and left_is_smaller and right_is_larger:

            current_sum = node.data + left_sum + right_sum

            max_sum = max(max_sum, current_sum)

            current_min = (
                left_min if left_min is not None else node.data
            )

            current_max = (
                right_max if right_max is not None else node.data
            )

            return True, current_sum, current_min, current_max

        # Invalid BST subtree.
        return False, 0, None, None

    solve(root)

    return max_sum


def run_program_77() -> None:
    print("\n--- PROGRAM 77: MAXIMUM SUM BST ---")

    root = read_tree()

    result = maximum_sum_bst(root)

    print("Maximum sum of a valid BST subtree:", result)


# ============================================================
# PROGRAM 78: RECOVER SWAPPED BST
# ============================================================

def recover_swapped_bst(root: Optional[TreeNode]) -> bool:
    """
    Recover a BST in which two node values were swapped.

    Uses inorder traversal to identify incorrect nodes.

    The tree structure is not modified.
    Only the two incorrect node values are swapped.

    Returns True if a swapped pair is found and corrected.
    """

    first: Optional[TreeNode] = None
    middle: Optional[TreeNode] = None
    last: Optional[TreeNode] = None

    previous: Optional[TreeNode] = None

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal first, middle, last, previous

        if node is None:
            return

        inorder(node.left)

        # Detect an inorder violation.
        if previous is not None and previous.data > node.data:

            if first is None:
                # First violation.
                first = previous
                middle = node

            else:
                # Second violation.
                last = node

        previous = node

        inorder(node.right)

    inorder(root)

    if first is None:
        return False

    if last is not None:
        # Non-adjacent swapped nodes.
        first.data, last.data = last.data, first.data

    elif middle is not None:
        # Adjacent swapped nodes.
        first.data, middle.data = middle.data, first.data

    else:
        return False

    return True


def run_program_78() -> None:
    print("\n--- PROGRAM 78: RECOVER SWAPPED BST ---")

    root = read_tree()

    print("Inorder before recovery:", display_inorder(root))

    recovered = recover_swapped_bst(root)

    if recovered:
        print("Swapped nodes successfully recovered.")
    else:
        print("No swapped pair was detected.")

    print("Inorder after recovery:", display_inorder(root))


# ============================================================
# PROGRAM 79: MORRIS INORDER TRAVERSAL
# ============================================================

def morris_inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """
    Perform inorder traversal using Morris Traversal.

    Does not use recursion or an explicit stack.

    Uses temporary threads to return to a node after
    processing its left subtree.

    The original tree structure is restored.
    """

    result: list[int] = []

    current = root

    while current is not None:

        # Case 1: No left subtree.
        if current.left is None:

            result.append(current.data)

            current = current.right

        else:

            # Find inorder predecessor.
            predecessor = current.left

            while (
                predecessor.right is not None
                and predecessor.right is not current
            ):
                predecessor = predecessor.right

            # First visit: create a temporary thread.
            if predecessor.right is None:

                predecessor.right = current

                current = current.left

            else:

                # Second visit: remove the temporary thread.
                predecessor.right = None

                result.append(current.data)

                current = current.right

    return result


def run_program_79() -> None:
    print("\n--- PROGRAM 79: MORRIS INORDER TRAVERSAL ---")

    root = read_tree()

    result = morris_inorder_traversal(root)

    print("Morris inorder traversal:", result)


# ============================================================
# PROGRAM 80: COUNT COMPLETE TREE NODES
# ============================================================

def count_complete_tree_nodes(root: Optional[TreeNode]) -> int:
    """
    Count nodes in a complete binary tree.

    Optimized approach:
        Calculate the height along the leftmost path.
        Calculate the height along the rightmost path.

    If both heights are equal, the subtree is perfect.

    Otherwise, recursively count its left and right subtrees.

    IMPORTANT:
        Input must be a complete binary tree.
    """

    if root is None:
        return 0

    def left_height(node: Optional[TreeNode]) -> int:
        height = 0

        while node is not None:
            height += 1
            node = node.left

        return height

    def right_height(node: Optional[TreeNode]) -> int:
        height = 0

        while node is not None:
            height += 1
            node = node.right

        return height

    left_h = left_height(root)
    right_h = right_height(root)

    # Equal heights indicate a perfect binary tree.
    if left_h == right_h:
        return (1 << left_h) - 1

    return (
        1
        + count_complete_tree_nodes(root.left)
        + count_complete_tree_nodes(root.right)
    )


def run_program_80() -> None:
    print("\n--- PROGRAM 80: COUNT COMPLETE TREE NODES ---")

    print("Enter a COMPLETE binary tree.")

    root = read_tree()

    result = count_complete_tree_nodes(root)

    print("Total number of nodes:", result)


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all_programs() -> None:
    print("\n========== RUNNING ALL DAY 16 PROGRAMS ==========")

    run_program_76()

    run_program_77()

    run_program_78()

    run_program_79()

    run_program_80()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    while True:

        print("\n==============================================")
        print("       MONTH 11 - DAY 16 DSA MENU")
        print("  ADVANCED TREE CONSTRUCTION AND QUERIES")
        print("==============================================")

        print("76. Construct Tree from Inorder and Postorder")
        print("77. Maximum Sum BST in Binary Tree")
        print("78. Recover Swapped BST")
        print("79. Morris Inorder Traversal")
        print("80. Count Complete Tree Nodes")
        print("81. Run All Programs")
        print("0. Exit")

        print("==============================================")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 76:
                run_program_76()

            elif choice == 77:
                run_program_77()

            elif choice == 78:
                run_program_78()

            elif choice == 79:
                run_program_79()

            elif choice == 80:
                run_program_80()

            elif choice == 81:
                run_all_programs()

            elif choice == 0:
                print(
                    "Exiting Day 16 DSA Programs. Keep practicing!"
                )
                break

            else:
                print("Invalid choice. Please select 0-81.")

        except ValueError as error:
            print("Input error:", error)

        except Exception as error:
            print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()
