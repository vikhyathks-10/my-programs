
from __future__ import annotations


class Heap:
    """A min heap or max heap implemented from scratch."""

    def __init__(
        self,
        values: list[int] | None = None,
        is_min_heap: bool = True,
    ) -> None:
        self.data: list[int] = values.copy() if values is not None else []
        self.is_min_heap = is_min_heap
        self.build_heap()

    def _has_higher_priority(self, first: int, second: int) -> bool:
        """Check which value should appear closer to the root."""
        if self.is_min_heap:
            return first < second
        return first > second

    def _sift_up(self, index: int) -> None:
        """Move a newly inserted value towards the root if needed."""
        while index > 0:
            parent = (index - 1) // 2

            if self._has_higher_priority(
                self.data[index], self.data[parent]
            ):
                self.data[index], self.data[parent] = (
                    self.data[parent],
                    self.data[index],
                )
                index = parent
            else:
                break

    def _sift_down(self, index: int) -> None:
        """Restore heap order by moving a value downwards."""
        size = len(self.data)

        while True:
            best = index
            left = 2 * index + 1
            right = 2 * index + 2

            if (
                left < size
                and self._has_higher_priority(
                    self.data[left], self.data[best]
                )
            ):
                best = left

            if (
                right < size
                and self._has_higher_priority(
                    self.data[right], self.data[best]
                )
            ):
                best = right

            if best == index:
                break

            self.data[index], self.data[best] = (
                self.data[best],
                self.data[index],
            )
            index = best

    def build_heap(self) -> None:
        """Convert the current list into a heap in O(n) time."""
        for index in range(len(self.data) // 2 - 1, -1, -1):
            self._sift_down(index)

    def insert(self, value: int) -> None:
        """Insert a value into the heap."""
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def delete_root(self) -> int | None:
        """Remove and return the root, or None if the heap is empty."""
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        root_value = self.data[0]
        self.data[0] = self.data.pop()
        self._sift_down(0)
        return root_value

    def peek(self) -> int | None:
        """Return the root without removing it."""
        if not self.data:
            return None
        return self.data[0]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def display(self) -> None:
        print("Heap array:", self.data)


def read_integer_list(prompt: str) -> list[int]:
    """Read a space-separated list of integers."""
    while True:
        try:
            text = input(prompt).strip()
            if not text:
                return []
            return [int(item) for item in text.split()]
        except ValueError:
            print("Invalid input. Please enter integers only.")


def read_integer(prompt: str) -> int:
    """Read one integer safely."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def read_heap_type() -> bool:
    """Return True for min heap and False for max heap."""
    while True:
        choice = input("Choose heap type (min/max): ").strip().lower()

        if choice in ("min", "m"):
            return True
        if choice in ("max", "x"):
            return False

        print("Please enter min or max.")


# Program 121: Implement a Min Heap from Scratch
def program_121() -> None:
    print("\n--- Program 121: Min Heap from Scratch ---")
    values = read_integer_list("Enter heap values: ")

    heap = Heap(values, is_min_heap=True)

    print("Min heap created.")
    heap.display()
    print("Minimum value (root):", heap.peek())


# Program 122: Implement a Max Heap from Scratch
def program_122() -> None:
    print("\n--- Program 122: Max Heap from Scratch ---")
    values = read_integer_list("Enter heap values: ")

    heap = Heap(values, is_min_heap=False)

    print("Max heap created.")
    heap.display()
    print("Maximum value (root):", heap.peek())


# Program 123: Implement Heap Insertion and Deletion
def program_123() -> None:
    print("\n--- Program 123: Heap Insertion and Deletion ---")
    is_min_heap = read_heap_type()
    values = read_integer_list("Enter initial heap values: ")
    heap = Heap(values, is_min_heap)

    print("Initial heap:")
    heap.display()

    while True:
        print("\n1. Insert a value")
        print("2. Delete the root")
        print("3. Peek at the root")
        print("4. Display heap")
        print("0. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = read_integer("Enter value to insert: ")
            heap.insert(value)
            print("After insertion:")
            heap.display()

        elif choice == "2":
            removed = heap.delete_root()

            if removed is None:
                print("Heap is empty. Nothing to delete.")
            else:
                print("Deleted root:", removed)
                heap.display()

        elif choice == "3":
            root_value = heap.peek()

            if root_value is None:
                print("Heap is empty.")
            else:
                print("Root value:", root_value)

        elif choice == "4":
            heap.display()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")


# Program 124: Convert an Array into a Heap
def program_124() -> None:
    print("\n--- Program 124: Convert Array into a Heap ---")
    values = read_integer_list("Enter array values: ")
    is_min_heap = read_heap_type()

    heap = Heap(values, is_min_heap)

    print("Original array:", values)
    print("Converted heap:")
    heap.display()

    if heap.is_empty():
        print("The array is empty.")
    else:
        print("Root value:", heap.peek())


# Program 125: Implement Heap Sort
def heap_sort(values: list[int]) -> list[int]:
    """Return the values in ascending order using heap sort."""
    heap = Heap(values, is_min_heap=False)
    sorted_values: list[int] = []

    while not heap.is_empty():
        value = heap.delete_root()
        if value is not None:
            sorted_values.append(value)

    return sorted_values


def program_125() -> None:
    print("\n--- Program 125: Heap Sort ---")
    values = read_integer_list("Enter numbers to sort: ")

    print("Original array:", values)
    print("Sorted array:", heap_sort(values))


def run_all() -> None:
    program_121()
    program_122()
    program_123()
    program_124()
    program_125()


def main() -> None:
    while True:
        print("\n========== DAY 25: HEAP FUNDAMENTALS ==========")
        print("121. Implement a Min Heap")
        print("122. Implement a Max Heap")
        print("123. Heap Insertion and Deletion")
        print("124. Convert an Array into a Heap")
        print("125. Heap Sort")
        print("126. Run All Programs")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "121":
            program_121()
        elif choice == "122":
            program_122()
        elif choice == "123":
            program_123()
        elif choice == "124":
            program_124()
        elif choice == "125":
            program_125()
        elif choice == "126":
            run_all()
        elif choice == "0":
            print("Exiting Day 25 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 121–126 or 0.")


if __name__ == "__main__":
    main()
