
from collections import deque


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
# PROGRAM 96: NUMBER OF PROVINCES
# ---------------------------------------------------------

def number_of_provinces(
    adjacency_matrix: list[list[int]]
) -> int:
    """
    Count connected groups of cities.

    adjacency_matrix[i][j] = 1 means cities i and j
    are directly connected.
    """

    n = len(adjacency_matrix)

    if any(len(row) != n for row in adjacency_matrix):
        raise ValueError("Adjacency matrix must be square.")

    visited = [False] * n
    provinces = 0

    def dfs(city: int) -> None:
        visited[city] = True

        for neighbour in range(n):
            if (
                adjacency_matrix[city][neighbour] == 1
                and not visited[neighbour]
            ):
                dfs(neighbour)

    for city in range(n):
        if not visited[city]:
            provinces += 1
            dfs(city)

    return provinces


def program_96() -> None:
    print("\nPROGRAM 96: NUMBER OF PROVINCES")

    adjacency_matrix = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

    result = number_of_provinces(adjacency_matrix)

    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)

    print("Number of Provinces:", result)


# ---------------------------------------------------------
# PROGRAM 97: NUMBER OF ISLANDS
# ---------------------------------------------------------

def number_of_islands(grid: list[list[str]]) -> int:
    """
    Count islands in a grid.

    '1' represents land.
    '0' represents water.

    Four-directional connections are considered.
    """

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    if any(len(row) != cols for row in grid):
        raise ValueError("Grid must be rectangular.")

    visited = [[False] * cols for _ in range(rows)]
    islands = 0

    def dfs(row: int, col: int) -> None:
        visited[row][col] = True

        for dr, dc in DIRECTIONS:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row][new_col] == "1"
                and not visited[new_row][new_col]
            ):
                dfs(new_row, new_col)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and not visited[row][col]:
                islands += 1
                dfs(row, col)

    return islands


def program_97() -> None:
    print("\nPROGRAM 97: NUMBER OF ISLANDS")

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "1"],
        ["0", "0", "0", "1", "1"]
    ]

    result = number_of_islands(grid)

    print("Grid:")
    for row in grid:
        print(row)

    print("Number of Islands:", result)


# ---------------------------------------------------------
# PROGRAM 98: FLOOD FILL ALGORITHM
# ---------------------------------------------------------

def flood_fill(
    image: list[list[int]],
    start_row: int,
    start_col: int,
    new_colour: int
) -> list[list[int]]:
    """
    Replace the connected region of the starting pixel
    with a new colour.
    """

    if not image:
        return image

    rows = len(image)
    cols = len(image[0])

    if any(len(row) != cols for row in image):
        raise ValueError("Image must be rectangular.")

    if not (0 <= start_row < rows and 0 <= start_col < cols):
        raise ValueError("Starting pixel is outside the image.")

    original_colour = image[start_row][start_col]

    if original_colour == new_colour:
        return image

    queue = deque([(start_row, start_col)])
    image[start_row][start_col] = new_colour

    while queue:
        row, col = queue.popleft()

        for dr, dc in DIRECTIONS:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and image[new_row][new_col] == original_colour
            ):
                image[new_row][new_col] = new_colour
                queue.append((new_row, new_col))

    return image


def program_98() -> None:
    print("\nPROGRAM 98: FLOOD FILL ALGORITHM")

    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    start_row = 1
    start_col = 1
    new_colour = 2

    print("Original Image:")
    for row in image:
        print(row)

    result = flood_fill(
        image,
        start_row,
        start_col,
        new_colour
    )

    print("\nImage After Flood Fill:")
    for row in result:
        print(row)


# ---------------------------------------------------------
# PROGRAM 99: ROTTING ORANGES
# ---------------------------------------------------------

def rotting_oranges(grid: list[list[int]]) -> int:
    """
    Find minimum minutes required to rot all fresh oranges.

    0 = Empty cell
    1 = Fresh orange
    2 = Rotten orange

    All rotten oranges spread simultaneously.
    """

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    if any(len(row) != cols for row in grid):
        raise ValueError("Grid must be rectangular.")

    queue = deque()
    fresh_count = 0

    # Add all initially rotten oranges to the queue.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append((row, col))
            elif grid[row][col] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    minutes = 0

    while queue and fresh_count > 0:
        level_size = len(queue)

        for _ in range(level_size):
            row, col = queue.popleft()

            for dr, dc in DIRECTIONS:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == 1
                ):
                    grid[new_row][new_col] = 2
                    fresh_count -= 1
                    queue.append((new_row, new_col))

        minutes += 1

    if fresh_count > 0:
        return -1

    return minutes


def program_99() -> None:
    print("\nPROGRAM 99: ROTTING ORANGES")

    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    print("Initial Grid:")
    for row in grid:
        print(row)

    result = rotting_oranges(grid)

    print("Minimum Time:", result, "minutes")

    print("\nFinal Grid:")
    for row in grid:
        print(row)


# ---------------------------------------------------------
# PROGRAM 100: SURROUNDED REGIONS
# ---------------------------------------------------------

def surrounded_regions(board: list[list[str]]) -> list[list[str]]:
    """
    Capture all 'O' regions surrounded by 'X'.

    Boundary-connected 'O' cells are safe and remain 'O'.
    Other 'O' cells are changed to 'X'.
    """

    if not board:
        return board

    rows = len(board)
    cols = len(board[0])

    if any(len(row) != cols for row in board):
        raise ValueError("Board must be rectangular.")

    if rows < 3 or cols < 3:
        return board

    def dfs(row: int, col: int) -> None:
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or board[row][col] != "O"
        ):
            return

        # Temporarily mark boundary-connected O as safe.
        board[row][col] = "#"

        for dr, dc in DIRECTIONS:
            dfs(row + dr, col + dc)

    # Explore O cells connected to the top and bottom boundaries.
    for col in range(cols):
        if board[0][col] == "O":
            dfs(0, col)

        if board[rows - 1][col] == "O":
            dfs(rows - 1, col)

    # Explore O cells connected to the left and right boundaries.
    for row in range(rows):
        if board[row][0] == "O":
            dfs(row, 0)

        if board[row][cols - 1] == "O":
            dfs(row, cols - 1)

    # Capture surrounded regions and restore safe regions.
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "O":
                board[row][col] = "X"
            elif board[row][col] == "#":
                board[row][col] = "O"

    return board


def program_100() -> None:
    print("\nPROGRAM 100: SURROUNDED REGIONS")

    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]

    print("Original Board:")
    for row in board:
        print(row)

    result = surrounded_regions(board)

    print("\nBoard After Capturing Regions:")
    for row in result:
        print(row)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    programs = {
        96: program_96,
        97: program_97,
        98: program_98,
        99: program_99,
        100: program_100
    }

    while True:
        print("\n" + "=" * 55)
        print("MONTH 11 - DAY 20: GRAPH TRAVERSAL APPLICATIONS")
        print("=" * 55)

        print("96. Number of Provinces")
        print("97. Number of Islands")
        print("98. Flood Fill Algorithm")
        print("99. Rotting Oranges")
        print("100. Surrounded Regions")
        print("101. Run All Programs")
        print("0. Exit")

        print("=" * 55)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 0:
                print("Exiting Day 20 programs. Keep practising!")
                break

            elif choice == 101:
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
