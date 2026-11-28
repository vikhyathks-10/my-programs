
import heapq
from typing import Optional
# ---------------------------------------------------------
# PROGRAM 136: DISJOINT SET UNION - UNION BY RANK
# ---------------------------------------------------------

class DisjointSet:
    def __init__(self, vertices: int) -> None:
        if vertices <= 0:
            raise ValueError("Number of vertices must be positive.")

        self.parent = list(range(vertices))
        self.rank = [0] * vertices
        self.components = vertices

    def find(self, node: int) -> int:
        if not 0 <= node < len(self.parent):
            raise ValueError("Invalid node.")

        # Path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, first: int, second: int) -> bool:
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return False

        # Union by rank
        if self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second

        elif self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first

        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1

        self.components -= 1
        return True

    def connected(self, first: int, second: int) -> bool:
        return self.find(first) == self.find(second)


def run_136() -> None:
    print("\nPROGRAM 136: DISJOINT SET UNION")

    dsu = DisjointSet(5)

    print("Initially, components:", dsu.components)

    operations = [
        (0, 1),
        (1, 2),
        (3, 4)
    ]

    for first, second in operations:
        dsu.union(first, second)
        print(
            f"After union({first}, {second}): "
            f"{dsu.components} components"
        )

    print("Are 0 and 2 connected?", dsu.connected(0, 2))
    print("Are 0 and 4 connected?", dsu.connected(0, 4))
    print("Representative of 2:", dsu.find(2))


# ---------------------------------------------------------
# PROGRAM 137: UNION BY SIZE
# ---------------------------------------------------------

class DisjointSetBySize:
    def __init__(self, vertices: int) -> None:
        if vertices <= 0:
            raise ValueError("Number of vertices must be positive.")

        self.parent = list(range(vertices))
        self.size = [1] * vertices
        self.components = vertices

    def find(self, node: int) -> int:
        if not 0 <= node < len(self.parent):
            raise ValueError("Invalid node.")

        # Path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, first: int, second: int) -> bool:
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return False

        # Attach smaller component under larger component.
        if self.size[root_first] < self.size[root_second]:
            root_first, root_second = root_second, root_first

        self.parent[root_second] = root_first
        self.size[root_first] += self.size[root_second]

        self.components -= 1
        return True

    def component_size(self, node: int) -> int:
        return self.size[self.find(node)]


def run_137() -> None:
    print("\nPROGRAM 137: UNION BY SIZE")

    dsu = DisjointSetBySize(7)

    edges = [
        (0, 1),
        (1, 2),
        (3, 4),
        (5, 6),
        (2, 3)
    ]

    for first, second in edges:
        dsu.union(first, second)

    print("Number of connected components:", dsu.components)

    for vertex in range(7):
        print(
            f"Vertex {vertex}: "
            f"Representative = {dsu.find(vertex)}, "
            f"Component size = {dsu.component_size(vertex)}"
        )

    print("Are 0 and 4 connected?", dsu.find(0) == dsu.find(4))
    print("Are 0 and 6 connected?", dsu.find(0) == dsu.find(6))


# ---------------------------------------------------------
# PROGRAM 138: KRUSKAL'S MINIMUM SPANNING TREE
# ---------------------------------------------------------

def kruskal_mst(
    vertices: int,
    edges: list[tuple[int, int, int]]
) -> tuple[list[tuple[int, int, int]], int]:
    """
    Each edge is (u, v, weight).

    Returns:
        Selected MST edges and total weight.

    Raises ValueError if the graph is disconnected.
    """

    if vertices <= 0:
        raise ValueError("Number of vertices must be positive.")

    for u, v, weight in edges:
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError("Edge contains an invalid vertex.")

    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    dsu = DisjointSet(vertices)
    mst_edges: list[tuple[int, int, int]] = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight

            if len(mst_edges) == vertices - 1:
                break

    if len(mst_edges) != vertices - 1:
        raise ValueError("A spanning tree does not exist; graph is disconnected.")

    return mst_edges, total_weight


def run_138() -> None:
    print("\nPROGRAM 138: KRUSKAL'S MINIMUM SPANNING TREE")

    vertices = 5

    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]

    mst_edges, total_weight = kruskal_mst(vertices, edges)

    print("Selected MST edges:")

    for u, v, weight in mst_edges:
        print(f"{u} -- {v} : {weight}")

    print("Total MST weight:", total_weight)


# ---------------------------------------------------------
# PROGRAM 139: PRIM'S MINIMUM SPANNING TREE
# ---------------------------------------------------------

def prim_mst(
    vertices: int,
    edges: list[tuple[int, int, int]],
    start: int = 0
) -> tuple[list[tuple[int, int, int]], int]:
    """
    Find an MST using Prim's algorithm.

    Each edge is (u, v, weight).
    The graph is undirected.

    Raises ValueError if the graph is disconnected.
    """

    if vertices <= 0 or not 0 <= start < vertices:
        raise ValueError("Invalid number of vertices or start vertex.")

    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(vertices)
    ]

    for u, v, weight in edges:
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError("Edge contains an invalid vertex.")

        adjacency[u].append((v, weight))
        adjacency[v].append((u, weight))

    visited = [False] * vertices

    # Heap entries: (weight, current_vertex, parent_vertex)
    min_heap: list[tuple[int, int, int]] = [
        (0, start, -1)
    ]

    mst_edges: list[tuple[int, int, int]] = []
    total_weight = 0

    while min_heap and len(mst_edges) < vertices - 1:
        weight, node, parent = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True

        if parent != -1:
            mst_edges.append((parent, node, weight))
            total_weight += weight

        for neighbour, edge_weight in adjacency[node]:
            if not visited[neighbour]:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbour, node)
                )

    if len(mst_edges) != vertices - 1:
        raise ValueError("A spanning tree does not exist; graph is disconnected.")

    return mst_edges, total_weight


def run_139() -> None:
    print("\nPROGRAM 139: PRIM'S MINIMUM SPANNING TREE")

    vertices = 5

    edges = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]

    mst_edges, total_weight = prim_mst(
        vertices,
        edges,
        start=0
    )

    print("Selected MST edges:")

    for u, v, weight in mst_edges:
        print(f"{u} -- {v} : {weight}")

    print("Total MST weight:", total_weight)


# ---------------------------------------------------------
# PROGRAM 140: REDUNDANT CONNECTION
# ---------------------------------------------------------

def redundant_connection(
    edges: list[tuple[int, int]]
) -> Optional[tuple[int, int]]:
    """
    Find the edge that creates a cycle.

    Vertices are numbered from 1 to N.
    Returns the last edge that connects vertices
    already belonging to the same component.
    """

    if not edges:
        return None

    vertices = max(
        max(u, v) for u, v in edges
    )

    if vertices <= 0:
        raise ValueError("Invalid vertex numbering.")

    dsu = DisjointSet(vertices + 1)

    for u, v in edges:
        if not (1 <= u <= vertices and 1 <= v <= vertices):
            raise ValueError("Vertices must be numbered from 1 to N.")

        if not dsu.union(u, v):
            return (u, v)

    return None


def run_140() -> None:
    print("\nPROGRAM 140: REDUNDANT CONNECTION")

    edges = [
        (1, 2),
        (1, 3),
        (2, 3)
    ]

    answer = redundant_connection(edges)

    if answer is None:
        print("No redundant connection found.")
    else:
        print("Redundant edge:", answer)
        print("Remove this edge to eliminate the cycle.")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    programs = {
        136: run_136,
        137: run_137,
        138: run_138,
        139: run_139,
        140: run_140
    }

    while True:
        print("\n" + "=" * 55)
        print("MONTH 11 - DAY 28: DSU AND MINIMUM SPANNING TREE")
        print("=" * 55)

        print("136. Disjoint Set Union")
        print("137. Union by Size")
        print("138. Kruskal's Minimum Spanning Tree")
        print("139. Prim's Minimum Spanning Tree")
        print("140. Redundant Connection")
        print("141. Run All Programs")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Exiting Day 28 programs. Goodbye!")
            break

        if choice == 141:
            for program in programs.values():
                program()
        elif choice in programs:
            programs[choice]()
        else:
            print("Invalid choice. Please select 136-141 or 0.")


if __name__ == "__main__":
    main()
