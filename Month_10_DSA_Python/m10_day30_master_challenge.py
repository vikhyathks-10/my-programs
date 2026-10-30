
from __future__ import annotations

import heapq


# ============================================================
# COMMON INPUT HELPERS
# ============================================================

def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def read_integer_list(prompt: str) -> list[int]:
    while True:
        try:
            text = input(prompt).strip()
            if not text:
                return []
            return [int(value) for value in text.split()]
        except ValueError:
            print("Enter integers separated by spaces.")


# ============================================================
# PROGRAM 146: LRU CACHE
# ============================================================

class DLLNode:
    """Node used by the doubly linked list."""

    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: DLLNode | None = None
        self.next: DLLNode | None = None


class LRUCache:
    """
    Least Recently Used cache.

    Dictionary provides O(1) average lookup.
    Doubly linked list maintains usage order.
    Most recently used node stays near the head.
    """

    def __init__(self, capacity: int) -> None:
        if capacity < 0:
            raise ValueError("Capacity cannot be negative.")

        self.capacity = capacity
        self.cache: dict[int, DLLNode] = {}

        self.head = DLLNode()
        self.tail = DLLNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLLNode) -> None:
        previous = node.prev
        following = node.next

        if previous is not None and following is not None:
            previous.next = following
            following.prev = previous

    def _insert_at_front(self, node: DLLNode) -> None:
        first = self.head.next

        node.prev = self.head
        node.next = first

        self.head.next = node

        if first is not None:
            first.prev = node

    def _move_to_front(self, node: DLLNode) -> None:
        self._remove(node)
        self._insert_at_front(node)

    def get(self, key: int) -> int:
        """Return value if present; otherwise return -1."""
        node = self.cache.get(key)

        if node is None:
            return -1

        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Insert or update a key-value pair."""
        if self.capacity == 0:
            return

        existing = self.cache.get(key)

        if existing is not None:
            existing.value = value
            self._move_to_front(existing)
            return

        new_node = DLLNode(key, value)
        self.cache[key] = new_node
        self._insert_at_front(new_node)

        if len(self.cache) > self.capacity:
            least_recent = self.tail.prev

            if least_recent is not None and least_recent is not self.head:
                self._remove(least_recent)
                del self.cache[least_recent.key]

    def display(self) -> None:
        """Display entries from most to least recently used."""
        result: list[tuple[int, int]] = []
        current = self.head.next

        while current is not None and current is not self.tail:
            result.append((current.key, current.value))
            current = current.next

        print("Cache (most recent to least recent):", result)


def program_146() -> None:
    print("\n--- Program 146: LRU Cache ---")

    capacity = read_integer("Enter cache capacity: ")

    if capacity < 0:
        print("Capacity cannot be negative.")
        return

    cache = LRUCache(capacity)

    while True:
        print("\n1. Put (key, value)")
        print("2. Get (key)")
        print("3. Display cache")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            key = read_integer("Enter key: ")
            value = read_integer("Enter value: ")
            cache.put(key, value)
            print("Put operation completed.")
            cache.display()

        elif choice == "2":
            key = read_integer("Enter key: ")
            result = cache.get(key)

            if result == -1:
                print("Key not found (or stored value is -1).")
            else:
                print("Value:", result)

            cache.display()

        elif choice == "3":
            cache.display()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ============================================================
# PROGRAM 147: MERGE K SORTED LINKED LISTS
# ============================================================

class ListNode:
    """Node of a singly linked list."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.next: ListNode | None = None


def create_linked_list(values: list[int]) -> ListNode | None:
    """Create a linked list from a list of values."""
    dummy = ListNode(0)
    tail = dummy

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    """Convert a linked list into a Python list."""
    result: list[int] = []
    current = head

    while current is not None:
        result.append(current.value)
        current = current.next

    return result


def merge_k_sorted_lists(
    lists: list[ListNode | None],
) -> ListNode | None:
    """
    Merge K sorted linked lists using a min heap.
    Heap entries use a unique counter to break ties safely.
    """
    min_heap: list[tuple[int, int, ListNode]] = []
    counter = 0

    for node in lists:
        if node is not None:
            heapq.heappush(min_heap, (node.value, counter, node))
            counter += 1

    dummy = ListNode(0)
    tail = dummy

    while min_heap:
        _, _, smallest = heapq.heappop(min_heap)

        tail.next = smallest
        tail = smallest

        if smallest.next is not None:
            heapq.heappush(
                min_heap,
                (smallest.next.value, counter, smallest.next),
            )
            counter += 1

    tail.next = None
    return dummy.next


def program_147() -> None:
    print("\n--- Program 147: Merge K Sorted Lists ---")

    k = read_integer("How many sorted linked lists? ")

    if k < 0:
        print("Number of lists cannot be negative.")
        return

    lists: list[ListNode | None] = []

    for index in range(k):
        print(f"Enter sorted list {index + 1}:")
        values = read_integer_list("Values (ascending): ")

        if values != sorted(values):
            print("This list is not sorted. Please enter it again.")
            return

        lists.append(create_linked_list(values))

    merged = merge_k_sorted_lists(lists)

    print("Merged sorted linked list:")
    print(linked_list_to_list(merged))


# ============================================================
# PROGRAM 148: BINARY TREE MAXIMUM PATH SUM
# ============================================================

class TreeNode:
    """Binary tree node."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def build_binary_tree(tokens: list[str]) -> TreeNode | None:
    """
    Build a binary tree from level-order input.
    Use 'null' for missing children.
    Example:  -10 9 20 null null 15 7
    """
    if not tokens or tokens[0].lower() == "null":
        return None

    root = TreeNode(int(tokens[0]))
    queue: list[TreeNode] = [root]
    index = 1
    front = 0

    while front < len(queue) and index < len(tokens):
        current = queue[front]
        front += 1

        left_value = tokens[index]
        index += 1

        if left_value.lower() != "null":
            current.left = TreeNode(int(left_value))
            queue.append(current.left)

        if index < len(tokens):
            right_value = tokens[index]
            index += 1

            if right_value.lower() != "null":
                current.right = TreeNode(int(right_value))
                queue.append(current.right)

    return root


def maximum_path_sum(root: TreeNode | None) -> int | None:
    """
    Find the maximum sum of any non-empty path.
    A path can begin and end at any two nodes.
    """
    if root is None:
        return None

    best_sum = float("-inf")

    def max_gain(node: TreeNode | None) -> int:
        nonlocal best_sum

        if node is None:
            return 0

        left_gain = max(0, max_gain(node.left))
        right_gain = max(0, max_gain(node.right))

        # A path may pass through this node and use both children.
        path_sum = node.value + left_gain + right_gain
        best_sum = max(best_sum, path_sum)

        # Return only one branch to the parent.
        return node.value + max(left_gain, right_gain)

    max_gain(root)
    return int(best_sum)


def program_148() -> None:
    print("\n--- Program 148: Binary Tree Maximum Path Sum ---")
    print("Enter level-order values separated by spaces.")
    print("Use 'null' for missing children.")
    print("Example: -10 9 20 null null 15 7")

    tokens = input("Enter tree: ").split()

    try:
        root = build_binary_tree(tokens)
    except ValueError:
        print("Invalid tree input. Use integers or 'null'.")
        return

    result = maximum_path_sum(root)

    if result is None:
        print("The tree is empty.")
    else:
        print("Maximum path sum:", result)


# ============================================================
# PROGRAM 149: MEDIAN FROM DATA STREAM
# ============================================================

class MedianFinder:
    """
    Two heaps:
    - max heap stores the smaller half.
    - min heap stores the larger half.
    """

    def __init__(self) -> None:
        self.lower_half: list[int] = []
        self.upper_half: list[int] = []

    def add_number(self, number: int) -> None:
        """Insert a number while maintaining the two-heap balance."""

        # Insert into the lower max heap.
        heapq.heappush(self.lower_half, -number)

        # Move the largest value from lower half to upper half.
        largest_lower = -heapq.heappop(self.lower_half)
        heapq.heappush(self.upper_half, largest_lower)

        # Keep lower half equal in size or one element larger.
        if len(self.upper_half) > len(self.lower_half):
            smallest_upper = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -smallest_upper)

    def find_median(self) -> float | None:
        """Return the current median."""
        if not self.lower_half:
            return None

        if len(self.lower_half) > len(self.upper_half):
            return float(-self.lower_half[0])

        return (
            -self.lower_half[0] + self.upper_half[0]
        ) / 2.0


def program_149() -> None:
    print("\n--- Program 149: Median from Data Stream ---")
    finder = MedianFinder()

    while True:
        print("\n1. Add number")
        print("2. Find current median")
        print("3. Display both heaps")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            number = read_integer("Enter number: ")
            finder.add_number(number)
            print("Number added.")

            median = finder.find_median()
            print("Current median:", median)

        elif choice == "2":
            median = finder.find_median()

            if median is None:
                print("No numbers have been added.")
            else:
                print("Current median:", median)

        elif choice == "3":
            print("Lower half (max heap):", [-x for x in finder.lower_half])
            print("Upper half (min heap):", finder.upper_half)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ============================================================
# PROGRAM 150: SERIALIZE AND DESERIALIZE BST
# ============================================================

class BSTNode:
    """Node for a binary search tree."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


def bst_insert(root: BSTNode | None, value: int) -> BSTNode:
    """Insert a unique value into a BST."""
    if root is None:
        return BSTNode(value)

    if value < root.value:
        root.left = bst_insert(root.left, value)
    elif value > root.value:
        root.right = bst_insert(root.right, value)

    return root


def serialize_bst(root: BSTNode | None) -> str:
    """
    Serialize a BST using preorder traversal.
    This implementation assumes unique integer values.
    """
    values: list[str] = []

    def preorder(node: BSTNode | None) -> None:
        if node is None:
            return

        values.append(str(node.value))
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return " ".join(values)


def deserialize_bst(data: str) -> BSTNode | None:
    """
    Reconstruct a BST from its preorder representation.
    Bounds ensure that each value is placed in the correct subtree.
    """
    if not data.strip():
        return None

    try:
        values = [int(value) for value in data.split()]
    except ValueError as error:
        raise ValueError("Serialized data must contain integers.") from error

    index = 0

    def build(
        lower: int | None,
        upper: int | None,
    ) -> BSTNode | None:
        nonlocal index

        if index >= len(values):
            return None

        value = values[index]

        if lower is not None and value <= lower:
            return None

        if upper is not None and value >= upper:
            return None

        index += 1
        node = BSTNode(value)

        node.left = build(lower, value)
        node.right = build(value, upper)

        return node

    root = build(None, None)

    if index != len(values):
        raise ValueError("Input is not a valid BST preorder traversal.")

    return root


def inorder_bst(root: BSTNode | None) -> list[int]:
    """Return inorder traversal of a BST."""
    result: list[int] = []

    def inorder(node: BSTNode | None) -> None:
        if node is None:
            return

        inorder(node.left)
        result.append(node.value)
        inorder(node.right)

    inorder(root)
    return result


def program_150() -> None:
    print("\n--- Program 150: Serialize and Deserialize BST ---")

    root: BSTNode | None = None
    values = read_integer_list("Enter unique BST values: ")

    if len(values) != len(set(values)):
        print("Please enter unique values only.")
        return

    for value in values:
        root = bst_insert(root, value)

    serialized = serialize_bst(root)

    print("Serialized BST:", serialized)

    reconstructed = deserialize_bst(serialized)

    print("Deserialized BST inorder traversal:")
    print(inorder_bst(reconstructed))

    print("Original inorder traversal:")
    print(inorder_bst(root))

    print(
        "Reconstruction successful:",
        inorder_bst(root) == inorder_bst(reconstructed),
    )


# ============================================================
# MAIN MENU
# ============================================================

def run_all() -> None:
    program_146()
    program_147()
    program_148()
    program_149()
    program_150()


def main() -> None:
    while True:
        print("\n========== DAY 30: MONTH 10 MASTER CHALLENGE ==========")
        print("146. LRU Cache")
        print("147. Merge K Sorted Lists")
        print("148. Binary Tree Maximum Path Sum")
        print("149. Median from Data Stream")
        print("150. Serialize and Deserialize BST")
        print("151. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "146":
            program_146()
        elif choice == "147":
            program_147()
        elif choice == "148":
            program_148()
        elif choice == "149":
            program_149()
        elif choice == "150":
            program_150()
        elif choice == "151":
            run_all()
        elif choice == "0":
            print("Month 10 Master Challenge completed. Congratulations!")
            break
        else:
            print("Invalid choice. Please select 146–151 or 0.")


if __name__ == "__main__":
    main()
