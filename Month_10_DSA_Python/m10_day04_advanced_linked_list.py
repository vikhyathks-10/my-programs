
# MONTH 10 - DAY 4
# Advanced Linked List Operations
# Programs 16-20

from __future__ import annotations


# ---------------------------------------------------------
# NODE CLASS
# ---------------------------------------------------------
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


# ---------------------------------------------------------
# SINGLY LINKED LIST CLASS
# ---------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    # Create a linked list
    def create(self, values: list[int]) -> None:
        self.head = None

        for value in values:
            self.insert_end(value)

        print("Linked list created successfully.")

    # Insert a node at the end
    def insert_end(self, value: int) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current: Node = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Display linked list safely (also handles cycles)
    def display(self) -> None:
        if self.head is None:
            print("Linked list is empty.")
            return

        current: Node | None = self.head
        visited: set[int] = set()

        print("Linked list:", end=" ")

        while current is not None:
            if id(current) in visited:
                print(f"(cycle back to {current.data})")
                return

            visited.add(id(current))
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # 16. Detect a cycle
    def detect_cycle(self) -> bool:
        slow: Node | None = self.head
        fast: Node | None = self.head

        while fast is not None and fast.next is not None:
            if slow is None:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

    # 17. Find the starting node of a cycle
    def cycle_start(self) -> Node | None:
        slow: Node | None = self.head
        fast: Node | None = self.head

        # First, find the meeting point
        while fast is not None and fast.next is not None:
            if slow is None:
                return None

            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            return None

        # Move one pointer to head.
        # Advance both one step at a time.
        first: Node | None = self.head
        second: Node | None = slow

        while first is not second:
            if first is None or second is None:
                return None

            first = first.next
            second = second.next

        return first

    # 18. Remove a cycle
    def remove_cycle(self) -> bool:
        start = self.cycle_start()

        if start is None:
            print("No cycle found.")
            return False

        # Find the last node in the cycle
        current: Node = start

        while current.next is not start:
            if current.next is None:
                return False

            current = current.next

        current.next = None
        print("Cycle removed successfully.")
        return True

    # 19. Remove duplicates from a sorted linked list
    def remove_duplicates(self) -> None:
        if self.head is None:
            print("Linked list is empty.")
            return

        current: Node = self.head
        removed = 0

        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
                removed += 1
            else:
                current = current.next

        print("Duplicates removed:", removed)

    # 20. Merge two sorted linked lists
    @staticmethod
    def merge_sorted(
        list1: LinkedList,
        list2: LinkedList
    ) -> LinkedList:
        merged = LinkedList()

        first: Node | None = list1.head
        second: Node | None = list2.head

        dummy = Node(0)
        tail: Node = dummy

        while first is not None and second is not None:
            if first.data <= second.data:
                tail.next = Node(first.data)
                first = first.next
            else:
                tail.next = Node(second.data)
                second = second.next

            next_tail = tail.next
            if next_tail is not None:
                tail = next_tail

        while first is not None:
            tail.next = Node(first.data)
            next_tail = tail.next
            if next_tail is not None:
                tail = next_tail
            first = first.next

        while second is not None:
            tail.next = Node(second.data)
            next_tail = tail.next
            if next_tail is not None:
                tail = next_tail
            second = second.next

        merged.head = dummy.next
        return merged


# ---------------------------------------------------------
# HELPER FUNCTION: CREATE A CYCLE
# ---------------------------------------------------------
def create_cycle(linked_list: LinkedList, position: int) -> bool:
    """
    Connect the last node to the node at the given
    1-based position. Position 0 means no cycle.
    """
    if position == 0:
        print("No cycle created.")
        return False

    if position < 1:
        print("Invalid position.")
        return False

    if linked_list.head is None:
        print("Cannot create a cycle in an empty list.")
        return False

    current: Node | None = linked_list.head
    target: Node | None = None
    last: Node | None = None
    index = 1

    while current is not None:
        if index == position:
            target = current

        last = current
        current = current.next
        index += 1

    if target is None or last is None:
        print("Position out of range.")
        return False

    last.next = target
    print(f"Cycle created at position {position}.")
    return True


# ---------------------------------------------------------
# PROGRAM FUNCTIONS
# ---------------------------------------------------------

# Program 16: Detect a cycle
def program_16(linked_list: LinkedList) -> None:
    if linked_list.detect_cycle():
        print("Cycle detected in the linked list.")
    else:
        print("No cycle detected.")


# Program 17: Find the starting node of a cycle
def program_17(linked_list: LinkedList) -> None:
    start = linked_list.cycle_start()

    if start is None:
        print("No cycle exists.")
    else:
        print("Cycle starts at node with value:", start.data)


# Program 18: Remove a cycle
def program_18(linked_list: LinkedList) -> None:
    linked_list.remove_cycle()
    linked_list.display()


# Program 19: Remove duplicates from a sorted list
def program_19(linked_list: LinkedList) -> None:
    linked_list.remove_duplicates()
    linked_list.display()


# Program 20: Merge two sorted linked lists
def program_20() -> None:
    values1 = list(map(
        int,
        input("Enter first sorted list: ").split()
    ))
    values2 = list(map(
        int,
        input("Enter second sorted list: ").split()
    ))

    list1 = LinkedList()
    list2 = LinkedList()

    list1.create(values1)
    list2.create(values2)

    print("\nFirst sorted list:")
    list1.display()

    print("Second sorted list:")
    list2.display()

    merged = LinkedList.merge_sorted(list1, list2)

    print("Merged sorted list:")
    merged.display()


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main() -> None:
    linked_list = LinkedList()

    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 4")
        print(" ADVANCED LINKED LIST OPERATIONS")
        print("======================================")
        print("1. Create linked list")
        print("2. Display linked list")
        print("3. Create a cycle for testing")
        print("4. Detect a cycle (Program 16)")
        print("5. Find cycle starting node (Program 17)")
        print("6. Remove cycle (Program 18)")
        print("7. Remove duplicates (Program 19)")
        print("8. Merge two sorted lists (Program 20)")
        print("9. Run all programs")
        print("10. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        try:
            if choice == 1:
                values = list(map(
                    int,
                    input("Enter elements separated by spaces: ").split()
                ))
                linked_list.create(values)
                linked_list.display()

            elif choice == 2:
                linked_list.display()

            elif choice == 3:
                position = int(input(
                    "Enter position for cycle (0 for no cycle): "
                ))
                create_cycle(linked_list, position)

            elif choice == 4:
                program_16(linked_list)

            elif choice == 5:
                program_17(linked_list)

            elif choice == 6:
                program_18(linked_list)

            elif choice == 7:
                program_19(linked_list)

            elif choice == 8:
                program_20()

            elif choice == 9:
                print("\nRunning all programs...")

                print("\nProgram 16: Detect a cycle")
                program_16(linked_list)

                print("\nProgram 17: Find cycle start")
                program_17(linked_list)

                print("\nProgram 18: Remove a cycle")
                program_18(linked_list)

                print("\nProgram 19: Remove duplicates")
                program_19(linked_list)

                print("\nProgram 20: Merge sorted lists")
                program_20()

            elif choice == 10:
                print("Exiting Month 10 - Day 4. Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()
