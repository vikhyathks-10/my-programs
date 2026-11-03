
from __future__ import annotations


# ============================================================
# PROGRAM 11 — N-QUEENS PROBLEM
# ============================================================

def solve_n_queens(n: int) -> list[list[str]]:
    if n <= 0:
        return []

    result: list[list[str]] = []

    board = [["."] * n for _ in range(n)]

    columns: set[int] = set()
    diagonals1: set[int] = set()  # row - col
    diagonals2: set[int] = set()  # row + col

    def backtrack(row: int) -> None:

        # All queens have been placed.
        if row == n:
            result.append(["".join(line) for line in board])
            return

        for col in range(n):

            if (
                col in columns
                or (row - col) in diagonals1
                or (row + col) in diagonals2
            ):
                continue

            # Place queen.
            board[row][col] = "Q"
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)

            backtrack(row + 1)

            # Backtrack: remove queen.
            board[row][col] = "."
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    backtrack(0)
    return result


def program_11() -> None:
    print("\nPROGRAM 11 — N-QUEENS PROBLEM")

    n = int(input("Enter the value of N: "))

    if n <= 0:
        print("N must be positive.")
        return

    solutions = solve_n_queens(n)

    if not solutions:
        print("No valid arrangements exist.")
        return

    print(f"\nTotal solutions: {len(solutions)}")

    for index, solution in enumerate(solutions, start=1):
        print(f"\nSolution {index}:")

        for row in solution:
            print(" ".join(row))


# ============================================================
# PROGRAM 12 — SUDOKU SOLVER
# ============================================================

def solve_sudoku(board: list[list[int]]) -> bool:
    """
    Solves a 9x9 Sudoku board in place.
    Empty cells are represented by 0.
    Returns True if a solution exists.
    """

    def is_valid(row: int, col: int, number: int) -> bool:

        # Check row.
        for j in range(9):
            if board[row][j] == number:
                return False

        # Check column.
        for i in range(9):
            if board[i][col] == number:
                return False

        # Check 3x3 box.
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == number:
                    return False

        return True

    def backtrack() -> bool:

        # Find the next empty cell.
        for row in range(9):
            for col in range(9):

                if board[row][col] == 0:

                    # Try numbers 1 through 9.
                    for number in range(1, 10):

                        if is_valid(row, col, number):

                            board[row][col] = number

                            if backtrack():
                                return True

                            # Undo the choice.
                            board[row][col] = 0

                    return False

        # No empty cells remain.
        return True

    return backtrack()


def print_sudoku(board: list[list[int]]) -> None:
    print("\n+-------+-------+-------+")

    for i, row in enumerate(board):

        print("|", end=" ")

        for j, number in enumerate(row):
            print(number if number != 0 else ".", end=" ")

            if (j + 1) % 3 == 0:
                print("|", end=" ")

        print()

        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")


def program_12() -> None:
    print("\nPROGRAM 12 — SUDOKU SOLVER")

    print("Enter 9 rows, each containing 9 numbers.")
    print("Use 0 for empty cells.")

    board: list[list[int]] = []

    for i in range(9):
        row = list(map(int, input(f"Row {i + 1}: ").split()))

        if len(row) != 9 or any(number < 0 or number > 9 for number in row):
            print("Invalid row. Enter exactly 9 numbers from 0 to 9.")
            return

        board.append(row)

    # Validate the initially filled cells.
    original_board = [row.copy() for row in board]

    for row in range(9):
        for col in range(9):

            number = board[row][col]

            if number != 0:
                board[row][col] = 0

                valid = True

                # Check whether this number conflicts with another
                # originally filled cell.
                for j in range(9):
                    if board[row][j] == number:
                        valid = False

                for i in range(9):
                    if board[i][col] == number:
                        valid = False

                start_row = (row // 3) * 3
                start_col = (col // 3) * 3

                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if board[i][j] == number:
                            valid = False

                board[row][col] = number

                if not valid:
                    print("Invalid Sudoku: conflicting initial values.")
                    return

    print("\nOriginal Sudoku:")
    print_sudoku(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_sudoku(board)
    else:
        board = original_board
        print("\nNo solution exists for this Sudoku.")


# ============================================================
# PROGRAM 13 — WORD SEARCH: FIND ALL POSSIBLE PATHS
# ============================================================

def find_word_paths(
    grid: list[list[str]],
    word: str
) -> list[list[tuple[int, int]]]:

    if not grid or not grid[0] or not word:
        return []

    rows = len(grid)
    cols = len(grid[0])

    if any(len(row) != cols for row in grid):
        return []

    result: list[list[tuple[int, int]]] = []

    visited = [[False] * cols for _ in range(rows)]

    # Four possible directions.
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    def backtrack(
        row: int,
        col: int,
        index: int,
        path: list[tuple[int, int]]
    ) -> None:

        # Entire word has been matched.
        if index == len(word):
            result.append(path.copy())
            return

        for row_change, col_change in directions:

            new_row = row + row_change
            new_col = col + col_change

            # Check boundaries.
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            # Check character and visited status.
            if (
                not visited[new_row][new_col]
                and grid[new_row][new_col] == word[index]
            ):

                visited[new_row][new_col] = True
                path.append((new_row, new_col))

                backtrack(
                    new_row,
                    new_col,
                    index + 1,
                    path
                )

                # Undo the current choice.
                path.pop()
                visited[new_row][new_col] = False

    # Try every cell as a starting position.
    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == word[0]:

                visited[row][col] = True

                backtrack(
                    row,
                    col,
                    1,
                    [(row, col)]
                )

                visited[row][col] = False

    return result


def program_13() -> None:
    print("\nPROGRAM 13 — WORD SEARCH")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be positive.")
        return

    print("Enter the character grid row by row.")

    grid: list[list[str]] = []

    for i in range(rows):
        row = input(f"Row {i + 1}: ").split()

        if len(row) != cols or any(len(ch) != 1 for ch in row):
            print("Enter exactly", cols, "single characters.")
            return

        grid.append(row)

    word = input("Enter the word to search: ")

    paths = find_word_paths(grid, word)

    print("\nGrid:")

    for row in grid:
        print(" ".join(row))

    if not paths:
        print("\nWord not found.")
        return

    print(f"\nFound {len(paths)} possible path(s):")

    for index, path in enumerate(paths, start=1):
        # Convert zero-based coordinates to one-based coordinates.
        display_path = [
            (row + 1, col + 1)
            for row, col in path
        ]

        print(f"Path {index}: {display_path}")


# ============================================================
# PROGRAM 14 — GENERATE BALANCED PARENTHESES
# ============================================================

def generate_parentheses(n: int) -> list[str]:

    if n < 0:
        return []

    result: list[str] = []

    def backtrack(
        current: str,
        open_count: int,
        close_count: int
    ) -> None:

        # All pairs have been placed.
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add an opening bracket if available.
        if open_count < n:
            backtrack(
                current + "(",
                open_count + 1,
                close_count
            )

        # Add a closing bracket only if it remains balanced.
        if close_count < open_count:
            backtrack(
                current + ")",
                open_count,
                close_count + 1
            )

    backtrack("", 0, 0)
    return result


def program_14() -> None:
    print("\nPROGRAM 14 — BALANCED PARENTHESES")

    n = int(input("Enter number of parenthesis pairs: "))

    if n < 0:
        print("Number of pairs cannot be negative.")
        return

    combinations = generate_parentheses(n)

    print("\nValid combinations:")

    for index, combination in enumerate(combinations, start=1):
        print(f"{index}. {combination}")

    print("Total combinations:", len(combinations))


# ============================================================
# PROGRAM 15 — PALINDROME PARTITIONING
# ============================================================

def palindrome_partitioning(text: str) -> list[list[str]]:

    result: list[list[str]] = []
    current: list[str] = []

    def is_palindrome(value: str) -> bool:
        return value == value[::-1]

    def backtrack(start: int) -> None:

        # Entire string has been partitioned.
        if start == len(text):
            result.append(current.copy())
            return

        # Try every possible next substring.
        for end in range(start + 1, len(text) + 1):

            substring = text[start:end]

            if is_palindrome(substring):

                current.append(substring)

                backtrack(end)

                # Backtracking.
                current.pop()

    backtrack(0)
    return result


def program_15() -> None:
    print("\nPROGRAM 15 — PALINDROME PARTITIONING")

    text = input("Enter a string: ")

    partitions = palindrome_partitioning(text)

    print("\nAll palindrome partitions:")

    for index, partition in enumerate(partitions, start=1):
        print(f"{index}. {partition}")

    print("Total partitions:", len(partitions))


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all() -> None:

    print("\n========== PROGRAM 11 ==========")
    program_11()

    print("\n========== PROGRAM 12 ==========")
    program_12()

    print("\n========== PROGRAM 13 ==========")
    program_13()

    print("\n========== PROGRAM 14 ==========")
    program_14()

    print("\n========== PROGRAM 15 ==========")
    program_15()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    while True:

        print("\n" + "=" * 60)
        print("          MONTH 11 — DAY 3: BACKTRACKING PROBLEMS")
        print("=" * 60)

        print("11. N-Queens Problem")
        print("12. Sudoku Solver")
        print("13. Word Search — All Possible Paths")
        print("14. Generate Balanced Parentheses")
        print("15. Palindrome Partitioning")
        print("16. Run All Programs")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "11":
            program_11()

        elif choice == "12":
            program_12()

        elif choice == "13":
            program_13()

        elif choice == "14":
            program_14()

        elif choice == "15":
            program_15()

        elif choice == "16":
            run_all()

        elif choice == "0":
            print("\nDay 3 Backtracking Problems Completed!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
