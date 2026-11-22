
from collections import deque
from typing import Optional


# ---------------------------------------------------------
# COMMON FOUR-DIRECTION MOVEMENTS
# ---------------------------------------------------------

DIRECTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]


# ---------------------------------------------------------
# PROGRAM 106: SHORTEST PATH IN AN UNWEIGHTED GRAPH
# ---------------------------------------------------------

def shortest_path_unweighted(
    graph: dict[int, list[int]],
    source: int
) -> dict[int, int]:
    """
    Find shortest distances from source to every vertex
    using BFS.

    Unreachable vertices have distance -1.
    """

    if source not in graph:
        raise ValueError("Source vertex does not exist.")

    distances = {vertex: -1 for vertex in graph}
    distances[source] = 0

    queue = deque([source])

    while queue:
        vertex = queue.popleft()

        for neighbour in graph[vertex]:
            if neighbour not in distances:
                raise ValueError("Graph contains an undefined vertex.")

            if distances[neighbour] == -1:
                distances[neighbour] = distances[vertex] + 1
                queue.append(neighbour)

    return distances


def program_106() -> None:
    print("\nPROGRAM 106: SHORTEST PATH IN AN UNWEIGHTED GRAPH")

    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4],
        6: []
    }

    source = 0

    result = shortest_path_unweighted(graph, source)

    print("Graph:", graph)
    print("Source Vertex:", source)
    print("Shortest Distances:")

    for vertex, distance in result.items():
        print(f"Vertex {vertex}: {distance}")


# ---------------------------------------------------------
# PROGRAM 107: SHORTEST PATH IN A BINARY MAZE
# ---------------------------------------------------------

def shortest_path_binary_maze(
    grid: list[list[int]],
    source: tuple[int, int],
    destination: tuple[int, int]
) -> int:
    """
    Find the shortest path in a binary grid.

    0 = Open cell
    1 = Blocked cell

    Returns the number of moves.
    Returns -1 if destination is unreachable.
    """

    if not grid:
        return -1

    rows = len(grid)
    cols = len(grid[0])

    if any(len(row) != cols for row in grid):
        raise ValueError("Grid must be rectangular.")

    if any(cell not in (0, 1) for row in grid for cell in row):
        raise ValueError("Grid must contain only 0 and 1.")

    sr, sc = source
    dr, dc = destination

    if not (0 <= sr < rows and 0 <= sc < cols):
        raise ValueError("Source is outside the grid.")

    if not (0 <= dr < rows and 0 <= dc < cols):
        raise ValueError("Destination is outside the grid.")

    if grid[sr][sc] == 1 or grid[dr][dc] == 1:
        return -1

    distances = [[-1] * cols for _ in range(rows)]

    queue = deque([(sr, sc)])
    distances[sr][sc] = 0

    while queue:
        row, col = queue.popleft()

        if (row, col) == destination:
            return distances[row][col]

        for row_change, col_change in DIRECTIONS:
            new_row = row + row_change
            new_col = col + col_change

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row][new_col] == 0
                and distances[new_row][new_col] == -1
            ):
                distances[new_row][new_col] = (
                    distances[row][col] + 1
                )
                queue.append((new_row, new_col))

    return -1


def program_107() -> None:
    print("\nPROGRAM 107: SHORTEST PATH IN A BINARY MAZE")

    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    source = (0, 0)
    destination = (3, 3)

    print("Maze:")
    for row in grid:
        print(row)

    print("Source:", source)
    print("Destination:", destination)

    result = shortest_path_binary_maze(
        grid,
        source,
        destination
    )

    print("Shortest Distance:", result)


# ---------------------------------------------------------
# PROGRAM 108: WORD LADDER
# ---------------------------------------------------------

def word_ladder(
    begin_word: str,
    end_word: str,
    word_list: list[str]
) -> int:
    """
    Find the minimum number of single-character
    transformations needed to reach end_word.

    Each intermediate word must exist in word_list.

    Returns the number of transformations.
    Returns -1 if no transformation is possible.
    """

    if len(begin_word) != len(end_word):
        return -1

    if begin_word == end_word:
        return 0

    word_set = {
        word for word in word_list
        if len(word) == len(begin_word)
    }

    if end_word not in word_set:
        return -1

    queue = deque([(begin_word, 0)])
    visited = {begin_word}

    while queue:
        current_word, steps = queue.popleft()

        for index in range(len(current_word)):
            for character_code in range(ord("a"), ord("z") + 1):
                character = chr(character_code)

                if character == current_word[index]:
                    continue

                new_word = (
                    current_word[:index]
                    + character
                    + current_word[index + 1:]
                )

                if new_word == end_word:
                    return steps + 1

                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))

    return -1


def program_108() -> None:
    print("\nPROGRAM 108: WORD LADDER")

    begin_word = "hit"
    end_word = "cog"

    word_list = [
        "hot",
        "dot",
        "dog",
        "lot",
        "log",
        "cog"
    ]

    result = word_ladder(
        begin_word,
        end_word,
        word_list
    )

    print("Starting Word:", begin_word)
    print("Target Word:", end_word)
    print("Dictionary:", word_list)

    print("Minimum Transformations:", result)


# ---------------------------------------------------------
# PROGRAM 109: MINIMUM MULTIPLICATIONS TO REACH END
# ---------------------------------------------------------

def minimum_multiplications(
    numbers: list[int],
    start: int,
    end: int,
    modulus: int = 100000
) -> int:
    """
    Find minimum multiplications needed to reach end.

    Every operation is:
        current = (current * number) % modulus

    Returns -1 if the target cannot be reached.
    """

    if modulus <= 0:
        raise ValueError("Modulus must be positive.")

    if not (0 <= start < modulus):
        raise ValueError("Starting value must be within the modulus.")

    if not (0 <= end < modulus):
        raise ValueError("Target value must be within the modulus.")

    if any(number < 0 for number in numbers):
        raise ValueError("Multipliers must be non-negative.")

    if start == end:
        return 0

    distances = [-1] * modulus
    distances[start] = 0

    queue = deque([start])

    while queue:
        current = queue.popleft()

        for number in numbers:
            next_value = (current * number) % modulus

            if distances[next_value] == -1:
                distances[next_value] = distances[current] + 1

                if next_value == end:
                    return distances[next_value]

                queue.append(next_value)

    return -1


def program_109() -> None:
    print("\nPROGRAM 109: MINIMUM MULTIPLICATIONS TO REACH END")

    numbers = [2, 5, 7]
    start = 3
    end = 30
    modulus = 100000

    result = minimum_multiplications(
        numbers,
        start,
        end,
        modulus
    )

    print("Multipliers:", numbers)
    print("Starting Value:", start)
    print("Target Value:", end)
    print("Modulus:", modulus)

    print("Minimum Multiplications:", result)


# ---------------------------------------------------------
# PROGRAM 110: SHORTEST PATH WITH OBSTACLE ELIMINATION
# ---------------------------------------------------------

def shortest_path_with_obstacles(
    grid: list[list[int]],
    k: int
) -> int:
    """
    Find the shortest path from top-left to bottom-right.

    0 = Empty cell
    1 = Obstacle

    At most k obstacles can be eliminated.

    Returns minimum number of moves, or -1 if impossible.
    """

    if not grid:
        return -1

    if k < 0:
        raise ValueError("K cannot be negative.")

    rows = len(grid)
    cols = len(grid[0])

    if any(len(row) != cols for row in grid):
        raise ValueError("Grid must be rectangular.")

    if any(cell not in (0, 1) for row in grid for cell in row):
        raise ValueError("Grid must contain only 0 and 1.")

    # Account for an obstacle at the starting cell, if present.
    remaining = k - grid[0][0]

    if remaining < 0:
        return -1

    if rows == 1 and cols == 1:
        return 0

    # State: row, column, remaining eliminations, distance.
    queue = deque([(0, 0, remaining, 0)])

    # best[row][col] stores the greatest remaining
    # elimination budget seen at this cell.
    best = [[-1] * cols for _ in range(rows)]
    best[0][0] = remaining

    while queue:
        row, col, left, distance = queue.popleft()

        for dr, dc in DIRECTIONS:
            new_row = row + dr
            new_col = col + dc

            if not (
                0 <= new_row < rows
                and 0 <= new_col < cols
            ):
                continue

            new_left = left - grid[new_row][new_col]

            if new_left < 0:
                continue

            if (new_row, new_col) == (rows - 1, cols - 1):
                return distance + 1

            # Ignore a state if we have already reached
            # this cell with an equal or greater budget.
            if new_left <= best[new_row][new_col]:
                continue

            best[new_row][new_col] = new_left

            queue.append(
                (new_row, new_col, new_left, distance + 1)
            )

    return -1


def program_110() -> None:
    print("\nPROGRAM 110: SHORTEST PATH WITH OBSTACLE ELIMINATION")

    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0]
    ]

    k = 1

    print("Grid:")
    for row in grid:
        print(row)

    print("Maximum Obstacles Allowed:", k)

    result = shortest_path_with_obstacles(grid, k)

    print("Shortest Path Length:", result)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    programs = {
        106: program_106,
        107: program_107,
        108: program_108,
        109: program_109,
        110: program_110
    }

    while True:
        print("\n" + "=" * 60)
        print("MONTH 11 - DAY 22: SHORTEST PATH ALGORITHMS")
        print("=" * 60)

        print("106. Shortest Path in an Unweighted Graph")
        print("107. Shortest Path in a Binary Maze")
        print("108. Word Ladder")
        print("109. Minimum Multiplications to Reach End")
        print("110. Shortest Path with Obstacle Elimination")
        print("111. Run All Programs")
        print("0. Exit")

        print("=" * 60)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 0:
                print("Exiting Day 22 programs. Keep practising!")
                break

            elif choice == 111:
                for number in programs:
                    programs[number]()

            elif choice in programs:
                programs[choice]()

            else:
                print("Invalid choice. Enter a valid menu option.")

        except ValueError as error:
            print("Invalid input:", error)


if __name__ == "__main__":
    main()
