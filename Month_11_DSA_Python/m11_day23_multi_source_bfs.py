
from collections import deque
from typing import Optional


# ============================================================
# PROGRAM 111: 01 MATRIX
# Find distance of every cell containing 1 to nearest 0.
# ============================================================

def update_matrix(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    distance = [[-1] * cols for _ in range(rows)]
    queue: deque[tuple[int, int]] = deque()

    # Add all zero cells as BFS starting points.
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                distance[row][col] = 0
                queue.append((row, col))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and distance[new_row][new_col] == -1
            ):
                distance[new_row][new_col] = distance[row][col] + 1
                queue.append((new_row, new_col))

    return distance


def demo_111() -> None:
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]

    print("Input Matrix:")
    for row in matrix:
        print(row)

    print("\nDistance Matrix:")
    for row in update_matrix(matrix):
        print(row)


# ============================================================
# PROGRAM 112: NEAREST EXIT FROM ENTRANCE IN MAZE
# Find shortest path to a boundary exit.
# ============================================================

def nearest_exit(
    maze: list[list[str]],
    entrance: tuple[int, int]
) -> int:

    if not maze or not maze[0]:
        return -1

    rows = len(maze)
    cols = len(maze[0])

    start_row, start_col = entrance

    queue: deque[tuple[int, int, int]] = deque()
    queue.append((start_row, start_col, 0))

    visited = [[False] * cols for _ in range(rows)]
    visited[start_row][start_col] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        row, col, steps = queue.popleft()

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and maze[new_row][new_col] == "."
                and not visited[new_row][new_col]
            ):

                # A boundary cell is an exit, except the entrance.
                if (
                    new_row == 0
                    or new_row == rows - 1
                    or new_col == 0
                    or new_col == cols - 1
                ):
                    return steps + 1

                visited[new_row][new_col] = True
                queue.append((new_row, new_col, steps + 1))

    return -1


def demo_112() -> None:
    maze = [
        ["+", "+", ".", "+"],
        [".", ".", ".", "+"],
        ["+", "+", "+", "."]
    ]

    entrance = (1, 2)

    print("Maze:")
    for row in maze:
        print(" ".join(row))

    print("\nEntrance:", entrance)
    print("Nearest exit distance:", nearest_exit(maze, entrance))


# ============================================================
# PROGRAM 113: AS FAR FROM LAND AS POSSIBLE
# Find maximum distance of water from nearest land.
# ============================================================

def max_distance_from_land(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    queue: deque[tuple[int, int, int]] = deque()
    land_count = 0
    water_count = 0

    # Add every land cell to the queue.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                queue.append((row, col, 0))
                land_count += 1
            else:
                water_count += 1

    # No land or no water means no valid maximum distance.
    if land_count == 0 or water_count == 0:
        return -1

    visited = [[False] * cols for _ in range(rows)]

    for row, col, _ in queue:
        visited[row][col] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    maximum_distance = 0

    while queue:
        row, col, distance = queue.popleft()
        maximum_distance = max(maximum_distance, distance)

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and not visited[new_row][new_col]
            ):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, distance + 1))

    return maximum_distance


def demo_113() -> None:
    grid = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]

    print("Grid:")
    for row in grid:
        print(row)

    print("\nMaximum distance from land:", max_distance_from_land(grid))


# ============================================================
# PROGRAM 114: MINIMUM GENETIC MUTATION
# Find minimum valid single-character mutations.
# ============================================================

def min_mutation(
    start_gene: str,
    end_gene: str,
    bank: list[str]
) -> int:

    if start_gene == end_gene:
        return 0

    bank_set = set(bank)

    if end_gene not in bank_set:
        return -1

    queue: deque[tuple[str, int]] = deque()
    queue.append((start_gene, 0))

    visited = {start_gene}
    genes = ["A", "C", "G", "T"]

    while queue:
        current_gene, mutations = queue.popleft()

        if current_gene == end_gene:
            return mutations

        for index in range(len(current_gene)):
            for gene in genes:

                if gene == current_gene[index]:
                    continue

                new_gene = (
                    current_gene[:index]
                    + gene
                    + current_gene[index + 1:]
                )

                if new_gene in bank_set and new_gene not in visited:
                    visited.add(new_gene)
                    queue.append((new_gene, mutations + 1))

    return -1


def demo_114() -> None:
    start_gene = "AACCGGTT"
    end_gene = "AAACGGTA"

    bank = [
        "AACCGGTA",
        "AACCGCTA",
        "AAACGGTA"
    ]

    print("Start Gene:", start_gene)
    print("End Gene:", end_gene)
    print("Gene Bank:", bank)

    print("\nMinimum mutations:", min_mutation(
        start_gene, end_gene, bank
    ))


# ============================================================
# PROGRAM 115: OPEN THE LOCK
# Find minimum turns to reach the target combination.
# ============================================================

def open_lock(deadends: list[str], target: str) -> int:

    start = "0000"
    dead_set = set(deadends)

    if start in dead_set:
        return -1

    if target == start:
        return 0

    queue: deque[tuple[str, int]] = deque()
    queue.append((start, 0))

    visited = {start}

    while queue:
        current, turns = queue.popleft()

        if current == target:
            return turns

        for index in range(4):
            digit = int(current[index])

            # Rotate wheel forward and backward.
            for change in (-1, 1):
                new_digit = (digit + change) % 10

                next_state = (
                    current[:index]
                    + str(new_digit)
                    + current[index + 1:]
                )

                if (
                    next_state not in dead_set
                    and next_state not in visited
                ):
                    if next_state == target:
                        return turns + 1

                    visited.add(next_state)
                    queue.append((next_state, turns + 1))

    return -1


def demo_115() -> None:
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"

    print("Deadends:", deadends)
    print("Target:", target)

    print("\nMinimum turns:", open_lock(deadends, target))


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:
    while True:
        print("\n" + "=" * 55)
        print("MONTH 11 - DAY 23: MULTI-SOURCE BFS")
        print("=" * 55)

        print("111. 01 Matrix")
        print("112. Nearest Exit from Entrance in Maze")
        print("113. As Far from Land as Possible")
        print("114. Minimum Genetic Mutation")
        print("115. Open the Lock")
        print("116. Run All Programs")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Day 23 completed. Keep practicing!")
            break

        programs = {
            111: demo_111,
            112: demo_112,
            113: demo_113,
            114: demo_114,
            115: demo_115
        }

        if choice == 116:
            for program_number in range(111, 116):
                print("\n" + "#" * 55)
                print(f"RUNNING PROGRAM {program_number}")
                print("#" * 55)
                programs[program_number]()
        elif choice in programs:
            programs[choice]()
        else:
            print("Invalid choice. Please select 111–116 or 0.")


if __name__ == "__main__":
    main()
