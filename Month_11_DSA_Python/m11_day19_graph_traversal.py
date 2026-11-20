
from collections import deque
from typing import Optional


# ---------------------------------------------------------
# COMMON GRAPH REPRESENTATION
# ---------------------------------------------------------

def create_graph(
    vertices: int,
    edges: list[tuple[int, int]]
) -> dict[int, list[int]]:
    """Create an undirected graph using an adjacency list."""

    if vertices < 0:
        raise ValueError("Number of vertices cannot be negative.")

    graph = {vertex: [] for vertex in range(vertices)}

    for u, v in edges:
        if u not in graph or v not in graph:
            raise ValueError("Edge contains an invalid vertex.")

        graph[u].append(v)
        graph[v].append(u)

    return graph


def validate_source(
    graph: dict[int, list[int]],
    source: int
) -> None:
    """Check whether the source vertex exists."""

    if source not in graph:
        raise ValueError("Source vertex does not exist in the graph.")


# ---------------------------------------------------------
# PROGRAM 91: BREADTH-FIRST SEARCH
# ---------------------------------------------------------

def breadth_first_search(
    graph: dict[int, list[int]],
    source: int
) -> list[int]:
    """
    Traverse a graph using BFS.

    BFS explores vertices level by level using a queue.
    """

    validate_source(graph, source)

    visited = {source}
    queue = deque([source])
    traversal = []

    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return traversal


def program_91() -> None:
    print("\nPROGRAM 91: BREADTH-FIRST SEARCH")

    graph = create_graph(
        6,
        [
            (0, 1),
            (0, 2),
            (1, 3),
            (1, 4),
            (2, 5)
        ]
    )

    source = 0
    result = breadth_first_search(graph, source)

    print("Graph:", graph)
    print("Starting vertex:", source)
    print("BFS Traversal:", result)


# ---------------------------------------------------------
# PROGRAM 92: DEPTH-FIRST SEARCH - RECURSIVE
# ---------------------------------------------------------

def dfs_recursive(
    graph: dict[int, list[int]],
    source: int
) -> list[int]:
    """
    Traverse a graph using recursive DFS.

    DFS explores one branch deeply before backtracking.
    """

    validate_source(graph, source)

    visited = set()
    traversal = []

    def dfs(vertex: int) -> None:
        visited.add(vertex)
        traversal.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfs(neighbour)

    dfs(source)

    return traversal


def program_92() -> None:
    print("\nPROGRAM 92: RECURSIVE DEPTH-FIRST SEARCH")

    graph = create_graph(
        6,
        [
            (0, 1),
            (0, 2),
            (1, 3),
            (1, 4),
            (2, 5)
        ]
    )

    source = 0
    result = dfs_recursive(graph, source)

    print("Graph:", graph)
    print("Starting vertex:", source)
    print("Recursive DFS Traversal:", result)


# ---------------------------------------------------------
# PROGRAM 93: DEPTH-FIRST SEARCH - ITERATIVE
# ---------------------------------------------------------

def dfs_iterative(
    graph: dict[int, list[int]],
    source: int
) -> list[int]:
    """
    Traverse a graph using iterative DFS.

    An explicit stack replaces recursive function calls.
    """

    validate_source(graph, source)

    visited = {source}
    stack = [source]
    traversal = []

    while stack:
        vertex = stack.pop()
        traversal.append(vertex)

        # Reverse neighbours to match recursive DFS order.
        for neighbour in reversed(graph[vertex]):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return traversal


def program_93() -> None:
    print("\nPROGRAM 93: ITERATIVE DEPTH-FIRST SEARCH")

    graph = create_graph(
        6,
        [
            (0, 1),
            (0, 2),
            (1, 3),
            (1, 4),
            (2, 5)
        ]
    )

    source = 0
    result = dfs_iterative(graph, source)

    print("Graph:", graph)
    print("Starting vertex:", source)
    print("Iterative DFS Traversal:", result)


# ---------------------------------------------------------
# PROGRAM 94: COUNT CONNECTED COMPONENTS
# ---------------------------------------------------------

def count_connected_components(
    graph: dict[int, list[int]]
) -> int:
    """
    Count the connected components in an undirected graph.

    Each new unvisited vertex starts a new component.
    """

    visited = set()
    components = 0

    for vertex in graph:
        if vertex not in visited:
            components += 1

            stack = [vertex]
            visited.add(vertex)

            while stack:
                current = stack.pop()

                for neighbour in graph[current]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        stack.append(neighbour)

    return components


def program_94() -> None:
    print("\nPROGRAM 94: COUNT CONNECTED COMPONENTS")

    graph = create_graph(
        8,
        [
            (0, 1),
            (1, 2),
            (3, 4),
            (5, 6)
        ]
    )

    result = count_connected_components(graph)

    print("Graph:", graph)
    print("Connected Components:", result)


# ---------------------------------------------------------
# PROGRAM 95: CHECK WHETHER A GRAPH IS CONNECTED
# ---------------------------------------------------------

def is_graph_connected(
    graph: dict[int, list[int]],
    source: Optional[int] = None
) -> bool:
    """
    Check whether every vertex is reachable from source.

    An empty graph is considered disconnected.
    """

    if not graph:
        return False

    if source is None:
        source = next(iter(graph))

    validate_source(graph, source)

    visited = set()
    stack = [source]
    visited.add(source)

    while stack:
        vertex = stack.pop()

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return len(visited) == len(graph)


def program_95() -> None:
    print("\nPROGRAM 95: CHECK WHETHER A GRAPH IS CONNECTED")

    connected_graph = create_graph(
        5,
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4)
        ]
    )

    disconnected_graph = create_graph(
        5,
        [
            (0, 1),
            (1, 2),
            (3, 4)
        ]
    )

    source = 0

    print("\nConnected Graph:", connected_graph)
    print(
        "Is Connected?",
        is_graph_connected(connected_graph, source)
    )

    print("\nDisconnected Graph:", disconnected_graph)
    print(
        "Is Connected?",
        is_graph_connected(disconnected_graph, source)
    )


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    programs = {
        91: program_91,
        92: program_92,
        93: program_93,
        94: program_94,
        95: program_95
    }

    while True:
        print("\n" + "=" * 55)
        print("MONTH 11 - DAY 19: GRAPH TRAVERSAL FUNDAMENTALS")
        print("=" * 55)

        print("91. Breadth-First Search")
        print("92. Depth-First Search - Recursive")
        print("93. Depth-First Search - Iterative")
        print("94. Count Connected Components")
        print("95. Check Whether a Graph Is Connected")
        print("96. Run All Programs")
        print("0. Exit")

        print("=" * 55)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 0:
                print("Exiting Day 19 programs. Keep practising!")
                break

            elif choice == 96:
                for number in programs:
                    programs[number]()

            elif choice in programs:
                programs[choice]()

            else:
                print("Invalid choice. Enter a number from 0 to 96.")

        except ValueError as error:
            print("Invalid input:", error)


if __name__ == "__main__":
    main()
