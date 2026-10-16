
from __future__ import annotations

from collections import defaultdict


# ==========================================================
# PROGRAM 76: Longest substring with exactly K distinct chars
# ==========================================================

def longest_substring_k_distinct() -> None:
    text = input("Enter a string: ")
    k = int(input("Enter K (number of distinct characters): "))

    if k <= 0:
        print("K must be positive.")
        return

    frequency: dict[str, int] = {}
    left = 0
    best_length = 0
    best_start = 0

    for right, char in enumerate(text):
        frequency[char] = frequency.get(char, 0) + 1

        # Shrink until the window has at most K distinct characters.
        while len(frequency) > k:
            left_char = text[left]
            frequency[left_char] -= 1

            if frequency[left_char] == 0:
                del frequency[left_char]

            left += 1

        # Record only windows containing exactly K distinct characters.
        if len(frequency) == k:
            window_length = right - left + 1

            if window_length > best_length:
                best_length = window_length
                best_start = left

    if best_length == 0:
        print(f"No substring has exactly {k} distinct characters.")
    else:
        result = text[best_start:best_start + best_length]
        print("Longest substring:", result)
        print("Length:", best_length)


# ==========================================================
# PROGRAM 77: Longest subarray with equal 0s and 1s
# ==========================================================

def longest_equal_zeros_ones() -> None:
    values = list(
        map(int, input("Enter an array containing only 0s and 1s: ").split())
    )

    if any(value not in (0, 1) for value in values):
        print("Invalid input. Only 0 and 1 are allowed.")
        return

    # Convert 0 to -1. Equal numbers of 0s and 1s then sum to zero.
    prefix_sum = 0
    first_occurrence: dict[int, int] = {0: -1}
    best_length = 0
    best_start = -1
    best_end = -1

    for index, value in enumerate(values):
        prefix_sum += 1 if value == 1 else -1

        if prefix_sum in first_occurrence:
            length = index - first_occurrence[prefix_sum]

            if length > best_length:
                best_length = length
                best_start = first_occurrence[prefix_sum] + 1
                best_end = index
        else:
            # Keep the earliest occurrence for the longest possible range.
            first_occurrence[prefix_sum] = index

    print("Longest length:", best_length)

    if best_length > 0:
        print("Subarray:", values[best_start:best_end + 1])
        print(f"Indices: {best_start} to {best_end}")
    else:
        print("No non-empty subarray has equal numbers of 0s and 1s.")


# ==========================================================
# PROGRAM 78: Count pairs with a given sum using hashing
# ==========================================================

def count_pairs_with_sum() -> None:
    values = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target sum: "))

    frequency: dict[int, int] = {}
    pair_count = 0

    for value in values:
        complement = target - value

        # Each previous occurrence of the complement forms one pair.
        pair_count += frequency.get(complement, 0)

        frequency[value] = frequency.get(value, 0) + 1

    print("Number of pairs with sum", target, ":", pair_count)


# ==========================================================
# PROGRAM 79: Longest zero-sum subarray
# ==========================================================

def longest_zero_sum_subarray() -> None:
    values = list(map(int, input("Enter array elements: ").split()))

    prefix_sum = 0
    first_occurrence: dict[int, int] = {0: -1}
    best_length = 0
    best_start = -1
    best_end = -1

    for index, value in enumerate(values):
        prefix_sum += value

        if prefix_sum in first_occurrence:
            length = index - first_occurrence[prefix_sum]

            if length > best_length:
                best_length = length
                best_start = first_occurrence[prefix_sum] + 1
                best_end = index
        else:
            # Preserve the earliest index for this prefix sum.
            first_occurrence[prefix_sum] = index

    print("Longest zero-sum subarray length:", best_length)

    if best_length > 0:
        print("Subarray:", values[best_start:best_end + 1])
        print(f"Indices: {best_start} to {best_end}")
    else:
        print("No non-empty zero-sum subarray exists.")


# ==========================================================
# PROGRAM 80: Design a frequency stack
# ==========================================================

class FrequencyStack:
    """
    Pop removes the most frequent value.
    If frequencies tie, the most recently pushed tied value is removed.
    """

    def __init__(self) -> None:
        self.frequency: dict[int, int] = {}
        self.group_stacks: dict[int, list[int]] = defaultdict(list)
        self.max_frequency = 0
        self.size = 0

    def push(self, value: int) -> None:
        new_frequency = self.frequency.get(value, 0) + 1
        self.frequency[value] = new_frequency

        if new_frequency > self.max_frequency:
            self.max_frequency = new_frequency

        self.group_stacks[new_frequency].append(value)
        self.size += 1

    def pop(self) -> int | None:
        if self.size == 0:
            return None

        values_at_max = self.group_stacks[self.max_frequency]
        value = values_at_max.pop()

        self.frequency[value] -= 1
        self.size -= 1

        if not values_at_max:
            del self.group_stacks[self.max_frequency]
            self.max_frequency -= 1

        return value

    def is_empty(self) -> bool:
        return self.size == 0


def frequency_stack_menu() -> None:
    stack = FrequencyStack()

    while True:
        print("\n--- PROGRAM 80: FREQUENCY STACK ---")
        print("1. Push value")
        print("2. Pop most frequent value")
        print("3. Check if empty")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            value = int(input("Enter integer value: "))
            stack.push(value)
            print("Pushed:", value)

        elif choice == "2":
            value = stack.pop()

            if value is None:
                print("Stack is empty.")
            else:
                print("Popped:", value)

        elif choice == "3":
            print("Empty:", stack.is_empty())

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ==========================================================
# MAIN MENU: PROGRAMS 76-80
# ==========================================================

def main() -> None:
    programs = {
        "76": (
            "Longest substring with exactly K distinct characters",
            longest_substring_k_distinct,
        ),
        "77": (
            "Longest subarray with equal 0s and 1s",
            longest_equal_zeros_ones,
        ),
        "78": (
            "Count pairs with a given sum",
            count_pairs_with_sum,
        ),
        "79": (
            "Longest zero-sum subarray",
            longest_zero_sum_subarray,
        ),
        "80": (
            "Design a frequency stack",
            frequency_stack_menu,
        ),
    }

    while True:
        print("\n========== MONTH 10 - DAY 16 ==========")

        for number, (description, _) in programs.items():
            print(f"{number}. {description}")

        print("81. Run all programs (76-80)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Day 16 practice completed!")
            break

        elif choice == "81":
            for number, (description, function) in programs.items():
                print(f"\n--- Program {number}: {description} ---")
                function()

        elif choice in programs:
            description, function = programs[choice]
            print(f"\n--- Program {choice}: {description} ---")
            function()

        else:
            print("Invalid choice. Enter 76-81 or 0.")


if __name__ == "__main__":
    main()
