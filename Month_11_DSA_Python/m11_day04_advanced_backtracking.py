
from __future__ import annotations

# ============================================================
# PROGRAM 16 — KNIGHT'S TOUR PROBLEM
# ============================================================

def solve_knights_tour(n: int) -> list[list[int]] | None:
    """
    Find one Knight's Tour on an N x N board.

    Every square must be visited exactly once.
    Returns the numbered board if a solution exists.
    """

    if n <= 0:
        return None

    board = [[-1] * n for _ in range(n)]

    moves = [
        (2, 1), (1, 2),
        (-1, 2), (-2, 1),
        (-2, -1), (-1, -2),
        (1, -2), (2, -1)
    ]

    def is_valid(row: int, col: int) -> bool:
        return (
            0 <= row < n
            and 0 <= col < n
            and board[row][col] == -1
        )

    def count_onward_moves(row: int, col: int) -> int:
        count = 0

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc

            if is_valid(new_row, new_col):
                count += 1

        return count

    def backtrack(row: int, col: int, move_number: int) -> bool:

        board[row][col] = move_number

        # All squares have been visited.
        if move_number == n * n - 1:
            return True

        # Generate valid next moves.
        candidates: list[tuple[int, int, int]] = []

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc

            if is_valid(new_row, new_col):
                onward = count_onward_moves(new_row, new_col)
                candidates.append((onward, new_row, new_col))

        # Warnsdorff's heuristic:
        # Try the square with the fewest onward moves first.
        candidates.sort()

        for _, new_row, new_col in candidates:

            if backtrack(new_row, new_col, move_number + 1):
                return True

        # Backtrack.
        board[row][col] = -1
        return False

    if backtrack(0, 0, 0):
        return board

    return None


def program_16() -> None:
    print("\nPROGRAM 16 — KNIGHT'S TOUR")

    n = int(input("Enter chessboard size N: "))

    if n <= 0:
        print("Board size must be positive.")
        return

    solution = solve_knights_tour(n)

    if solution is None:
        print("No Knight's Tour was found.")
        return

    print("\nKnight's Tour solution:")
    print("Numbers indicate the order of moves.\n")

    for row in solution:
        print(" ".join(f"{value:3}" for value in row))


# ============================================================
# PROGRAM 17 — ALL HAMILTONIAN PATHS IN AN UNDIRECTED GRAPH
# ============================================================

def find_hamiltonian_paths(
    vertices: int,
    edges: list[tuple[int, int]]
) -> list[list[int]]:
    """
    Find all Hamiltonian paths in an undirected graph.

    A Hamiltonian path visits every vertex exactly once.
    Reverse paths are treated as the same path.
    """

    if vertices <= 0:
        return []

    graph: list[list[int]] = [[] for _ in range(vertices)]

    for u, v in edges:

        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError("Edge contains an invalid vertex.")

        if u == v:
            continue

        if v not in graph[u]:
            graph[u].append(v)

        if u not in graph[v]:
            graph[v].append(u)

    for neighbours in graph:
        neighbours.sort()

    result: list[list[int]] = []
    visited = [False] * vertices

    # Store canonical paths to avoid reverse duplicates.
    unique_paths: set[tuple[int, ...]] = set()

    def backtrack(
        current: int,
        path: list[int]
    ) -> None:

        # Every vertex has been visited.
        if len(path) == vertices:

            forward = tuple(path)
            backward = tuple(reversed(path))

            canonical = min(forward, backward)

            if canonical not in unique_paths:
                unique_paths.add(canonical)
                result.append(path.copy())

            return

        for neighbour in graph[current]:

            if not visited[neighbour]:

                visited[neighbour] = True
                path.append(neighbour)

                backtrack(neighbour, path)

                # Backtracking.
                path.pop()
                visited[neighbour] = False

    # Try every vertex as a starting point.
    for start in range(vertices):

        visited[start] = True

        backtrack(start, [start])

        visited[start] = False

    return result


def program_17() -> None:
    print("\nPROGRAM 17 — HAMILTONIAN PATHS")

    vertices = int(input("Enter number of vertices: "))
    edge_count = int(input("Enter number of edges: "))

    if vertices <= 0 or edge_count < 0:
        print("Invalid graph dimensions.")
        return

    print("Enter edges using 0-based vertex numbers.")
    edges: list[tuple[int, int]] = []

    for i in range(edge_count):
        values = list(
            map(int, input(f"Edge {i + 1} (u v): ").split())
        )

        if len(values) != 2:
            print("Each edge must contain exactly two vertices.")
            return

        edges.append((values[0], values[1]))

    try:
        paths = find_hamiltonian_paths(vertices, edges)

        if not paths:
            print("\nNo Hamiltonian path exists.")
            return

        print(f"\nFound {len(paths)} unique Hamiltonian path(s):")

        for index, path in enumerate(paths, start=1):
            print(f"{index}. {' -> '.join(map(str, path))}")

    except ValueError as error:
        print("Error:", error)


# ============================================================
# PROGRAM 18 — WORD BREAK USING BACKTRACKING
# ============================================================

def word_break_all(
    text: str,
    dictionary: list[str]
) -> list[list[str]]:
    """
    Find all ways to divide a string into dictionary words.
    """

    if any(word == "" for word in dictionary):
        raise ValueError("Dictionary words cannot be empty.")

    word_set = set(dictionary)
    result: list[list[str]] = []

    current: list[str] = []

    # Memoize starting positions that cannot lead to a solution.
    failed_positions: set[int] = set()

    def backtrack(start: int) -> bool:

        if start == len(text):
            result.append(current.copy())
            return True

        if start in failed_positions:
            return False

        found = False

        for end in range(start + 1, len(text) + 1):

            word = text[start:end]

            if word in word_set:

                current.append(word)

                if backtrack(end):
                    found = True

                current.pop()

        if not found:
            failed_positions.add(start)

        return found

    backtrack(0)

    return result


def program_18() -> None:
    print("\nPROGRAM 18 — WORD BREAK")

    text = input("Enter the string: ")

    dictionary = input(
        "Enter dictionary words separated by spaces: "
    ).split()

    try:
        combinations = word_break_all(text, dictionary)

        if not combinations:
            print("\nWord Break is not possible.")
            return

        print("\nAll valid segmentations:")

        for index, combination in enumerate(combinations, start=1):
            print(f"{index}. {' '.join(combination)}")

        print("Total segmentations:", len(combinations))

    except ValueError as error:
        print("Error:", error)


# ============================================================
# PROGRAM 19 — UNIQUE PERMUTATIONS WITH DUPLICATES
# ============================================================

def unique_permutations(numbers: list[int]) -> list[list[int]]:
    """
    Generate unique permutations even when elements repeat.
    """

    numbers = sorted(numbers)

    result: list[list[int]] = []

    used = [False] * len(numbers)

    def backtrack(current: list[int]) -> None:

        if len(current) == len(numbers):
            result.append(current.copy())
            return

        for i in range(len(numbers)):

            if used[i]:
                continue

            # Skip duplicate choices at the same recursion level.
            if (
                i > 0
                and numbers[i] == numbers[i - 1]
                and not used[i - 1]
            ):
                continue

            used[i] = True
            current.append(numbers[i])

            backtrack(current)

            # Backtracking.
            current.pop()
            used[i] = False

    backtrack([])

    return result


def program_19() -> None:
    print("\nPROGRAM 19 — UNIQUE PERMUTATIONS")

    numbers = list(
        map(int, input("Enter array elements: ").split())
    )

    permutations = unique_permutations(numbers)

    print("\nUnique permutations:")

    for index, permutation in enumerate(permutations, start=1):
        print(f"{index}. {permutation}")

    print("Total unique permutations:", len(permutations))


# ============================================================
# PROGRAM 20 — ALL PATHS THROUGH A MATRIX WITH OBSTACLES
# ============================================================

def find_matrix_paths(
    matrix: list[list[int]]
) -> list[str]:
    """
    Find all paths from top-left to bottom-right.

    0 = open cell
    1 = obstacle

    Allowed movements: Right (R) and Down (D).
    """

    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    if any(len(row) != cols for row in matrix):
        return []

    # Starting or destination cell is blocked.
    if matrix[0][0] == 1 or matrix[rows - 1][cols - 1] == 1:
        return []

    if any(value not in (0, 1) for row in matrix for value in row):
        raise ValueError("Matrix must contain only 0 and 1.")

    result: list[str] = []

    def backtrack(row: int, col: int, path: str) -> None:

        # Destination reached.
        if row == rows - 1 and col == cols - 1:
            result.append(path)
            return

        # Move Right.
        if col + 1 < cols and matrix[row][col + 1] == 0:
            backtrack(row, col + 1, path + "R")

        # Move Down.
        if row + 1 < rows and matrix[row + 1][col] == 0:
            backtrack(row + 1, col, path + "D")

    backtrack(0, 0, "")

    return result


def program_20() -> None:
    print("\nPROGRAM 20 — MATRIX PATHS WITH OBSTACLES")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be positive.")
        return

    print("Enter matrix values row by row.")
    print("Use 0 for an open cell and 1 for an obstacle.")

    matrix: list[list[int]] = []

    for i in range(rows):

        row = list(
            map(int, input(f"Row {i + 1}: ").split())
        )

        if len(row) != cols or any(value not in (0, 1) for value in row):
            print("Invalid row. Enter exactly", cols, "values of 0 or 1.")
            return

        matrix.append(row)

    paths = find_matrix_paths(matrix)

    print("\nMatrix:")

    for row in matrix:
        print(" ".join(map(str, row)))

    if not paths:
        print("\nNo valid path exists.")
        return

    print("\nAll possible paths:")

    for index, path in enumerate(paths, start=1):
        print(f"{index}. {path}")

    print("Total paths:", len(paths))


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all() -> None:

    print("\n========== PROGRAM 16 ==========")
    program_16()

    print("\n========== PROGRAM 17 ==========")
    program_17()

    print("\n========== PROGRAM 18 ==========")
    program_18()

    print("\n========== PROGRAM 19 ==========")
    program_19()

    print("\n========== PROGRAM 20 ==========")
    program_20()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    while True:

        print("\n" + "=" * 60)
        print("          MONTH 11 — DAY 4: ADVANCED BACKTRACKING")
        print("=" * 60)

        print("16. Knight's Tour")
        print("17. All Hamiltonian Paths in a Graph")
        print("18. Word Break Using Backtracking")
        print("19. Unique Permutations with Duplicates")
        print("20. Matrix Paths with Obstacles")
        print("21. Run All Programs")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "16":
            program_16()

        elif choice == "17":
            program_17()

        elif choice == "18":
            program_18()

        elif choice == "19":
            program_19()

        elif choice == "20":
            program_20()

        elif choice == "21":
            run_all()

        elif choice == "0":
            print("\nDay 4 Advanced Backtracking Completed!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
