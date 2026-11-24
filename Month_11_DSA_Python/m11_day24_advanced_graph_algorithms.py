
from collections import deque


# ============================================================
# PROGRAM 116: COUNT ENCLAVES
# Count land cells that cannot reach any grid boundary.
# ============================================================

def count_enclaves(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]
    queue: deque[tuple[int, int]] = deque()

    # Add all boundary land cells to the queue.
    for row in range(rows):
        for col in range(cols):
            if (
                (row == 0 or row == rows - 1 or
                 col == 0 or col == cols - 1)
                and grid[row][col] == 1
                and not visited[row][col]
            ):
                visited[row][col] = True
                queue.append((row, col))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Remove all land connected to the boundary.
    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and grid[new_row][new_col] == 1
                and not visited[new_row][new_col]
            ):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))

    # Count remaining unvisited land cells.
    enclaves = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and not visited[row][col]:
                enclaves += 1

    return enclaves


def demo_116() -> None:
    grid = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    print("Input Grid:")
    for row in grid:
        print(row)

    print("\nNumber of Enclaves:", count_enclaves(grid))


# ============================================================
# PROGRAM 117: NUMBER OF DISTINCT ISLANDS
# Count unique island shapes, considering translations equal.
# ============================================================

def count_distinct_islands(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]
    distinct_shapes: set[tuple[tuple[int, int], ...]] = set()

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == 1 and not visited[row][col]:

                queue: deque[tuple[int, int]] = deque()
                queue.append((row, col))
                visited[row][col] = True

                shape: list[tuple[int, int]] = []

                # Store coordinates relative to the island's origin.
                while queue:
                    current_row, current_col = queue.popleft()

                    relative_position = (
                        current_row - row,
                        current_col - col
                    )
                    shape.append(relative_position)

                    for dr, dc in directions:
                        new_row = current_row + dr
                        new_col = current_col + dc

                        if (
                            0 <= new_row < rows
                            and 0 <= new_col < cols
                            and grid[new_row][new_col] == 1
                            and not visited[new_row][new_col]
                        ):
                            visited[new_row][new_col] = True
                            queue.append((new_row, new_col))

                # Sort coordinates to create a consistent shape.
                distinct_shapes.add(tuple(sorted(shape)))

    return len(distinct_shapes)


def demo_117() -> None:
    grid = [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 0, 1, 0]
    ]

    print("Input Grid:")
    for row in grid:
        print(row)

    print("\nNumber of Distinct Islands:", count_distinct_islands(grid))


# ============================================================
# PROGRAM 118: ARTICULATION POINTS
# Find vertices whose removal increases connected components.
# Uses Tarjan's DFS algorithm.
# ============================================================

def articulation_points(
    vertices: int,
    edges: list[tuple[int, int]]
) -> list[int]:

    graph: list[list[int]] = [[] for _ in range(vertices)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    discovery = [-1] * vertices
    low = [0] * vertices
    parent = [-1] * vertices
    result: set[int] = set()

    timer = 0

    def dfs(node: int) -> None:
        nonlocal timer

        discovery[node] = timer
        low[node] = timer
        timer += 1

        children = 0

        for neighbour in graph[node]:

            if discovery[neighbour] == -1:
                parent[neighbour] = node
                children += 1

                dfs(neighbour)

                low[node] = min(low[node], low[neighbour])

                # Root is an articulation point if it has
                # more than one DFS child.
                if parent[node] == -1 and children > 1:
                    result.add(node)

                # Non-root is an articulation point if
                # the child cannot reach an ancestor of node.
                if (
                    parent[node] != -1
                    and low[neighbour] >= discovery[node]
                ):
                    result.add(node)

            elif neighbour != parent[node]:
                low[node] = min(low[node], discovery[neighbour])

    # Handle disconnected graphs.
    for vertex in range(vertices):
        if discovery[vertex] == -1:
            dfs(vertex)

    return sorted(result)


def demo_118() -> None:
    vertices = 5

    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (1, 3),
        (3, 4)
    ]

    print("Vertices:", vertices)
    print("Edges:", edges)

    print("\nArticulation Points:", articulation_points(vertices, edges))


# ============================================================
# PROGRAM 119: BRIDGES IN A GRAPH
# Find edges whose removal increases connected components.
# Uses Tarjan's DFS algorithm.
# ============================================================

def find_bridges(
    vertices: int,
    edges: list[tuple[int, int]]
) -> list[tuple[int, int]]:

    graph: list[list[int]] = [[] for _ in range(vertices)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    discovery = [-1] * vertices
    low = [0] * vertices
    parent = [-1] * vertices

    bridges: list[tuple[int, int]] = []
    timer = 0

    def dfs(node: int) -> None:
        nonlocal timer

        discovery[node] = timer
        low[node] = timer
        timer += 1

        for neighbour in graph[node]:

            if discovery[neighbour] == -1:
                parent[neighbour] = node

                dfs(neighbour)

                low[node] = min(low[node], low[neighbour])

                # If child cannot reach node or an ancestor,
                # the edge between node and child is a bridge.
                if low[neighbour] > discovery[node]:
                    bridges.append((node, neighbour))

            elif neighbour != parent[node]:
                low[node] = min(low[node], discovery[neighbour])

    # Handle disconnected graphs.
    for vertex in range(vertices):
        if discovery[vertex] == -1:
            dfs(vertex)

    return sorted(bridges)


def demo_119() -> None:
    vertices = 5

    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (1, 3),
        (3, 4)
    ]

    print("Vertices:", vertices)
    print("Edges:", edges)

    print("\nBridges:", find_bridges(vertices, edges))


# ============================================================
# PROGRAM 120: STRONGLY CONNECTED COMPONENTS
# Find SCCs in a directed graph using Kosaraju's algorithm.
# ============================================================

def kosaraju_scc(
    vertices: int,
    edges: list[tuple[int, int]]
) -> list[list[int]]:

    graph: list[list[int]] = [[] for _ in range(vertices)]
    reverse_graph: list[list[int]] = [[] for _ in range(vertices)]

    # Build original graph and reversed graph.
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)

    visited = [False] * vertices
    stack: list[int] = []

    # STEP 1: DFS and store vertices by finishing order.
    def first_dfs(node: int) -> None:
        visited[node] = True

        for neighbour in graph[node]:
            if not visited[neighbour]:
                first_dfs(neighbour)

        stack.append(node)

    for vertex in range(vertices):
        if not visited[vertex]:
            first_dfs(vertex)

    # STEP 2: DFS on reversed graph in decreasing
    # order of finishing times.
    visited = [False] * vertices
    components: list[list[int]] = []

    def second_dfs(node: int, component: list[int]) -> None:
        visited[node] = True
        component.append(node)

        for neighbour in reverse_graph[node]:
            if not visited[neighbour]:
                second_dfs(neighbour, component)

    while stack:
        node = stack.pop()

        if not visited[node]:
            component: list[int] = []
            second_dfs(node, component)
            components.append(sorted(component))

    return components


def demo_120() -> None:
    vertices = 5

    edges = [
        (0, 2),
        (2, 1),
        (1, 0),
        (0, 3),
        (3, 4)
    ]

    print("Vertices:", vertices)
    print("Directed Edges:", edges)

    components = kosaraju_scc(vertices, edges)

    print("\nStrongly Connected Components:")

    for index, component in enumerate(components, start=1):
        print(f"SCC {index}: {component}")


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    programs = {
        116: demo_116,
        117: demo_117,
        118: demo_118,
        119: demo_119,
        120: demo_120
    }

    while True:
        print("\n" + "=" * 60)
        print("MONTH 11 - DAY 24: ADVANCED GRAPH ALGORITHMS")
        print("=" * 60)

        print("116. Count Enclaves")
        print("117. Number of Distinct Islands")
        print("118. Articulation Points")
        print("119. Bridges in a Graph")
        print("120. Strongly Connected Components")
        print("121. Run All Programs")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Day 24 completed. Keep practicing!")
            break

        elif choice == 121:
            for number in range(116, 121):
                print("\n" + "#" * 60)
                print(f"RUNNING PROGRAM {number}")
                print("#" * 60)
                programs[number]()

        elif choice in programs:
            programs[choice]()

        else:
            print("Invalid choice. Please select 116–121 or 0.")


if __name__ == "__main__":
    main()
