
# MONTH 10 - DAY 2
# Linked List Deletion
# Programs 6-10

from __future__ import annotations


# ---------------------------------------------------------
# NODE CLASS
# ---------------------------------------------------------
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None


# ---------------------------------------------------------
# SINGLY LINKED LIST CLASS
# ---------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    # Create a linked list
    def create(self, values: list[int]):
        self.head = None

        for value in values:
            self.insert_end(value)

        print("Linked list created successfully.")

    # Display linked list
    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        current = self.head
        print("Linked list:", end=" ")

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # Helper: Insert at end
    def insert_end(self, value: int):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # 6. Delete the first node
    def delete_first(self):
        if self.head is None:
            print("Linked list is empty. Nothing to delete.")
            return

        deleted_value = self.head.data
        self.head = self.head.next

        print("Deleted first node:", deleted_value)

    # 7. Delete the last node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty. Nothing to delete.")
            return

        # Only one node
        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            print("Deleted last node:", deleted_value)
            return

        current = self.head

        # Stop at the second-last node
        while current.next is not None and current.next.next is not None:
            current = current.next

        # Delete the last node
        last_node = current.next

        if last_node is None:
            return

        deleted_value = last_node.data
        current.next = None

        print("Deleted last node:", deleted_value)

    # 8. Delete a node at a given position (1-based)
    def delete_position(self, position: int):
        if position < 1:
            print("Invalid position.")
            return

        if self.head is None:
            print("Linked list is empty. Nothing to delete.")
            return

        # Delete first node
        if position == 1:
            self.delete_first()
            return

        current = self.head

        # Move to the node just before the target
        for _ in range(position - 2):
            if current.next is None:
                print("Position out of range.")
                return

            current = current.next

        target = current.next

        if target is None:
            print("Position out of range.")
            return

        deleted_value = target.data
        current.next = target.next

        print("Deleted node at position", position, ":", deleted_value)

    # 9. Delete the first node with a given value
    def delete_value(self, value: int):
        if self.head is None:
            print("Linked list is empty. Nothing to delete.")
            return

        # Check the head node
        if self.head.data == value:
            self.head = self.head.next
            print("Deleted node with value:", value)
            return

        current = self.head

        while current.next is not None:
            target = current.next

            if target.data == value:
                current.next = target.next
                print("Deleted node with value:", value)
                return

            current = target

        print("Value not found.")

    # 10. Delete all occurrences of a given value
    def delete_all_occurrences(self, value: int):
        deleted_count = 0

        # Remove matching nodes from the beginning
        while self.head is not None and self.head.data == value:
            self.head = self.head.next
            deleted_count += 1

        # Remove matching nodes from the rest of the list
        current = self.head

        while current is not None and current.next is not None:
            target = current.next

            if target.data == value:
                current.next = target.next
                deleted_count += 1
            else:
                current = target

        if deleted_count == 0:
            print("Value not found.")
        else:
            print("Deleted", deleted_count, "occurrence(s) of", value)


# ---------------------------------------------------------
# PROGRAM FUNCTIONS
# ---------------------------------------------------------

# Program 6: Delete the first node
def program_6(linked_list: LinkedList):
    linked_list.delete_first()
    linked_list.display()


# Program 7: Delete the last node
def program_7(linked_list: LinkedList):
    linked_list.delete_last()
    linked_list.display()


# Program 8: Delete at a given position
def program_8(linked_list: LinkedList):
    position = int(input("Enter position to delete (starting from 1): "))
    linked_list.delete_position(position)
    linked_list.display()


# Program 9: Delete a node with a given value
def program_9(linked_list: LinkedList):
    value = int(input("Enter value to delete: "))
    linked_list.delete_value(value)
    linked_list.display()


# Program 10: Delete all occurrences
def program_10(linked_list: LinkedList):
    value = int(input("Enter value to delete completely: "))
    linked_list.delete_all_occurrences(value)
    linked_list.display()


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():
    linked_list = LinkedList()

    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 2: LINKED LIST DELETION")
        print("======================================")
        print("1. Create linked list")
        print("2. Display linked list")
        print("3. Delete first node (Program 6)")
        print("4. Delete last node (Program 7)")
        print("5. Delete node at position (Program 8)")
        print("6. Delete node by value (Program 9)")
        print("7. Delete all occurrences (Program 10)")
        print("8. Run all deletion programs")
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
                program_6(linked_list)

            elif choice == 4:
                program_7(linked_list)

            elif choice == 5:
                program_8(linked_list)

            elif choice == 6:
                program_9(linked_list)

            elif choice == 7:
                program_10(linked_list)

            elif choice == 8:
                print("\nRunning all deletion programs...")

                print("\nProgram 6: Delete first node")
                program_6(linked_list)

                print("\nProgram 7: Delete last node")
                program_7(linked_list)

                print("\nProgram 8: Delete at position")
                program_8(linked_list)

                print("\nProgram 9: Delete by value")
                program_9(linked_list)

                print("\nProgram 10: Delete all occurrences")
                program_10(linked_list)

            elif choice == 9:
                print("Exiting Month 10 - Day 2. Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()