
from collections import deque
from typing import Optional

# ---------------------------------------------------------
# COMMON GRAPH TRAVERSAL FUNCTIONS
# ---------------------------------------------------------

def bfs_iterative(
    graph: dict[int, list[int]],
    source: int
) -> list[int]:
    """BFS using an explicit queue."""

    if source not in graph:
        raise ValueError("Source vertex does not exist.")

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

def bfs_recursive(
    graph: dict[int, list[int]],
    source: int
) -> list[int]:
    """BFS using recursion to process a queue."""

    if source not in graph:
        raise ValueError("Source vertex does not exist.")

    visited = {source}
    queue = deque([source])
    traversal = []

    def process_queue() -> None:
        if not queue:
            return

        vertex = queue.popleft()
        traversal.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

        process_queue()

    process_queue()
    return traversal

def dfs_recursive(
    graph: dict[int, list[int]],
    source: int
) -> list[int]:
    """DFS using recursive function calls."""

    if source not in graph:
        raise ValueError("Source vertex does not exist.")

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

def dfs_iterative(
    graph: dict[int, list[int]],
    source: int
) -> list[int]:
    """DFS using an explicit stack."""

    if source not in graph:
        raise ValueError("Source vertex does not exist.")

    visited = {source}
    stack = [source]
    traversal = []

    while stack:
        vertex = stack.pop()
        traversal.append(vertex)

        for neighbour in reversed(graph[vertex]):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return traversal

# ---------------------------------------------------------
# PROGRAM 101: CLONE GRAPH
# ---------------------------------------------------------

class GraphNode:
    """Represents a node in an undirected graph."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.neighbours: list[GraphNode] = []

def clone_graph(
    node: Optional[GraphNode]
) -> Optional[GraphNode]:
    """
    Create a deep copy of a connected undirected graph.

    A dictionary maps each original node to its cloned node.
    """

    if node is None:
        return None

    clones: dict[GraphNode, GraphNode] = {}

    def dfs(original: GraphNode) -> GraphNode:
        if original in clones:
            return clones[original]

        # Create a new copy of the original node.
        copied = GraphNode(original.value)
        clones[original] = copied

        # Clone all neighbouring nodes.
        for neighbour in original.neighbours:
            copied.neighbours.append(dfs(neighbour))

        return copied

    return dfs(node)

def display_graph(node: Optional[GraphNode]) -> None:
    """Display a graph using BFS."""

    if node is None:
        print("Empty graph.")
        return

    visited = {node}
    queue = deque([node])

    while queue:
        current = queue.popleft()

        neighbour_values = [
            neighbour.value
            for neighbour in current.neighbours
        ]

        print(f"{current.value} -> {neighbour_values}")

        for neighbour in current.neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def program_101() -> None:
    print("\nPROGRAM 101: CLONE GRAPH")

    # Construct an undirected graph.
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)

    node1.neighbours = [node2, node4]
    node2.neighbours = [node1, node3]
    node3.neighbours = [node2, node4]
    node4.neighbours = [node1, node3]

    print("\nOriginal Graph:")
    display_graph(node1)

    cloned = clone_graph(node1)

    print("\nCloned Graph:")
    display_graph(cloned)

    print("\nDeep Copy Verification:")
    print("Original and clone are different objects:",
          node1 is not cloned)

    if cloned is not None:
        print(
            "Original neighbour and cloned neighbour are different:",
            node1.neighbours[0] is not cloned.neighbours[0]
        )

# ---------------------------------------------------------
# PROGRAM 102: DETECT CYCLE IN UNDIRECTED GRAPH
# ---------------------------------------------------------

def has_cycle_undirected(
    graph: dict[int, list[int]]
) -> bool:
    """
    Detect a cycle in an undirected graph using BFS.

    A visited neighbour that is not the parent indicates a cycle.
    Handles disconnected graphs.
    """

    visited = set()

    for start in graph:
        if start in visited:
            continue

        queue = deque([(start, -1)])
        visited.add(start)

        while queue:
            vertex, parent = queue.popleft()

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, vertex))

                elif neighbour != parent:
                    return True

    return False

def program_102() -> None:
    print("\nPROGRAM 102: DETECT CYCLE IN UNDIRECTED GRAPH")

    cyclic_graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        3: [4],
        4: [3]
    }

    acyclic_graph = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3]
    }

    print("Cyclic Graph:", cyclic_graph)
    print("Contains Cycle:", has_cycle_undirected(cyclic_graph))

    print("\nAcyclic Graph:", acyclic_graph)
    print("Contains Cycle:", has_cycle_undirected(acyclic_graph))

# ---------------------------------------------------------
# PROGRAM 103: DETECT CYCLE IN DIRECTED GRAPH
# ---------------------------------------------------------

def has_cycle_directed(
    graph: dict[int, list[int]]
) -> bool:
    """
    Detect a cycle in a directed graph using DFS.

    0 = Unvisited
    1 = Visiting (currently in recursion path)
    2 = Visited (fully processed)
    """

    state = {vertex: 0 for vertex in graph}

    def dfs(vertex: int) -> bool:
        state[vertex] = 1

        for neighbour in graph[vertex]:
            if neighbour not in state:
                raise ValueError("Graph contains an undefined vertex.")

            if state[neighbour] == 1:
                return True

            if state[neighbour] == 0:
                if dfs(neighbour):
                    return True

        state[vertex] = 2
        return False

    for vertex in graph:
        if state[vertex] == 0:
            if dfs(vertex):
                return True

    return False

def program_103() -> None:
    print("\nPROGRAM 103: DETECT CYCLE IN DIRECTED GRAPH")

    cyclic_graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: []
    }

    acyclic_graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }

    print("Cyclic Directed Graph:", cyclic_graph)
    print("Contains Cycle:", has_cycle_directed(cyclic_graph))

    print("\nAcyclic Directed Graph:", acyclic_graph)
    print("Contains Cycle:", has_cycle_directed(acyclic_graph))

# ---------------------------------------------------------
# PROGRAM 104: FIND EVENTUAL SAFE STATES
# ---------------------------------------------------------

def eventual_safe_states(
    graph: list[list[int]]
) -> list[int]:
    """
    Find vertices from which every possible path
    eventually reaches a terminal node.

    Uses reverse graph construction and topological BFS.
    """

    n = len(graph)

    reverse_graph: list[list[int]] = [[] for _ in range(n)]
    outdegree = [0] * n

    # Build the reverse graph.
    for vertex in range(n):
        for neighbour in graph[vertex]:
            if not 0 <= neighbour < n:
                raise ValueError("Invalid vertex in graph.")

            reverse_graph[neighbour].append(vertex)
            outdegree[vertex] += 1

    # Terminal vertices have outdegree zero.
    queue = deque()

    for vertex in range(n):
        if outdegree[vertex] == 0:
            queue.append(vertex)

    safe = []

    # Process terminal vertices and their predecessors.
    while queue:
        vertex = queue.popleft()
        safe.append(vertex)

        for predecessor in reverse_graph[vertex]:
            outdegree[predecessor] -= 1

            if outdegree[predecessor] == 0:
                queue.append(predecessor)

    return sorted(safe)

def program_104() -> None:
    print("\nPROGRAM 104: FIND EVENTUAL SAFE STATES")

    graph = [
        [1, 2],
        [2, 3],
        [5],
        [0],
        [5],
        [],
        []
    ]

    result = eventual_safe_states(graph)

    print("Directed Graph:", graph)
    print("Eventual Safe States:", result)

# ---------------------------------------------------------
# PROGRAM 105: CHECK WHETHER A GRAPH IS BIPARTITE
# ---------------------------------------------------------

def is_bipartite(
    graph: dict[int, list[int]]
) -> bool:
    """
    Check whether an undirected graph is bipartite.

    Assigns two colours to adjacent vertices using BFS.
    Handles disconnected graphs.
    """

    colour = {vertex: -1 for vertex in graph}

    for start in graph:
        if colour[start] != -1:
            continue

        queue = deque([start])
        colour[start] = 0

        while queue:
            vertex = queue.popleft()

            for neighbour in graph[vertex]:
                if neighbour not in colour:
                    raise ValueError("Graph contains an undefined vertex.")

                if colour[neighbour] == -1:
                    colour[neighbour] = 1 - colour[vertex]
                    queue.append(neighbour)

                elif colour[neighbour] == colour[vertex]:
                    return False

    return True

def program_105() -> None:
    print("\nPROGRAM 105: CHECK WHETHER A GRAPH IS BIPARTITE")

    bipartite_graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }

    non_bipartite_graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }

    print("Bipartite Graph:", bipartite_graph)
    print("Is Bipartite:", is_bipartite(bipartite_graph))

    print("\nNon-Bipartite Graph:", non_bipartite_graph)
    print("Is Bipartite:", is_bipartite(non_bipartite_graph))

# ---------------------------------------------------------
# WEEKLY CHALLENGE: BFS AND DFS IN FOUR WAYS
# ---------------------------------------------------------

def weekly_challenge() -> None:
    print("\nWEEKLY CHALLENGE: BFS AND DFS")

    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2]
    }

    source = 0

    print("\nGraph:", graph)
    print("Starting Vertex:", source)

    print("\n1. BFS - Iterative:")
    print(bfs_iterative(graph, source))

    print("\n2. BFS - Recursive:")
    print(bfs_recursive(graph, source))

    print("\n3. DFS - Recursive:")
    print(dfs_recursive(graph, source))

    print("\n4. DFS - Iterative:")
    print(dfs_iterative(graph, source))

    print("\n5. Number of Islands - Revision:")

    grid = [
        ["1", "1", "0", "0"],
        ["1", "0", "0", "1"],
        ["0", "0", "1", "1"],
        ["0", "0", "0", "0"]
    ]

    # Each connected group of 1s is one island.
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    islands = 0

    def island_dfs(row: int, col: int) -> None:
        visited[row][col] = True

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = row + dr
            nc = col + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == "1"
                and not visited[nr][nc]
            ):
                island_dfs(nr, nc)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and not visited[row][col]:
                islands += 1
                island_dfs(row, col)

    print("Number of Islands:", islands)

    print("\n6. Cycle Detection - Revision:")

    cycle_test_graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        3: [4],
        4: [3]
    }

    print(
        "Undirected Graph Contains Cycle:",
        has_cycle_undirected(cycle_test_graph)
    )

# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    programs = {
        101: program_101,
        102: program_102,
        103: program_103,
        104: program_104,
        105: program_105
    }

    while True:
        print("\n" + "=" * 58)
        print("MONTH 11 - DAY 21: WEEK 3 GRAPH REVISION")
        print("=" * 58)

        print("101. Clone Graph")
        print("102. Detect Cycle in Undirected Graph")
        print("103. Detect Cycle in Directed Graph")
        print("104. Find Eventual Safe States")
        print("105. Is Graph Bipartite?")
        print("106. Weekly Challenge - BFS and DFS")
        print("107. Run All Programs")
        print("0. Exit")

        print("=" * 58)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 0:
                print("Exiting Day 21 programs. Keep practising!")
                break

            elif choice == 106:
                weekly_challenge()

            elif choice == 107:
                for number in programs:
                    programs[number]()

                weekly_challenge()

            elif choice in programs:
                programs[choice]()

            else:
                print("Invalid choice. Enter a valid menu option.")

        except ValueError as error:
            print("Invalid input:", error)

if __name__ == "__main__":
    main()