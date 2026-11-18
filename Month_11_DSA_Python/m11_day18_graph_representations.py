
# ============================================================
# MONTH 11 - DAY 18
# GRAPH FUNDAMENTALS AND REPRESENTATIONS
# Programs 86-90
# ============================================================
from typing import Optional
# ============================================================
# COMMON INPUT FUNCTIONS
# ============================================================

def read_edges(
    edge_count: int,
    weighted: bool = False
) -> list[tuple[int, ...]]:
    """Read graph edges from the user."""

    edges: list[tuple[int, ...]] = []

    for index in range(edge_count):

        if weighted:
            source, destination, weight = map(
                int,
                input(
                    f"Enter edge {index + 1} (source destination weight): "
                ).split()
            )

            edges.append((source, destination, weight))

        else:
            source, destination = map(
                int,
                input(
                    f"Enter edge {index + 1} (source destination): "
                ).split()
            )

            edges.append((source, destination))

    return edges


def validate_vertex(vertex: int, vertices: int) -> None:
    """Check whether a vertex belongs to a fixed-size graph."""

    if vertex < 0 or vertex >= vertices:
        raise ValueError(
            f"Invalid vertex {vertex}. Valid vertices are 0 to {vertices - 1}."
        )


# ============================================================
# PROGRAM 86: GRAPH REPRESENTATION USING ADJACENCY MATRIX
# ============================================================

class AdjacencyMatrixGraph:
    """
    Represent an undirected graph using an adjacency matrix.

    matrix[i][j] = 1 means an edge exists between i and j.
    matrix[i][j] = 0 means no edge exists.
    """

    def __init__(self, vertices: int) -> None:

        if vertices <= 0:
            raise ValueError("Number of vertices must be positive.")

        self.vertices = vertices

        self.matrix: list[list[int]] = [
            [0 for _ in range(vertices)]
            for _ in range(vertices)
        ]

    def add_edge(self, source: int, destination: int) -> None:

        validate_vertex(source, self.vertices)
        validate_vertex(destination, self.vertices)

        self.matrix[source][destination] = 1
        self.matrix[destination][source] = 1

    def remove_edge(self, source: int, destination: int) -> None:

        validate_vertex(source, self.vertices)
        validate_vertex(destination, self.vertices)

        self.matrix[source][destination] = 0
        self.matrix[destination][source] = 0

    def has_edge(self, source: int, destination: int) -> bool:

        validate_vertex(source, self.vertices)
        validate_vertex(destination, self.vertices)

        return self.matrix[source][destination] == 1

    def display(self) -> None:

        print("\nAdjacency Matrix:")

        print("   ", end="")

        for vertex in range(self.vertices):
            print(vertex, end=" ")

        print()

        for index, row in enumerate(self.matrix):
            print(index, row)


def run_program_86() -> None:

    print("\n--- PROGRAM 86: ADJACENCY MATRIX ---")

    vertices = int(input("Enter number of vertices: "))

    graph = AdjacencyMatrixGraph(vertices)

    edge_count = int(input("Enter number of edges: "))

    edges = read_edges(edge_count)

    for source, destination in edges:
        graph.add_edge(source, destination)

    graph.display()

    while True:

        print("\n1. Insert edge")
        print("2. Delete edge")
        print("3. Check edge")
        print("4. Display matrix")
        print("0. Return to main menu")

        choice = int(input("Enter choice: "))

        if choice == 1:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            graph.add_edge(source, destination)

            print("Edge inserted successfully.")

        elif choice == 2:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            graph.remove_edge(source, destination)

            print("Edge deleted successfully.")

        elif choice == 3:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            if graph.has_edge(source, destination):
                print("Edge exists.")
            else:
                print("Edge does not exist.")

        elif choice == 4:

            graph.display()

        elif choice == 0:

            break

        else:

            print("Invalid choice.")


# ============================================================
# PROGRAM 87: GRAPH REPRESENTATION USING ADJACENCY LIST
# ============================================================

class AdjacencyListGraph:
    """
    Represent an undirected graph using adjacency lists.

    Each vertex stores a list of its neighbouring vertices.
    """

    def __init__(self, vertices: int) -> None:

        if vertices <= 0:
            raise ValueError("Number of vertices must be positive.")

        self.adjacency: dict[int, list[int]] = {
            vertex: []
            for vertex in range(vertices)
        }

    def add_edge(self, source: int, destination: int) -> None:

        if source not in self.adjacency:
            raise ValueError("Source vertex does not exist.")

        if destination not in self.adjacency:
            raise ValueError("Destination vertex does not exist.")

        if destination not in self.adjacency[source]:
            self.adjacency[source].append(destination)

        if source not in self.adjacency[destination]:
            self.adjacency[destination].append(source)

    def remove_edge(self, source: int, destination: int) -> None:

        if source not in self.adjacency:
            raise ValueError("Source vertex does not exist.")

        if destination not in self.adjacency:
            raise ValueError("Destination vertex does not exist.")

        if destination in self.adjacency[source]:
            self.adjacency[source].remove(destination)

        if source in self.adjacency[destination]:
            self.adjacency[destination].remove(source)

    def add_vertex(self) -> int:

        new_vertex = (
            max(self.adjacency.keys()) + 1
            if self.adjacency
            else 0
        )

        self.adjacency[new_vertex] = []

        return new_vertex

    def remove_vertex(self, vertex: int) -> None:

        if vertex not in self.adjacency:
            raise ValueError("Vertex does not exist.")

        del self.adjacency[vertex]

        # Remove all references to this vertex.
        for neighbours in self.adjacency.values():

            if vertex in neighbours:
                neighbours.remove(vertex)

    def has_edge(self, source: int, destination: int) -> bool:

        if source not in self.adjacency:
            raise ValueError("Source vertex does not exist.")

        if destination not in self.adjacency:
            raise ValueError("Destination vertex does not exist.")

        return destination in self.adjacency[source]

    def display(self) -> None:

        print("\nAdjacency List:")

        for vertex in sorted(self.adjacency):

            neighbours = sorted(self.adjacency[vertex])

            print(f"{vertex} -> {neighbours}")


def run_program_87() -> None:

    print("\n--- PROGRAM 87: ADJACENCY LIST ---")

    vertices = int(input("Enter number of vertices: "))

    graph = AdjacencyListGraph(vertices)

    edge_count = int(input("Enter number of edges: "))

    edges = read_edges(edge_count)

    for source, destination in edges:
        graph.add_edge(source, destination)

    graph.display()

    while True:

        print("\n1. Insert edge")
        print("2. Delete edge")
        print("3. Add vertex")
        print("4. Remove vertex")
        print("5. Check edge")
        print("6. Display graph")
        print("0. Return to main menu")

        choice = int(input("Enter choice: "))

        if choice == 1:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            graph.add_edge(source, destination)

            print("Edge inserted successfully.")

        elif choice == 2:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            graph.remove_edge(source, destination)

            print("Edge deleted successfully.")

        elif choice == 3:

            vertex = graph.add_vertex()

            print("New vertex created:", vertex)

        elif choice == 4:

            vertex = int(input("Enter vertex to remove: "))

            graph.remove_vertex(vertex)

            print("Vertex removed successfully.")

        elif choice == 5:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            print("Edge exists." if graph.has_edge(
                source, destination
            ) else "Edge does not exist.")

        elif choice == 6:

            graph.display()

        elif choice == 0:

            break

        else:

            print("Invalid choice.")


# ============================================================
# PROGRAM 88: DIRECTED AND UNDIRECTED GRAPH
# ============================================================

class BasicGraph:
    """
    Graph supporting both directed and undirected edges.

    Vertices are stored using an adjacency dictionary.
    """

    def __init__(self, directed: bool) -> None:

        self.directed = directed

        self.adjacency: dict[int, set[int]] = {}

    def add_vertex(self, vertex: int) -> None:

        if vertex in self.adjacency:
            raise ValueError("Vertex already exists.")

        self.adjacency[vertex] = set()

    def remove_vertex(self, vertex: int) -> None:

        if vertex not in self.adjacency:
            raise ValueError("Vertex does not exist.")

        del self.adjacency[vertex]

        for neighbours in self.adjacency.values():
            neighbours.discard(vertex)

    def add_edge(self, source: int, destination: int) -> None:

        if source not in self.adjacency:
            raise ValueError("Source vertex does not exist.")

        if destination not in self.adjacency:
            raise ValueError("Destination vertex does not exist.")

        self.adjacency[source].add(destination)

        if not self.directed:
            self.adjacency[destination].add(source)

    def remove_edge(self, source: int, destination: int) -> None:

        if source not in self.adjacency:
            raise ValueError("Source vertex does not exist.")

        if destination not in self.adjacency:
            raise ValueError("Destination vertex does not exist.")

        self.adjacency[source].discard(destination)

        if not self.directed:
            self.adjacency[destination].discard(source)

    def display(self) -> None:

        graph_type = (
            "Directed Graph"
            if self.directed
            else "Undirected Graph"
        )

        print(f"\n{graph_type}:")

        for vertex in sorted(self.adjacency):

            print(
                f"{vertex} -> {sorted(self.adjacency[vertex])}"
            )


def run_program_88() -> None:

    print("\n--- PROGRAM 88: DIRECTED AND UNDIRECTED GRAPH ---")

    print("1. Directed Graph")
    print("2. Undirected Graph")

    graph_choice = int(input("Choose graph type: "))

    if graph_choice not in (1, 2):
        raise ValueError("Invalid graph type.")

    graph = BasicGraph(directed=(graph_choice == 1))

    vertices = int(input("Enter number of vertices: "))

    if vertices <= 0:
        raise ValueError("Number of vertices must be positive.")

    for vertex in range(vertices):
        graph.add_vertex(vertex)

    edge_count = int(input("Enter number of edges: "))

    edges = read_edges(edge_count)

    for source, destination in edges:
        graph.add_edge(source, destination)

    graph.display()

    while True:

        print("\n1. Add vertex")
        print("2. Remove vertex")
        print("3. Add edge")
        print("4. Remove edge")
        print("5. Display graph")
        print("0. Return to main menu")

        choice = int(input("Enter choice: "))

        if choice == 1:

            vertex = int(input("Enter new vertex value: "))

            graph.add_vertex(vertex)

            print("Vertex added.")

        elif choice == 2:

            vertex = int(input("Enter vertex to remove: "))

            graph.remove_vertex(vertex)

            print("Vertex removed.")

        elif choice == 3:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            graph.add_edge(source, destination)

            print("Edge added.")

        elif choice == 4:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            graph.remove_edge(source, destination)

            print("Edge removed.")

        elif choice == 5:

            graph.display()

        elif choice == 0:

            break

        else:

            print("Invalid choice.")


# ============================================================
# PROGRAM 89: WEIGHTED GRAPH REPRESENTATION
# ============================================================

class WeightedGraph:
    """
    Represent a weighted undirected graph.

    adjacency[source][destination] = weight
    """

    def __init__(self, vertices: int) -> None:

        if vertices <= 0:
            raise ValueError("Number of vertices must be positive.")

        self.adjacency: dict[int, dict[int, int]] = {
            vertex: {}
            for vertex in range(vertices)
        }

    def add_edge(
        self,
        source: int,
        destination: int,
        weight: int
    ) -> None:

        if source not in self.adjacency:
            raise ValueError("Source vertex does not exist.")

        if destination not in self.adjacency:
            raise ValueError("Destination vertex does not exist.")

        self.adjacency[source][destination] = weight
        self.adjacency[destination][source] = weight

    def remove_edge(self, source: int, destination: int) -> None:

        if source not in self.adjacency:
            raise ValueError("Source vertex does not exist.")

        if destination not in self.adjacency:
            raise ValueError("Destination vertex does not exist.")

        self.adjacency[source].pop(destination, None)
        self.adjacency[destination].pop(source, None)

    def get_weight(self, source: int, destination: int) -> Optional[int]:

        if source not in self.adjacency:
            raise ValueError("Source vertex does not exist.")

        if destination not in self.adjacency:
            raise ValueError("Destination vertex does not exist.")

        return self.adjacency[source].get(destination)

    def display(self) -> None:

        print("\nWeighted Adjacency List:")

        for vertex in sorted(self.adjacency):

            print(f"{vertex} -> {self.adjacency[vertex]}")


def run_program_89() -> None:

    print("\n--- PROGRAM 89: WEIGHTED GRAPH ---")

    vertices = int(input("Enter number of vertices: "))

    graph = WeightedGraph(vertices)

    edge_count = int(input("Enter number of edges: "))

    edges = read_edges(edge_count, weighted=True)

    for source, destination, weight in edges:
        graph.add_edge(source, destination, weight)

    graph.display()

    while True:

        print("\n1. Add weighted edge")
        print("2. Remove edge")
        print("3. Retrieve edge weight")
        print("4. Display graph")
        print("0. Return to main menu")

        choice = int(input("Enter choice: "))

        if choice == 1:

            source, destination, weight = map(
                int,
                input("Enter source destination weight: ").split()
            )

            graph.add_edge(source, destination, weight)

            print("Weighted edge added.")

        elif choice == 2:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            graph.remove_edge(source, destination)

            print("Edge removed.")

        elif choice == 3:

            source, destination = map(
                int,
                input("Enter source and destination: ").split()
            )

            weight = graph.get_weight(source, destination)

            if weight is None:
                print("Edge does not exist.")
            else:
                print("Edge weight:", weight)

        elif choice == 4:

            graph.display()

        elif choice == 0:

            break

        else:

            print("Invalid choice.")


# ============================================================
# PROGRAM 90: GRAPH DEGREE CALCULATION
# ============================================================

def calculate_undirected_degrees(
    vertices: int,
    edges: list[tuple[int, ...]]
) -> dict[int, int]:
    """
    Calculate degree of every vertex in an undirected graph.

    A self-loop contributes 2 to the degree.
    """

    degrees: dict[int, int] = {
        vertex: 0
        for vertex in range(vertices)
    }

    for edge in edges:

        source = edge[0]
        destination = edge[1]

        validate_vertex(source, vertices)
        validate_vertex(destination, vertices)

        if source == destination:
            degrees[source] += 2
        else:
            degrees[source] += 1
            degrees[destination] += 1

    return degrees


def calculate_directed_degrees(
    vertices: int,
    edges: list[tuple[int, ...]]
) -> tuple[dict[int, int], dict[int, int]]:
    """
    Calculate indegree and outdegree of every vertex.

    Outdegree = Number of outgoing edges.
    Indegree = Number of incoming edges.

    A directed self-loop contributes one to each.
    """

    indegree: dict[int, int] = {
        vertex: 0
        for vertex in range(vertices)
    }

    outdegree: dict[int, int] = {
        vertex: 0
        for vertex in range(vertices)
    }

    for edge in edges:

        source = edge[0]
        destination = edge[1]

        validate_vertex(source, vertices)
        validate_vertex(destination, vertices)

        outdegree[source] += 1
        indegree[destination] += 1

    return indegree, outdegree


def run_program_90() -> None:

    print("\n--- PROGRAM 90: GRAPH DEGREE CALCULATION ---")

    print("1. Undirected Graph")
    print("2. Directed Graph")

    choice = int(input("Choose graph type: "))

    if choice not in (1, 2):
        raise ValueError("Invalid graph type.")

    vertices = int(input("Enter number of vertices: "))

    if vertices <= 0:
        raise ValueError("Number of vertices must be positive.")

    edge_count = int(input("Enter number of edges: "))

    edges = read_edges(edge_count)

    if choice == 1:

        degrees = calculate_undirected_degrees(
            vertices,
            edges
        )

        print("\nVertex Degrees:")

        for vertex in range(vertices):
            print(
                f"Vertex {vertex}: Degree = {degrees[vertex]}"
            )

        print(
            "Sum of degrees:",
            sum(degrees.values())
        )

    else:

        indegree, outdegree = calculate_directed_degrees(
            vertices,
            edges
        )

        print("\nDirected Graph Degrees:")

        for vertex in range(vertices):

            print(
                f"Vertex {vertex}: "
                f"Indegree = {indegree[vertex]}, "
                f"Outdegree = {outdegree[vertex]}"
            )

        print("Total indegree:", sum(indegree.values()))
        print("Total outdegree:", sum(outdegree.values()))


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all_programs() -> None:

    print("\n========== RUNNING ALL DAY 18 PROGRAMS ==========")

    run_program_86()

    run_program_87()

    run_program_88()

    run_program_89()

    run_program_90()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    while True:

        print("\n==============================================")
        print("       MONTH 11 - DAY 18 DSA MENU")
        print("       GRAPH FUNDAMENTALS")
        print("==============================================")

        print("86. Graph Using Adjacency Matrix")
        print("87. Graph Using Adjacency List")
        print("88. Directed and Undirected Graph")
        print("89. Weighted Graph Representation")
        print("90. Graph Degree Calculation")
        print("91. Run All Programs")
        print("0. Exit")

        print("==============================================")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 86:
                run_program_86()

            elif choice == 87:
                run_program_87()

            elif choice == 88:
                run_program_88()

            elif choice == 89:
                run_program_89()

            elif choice == 90:
                run_program_90()

            elif choice == 91:
                run_all_programs()

            elif choice == 0:

                print(
                    "Exiting Day 18 DSA Programs. Keep practicing!"
                )

                break

            else:

                print("Invalid choice. Please select 0-91.")

        except ValueError as error:

            print("Input error:", error)

        except Exception as error:

            print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()
