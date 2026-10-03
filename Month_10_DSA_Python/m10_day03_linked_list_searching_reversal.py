
# MONTH 10 - DAY 3
# Linked List Searching and Reversal
# Programs 11-15

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

    # Display linked list
    def display(self) -> None:
        if self.head is None:
            print("Linked list is empty.")
            return

        current: Node = self.head
        print("Linked list:", end=" ")

        while True:
            print(current.data, end=" -> ")

            if current.next is None:
                break

            current = current.next

        print("None")

    # 11. Search for an element
    def search(self, target: int) -> int:
        current: Node | None = self.head
        position = 1

        while current is not None:
            if current.data == target:
                return position

            current = current.next
            position += 1

        return -1

    # 12. Find the middle node
    def find_middle(self) -> int | None:
        if self.head is None:
            return None

        slow: Node = self.head
        fast: Node | None = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[assignment]
            fast = fast.next.next

        return slow.data

    # 13. Reverse iteratively
    def reverse_iterative(self) -> None:
        previous: Node | None = None
        current: Node | None = self.head

        while current is not None:
            next_node: Node | None = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
        print("Linked list reversed iteratively.")

    # 14. Reverse recursively
    def reverse_recursive(self) -> None:
        def reverse(node: Node | None) -> Node | None:
            if node is None or node.next is None:
                return node

            next_node: Node = node.next
            new_head = reverse(next_node)

            next_node.next = node
            node.next = None

            return new_head

        self.head = reverse(self.head)
        print("Linked list reversed recursively.")

    # 15. Find Nth node from the end
    def nth_from_end(self, n: int) -> int | None:
        if n <= 0:
            return None

        first: Node | None = self.head
        second: Node | None = self.head

        # Move first pointer n steps ahead
        for _ in range(n):
            if first is None:
                return None

            first = first.next

        # Move both pointers together
        while first is not None:
            first = first.next

            if second is not None:
                second = second.next

        if second is None:
            return None

        return second.data


# ---------------------------------------------------------
# PROGRAM FUNCTIONS
# ---------------------------------------------------------

# Program 11: Search for an element
def program_11(linked_list: LinkedList) -> None:
    target = int(input("Enter element to search: "))
    position = linked_list.search(target)

    if position == -1:
        print("Element not found.")
    else:
        print(f"Element found at position {position}.")


# Program 12: Find the middle node
def program_12(linked_list: LinkedList) -> None:
    middle = linked_list.find_middle()

    if middle is None:
        print("Linked list is empty.")
    else:
        print("Middle node value:", middle)


# Program 13: Reverse iteratively
def program_13(linked_list: LinkedList) -> None:
    linked_list.reverse_iterative()
    linked_list.display()


# Program 14: Reverse recursively
def program_14(linked_list: LinkedList) -> None:
    linked_list.reverse_recursive()
    linked_list.display()


# Program 15: Find Nth node from the end
def program_15(linked_list: LinkedList) -> None:
    n = int(input("Enter N (position from the end): "))
    result = linked_list.nth_from_end(n)

    if result is None:
        print("Invalid N or linked list is empty.")
    else:
        print(f"{n}th node from the end:", result)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main() -> None:
    linked_list = LinkedList()

    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 3: LINKED LIST")
        print(" SEARCHING AND REVERSAL")
        print("======================================")
        print("1. Create linked list")
        print("2. Display linked list")
        print("3. Search element (Program 11)")
        print("4. Find middle node (Program 12)")
        print("5. Reverse iteratively (Program 13)")
        print("6. Reverse recursively (Program 14)")
        print("7. Find Nth node from end (Program 15)")
        print("8. Run all programs")
        print("9. Exit")
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
                program_11(linked_list)

            elif choice == 4:
                program_12(linked_list)

            elif choice == 5:
                program_13(linked_list)

            elif choice == 6:
                program_14(linked_list)

            elif choice == 7:
                program_15(linked_list)

            elif choice == 8:
                print("\nRunning all programs...")

                print("\nProgram 11: Search")
                program_11(linked_list)

                print("\nProgram 12: Find middle")
                program_12(linked_list)

                print("\nProgram 13: Reverse iteratively")
                program_13(linked_list)

                print("\nProgram 14: Reverse recursively")
                program_14(linked_list)

                print("\nProgram 15: Nth node from end")
                program_15(linked_list)

            elif choice == 9:
                print("Exiting Month 10 - Day 3. Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()