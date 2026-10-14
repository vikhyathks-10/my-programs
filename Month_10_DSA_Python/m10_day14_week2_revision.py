
from __future__ import annotations

from collections import deque
from typing import Deque


# ==========================================================
# PROGRAM 66: Simplify a Unix-style file path using a stack
# ==========================================================

def simplify_path() -> None:
    path = input("Enter an absolute Unix-style path: ").strip()

    if not path.startswith("/"):
        print("Please enter an absolute path beginning with '/'.")
        return

    stack: list[str] = []

    for component in path.split("/"):
        if component == "" or component == ".":
            continue

        if component == "..":
            if stack:
                stack.pop()
        else:
            stack.append(component)

    simplified = "/" + "/".join(stack)
    print("Simplified path:", simplified)


# ==========================================================
# PROGRAM 67: Remove adjacent duplicate characters
# ==========================================================

def remove_adjacent_duplicates() -> None:
    text = input("Enter a string: ")

    stack: list[str] = []

    for char in text:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = "".join(stack)
    print("After removing adjacent duplicates:", result)


# ==========================================================
# PROGRAM 68: Largest rectangular area in a binary matrix
# ==========================================================

def largest_histogram_rectangle(heights: list[int]) -> int:
    """Return the largest rectangle area in a histogram."""
    stack: list[int] = []
    max_area = 0

    # The extra zero flushes all remaining histogram bars.
    extended = heights + [0]

    for i, height in enumerate(extended):
        while stack and extended[stack[-1]] > height:
            bar_height = extended[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            max_area = max(max_area, bar_height * width)

        stack.append(i)

    return max_area


def largest_binary_matrix_rectangle() -> None:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be positive.")
        return

    matrix: list[list[int]] = []

    print("Enter each row as", cols, "binary values separated by spaces:")

    for row_index in range(rows):
        row = list(
            map(
                int,
                input(f"Row {row_index + 1}: ").split()
            )
        )

        if len(row) != cols or any(value not in (0, 1) for value in row):
            print("Invalid row. Enter exactly", cols, "values, each 0 or 1.")
            return

        matrix.append(row)

    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for col in range(cols):
            if row[col] == 1:
                heights[col] += 1
            else:
                heights[col] = 0

        max_area = max(
            max_area,
            largest_histogram_rectangle(heights)
        )

    print("Largest rectangular area of 1s:", max_area)


# ==========================================================
# PROGRAM 69: Recent counter using a queue
# ==========================================================

class RecentCounter:
    """Count requests in the inclusive interval [t - 3000, t]."""

    def __init__(self) -> None:
        self.requests: Deque[int] = deque()
        self.last_time: int | None = None

    def ping(self, t: int) -> int:
        if self.last_time is not None and t < self.last_time:
            raise ValueError("Timestamps must be non-decreasing.")

        self.last_time = t
        self.requests.append(t)

        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)


def recent_counter_menu() -> None:
    counter = RecentCounter()

    print("Enter request timestamps in non-decreasing order.")
    print("Type 'q' to return to the main menu.")

    while True:
        entry = input("Enter timestamp t: ").strip()

        if entry.lower() == "q":
            break

        try:
            t = int(entry)
            count = counter.ping(t)
            print("Requests in the last 3000 time units:", count)
        except ValueError as error:
            print("Invalid input:", error)


# ==========================================================
# PROGRAM 70: Browser history using two stacks
# ==========================================================

class BrowserHistory:
    """Browser history with back and forward navigation."""

    def __init__(self, homepage: str) -> None:
        self.current = homepage
        self.back_stack: list[str] = []
        self.forward_stack: list[str] = []

    def visit(self, url: str) -> None:
        self.back_stack.append(self.current)
        self.current = url

        # Visiting a new page clears the forward history.
        self.forward_stack.clear()

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.back_stack:
                break

            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()

        return self.current

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.forward_stack:
                break

            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()

        return self.current

    def show_history(self) -> None:
        print("Back history (oldest to newest):", self.back_stack)
        print("Current page:", self.current)
        print("Forward history (nearest first):", list(reversed(self.forward_stack)))


def browser_history_menu() -> None:
    homepage = input("Enter homepage URL: ").strip()

    if not homepage:
        print("Homepage cannot be empty.")
        return

    browser = BrowserHistory(homepage)

    while True:
        print("\n--- BROWSER HISTORY ---")
        print("1. Visit a new page")
        print("2. Go back")
        print("3. Go forward")
        print("4. Show current page")
        print("5. Display history")
        print("0. Return to main menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            url = input("Enter URL to visit: ").strip()

            if url:
                browser.visit(url)
                print("Current page:", browser.current)
            else:
                print("URL cannot be empty.")

        elif choice == "2":
            steps = int(input("Number of steps back: "))

            if steps < 0:
                print("Steps cannot be negative.")
            else:
                print("Current page:", browser.back(steps))

        elif choice == "3":
            steps = int(input("Number of steps forward: "))

            if steps < 0:
                print("Steps cannot be negative.")
            else:
                print("Current page:", browser.forward(steps))

        elif choice == "4":
            print("Current page:", browser.current)

        elif choice == "5":
            browser.show_history()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


# ==========================================================
# MAIN MENU: PROGRAMS 66-70
# ==========================================================

def main() -> None:
    programs = {
        "66": ("Simplify a Unix-style file path", simplify_path),
        "67": ("Remove adjacent duplicate characters", remove_adjacent_duplicates),
        "68": ("Largest rectangle in a binary matrix",
               largest_binary_matrix_rectangle),
        "69": ("Recent counter using a queue", recent_counter_menu),
        "70": ("Browser history using two stacks", browser_history_menu),
    }

    while True:
        print("\n========== MONTH 10 - DAY 14 ==========")

        for number, (description, _) in programs.items():
            print(f"{number}. {description}")

        print("71. Run all programs (66-70)")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Week 2 revision completed. Keep practising!")
            break

        elif choice == "71":
            for number, (description, function) in programs.items():
                print(f"\n--- Program {number}: {description} ---")
                function()

        elif choice in programs:
            description, function = programs[choice]
            print(f"\n--- Program {choice}: {description} ---")
            function()

        else:
            print("Invalid choice. Enter 66-71 or 0.")


if __name__ == "__main__":
    main()
