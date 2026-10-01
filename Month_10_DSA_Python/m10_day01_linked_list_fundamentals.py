# MONTH 10 - DAY 1
# Linked List Fundamentals
# Programs 1-5

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

    # 1. Create a linked list
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

    # 2. Insert at beginning
    def insert_beginning(self, value: int):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        print("Node inserted at beginning.")

    # 3. Insert at end
    def insert_end(self, value: int):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # 4. Insert at a given position (1-based)
    def insert_position(self, value: int, position: int):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_beginning(value)
            return

        current = self.head

        # Move to the node just before the required position
        for _ in range(position - 2):
            if current is None:
                print("Position out of range.")
                return

            current = current.next

        if current is None:
            print("Position out of range.")
            return

        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

        print("Node inserted at position", position)

    # 5. Count nodes
    def count_nodes(self) -> int:
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count


# ---------------------------------------------------------
# PROGRAM FUNCTIONS
# ---------------------------------------------------------

# Program 1: Create and display linked list
def program_1(linked_list: LinkedList):
    values = list(map(
        int,
        input("Enter elements separated by spaces: ").split()
    ))

    linked_list.create(values)
    linked_list.display()


# Program 2: Insert at beginning
def program_2(linked_list: LinkedList):
    value = int(input("Enter value to insert: "))

    linked_list.insert_beginning(value)
    linked_list.display()


# Program 3: Insert at end
def program_3(linked_list: LinkedList):
    value = int(input("Enter value to insert: "))

    linked_list.insert_end(value)
    print("Node inserted at end.")
    linked_list.display()


# Program 4: Insert at a given position
def program_4(linked_list: LinkedList):
    value = int(input("Enter value to insert: "))
    position = int(input("Enter position (starting from 1): "))

    linked_list.insert_position(value, position)
    linked_list.display()


# Program 5: Count nodes
def program_5(linked_list: LinkedList):
    count = linked_list.count_nodes()
    print("Number of nodes:", count)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():
    linked_list = LinkedList()

    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 1: LINKED LIST")
        print("======================================")
        print("1. Create and display linked list")
        print("2. Insert node at beginning")
        print("3. Insert node at end")
        print("4. Insert node at given position")
        print("5. Count number of nodes")
        print("6. Display current linked list")
        print("7. Run all programs")
        print("8. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        try:
            if choice == 1:
                program_1(linked_list)

            elif choice == 2:
                program_2(linked_list)

            elif choice == 3:
                program_3(linked_list)

            elif choice == 4:
                program_4(linked_list)

            elif choice == 5:
                program_5(linked_list)

            elif choice == 6:
                linked_list.display()

            elif choice == 7:
                print("\nRunning all programs...")

                program_1(linked_list)
                program_2(linked_list)
                program_3(linked_list)
                program_4(linked_list)
                program_5(linked_list)

            elif choice == 8:
                print("Exiting Month 10 - Day 1. Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()