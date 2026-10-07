# MONTH 10 - DAY 7
# WEEK 1 REVISION
# Programs 31-35

from __future__ import annotations


# ---------------------------------------------------------
# NODE CLASS
# ---------------------------------------------------------
class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


# ---------------------------------------------------------
# LINKED LIST CLASS
# ---------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    # -----------------------------------------------------
    # Create linked list
    # -----------------------------------------------------
    def create(self, values: list[int]) -> None:
        self.head = None

        for value in values:
            self.insert_end(value)

    # -----------------------------------------------------
    # Insert at end
    # -----------------------------------------------------
    def insert_end(self, value: int) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current: Node = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # -----------------------------------------------------
    # Display linked list
    # -----------------------------------------------------
    def display(self) -> None:
        if self.head is None:
            print("Linked list is empty.")
            return

        current: Node | None = self.head

        print("Linked list:", end=" ")

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    # =====================================================
    # PROGRAM 31
    # Find middle using slow and fast pointers
    # =====================================================
    def find_middle(self) -> int | None:
        if self.head is None:
            return None

        slow: Node = self.head
        fast: Node | None = self.head

        while fast is not None and fast.next is not None:
            next_slow = slow.next

            if next_slow is None:
                break

            slow = next_slow
            fast = fast.next.next

        return slow.data

    # =====================================================
    # PROGRAM 32
    # Find intersection of two sorted linked lists
    # =====================================================
    @staticmethod
    def intersection_sorted(
        list1: LinkedList,
        list2: LinkedList
    ) -> LinkedList:

        result = LinkedList()

        first: Node | None = list1.head
        second: Node | None = list2.head

        while first is not None and second is not None:

            if first.data == second.data:
                result.insert_end(first.data)
                first = first.next
                second = second.next

            elif first.data < second.data:
                first = first.next

            else:
                second = second.next

        return result

    # =====================================================
    # PROGRAM 33
    # Sort linked list using merge sort
    # =====================================================
    def merge_sort(self) -> None:
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head: Node | None) -> Node | None:

        # Base case
        if head is None or head.next is None:
            return head

        # Find middle
        slow: Node = head
        fast: Node | None = head.next

        while fast is not None and fast.next is not None:
            next_slow = slow.next

            if next_slow is None:
                break

            slow = next_slow
            fast = fast.next.next

        # Split the list
        second_head: Node | None = slow.next
        slow.next = None

        # Sort both halves
        left = self._merge_sort(head)
        right = self._merge_sort(second_head)

        # Merge sorted halves
        return self._merge(left, right)

    def _merge(
        self,
        first: Node | None,
        second: Node | None
    ) -> Node | None:

        dummy = Node(0)
        tail: Node = dummy

        while first is not None and second is not None:

            if first.data <= second.data:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next

            next_tail = tail.next

            if next_tail is not None:
                tail = next_tail

        if first is not None:
            tail.next = first

        elif second is not None:
            tail.next = second

        return dummy.next

    # =====================================================
    # PROGRAM 34
    # Remove Nth node from end in one traversal
    # =====================================================
    def remove_nth_from_end(self, n: int) -> bool:

        if n <= 0:
            return False

        # Dummy node makes deletion of the first node easier
        dummy = Node(0)
        dummy.next = self.head

        first: Node | None = dummy
        second: Node | None = dummy

        # Move first pointer n+1 positions ahead
        for _ in range(n + 1):

            if first is None:
                return False

            first = first.next

        # Move both pointers together
        while first is not None:

            first = first.next

            if second is not None:
                second = second.next

        # second must point to the node before target
        if second is None or second.next is None:
            return False

        second.next = second.next.next

        self.head = dummy.next

        return True

    # =====================================================
    # PROGRAM 35
    # Reorder list: first -> last -> second -> second-last
    # =====================================================
    def reorder(self) -> None:

        if self.head is None or self.head.next is None:
            return

        # -------------------------------------------------
        # Step 1: Find middle
        # -------------------------------------------------
        slow: Node = self.head
        fast: Node | None = self.head

        while fast is not None and fast.next is not None:

            next_slow = slow.next

            if next_slow is None:
                break

            slow = next_slow
            fast = fast.next.next

        # -------------------------------------------------
        # Step 2: Split the list
        # -------------------------------------------------
        second: Node | None = slow.next
        slow.next = None

        # -------------------------------------------------
        # Step 3: Reverse second half
        # -------------------------------------------------
        previous: Node | None = None
        current: Node | None = second

        while current is not None:

            next_node: Node | None = current.next
            current.next = previous
            previous = current
            current = next_node

        second = previous

        # -------------------------------------------------
        # Step 4: Merge alternating nodes
        # -------------------------------------------------
        first: Node | None = self.head

        while first is not None and second is not None:

            first_next: Node | None = first.next
            second_next: Node | None = second.next

            first.next = second
            second.next = first_next

            if first_next is None:
                break

            first = first_next
            second = second_next


# =========================================================
# PROGRAM 31
# =========================================================
def program_31() -> None:

    values = list(map(
        int,
        input("Enter linked list elements: ").split()
    ))

    linked_list = LinkedList()
    linked_list.create(values)

    linked_list.display()

    middle = linked_list.find_middle()

    if middle is None:
        print("Linked list is empty.")
    else:
        print("Middle node:", middle)


# =========================================================
# PROGRAM 32
# =========================================================
def program_32() -> None:

    values1 = list(map(
        int,
        input("Enter first sorted linked list: ").split()
    ))

    values2 = list(map(
        int,
        input("Enter second sorted linked list: ").split()
    ))

    list1 = LinkedList()
    list2 = LinkedList()

    list1.create(values1)
    list2.create(values2)

    print("\nFirst sorted list:")
    list1.display()

    print("Second sorted list:")
    list2.display()

    result = LinkedList.intersection_sorted(list1, list2)

    print("Intersection:")
    result.display()


# =========================================================
# PROGRAM 33
# =========================================================
def program_33() -> None:

    values = list(map(
        int,
        input("Enter linked list elements: ").split()
    ))

    linked_list = LinkedList()
    linked_list.create(values)

    print("\nOriginal list:")
    linked_list.display()

    linked_list.merge_sort()

    print("Sorted linked list:")
    linked_list.display()


# =========================================================
# PROGRAM 34
# =========================================================
def program_34() -> None:

    values = list(map(
        int,
        input("Enter linked list elements: ").split()
    ))

    n = int(input("Enter N (node from the end to remove): "))

    linked_list = LinkedList()
    linked_list.create(values)

    print("\nOriginal list:")
    linked_list.display()

    if linked_list.remove_nth_from_end(n):
        print(f"Removed the {n}th node from the end.")
        print("Updated list:")
        linked_list.display()
    else:
        print("Invalid N. Node could not be removed.")


# =========================================================
# PROGRAM 35
# =========================================================
def program_35() -> None:

    values = list(map(
        int,
        input("Enter linked list elements: ").split()
    ))

    linked_list = LinkedList()
    linked_list.create(values)

    print("\nOriginal list:")
    linked_list.display()

    linked_list.reorder()

    print("Reordered linked list:")
    linked_list.display()


# =========================================================
# RUN ALL PROGRAMS
# =========================================================
def run_all() -> None:

    print("\n======================================")
    print(" PROGRAM 31: FIND MIDDLE")
    print("======================================")
    program_31()

    print("\n======================================")
    print(" PROGRAM 32: INTERSECTION")
    print("======================================")
    program_32()

    print("\n======================================")
    print(" PROGRAM 33: MERGE SORT")
    print("======================================")
    program_33()

    print("\n======================================")
    print(" PROGRAM 34: REMOVE NTH FROM END")
    print("======================================")
    program_34()

    print("\n======================================")
    print(" PROGRAM 35: REORDER LINKED LIST")
    print("======================================")
    program_35()


# =========================================================
# MAIN MENU
# =========================================================
def main() -> None:

    while True:

        print("\n======================================")
        print(" MONTH 10 - DAY 7")
        print(" WEEK 1 LINKED LIST REVISION")
        print("======================================")
        print("31. Find middle using slow and fast pointers")
        print("32. Intersection of two sorted linked lists")
        print("33. Sort linked list using merge sort")
        print("34. Remove Nth node from end")
        print("35. Reorder linked list")
        print("36. Run all programs")
        print("37. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        try:

            if choice == 31:
                program_31()

            elif choice == 32:
                program_32()

            elif choice == 33:
                program_33()

            elif choice == 34:
                program_34()

            elif choice == 35:
                program_35()

            elif choice == 36:
                run_all()

            elif choice == 37:
                print("Exiting Month 10 - Day 7.")
                print("Week 1 completed. Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter integers only.")


# =========================================================
# PROGRAM START
# =========================================================
if __name__ == "__main__":
    main()