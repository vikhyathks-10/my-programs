
from __future__ import annotations


class Node:
    """A node in a Binary Search Tree."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


def read_integer_list(prompt: str) -> list[int]:
    """Read integers separated by spaces."""
    while True:
        try:
            text = input(prompt).strip()
            if not text:
                return []
            return [int(item) for item in text.split()]
        except ValueError:
            print("Invalid input. Please enter integers only.")


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
    """Build a BST by inserting values in order."""
    root: Node | None = None

    for value in values:
        root = insert_bst(root, value)

    return root


def read_bst() -> Node | None:
    values = read_integer_list(
        "Enter unique BST values separated by spaces: "
    )

    if not values:
        print("The BST is empty.")
        return None

    return build_bst(values)


def search_bst(root: Node | None, target: int) -> Node | None:
    """Search for a value in a BST."""
    current = root

    while current is not None:
        if target == current.value:
            return current
        if target < current.value:
            current = current.left
        else:
            current = current.right

    return None


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


# Program 116: Lowest Common Ancestor in a BST
def lowest_common_ancestor(
    root: Node | None, first: int, second: int
) -> int | None:
    """Return the LCA value when both target values exist."""
    if search_bst(root, first) is None:
        return None
    if search_bst(root, second) is None:
        return None

    current = root

    while current is not None:
        if first < current.value and second < current.value:
            current = current.left
        elif first > current.value and second > current.value:
            current = current.right
        else:
            return current.value

    return None


def program_116() -> None:
    print("\n--- Program 116: Lowest Common Ancestor ---")
    root = read_bst()

    if root is None:
        return

    display_bst(root)
    first = int(input("Enter the first node value: "))
    second = int(input("Enter the second node value: "))

    result = lowest_common_ancestor(root, first, second)

    if result is None:
        print("One or both values are not present in the BST.")
    else:
        print("Lowest common ancestor:", result)


# Program 117: Convert a Sorted Array into a Balanced BST
def sorted_array_to_bst(values: list[int]) -> Node | None:
    """Build a height-balanced BST from a sorted array."""
    def build(left: int, right: int) -> Node | None:
        if left > right:
            return None

        middle = (left + right) // 2
        node = Node(values[middle])
        node.left = build(left, middle - 1)
        node.right = build(middle + 1, right)
        return node

    return build(0, len(values) - 1)


def tree_height(root: Node | None) -> int:
    if root is None:
        return 0

    return 1 + max(tree_height(root.left), tree_height(root.right))


def program_117() -> None:
    print("\n--- Program 117: Sorted Array to Balanced BST ---")
    values = read_integer_list(
        "Enter sorted, unique integers in ascending order: "
    )

    if not values:
        print("The array is empty.")
        return

    if values != sorted(values) or len(values) != len(set(values)):
        print("Please enter unique values in ascending order.")
        return

    root = sorted_array_to_bst(values)

    print("Balanced BST created.")
    print("Inorder traversal:", inorder_values(root))
    print("Tree height:", tree_height(root))


# Program 118: Recover a BST with Two Swapped Nodes
def recover_bst(root: Node | None) -> bool:
    """
    Recover a BST where exactly two node values were swapped.
    Return True if a swapped pair was found and corrected.
    """
    previous: Node | None = None
    first: Node | None = None
    second: Node | None = None
    stack: list[Node] = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()

        if previous is not None and previous.value > current.value:
            if first is None:
                first = previous
            second = current

        previous = current
        current = current.right

    if first is None or second is None:
        return False

    first.value, second.value = second.value, first.value
    return True


def program_118() -> None:
    print("\n--- Program 118: Recover a Swapped BST ---")
    root = read_bst()

    if root is None:
        return

    print("Original inorder traversal:")
    display_bst(root)

    first_value = int(input("Enter the first value to swap: "))
    second_value = int(input("Enter the second value to swap: "))

    first_node = search_bst(root, first_value)
    second_node = search_bst(root, second_value)

    if first_node is None or second_node is None:
        print("Both values must exist in the BST.")
        return

    if first_node is second_node:
        print("Choose two different values.")
        return

    # Simulate the two-node swap to create an invalid BST.
    first_node.value, second_node.value = (
        second_node.value,
        first_node.value,
    )

    print("After swapping, inorder traversal:")
    display_bst(root)

    if recover_bst(root):
        print("BST recovered successfully.")
        display_bst(root)
    else:
        print("No swapped pair could be recovered.")


# Program 119: Find a Pair with a Given Sum in a BST
def find_pair_with_sum(
    root: Node | None, target: int
) -> tuple[int, int] | None:
    """Find two distinct BST values whose sum equals target."""
    values = inorder_values(root)
    left = 0
    right = len(values) - 1

    while left < right:
        current_sum = values[left] + values[right]

        if current_sum == target:
            return values[left], values[right]
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return None


def program_119() -> None:
    print("\n--- Program 119: Pair with a Given Sum ---")
    root = read_bst()

    if root is None:
        return

    display_bst(root)
    target = int(input("Enter the target sum: "))
    result = find_pair_with_sum(root, target)

    if result is None:
        print("No pair with the given sum exists.")
    else:
        first, second = result
        print(f"Pair found: {first} + {second} = {target}")


# Program 120: Find the Closest Value to a Target
def closest_value(root: Node | None, target: float) -> int | None:
    """Return the BST value closest to the target."""
    if root is None:
        return None

    current = root
    closest = root.value

    while current is not None:
        current_difference = abs(current.value - target)
        closest_difference = abs(closest - target)

        if current_difference < closest_difference:
            closest = current.value
        elif current_difference == closest_difference:
            closest = min(closest, current.value)

        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            return current.value

    return closest


def program_120() -> None:
    print("\n--- Program 120: Closest Value to a Target ---")
    root = read_bst()

    if root is None:
        return

    display_bst(root)

    while True:
        try:
            target = float(input("Enter the target value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    result = closest_value(root, target)

    if result is None:
        print("The BST is empty.")
    else:
        print(f"Closest value to {target}:", result)


def run_all() -> None:
    program_116()
    program_117()
    program_118()
    program_119()
    program_120()


def main() -> None:
    while True:
        print("\n========== DAY 24: ADVANCED BST ==========")
        print("116. Lowest Common Ancestor in a BST")
        print("117. Sorted Array to Balanced BST")
        print("118. Recover BST with Two Swapped Nodes")
        print("119. Pair with a Given Sum")
        print("120. Closest Value to a Target")
        print("121. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "116":
            program_116()
        elif choice == "117":
            program_117()
        elif choice == "118":
            program_118()
        elif choice == "119":
            program_119()
        elif choice == "120":
            program_120()
        elif choice == "121":
            run_all()
        elif choice == "0":
            print("Exiting Day 24 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 116–121 or 0.")


if __name__ == "__main__":
    main()
